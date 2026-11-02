>>> HOW TO RUN THIS <<<
This is the digest prompt for ciscolive-us-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ciscolive-us-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ciscolive-us-2025.md
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

Below is the program for Cisco Live US 2025 (San Diego) (vendor). Read it and produce a digest
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
conference: Cisco Live US 2025 (San Diego)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1748366287882001oJzH
generated: 2026-11-02
registry_key: ciscolive-us-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## 2025 San Diego

### AIOPS for Cisco Secure Firewall: Enhancing Operational Efficiency and Security - BRKSEC-2883
Speakers: Gayathri Nagarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272004284001zTkP
In today's rapidly evolving digital landscape, managing firewalls has become a critical yet complex challenge for IT and security teams. As network complexity and cyber threats increase, effective firewall management is crucial for maintaining robust security postures and operational efficiency. This session unveils the strategic vision behind AIOps for Cisco Secure Firewall, offering proactive insights and recommendations that transform firewall management. By leveraging AIOps, organizations can significantly reduce downtime, minimize misconfigurations, and lower operational costs. Imagine efficiently creating and managing rules, swiftly addressing traffic monitoring needs, and drastically reducing downtime from hours to minutes.

### Catalyst Switching enabled Smart Buildings : Beyond PoE Connectivity - BRKENS-2603
Speakers: Veera Bhaskar Mutyala (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271920882001zNQT
Ride-hailing services altered the perception of a car from a basic commuter to a potential source of revenue by allowing car owners to monetize their vehicles through apps; in a similar vein, 90-watt Power over Ethernet with 10 Gigabit speeds on standard category cable is transforming the campus Ethernet from a simple data connection medium into an intelligent last-mile power delivery engine capable of advanced management and analytics and better ROI. This session will explore the capabilities of Catalyst and Cisco switches in campus networks, going beyond basic PoE connectivity to cover the latest innovations on our Campus switch platforms, such as Energy Management with Catalyst Center, smart power management policies, and IOT app-hosting." By the end of this session, you will have a deeper understanding of PoE technology, enabling you to leverage its cost-saving benefits through reduced cabling and increased workspace flexibility. Finally, we will explore how smart buildings achieve sustainability via energy efficiency and resource optimization, featuring real-world deployments and Cisco partner solutions for future-proofed workspaces like sensor-equipped smart desks, CDP-integrated smart building devices, and the possibilities of FMP-enabled DC microgrids."

### Cracking the Code to IT Resilience: Real-Time Insights, Real Business Impact - ITLGEN-2071
Speakers: Kevin LeBlanc (Cisco), Jon Moore (Progressive Casualty Insurance Company.), Mark Kennison (Global Payments)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271958208001zhTi
In Today's fast-moving, complex IT environments, the real challenge isn't just figuring out what's broken—it's knowing which problems matter most to your business and bottom line. Join us to learn how new integrations, like the two-way connection between Splunk ITSI and Cisco ThousandEyes, and Splunk Observability Cloud with AppDynamics, are delivering real-time, AI-powered insights that help you prioritize, act faster, simplify the chaos and reduce downtime. This session features a live demo and a candid on-stage conversation with a customer, who will share their own journey and lessons learned. With actionable insights, bold predictions about the future of AI in IT operations, and a live Q&A, you'll walk away with fresh ideas to drive resilience, collaboration, and measurable value for your organization. Don't miss this chance to transform how you lead in the face of IT complexity.

### End User Experience + NMS = Auvik FTW! - VILNWT-2000
Speakers: Steve Petryschuk (Auvik)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271972180001zDER
User satisfaction was ranked the most important success metric for IT teams in Auvik's IT Trends 2025 Report, with 48% of respondents indicating that customer and end user experience is their team's primary success metric. So how do your existing network management tools stack up in addressing user satisfaction? Sure, they can handle the network management basics - latency alerting, packet loss tracking, netflow, etc - but how are they really supporting your success if success is tied to user satisfaction and user experience? With Auvik, you gain the power to spot and fix issues before they have a chance to disrupt productivity or satisfaction. Building on a foundation of critical NMS capabilities and differentiating with end-user visibility into any user, on any network, Auvik's toolset will help you modernize the management of your mid-size network. Ditch the legacy network management systems and get ahead with Auvik. Come see for yourself how easy it is to switch.

### From Agents to Ecosystems: Why Cisco is Building the Internet of Agents - AIHUB-1950
Speakers: Papi Menon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271925938001z8aU
In 1984, Cisco built routers that helped create the Internet. Forty years later, we're facing a similar inflection point with AI agents that can't effectively communicate with each other. The real power of AI won't come from isolated agents but from their ability to collaborate across your enterprise - yet most organizations are building digital silos that will limit their potential. In this session, we'll reveal: The three architectural patterns for connecting agents (deterministic, semantically-routed, and planner-based) and when to use each in your environment How the open-source AGNTCY collective is creating standardized protocols that solve the agent interoperability challenge Real examples of how multi-agent workflows are transforming IT operations, security response, and customer support This is the infrastructure conversation you need to have now, not next year. Just as TCP/IP became the foundation of modern networking, agent interoperability protocols will determine which AI investments succeed and which become technical debt. Perfect for IT leaders and practitioners building AI-ready data centers and resilient digital operations. No specialized AI knowledge needed - just the foresight to prepare your infrastructure for the next evolution of enterprise computing.

### SAN Congestion Management and SAN Analytics - BRKDCN-2942
Speakers: Ed Mazurek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889597001zcDC
Demand for storage is growing at an unprecedented pace. At the same time, the demand for high performance is driving an increased need to understand and detect issues before they become a problem. This session covers the most common issues observed in modern Storage Area Networks (SANs) and introduces the latest Cisco innovations to help you detect, identify, and most importantly, prevent congestion from happening. Furthermore, you will learn how to utilize the latest innovations with MDS switches, SAN Analytics, and Nexus Dashboard SAN Insights to answer the toughest questions SAN administrators face today, such as how to identify the root cause of performance issues, pinpoint the source of link over-utilization, and predict congestion before it ever occurs.

### Webex Troubleshooting Superpowers with ThousandEyes and Meraki Integrations - BRKCOL-2662
Speakers: Paul Giralt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271854343001zS5R
Cisco Webex Control Hub offers valuable insights into media quality issues, but understanding the underlying cause of these issues can be elusive. ThousandEyes and Meraki Dashboard, providing unrivaled network-level visibility, but until now, have not had an easy way to correlate network events with media quality events. By seamlessly integrating Webex with ThousandEyes and Meraki Dashboard, you gain unparalleled visibility into your Webex traffic, empowering you to swiftly identify and resolve any challenges that arise. Join us for an enlightening session as we delve into the art of media quality troubleshooting within Webex Control Hub. Discover how the integration of ThousandEyes and Meraki Dashboard elevates your troubleshooting capabilities by incorporating additional telemetry into Control Hub. With real-world examples, we will showcase how these integrations can effectively help diagnose and address real-world issues.

### Why Cisco Secure WAF/WAAP is Essential for Safeguarding Exposed Applications and APIs - BRKSEC-1039
Speakers: Virg Santos (Radware - Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271997980001zriz
In today's digital landscape, web and API vulnerabilities are prime targets for cyberattacks. This session dives into the critical OWASP Top 10 threats that can compromise your applications and APIs, exploring how Cisco Secure Web Application Firewall (WAF) and API Protection play a pivotal role in proactively detecting and mitigating these risks. We will walk through examples of these common threats and discuss why it's important to dynamically block them to ensure the security of your applications and APIs.

### 1 to 100: Master All Steps of Automated and Seamless Deployment, Integration, and Migration of Large SDA and SD-WAN Networks - BRKENS-3834
Speakers: Jennifer Bowman (Cisco), Dhrumil Prajapati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271925157001zYr1
Do you know what it takes to plan and migrate a site of any size to Cisco SD-Access and SD-WAN network at scale? How about automating entire migration of both solutions? This session explains just that. We will cover every bit of detail involving how to deploy, seamlessly integrate, and migrate SD-Access and SD-WAN networks at scale with automation in large enterprise networks. This session will demonstrate the key fundamentals in designing, deploying, and operating a software-driven network at scale. Key concepts include creating modules and prescriptive handoffs, transport considerations, security, migrating the brownfield environment from circuits to change controls, and how automation will bring you scale. In the end, you will walk away with a comprehensive plan to start your SDA and SD-WAN journey.

### 1 to 50 proven steps in building effective end-to-end automation strategy for multi-domain networks - BRKXAR-2033
Speakers: Dhrumil Prajapati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271868893001ziB5
In today's complex IT landscape, organizations face the challenge of managing multiple network domains, including data centers, WAN/LAN, security, and cloud environments. This session will explore how IT architects and leaders can implement a cohesive automation strategy to seamlessly integrate these domains, enhancing organizational efficiency and effectiveness. We will take a deep dive into proven customer use cases, outlining the key steps and strategies necessary for such— environments through an orchestration and CI/CD pipeline. Join us to discover how to transform your network management approach and drive innovation across your organization.

### 10X digital resilience results with a unified data + AI approach - PSOOBS-1114
Speakers: Julie Gibbs (Cisco), Sonal Pardeshi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977205001zxqR
Uncover how a unified data+AI strategy can boost digital resilience tenfold. This session highlights Splunk's AI strategy, using agentic AI to automate observability and security tasks like root cause analysis and threat hunting. Learn how Cisco and Splunk combine data-driven insights across networking, monitoring, and security, streamlines SOC/NOC workflows. Gain practical knowledge to leverage autonomous AI, fortifying defenses and optimizing performance to meet business objectives with confidence.

### 123 URWB: A Wireless Network Engineer's Guide - BRKIOT-2027
Speakers: DJ Cole (Cisco), Alice Masini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271954154001zCY6
Bring reliability beyond the Wi-Fi boundaries with Cisco Ultra-Reliable Wireless Backhaul (URWB) technology. This technology has proven its value as a solution for wireless connectivity for mission-critical applications. In this session, we will explore the latest Cisco annoucements regarding URWB innovations within the Cisco Wireless portfolio and attendees will learn how to leverage on URWB and Wi-Fi across the Cisco Wireless ecosystem to boost operational efficiency and productivity. Attendees will understand the architecture, the implementation, and the capabilities the Cisco Wireless Solution can provide together with an overview of the major use cases and verticals where the integrated solution becomes game changer for productivity and efficiency.

### 3 Design Principles to Solving WAN Challenges - BRKENT-2794
Speakers: Jeffry Handal (Cisco), Prashant Tripathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271932424001zF4W
Connectivity is the foundation from which we build the digital world. Paired with Cisco's Secure Router platforms, we now have a transformative approach to driving your digital transformation journey; paving the way to consuming the new forms of WAN connectivity the market has to offer. The presentation will explore key architectural components and design principles underpinning Cisco Secure Router platforms, highlighting their ability to seamlessly integrate cloud-managed and on-premise deployments. Additionally, the presentation will cover the building blocks to achieve secure and assured connectivity for efficient network operations and improved user experiences.

### 4 Ways to Streamline Your Licensing with Cisco's Networking Subscription Across Your Portfolio - BRKXAR-1013
Speakers: Juan Rodriguez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271867761001zSuJ
Has navigating Catalyst Center and Meraki licensing been a challenge for you? Cisco's evolving licensing models bring flexibility and scalability to network operations, but navigating Catalyst Center and Meraki licensing can be complex. This session breaks it down, providing a clear understanding of how these two distinct experiences come together under a unified licensing approach. We'll explore the differences between Catalyst Center (CSSM) and Meraki Dashboard licensing, how to transition traditional licensing to Cisco Networking Subscription, and strategies for consolidating networking licenses into a single subscription model. Learn how unified licensing work and dispelling myths and clarifying Functions across platforms. Additionally, We'll cover new Unified licensing, for Wi-Fi7, switching and routing and how it fits into the evolving licensing framework. Walk away with best practices to simplify license management, ensure compliance, and optimize your network licensing strategy.

### 400G, 800G, and Terabit Pluggable Optics: What You Need to Know - BRKOPT-2699
Speakers: Mark Nowell (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967757001zfoK
Optical interfaces are fundamental in our networks, and the technology is always being pushed to higher speeds. New developments happening in this space will enable the next generation of higher-capacity networks. This session will provide participants with insights into the current trends and the next development areas for high-speed optical interconnects, what is driving the development, and what the priorities are for success. The session will focus on these following areas: Industry dynamics, AI impacts Current 400G pluggable optics technologies and their applications Next-generation pluggable form factors for 800G and 1.6T (including their breakout use cases) New 800 Gb/s and 1.6 Tb/s Ethernet standardization Next-generation optical co-packaging developments for integrating optical interfaces into ASICs The session will cover both coherent and noncoherent optics and will target participants with a working knowledge of deploying optical interfaces and modules. Finally, we will also highlight some of the implications to the systems and networks that incorporate these optical interfaces.

### 5 Tools You Should Learn to Level Up Your Network Automation Game - BRKDEV-2149
Speakers: Quinn Snyder (Cisco), Kareem Iskander (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271911234001zWV8
So, you're on the journey to becoming a DevNet Expert, huh? You've got the lowdown on Python and APIs for network wizardry. But now, it's time to kick it up a notch and dive into some real-deal industry tricks to boost your automation mojo. Meet Kareem and Quinn, two jabronis who've done it all from network engineering to software development. Hang out with these two cool cats as they spill the beans on the top 5 gotta-know tools to rock your way to becoming a DevNet automation guru!

### 5 new things you need to know about Catalyst Center licensing - BRKOPS-2835
Speakers: Gayathri Devi Viswanathan Nagendran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271987218001zR8D
Ever wondered what licenses you need to deploy Catalyst Center for your Enterprise Campus? Not sure of Essentials or Advantage - we got you covered. Can't distinguish between supported and limited visibility or overwhelmed with managing licenses? - don't worry, we still have you covered. This session breaks down every component of Catalyst Center licensing for you - from appliance to devices, subscriptions to support and better yet, simplified license management. We will uncover the value of unified Catalyst licensing for operational simplicity. You will learn about the licensing policy for legacy cisco devices and 3rd party devices, discuss the recent policy changes with Catalyst Center licensing and learn ways of managing smart licenses using Catalyst Center License Manager. We will demonstrate: 1. What if scenarios when using different IOS version between different license modes 2. Managing legacy (LDoS) & 3rd party devices in Catalyst Center 3. Managing smart licenses and SLuP licenses using License Manager 4. Monitoring unified Catalyst licenses using License Manager 5. License compliance reports

### 7 Steps: Master the art of unifying Multicloud secure Connectivity and Design - Cisco SD-WAN + Multicloud Defense - BRKENT-2283
Speakers: John Clark (Cisco), Prashant Tripathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933986001zdHq
Cisco SD-WAN seamlessly orchestrates connectivity, enabling access to workloads across multiple clouds. Through native integration with leading cloud service providers like AWS, Azure, and Google Cloud, as well as middle-mile providers such as Megaport and Equinix, it ensures secure inter-site/inter-region connectivity. The solution integrates with AWS Cloud WAN, leveraging Transit Gateway architecture, collaborates with Google NCC for Google Cloud connectivity, and utilizes Azure's vWAN and vHUBs. Inter-cloud SD-WAN connectivity between diverse cloud providers is facilitated by SD-WAN Gateways. With the powerful addition of Multicloud Defense, the solution delivers comprehensive security, unifying policies across AWS, Azure, and Google Cloud for on-demand protection of workloads and inter-cloud traffic. This paves the way for converged multi-cloud networking and security

### A Day in the Life of an AI-enabled Software Developer - ITLGEN-2057
Speakers: Stephen Byrnes (Cisco), Richard Delisser (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271957058001z32h
In this session we will step into a future day-in-the-life of a software engineer to explore the transformative impact of AI on the developer experience. From coding to debugging, this session will cover the use of integrated tools such as GitHub Copilot, chatbots, Splunk, and more. Experience live demonstrations and best practices for integrating AI into your development environment, and see how embracing these technologies can amplify productivity, reduce cognitive load, and free up time for innovation. Join us as we reimagine what's possible in the world of AI-enabled development.

### A Developer's Introduction to Splunk Observability Cloud - DEVNET-2366
Speakers: Greg Leffler (Splunk), Wayne Brown (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904993001zK7n
Observability offers a lot of benefits - faster MTTD, better understanding of your architecture, and the ability to find root causes faster, but getting started can be tough - and understanding exactly what observability tools can do for you can be even harder. In this session, you'll learn how to instrument applications to send data into Splunk Observability Cloud with zero code changes. Starting with an overview of observability in general, next, you'll see a demo of our automatic OpenTelemetry instrumentation for a Java app. Finally, you'll see a troubleshooting workflow in Splunk Observability Cloud, highlighting the use of Splunk APM and Splunk Log Observer Connect to quickly isolate a problem to the root cause.

### A Fireside Chat with Network Engineers about AI - CISCOU-1055
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271839694001zlwf
Gather round the warm fire, bring a drink, maybe a security cable, and let's talk the good, the bad, and the ugly about AI and work as a network engineer today. What are some fantastic ways AI can make our jobs easier that we should all know about? Share a story about how AI has made your job tougher? What does it mean to actually build a network for AI to run on? What should we be learning today to make ourselves valuable tomorrow? These are just some of the kinds of questions that will be asked in this open discussion with a group of network engineers, just like you...

### A Future Proof Workforce in Healthcare, powered by Jamf, Apple, and Cisco Private 5G - VILENT-1004
Speakers: Tim Knox (Jamf), Sam Weiss (Jamf), David Cote (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271925747001zfSI
In healthcare, every moment matters. Reliable connectivity in this environment is critical. Join this session to explore how the combination of Cisco Private 5G, Apple, and Jamf's Apple-first management and security platform can deliver fifteen bars of connectivity, transforming mobility in healthcare environments. We'll explore the technologies that enhance performance, data protection, and reliability helping healthcare IT deliver business outcomes from faster and more secure clinical and research workflows and more immersive meeting environments. Join us to explore technical architectures, real-world use cases, and how to enable consistent, secure, and scalable mobility workflows - without compromising the Apple experience clinicians trust every day.

### A Network Engineer's Blueprint for ACI Forwarding - BRKDCN-3900
Speakers: Joseph Young (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892454001z21h
As the Cisco Application Centric Infrastructure (ACI) list of features continues to expand and encompass more data center architectures, it is more important than ever to have a good understanding of how a packet is forwarded end to end. This session will provide a deep dive into how ACI forwards traffic. Important questions that will be covered include: How do the basic forwarding mechanisms in ACI work (VXLAN, TEP reachability, end point learning, etc.)? In what ways does ACI forwarding differ from legacy environments? What do the forwarding-related configuration options do? How can an engineer effectively prove what is happening to a packet? At the end of this session attendees should be able to explain in detail how ACI would handle a specific flow as well as use available tools to debug and verify what is happening. Attendees should already have a deep understanding of routing and switching fundamentals in legacy environments and knowledge of basic ACI constructs (endpoint groups, contracts, bridge domains, VRFs).

### A New Approach to Digital Resilience: Get Ahead of Issues and Minimize Business Impact - KDDOBS-1000
Speakers: Kevin LeBlanc (Cisco), Raja Mukhopadhyay (Cisco), Michael Bryan (Honeywell)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591954036001pdJm
In today's complex digital environments, maintaining flawless security and system performance is nearly impossible. This session delves into the world of digital resilience—how organizations can manage multiple issues strategically to minimize disruption, prioritizing them based on their impact to customers and the bottom line. We'll dedicate substantial time to the latest Splunk Observability innovations, and you'll hear from customers about how their teams leverage comprehensive data integrations, advanced analytics and AI to make triage decisions based on how an issue impacts the business, instead of fighting every problem with equal urgency.

### A New Era of Cross-domain Diagnostics with AI and Agentic Systems - BRKETI-2172
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915469001z2b2
This session delves into the realm of troubleshooting and explores future potentials, asking: Can AI diagnose problems like a human and assist with complex, cross-domain troubleshooting tasks? This exploration will proceed through three incremental steps: analyzing logs with Large Language Models (LLMs), analyzing streaming router telemetry with AI, and employing an agentic AI approach to diagnose complex, cross-domain/cross-vendor deployments involving applications, middleware, servers, and networks. Note: This session is an extended version of AIHUB-2006 - "Applying AI/ML Methods to Diagnose Network Issues Using Telemetry Data"

### ACI Layer 4-7 Policy-Based Redirect (PBR) Deep Dive and Tips - BRKDCN-3982
Speakers: Minako Higuchi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893209001zLLo
When designing network security in a data center, have you ever wondered where to enforce security policies and how to steer traffic to get firewalls to inspect the traffic? How would the use of Cisco ACI affect your Layer 4-7 services such as firewalls, IPSs, and load balancers? This session will provide a deep dive into ACI Layer 4-7 service integration capabilities, especially PBR service graphs. It will cover ACI contract security capabilities, how forwarding works to steer traffic, design options with common use cases, and multi-location data center design options. The basic assumption is that participants will have a solid knowledge of Cisco ACI and its functional components, including EPGs, contracts, VRF, bridge domains, Multi-Pod, Multi-Site, etc.

### ACI Multi-Site Architecture and Deployment - BRKDCN-2980
Speakers: John Weston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271891703001z0hT
The need to deploy ACI in multiple data center sites to provide redundancy is a common requirement for both enterprise and service providers. This session introduces the application, operation, and availability considerations for Cisco ACI multi-site and covers multiple aspect of the architecture, including an introduction and positioning between multi-pod and multi-site architectures, inter-site network (ISN) deployment considerations, ACI Nexus Dashboard Orchestrator (NDO, formerly MSO) architecture and deployment, ACI multi-site control and data plane, connecting to the external layer 3 domain, and network services integration. The expectation is that attendees already have at least a basic understanding of ACI in order to get the best out of this session.

### ACI Objects: How to Avoid Getting Your Configuration Wires Crossed - BRKDCN-2647
Speakers: Davis Creemer (Cisco), Chris Merkel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885609001zGZa
This session is designed for engineers and architects who spend time designing and implementing ACI-based solutions. With a focus on best-practice and scalability, we will review common design challenges and how to avoid them. The ACI object model provides a powerful way to set policy once and reuse it as needed, but knowing how to use these objects can be challenging. It can also be easy to find yourself in an endless configuration sprawl. From the AAEP and pDom to the EPG and the layer 3 out, we will talk about many of the commonly used objects, their relationships, their purposes, and how to optimally reuse them for truly scalable solutions. Attendees should have a general understanding of ACI and some familiarity with its common objects.

### ACI Troubleshooting: A Deep Dive into PBR - BRKDCN-3615
Speakers: Michael Garcia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271886937001zPPd
This session will delve into troubleshooting policy-based redirect (PBR), offering insights from a network engineer's standpoint, and will examine typical PBR scenarios deployed in ACI environments. By utilizing layer 4/layer 7 services within ACI, we can automate integration while also simplifying configurations. ACI's PBR functionality enables us to direct traffic toward service devices, facilitating thorough packet inspection. Given the growing demand for transparent services like firewalls and load balancers in modern setups, it's crucial to grasp the workings of PBR.

### ACI Troubleshooting: Advanced Layer 3 Out Features - BRKDCN-3678
Speakers: Jessica Rueda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271887325001z377
A Layer 3 Out (L3Out) in Cisco ACI controls the external connectivity toward the fabric. In this session, we will build on top of earlier Cisco Live Layer 3 Out sessions and dive deep into features such as route control and transit routing. We will cover this from both a single-pod and multi-pod perspective and explore troubleshooting, best practices, and inner workings.

### ACI Troubleshooting: Expand Your Tool Set with Nexus Dashboard Insights - BRKDCN-2626
Speakers: Ivan Kovacevic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884262001ztIJ
Attend this session to learn how to troubleshoot your ACI fabric through NDI's Day 2 ops capabilities. We will demonstrate how these tools fit into your troubleshooting tool belt and show through practical examples how you can use them on a daily basis. Tired of spending hours and hours on troubleshooting? We're looking forward to meeting you and showing you a different way.

### ACI Troubleshooting: Optimize Your APIC User Experience through API Mastery - BRKDCN-2635
Speakers: Gabriel Monroy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884844001zeeW
All configuration interactions with an application-centric infrastructure (ACI) fabric begin with an API call. Every day brings new integrations and monitoring tools, which take advantage of the APIC's single-northbound API. It is imperative to understand that APIC performance has a direct correlation to API request handling, and to have a methodology to isolate issues related to both. You will leave this session having learned how the API relies on APIC subsystems, which features are available to optimize and protect the API, and how to isolate and troubleshoot APIC and API performance issues.

### AI Agents 101: An Introduction to Agents and Examples of How to Build Them - BRKETI-1008
Speakers: Tim Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916048001ziug
When Generative AI burst on the scene three years ago, the world was abuzz with the technology's natural language processing capabilities. Since its introduction, the industry has now seen three major transitions in GenAI architectures: chatbots with prompt engineering, AI assistants enhanced with RAG, and now AI agents. The speed of innovation in this space is FAST and understanding the terminology and architectural differences has become a barrier to adoption. This session will demystify agents by introducing the key criteria for agents, the levels of agentic AI autonomy, and popular frameworks for building agents. Attendees will see specific code examples of these frameworks, demonstrating levels of autonomy. Relevant Responsible AI (RAI) concerns regarding autonomy will be discussed. To conclude the session, potential emerging technologies in agentic AI will be highlighted. Knowledge of a programming language like Python and Gen AI concepts will greatly enhance the attendee's experience.

### AI Agents and Agentic Frameworks: An Overview - AIHUB-2170
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271913355001zqk1
Agentic AI represents a significant advancement in artificial intelligence (AI), characterized by its enhanced autonomy, decision-making capabilities, and adaptability, which could lead to transformative developments. Unlike conventional AI systems that are rigidly programmed for specific tasks, agentic AI can understand and interpret complex and nuanced context and goals, allowing for more sophisticated interactions and decision-making processes. AI agent teams have shown proficiency and results that exceed those of even the most sophisticated Large Language Models (LLMs) in single-query situations. This session delves into the principal innovations and core principles that underpin Agentic AI, drawing on examples from current frameworks such as LangGraph, Autogen, Semantic Kernel and Swarms. It evaluates trends in multi-agent distributed systems and the evolving dynamics of human-AI cooperation. The session concludes by assessing open challenges and future directions in agentic AI.

### AI Agents with Cisco and Splunk - AIHUB-2494
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271975270001zbTc
AI-enabled agents are the talk of the industry and can serve as the basis to address many important customer issues around network, application visibility, security and control. But which agents and which capabilities to use to address which set of issues? Come to this fast-paced, fun AI Hub session to dive into the world of AI agents available from both Cisco and Splunk, showcasing key capabilities and highlighting how they can be used to address real-world use cases. Presenting this session are Errol Roberts and Dave Zacks, both Cisco Distinguished Engineers as well as Cisco Live Distinguished Speakers and AI enthusiasts. Come to this exciting and engaging session to see the latest AI agents and tools from Splunk and Cisco in action!

### AI Changes Everything: A New Blueprint for Network Security, Zero Trust, and the SOC - KDDSEC-1000
Speakers: Tom Gillis (Cisco), Mike Horn (Cisco), Peter Bailey (Cisco), Shawn Clark (Cleveland Clinic Foundation)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591952508001pGUf
Cisco shines where security meets the network. Backed by decades of experience in networking and security—and now powered by AI—we're delivering the most significant security innovations in our 40-year history. Join Tom Gillis, SVP & General Manager, Infrastructure & Security Group at Cisco and Mike Horn, SVP & General Manager, Splunk Security Products, to get a deeper look at smarter, more effective security solutions. You will get the inside scoop on how Cisco is securing the hybrid workforce against identity-based threats, enabling safe AI adoption, disrupting the firewall landscape, and—together with Splunk—transforming security analytics and response. You'll also hear directly from a Cisco customer sharing how these innovations are transforming their security strategy and delivering real-world results.

### AI Driven Operations and Self-Healing Cisco Secure Access - BRKSEC-2772
Speakers: Esra Dumanli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003312001zbVB
In this session, we will explore how to leverage artificial intelligence in transforming day 2 operations for Cisco Secure Access. Discover how AI-driven automation enhances operational efficiency, proactively detects and resolves issues, and enables self-healing capabilities to ensure seamless and secure connectivity. Through real-world digital experience monitoring and troubleshooting use cases, we will show how combination of traditional telemetry and synthetic data can generate insights into intelligent, resilient and adaptive framework. Attendees will learn about the latest advancements that empower secure access, ensuring resilient and reliable services. The session will highlight use cases demonstrating AI's role in transforming traditional network management into a more agile, intelligent, and secure framework, ultimately improving user experience and operational agility.

### AI Infra for the Rest of Us - BRKDCN-2677
Speakers: Shelly Cadora (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271886750001zxxv
The dazzling speed and scale of shiny new AI factories can sometimes overshadow a simple truth: cloud-based AI is not for everyone. If your AI use case requires enhanced data security, regulatory compliance, lower latencies or just better economics, then an on-prem AI cluster might be the better answer. But building and operating your own cluster can be daunting. How do you build a lossless Ethernet fabric? Do you need GPUs, CPUs, DPUs or all three? What kind of storage maximizes performance? And how do you connect it all together? In this session, we will show how Nexus Hyperfabric for AI meets the challenge, delivering a simple-to-operate (really!) AI cluster, complete with compute, storage and networking for your on-prem use cases. Hyperfabric for AI handles the whole process, from design to ordering, to deployment to maintenance, and operations, so you can focus on your AI apps, not your infrastructure.

### AI Infrastructure Choices for the Agentic Era - PSOMSI-1003
Speakers: Jonathan Gilad (Cisco), Sree Chadalavada (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271960576001zHyJ
As GenAI adoption increases rapidly, agentic AI introduces a world where connected AI agents and people collaborate to orchestrate complex workflows. See how Cisco data center and WAN portfolios help you deliver these AI outcomes across mass-scale, large, and edge environments. Explore the infrastructure that powers LLMs, inferencing, and agentic AI, and how Cisco silicon, Ethernet, optics, compute, data center interconnect, and security innovations deliver performance and scale to support the complete AI lifecycle in — and between — data centers.

### AI Outcomes with Knowledge Automation Bot - VILCCT-1013
Speakers: Tom Golino (Verint)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271863105001zlb7
Realize AI outcomes from your existing enterprise content in days – not weeks or months – without the need for content migration with the Knowledge Automation Bot. Provide agents with the right answer at the right time, without the need for searching across multiple content repositories and use Generative AI to summarize knowledge search results, to make answers easy for agents to consume.

### AI Policy: Global Implications and Regulatory Shifts - PP-1311
Speakers: Jeff Campbell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271948061001zdZH
With the U.S. signaling a light-touch approach to AI regulation, the impact on global policy frameworks could be significant. As AI continues to transform industries and societies, governments are weighing how to balance innovation with oversight, and the U.S. stance could set the tone for regulatory approaches in other regions. In this session, you'll gain insight into how U.S. decisions may shape global AI regulation and Cisco's role in guiding the future of AI policy.

### AI Transformation Done Right: Strategies for Success in Customer Experience - CNCETI-1001
Speakers: Kamesh Akundi (Infosys Limited)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912772001zj5O
How can we harness AI technology to create customer experiences that are more seamless, empowering, and human? This session will deliver a research-driven blueprint for five game-changing AI opportunities, supported by real-world examples. It will also debunk common myths, reveal overlooked opportunities, and equip you with the insights needed to implement AI effectively — ultimately driving success in customer experience.

### AI Unpacked: Transforming Digital Collaboration with Webex - BRKCOL-2069
Speakers: Omer Ilyas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271852446001zJYW
In this session, We'll demystify AI, exploring how technologies like machine learning and Large Language Models (LLMs) can transform digital interactions. We'll focus on integrating these advancements with the Webex API, LangChain to create systems that respond to natural language, enhancing communication efficiency and user experience. Covering technical basics, architecture, and practical solutions, this session will offer insights for developers, IT professionals, and AI enthusiasts alike. A live demo will showcase how AI can revolutionize digital communication, equipping attendees with knowledge to implement these innovations in their own projects.

### AI Wireless Operation - when AI meets Cisco Meraki Wireless - BRKEWN-2039
Speakers: Minse Kim (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271940239001zGZ2
We are living in a world where tech is synonymous to the AI. like MSG, everything seems to get more savory with AI. But can AI solve my latest challenges such as 6GHz, WPA3 and plethora of new devices and ever hiking expectations? This session provides the answers to the network operators who are seeking pragmatic examples and workflows of how to use the latest AI technologies in the Cisco Meraki wireless management to accelerate and assist your wireless deployment, operation and troubleshooting using AI. #GenAI #AI-RRM #chatbot #packetcapture #CUI

### AI and Advanced Automation for Seamless Network Migration - PSOMSI-1004
Speakers: Saumya Dubey (Cisco), Kerri Hale (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271960763001zr1I
This session explores how AI/ ML can streamline network migration with insights from Cisco automation tools and innovations. We'll showcase real world customer stories through strategic planning, product selection, and implementation. Learn how to optimize for cost savings and operational efficiencies, leveraging predictive forecasting, model training, and evaluation. Your roadmap to embed AI-driven automation and build cost-effective, optimized infrastructure is here.

### AI at Scale: How Cisco, NVIDIA, and WWT are Powering the Future of Enterprise AI - CNCETI-1000
Speakers: Neil Anderson (World Wide Technology, Inc)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271913738001zpNl
This session will focus on the innovation between Cisco, NVIDIA, and WWT to bring scaled AI solutions to market for Enterprise clients. We will discuss: Why WWT for AI? How WWT is accelerating the Cisco/Nvidia partnership Innovation in WWT's AI proving ground labs What it means for customers

### AI at Scale: Infrastructure, Insight, and the Role of IT Leadership - ITLGEN-2067
Speakers: Chris Marriott (NVIDIA), Jeremy Foster (Cisco), Jose Marie Griffiths (Dakota State University)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271957830001zXPB
AI is redefining how organizations operate — and IT leaders are at the center of this transformation. From infrastructure decisions to governance and workforce readiness, the path to enterprise-scale AI is as complex as it is critical. In this session, Cisco Compute leader Jeremy Foster and Nvidia Enterprise Solutions leader Chris Marriott are joined by Dr. Jose-Marie Griffiths, President of Dakota State University, for a strategic discussion on what it takes to lead in the age of AI. you'll hear how DSU is applying Cisco and NVIDIA technologies to support cutting-edge education and research, and how their experience mirrors the broader challenges and opportunities facing enterprise IT. They will discuss: Real-world insights from DSU's transformation into a living lab for AI, cybersecurity, and quantum innovation What enterprise infrastructure must deliver to support AI at scale The evolving role of IT leadership in policy, ethics, and responsible AI deployment This session offers a unique blend of industry, academic, and policy perspectives designed to help IT leaders turn AI ambition into action.

### AI for Calling made easy: Imagicle's latest updates for Webex - VILCOL-1066
Speakers: Anthony Genna (Imagicle)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848414001zFw4
SolutionsPlus Partner Imagicle will present the latest updates to its UCX Platform, including Compliance Recording, which is natively integrated with Webex's built-in recording solution; Imagicle Virtual Receptionist, the AI-powered digital twin of human receptionists designed to answer common questions and transfer calls to the appropriate contact or department; Engage Essentials, now available on Cisco Global Price List SolutionsPlus, the ideal companion for Webex Calling Multi-Tenant, which enhances Customer Experience Assist by adding digital chat channel capabilities to the Webex App; automate interactions with Virtual Agents and more.

### AI for the Future: Transforming Trends into Impact - IF-2000
Speakers: Shadnaz Nia (Cisco), Annie Hardy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271950370001ze79
As artificial intelligence reshapes industries, its potential to power an inclusive future has never been more profound. This session delves into compelling real-world AI adoption stories, examining how Cisco's AI-driven technologies and solutions are enabling equitable opportunities and redefining innovation. From Full-Stack Observability to Cisco SecureX, we'll explore the specific tools and frameworks that organizations are using to bridge gaps, foster innovation, and address global challenges. you'll leave this session with: Insights into transformative AI use cases utilizing Cisco technologies to deliver inclusive and sustainable outcomes. An understanding of emerging AI trends and their implications for businesses and communities. Practical strategies to integrate inclusive principles into AI adoption for meaningful impact and measurable ROI. Designed for participants with an intermediate understanding of AI and industry trends, this session blends thought leadership with actionable insights, demonstrating how Cisco and its partners are driving purposeful, technology-led transformations. Supporting Information for Submission: 1. Specific Technologies or Solutions: This session will highlight Cisco's leading technologies that play a pivotal role in advancing AI and inclusivity: Cisco SecureX: Enhances security while simplifying operations, ensuring AI-driven solutions remain secure and compliant. Full-Stack Observability (FSO): Provides end-to-end visibility across the tech stack, optimizing AI-driven workflows and supporting inclusive digital experiences. Cisco Webex Collaboration Suite: Facilitates accessible and inclusive communication through AI-powered features like real-time transcription and translation. Cisco Meraki IoT Solutions: Demonstrates AI in smart environments to create equitable access to resources and improve operational efficiencies. 2. ROI of Inclusive AI Trends: Inclusive AI isn't just a social good; it also delivers tangible business benefits. Examples include: Expanded Market Reach: AI solutions that cater to diverse needs allow businesses to tap into new customer segments, increasing revenue opportunities. Enhanced Employee Productivity: Inclusive AI tools, such as Webex's accessibility features, improve workforce efficiency by empowering all employees to contribute fully. Optimized Operations: Full-Stack Observability reduces downtime and operational inefficiencies, leading to cost savings and higher profitability. Stronger Brand Loyalty: Companies adopting inclusive AI solutions build trust and loyalty among customers who value equitable practices.

### AI in Cisco Certifications: Elevate Your Expertise - BRKCRT-1012
Speakers: Yusuf Bhaiji (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271834326001zceH
Uncover the essential differences between "AI in the network" and "AI on the network," and understand how these concepts are reshaping the technological landscape. Join us for an insightful session that delves into the world of AI, exploring their transformative impact across various technologies and job roles and ever-growing demand for reskilling & upskilling. This session will provide a deep dive into how Cisco is integrating AI skills across certification programs, including CCNA, CCNP, CCIE, and CCDE. We will discuss the inclusion of AI topics in these exams, ensuring that IT professionals are equipped with the essential knowledge and skills to harness AI technologies effectively in their roles. Whether you're preparing for certification or seeking to deepen your understanding of AI's role across technologies, this session offers valuable insights into the future of AI integration. Take advantage of this opportunity to stay at the forefront of technological advancements.

### AI in Collaboration: Techniques and Architectures for Audio, Video and Language A.I. - BRKCOL-2976
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857591001zdJn
In this session, we will look at the AI architectures behind audio, video and language AI in collaboration technology. This includes real time media models for audio and video along with cloud architectures for interaction with large language models (LLM). This session will look at the generative AI technology behind commonly used features such as message and meeting summarization, contact centre AI assistants, Slido poll generation and AI generated vidcasts. We will also look at edge AI models for realtime media such as face detection and background noise removal.

### AI-Accelerated Networking -- The Key to Modernizing Your Cisco Infrastructure - CNCNWT-1008
Speakers: Richard Garratt (NTT DATA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971580001z9OH
As AI, security, and software-driven advancements reshape enterprise networks, organizations must modernize their Cisco infrastructure to keep pace with increasing demands for agility, security, and automation. In this session, We'll explore how AI-accelerated networking, combined with a lifecycle approach, simplifies operations and unlocks new efficiencies. Discover how NTT DATA's Customer Experience Platform (CXP 2.0) enables seamless adoption, AI-driven insights, and automation through AIOps, helping organizations optimize performance, reduce complexity, and drive continuous innovation. Join us to learn how to future-proof your network and maximize the value of your Cisco investments.

### AI-Assisted Code Generation for Network Automation with CWM and NSO - DEVNET-2635
Speakers: Wai Tai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271906165001zZRx
AI is being used in a lot of different areas in the networking industry for improving productivity. This talk is on my experience of using GitHub Copilot to generate code for Crosswork Workflow Manager Workflows, adapters, and for retrieving information from NSO via its RESTCONF interface. I will share the challenges I have encountered with vendor specific product APIs and Serverless Workflow DSL code and the good results I got when context is provided. You'll leave this session with a clear understanding of how to leverage AI-assisted code generation in areas with limited publicly available examples, along with insights into its potential for network automation.

### AI-Directed Troubleshooting for 3-Tier Applications - BRKOBS-1023
Speakers: Gatha Sehgal (Cisco), Michael Raich (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271979715001z44h
Data overload, siloed information, and limited visibility across systems continue to pose significant challenges for IT Operations (ITOps) teams working to identify the root cause of issues causing downtime. In this session, we will explore how AI-directed troubleshooting in Splunk AppDynamics can revolutionize incident management by providing intelligent insights, automating data analysis, and offering predictive recommendations. Attendees will gain an understanding of how AI solutions can streamline root cause analysis, reduce mean time to resolution (MTTR), and enhance overall application reliability. Join us to discover how leveraging AI-driven tools can empower your ITOps team to overcome troubleshooting challenges and ensure seamless application performance.

### AI-Driven Packet Analysis - Is It Real, Can It Help You? - CNCSEC-1008
Speakers: Christopher Greer (Packet Pioneer), Ward Cobleigh (VIAVI Solutions)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271935761001zwjV
As network environments grow in complexity, speeds, and feeds, packet analysis gets increasingly challenging. In this session, We'll look at how Artificial Intelligence can change the game automating anomaly detection, accelerating root cause identification, and revealing patterns in network traffic that might otherwise go unnoticed. We'll examine how AI fits into your current troubleshooting workflow, where it's reliable, and where we need to validate its findings. Can AI really spot the issues you care about? How do you know when to trust it and when to take a second look? Whether you're a network engineer, a security analyst, or anyone responsible for performance and uptime, you'll walk away from this session with practical guidance on using AI to streamline manual analysis, improve accuracy, and gain deeper insight into network behavior. What you'll Learn: How AI can automatically identify anomalies in packet captures Ways to speed up root cause identification using machine learning models Practical techniques and tools you can utilize today Why Attend: See how AI is transforming packet analysis—its strengths, limitations, and how to make it work to your advantage Cut through network noise with faster, more intelligent insights Learn how to evaluate the trustworthiness of AI tools in a high-stakes, ever-evolving environment

### AI-Powered Automation: Building Smarter Apps for Cisco Catalyst Center Operations - BRKOPS-2570
Speakers: Casey Hamilton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271989367001z7WW
In this session, we will explore the transformative potential of integrating AI technologies with Cisco Catalyst Center. By harnessing the power of AI and tools like GitHub Copilot, attendees will learn how to efficiently develop applications using the 570 APIs available in Catalyst Center. These APIs span categories such as General DNA, Wireless, SDA, Integration, Event and Notification, Image Management, Compliance, Device Management, and more. The session will include a live demonstration of collecting APIs, feeding them into AI tools to develop a lightweight application, and showcasing how this can automate network operations. Participants will gain insights into creating adaptable, flexible, and secure environments across switching, wireless, and endpoint infrastructures.

### AI-Powered Management and Assurance - from Edge to Cloud and Beyond - CENAPP-1019
Speakers: Diego Turi de Oliveira (Ita? Unibanco), Sanjay Mehta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592613674001XtgF
As digital experiences increasingly rely on a complex mix of owned and third-party infrastructure, the pressure to deliver resilient, high-performance operations continues to grow. This Cisco Live Center Stage session explores how Cisco's cloud-based platform—combining unified management, end-to-end assurance, advanced AI capabilities, and Splunk integration—gives IT full visibility and control from edge to cloud. Join us to discover how Cisco is transforming operations with AI-powered assurance and unified management—giving IT the power to detect, pinpoint, and prevent issues before they impact user experience across cloud, hybrid, and on-premises environments. Real-world customer stories will highlight gains in visibility, control, and agility, with practical takeaways you can explore further in the Cisco Showcase.

### AI-Powered Mobile Networks - BRKMSI-2003
Speakers: Taran Deshpande (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271962491001zH0u
Discover how Cisco's innovative Service Provider AI/ML solution empowers Mobile Network Operators to optimize performance and streamline operations. Integrated with the routing portfolio, the solution leverages Machine Learning algorithms to provide a comprehensive view of mobile network performance at the cell site, application, and user levels. With real-time data analytics, operators can monitor end-to-end customer experience at the cell site, user, and application levels by tracking customer experience metrics. These AI-driven insights help operators proactively address network congestion issues, deactivate unnecessary cell sites to save energy, and identify the hidden underperforming cell sites before they lead to customer churn. The session will include a demonstration of Network Intelligence and Energy Reduction applications. Join us to explore how AI-powered mobile networks and automation can enhance customer experience, drive efficiency, support sustainability goals, and unlock new revenue opportunities.

### AI-Powered Network Operations: Proactive Detection, Analysis & Automation - VILOBS-2003
Speakers: Avraham Rosenbach (NetOp AI)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271974855001zwv8
As enterprise networks grow in complexity, IT teams must move beyond reactive troubleshooting to proactive, AI-driven network operations. By leveraging artificial intelligence and machine learning, organizations can automate issue detection, accelerate root cause analysis, and gain predictive insights that prevent disruptions before they occur. This session explores how AI-based analytics, automated assessments, and intelligent reporting can enhance network resilience, optimize operations, and reduce IT overhead. you'll leave this session with ideas to help you: Leverage AI for early detection of network issues, minimizing downtime and performance degradation. Implement proactive, automated detection and troubleshooting , using AI/ML to analyze and resolve impactful incidents before they escalate. Gain AI-driven analytics and predictive insights through automated assessments and reporting, enabling data-driven decision-making. Designed for network engineers, IT managers, and architects, this session includes live demonstrations of AI-powered incident correlation, predictive analytics, and automated troubleshooting in action.

### AI-Powered Operations: Copilots and RCA - CNCOBS-2002
Speakers: John Capobianco (Selector AI)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271974267001zfLK
AI is revolutionizing network operations, making infrastructure more intelligent and responsive. This session explores how AI-powered Copilots and Root Cause Analysis (RCA) enhance automation, troubleshooting, and remediation. Learn how Copilots provide real-time insights and AI-assisted decision-making, while RCA and AI agents enable proactive, self-healing networks. Through real-world examples, see how AI detects, diagnoses, and resolves issues automatically. The future of network automation is here—start integrating AI into your workflows and transform how you interact with your infrastructure, making it a true teammate.

### AI-Powered Scripting with GitHub Copilot - DEVNET-2159
Speakers: Jock Reed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271901342001z8TF
The irony of automation is that although there is plenty to be automated, we don't always have time to do it. With GitHub Copilot, you can provide natural language prompts and receive AI code suggestions, answers to questions found in your organization's documentation, and suggested descriptions for pull requests. This session dives into how these features can power your scripting workflow by using AI-powered scripts and Cisco Security APIs as examples.

### AI-driven Assurance: Transforming Network Operations - ITLGEN-2072
Speakers: Jon Woolwine (Cisco), Michael Bryan (Honeywell), Prab Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271958398001zwfn
Today's IT operations depend on a complex digital environment that spans owned and unowned networks, infrastructure, and applications. Implementing AI/ML technology can help IT teams improve security, troubleshooting and optimization within their environments; however, only 13% of companies globally are ready to apply AI and AI-powered technologies to their full potential. Join us to hear where Cisco's making investments in AI and observability to make it easier for IT Ops teams to see the user experience end to end. We'll provide insight into how Cisco runs its own network using data across its observability and assurance solutions and share how Honeywell assures digital resiliency across its business areas.

### AI-driven IT operations with Cisco Intersight - PSODCN-1012
Speakers: Gautham Ravi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271880977001z7Lk
In today's complex IT landscape, AI is no longer a luxury, but a necessity. This session explores how Cisco Intersight, Cisco's cloud-based IT operations platform, leverages AI to simplify infrastructure management. Whether you're new to Intersight or a seasoned user, discover how its SaaS model unifies operations and intelligence, eliminating manual tasks and operational silos. Learn about AI-driven capabilities like proactive security advisories, hardware compatibility alerts, and connected support intelligence that save time and resources. See how Intersight's Metrics Explorer enables comprehensive performance analysis and forecasting, empowering IT teams to focus on strategic initiatives and drive AI solutions across the enterprise. You'll leave with a clear understanding of how Intersight can transform your IT operations with the power of AI and where Cisco is taking it.

### AI-ready Industrial Networks: Discover How the Latest in Industrial Ethernet Switching Powers the Future - PSOIOT-1018
Speakers: Ruben Lobo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271951363001zcvU
AI has an immense potential to revolutionize industries, but its successful implementation hinges on a robust and secure network infrastructure . Industrial networks must step up to fulfill the challenging requirements needed to enable AI use cases and become the nervous system connecting physical components to the intelligence driving automation, resiliency, and enhanced security, leading to a new era of industrial efficiency and innovation. Join us as we explore how the latest Cisco Industrial Ethernet switches help build modern industrial networks that provide low-latency high-bandwidth connectivity for time-sensitive operational data, advanced security, and comprehensive visibility. These networks are foundational for deploying AI applications like virtual PLCs and vision systems , among others.

### AI/ML for Network Engineers - BRKENT-2209
Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933795001zkBW
This is an updated session for Cisco Live San Diego 2025 with a keen focus on AI and large language models (LLMs) for network engineers. In this fun and engaging session, attendees will review the various advanced Cisco AI/ML capabilities available to address network and application use cases, explore how AI network infrastructures are built, and most importantly, delve into practical examples of how you can use AI and LLMs to address your own network deployments, as well as expand your understanding of AI use cases and available tool sets. Presenting this session are the dynamic duo of Dave Zacks and Patrick leMaistre, both Cisco Live Distinguished Speakers with a passion for all things AI. Come to this session to gain insight into how AI can be used to help your organization succeed.

### AIOps 101: What is AIOps and how it can help you - BRKOBS-1012
Speakers: Isha Gandhi (Cisco), Annette Sheppard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271978369001z1st
AI is the current hot topic, but what is AIOps? In this session, we'll cut through the hype to define AIOps, how it can help you and how to get started. With real-world examples of how businesses succeed using Splunk's AIOps capabilities, we'll discuss applying AI and ML to accelerate incident response, reduce MTTD and MTTR, cut costs and empower teams with the tools they need to make decisions quickly.

### AMD: The Future of AI and HPC: Open, Scalable and High Performance Infrastructure Solutions - CNCDCN-1019
Speakers: Sandeep Subramaniam (AMD)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271878042001zI2X
As the demands for modern data centers evolve, the need for scalable, intelligent solutions becomes more critical. During this session Yousuf Khan, Corporate Vice President of Business and Product Management for Networking Technology Solutions, will highlight how AMD provides a full-stack solution designed to match the complexities of today's data center challenges. He will showcase how the complete suite of products - from networking hardware to AI-powered CPU and GPUs - delivers fully programable cutting-edge performance. Join us and discover how we can drive innovation together. ogether.r

### AWX 101: Getting Started in Automation with the Ansible AWX Platform - DEVNET-1060
Speakers: Tim Glen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893983001z6uI
Have you heard of Ansible but are concerned about another CLI? Do you know Ansible and want to take your skillset to the next level? Are you ready for the POWER of the Ansible AWX Platform!? Ansible is the industry's de facto automation tool and can automate almost any product a network engineer could use. But it gets better; AWX is Ansible's open-source big brother and provides Ansible with a powerful, user-friendly GUI front end. In this introductory session, participants will learn practical AWX concepts such as credentials, inventories, templates, and jobs. Demos will include AWX's Git integration for source control, building inventories, configuring templates, and reviewing jobs. Finally, we will discuss and automate some of the latest IOS XE sustainability features to help reduce power usage across all your Cat 9000 switches!

### AWX 201: Advanced Automation Techniques with Ansible AWX and Cisco Security - DEVNET-2517
Speakers: Tim Glen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271905765001zS00
Do you need better troubleshooting tools than Ansible CLI provides? Is managing your Ansible Playbooks, inventories, and logs cumbersome? Are you interested in storing your automation credentials in a highly secure Vault? Get ready to see some POWERFUL automation with the Ansible AWX Platform! In this session, participants will acquire advanced skills that will enable them to tackle more complex automation tasks. This session will focus on several things, including AWX Execution Environments, External Secret Management with Hashi Corp Vault, Multi-Project Workflows and finally ISE certificate management using AWX and Let's Encrypt. Participants should already be familiar with practical AWX concepts such as credentials, inventories, jobs, and templates.

### Accelerate Your AI Workloads with UCSAI-885-M8 - TACDCN-2018
Speakers: Jason Smith (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271882108001zkCr
Join us while we work through the set up of the UCSAI-885-M8 AI server. This session will cover the basics from the initial power up and IP configurations all the way through connecting your new server to Intersight. Highlights will include, tech-support generation, upgrades, a walk through of the BMC, and much more.

### Accelerate Your Cloud Journey with Cisco and AWS - CNCGEN-1015
Speakers: Sudha Thillai Govindarajan (AMAZON WEB SERVICES), Ranjit Kalidasan (Amazon Web Services (AWS)), Josh Leatham (Amazon Web Services)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271943369001zTgp
In today's digital landscape, enterprises are increasingly adopting cloud-first strategies to drive innovation, scalability, and business agility. This session explores how Cisco and AWS have aligned their strategic visions to create a powerful ecosystem that accelerates enterprise cloud adoption while addressing critical challenges in security, networking, observability, and collaboration. We'll begin by examining why leading organizations are embracing cloud-first approaches and how the combined strengths of Cisco and AWS deliver comprehensive solutions that optimize cloud investments. Attendees will gain insights into AWS's core offerings and Well-Architected Framework, followed by an in-depth look at how Cisco's expanded portfolio—including the recent Splunk acquisition—complements and enhances the AWS cloud experience. Through practical examples and use cases, we'll demonstrate how Cisco solutions provide: • Enhanced observability across hybrid environments • Comprehensive security that extends from on-premises to cloud • Seamless networking that bridges traditional and cloud infrastructures • Collaboration tools optimized for distributed workforces

### Accelerating AI with Cisco Infrastructure and NVIDIA Blueprints - CISCOU-2062
Speakers: Charu Chaubal (NVIDIA), Paniraja Koppa (Cisco), Chris O'Brien (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271842143001zB5B
This session explores the collaboration between Cisco Compute and NVIDIA to advance AI deployments using cutting-edge digital infrastructure. Leveraging Cisco's AI PODs and NVIDIA GPUs, we highlight how full stack architecture bundles optimize AI operations in healthcare, finance, and other sectors. NVIDIA's Blueprints for agentic and generative AI ensure rapid deployment and adoption, enhancing efficiency. Discover how Cisco's infrastructure, paired with NVIDIA Blueprints, elevates an organization's AI experience. Join us to see how these solutions empower organizations to scale intelligence and transform business outcomes.

### Accelerating Modernization and Execution Strategies for AI - CENCX-2205
Speakers: Eric Knipp (Cisco), Carlos Pereira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592614208001XH62
Join us to explore how AI can be integrated into your business strategy and deliverables, ensuring alignment with core objectives while maintaining security, scalability, and efficiency. With many enterprises transitioning from piloting to operationalizing AI, the push to modernizing their secure IT infrastructure to support AI initiatives and other advanced technologies has accelerated. Carlos Pereira, Cisco Fellow and Chief Architect, CX, will discuss how to identify impactful use cases and efficiently design and develop AI solutions through experimentation, validation and deployment. Eric Knipp, Senior Vice President, CX Americas, will highlight the importance of strategic partnerships and policies to secure your AI infrastructure and safeguard intellectual property. Together, they present a practical approach to AI adoption, enhancing existing business functions and leveraging unique insights to drive growth and efficiency through informed and strategic AI integration.

### Accelerating Operational Excellence with Cisco Nexus Dashboard -- A WWT & Cisco Success Story - CSSDCN-1007
Speakers: Karishma Gupta (Cisco), Nathan Litz (World Wide Technology)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879006001z7Ti
As data centers become more complex and distributed, network teams need smarter ways to manage scale, performance, and risk - especially in AI/ML-driven environments. In this session, you'll learn how World Wide Technology (WWT) partnered with Cisco to unify and simplify their operations across multiple fabrics using a consolidated operational model offered by Nexus Dashboard. Discover key lessons from WWT's journey: • How to prepare your network to support demanding AI/ML workloads • Ways to leverage telemetry and automation to reduce troubleshooting time • Best practices for scaling securely and improving compliance across hybrid environments Join us to gain practical insights into transitioning toward intent-based operations and building a resilient, intelligent network foundation.

### Accelerating Your Core Networking Journey - CNCMSI-2000
Speakers: Michael DiVincenzo (WORLD WIDE TECHNOLOGY INC), John Chiarini (WORLD WIDE TECHNOLOGY)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959799001z7vR
Convergence of the optical & packet networks promises a future of simplified operations, powerful capabilities, and reduced costs. Here's how WWT can help. 1 Network Assessment on all current and proposed traffic types/patterns/growth/ Protection. AI will impact all of these factors to varying degrees during the lifecycle of any selection made today. 2 Update on Solution Components and very latest on enhancements that improve the HW/SW/Automation elements value proposition in total solution 3 Potential Migration paths with ROIs/ Risk/Benefit analysis 4 Partner full lifecycle services that support these changes in the MAN/WAN and DC architectures 5 Focus on unique POC/Lab capabilities in mixed vendor mixed OS management migrations Implementing a converged optical & packet architecture can be a difficult task. Let WWT help accelerate the time to validate, deploy and migrate your services. WWT has the expertise and capabilities to deliver a complete end to end optical & packet architecture and can ease the path towards migration.

### Achieve Digital Resilience with AI-Powered Automation - PSOMSI-1002
Speakers: Javier Antich (Cisco), Vidya Sawhny (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271960376001zsiA
As subscriber expectations rise, service providers must enhance service agility, improve efficiencies, and elevate customer experiences. In this session, discover how Cisco's AI-powered end-to-end automation and assurance solutions provide service providers with predictive insights and analytics, enabling them to plan, deploy, and manage networks intelligently with speed, accuracy, and scalability. See how AI-enabled automation transforms vast amounts of network data into actionable insights while leveraging AI/ML to optimize performance, detect anomalies, and boost digital resilience. This empowers customers to transition from manual, reactive approaches to proactive solutions and make faster, more reliable decisions.

### Achieving Industry Standards, Frameworks and Architectures Using Duo - BRKSEC-1017
Speakers: Ned Zaldivar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272006425001z4KK
Identity is the new perimeter. You need identity for everything in your life. Drive a car, get on a plane, buy medication.... The same is true with accessing business applications. Without proper identity, how can the business application really trust you or your device? username and password? biometrics/password-less, SSO, SAML, certificate? How can your business achieve or comply with industry standards, frameworks and architectures? Using DUO technology you will learn ways to achieve PCI DSS, Zero Trust Network Access, Secure Access Service Edge, Security Services Edge, HIPAA, NERC/CIP or NIST frameworks and architectures. Ultimately increasing your organizations security posture.

### Active Defense and Adversary Engagement using Mitre Engage - BRKSEC-2182
Speakers: Mark Stephens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001955001zJ90
Are you prepared to confront the unsettling reality that a cyber adversary may already be lurking undetected within your network's shadows? The thought alone is enough to keep any security professional up at night. But fear not, because our upcoming session is an absolute must-attend for anyone serious about cybersecurity. We will delve deep into the cutting-edge Mitre Engage framework, a revolutionary approach that empowers you to proactively hunt down and neutralize threats before they escalate. This isn't just another lecture; it's an interactive experience that will equip you with the skills and insights to turn the tables on intruders. By joining this session, you'll transform from a passive defender, anxiously awaiting an attacker's misstep, to a strategic enforcer of your network's integrity. Don't miss this opportunity to gain a critical edge in the ever-evolving battle against cyber threats. Secure your spot now and be the force that keeps adversaries at bay. Your network's safety hinges on your proactive stance—be the one who takes it.

### Add Visibility to Your S(A)SE with ThousandEyes - BRKSEC-2857
Speakers: Primoz Kolman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003895001z5Jz
Your organization may be utilizing Cisco Secure Access and Cisco SD-WAN . Perhaps you are contemplating the deployment of Security Service Edge ( SSE ) or the more comprehensive Secure Access Service Edge ( SASE ) technologies. Are you concerned about the loss of control and visibility during the transition of your infrastructure to the Internet and the cloud? This session will demystify how ThousandEyes enables Experience Insights within Secure Access and provides you visibility across your SD-WAN network. You will learn how and what to deploy to assure your employee's digital experience against software as a service (SaaS) and on-prem applications, regardless of where your users are (in the office, at home, or abroad), whether you use Cisco Secure Access, Cisco SD-WAN, or a combination of both. Tjis is an intermediate level session. Atendees should have a basic knowledge about ThousandEyes, Secure Access or Cisco SD-WAN solutions.

### Advanced Border Gateway Protocol - BRKENT-3219
Speakers: Gustavo Sibaja (Cisco), Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271935149001zLtt
Session "Border Gateway Protocol Fundamentals - BRKENT-1179" laid the groundwork for understanding fundamental BGP operations. As a natural progression, this breakout session will serve as a continuation, delving into advanced protocol features that propel network architectures to new heights of efficiency, security, and scalability. In this session, we embark on a journey beyond the basics, exploring the intricacies of advanced BGP design and implementation. Topics to be covered include, but are not limited to: - Protocol Extensibility: Unraveling the intricacies of extending existing BGP capabilities to accommodate new functionalities and adapt to evolving requirements without compromising interoperability. - Security Enhancements: Exploring advanced security mechanisms embedded within BGP to mitigate emerging threats. - Scalability Solutions: Examining techniques for optimizing BGP performance to scale seamlessly with the exponential growth of network traffic and devices. Participants will gain a deeper understanding of advanced BGP features. Whether you're a seasoned network architect or an aspiring networking enthusiast, this session offers invaluable insights to propel your expertise to the next level.

### Advanced Campus Network Design: Multilayer Architectures and Next-Gen Protocols - BRKENS-2500
Speakers: Shawn Wargo (Cisco), Jakub Matela (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271923214001zwdJ
This advanced session builds on the foundational knowledge from "Introduction to Campus Network Design and Multilayer Architectures - BRKENS-1500" and refreshes the core concepts of "Enterprise Campus Design: Multilayer Architectures and Design Principles - BRKENS-2031. Attendees will explore the details of designing high-performance, scalable multilayer campus networks, with an emphasis on advanced protocols and technology integration. Key topics include: Advanced aspects of multilayer campus network design Pros and cons of different design models (1-2-3 or 4+ Tier) Advanced protocol implementations (ECMP vs. StackWise / MPLS vs. EVPN vs. SD-Access) Integration with wireless and security solutions Real-world examples and best practices for optimizing enterprise networks This session is geared towards professionals responsible for the design, deployment, and management of enterprise campus networks, who possess a solid understanding of LAN switching and routing fundamentals.

### Advanced Catalyst SD-WAN Policies Troubleshooting - BRKENT-3797
Speakers: Eugene Khabarov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271935535001zg7J
This is a deep-dive session on troubleshooting Cisco SD-WAN policies. It is based on extensive experience from the TAC and BU escalation teams. The main goal of this session is to demonstrate troubleshooting tools, approaches, interesting failure scenarios and common pitfalls that have been observed in the field. These include configuration and design mistakes with centralized control, data, and application-aware routing policies. The session will be based on various real-life scenarios involving DIA, NAT, traffic engineering, routing, deep packet inspection, classification, and QoS marking. It will show how behaviors that are not initially expected can be revealed through advanced troubleshooting methodologies. And yes, we will be using the CLI a lot. Please note that this is an advanced-level session and it does not cover the basics of SD-WAN. The target audience for this session includes network architects, consultants, engineers, and network designers who are seeking a deeper understanding of SD-WAN policies troubleshooting, as well as knowledge to avoid common mistakes in their day-to-day operations, design, and deployment activities when working with a Cisco SD-WAN solution. It is recommended to have reviewed the "Advanced SD-WAN Routing Troubleshooting" session (BTKENT-3793) from CiscoLive OnDemandLibrry as a prerequisite for this session.

### Advanced LISP SD-Access Forwarding Architecture - BRKENS-3826
Speakers: Jerome Dolphin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924965001zuTH
This session will delve into the fundamentals of packet forwarding within a LISP Pub/Sub SD-Access Fabric. We will explore the use cases for LISP, Cisco Express Forwarding (CEF), and Switch Integrated Security Features (SISF). The contribution of each technology to SD-Access packet forwarding and security will be systematically examined, supported by concise lab demonstrations to illustrate the underlying concepts. Participants should anticipate a session focused on protocol analysis, IOS XE configurations, and CLI operations. It is recommended that participants review the content of BRKENS-2810 and BRKENS-2811 prior to attending.

### Advanced SDWAN design with Cisco Secure Firewall - BRKSEC-3058
Speakers: Jeff Fanelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012951001zsI9
Complexity of SD-WAN and cloud based VPN use cases means customers need more advanced VPN capabilities in their firewall platforms. This 90 minute breakout session will detail advanced use case designs for Secure Firewall Threat Defense and ASA VTI (Virtual Tunnel Interface) based VPN use cases and associated WAN routing protocols. Hub and spoke VPN, full mesh VPN, and SASE tunnel connectivity to Cisco Umbrella use cases will be detailed, along with brief troubleshooting overviews. Branch SDWAN application optimization capabilities will also be detailed.

### Advanced SGT - Multi Domain Context - BRKSEC-3707
Speakers: Darrin Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272013754001zB6E
This session examines the use cases for Security Group Tags (SGTs) and how SGTs have evolved into the defacto language for security policy within Cisco and the industry. SGT uses software defined network abstractions to enable scaling of network security within enterprises for a Unified Zero Trust Network Access solution. This session will review lower level design, configuration, monitoring and troubleshooting of SGTs and SGACLs applied to use cases like user/device segmentation, IaaS and SaaS policy controls as well malware mitigate Security Group technology will be discussed as applied to LAN, WLAN, WAN and Data Center networks. This session is aimed at Network/Network Security Specialists and Architects involved in designing and building advanced security solutions scenarios using Cisco network and security appliance deployment models. Attendees should be familiar with SGTs, Cisco routing, switching, wireless and security appliances at a conceptual level and a detail knowledge of one of those disciplines. Suggested prior sessions include sessions on the Identity Services Engine (ISE), SDA, Segmentation and network authentication (802.1X on wired and WLAN).

### Advanced Security Strategies by Baltimore Police Department and Howard County - CSSSEC-2010
Speakers: Yue Zhu (Baltimore City Police Dept.), Rob Paris (Cisco), TJ Mayotte (Howard County Government)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271874900001zXhL
Join a security fireside chat featuring leaders from Baltimore City Police Department and Howard County Maryland government as they share their transformative security strategies utilizing Cisco solutions. BPD will bring perspective on their journey with XDR security architecture, improving digital resilience and operational efficiency as largest independent city in the USA. Howard County will discuss how they are securing their communities in the surrounding Washington DC Capital region with Cisco Security solutions. In this chat, gain insights into adopting innovative security measures across diverse sectors.

### Advanced Storage Area Network Design - BRKDCN-2941
Speakers: Ed Mazurek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889406001zyQ0
This session presents the details of the protocols, principles, and practices used in designing Fibre Channel(FC) storage area networks (SANs). A review of FC protocols will be followed with a discussion of the advanced capabilities of the Cisco MDS 9000 family. Design principles and practices for building FC SANs in a multi-speed, multi-protocol environments, including high availability, security, scalability, and management. Included are topology design choices, optimal use of hardware, fabric routing (FSPF), link aggregation (Port Channels), TCAM usage and Virtual Fabrics (VSANs). The last section will cover integration of intelligent SAN services such as SAN extension with FCIP using the new 1/10/40G IPS,2/4/8/10/16G FC Module and optical extension (CWDM and DWDM), Acceleration, and Data Mobility. This session also covered SAN management using Nexus Dashboard.

### Advanced Terraform Techniques: Moving Beyond the Scaffolding - DEVNET-3722
Speakers: Quinn Snyder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271910650001zlkb
A lot of emphasis is put on the use of Terraform to create immutable structures within an API-enabled product or platform. However, this barely scratches the surface of what is possible. In this session, we'll discuss the creation of Terraform modules, how to manipulate data, and how to use conditionals, loops, and other "programmatic constructs" to take your Terraform HCL to the next level!

### Advanced Wi-Fi Tuning: Become an Expert While Getting a Little Help from AI - BRKEWN-3413
Speakers: Jim Florwick (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271942414001zu14
Participants will learn the RF design and implementation guidelines necessary to plan, configure, and implement Wi-Fi networks that meet the evolving regulatory (6 GHz) and customer RF demands. Wi-Fi is changing, and there has never been a more exciting time to be in RF technologies. In this session, you will learn about Cisco's newest Catalyst wireless access points and antennas, including the latest Wi-Fi 6E access point and the new Wi-Fi 6 stadium antenna. Participants will learn and understand the current coverage and design best practices as well as what this means to the evolving RF landscape around the world. Everything we know is evolving. This session will provide a deep dive on how to think about and manage Wi-Fi 6E, RRM, spectrum intelligence, and the evolution of multi-band operations within the infrastructure. The evolution to Wi-Fi 6E brings amazing RF capacity gains. Wi-Fi 6E also means new pressures on the wired infrastructure capacity and power that supports it. Attendees will learn what to expect and how to manage and plan for future needs now. Session attendees will be able to successfully use the information to navigate and understand today's fluid RF and mobility landscapes and articulate the benefits to their customers, enabling the best wireless and mobility experiences yet.

### Advanced YANG Data Modeling for Cisco NSO - DEVNET-3014
Speakers: Bartosz Luraniec (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271909486001zV1G
Cisco Network Services Orchestrator (NSO) is software for automating services across traditional and virtualized networks. Used with YANG data models enables us to manage large topologies, work with multi-vendor nodes, automate, and scale. The participants will have the possibility to see how YANG tricks combined with NSO can make their business more agile and promote non-stop operations as they will be able to manage network changes, modify services, and reconfigure devices in real time. During this session, the participants will be able to discover YANG solutions derived from Cisco CX best practices on various large scale NSO deployments, and discuss strengths and limitations over a demonstration.

### Advancements and Applications of Coherent Pluggable Technology in High Bandwidth Transport Networks - BRKOPT-2556
Speakers: Anuj Malik (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963268001zbFi
Coherent pluggable technology has emerged as a pivotal solution, integrating coherent optics into pluggable transceivers. This innovation offers a scalable, flexible, and cost-effective approach to meet the increasing demand for bandwidth. This presentation will delve into the technical underpinnings of coherent pluggable technology, including key components such as tunable lasers, high-speed ADC/DACs, and sophisticated DSP algorithms. It will also explore the performance metrics, such as data rates, reach, and power consumption, comparing them with traditional coherent solutions. Furthermore, the session will highlight real-world deployment scenarios, case studies, and future trends, underscoring the transformative impact of coherent pluggables leading to convergence of IP and Optical layers.

### Agentic AI Meets Network Digital Twin - CNCOPS-2003
Speakers: Nikhil Handigol (Forward)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271984044001zWti
Agentic AI holds great potential in networking and security, but its effectiveness relies on high-quality data and trusted decision-making. Forward Networks delivers both through its comprehensive, vendor-agnostic network data and verifiable insights. This session will demonstrate how Forward Networks' Network Digital Twin enables AI agents with end-to-end vendor-agnostic configuration, state, and path data. We'll present a coordinated swarm of agents delivering deep network insights, including a universal query agent that unifies their capabilities. Finally, We'll highlight seamless integration with platforms like ServiceNow through a ticketing agent that enriches tickets with real-time network context to streamline resolution.

### Agentic AI and NetDevOps: Enabling a New Era of Network Change Validation - BRKNWT-2502
Speakers: Giovanna Carofiglio (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271972745001zeee
As networks grow in complexity and scale, the need for robust change validation processes has never been more critical. Despite years of research and the development of numerous tools for network verification, significant gaps remain in creating a unified platform that seamlessly integrates Network Source of Truth Data, Verification tools, simulators, and emulators. This Cisco Live breakout session delves into how Agentic AI and NetDevOps can bridge these gaps and usher in a new era of network change validation. We start by addressing the current challenges in the heterogeneous landscape of network verification tools. The absence of a reference platform complicates efforts to consolidate critical data and tools, hindering effective validation and innovation. However, the advent of Agentic AI offers promising solutions. By leveraging generative AI, we can automate and enhance network operations, enabling sophisticated data modeling by means of network digital twins as agentic tools. These digital twins serve as accurate replicas of production networks, invaluable for verification, testing, and reasoning about change or validation intents. Moreover, adopting an automated, DevOps-inspired approach can revolutionize network change validation. In this session, you will learn: The current limitations in network verification tools and the need for a unified platform. How Agentic AI enhances network modeling and validation through digital twin technology. The transformative impact of NetDevOps in automating and optimizing network change processes. Practical strategies for integrating these technologies to achieve an efficient network validation workflow. Join us to explore how Agentic AI and NetDevOps can empower your organization to overcome existing challenges due to manual costly error-prone network operations and lead the change in innovative network management.

### Agentic AI for Troubleshooting and Change Management: A Glimpse at the Future - DEVNET-2094
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899986001zfdB
Agentic AI, characterized by autonomous decision-making capabilities, is poised to revolutionize troubleshooting and change management in IT operations. This presentation explores how agentic AI systems can autonomously identify, diagnose, and resolve issues, minimizing downtime and reducing human intervention. By leveraging machine learning and real-time data analysis, these AI agents can diagnose complex multi-domain systems like humans do. Gone are the days, where cross domain troubleshooting and change impact prediction required consolidation of all data into a single data-lake, complex rule systems and ontologies. Join us for a glimpse into the future where agentic AI transforms how we manage IT systems.

### AgenticOps in Motion: AI Agents Powering a Unified Cisco Experience - BRKXAR-2028
Speakers: Richard Jang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271870813001zIEG
Generative AI has entered the mainstream, delivering powerful results across industries and reshaping how work gets done. But the next wave isn't just about chat interfaces it's about autonomous agents that can reason, plan, and act across systems. At Cisco, we call this emerging shift AgenticOps : a new operational model where AI Agents unify the user experience across networking, security, and collaboration. In this session, We'll begin by demystifying the foundations of AI—machine learning, neural etworks, and generative models—and explain how they power Today's AI Assistants. Then, We'll show how Cisco is going beyond individual product assistants to create a connected network of AI Agents that work together across domains. you'll see how AgenticOps enables dynamic troubleshooting, automation, and seamless workflows that span Cisco's vast ecosystem. Whether you're looking to grasp the core principles of AI or want to understand how agent-based intelligence is transforming enterprise IT, this session offers both strategic insight and real-world application.

### An Inside Look at How Cisco Does IT - ITLGEN-2060
Speakers: Fletcher Previn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959611001z4d8
Every minute an employee spends struggling with a system is a minute they're not doing the work they were hired to do and the work they're passionate about. That's friction that IT has a unique responsibility to alleviate. Join Fletcher Previn, Cisco SVP & Chief Information Officer, for a keynote address on the unique role and responsibility of IT in shaping culture and employee experience in enterprise organizations, and how Cisco IT leverages AI as a force multiplier.

### An Introduction to Quantum Mechanics, Computing, and Networking - BRKETI-1401
Speakers: Tim Szigeti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916244001zYZ1
Cisco is making a major R&D investment in quantum networking, as future communication systems equipped with quantum networks will open new possibilities in several technology domains, including distributed quantum computing, secure communications, global clock synchronization, high-accuracy sensors, and more. This is an introductory session to the science and technologies that enable quantum networking. This session will begin with a brief introduction to quantum mechanics, with a focus on quantum bits (qubits) and some of their special properties, including superposition, entanglement, and no-cloning (Note: this discussion will include some mathematical concepts and proofs). This will be followed by an overview of quantum computing, to better understand the direct impact and demands this emerging technology is already having on network communications and security. Finally, we'll bring it all together to outline the building blocks, opportunities, and challenges of building quantum networks, as well as highlight what Cisco is already doing in this exciting space!

### An Introduction to SONiC on Cisco 8000 - DEVNET-1086
Speakers: Suhaib Ahmad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271894173001zLyt
SONiC is an open and disaggregated network operating system with features geared towards web and service provider use-cases. It provides a unified software architecture consistent across multiple vendors and ASICs. This DevNet session will introduce participants to the SONiC software architecture, design principles as well as the SAI abstraction layer that enables SONiC on Cisco 8000 routers. The session will also showcase the management framework supported by SONiC and highlight SONiC serviceability features for operational ease. Finally, we will discuss key networking features in Cisco 8000 routers running SONiC to understand the network roles that SONiC can fulfill.

### An Introduction to eBPF for Network Security Engineers - DEVNET-2927
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271908120001zudD
In today's rapidly evolving cybersecurity landscape, staying ahead of threats requires cutting-edge tools and techniques. Extended Berkeley Packet Filter (eBPF) is transforming how network security engineers monitor and protect systems in real-time. This session will introduce eBPF's powerful capabilities for network security, offering live examples tailored for security professionals. Participants will learn how to leverage eBPF to monitor network traffic and detect suspicious patterns and potential attacks, trace system calls to identify unauthorized access attempts, and block malicious connections based on predefined security policies. You'll leave this session with ideas to help you enhance your security monitoring, detect anomalies, and respond to threats more effectively. Understanding of basic network protocols and Linux system internals is recommended. The session includes live demonstrations of eBPF in action, showcasing practical use cases and real-time analysis techniques. You will also learn how eBPF is leveraged by Cisco Hypershield, a groundbreaking security architecture designed to defend modern, AI-scale data centers. Join us to explore how eBPF can be a game-changer in your security toolkit and empower you to safeguard your network with advanced, real-time monitoring capabilities.

### Application Security with eBPF and Hypershield API - DEVNET-1691
Speakers: Oleksii Borysenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271896702001zAZR
As businesses migrate applications across hybrid cloud landscapes, eBPF technology enables more dynamic, granular security and performance monitoring in increasingly complex containerized and microservices environments. By leveraging advanced API capabilities, Hypershield enables organizations to integrate sophisticated security controls into their CICD pipelines, automate policy testing, and empower SecOps teams to proactively manage and respond to emerging threats through intelligent, AI-driven compensating controls and self-qualified updates.

### Applying AI/ML Methods to Diagnose Network Issues Using Telemetry Data - AIHUB-2006
Speakers: Frank Brockners (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866785001z3jd
Troubleshooting remains largely a manual process, with substantial time devoted to diagnosing issues. This session explores how AI/ML can expedite initial diagnoses. It delves into the suitability of various AI/ML techniques for network data and different phases of analysis, such as problem identification and diagnosis. Using real-world telemetry data as a foundation, we will collectively examine and demonstrate the use of diverse AI/ML approaches, including large language models, to pinpoint and diagnose issues. Concurrently, we will discuss the advantages and drawbacks of the various technologies employed. Note: This session is a shortened version of the breakout session BRKETI-2172 - "A New Era of Cross-domain Diagnostics with AI and Agentic Systems"

### Applying UCS X-Series Advanced Power and Cooling Management to Your Sustainability Goals and Reporting - BRKCOM-2933
Speakers: Doron Chosnek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271862347001zVpA
We will review the unique technical differentiators of the X-Series modular platform including fabric-based computing, power and cooling architecture, relevant policy options for tuning power demand and the measurement and reporting options. We will examine the impact of power saving settings on power consumption and best practices for optimal workload performance. We will discuss how these relate to your energy related sustainability goals and reporting. We will also review how modular systems provide other direct benefits to overall sustainability objectives.

### Architecting AI-Assisted Automation Frameworks for Large-Scale Deployments? - BRKATO-2001
Speakers: Faisal Azizullah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271831712001zbha
As organizations scale their operations, the integration of AI into automation frameworks has become a critical enabler for efficiency, security, and adaptability. This session provides a practical guide to designing scalable, AI-driven automation frameworks that streamline processes and optimize infrastructure. Attendees will learn the core principles of AI-assisted automation, including modular framework design, dynamic workflow automation, and infrastructure optimization. The session will explore how to leverage AI for real-time decision-making, anomaly detection, and proactive resource management while maintaining robust security with zero-trust principles and enhanced observability. Participants will see how to integrate Cisco's automation ecosystem—including Nexus Dashboard, AppDynamics, and ThousandEyes—with orchestration tools like Ansible and Terraform. This session focuses on practical, actionable strategies to build scalable, flexible solutions that address real-world challenges and align with modern enterprise needs. Whether you're starting your automation journey or enhancing existing workflows, this session equips you with the knowledge to design AI-powered frameworks ready for large-scale deployments.

### Architecting Hybrid Multicloud Infrastructures - BRKDCN-2916
Speakers: David Jansen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271888643001zmJj
Cloud continues to be the disruptor, and customers have been on the cloud journey for several years. This session will address the following architectural trends and provide guidance for the growing demand of users and applications being everywhere in a multicloud world. As applications and data migrate from traditional private data centers to public clouds, private data centers and applications remain critical. This session will offer architectural guidance to help customers optimize and understand traffic flows, achieve operational efficiencies, and gain visibility in a multicloud world.

### Architecting Layer 4-7 Network Services in a Multi-Tenant Data Center with VXLAN EVPN - BRKDCN-2974
Speakers: Matthias Wessendorf (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271891516001zUaP
With VXLAN BGP EVPN data center fabrics, we now embrace integrated multi-tenant capabilites. With this, not only is the requirement for tenant separation present but also interconnectivity and attachment of layer 4-7 services. This session specifically covers requirements and approaches for deploying multi-tenant data center fabric with a focus on how to archive multi-tenancy within data plane and control plane around VxLAN with BGP EVPN. Further, the session will cover integration of layer 4-7 services to satisfy the needs of tenant interconnectivity, security appliance, and load balancers attachement. We will define the notion of multi-tenancy and how it relates to small, medium, and large enterprises, as well as discuss hardware and software technologies as they map to multi-tenant data centers. Subsequently, the integrating of layer 4-7 services into VxLAN with BGP EVPN is approached. This session will focus exclusivly on data center fabric deployments with VXLAN BGP EVPN including EVPN multi-site.

### Architecting Private Cloud-Like Services with Cisco Nexus and Isovalent - Cilium - BRKDCN-2982
Speakers: Stephen McCabe (Cisco), Christopher Luciano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271891894001zgUA
As businesses increasingly seek to replicate the agility and scalability of public cloud services within their private cloud environments, leveraging the right tools and architectures has never been more critical. Recent advancements in network overlays, container networking, and service observability make this an opportune time to explore building "AWS-like" services in private clouds. This session dives deep into how Nexus EVPN/VXLAN and Cilium can power next-generation private cloud solutions.

### Architecting Secure Multidomain Networks and Automating with Net-As-Code: Integrating ACI, VXLAN EVPN, SDA, SD-WAN, MPLS, and Cloud - BRKXAR-3022
Speakers: Navin Suvarna (Cisco), Dhrumil Prajapati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871955001z1hR
Modern enterprises rely on multiple software-defined networking domains - ACI, VXLAN EVPN, SDA, SD-WAN, MPLS, and Cloud, but integrating them into a secure, scalable, and cohesive architecture remains a challenge. This session explores how to architect multidomain networks that enable seamless interoperability while ensuring strong security and policy consistency. Once the architecture is established, the next challenge is automation —this is where Net-As-Code comes into play. We will demonstrate how Net-As-Code simplifies cross-domain orchestration, enhances operational agility, and ensures consistent policy enforcement. Another key focus will be on security , specifically the use and exchange of Scalable Group Tags (SGTs) across domains to enable dynamic segmentation and strengthen zero-trust policies. While automation enhances operational efficiency, security must be architected into the foundation to ensure robust, policy-driven protection across domains. Join the authors of Designing Real-World Multi-Domain Networks as they share proven strategies, real-world use cases, and lessons learned from years of architectural and automation expertise. Attendees will leave with a clear understanding of how to design secure multidomain networks , use Net-As-Code to automate operations , and architect security policies that span across domains .

### Architecting a Private Cloud for AI Workloads - BRKCOM-2519
Speakers: Dan Stacks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861002001zYyB
As artificial intelligence (AI) continues to revolutionize industries, the need for robust and scalable infrastructure to support AI workloads becomes paramount. This session will provide an overview of AI workloads and the critical infrastructure considerations necessary to support them. Participants will learn how to translate model cards into specific infrastructure requirements, effectively size their deployments, and understand the power and physical capacity considerations essential for optimal performance.

### Architectural Best Practices for Ensuring High Availability of IOS XR IP/MPLS Backbone Networks - BRKSPG-2080
Speakers: David Smith (Cisco), Lokesh Khanna (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271968328001zRi6
Network failures and erroneous events can significantly compromise network performance and availability. Predicting and preventing every possible failure scenario is challenging. Thus, implementing high availability (HA) strategies is essential to mitigate the negative effects of such events. In this breakout session, we will review architectural principles and best practices for ensuring high availability of IP/MPLS backbone networks using IOS XR software. Join us to gain valuable insights and practical advice on strengthening the resilience and robustness of your IOS XR network infrastructure.

### Are You Prepared for the Next Typhoon? - BRKSEC-2499
Speakers: Paul Giralt (Cisco), Steve Nowell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003117001zp8C
In 2024, the U.S. government confirmed public reports of widespread intrusion activity against multi-vendor infrastructure at several major telecommunications companies perpetuated by highly sophisticated threat actors known as Salt Typhoon. This session will kick off with insights from Cisco Talos, highlighting the nature of these threat activities to deepen your understanding of the attack surface and the need for action to protect your infrastructure. We will then discuss specific steps you can take today to protect your network infrastructure from future attacks through hardening recommendations and best practices. Finally, we will discuss future enhancements to make your network infrastructure more secure by default and give you the opportunity to provide feedback on these plans. Come join us to learn how you can strengthen visibility and defenses to be better prepared to detect and respond to future attacks and avoid being struck by the next Typhoon.

### Art of generating images - CTF-1049
Speakers: Supratim Chakraborty (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271914138001zZX4
"The generation of images using artificial intelligence represents a profound intersection of art, computation, and human imagination. Driven by advances in deep learning—particularly Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs), and diffusion models—AI image generation has evolved from rudimentary pixel predictions to photorealistic renderings, artistic styles, and concept-driven visualizations. This process, often guided by textual prompts or semantic conditions, transforms abstract ideas into coherent visual outputs, enabling novel forms of creative expression and human-computer collaboration. At the core of this art lies prompt engineering, model selection, and iterative refinement, where creators manipulate latent spaces and conditioning inputs to sculpt desired outcomes. The resulting images are not merely outputs of code but co-creations that reflect both algorithmic possibilities and human intention. As AI-generated imagery becomes more nuanced and accessible, it challenges traditional notions of authorship, originality, and aesthetics. This talk explores the artistic and technical methodologies behind AI image generation, the role of generative models in visual storytelling, and the ethical and cultural implications of this emerging digital art form."

### Asset Intelligence in Action: AI-Powered Attack Surface Management - VILSEC-2005
Speakers: Joseph Alapat (Liongard)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271992487001z1iz
Today's cyber threats don't wait — and neither should your defenses. As IT environments grow more complex and attackers more creative, it's time to shift from reactive event-based security to proactive cyber resilience. In this fast-paced session, We'll explore how the convergence of External Attack Surface Management (EASM), Cyber Asset Attack Surface Management (CAASM), Continuous Threat Exposure Management (CTEM), and traditional ASM is reshaping how security leaders stay ahead of threats. At the heart of this transformation is Asset Intelligence'the powerful result of combining automated asset inventory with artificial intelligence. AI is accelerating ASM capabilities by surfacing misconfigurations, uncovering hidden risks, and enabling faster, smarter remediation. Designed for IT and security professionals, this session features real-world examples from IT teams, MSSPs, and security-focused integrators who are gaining deep visibility and control over their risk surface — proactively strengthening their security posture before threats strike. you'll leave this session with ideas to help you: Build a unified, continuous approach to managing internal and external attack surfaces Detect misconfigurations and shadow changes before they become threats Use AI to prioritize risks and respond faster with smarter remediation If you're ready to get left of boom — and stay there — this session will show you how

### Assurance, Experience, and Insights: Building Digital Resilience - BRKOBS-1198
Speakers: Chris Crocco (Cisco), Robert Mandelbaum (Splunk / Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271980100001zL2s
Digital resilience is crucial for preventing potential disruptions to business operations, including exposure to security threats and revenue loss due to performance issues. This session will demonstrate how the combination of Cisco Networking and Splunk enables customers to integrate their infrastructure with Splunk's industry-leading platform. We will showcase how Assurance and Digital Experience Management, together with ThousandEyes and IT Service Intelligence (ITSI), are used to correlate network infrastructure performance across the enterprise.

### Assure Application and API Reliability in DevOps Environments with ThousandEyes - BRKAPP-2034
Speakers: Joe Dougherty (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272016309001zLFd
In our fast-paced world, the reliability of applications and APIs is foundational to delivering seamless and delightful user experiences. At the same time, visibility shrinking, and teams are finding themselves more are reactive to changes from both within their own organization and from external dependencies. This talk will provide strategies and tools essential for effective monitoring in our increasingly interconnected technology stack. We will explore how the transition to DevOps practices changes how approach ensuring reliability, the challenges of assuring uptime when you can't control what goes into every release, and practical insights into implementing robust monitoring of web pages, applications, and APIs using ThousandEyes.

### Assuring Touchless Payment Transactions at US Bank's Elavon with ThousandEyes - CSSOBS-1000
Speakers: DAVID SMITH (US Bank), Jason Warfield (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271874305001zl4S
Elavon, a subsidiary of US Bank, is a global leader in payment processing, handling $558 billion in transactions for over 1,000,000 merchants. Recently, Elavon and Delta Airlines partnered to offer Tap to Pay on iPhone across all US-based domestic flights. This allows travelers to simply tap their credit card or phone with a digital wallet to pay for meals and drinks. This micro-second, revolutionary process is assured by ThousandEyes. This is just one of the latest examples of how ThousandEyes provides digital resilience for the millions of Elavon transactions each day. During this session, learn from David Smith, Vice President/Manager, Core Network Engineering at US Bank, about: - Why Elavon and US Bank trust ThousandEyes to monitor and assure transactions over networks they own and don't own - An overview of the Tap to Pay on iPhone process and where ThousandEyes fits in - Future applications of ThousandEyes in the Elavon business

### AtlasIED: Technology Solutions for Safer Environments - VILCOL-1061
Speakers: Manny Kitagawa (AtlasIED)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271847487001zBrZ
This session will explain what AtlasIED IPX IP endpoints are, their technology and how they are an essential part of Singlewire's InformaCast notification application to provide a secure, productive, and efficient campus environment. Participants will learn how to deliver information to occupants in all areas of a campus with intelligible audio, legible text messages, and color coded visual signaling for normal, warning, and critical events. In addition, participants will learn how to use AtlasIED IPX IP endpoints as an interface to 3 rd party systems providing event automation for those systems that play a role in that occasion. Most importantly, participants learn how to leverage Cisco's UC network architecture as the foundation for the AltasIED and Singlewire Mass-Communication solution. Learning Objectives: At the end of this session participants will be able to: Comprehend the concept of Mass Communication and leverage Cisco's UC network architecture Recognize the advantages of Singlewire InformaCast notification application using AtlasIED IPX audio/visual IP Endpoints.

### Atomic Config Replace with Cisco Catalyst 9000 - BRKENS-2604
Speakers: Ashil Parekh (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921075001zF0i
Atomic Configuration and atomic config replace is becoming more and more requested, and this session dives deep into the newly introduced features within IOS XE and the Catalyst 9000 family. Being able to manage configuration in an atomic fashion allows teams to more effectively manage the change and network configuration drift. Using CLI or API the atomic config replace features will be demonstrated so that you can immediately benefit from leveraging either partial config or complete config replace. Easily replace ACL, policies, or interface configurations, or supply a complete config and that config will be set regardless of existing configuration.

### Authentication, Authorization and Provision for Cisco Collaboration, what is new? - BRKCOL-2007
Speakers: Paulo Jorge Correia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271855279001zjJY
We will understand the best practice to bridge identity between cloud and on-premises and will understand when and how to leverage the different protocols and mechanisms (SCIM, LDAP, REST API) to do provision of users. We will also explore the new directory services for cloud register and linked devices/clients. We will understand how SCIM 2 will allow Cisco to better interconnect to Cloud IdM's We will understand how the Cisco Webex Entra ID Wizard is going to improve the life of the collaboration administrators. We will understand what is new in Cisco Collaboration from an Identity prespective.

### Automate Catalyst Center with Cisco Workflows - BRKOPS-2379
Speakers: Keith Baldwin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988988001zAjn
Significantly reduce network deployment times and enhance accuracy through automation with Cisco Workflows. Cisco Workflows transforms network automation and orchestration. This innovative solution seamlessly integrates Cisco and third-party automation controllers using REST-API, PowerShell, and SSH. Cisco Workflows enables users to create comprehensive workflows for end-to-end orchestration across various products, such as automating a branch SD-WAN router, Catalyst switching, and Meraki APs, all within a unified network interface. This session provides an in-depth overview of the platform, demonstrating its capabilities with on-prem management platforms and showcasing complete network automation. Additionally, it highlights the benefits of a collaborative DevOps approach in overcoming deployment challenges and boosting operational efficiency. The session also showcases the integration of Cisco products with low-code/no-code solutions to streamline IT processes and enable seamless project deployment.

### Automate Everything: Simplifying Hybrid Cloud with Cisco + AWS Integrations - CNCGEN-1016
Speakers: Sanjay Popli (AWS)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271942992001zN4a
In today’s fast-paced digital landscape, simplicity, speed, and security are non-negotiable. That’s why Cisco and AWS have joined forces to help customers automate everything across their hybrid cloud environments. Through powerful integrations—like Cisco Intersight with AWS services, Cisco SD-WAN Cloud OnRamp, and unified security frameworks—this partnership delivers a seamless, policy-driven experience from on-prem to cloud. Whether you're modernizing applications, optimizing cloud connectivity, or securing workloads, Cisco + AWS help you reduce complexity and accelerate outcomes. Join us to discover how automation, visibility, and integration can empower your business to innovate faster, operate more efficiently, and scale with confidence.

### Automate SONiC configuration using Ansible - DEVNET-2990
Speakers: Suhaib Ahmad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271908899001z2fE
SONiC is an open-source Network Operating system based on Debian Linux. Open-PID Cisco 8000 series routers can support community SONiC as a Network Operating System. This session will introduce the configuration management system supported by SONiC. It will cover how SONiC supports configuration of network parameters using CLI commands, JSON configuration files, and other programmatic interfaces. The session will cover how attendees can automate configuration workflows using Ansible and introduce the Cisco SONiC collection available on Ansible Galaxy.

### Automate your NX-OS Data Center fabrics using Ansible, NETCONF and YANG - DEVNET-2143
Speakers: Gerard Sheehan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271900761001zCYi
NETCONF and YANG are quickly becoming the industry standard transport and encoding, to manage network fabrics. Come and see how you can manage your NX-OS fabric, from Day 1-N with NETCONF and YANG, using DIY in-house tools, or leveraging open-source tools such as Ansible.

### Automate, Manage, and Migrate Traditional 3-Tier vPC-Based Deployment using Nexus Dashboard - BRKDCN-2618
Speakers: Parth Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271883874001zod0
This session will focus on Automating and Managing Enhanced Classic LAN, known as traditional Three-Tier vPC-based Data Center Classic Ethernet networks, using Nexus Dashboard (ND). Learn how to deploy a Greenfield network using Nexus 9000 with built-in best practice configuration templates, or Brownfield import your existing vPC Data Centers using Nexus 7000 and Nexus 9000 into Nexus Dashboard. The session will also cover built-in automated workflows to deploy Classic Ethernet-based Networks and VRFs and the ability to hand off these Networks to the External domain using VRF-LITE. For customers looking to migrate to modern architecture with VXLAN BGP EVPN using Nexus 9000, this session will conclude with some highlights on the coexistence of Classic Ethernet and VXLAN Networks alongside the migration steps using Nexus Dashboard. A basic knowledge of Nexus Dashboard will be helpful.

### Automated Meraki switchport configuration copies for switch lifecycle replacement - CISCOU-1051
Speakers: Ed Novak (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271839100001zcqL
Are you facing the challenge of a Meraki switch lifecycle replacement? Are you daunted by having to copy all the switchport configurations to your new devices? This session will demonstrate how to simply and easily automate the coping of switchport configurations from one Meraki switch to another using Cisco Networking Cloud Workflows. Learn how Cisco Workflows can streamline operations by automating repetitive and error-prone tasks, resulting in significant time savings and reduced complexity. With a no-code/low-code development environment and a seamless drag-and-drop interface, Cisco Workflows enables automation across Cisco and third-party applications, enhancing accuracy and business performance.

### Automatic Discovery, Unmatched Visibility, Speed, and Context to Failure-Proof Your Kubernetes and Containerized Environments - BRKOBS-2012
Speakers: Greg Leffler (Splunk), Hemant Seth (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271981330001zVIz
Complex architectures make it harder to detect and resolve problems, and Splunk customers know this all too well. Still, we've helped customers reduce mean time to resolution (MTTR) by more than 90% even while managing more than 1,000 microservices, 6,000 hosts, and 15,000 containers thanks in part to Splunk Observability Cloud Infrastructure Monitoring capability and Kubernetes navigator. Kubernetes navigator is a turnkey, enterprise-grade monitoring solution for even the largest of Kubernetes environments that provides an intuitive way to understand and manage the performance of Kubernetes environments with an instant, comprehensive out-of-the-box hierarchical view of nodes, pods, and containers. Join us in this session to learn how Kubernetes navigator can help you failure-proof your Kubernetes environment to prevent service degradation and avoid downtime. We'll highlight: - Customizable dashboards and charts providing instant visualization of Kubernetes objects, their health, and their performance. - Easy-to-understand interactive cluster maps that help you easily understand and explore interdependencies. - New features designed to help streamline Kubernetes troubleshooting

### Automating Cloud Security: From Legacy Solutions to Agile Application Protection - DEVNET-2801
Speakers: Brennan Bouchard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912201001ziLw
Is your company transitioning applications to the public cloud and relying on outdated on-premises security solutions? Are you struggling to adapt these traditional solutions to secure more dynamic application stacks deployed in Kubernetes and serverless environments? If so, this session is designed for you. In this session, we will demonstrate how to secure applications either being migrated to, or built natively in the public cloud using automation. We will begin by discussing deployment models, such as Centralized and Distributed, to determine appropriate firewall placements, like Firewall Threat Defense (FTD) or Multicloud Defense. Next, we will explore securing workloads, focusing on segmentation and visibility options for cloud instances, containers, serverless applications, and Database as a Service (DBaaS) backends, utilizing emerging technologies such as Hypershield, Isovalent, Panoptica, and Secure Workload. By leveraging the visibility and telemetry from these solutions, we can enhance our data and streamline our Incident, Threat, Detection, and Response (ITDR) processes through integration with Splunk and Cisco XDR. Finally, we will review options for automating the entire architecture into a secure CI/CD pipeline.

### Automating Diverse Multi-Domain Networks End-to-End - BRKOPS-2544
Speakers: Chad Hill (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271987025001z60y
Whether Enterprise, Data Center, or WAN, organizations face challenges in streamlining automation approaches that transcends typical IT domain silos, especially in multi-domain and heterogenous environments. This session will dive into how Cisco Network Services Orchestrator (NSO) can transform network automation for organizations operating across diverse domain environments, requiring flexible, adaptive solutions. By exploring real-world use cases, attendees will gain insights into a service-oriented design approaches for multi-domain network automation. From the initial device provisioning to end-to-end service data models and common network operations tasks, this session will provide lessons learned and strategies to accelerate your automation journey.?

### Automating Micro-Segmentation and Deploying Layer 4-7 Services in VXLAN EVPN Fabrics using Group Policy Option (GPO) and Nexus Dashboard - BRKDCN-2909
Speakers: Alessandro De Prato (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271887696001zaSk
Macro and Micro Segmentation are key design strategies for securing any data center. This session describes the new segmentation capabilities introduced in NXOS VXLAN EVPN fabrics to enhance the security posture inside the perimeter of the data center. You will learn about security groups, security group ACLs, and how they leverage VXLAN Group Policy model to classify endpoints dynamically. Participants will learn how contracts can be used to allow or deny undesired traffic, and to implement a zero-trust model where endpoints can only communicate with other endpoints as per allowed policies. This session will cover the various use cases and techniques network operators can leverage to divide the data center into distinct security zones and enable workloads to communicate regardless of where these applications reside within the network. This session will also contain few live demos to highlight the automation and management functionalities offered by Nexus Dashboard to enable micro-segmentation traffic enforcement in the DC. Prior knowledge of VXLAN EVPN and Nexus Dashboard will be beneficial. Those interested in the underlying architecture of GPO, including an in depth understanding on how the control and data planes operate, should consider attending BRKDCN-2633 before this session.

### Automating Network Compliance with Cisco's Network as Code - BRKOPS-1388
Speakers: Greg Leider (Cisco), MICHAEL WYNSTON (FISERV)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985796001znlm
Network operators today are faced with the challenge of operating networks at scale. Various methods have been developed over the years for automation. In the past years a new method has been brought from the management of cloud infrastructure known as Infrastructure as Code. This capability allows the ability to introduce software discipline into network operations. The incorporation of a single source of truth allows you to incorporate direct compliance across your network devices. With this known data model that represents your network you can then simplify how automation is executed. Cisco has developed a capability known as Network as Code, which is available across many architectures, which incorporates these elements to allow you to manage network change. Join us for this session where we will go in-depth showing how to accelerate automation in your network and provide best practices in the following areas: 1) Building a trusted network source of truth in a source code repository 2) Building a digital twin or suitable test environment for your network 3) Implement software development lifecycle (SDLC) best practices for infrastructure management 4) Build Vertical Automation specific to technology domains and protocols 5) Build Horizontal Automation to ensure security compliance, regulatory adherence, and consistent user experience Reference: https://netascode.cisco.com/

### Automating Network Compliance: Leveraging Cisco NSO for Compliance Auditing, Reporting, and Remediation - DEVNET-2144
Speakers: Chad Hill (Cisco), Gavin Littleboy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271900949001z4A6
This session explores the challenges and real-world solutions to meet organizational standards and industry compliance regulations for networks. Participants will discover how to leverage Cisco Network Services Orchestrator (NSO) compliance reporting to audit network configuration using compliance templates. The session dives into the evolution of auditing to automating network configuration baselines for standardized network deployments. Participants will understand how these tools facilitate continuous compliance checks and remediation of non-compliant configurations. By exploring real-world examples to illustrate the implementation of these strategies, participants can gain valuable insights into increasing security posture and meeting compliance needs for networks.

### Automating Root-Cause Network Troubleshooting - CNCTRS-2000
Speakers: Tim Titus (PathSolutions)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271935952001zAnw
Most NetOps teams spend the majority of their time troubleshooting network glitches and problems that occur throughout the network. There is a lot of information that needs to be manually collected and analyzed to arrive at a root-cause resolution. If you were able to know everything your network equipment knew, you could proactively troubleshoot the problems before users complain about impacted services. Join this session and learn about how to automate collection of information throughout the network, and how to automate the analysis of the information to arrive at plain-English, root-cause resolutions.

### Automating Vulnerability Intelligence for Network Security - VILENS-2002
Speakers: Amar Ramakrishnan (BackBox)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271918954001ztzS
Managing vulnerabilities in complex networks remains a significant challenge, requiring effective remediation strategies. The vast amount of CVE data from various sources often overwhelms IT and security teams, making prioritizing and resolving critical threats a significant hurdle. This session examines how the Cisco and BackBox integrated solution offers vulnerability intelligence alongside no-code automation, risk scoring, vulnerability remediation, and change monitoring to assist organizations in streamlining vulnerability management, mitigating risks more effectively, and significantly enhancing their overall security posture.

### Automation Advocacy: Bridging the gap from Ops to DevOps - DEVNET-2237
Speakers: Allison Estes-Smargiassi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271902098001zwzZ
You're all in on automation - you've learned every tool you can get your hands on and have started automating some of your own tasks. Now what? Maybe you have big plans - new tools to implement, scripts to write, pipelines to build - but now you need buy-in from the rest of your team. Going from small one-off automation to automations at scale takes lots of time and effort, which can be a tough sell in the fast pace environments that many teams face, where it's easier to keep doing things the way they've always been done. In this session, We'll be sharing the automation journey of DevNet Sandbox over the past 3 years with a specific focus on how we got the ball rolling. We'll talk about the paradigm shift from Ops to DevOps, as well as some tips and tricks we've found to ease into that transition.

### Automation After the Honeymoon Phase - BRKOPS-2849
Speakers: Colin Lacy (Cisco), Julia Clarke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271987411001zKtF
Automation is essential for scaling network operations, but what happens when your tools reach Day 2 maturity? Beyond the initial benefits, maintaining and evolving automation to meet changing business needs presents unique challenges—challenges often overlooked in the rush to implement. This talk dives into the realities of Day 2 automation. We'll explore real-world examples of issues like skills gaps, technical debt, and tightly coupled scripts that can hinder progress. Learn how to adapt and future-proof your automation efforts by fostering collaboration between engineers and business stakeholders. You'll gain insights into making your tools more durable, flexible, and aligned with evolving business priorities. Discover why the key to long-term automation success lies less in the tools—like Python, Ansible, and Terraform—and more in the people driving their use. If you're a network engineer with experience in automation and an operations focus, this session will give you actionable strategies to thrive in a Day 2 world.

### Automation and In-Depth Troubleshooting of Cisco Catalyst 8000, ASR 1000, ISR, and SD-WAN Edge - BRKTRS-3475
Speakers: Frederic Detienne (Cisco), Olivier Pelerin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271937084001zkiD
In this session, we will start by explaining the architecture of the Cisco Catalyst 8000, ASR 1000, and ISR in autonomous / SD-routing / SD-WAN Edge mode. With this knowledge, we will gain in-depth understanding of traffic forwarding and advanced feature processing. We will also introduce RADKit, a troubleshooting automation tool, to accelerate network-wide or complex data capture. We will demonstrate problem isolation and root cause analysis on a live, feature-rich network such as routing, QoS, IPsec (FlexVPN and SD-WAN), and NAT.

### Automation and Orchestration Strategies for the Cloud-First Enterprise - BRKCLD-1444
Speakers: Arvind Kumar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845570001zlfr
As digital transformation is at the forefront in securely enabling applications to run anywhere, adopting a cloud mindset is necessary for simplifying how we build, manage, and operate an agile infrastructure that can meet demands. Automation and orchestration capabilities are essential to leverage for common tasks and workflows, which are enabled on a programmable stack that extends from on-premises into the cloud. Popular trends such as SASE, 5G, AI operations, and cloud-native application architectures are accelerating, and a DevOps and CloudOps integrated approach can simplify operations, implementing cloud-scale changes with predictable results. This session will provide a view into the automation framework and tools recommended to get started, as well as how to orchestrate workflows across multi-domain environments. It will highlight how simplicity drives a reduction in OpEx. The session will also discuss emerging concepts related to SASE, hybrid cloud, enhanced observability with analytics, and closed-loop automation. Practical examples from enterprise customers will showcase how automation and orchestration are put into action, with insights and best practices from the customer experience team.

### BGP EVPN in Enterprise Campuses with Catalyst 9000 Series Switches - BRKENS-2092
Speakers: Raj Kumar Goli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271920082001zAdU
This session will cover the enterprise BGP EVPN solution in the campus using Catalyst 9000 platforms. We will discuss the major drivers behind the adoption of the technology, supported features, interoperability between other Cisco platforms, and different design considerations when it comes to deploying it in production. This session is more focused on design considerations from an enterprise network perspective. During the session, we will also cover some best practices, newly added capabilities, and enhancements to the solution.

### Because "It's the Network's Fault" Shouldn't Be Your Default Answer - CNCOBS-2000
Speakers: Surbhi Paul (Gigamon)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271974075001zFgq
Tired of being caught in the blame game every time an app slows down - only to prove otherwise after hours of troubleshooting? What if your app and security teams could see what you see, right from their SIEM or observability tools? Come and see how you move from reactive firefighting to proactive assurance by: Gaining complete visibility into East-West lateral traffic—including container-to-container and IoT/OT communications—across your hybrid cloud. Leveraging Layer 4–7 network-derived telemetry to detect performance bottlenecks and threats early, from port spoofing and shadow IT to unsanctioned AI use. Empowering app and security teams with the network intelligence and insights they need to validate root causes—so you can finally retire the default blame game. Let’s turn the network into your greatest ally, not the usual suspect.

### Beginner's Guide to ThousandEyes - BRKENT-1656
Speakers: Primoz Kolman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271930920001zXrU
Your company relies on various connectivity options to ensure all your locations can connect over the same network. Your business-critical applications are migrating into the cloud and you rely on internet connectivity to process critical workloads. Your IT and networking teams are working on SD-WAN and SASE implementation, but are burdened with incident management , spending a great deal of unproductive time in war rooms, avoiding accountability, and struggling with inefficient tools . ThousandEyes plays a central role in identifying the source of critical performance degradation incidents . You will learn how ThousandEyes can help you gather and visualize data across application and network layers and quickly identify the source of critical incidents.

### Behind the Curtain: AI, Infrastructure & Operations Inside Cisco - ITLGEN-2068
Speakers: Harinath Nagarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272018637001zQuP
As AI becomes essential to meaningful and sustainable business transformation, the Infrastructure and Operations that supports it must evolve — intelligently, securely, and at scale. In this leadership session, we will take you behind the curtain of Cisco's own infrastructure journey: how we modernized our infrastructure, supercharged operations, and scaled AI Infrastructure and Platform services leveraging Cisco and leading-edge technologies. Discover how Cisco developed an enterprise reference architecture for AI Infrastructure that provides high-performance and future-ready AI networks and compute with pervasive security, real-time telemetry, and common AI services that make it easier for teams to develop, deploy, and run AI workloads. This session will showcase key strategic insights from Cisco's journey, providing a playbook for leaders looking to unlock the full potential of AI, Infrastructure & Operations.

### Best Practices around organizing your teams to respond to events your environment - CTF-1032
Speakers: Michael Lipsey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271984234001zyVD
Managing events and notifications from various sources is crucial for maintaining operational efficiency and responsiveness. This session will explore effective strategies and tools for consolidating and managing notifications from diverse systems, ensuring that critical information is not lost in the noise and that your teams are able to both prevent and respond issues that could lead to downtime.

### Best Practices for Compute Connectivity with the 6th Generation Fabric Interconnect - BRKCOM-2658
Speakers: Joost Van Der Made (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861189001zGAx
This session will explore the latest advancements and fabric features of the 6th generation UCS Fabric Interconnect (FI). Attendees will learn about Intersight best practices for optimizing compute fabric, storage, including the integration of Fibre Channel (FC) and NVMe Over Fabric protocols. This session will provide practical guidance on leveraging these innovations to improve performance and scalability in your data center. Delve into the intricacies of this cutting-edge technology and understand its potential advantages for your Cisco UCS environment. This session will cover details and best preactices for: - The 6th Generation Fabric Interconnect - Interisght Domain Profile for the 6th gen FI - Intersight and 6th Gen FI with Storage Protocols.

### Best Practices for Troubleshooting Cisco Catalyst 8000 Edge Platforms - BRKTRS-2572
Speakers: Michal Stanczyk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271936697001zK7f
In this session, attendees will learn various techniques and tools used by Cisco TAC experts to diagnose Cisco Catalyst 8000 Edge Platforms effectively. The session is crafted to provide practical solutions to everyday challenges in the field, including common issues related to system performance and packet forwarding. Relevant serviceability capabilities that help reduce the time to identify the problem will be also covered. Participants will walk away with actionable guidance that can be immediately implemented in their day-to-day job.

### Best Practices for Webex Meetings and Webinars - BRKCOL-2083
Speakers: Iain Buck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271852815001zrha
The ability to effectively conduct virtual meetings and webinars is crucial for business success and organizational communication. This session offers guidance on best practices for leveraging Webex Meetings and Webinars, focusing on three critical phases: pre-meeting preparation, meeting production, and post-meeting activities. Participants will gain insights into planning techniques to ensure seamless execution, including the optimal setup of meeting agendas, participant management, and technical configurations incuding registration, customisation and Branding. During the meeting production phase, emphasis will be placed on engagement strategies, leveraging advanced Webex meetings & Webinars features such as Stage Manager, AI assistance, accessiblilty, translation and Interpretation. Finally, the session will explore the importance of post-meeting analysis through comprehensive reporting and follow-up activities, which are essential for evaluating meeting effectiveness, driving continuous improvement, and fostering ongoing engagement. This session is designed for people seeking to elevate their virtual meeting capabilities and deliver impactful, results-driven virtual experiences.

### Best Practices of Virtual Port Channel in VXLAN EVPN Fabrics - BRKDCN-2912
Speakers: Parth Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271888075001zwfe
This session will focus on vPC (Virtual Port Channel) in the context of VXLAN BGP EVPN Data Center deployments. The attendees will learn different models of vPC, including Fabric peering and the distribution of BGP EVPN control-plane in advertising the host and network routes behind a vPC VTEP, alongside examples of packet walks. Furthermore, the session will cover configuration best practices to fine-tune the VXLAN VTEP convergence while using vPC. Lastly, we will conclude the session by exploring use-cases of vPC Border-Gateway in managing Data Center Interconnect (DCI) using Multi-Site and the ability to manage and simplify the automaton with the help of Nexus Dashboard.

### Beyond DMARC: Full-Spectrum Domain Defense Against Impersonation Attacks - VILSEC-1051
Speakers: Brian Westnedge (Red Sift)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271991900001zaRK
Email remains the primary entry point for cyberattacks, with domain impersonation evolving beyond simple spoofing. While DMARC (Domain-based Message Authentication, Reporting & Conformance) is a crucial first step, attackers now leverage lookalike domains and DNS misconfigurations to bypass traditional security measures. This session explores the current state of domain-based threats, why a layered defense strategy is essential, and will provide ideas to help you: Implement a "full-spectrum" domain defense strategy: Participants will learn how to combine DMARC enforcement with DNS monitoring and brand protection to create a robust defense against both exact-domain spoofing and lookalike domain attacks. Identify and mitigate DNS misconfigurations: The session will cover common DNS vulnerabilities, including subdomain hijacking, oversized SPF records, and dangling CNAME records and how these misconfigurations can be exploited by attackers to bypass authentication and send phishing emails from legitimate subdomains. Detect and take down lookalike domains: Participants will gain insights into how attackers create deceptive variations of domains and how these lookalikes are used in phishing campaigns and fraud, and understand the importance of brand monitoring and automated lookalike assessment using AI-powered risk scoring. The presentation will ultimately demonstrate a layered domain defense solution that combines Domain Protection by Red Sift OnDMARC and Red Sift Brand Trust and how these SolutionsPlus offerings work together to provide comprehensive protection.

### Beyond GPUs: Essentials of Gen AI, Networking Backbone & Best Practices for AI Success! - AIHUB-1015
Speakers: Siva Kanth Sattiraju (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271876846001z39O
Training large language models (LLMs) is a high-stakes process where even a single dropped connection can derail an entire training run, wasting days of compute time. Success hinges not just on GPU power but on a robust networking infrastructure backbone that ensures seamless communication across distributed clusters. Our team of engineers utilized Nexus 9000 Series switches provisioned and managed by Nexus Dashboard to train and fine-tune frontier large language models and run inference workloads across distributed clusters of GPUs. Drawing from best practices and defensive publications authored by the speaker — this session discusses the essentials of Gen AI, an overview of the AI/ML backend networking fabric and Best Practices for building successful AI applications.

### Beyond Limits: The Innovative Journey of Industry 4.0 - BRKIOT-2019
Speakers: Kevin Wood (Cisco), Luke Biroldi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271952973001zPh4
In this session, we will explore Industry 4.0's transformative impact on modern industries and the limitless possibilities it unveils. We will delve into the key technologies driving this change, such as the Internet of Things (IoT), Industrial Security and Visibility, Industrial Segmentation, Artificial intelligence (AI), and Big Data analytics, and discuss how they synergize to enhance productivity efficiency, and innovation. We will highlight the Industrial Network, which is an enabler to take advantage of this competitive inflection point. Walk away from this session with a picture of a reference architecture based on Cisco Validated Designs.

### Beyond MCP and A2A: How Cisco is building the Internet of Agents with LangChain, CrewAI, Galileo, and MongoDB - PSOETI-1113
Speakers: Papi Menon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271914510001zbwr
How Cisco is helping to build an open, interoperable Internet of Agents with standard methods for discovering and managing Agents across a variety of frameworks and platforms.

### Beyond Wi-Fi: Enable your IoT Solutions with Cisco Wireless - BRKEWN-1266
Speakers: Christopher Williams (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271938260001zgM3
Come learn about how Cisco's wireless portfolio (on-prem and cloud managed) is able to meet the demands of the IoT landscape by allowing Cisco Wireless Access Points act as edge computing agents. As more IoT applications are being served as containerized applications, APs need to be able to sandbox an application and isolate it from the rest of the AP's software. By isolating computing resources for hosted applications and leveraging relevant IoT protocols directly on APs, customers can unlock the latest Cisco-proprietary and partner-integrated IoT solutions for Asset Tracking, Environmental Monitoring, and Workspace Optimization.

### Beyond the Call Center: Turning Conversations Into Business Intelligence with AI - VILCCT-1011
Speakers: Gennadiy Bezkorovayniy (MiaRec)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271862717001zwww
Today's contact centers generate vast amounts of customer data — but most of it goes untapped. With the rise of artificial intelligence (AI), organizations can now analyze every conversation across channels to gain deep, actionable insights. This session explores how AI-powered conversation analytics solutions like MiaRec transform these interactions into business intelligence that drives enterprise-wide impact. You'll leave this session with ideas to help you: • Use AI to automatically evaluate agent performance and track customer experience metrics such as Net Promoter Score (NPS) and Customer Satisfaction (CSAT). • Detect trends, uncover root causes of customer issues, and reduce churn through proactive insight. • Extend the value of conversation analytics beyond the contact center to sales, product, and operations teams. This session is ideal for customer experience leaders, contact center managers, and IT professionals interested in practical, scalable ways to apply AI across the customer journey. No advanced technical experience is required.

### BlueCat and Cisco: Integrate, Automate, Protect and Analyze for Secure Networks - CNCSEC-1007
Speakers: Christopher Smithee (BlueCat Networks Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271994019001zz7k
Modern network complexities can introduce security risks, operational risks, and create huge operational expense on your organizations when not properly managed. Operational health of your network depends both on proper planning and management as well as active monitoring to reduce risks. During the session, participants will learn how BlueCat's helps you augment your Cisco implementations to address modern network issues and: Prevent Network and Security risk through proper planning and leverage automation to reduce new risks. Detect malicious activity and configuration issues before they create new problems Respond by limiting access of malicious hosts once detected and providing an audit of activity for forensic investigation

### Boost Mobile's Journey Toward Reduced Risk and Improved Automation with a Network Digital Twin - CNCCLD-2005
Speakers: Sumugam Balachandran (Boost Mobile), Nikhil Handigol (Forward)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272018442001zS6c
In the fast-paced world of telecom, achieving reliable, high-performance connectivity while maintaining operational efficiency is a continuous journey. In this session, gain an inside look at Boost Mobile’s ongoing transformation as it deploys a Network Digital Twin in a 5G Open RAN cloud-native environment—advancing resiliency, automation, and intelligent operations. This groundbreaking initiative is already demonstrating early momentum, enabling Boost Mobile to simulate network changes, proactively address risks, and streamline lifecycle management. Learn how the team is embedding this technology into daily operations to improve agility and drive efficiency across the board. What You’ll Learn: • How Boost is utilizing a single source of network truth to accelerate troubleshooting, streamline escalations, and plan changes more effectively • Integration with Incident Management systems to automate incident triage and enhance root cause analysis • Early gains from intent-based verification—with a forward-looking goal of exiting change windows with a fully verified, healthy network Whether you're just beginning your automation journey or looking to evolve operational models, this session offers real-time insights and practical strategies from Boost Mobile’s path toward smarter network operations.

### Boosting Customer Experience with Flow Orchestration in Webex Contact Center - BRKCCT-2345
Speakers: Krishna Tyagi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271865809001z9gu
Tired of complex contact centre environments and slow time-to-value? This session introduces Webex Contact Center Flow Orchestration—designed for simplicity, adoption, and speed. Built natively to integrate with data, APIs, digital channels, and automation. Flow Orchestration empowers businesses to achieve superior customer and agent experiences, faster. See how it simplifies administration, monitoring, and real-time tracking and actions for supervisors. This 1.5-hour session provides an in-depth, yet easy-to-follow, exploration of recent advancements in Webex Contact Center capabilities—your key to crafting superior customer journeys. We'll cover basic and advanced features, including the latest admin-friendly enhancements, giving you a comprehensive understanding of how to exceed business objectives without complex coding. Participants will: Discover advanced features and the newest Webex contact Center updates that enhance functionality and flexibility with real-world use cases. Learn best practices and practical tips for designing, implementing, and managing effective contact centre flows with minimal effort. Join us to transform your contact centre's customer experience with the power of Flow Designer in Webex Contact Center

### Border Gateway Protocol Fundamentals - BRKENT-1179
Speakers: Gustavo Sibaja (Cisco), Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271932827001zy7D
Border Gateway Protocol (BGP) is the glue that holds the entire internet together, and it is just as crucial in service provider networks and data centers, too. Because of this, BGP has become one of the few must-know protocols. Over its 30 years of existence, BGP has grown vastly in its capabilities but its fundamentals remain the same. It is precisely BGP's core that this breakout session targets, but don't confuse "fundamental" with "simple." The goal of this session is to cover BGP's principles while focusing very strongly on the WHY of things. With the solid foundation this session seeks to build, it will later be easy to understand the current extensions and applications of BGP, ranging from service provider deployments through Ethernet VPNs. This is definitely NOT your grandpa's crash course on BGP. NOTE: For maximum benefit, a working knowledge of TCP/IP and basics of IP routing is strongly recommended.

### Break Down the Walls: Unify IT and OT Cybersecurity with Cyber Vision and Splunk - PSOIOT-1042
Speakers: Andrew McPhee (Cisco), Paul Pelletier (Splunk/Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271952160001zVNT
As cyber threats keep growing, manufacturing, energy, and transportation industries face an urgent battle to protect industrial operations. Managing OT security in isolation is no longer viable. How can IT build on security tools and skills they already have and help the line of business protect their industrial settings? What are Cisco and Splunk doing to help unify IT and OT security to better protect the global enterprise? Join this session to learn how Cisco can secure industrial networks at scale: • What's new in Cisco Cyber Vision and how does it bring OT context to existing IT security tools? • How to use Cisco ISE or Secure Firewall to automate industrial network segmentation and better protect operations? • What is the SOC of the future and how can Splunk help unify threat detection across IT, OT and Cloud?

### Breaking Organizational Silos and Building Customer Trust - ITLGEN-2056
Speakers: Dev Stahlkopf (Cisco), Fletcher Previn (Cisco), Carrie Palin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959040001zQhN
Building an effective AI and Data strategy is a team sport, requiring collaboration across multiple teams and skillsets. Join members of the Cisco senior leadership team for a candid conversation about solving the multidisciplinary challenges of the AI era, focusing on the critical themes of strategy, operations, and governance. The session aims to help leaders in IT think cross-functionally as they work to align their organization's AI and data initiatives with business goals, emphasizing scalability, resilience, and safety in the evolving technological landscape.

### Breaking the Identity Provider Mold with Duo - BRKSEC-2082
Speakers: Clayton Ballreich (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271999946001zFUj
So many identity providers, so little time. Organizations struggle with identity sprawl, often because of mergers, acquisitions, or new technological demands. Identity providers in the market are commonly focused on selling their solutions and instructing customers to fit their molds. What if there was a better way? With Duo Directory, customers can federate their applications to one source, simplifying their identity infrastructure and reducing management overhead. Want the flexibility to onboard users with or without a password? Want the ability to simplify the end user authentication experience? Duo has you covered. Participants in this session will: Learn the capabilities of Duo Directory Discover what business challenges Duo Directory helps solve Understand how Duo Directory can help consolidate multiple or migrate from other identity providers Participants can expect demonstrations of Duo Directory functionality, the end user experience, and how to work with or migrate from other identity providers. An understanding of what an identity provider does, how to federate applications to an identity provider and experience working with end user authentication is expected for this session.

### Bridge to the Skies -- How to securely connect to your workloads in the cloud with Meraki SD-WAN - BRKENT-2087
Speakers: Juan Sterbenc (Cisco), Simarbir Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271970249001zWzM
Organizations are rapidly adopting Public Cloud strategies for ease-of-deployment, scalability and cost optimization. To ensure proper cloud integration, network engineers need to guarantee best-in-class connectivity and security for the deployed workloads. There is a myriad of technologies involved in this process, normally from different vendors, that only increase complexity. Additionally, Public Cloud networks often do not follow the same traditional on-prem networking constructs, leading to poor implementations. In this session, we will show you how Cisco Meraki can bridge these gaps while maintaining simplicity and security. You will learn about the latest vMX innovations around cloud security and interconnectivity, we will go over validated designs for every public cloud vendor and learn how to deliver high-availability, scalability and security.

### Bridging the Gap: Integrating Identity Security Across Platforms - BRKSEC-2910
Speakers: Jeremiah Williams (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272005256001zQbn
The application and enforcement of identity and security controls vary significantly by platform, creating challenges when addressing emerging threats. Discover how Cisco's Duo and Identity Intelligence (CII) streamline identity security integrations, offering a consistent experience for both administrators and users across diverse platforms, while addressing the distinct needs of each group. This session tackles the real-world challenges organizations face in enforcing identity security controls across multiple systems, such as single sign-on, passwordless authentication, device identity and hygiene, and policy-based access controls. We will delve into the critical roles of identity security posture management (ISPM) and identity threat detection and response (ITDR). Designed for practitioners with a foundational understanding of Identity and Access Management (IAM), this technical session features engaging demonstrations of Cisco's solutions, illustrating effective practices before, during, and after authentication. Participants will leave with actionable strategies to ensure seamless and secure experiences across all platforms, gaining valuable tools and insights for navigating evolving identity threat landscape.

### Bridging the Gap: Unlocking the Power of OT Skills in the Digital Age - CISCOU-1050
Speakers: James Risler (Cisco), Mai Vang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271838901001zmpQ
Join our 30-minute session to discover how the convergence of Operational Technology (OT) and Information Technology (IT) is revolutionizing industries. Learn the essential OT skills needed to drive innovation, enhance safety, and optimize processes across sectors like manufacturing and energy. Equip yourself to bridge the OT-IT divide and future-proof your career in the digital age.

### Bringing Network Detections and Visibilty to Splunk - BRKSEC-2928
Speakers: Eric Rennie (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272005447001zBov
This session will include material that explains how Secure Network Analytics brings network detections to Splunk enterprise security. The session will cover use cases of the solutions as listed below: • Response Management - Secure Network Analytics using syslog to send to Splunk - Secure Network Analytics using webhooks to send to Splunk • Pivoting o Secure Network Analytics pivoting directly to Splunk with external lookups o Splunk pivoting directly to Secure Network Analytics • Cisco Security Cloud (CSC) App - Using the CSC App to populate network telemetry from SNA into Splunk - Using the CSA App as technical add on to generate notables in Enterprise Security • Splunk Enterprise Security - Using correlation rules (SPL) to populate Enterprise Security and Risk Based Alerts (RBA) for Secure Network Analytics alerts that contain MITRE context. This session will allow the participants to learn how we bring network detections and visibility from SNA to Splunk.

### Build Future-Ready Branch Networks with Next-Gen Secure Routers - PSOENT-1023
Speakers: Pratik Desai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271927818001z3tB
As businesses evaluate how to manage the explosion in AI-related branch traffic and cyber threat actors, Cisco Secure Routing is leading the way. Learn how Cisco empowers enterprises to shrink risk, boost network reliability, and strengthen future-readiness. Discover how Cisco redefines future-proofed workplaces with platform-level security, advanced performance engineering, and management flexibility.

### Build a More Sustainable Network: The Journey from 'As-is' to 'To-be' - BRKGRN-1021
Speakers: Jaypal Baviskar (Cisco), Afshan Sabha Mulla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271946670001ztjM
Although 72% of companies believe climate change possesses risks that could significantly impact their operations and revenue, only a small fraction have developed methods and tools to evaluate the progress of their actions towards Sustanability goals. In this session we will discuss the practical strategies an organisation could adopt to help improve sustainability in IT. The session will focus on how Cisco's products, platforms, services and solutions can help support their sustainability journey. The session will describe the 'as-is' network of a customer scenario and how they could transform to a more sustainable 'to-be' network, using elements like Intersight Workload Optimizer (IWO), network virtualisation, product integration, automation, cloud networking offerings etc.

### Build the Future-Proof Workplace with One Cisco Enterprise Switching - PSOENT-1019
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271927055001zLDA
Enterprises need scalable, secure, and intelligent network infrastructure to power AI, smart buildings, hybrid work, and seamless collaboration. Cisco switching solutions deliver unmatched performance and security, empowering organizations to connect and innovate across campuses, branches, factories, and beyond.

### Building Autonomous networks journey with Cisco Crosswork Network Automation - BRKSPG-2870
Speakers: Deepak Bhargava (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271965039001zbI1
Faced with increasing operational costs, Service Providers and Enterprises are challenged with cost-effective delivery of network services meeting the target SLAs. Network programmability, SDN control and closed loop automation are the key building blocks to help streamline and simplify operational processes, drive operational agility and keep the costs at bay. The session offers you a deeper insight into Cisco Crosswork Network Automation and how you can utilize it to gather actionable insights, streamline actions to automate time-consuming operational processes, and realize the journey towards Autonomous networks. This session focuses on automation use-cases that such as service and transport provisioning, real-time network optimization, traffic congestion mitigation, large scale software upgrades, and programmable workflows for closed loop actions. The session will include demonstrations highlighting how you can improve your operational agility.

### Building Digital Equity with Fiber-based Network Connectivity, Wireless, IoT and Local Governments - CSSEWN-1020
Speakers: Joe Webster (Montgomery County Government), Kenya Asli (City of Baltimore), Meghan Steele (Cisco), TJ Mayotte (Howard County Government)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271875488001zQ9x
In today's interconnected world, equitable internet access is vital for education, economic growth, and community well-being. Local governments are increasingly leveraging advanced wireless technologies to bridge the digital divide, ensuring communities enjoy reliable and inclusive internet access. This session delves into how various cities and counties are utilizing Cisco Ultra-Reliable Wireless Backhaul to promote digital equity across diverse populations. This fireside chat will discuss: Montgomery County's low-income and special needs 300Mbps/300Mbps free internet service ("MoCoNet") in residential developments with built-in Wi-Fi to enable connected living Baltimore City Broadband and Digital Equity that supports strategy development Howard County's implementation of wireless internet across public spaces and parks to enhance community connectivity Attendees will learn how local governments use fiber-based network connectivity, IoT and wireless backhaul technologies to develop effective digital equity initiatives and integrate in-home and wireless infrastructure into public projects.

### Building End-to-End a Full-stack AI-Optimised Data Centers: Architectures and Best Practices - BRKCOM-2115
Speakers: Roger Dickinson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271860439001zeI4
In this session, you will learn about the end-to-end architectural recommendations and the best practices for designing a High-Performance data centers for AI workload. This session into the integration of high-performance computing, ultra-low-latency networking, and high-speed storage solutions tailored for AI applications. Attendees will gain insights into scalable designs that accommodate the unique demands of AI, ensuring efficiency and performance

### Building Incident Response Actions for Meraki using Cisco XDR Automation - DEVNET-2057
Speakers: Awais Khan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271898844001zTNV
XDR automation allows you to run powerful workflows in the cloud to automate how your organization investigates and responds to the threats. You can use our built-in playbooks, import from cisco or build your own custom workflows from scratch. This simplifies and accelerate security operations by acheiving End to End Automated Threat Detection & Response. Join us in this session to learn how to create XDR workflows from the scratch using a no-to-low code approach and how you can use Meraki API's inside those workflows to control and restrict the comprised users or devices on the Network infrastructure.

### Building Multi-Agent Systems with AGNTCY - DEVNET-2028
Speakers: Cody Kai Hartsook (Cisco), John Parello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271898106001zbud
AI is reshaping software development — and the next leap is building systems made of many collaborating agents, not just single models. In this session, We'll shift slightly from the broader AI trends originally previewed and dive into AGNTCY.org, an open-source project for building and deploying multi-agent systems. We'll explore the AGNTCY architecture and its core components — the Agent Directory, Open Agent Schema Framework (OASF), and Agent Connect Protocol (ACP) — and walk through a live sample application showcasing real-world multi-agent interactions. We'll also compare AGNTCY to other emerging open-source efforts, including Model Context Protocol (MCP) and projects from other players in the agent ecosystem. Whether you're new to multi-agent design or already experimenting, this session will give you a clear, hands-on foundation for building the next generation of AI-powered systems.

### Building Resilient Security Postures for Cloud and Applications in the AI and Multicloud Era - BRKSEC-2171
Speakers: Pascale Delaunay (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272008234001zNZn
As organizations adopt multicloud strategies, the complexity of their security landscapes grows. This session is crucial for navigating these challenges, offering guidance to build resilient security postures for cloud environments and applications in the AI and multicloud era. This session will cover Cisco's comprehensive security solutions, powered by AI and ML, including Security Cloud Control, to navigate this terrain. Attendees will gain insights into the evolving threat landscape across network, cloud, application, and AI security, highlighting differences and similarities between tools in each domain. The session focuses on best practices for building a resilient security posture, emphasizing AI-powered solutions, zero-trust frameworks, and securing cloud-native applications, APIs, and AI models. Understanding the unique challenges and intersections of these domains allows organizations to develop comprehensive security strategies that protect assets and minimize risk. Attendees will receive actionable advice to enhance their security measures immediately and learn how to implement a zero-trust model effectively. By attending, you'll gain insights into cutting-edge trends, empowering you to build a resilient IT environment in the AI and multicloud era.

### Building Secure AI Infrastructures - CENDCN-1359
Speakers: Jake Katz (Cisco), Murali Gandluru (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592612950001Xjjb
As organizations accelerate AI adoption, networking complexity and security concerns remain primary barriers to successful deployment. AI workloads demand specialized networking architectures that can handle massive data flows while maintaining enterprise-grade security and observability. This session explores how modern AI networking solutions address these critical challenges. Learn how simplified lifecycle management and intelligent automation can reduce operational overhead while ensuring optimal performance for AI workloads, and discover approaches that provide unified visibility and control across complex AI networking environments.

### Building Webex Integrations for Developers Using AI - DEVNET-2155
Speakers: Adam Ranganathan (Cisco), Sheshadri Mookherjee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271901147001zLfo
Unlock the full potential of Webex by integrating, customizing, and personalizing your deployments with cutting-edge tools. Webex's advanced AI capabilities streamline this process, making it faster and more efficient than ever to discover developer tools, including APIs, SDKs, and frameworks, and to leverage them with AI-generated code snippets. Join us for an insightful session featuring a live demo of how AI simplifies and accelerates the development of integrations and apps for Webex Suite and Webex Contact Center. Additionally, you'll gain actionable insights and practical strategies to utilize AI to enhance the value and performance of your Webex deployments by aligning with user workflows. The session will also explore the future roadmap of AI in Webex development, highlighting upcoming enhancements and features designed to further empower your projects. Product Managers, Solution Architects, Developers, and IT Admins who work with Webex should not miss this opportunity to elevate your Webex experience and stay ahead in the rapidly evolving world of AI-driven development.

### Building Your Own Cisco DevNet Sandbox Experience - DEVNET-1348
Speakers: David Ben Shabat (Quali)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271895337001z6nS
Cisco DevNet's Sandbox experience was created to solve a unique challenge. A small team of internal DevNet engineers needed to support a global community of hundreds of thousands of developers with an intuitive, always-on experience to deploy sandbox environments on-demand. While not many teams face the same scale, the task of delivering resources across large teams is universal among engineering organizations. This session will showcase the technology that enabled the Cisco DevNet team to deliver on this promise and demonstrate how to create a similar experience to scale the delivery of on-demand resources, ranging from basic compute resources to complex workloads supporting AI agents and applications.

### Building a Winning Observability Strategy - PSOOBS-1111
Speakers: Mike Simon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271976624001zNG3
As enterprises face the growing complexity of hybrid environments and microservices, observability has become essential to maintaining operational resilience and driving business outcomes. However, achieving enterprise observability requires more than just tools — it demands a cohesive strategy. In this session, tailored for IT leaders, you'll gain practical insights into building a robust observability framework. you'll leave with actionable best practices that organizations can implement now to address current challenges and a forward-looking approach to shape your observability efforts for the future. Drawing from real-world examples and experiences with large enterprises, this session will help you develop a clear vision for enterprise observability, providing a roadmap for both tactical wins and long-term success. No demos — just practical advice to elevate your observability practice. Key Takeaways: Why enterprise observability requires a strategic approach. Tactical steps to optimize observability efforts today. How to align observability practices with future organizational needs.

### Building a simple and scalable multicloud network for Hybrid WANs, with Cisco Secure WAN - BRKCLD-2029
Speakers: Hamzah Kardame (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271846540001zBMr
Hybrid cloud based WAN environments that mix private cloud, on-premises networks and public cloud networks are quickly becoming the norm for Enterprises today. In this session, you will learn how the Catalyst Secure WAN solution and it's robust Cloud OnRamp integrations into AWS, Azure, GCP, Equinix and Megaport, can simplify the deployment of a secure, scalable WAN fabric that works across any private or public WANs, connecting workloads and apps hosted across multiple clouds to users and machines anywhere, across branch offices, datacenters, colos, hotels, cafes and homes. Key takeaways from this session: 1. How to build a simple, secure, unified network across public clouds and connect it to the private WAN in a matter of minutes via Catalyst Secure WAN 2. Optimizing your multicloud network - managing cloud egress traffic, enabling NAT, enforcing perimeter security within and across clouds and optimizing application access via TCP opt, FEC, caching etc. 3. Monitoring and troubleshooting the multicloud network - discover top apps/flows, services being accessed, bandwidth usage, trace flows etc.

### Building an Enterprise-Class AI/ML Infrastructure using Cisco UCS, NVIDIA GPUs, and Red Hat OpenShift AI for MLOps - BRKCOM-2018
Speakers: Archana Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271859687001zt83
Artificial Intelligence (AI) and Machine Learning (ML) are transforming industries and fueling innovation. However, to fully harness its potential, a robust and scalable infrastructure is essential. In this session, we will explore: Infrastructure requirements for accommodating the diverse needs of AI/ML workloads Designing and building flexible, resilient AI/ML infrastructure using Cisco UCS servers with, NVIDIA GPUs, Cisco Nexus switching, and Red Hat OpenShift Accelerating and streamlining AI/ML projects by leveraging MLOps with Red Hat OpenShift AI, deployed on a Cisco UCS-based converged infrastructure solution. An overview of Cisco UCS-based infrastructure solutions to effectively operationalize AI/ML initiatives Join us to gain a comprehensive understanding of how Cisco UCS infrastructure solutions can simplify your AI journey and assist you in building a robust AI stack for deploying AI/ML applications that deliver significant value for your business.

### CCNP Enterprise Network Troubleshooting Deep Dive - BRKCRT-2285
Speakers: Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271836062001zyuH
On Monday, your colleague Max tried to upgrade the network, but now Rohan can't access data on a server, Emma can't connect to the internet, and Joe can't SSH to a core switch. What do you do? Where do you start? This session will help you improve the skills and knowledge you need to maintain an enterprise network and to diagnose and resolve network problems quickly and effectively. You will hone your troubleshooting skills in real-world networking scenarios in preparation for the CCNP Enterprise ENCOR and ENARSI certification exams. Attendees should already be familiar with the implementation and verification of enterprise routing and switching technologies, such as: Layer 2 switching (VLANs, trunks, port security, LACP, PAgP, STP) Inter-VLAN routing HSRP, VRRP, and GLBP EIGRP, OSPF, and BGP Layer 3 path control Redistribution IPv6 networking This session is for you if you are currently preparing for CCNP Enterprise certification, or seeking to advance your existing troubleshooting skills relating to IPv4 and IPv6 network solutions. During the session, you will review some basic troubleshooting methodologies and procedures, as well as participate in an interactive debrief of the issues presented.

### CI/CD Pipelines for Infrastructure Automation - BRKDEV-2117
Speakers: Adrian Iliesiu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271911033001z87L
CI/CD pipelines have been used as part of software development lifecycle for years. With the advent of network programmability and infrastructure automation, it is now possible to extend the benefits of using CI/CD pipelines to also manage and monitor infrastructure. In this talk, I will go over how to build and use a CI/CD pipeline based on GitLab CE for infrastructure management and automation. The pipeline can be used for testing network configurations in a Cisco CML environment before deploying to production. Other components of the pipeline are Cisco pyATS, Ansible and Cisco Open NX-OS.

### CIO Insights: Transforming Education and Research Across University of California, San Diego and University of California Riverside - CSSXAR-1896
Speakers: Matthew Gunkel (UC Riverside), Tim Lake (Cisco), Vince Kellen (UC San Diego)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271867370001zB6B
Join us for a fireside chat featuring Vince Kellen, CIO of UC San Diego, and Matthew Gunkel, CIO of UC Riverside. They will share insights into how two University of California campuses have leveraged strategic relationships to drive campus evolution, accelerate digital transformation, AI readiness, and enhance cybersecurity post-pandemic. The discussion will cover the challenges faced and how Cisco partnered with these CIOs. The panel will focus on strategies for campus modernization to meet and exceed the expectations of students, faculty, and researchers in the new era of AI.

### CISCO SILICON ONE & ULTRA ETHERNET FOR AI INFRASTRUCTURE - BRKNWT-2508
Speakers: Ramesh Sivakolundu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973510001zzbR
Artificial Intelligence (AI) is changing our society and the industry in many ways and the industry is evolving to adapt to the explosive growth. AI Fabrics, specialized high performance, low latency networks deployed across a cluster interconnect the GPUs used for AI training and inference. This session would address the problems with the current fragmented network built around Infiniband, Ethernet (ROCEv2) and introduce Ultra Ethernet as an industry trend for AI Fabrics. The session will highlight the flexibility and programmability of Cisco Silicon One to seamlessly power Ultra Ethernet based AI Fabrics.

### CTF Break for your Brain: Lockpicking - Pin Tumbler Locks - CTF-1036
Speakers: Jeremy Junginger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271943743001zlJX
Sometimes we need to give our brains a moment to rest. CTF BfyB Sessions are designed to let you spend a few minutes thinking about something completely non-IT related. For this session, we'll be joining our resident lock picking experts as they explain the in's and out's of picking a tumbler lock.

### Calling Interoperability with Microsoft Teams - BRKCOL-2067
Speakers: Sara Macias Salete (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271855654001zqzL
This intermediate-level session provides attendees with a detailed understanding of Cisco Call for Microsoft Teams, the client-side integration that provides interoperability between Microsoft Teams and the Cisco Calling Platforms The following topics will covered in this breakout: Overview of all the interoperability options between Microsoft Teams and Cisco (15% of the session), including: Using Cisco Phones and Peripherals with Microsoft Teams Direct Routing and Interworking options via CUBE Cisco Call for Microsoft Teams (85% of the session) Client-side integration for Webex Calling and Cisco Unified Communications Manager Live demo showing all the new features Architecture, deployment and best practices A basic understanding of Cisco calling solutions is necessary to comprehend the content of this session. To gain further insights into Microsoft Direct Routing, please consider attending the session BRKCOL-2314: CUBE v14 Updates.

### Campus Switching Architecture for Future Proofed Workspaces - BRKARC-2668
Speakers: Kenny Lei (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271918002001z3S2
As campus workspaces evolve with newer endpoints and applications, there are increasing demands on campus networks. In this session, we will explore how future Cisco campus switches are engineered to meet these changing requirements. We'll delve into the hardware and software architecture of these switches and examine the features that contribute to building a simple, secure, and highly available campus network. Additionally, the session will cover the key components at the core of these switches, focusing on the role of the ASIC.

### Campus Switching Innovations for Future Proofed Workspaces - BRKENS-2609
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271923415001zdoJ
Modern workspaces demand secure, scalable, and high-performing networks to support hybrid work, IoT, next-gen technologies, and sustainability goals. This session introduces Cisco's new switches alongside key innovations, such as pervasive security, AI-driven insights, software-defined access, and cloud management. Discover how these solutions simplify management, enhance scalability, boost energy efficiency, and enable smart, resilient, and sustainable environments ready to meet tomorrow's challenges.

### Catalyst 9000 Series Switching Family: Access - BRKARC-2098
Speakers: Ovua Harcourt (Cisco), Manish Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271869270001zmSX
This session will cover the platform overview of Catalyst 9000 access switches. It will share the details of the Catalyst 9000 product portfolio, which will include new additions in fixed and modular access series: Catalyst 9200, Catalyst 9300/X, and Catalyst 9400/X. The session will discuss the component at the heart of these switches, which is the ASIC. It will also cover common attributes, technologies, and features of Catalyst 9000 switches.

### Catalyst 9000 Series Switching Family: Core and Distribution - BRKARC-2099
Speakers: Kenny Lei (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916830001zUeU
This session will cover the platform overview of Cisco Catalyst 9000 Series core and distribution switches. It will share the details of the Catalyst 9000 product portfolio, which will include new additions in fixed and modular core and distribution switching series (Catalyst 9500/X and Catalyst 9600/X). The session will talk about the component at the heart of these switches which is the ASIC. It will also cover common attributes, technologies, and features in the Catalyst 9000 Series Switches.

### Catalyst 9800 Configuration Best Practices - BRKEWN-2339
Speakers: Ignacio Fite Lopez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941997001znW8
Understand the best practices, design recommendations, and useful practical deployment tips on how to successfully migrate from your current AireOS wireless network to a Catalyst wireless one, covering from day 0 to day N.

### Catalyst Center Network Operations Essentials using UI and APIs - DEVNET-2660
Speakers: Adrian Iliesiu (Cisco), Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912014001zESl
In this session, will explore the essential workflows for managing your Cisco Catalyst Center infrastructure. We'll focus on the Catalyst Center platform, covering topics such as device onboarding, provisioning, software upgrades, and device configuration. Attendees will learn how to configure the Catalyst Center features using the Graphical User Interface, APIs and the DevOps libraries: Python SDK, Ansible, Terraform. We will review also the options to integrate with third party platforms for your runbook environment: Jenkins and GitLab. The session includes demos for Catalyst Center network operations and open-source code. This is 105 minute session.

### Catalyst Center and Meraki Cloud: The Right Choice for your Catalyst 9000 Switch Management! - BRKENS-1601
Speakers: Aishwarya Sudeep (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271922824001zsjR
Given the unique advantages of both cloud-based and on-premises network management, and the prevailing trend among organizations embracing a hybrid approach, it is crucial to recognize what seamlessly fits your network. Cisco addresses the diverse feature needs of today with two solutions, the cloud-based Cisco Meraki management and the on-premises-based Cisco Catalyst Center for Catalyst 9000 switches, each boasting its own distinct advantages based on network complexity and size. During this session, participants will delve into the essential features for monitoring and managing their Catalyst 9000 switches like configuration, assurance, and analytics, as well as campus use cases. Live demonstrations will be conducted on both network management tools, empowering participants to make informed decisions for their networks "Your network, your way."

### Catalyst Full Stack Intelligent Observability Powered by Splunk - BRKOBS-2111
Speakers: Sarav Radhakrishnan (Cisco), Salah Ramlawi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271932617001zn72
As enterprises digitalize their infrastructure, they are looking for real-time monitoring and observability to empower their daily operations through the power of AI. However, there is a fine line between granular visibility across all domains in your network and "dashboard fatigue" that comes with managing several solutions Several products across Cisco networking and security have joined forces to produce a common application that leverages data from across the LAN, WAN, Identity, and applications (IT and OT), and it does so with the help of the technical add ons. This session provides a deep dive into the Cisco Enterprise Networking app that aims to empower NetOps and SecOps teams by providing fine grain visibility into all areas across the network.

### Catalyst powered Intelligent Ready Building Framework - BRKXAR-2023
Speakers: Ryan Casey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271868143001zTfA
Commercial buildings use roughly 40% of all energy produced in the world and they contain more than 30 subsystems to perform daily activities. This session will focus on three key aspects of delivering intelligent space: converged networks, automation, and security. We will take a deeper dive into Cisco Spaces, third-party integrations, and how this is enabling additional automation techniques, reducing total energy consumption. Join this session as we explore the challenges faced in delivering Cisco's Paris HQ, the architecture behind the solutions, and best practices.

### Charting the course: A strategic approach to SDI adoption - BRKXAR-2035
Speakers: Dave Lucas (Cisco), Hanna Woldeyesus (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271869081001zTFE
Deploying a Software-Defined Infrastructure (SDI) across your campus and data center is a complex transformation. How do you approach it strategically? What are the key building blocks? How do you prioritize adoption while navigating potential challenges? This session will provide a journey-mapping approach to SDI adoption. Learn how to ask the right questions and establish clear priorities to build a successful roadmap. Whether you're just starting or refining your strategy, this session will help you chart a path forward. This session is intended to be about the approach and building the strategy; it is not intended about how to deploy Software-Defined Infrastructure technologies. However, understanding the technologies is recommended for this session.

### Check-M8! Changing the AI Game with the latest UCS Innovations - BRKCOM-1047
Speakers: Bryan Hilton (Cisco), Gregory Wilkinson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271859112001zoSK
Modern applications and AI use cases are driving significant challenges in the data center and are challenging the way traditional infrastructure has been deployed. Come join us as we discuss the game changing innovation that has been introduced in the UCS portfolio to address those challenges and future proof your infrastructure investments. We will be discussing the latest UCS announcements around Intel, AMD, and NVIDIA with our rack and modular platforms.

### Choosing the Right Cisco Catalyst Center Deployment Model for Your Network - BRKOPS-2698
Speakers: Lila Rousseaux (Cisco), Adam Radford (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271989977001zLsG
Cisco Catalyst Center has evolved from a single appliance option to a robust platform offering diverse deployment models, including both physical and virtual appliances. With options for clusters, disaster recovery, and varying scales, network administrators now have greater flexibility but also more decisions to make. This session is designed give network administrators enough information to help them select the optimal deployment model for their unique environments. Topics will include: Physical vs. virtual appliance options. Scaling considerations and capacity planning. Backup and restore capabilities. High availability and disaster recovery models. Leveraging Catalyst Center Global Manager for multi-site management. Gain clarity on deployment strategies and make informed decisions to maximize the potential of your Catalyst Center implementation.

### Circuit-Style Segment Routing and Service Emulation - BRKMPL-2133
Speakers: Thomas Peiyao Wang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271961536001zPzC
This session will demonstrate how to enable time-division multiplexing (TDM) and private-line emulation services over bandwidth-guaranteed circuit-style segment routing. Participants will also see service emulation use cases over the resilient circuit-style segment routing transport. Traditional circuits over SONET/SDH transport are becoming outdated, even at the end of life, and costs are skyrocketing. Segment routing has been well adopted by the market. Circuit-style segment routing provides an alternative solution to offering reliable transport, but much cheaper than SONET/SDH. The centralized SR-PCE helps to compute the network resources and ensure the bandwidth-guaranteed CS-SR data path with protection.

### Circular Design Can Increase Efficiency and Cut Costs - PP-1302
Speakers: David Stallings (Cisco), Mary de Wysocki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271947271001zP5g
Many IT leaders are tasked with reducing their network's impact on the environment, all while keeping costs down, maintaining performance, and supporting increased workloads. Cisco is helping you address this challenge through its Circular Design Principles — which influence everything from the amount of energy our products consume, to the amount of plastic we use to the recyclability of our packaging. Circular Design Principles can help you keep your hardware in service longer, lower your energy use, reduce e-waste, and even cut costs. Hear from a product engineering leader who is incorporating circular design into the products you use, and see examples of products that can help you address both business- and sustainability benefits to your company.

### Cisco 8000 Technical Update: Powered by Silicon One and IOS XR - BRKSPG-2944
Speakers: Eddie Chami (Cisco), Chang Soo Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271968900001z3W6
Cisco 8000 series routers are cloud-enhanced systems powered by Silicon One and IOS XR software. In this technical session, participants will discover the latest Cisco 8000 portfolio, including 8800 distributed systems, 8200, and 8100 fixed systems, and the new Cisco 8600 centralized system. Technical material will detail ASIC and hardware architecture, capabilities, scale, forwarding, QoS, and life of a packet. IOS XR software architecture and operations along with 400G ZR/ZR+/Bright ZR+ optics support will also be addressed in this presentation. Lastly, the speaker will deep dive into various tools and techniques available to troubleshoot packet forwarding and NPU internal memory resources using available monitoring options. This breakout is not about Catalyst 8000 Edge platforms family.

### Cisco 8500 and 8400 Series Secure Routers for Scalable WAN Aggregation - BRKARC-2885
Speakers: Sumant Mali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271917220001zL0i
Cisco 8500 and 8400 Series Secure Routers are built to empower WAN aggregation deployments for Enterprise, IoT networks. The session will start with platform overview to advance into architecture deep dive covering data plane and control plane operations, connectivity and performance insights. Understanding the architecture benefits, we shall acquaint them to variety of WAN aggregation and Campus Edge use-cases. At the end, you will have bonus insights on advance troubleshooting tools for these platforms.

### Cisco ACI Contract Deep Dive for CCNP Data Center Candidates - BRKCRT-2023
Speakers: Joe Rinehart (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271835863001zkLx
Contracts comprise one of the most fundamental building blocks in Cisco ACI, and we often think of them functioning a lot like traditional access-lists, but the internal details are substantially different. How do they actually accomplish traffic regulation? What is the relationship between contracts (as configured in the APIC GUI) and zoning rules (programming on the switches)? What effects do taboos, VzAny and preferred groups have on data flows? The finer details on the operation of contracts answer these questions and many more. Success on the Data Center Core and ACI Elective exams hinges on a thorough understanding of contract operation.

### Cisco ACI EPGs vs. ESGs: Comparison and Use Cases for Each - CISCOU-2066
Speakers: Joe Rinehart (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271842895001zlXg
Endpoint Security Groups (ESGs) were introduced in ACI code 5.0 as an additional construct in addition to Endpoint Groups (EPGs). Even today, there is some confusion about the differences between them and the best time to use each one. This session will outline the differences and present some use case for each.

### Cisco ACI Multi-Pod Design and Deployment - BRKDCN-2949
Speakers: John Weston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271890375001zirM
Deploying ACI across multiple data center locations or rooms to ensure redundancy is a common requirement for enterprises and service providers. This session will explore the ACI Multi-Pod solution, which uses a single APIC controller cluster to manage and connect separate ACI sites over an inter-pod network. We will discuss: The functional components of the Multi-Pod architecture Deployment considerations, including APIC cluster options Updated with ACI features for Multi-Pod fabrics, such as: Connecting APIC clusters over a Layer 3 network Virtual APIC clusters Multi-Pod back-to-back connectivity without an IPN BGP underlay support Join us to gain insights into effectively deploying the ACI Multi-Pod solution.

### Cisco AI Assistant to Troubleshoot Application and Network Connectivity - BRKOBS-1019
Speakers: Saila Talagadadeevi (Cisco), Yuvnesh Modi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272016900001zCi8
In today's digital landscape, maintaining seamless connectivity for applications and devices is crucial. ThousandEyes, integrated with Cisco AI assistant, offers a powerful solution for troubleshooting connectivity issues. This integration utilizes ThousandEyes' network intelligence to monitor and diagnose problems across the entire network path, from user devices to cloud services. By deploying agents across various network segments, ThousandEyes gathers detailed performance data, identifying bottlenecks, outages, and anomalies. The Cisco AI assistant enhances this capability by providing intuitive insights and actionable recommendations based on the collected data, enabling IT teams to swiftly address issues and minimize downtime. This synergy between ThousandEyes' comprehensive visibility and the conversational capabilities of the Cisco AI assistant ensures a proactive approach to maintaining optimal connectivity and performance, thus supporting business continuity and enhancing user satisfaction.

### Cisco AI portfolio - CTF-1050
Speakers: Supratim Chakraborty (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271858549001z7bK
Cisco's AI portfolio is strategically designed to empower enterprises across every phase of AI adoption'spanning infrastructure, security, data, software, and services. At the foundation lies Infrastructure, providing scalable and high-performance compute and network solutions to meet the surging demands of AI workloads. Security ensures trusted AI deployment, embedding protection across the organization's digital and operational environments. With Data as the new currency, Cisco enables real-time, large-scale data visibility and management, forming the backbone of intelligent decision-making. The portfolio further integrates AI-powered Software to drive operational efficiency, offering intelligent automation and insights through AI-native tools. Finally, Cisco's Services provide expert guidance to accelerate AI integration, from initial strategy to full-scale deployment. Together, these pillars form a cohesive ecosystem that transforms AI potential into enterprise-ready reality.

### Cisco Assurance for Federal IT: FedRAMP-Ready Solutions for Secure, Cloud-First Operations - PSOENT-1024
Speakers: James Parnham (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928021001zNsv
As federal agencies expand into cloud and hybrid environments, visibility and compliance remain critical. Cisco solutions provide secure infrastructure and actionable insights across networks, ISPs, and cloud services. Join us to learn how Cisco is advancing its FedRAMP journey to support the evolving needs of federal IT'through Meraki (Moderate authorized) and ThousandEyes (authorization in progress). See how agencies are improving performance, reducing risk, and modernizing with confidence.

### Cisco Catalyst 9000 Series, Cisco Silicon One, and IOS XE Architecture and Innovation - BRKARC-2092
Speakers: Shawn Wargo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271917613001zl7p
This is a combined session covering Cisco ASICs on Catalyst 9000 Series Switches (BRKARC-2091) and Cisco IOS-XE on Catalyst 9000 Series Switches (BRKARC-2090). This level II (intermediate) session will focus on the hardware and software components upon which the Cisco Catalyst 9000 Series Switches are built. Key topics covered regarding Cisco IOSXE on Catalyst 9000 Series Switches: Why do we need ASICs? (vs. CPUs & FPGAs) Cisco UADP and Programmable ASICs Cisco SiliconOne next-generation ASICs The future of Catalyst 9000 Series Switches hardware Key topics covered regarding Cisco IOS-XE on Catalyst 9000 Series Switches: Recap of the basic principles and history of Cisco IOS Overview of the software components of Catalyst 9000 IOS-XE Key innovations enabled by IOS-XE releases 17.9-17.15 What's new with IOSXE release 17.18 onwards A glimpse into the future of Catalyst 9000 Series Switches software This session can be used to help design and position different Catalyst 9000 Series products with a deeper understanding of the underlying hardware and software.

### Cisco Catalyst 9000 Switching QoS with Silicon One ASICs Deep Dive - BRKARC-2039
Speakers: Ninad Diwakar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271917416001zNWB
This session will deep dive into the QoS model used in the Cisco Catalyst 9000 Series of switches powered by the Cisco Silicon One ASICs. The session will cover platform-specific designs for classification, policing, and ingress and egress queueing policies which are applicable to the Catalyst 9000 switches. To close things off, the session will cover thought processes to be followed for migration configurations from Catalyst 6500 Series switches over to the Catalyst 9000 Series switches. This is an intermediate session and attendees are assumed to have a basic understanding of different QoS operations and terminology.

### Cisco Catalyst Center Integration with ServiceNow - TACENT-2022
Speakers: Isabel Maqueda (Cisco), Joshua Sprague (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271929189001ziLW
• Identify essential components for successful integration. • Clarify each configuration requirement and request for the integration. • Define the scope and limitations of the integration: • Applicable with or without the CatC application installed on ServiceNow. • Highlight common issues that can be promptly addressed and resolved.

### Cisco Catalyst Center: Built-In Integrations for Streamlined Network Operations - BRKOPS-2609
Speakers: P Surya Prakash Rao (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271989578001zxal
Integrating with different ecosystems is essential for simplifying the management of large networks. These integrations help provide clear visibility and insights, acting as a single source of truth for network policies, configurations, and devices. In this session, we will explore the built-in integrations between Cisco Catalyst Center and various Cisco and external ecosystems. We'll discuss use cases that demonstrate how network operations can be streamlined and IT processes improved. This session will cover Built-In integrations of Catalyst Center with Ekahau, Cisco Spaces, Cisco ISE, MS Teams, Cisco Webex, Thousand Eyes, Stealthwatch, ITSM and Event Notification Integrations. Topics to be covered include: Visibility of Wireless Networks: Enhance end-to-end Visibility of Wireless APs, Endpoints, Rogues and Interferers and tools to improve the coverage and performance of wireless networks. Security Policies: Enhanced visibility of deployed secure policies and endpoints with AI-driven analytics and network-driven deep-packet inspection for better threat detection and response Application Performance: Improving visibility into application performance and simplifying troubleshooting for faster issue resolution. Incident Management: Streamlining ticketing processes for incidents and change management to reduce costs and enhance efficiency.

### Cisco Catalyst SD-WAN Fundamentals - CISCOU-1052
Speakers: Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271839302001zo8v
Learn the basics of Cisco Catalyst SD-WAN in this short, interactive session. Discover what all the hype is about Cisco Catalyst SD-WAN, how it works, why it's augmenting the traditional WAN, and how it makes it easier to securely access cloud-based services such as AWS, MS Azure, GCP, Cisco Umbrella, Cisco ThousandEyes and Megaport. We will look at some customer use-cases and benefits, as well as see how Cisco Catalyst SD-WAN can help solve today's business challenges.

### Cisco Catalyst SD-WAN: Start Here - BRKENT-2108
Speakers: Lars Granberg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933422001zF7v
The Catalyst SD-WAN 'Start Here' session is designed to provide participants with a comprehensive introduction to Cisco's Catalyst SD-WAN solution. This session will explore how Catalyst SD-WAN enables organizations to connect any user to any application with integrated multicloud capabilities, robust security, and predictive intelligence. Attendees will gain insights into the key features of Catalyst SD-WAN, including its SASE-enabled architecture, application-aware routing, and centralized management through the Catalyst SD-WAN Manager. Key topics include: • Overview of Catalyst SD-WAN Architecture: Understanding the components such as the SD-WAN Manager, Validator, Controller and Edge devices. • Deployment Scenarios: Exploring on-premises, cloud-based, and hybrid deployment options. • Operational Simplicity: Demonstrating how automation and analytics simplify network management and enhance visibility. • Integrated Security: Highlighting features like Secure Firewall with IPS and Secure Access Service Edge (SASE) capabilities.

### Cisco Certifications Portfolio Updates - CISCOU-1048
Speakers: Mubasher Nawaz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271838505001zspY
Are you preparing for the Cisco Certification Exam? Come join us to learn about upcoming changes to the Cisco Certification exams aligning with Annual Certification roadmaps and get answer to all your Certification questions as you prepare for your Certification Journey from Entry to Expert level. Know about the resources to prep for you exam and where to find them.

### Cisco Certifications Portfolio Updates - PSOCRT-1026
Speakers: Mubasher Nawaz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833572001zdTS
Are you preparing for the Cisco Certification Exam? Come join us to learn about upcoming changes to the Cisco Certification exams aligning with Annual Certification roadmaps and get answer to all your Certification questions as you prepare for your Certification Journey from Entry to Expert level. Know about the resources to prep for you exam and where to find them.

### Cisco Compute Automation with Natural Language - BRKATO-1010
Speakers: David Cedrone (VZURE Solutions), Mohit Vaswani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271831520001zPF5
The integration of Artificial Intelligence (AI) with Cisco's Unified Computing System (UCS) marks a significant advancement in data center technology, offering enhanced scalability, and efficiency. By leveraging AI, organizations can achieve a more adaptive and resilient computing environment, capable of meeting the dynamic needs of modern enterprises. This session explores the deployment strategies of UCS infrastructure with natural language using Cisco Partner VZURE's AI Solution. We will delve into tools such as Intersight and the role of AI in automating and improving UCS operations and configuration.

### Cisco Connected Justice Virtual Visitation Solution (VVS) and Offender Reservation Platform - BRKXAR-2132
Speakers: Mubashir A Khan (Cisco), Rob Jennings (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871769001zj4y
Cisco (CX) Virtual Visitations Service (VVS): Cisco CX has created a purpose-built hosted solution that overcomes the challenges of remote video conferencing within corrections or other secure environments. VVS helps rapidly design, implement, and deploy a real-time voice, video, and data connectivity solution via Webex that is easily managed by incorporating automation, configurable workflows, role-based access into the visitation solution and a zero-touch visitation joining experience. The VVS portal can be integrated with the customer's information system such as a Customer Management System to access basic user information including the location to automatically choose an appropriate Cisco Webex video device for the visitation based on visitation policy and device availability. Cisco's VVS solution can be customized to meet facility policies including visitation schedules, approval flows, visitation duration and automatic recording for certain types of visits. Use cases include professional visitation like attorneys or telehealth, court hearings, educational content and more.

### Cisco Data Center: Built for AI. Ready for Everything. - CENDCN-1399
Speakers: Jeremy Foster (Cisco), Dan Wendlandt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592612208001XIar
IT leaders are under pressure—rising costs, fragmented tools, and the race to be AI-ready are forcing a fundamental rethink of infrastructure strategy. Cisco is redefining the data center with a unified approach that simplifies complexity, accelerates innovation, and puts you back in control. While others build boxes, we're building the foundation for the future - with intelligent, cloud-managed operations so you can deploy, monitor, and optimize infrastructure from anywhere, at any scale. This session isn't about hardware—it's about building what's next. Automated lifecycle management. Seamless workload mobility. Built-in visibility, security and control from edge to cloud. Stop managing silos. Start building smarter. Join us in the AI Hub to see how Cisco is turning data centers into launchpads for what's next.

### Cisco HCI Solution 101 in 60 Minutes - BRKCOM-1010
Speakers: Sho Funatsu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271858927001z9M8
The Cisco hyper-converged infrastructure (HCI) solutions can power your applications and data anywhere, optimize operations from your core data center to the edge and into public clouds, and increase agility by accelerating DevOps practices. This session will cover the introduction to the Cisco HCI solutions with Cisco Intersight. Together, this combined solution disrupts the traditional operational model by eliminating the burdens of managing distributed infrastructure. Discussions will focus on multiple solution options, simplified management of Day-0 through Day-2 operations and how Cisco HCI helps you maximize value while minimize costs. Those attending the session will get a comprehensive view of Cisco HCI solution offerings, architecture, and operations.

### Cisco Hypershield: Mastering Next-Generation Security - BRKSEC-2265
Speakers: Jeroen Wittock (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009777001z010
If ever I did a security masterclass in 90 minutes, this is it. We will talk about eBPF, dual dataplane, and the many different types of AI that are the core of Cisco Hypershield. In addition, we will spend some time on our vision where security operators and administrators can move away from writing policy and spend more time on increasing the overall security of the environment in it's entirety. We will show the tools to do that, as well as the tools that will make it easy to discover if any known CVE's are applicable in your environment, and how to deploy shields to address these CVE's without impacting the application itself. We'll show how Cisco Hypershield will make it easier to deploy the right segmentation strategies for your specific environment, and how to keep those segmentation policies current to actual state of your environment. The session will end with an overview of the native automation capabilities through the API and demo scripts.

### Cisco IOS XE: Telemetry, Automation, and YANG -- Oh My! - BRKOPS-1401
Speakers: Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271987619001zCrG
This programmability and automation on Cisco Catalyst IOS XE includes an overview of the YANG based API's and the associated toolings. The session will cover automation at every device stage including device onboarding, device configuration management, device monitoring and device optimization. Many tools such as YANG Suite will be used to demonstrate finding a YANG model and building API calls to push to Catalyst devices. The Model Driven Telemetry capabilities will also be discussed and the example Docker container for collection and visualization will be demonstrated. Guest Shell, the Python and NETCONF API, and other innovations that enable our devices to be deployed, managed, and configured with ease at scale.

### Cisco IOS-XR 8000: Troubleshooting LPTS Drops - TACMSI-2000
Speakers: Mario Sotres Cataño (Cisco), Ricardo Ferrer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272015906001z5Mg
"Designed for high-performance Service Provider environments, the Cisco 8000 series routers boast advanced architectures, yet troubleshooting packet drops within these systems remains a complex challenge. This session delves into the internal packet processing mechanisms of the Cisco 8000 platform, equipping engineers with the skills to effectively identify and address packet drops. Participants will learn to analyze internal packet flows, employ vital diagnostic commands, and comprehend the architecture's influence on forwarding behavior. The session aims to offer a practical approach to resolving packet drops, incorporating real-life examples and established methodologies to ensure consistent and reliable network performance."

### Cisco IP Phones, Headsets, and Webcams: The Product Updates that we all Need to Know - BRKCOL-2068
Speakers: David Scott (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271855862001z11r
Explore the latest information on features for the Cisco IP Phones along with the many Cisco peripherals that can benefit your organization. Deep Dive on the new Cisco Desk Phone 9800 Series Hotdesking and meetings Phone migration DECT Wireless Phones and Cisco Wireless Phones 840/860. Which to deploy where? Cisco Headsets including Microsoft Certified Cisco Headsets

### Cisco ISE Log Analytics - TACSEC-2018
Speakers: Ethan Glaser (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271996780001zxeJ
Cisco Identity Service Engine's Log Analytics service is a built-in ELK stack to monitor performance and troubleshoot issues within ISE. Log Analytics helps enhance the visibility of your secure network and easily provides insights of active issues within your network. We will break down the monitoring and reporting capabilities of Log Analytics using pre-defined dashboards then take a look at common issues seen within ISE and how we can use Log Analytics as a tool to spotlight these issues, narrow our troubleshooting scope, and provide a deeper analysis of the issue how to resolve the issue. Attendees will gain a deeper understanding of the Log Analytics tool within ISE and should take away useful troubleshooting techniques to help resolve and mitigate issues in their own networks.

### Cisco ISE Meets Azure Cloud. Deploy, Automate, Integrate with Entra ID and Intune - BRKSEC-2416
Speakers: Eugene Korneychuk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010179001zbJL
ISE perfectly fits into ZTN, Today, ISE can be a Azure cloud native solution as well. This session will unleash ISE in Azure capabilities, talk about ISE deployment in Azure, Automation of such deployment, Integration with Entra ID and Intune.

### Cisco ISE: Implement these 5 technical wins that will help you to maximize Network Security. - CTF-1040
Speakers: Andres Sarmiento (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271994398001zzn8
In Today's rapidly evolving threat landscape, network security is more critical than ever. Join us for an in-depth session on Cisco Identity Services Engine (ISE) and discover five actionable technical strategies to bolster your network's defenses. This session is designed for customers looking to maximize the value of their Cisco ISE investment and those planning their next steps in network security. Explore how Asset Visibility enhances your ability to identify and categorize every device on your network. Learn how Posture and Compliance Assessments ensure your endpoints meet security standards before they access critical resources. Dive into the power of micro-segmentation with Cisco TrustSec, enabling you to contain threats and enforce granular security policies. Whether you're deploying Cisco ISE for the first time or optimizing an existing implementation, these technical wins will give you the tools and insights needed to secure your environment effectively. Don't miss this opportunity to elevate your network security strategy with practical guidance from Cisco experts

### Cisco IT's Journey to SSE - Enabling Hybrid Work with Cisco Secure Access - BRKCOC-2040
Speakers: Mike Cifelli (Cisco), Joe DeSanto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837189001zgLR
Cisco IT's journey to Security Service Edge (SSE) highlights prevailing success in our strategic expansion ensuring consistent, reliable, and secure hybrid worker connectivity worldwide. Through the integration of VPNaaS, Zero Trust Network Access (ZTNA), and Generative AI protection with Secure Web Gateway (SWG), all managed by the Cisco Secure Access cloud service, customers will learn how our adoption is achieving robust and secure access without the need for hardware. You will also gain insights into our journey on how we are transforming user experience and security while overcoming IT business challenges and ultimately paving the way for enterprise scale and stability.

### Cisco IT: Streamlining Network Management and Decisions with Catalyst Center Automation and Splunk - BRKCOC-2483
Speakers: Jerry Akouala Gampio (Cisco), Dan Rowe (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837374001zc6k
In the fast-paced world of network management, automation is essential for achieving efficiency and reliability. This session will delve into the powerful automation capabilities of Cisco Catalyst Center, focusing on three critical functionalities: automated software upgrades with SWIM (Software Image Management), automated incident creation utilising predictive AI network trends with automated resolution and last but not least, data visualisation in Splunk. To enhance efficiency and minimize errors, Cisco IT developed Atomic SWIM, an automated system that leverages Catalyst Center's APIs to schedule and activate upgrades while ensuring system health. Day N templates enable the quick and standardized configuration of network devices, ensuring compliance with best practices. Additionally, automated incident resolution can be achieved by deploying the relevant Day N template to correct any incorrect or outdated configurations. The Catalyst Center APIs are also employed to pull various data sets and send it to Splunk for comprehensive visualisations, empowering data-driven decision-making. One of the key projects driven by Splunk data insights is Managed Access, where we transitioned to a certificate-only wireless. By leveraging data visualised in Splunk, we were able to identify devices still using username/password as well as have an understanding of the user-base being affected to ensure a smoother user-experience during migration. This session will explore the practical applications of Catalyst Center and Splunk, highlighting real-world scenarios and lessons learned from Cisco IT's deployments. Attendees will gain insights into how these tools can be leveraged together to enhance network management, drive strategic projects, and make more informed decisions.

### Cisco N9300 Smart Switch - CTF-1052
Speakers: Roxana Diaz Hernandez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879596001zRDC
In this session, attendees learn about Cisco Smart Switch use cases, Hypershield capabilities, how to redirect traffic to the DPU, and perform a packet walk-through and we will demonstrate the benefits, including improved security and enhanced network security enforcement.

### Cisco Nexus 9000 Architecture - BRKDCN-3939
Speakers: Faraz Taifehesmatian (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892827001zyLO
This session presents an in-depth study of the architecture of the latest generation of Nexus 9000 modular and top-of-rack data center switches. Topics include ASIC architecture, forwarding mechanics, and physical design elements, as well as a discussion of key hardware-enabled features and capabilities that combine to provide high-performance data center network services.

### Cisco Nexus Smart Switches with DPUs. A window to a transparent secure datacenter network architecture - BRKDCN-2643
Speakers: Maurizio Portolani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885424001ztCZ
This session explores the integration of Cisco's Nexus Smart Switch with Cisco Hypershield's AI-native security architecture to enhance network security and performance. Attendees will learn about use cases, embedding security enforcement into network infrastructure using DPUs for high-capacity throughput and intelligent policy enforcement. The session highlights benefits such as improved security, flexibility, and effective protection offering insights into the future of network security and Cisco's transformative solutions.

### Cisco Panduit Network + Power solutions drive scale, energy efficiency for Data Centers & Enterprise - CNCETI-2002
Speakers: Christopher Liljenstolpe (Cisco), Andrew Lu (Cisco), Mahmoud Ibrahim (Panduit)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271913942001zeZX
Applications such as AI and IoT are driving demand for higher network speeds and more power. Join Cisco and Panduit to learn about the validated solutions we have developed to address these pressing network and power needs. This session will cover the following topics: Exciting announcements about Panduit Fault Managed Power System (FMPS) + Cisco Catalyst PoE switching platform delivering an end-to-end DC power distribution system for smart buildings. Breakout architectures using Panduit fiber + Cisco Nexus switches and optics enabling energy efficiency and seamless migration from Enterprise to AI data centers. Panduit iPDUs + Cisco Nexus Dashboard providing greater visibility to energy usage and insights.

### Cisco SD-Access Transit: Advanced Design Principles - BRKENS-2816
Speakers: Jerome Dolphin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924574001zt2d
Cisco SD-Access Transit simply interconnects SD-Access Fabric Sites while preserving end-to-end macro-segmentation (Virtual Networks) and micro-segmentation (Security Group Tags). A LISP Pub/Sub SD-Access Transit offers a suite of foundational capabilities that can elegantly solve simple to complex inter-site connectivity requirements, ranging from two Fabric Sites in the same campus to a global network with hundreds of Fabric Sites. Attend this session to learn how to solve for resiliency, scale, MTU, high availability, routing summarisation, multiple exit points, location-based route steering, egress prefix prioritisation, multicast routing and multiple Cisco Catalyst Center clusters. Attendees are advised to be familiar with the introductory material discussed in BRKENS-2810 and BRKENS-2811 before attending this session.

### Cisco Secure AI Factory with NVIDIA Overview - PSODCN-1076
Speakers: Daryl Coon (Cisco), Abhinav Joshi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271881168001zUKI
Learn how you can accelerate your adoption of AI to unlock differentiated outcomes with confidence and unprecedented security. We will provide an overview of how Cisco Secure AI Factory with NVIDIA delivers a scalable, high-performance AI infrastructure built upon a foundation of security and choice. You'll be able to streamline the development, deployment, and protection of your AI workloads.

### Cisco Secure Firewall Platforms Deep Dive - BRKSEC-2239
Speakers: Lukasz Bromirski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009201001zM7T
This intermediate session will provide a deep dive into Secure Firewall security platforms and the associated application use cases. We'll cover hardware platform news and innovations, capabilities in 7.6 and 7.7 that introduce interesting new capabilities, as well as various aspects of the security application framework. The session will also address specific popular topics in design with NGFW like: single-flow (elephant flows), visibility into encrypted traffic without decrypting it (EVE), QUIC and TLS inspection implications on FTD throughput, inter-chassis clustering, multi-tenancy with Multi-and VRFs. At the end of the session, we'll also cover common internet edge scenarios with BGP. Working knowledge of FTD knowledge is required.

### Cisco Security Cloud Control - Bringing the Cisco Security Portfolio Together - BRKSEC-1656
Speakers: Adam Bragg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271999360001zqqW
In this session, participant will learn about Security Cloud Control, Cisco's new platform to unite the Cisco Security Portfolio. This session is targeted for people who use one or more Security products from Cisco, including: • Cisco Firewalls • Cisco Secure Access • Cisco Hypershield • Cisco AI Firewall • Cisco Multicloud Defense • Meraki Firewalls This introductory session will introduce the audience to the concepts and current capabilities of the Cisco Security Platform. Participants will learn how to: • Get started with the Security Cloud Control • Add their existing products and services into the Security Cloud Control • Provision new products and services using Security Cloud Control • Manage Roles and Users with Security Cloud Control • Configure Security Cloud Control to integrate with their existing Identity Provider • Leverage Security Cloud Control to maximize their Cloud Protection Suite investment At the conclusion of the session, we will talk about what is coming soon and where we are headed next.

### Cisco Silicon for AI: Capabilities, Designs and Results - BRKARC-2095
Speakers: Dave Zacks (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916631001zdvP
We all know that AI is changing the world. But have you ever wondered how you can build networks that support AI/ML workloads and how Cisco designs and builds the platforms to support your AI efforts? If so, this is the session for you. Attendees at this session will learn how Cisco platforms are being architected to support and optimize AI/ML workloads, the benefits these capabilities provide, and most importantly, how you can leverage these sets of functionality in your own network designs and implementations. Presenting this session is the dynamic duo of Peter Jones, Distinguished Engineer and Cisco Live Distinguished Speaker, and Dave Zacks, Distinguished Engineer and Cisco Live Distinguished Speaker Hall of Fame Elite member. Come to this exciting, in-depth, and fun session to see the latest in Cisco silicon and platform innovations to support AI.

### Cisco Software-Defined Access LISP Solution Fundamentals - BRKENS-2810
Speakers: Kedar Karmarkar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924385001z9Ay
Cisco SD-Access LISP is an evolution from traditional campus LAN to networks that directly implement the intent of an organization through a zero-trust architectural framework. SD-Access LISP intent-based automation seamlessly scales from one to tens of thousands of wired and wireless networking devices, reliably connecting and securing businesses of all sizes around the world. This presentation will be a technical introduction to SD-Access LISP, exploring and explaining the high-level concepts and components that underpin the solution.

### Cisco Spaces: Advanced Location Based Services for Enterprise Networks - BRKEWN-2658
Speakers: Nirav Turakhia (Cisco), Bharath Jayaram (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271939246001z1vx
Learn how to leverage Cisco Spaces to complement your Cisco Enterprise Network deployments. Beginning with an overview of Spaces Full Stack, the discussion covers details on how to create Spaces Standard and Pro Maps; Auto place Access Points and prepare your network for location based services tasks that traditionally demand weeks of effort and additional resources. Furthermore, the discussion delves into achieving sub-meter location accuracy with Ultra-WideBand (UWB), providing insights into setup procedures, best practices, and deployment strategies. By sharing practical insights, learnings, and troubleshooting tips, this session will provide attendees with the knowledge and tools necessary to optimize location based services outcomes and enhancing wifi onboarding efficiency.

### Cisco Talos and the Threat Landscape: Insights from Talos on Threats, Malware, TTPs, and AI - BRKSEC-2884
Speakers: William Largent (Cisco Talos)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272004485001zG9c
"In this session, we will explore the latest cybersecurity threats through an in-depth analysis of Cisco Talos' cutting-edge research. Our discussion will cover the current threat landscape, including the rise of sophisticated malware, the tactics of ransomware gangs, and the growing role of state-sponsored actors in cyber espionage and attacks. Attendees will gain crucial insights, equipping them to recognize and respond to these emerging threats. Leveraging Cisco Talos' extensive research, we will examine the tactics, techniques, and procedures (TTPs) of threat actors and highlight essential security technologies for defense. To conclude, we will focus on the dual role of Large Language Models (LLMs) and artificial intelligence in cybersecurity. We'll explore how these technologies are used offensively by threat actors to remove language barriers - conduct rapid, precise, and automated attacks, while also discussing the vulnerabilities they present as potential attack surfaces. This session underscores the importance of securing these advanced technologies against exploitation, empowering attendees with knowledge and tools for proactive security management.

### Cisco Unified Communications Manager (CUCM) Platform Update for On Premise Calling and Webex Calling Dedicated Instance (DI) - BRKCOL-2076
Speakers: Manish Joshi (Cisco), Justin Jordan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271856059001zlaF
Come and learn about how Cisco is committed to providing flexibility and confidence to customers through their digital transformation journey with the power of Cisco Unified Communication Manager (CUCM) platform.This session will cover Cisco's CUCM product strategy, product lifecycle changes, and high level roadmap for On-prem deployments including solution with Jabber, Webex App, Devices and Cisco Meeting Server. Session will also enable you with detailed insights on key platform updates, specifications, and compatibility requirements to help you Upgrade to CUCM 15 with confidence. You will also learn latest on Webex Calling strategy and how CUCM platform empowers customer's cloud journey with Webex Calling Dedicated Instance. Session will cover overview of Dedicated Instance & latest enhancements and discuss migration options to the latest CUCM versions, the Webex app, and Webex Calling.

### Cisco Video Endpoints Update - BRKCOL-2390
Speakers: Charlie Thorpe (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271854153001zkld
In this session, we'll explore the latest updates to the Cisco collaboration portfolio, with a focus on Cisco video devices, RoomOS, and Microsoft Teams Rooms. We'll also delve into Cinematic experiences and take a closer look at the newly released Ceiling Microphone Pro. For a comprehensive understanding of Microsoft Teams Rooms on Cisco video devices, attending session BRKCOL-2185 is highly recommended.

### Cisco XDR - Making Sense of all the Parts and Pieces - BRKSEC-2113
Speakers: Oxana Sannikova (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272007251001zshI
Join us for a session where we delve into how Extended Detection and Response (XDR) can transform your security operations and drive impactful business outcomes. We will help answer the following questions and much more! What should an XDR be? Is Cisco XDR a SIEM or a SOAR? Is it something else? Is Cisco XDR just an evolution to Cisco SecureX, or is it different? How does it work, and what is happening behind the scenes? How does Cisco XDR make my Security Response more efficient & effective? What components are critical to make an XDR an effective tool? In this session, you will get a full walkthrough of Cisco XDR feature set, and latest innovations with concrete use cases and demos that will allow you to accelerate your SOC.

### Cisco collaboration devices with Microsoft Teams Rooms - Deployment and Best Practices - BRKCOL-2185
Speakers: Charlie Thorpe (Cisco), Davide Preti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853589001zeWY
This intermediate-level session will guide attendees through the deployment of Cisco collaboration devices with Microsoft Teams Rooms. We will cover pre-configuration steps and requirements touching on Office 365 admin center and Webex Control Hub. We will explore in more detail: Office 365 admin centers Exchange Teams Intune Webex Control Hub Workspaces Devices Analytics We will cover the deployment process, including looking at supported capabilities, best practices, end user experiences and our recommendations to achieve a successful deployment. This session will also be beneficial for attendees of BRKCOL-2184

### Cisco video devices interoperability: Webex, Microsoft, Google, and Zoom - Get the latest updates! - BRKCOL-2184
Speakers: Davide Preti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853398001zzw4
This intermediate-level session provides an update about the latest features and an overview of the technology roadmap regarding the Cisco Collaboration solution and its interoperability with Microsoft, Google and Zoom. We will explore high-level architectures, supported capabilities and an overview of the newest features for the three of them. Both Cisco Rooms experience (RoomOS) and Microsoft Teams Rooms (MTR) experience will be covered. For those interested in deploying Cisco Video Devices for Microsoft Teams, with a Live demo, check out BRKCOL-2185 For those interested in Calling interop with Microsoft Teams, check out BRKCOL-2067

### Cisco wireless Wi-Fi 7 and Ultra Wideband. What is your location and uses? - CTF-1045
Speakers: Blanca Wong Mosquera (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271937663001zvGL
With the introduction of our Cisco wireless Wi-Fi 7 access point. Cisco introduced dedicated Ultra Wideband radios into the portfolio. Ultra wideband provides sub meter accuracy for location services. This will also be able to enable AP autoplacement with UWB, assest tracking use cases, and Indoor navigation via UWB. This technology enhances Cisco's portfolio to now include Wi-Fi, BLE and UWB for location based services (LBS).

### Cisco's Reimagined Workspaces: Recipes for Success - PSOCOL-1032
Speakers: Mark Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271850129001zMCE
When people returned to the office — was it the experience they expected? Are your workspaces adequately addressing the challenges of hybrid work? Cisco has been rethinking its approach to workspace design. Join this session to hear how Cisco IT, HR, and Corporate Real Estate Teams worked in lockstep to: • Create a shared vision for workspaces of the future • Understand the different purposes that Cisco properties fulfil • Transform flagship sites in New York, Chicago, Atlanta, Paris, Milan, and London • Save real-estate costs, increase occupancy levels, and reduce carbon footprint • Embrace collaboration-centric workspaces, and unassigned seating plans • Leverage rich workspace analytics to continually improve the employee experience and well-being. You'll hear how Cisco smart buildings solutions with PoE network infrastructure, Cisco Collaboration devices, and suite of cloud management tools facilitate future-ready workspaces. Plus discover resources that we've created that enable you to learn from Cisco's experience and apply standardized workspace templates that can accelerate your own workspace transformation.

### Cisco's SASE Approach - Unifying Networking, Identity and Security - BRKSEC-2286
Speakers: Fay Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272002926001zBBh
This session illustrates how Cisco Secure Access, ISE, Catalyst SD-WAN secures all applications, users and things. This session will dive into configuration and deployment of granular security controls that can be enforced across both private and public traffic, how detailed identity attributes and contextual data, represented by SGTs, can inform intelligent access decisions for users and things, and how real-time performance data and new policy result simulation can drive consistent performance and avoid downtime. This session is aimed at Network/Network Security Specialists and Architects involved in designing and building advanced security

### Cisco's Technology Blueprint for Secure and Resilient Communities - PP-1306
Speakers: Russell (Rusty) Smith (Cisco), Bongsu Cho (LG Electronics), Jen Kirkpatrick (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271948632001zdhK
Don't be susceptible to vulnerabilities — discover how Cisco's AI-powered solutions, including Meraki security systems, are revolutionizing safety and connectivity across industries worldwide. Through strategic partnerships and the Country Digital Acceleration program, Cisco integrates cutting-edge AI and Meraki cameras to monitor health and safety, creating scalable blueprints for success. Learn how Cisco's innovative technologies are driving growth, fostering digital skills, and empowering organizations to gain a competitive edge by securing their environments and operations. Key Takeaways: - AI-Driven Safety and Connectivity: Explore how Cisco Meraki's AI-powered security systems provide real-time insights to enhance public safety and connectivity, with scalable solutions for diverse industries. (Wiikwemkoong & Wichita State) - Strategic Partnerships in Action: Discover how LG Electronics uses Meraki cameras and AI to monitor health and safety, offering a replicable model for innovation and growth. - Empowering Communities Through Technology: Learn how Cisco collaborates with organizations and programs like the Country Digital Acceleration initiative to deliver secure, connected environments, ensuring safety and resilience in schools, businesses, and communities.

### Cisco's Unified Security Agent: Cisco Secure Client. Bringing AnyConnect, Secure Endpoint, Orbital, Secure Access & Umbrella Together - BRKSEC-2834
Speakers: Bill Yazji (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272011370001zmXW
We have all heard the complaints or have done the complaining ourselves: "Cisco has too many agents" or "I'm not installing another agent on our company's workstations." Come learn from Bill Yazji, while he shows you that Cisco has listened to the complaints and delivered a unified security agent called Cisco Secure Client. Cisco Secure Client (CSC) provides a modular framework allowing for AnyConnect VPN, Cisco Secure Endpoint (formerly AMP for Endpoints), Network Visibility Module, Secure Access & Umbrella Cloud Security, ISE Posture, Secure Firewall Posture (formerly Hostscan) and the Network Access Module (NAM) to all exist together; with a modern cloud-based management coming from Cisco XDR - connected intimately with XDR device insights. In this session, we will dive into the technology behind the Secure Client, how things really work and the nuances where they do not. We will cover deployment models from the cloud and using your own software deployment mechanisms. We will learn all about the seamless upgrade flows from existing AnyConnect and Secure Endpoint (AMP) agents (oh wait, AnyConnect is EOL, surely you aren't using it anymore - but just in case) Come spend some time with Bill & be entertained while learning all about this exciting development from Cisco Security.

### Cisco's Winning Playbook for the National Football League (NFL) - PP-1303
Speakers: Lynn Bloomer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271844412001z2fP
As digital innovation continues to reshape the world, Cisco is at the forefront of empowering athletes and communities through its partnership with the National Football League, bridging the digital divide. This session will delve into how Cisco leverages its advanced technology and the Cisco Networking Academy to equip students and athletes with essential digital skills, supported by a progressive education platform, cutting-edge curriculum, superior learning experiences, and an unparalleled partner ecosystem, all designed to prepare learners with real-world skills and opportunities. Hear from our Dream Team — a group of handpicked Networking Academy students and alumni who help build the networking infrastructure at large-scale events — as they share their experiences in enhancing their digital skills and securing job opportunities. Discover the strategic advantages of Cisco's partnerships, which support brand reputation and influence in key markets, and learn how these innovative efforts are setting new standards for digital engagement and empowerment. Don't miss this chance to explore how Cisco's playbook can open opportunities to tap into skilling your own talent pool while enhancing projects and driving success.

### Cisco, Netbox and Ansible - Automating your source of truth to streamline your Data Center deployments - DEVNET-2827
Speakers: Thomas Renzy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271907338001zg8b
NetBox is a popular tool that can act as a source of truth for everything that is on your network. Ansible is an open source automation tool that can be used to help provision your Cisco infrastructure. In this session, attendees will learn of the capabilities that are available to combine these tools to allow an automated, streamlined deployment of their Data Centers. This session will take attendees through the benefits, set up of the environment, and demos so that they will see the exciting capabilities that are available with all of these tools.

### Cloud Insights: Making the Invisible Visible - A ThousandEyes Technical Account Manager's Case Study Perspective - BRKOBS-1018
Speakers: Oscar Eduardo Olivares Dominguez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272016701001zuD5
Are you operating in a cloud environment where dozens or even hundreds of interconnected instances, each with its unique access rules, private and public connections, load balancers, and accelerators? These elements create a complex environment that can leave you feeling lost when troubleshooting. If so, you're not alone! In this session, ideal for IT and Operations teams, you will discover, through a Technical Account Manager's (TAM) case study, how Cloud Insights from Cisco ThousandEyes can tackle these challenges by providing time-correlated configuration changes and a comprehensive network map, reducing troubleshooting from hours to just minutes or even seconds, thereby minimizing your Mean Time to Recover (MTTR). This unparalleled visibility in the cloud enhances your Digital Experience Assurance by breaking down silos across on-premises networks, cloud environments, and beyond.

### Cloud Management of Cisco Secure Firewall - BRKSEC-2166
Speakers: Ted Bedwell (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272000968001zhVT
Cloud delivered management of secure firewall increases reliability, scalability, and capability. Join Ted Bedwell in this exploration of the inner workings of this unique solution, new innovations, and how it differs from the traditional Firewall Management Center.

### Cloud Security APIs and Splunk: Best Practices In Practice - DEVNET-2125
Speakers: Yaron Caspy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271900368001zaCM
Why did we build a Splunk Application for Secure Access/Umbrella? Hint: Its not just about data. The Cloud Security App for Splunk utilizes Secure Access/Umbrella, Investigate and Cloudlock APIs. During this session, we are going to walk you through how the different modules answer SOC, (Security Operations Center), and Threat Hunter needs, while looking under the hood to see which APIs we use, why we chose them, what the implementation looks like and how the application evolved based on customer feedback.

### Cloud-Managed Data Center Networking Made Easy: Introducing Cisco Hyperfabric AI - PSODCN-1008
Speakers: Russell Rice (Cisco), Kumar Reddy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271880174001zl4t
See how Cisco Hyperfabric AI lets you to build and manage AI clusters and fabric from one unified solution. Built atop our cloud-managed controller, Hyperfabric AI makes it easy to design, deploy, and manage clusters and fabrics across data centers, colocation facilities, and distributed edge sites. Developed in partnership with NVIDIA and VAST, Hyperfabric AI provides modular, full-stack AI infrastructure and full-stack AI development tools to deliver flexibility and scale for AI innovation.

### Cloud-spotting Amazon Web Services: Monitor your Cloud Infrastructure using ThousandEyes Cloud Insights - CTF-1034
Speakers: Mauro Caballero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271976059001zfPL
Over the last few years, cloud adoption has taken the world by storm. Gone are the days when engineers just had to worry about their own enterprise network performance, now having to provide assurance on non-owned networks. As such, cloud observability is not just a nice-to-have anymore, but a necessity. In this session you will learn how to use ThousandEyes Cloud Insights to monitor your AWS infrastructure, networks and business-critical applications, to help you reduce your Mean Time to Diagnostic/Resolution for AWS-hosted workloads.

### Common Policy to rule them all: Seamlessly Integrate SDA, SD-WAN, ACI and Cloud - BRKXAR-2001
Speakers: Markus Harbeck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271869647001zMuK
What is Cisco Common policy? Leverage Identity Services Engine (ISE) as policy broker for SDA, SD-WAN, ACI and Cloud. How can you extend your Microsegment all the way to the Cloud and your Datacenter with ACI? And what's in for you? The session will demonstrate how ISE brokers policies between the SDA-SDWAN-ACI interfaces. The session shows how to build an end-to-end policy from the campus to the data center. Design and best practices for SDA to SDWAN and ACI will be shown. Finally, a live demonstration will allow the attendee to visualize the building of the software defined enterprise and secure segmentation.

### Common policy for zero-trust network security: The unified Meraki approach - BRKARC-2750
Speakers: Alex Burger (Cisco), Jaideep Kukunuru (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971204001zjzw
Network security has been an inherent part of most network solutions for many years, however, policy definitions vary significantly between platforms and solutions. In this session, you will learn how Cisco Meraki uses a common policy approach to provide consistent, organization-wide security and network visibility across your organization. Learn how Adaptive Policy integrates TrustSec across the Meraki full-stack solutions (wired, wireless, and security) with an easy-to-deploy, consume, and operate solution that has been built in a cloud-centric and scalable design. You will learn best-practice designs leveraging enhanced segmentation and dynamic role-based access control through Meraki Access Manager to achieve agile security without requiring subnet or VLAN changes, dynamically, based on endpoint profile and user.

### Complexity: The Enemy of Security - CTF-1042
Speakers: Mike Veedock (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271994596001zWhx
In this session we'll look at the historic relationship between Security and Complexity. Learn about simple Cisco solutions that will transform your risky complex network into a reliable, safe, highly efficient machine. You'll learn tips, tricks, and tools so that you can finally get some sleep at night while being the hero of your network!

### Compliance Reporting from the Source of Truth - BRKXAR-2026
Speakers: Chad Mitchell (Cisco), Zig Zsiga (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271870442001zW9y
Compliance comes in many forms and reaches across multiple endpoint or device types. The status and enforcement of compliance adds additional complexities that require full situational awareness and network wide information that could dictate action now or action later. The Department of Defense Comply to Connect (C2C) program introduces these problems in an enterprise wide implementation mandate that can be a daunting and complex process. Thankfully, Splunk is poised perfectly to handle this problem. In this session, participants will examine the multitude of inputs and attributes that must be collected and reported on for the C2C program compliance. Using multiple data inputs from solutions like Cisco ISE, Secure Network Analytics, Secure Firewall, and multiple third party solutions attendees will see how data can be correlated and acted upon to achieve the outcomes of the C2C program while also setting the stage for Zero Trust. By the end of the session, you'll be equipped with practical ideas to identify the attributes and their sources that apply to your C2C journey and how they can be presented with Splunk to give you actionable intelligence, in real time, on the compliance of your network.

### Configuration and troubleshooting UCCE/PCCE integration with Webex Connect for Digital Channels - TACCOL-2017
Speakers: Tushar Nagpure (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271851680001zfmV
Contact Center Enterprise solutions integrate with Webex Connect to allow customers to interact with digital channels of their preference such as Email, SMS, Facebook Messenger, WhatsApp, and other channels. It facilitates bot integration powered by AI for customers to get response for common questions and escalate to live agents on CCE Finesse. This session reviews Webex Connect integration and configuration requirements and related troubleshooting.

### Configuring and Troubleshooting Catalyst Center Templates - CISCOU-3004
Speakers: ALAN GARDNER (Current Technologies Computer Learning Center INC)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271843842001zIrJ
This session covers the creation, deployment, and troubleshooting of templates in Cisco Catalyst Center, enabling efficient network automation. Attendees will learn to standardize configurations, integrate templates with policies, and resolve common deployment issues. Key topics include template design, variable implementation, policy-based automation, and troubleshooting techniques. Real-world use cases will highlight best practices for ensuring consistency and compliance. Ideal for network engineers and IT professionals seeking to optimize Catalyst Center for scalable and automated network management.

### Connecting & Securing Critical Infrastructure with Industrial Networking in an AI-Native World - CENIOT-1149
Speakers: Massimo Mistretta (Planet Farms), Daniel Mastropietro (THE WALT DISNEY COMPANY), Samuel Pasquier (Cisco), Keith Higgins (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592614030001XQec
In an era where AI and automation are redefining industry landscapes, operational networks are at the heart of this transformation. Critical infrastructure sectors such as manufacturing, utilities, and transportation face escalating cybersecurity threats, operational complexity, and a global shortage of skilled labor. Amid these challenges, the demand for data-driven capabilities, AI-ready infrastructure, and digital resilience is rising. Industrial networks play a pivotal role as enablers for AI use cases within the industrial sector, driving significant advancements and efficiencies. In this session, we will explore how AI-driven innovations and IT principles—such as network automation, software-defined networking, and advanced cybersecurity frameworks—are revolutionizing OT networks. Discover how these technologies are essential in overcoming labor shortages, enhancing productivity, and ensuring workplace safety, while enabling industries to swiftly adapt to evolving demands. Join us to explore strategies and solutions driving sustainable growth and resilience in today's technology-driven environment, uncovering the future of industrial networks and their profound impact on modern industries.

### Connecting Beyond Fabric: Catalyst 9000 BGP EVPN Handoff Scenarios - BRKENS-2652
Speakers: Manish Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921644001zI87
Explore how Catalyst 9000 switches enable seamless connectivity between your VXLAN EVPN campus fabric and external networks. This session dives into practical handoff scenarios, including interconnecting with data centers, WAN, and legacy networks. Gain insights into configuring and optimizing BGP EVPN handoffs to ensure scalability, resilience, and secure integration with the outside world. Whether you're extending your enterprise network to the cloud or bridging different environments, this session provides the tools and strategies needed for a smooth transition. Join us to unlock the full potential of your Catalyst 9000-based campus fabric!

### Connecting Your Data to LLMs: Identity, Functions and Agents are all you Need - BRKETI-2411
Speakers: Guillaume De Saint Marc (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915660001znU9
To truly exploit the benefits of Generative AI, most organizations need to connect their data to LLMs, but the challenges immediately start to pile up. Indeed, most organizations would like to use the data in their current systems just as they are today, without going through data adaptations and cumbersome migrations. Moreover, many organizations need to bring Generative AI to their data (e.g., residing on prem or on their own datacenters) instead of moving the data to models hosted in public clouds. In this session, you will learn about new architectures and tools enabling to connect your data to LLMs under your control. You will learn new techniques to inspect user prompts in real time and automatically: Identify and confirm the data required to complete the request carried in a prompt Determine whether the user has rightful access to such data Serve 'the right' data Finally, you will learn about Cisco's innovations in this space and the tools available for connecting your data to LLMs.

### Connecting and protecting educational institutions in the AI era - PSOIND-1018
Speakers: Mary Schlegelmilch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271944495001zL1I
In the AI era, educational institutions are integrating AI technologies to enhance learning experiences, personalize education, and improve administrative efficiency. AI facilitates adaptive learning platforms, data-driven insights for student performance, and streamlined campus operations. However, this increased connectivity also introduces cybersecurity challenges, necessitating the protection of sensitive student data and institutional systems. Educational institutions must implement comprehensive security measures, including data encryption, secure access controls, and ongoing cybersecurity education for staff and students. By combining AI advancements with robust security frameworks, educational institutions can foster innovation in education while safeguarding data privacy and maintaining trust.

### Connecting and protecting financial institutions in the AI era - PSOIND-1020
Speakers: Al Slamecka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271944877001zVzq
Cisco is revolutionizing how infrastructure and data connect and protect financial institutions in the AI era. We uniquely power how people and technology work together – across the physical and digital worlds – to unlock innovation and productivity. See how financial institutions can combine AI innovations with strong security practices, to offer improved services while safeguarding customer trust and data integrity.

### Connecting and protecting government agencies in the AI era - PSOIND-1016
Speakers: Matthew Dietz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271944116001z0xe
In the AI era, government agencies are adopting AI technologies to enhance service delivery, improve decision-making, and streamline operations. These advancements enable better data analysis, efficient resource management, and more responsive resident services. However, the increased use of AI also presents significant cybersecurity challenges, requiring robust measures to protect sensitive information and critical infrastructure. Agencies must implement strong security protocols, real-time threat detection, and comprehensive training for personnel to safeguard against cyber threats. By integrating AI-driven solutions with stringent security practices, government agencies can enhance operational efficiency while ensuring the protection of data and public trust.

### Connecting and protecting healthcare organizations in the AI era - PSOIND-1014
Speakers: Kyle Roach (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271943931001z45w
Cisco is revolutionizing how infrastructure and data connect and protect healthcare organizations in the AI era. We uniquely power how people and technology work together — across the physical and digital worlds — to unlock innovation and productivity. See how organizations are using AI-driven tools to securely improve patient care, streamline operations, and enhance data management.

### Connecting and protecting manufacturing organizations in the AI era - PSOIND-1017
Speakers: Carlos Rojas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271944310001zflX
In the AI era, manufacturing organizations are leveraging AI technologies to enhance connectivity and optimize their operations. These advancements enable real-time monitoring, predictive maintenance, and improved supply chain efficiency. However, as connectivity increases, so do cybersecurity risks. Protecting these organizations requires implementing robust security measures, such as network security protocols, employee cybersecurity training, and AI-driven threat detection systems. By integrating AI solutions with comprehensive security strategies, manufacturers can drive innovation, efficiency and new ways of working while safeguarding their operations and data integrity.

### Connecting and protecting retail businesses in the AI era - PSOIND-1019
Speakers: Derek Dykens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271944684001zAks
In the AI era, retailers are harnessing AI technologies to enhance customer engagement, optimize inventory management, and streamline operations. AI enables personalized shopping experiences and efficient supply chain management through data-driven insights. However, increased connectivity also raises cybersecurity concerns, making the protection of customer data and retail systems paramount. Retailers must adopt robust security measures, including encryption, secure payment systems, and staff training in cybersecurity practices. By integrating AI innovations with strong security frameworks, retailers can drive growth and maintain customer trust while safeguarding data integrity.

### Connectivity beyond the basics: Design and Deployment tips for MESH, WGB and URWB - BRKEWN-2049
Speakers: Dave Benham (Cisco), Ian Procyk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941027001zNaE
Have an upcoming project requiring pervasive outdoor coverage? Looking for gudiance on wireless bridging? Perhaps you have some questions related to our workgroup bridge or the newly announced integration of URWB on the 9800/APs. This session aims to address these questions with practical, real-world deployment examples and test results.

### Conquer Complexity: Unified Branch Solutions for Simplified Security and Network Operations - CENENS-1503
Speakers: Kris Rangarajan (Cisco), Ralf Huebenthal (Nestle), Lee Peterson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592613850001Xkdx
The branch is changing - businesses are navigating the complexities of cloud migration with direct internet access, increased security threats with more unmanaged devices and Post Quantum Cryptography, and a need for WAN modernization to meet new bandwidth requirements and expanded connectivity demands across multicloud environments. To address this, they seek solutions that offer simplified management with fewer vendors across networking and security without compromising performance. In this session, we'll introduce a unified branch approach, integrating routing with embedded security, switching, Wi-Fi, and ThousandEyes, all managed by a platform dashboard. With optional branch as code and success tracks, business will have the foundation for efficient management, visibility, and control across your entire network infrastructure.

### Considerations on Data Center Sustainability - BRKDCN-2625
Speakers: Arvind Durai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884067001zAQ9
The impact of carbon emissions and the need to be more conscious of the effects of IT operations and solutions in the context of environmental goals is rapidly becoming a key topic. In this session, we will introduce the topic with some non-obvious concepts and facts and give an overview of elements within Cisco UCS X-Series, Intersight, and cloud networking offerings that can help advance organizations towards achieving these goals. As more data and processing needs exist, and are growing rapidly everywhere from the cloud to edge, providers and customers are exploring methods to reduce the impact on the environment from all operations, including the key area of IT.

### Cracking the Code: How to Outsmart AI-Driven Cyber Attacks - CNCSEC-1010
Speakers: Jagpreet Singh (EnterOne)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271990935001zpqe
>Learn how Today's AI threats bypass traditional defenses—and how you can reinforce your network for what's coming next. Join EnterOne to explore how Meraki, SD-WAN, Cisco Secure Access, Splunk, and CyberVision work together to build secure, cloud-managed networks with full visibility and control from edge to cloud to industrial environments. Learn how to simplify network operations, strengthen your security posture, and protect against Today's evolving threats—including those driven by AI. Whether you're planning a new deployment or optimizing your current setup, EnterOne provides the training and implementation services to help you move from strategy to execution with confidence.

### Cracking the Code: Three Leadership Secrets AI Can't Master - IF-1028
Speakers: Kurtis Yang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949786001zVXF
As AI technology continues to reshape the workplace, the role of human leadership becomes more crucial than ever. In this session, we explore how successful leaders can harness the power of AI while maintaining essential human qualities such as empathy, creativity, and strategic thinking. We'll discuss how inclusive leadership fosters teamwork and drives sustainable success. While AI excels at automating processes and analyzing vast datasets, it is the human leader's ability to inspire, guide, and connect with people that truly propels organizations forward. Join us to learn what it takes to not only survive but thrive in the AI era, leading your organization to new heights.

### Crafting Tests at the Speed of your Network - BRKATO-1009
Speakers: Aaron Carter (Cisco), Nandakumar Arunachalam (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271832638001ze2o
In today's environment generative AI has significantly accelerated the pace of software development so use this same generative AI for test development. Embark on the frontier of cutting edge testing methodologies with Behavior Driven Development (BDD) using Cisco's CX Test Automation Manager (CXTM), Python, Robot Framework and Github CoPilot. With an advanced framework like CXTM you are enabled to create sophisticated testing capabilities and using a generative AI tool like Github CoPilot you can rapidly development python code wrapped into BDD tests written in Robot Framework. Now, combine all this to pave a way for collaborative testing with Cisco devices via CLI, REST API and NETCONF for your organization's network. In this session we will walk through strategic methods of achieving accelerated test development validating network environments. Attendees will walk away with an enhanced grasp of validating and testing their network, accelerating the pace of their operations.

### Create Future-Ready Workspaces with Cisco Workspace Designer - PSOCOL-1031
Speakers: Marte Holt Sannesmoen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271849942001zfrr
AI is unlocking human potential by improving employee experiences, enhancing collaboration and raising productivity. But are your workspaces ready to capitalize on this potential? Join this session to discover how Cisco is helping organizations to: • Simplify and accelerate workplace transformation with hardware that can be customized for your needs. • Create spaces that leverage AI-powered camera and audio-intelligence that enables immersive, equitable, and secure collaboration. • Deliver consistent user experiences in any workspace, on any platform — Webex, Microsoft Teams, Google, and Zoom. • Provide IT, HR, and Corporate Real Estate with blueprints featuring equipment lists, installation guides, and room coverage charts. We'll also demo the new Cisco Workspace Designer, featuring the latest Cisco collaboration devices such as the Ceiling Microphone Pro, and cinematic meeting experiences with Cross-View. Plus, hear about smart buildings integrations for room booking and hotdesking with Cisco Spaces.

### Creating Digitally Resilient Meraki Networks with Splunk and ThousandEyes - BRKOBS-2100
Speakers: Sam Scudere-Weiss (splunk), Steven Carter (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271983082001zEOx
Telemetry is key to prevent, detect, and respond to events that could disrupt digital experiences and impact business performance. This session, featuring numerous demonstrations, explores the telemetry data available in Meraki, including syslog, NetFlow, APIs, and ThousandEyes Agents, and focuses on transforming this data into actionable insights using Splunk. Using the integration of data between Meraki and ThousandEyes and leveraging the AI/ML tools in Splunk to filter noise and enhance data utility, we transform otherwise unmanageable data into actionable intelligence. Finally, we show how IT Service Intelligence (ITSI) aggregates the collected data into a comprehensive view of service-level health, enabling quick detection and resolution of issues without constant dashboard monitoring.

### Creating Efficient and Scalable Intersight Architectures for large Enterprise and MSPs - BRKCOM-2019
Speakers: Matthew Faiello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861568001z85s
Cisco Intersight Infrastructure Service (IIS) brings powerful and scalable capabilities to efficiently manage Large Enterprises and Managed Service Provider (MSP) use-cases. This session will focus on various design considerations, features and functionalities of Intersight that make these large management models scalable, efficient and powerful. From robust and granular segmentation (down to a server per server basis), to scheduled Firmware Upgrade operations, to the new role-based access control (RBAC) model, that provides the most granular permissions for modifying existing or creating new roles, Cisco Intersight is setting the bar once again for powerful server infrastructure management. Need visualization into performance metrics? Cisco Intersight provides robust, and ever-evolving Metrics Collection and Explorer capabilities to put graphical data points at your fingertips to help troubleshoot and ensure the health of your UCS ecosystem. Intersight is growing and emerging and we've listened to and incorporated many feature requests at the suggestion from our customer base. Come learn and also get a glimpse of what's around the corner - with Cisco Intersight!

### Creating an Application-Optimized SASE-Enabled Architecture - BRKXAR-1000
Speakers: Kyle Barnes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271869459001zLdA
There is a growing landscape of applications, users, and devices on the move. Today's IT teams face a common challenge: securing the network while minimizing complexity. SD-WAN, SaaS, multicloud, etc. what are all of these things, why do you care about them, and what value do they bring individually as well as collectively? The intent of the session is to touch on these points while assisting the participant in understanding how the different pieces of the Secure Access Secure Edge (SASE) puzzle fit together. This session will cover Umbrella, SD-WAN, Cisco SaaS, and ThousandEyes fundamentals. A baseline understanding of enterprise architecture is recommended, but not required.

### Cross Architecture Approach to AI - AIHUB-1009
Speakers: John Cuneo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866377001zivV
Interest in AI has exploded in the past year, thanks in part to the popularity of ChatGPT and subsequent GPT implementations. Organizations across all verticals are evaluating and building strategy around how AI driven technologies can transform business processes and customer engagement. With this, teams are facing new challenges and considerations to deliver architectures that meet the demand and scale of these solutions. This speaker led session will cover an overview on how to approach and design a scalable architecture for AI workloads. The session will cover how Cisco's platform approach can handle density and scale of training models, with the simplicity and management to deploy inferencing at scale. Attendees will leave with a roadmap to explore the power of AI while maintaining the controls and sovereignty over their data.

### Crosswork Planning using Predictive Analytics to power AI OPS - BRKOPS-1643
Speakers: Julia Palomino (Cisco), Fung Lim (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271987808001zcF1
Crosswork Planning was recently introduced to the market. This next generation microservices-based architecture, with modern GUI, is the successor to WAE, the World's leading network planning tool. Join us to hear how you can use this predictive analytics operation tool for proactively managing the capacity of your IP core network. This session will start at the basics and cover among other topics: Modeling - Network Model construction and validation Visibility - Visualize your network and traffic in a single pane of glass De-risking - Automate worse-case failure analysis of the entire network Capacity Planning - Plan for the future and minimize spend Optimization - optimal metrics, optimal Segment Routing paths This will be a combination of slides (argh! kept to a minimum) and live demos (much more fun!) Attendees will walk away knowing that Crosswork Planning has been built by network Engineers for Network Engineers. Look forward to welcoming you to the future of network planning.

### Customer Case Studies: Lessons Learned from the Cisco SD-WAN Design Council - BRKENT-2660
Speakers: Tom Kunath (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271934571001zCWI
In this session, we discuss lessons learned from different non-typical SD-WAN designs submitted to the Cisco design council. These will be presented as anonymized case studies, highlighting the diverse set of Catalyst SD-WAN connectivity and security features that our customers have deployed to meet their unique business needs. Example designs and best practices will be provided for multiple industries, such as retail, financial services, healthcare, energy, and transportation.

### Cybersecurity Compliance: Accelerating Global Market Access, FedRAMP and Beyond - ITLGEN-2058
Speakers: Kaly McKenna (Beacon Global Strategies), Shaina Tamburr (Cisco), Mike Witzman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271957249001zKZH
In today's rapidly evolving global dynamics, organizations face unpredictable geopolitical tensions, increasing cybersecurity threats, and ongoing national security challenges. Coupled with an explosion of data, a wave of compliance regulations has emerged across all markets necessitating an accelerated unified, standard framework of products across all segments and geographic markets to safeguard our customers and national assets. In this session, Shaina Tamburr, VP of Market Access Revenue Acceleration, and Mike Witzman, VP of U.S. Public Sector, will discuss how Cisco is accelerating compliance for the United States Public Sector, EU, and defense sectors. They will share examples of how improved time-to-market enables customers to achieve business outcomes and realize value more quickly. Guest speaker Kaly McKenna, VP at Beacon Global Strategies, decorated combat pilot, and the first military fellow to the Defense Innovation Board, will join Mike for a fireside chat. The discussion will provide insights into IT modernization, artificial intelligence (AI), the evolving regulatory landscape, and their implications for government and industry.

### Cybersecurity Threat Intelligence Ecosystems - BRKSEC-1187
Speakers: Jeremy Stanley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271998376001zDRY
U.S. critical infrastructure faces risks as cyber adversaries exploit vulnerabilities with wide-ranging impacts. Timely threat intelligence is vital for regional cybersecurity strategies. This session covers the history of threat intelligence sharing, the development of these ecosystems, and their importance to communities and regions nationwide.

### DHCP Relay deep troubleshooting in ACI Fabric - TACDCN-2017
Speakers: Jason Thompson (Cisco), Antonio Perez Oseguera (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271881915001zAv4
Will focus on advanced techniques for diagnosing and resolving complex issues related to DHCP relay in network infrastructures. Targeted at network engineers and IT professionals with a foundational understanding of DHCP, the session will cover the inner workings of DHCP relay agents, misconfigurations, and advanced troubleshooting methods.

### Data Center Migration - Moving your critical workload without disrupting your business - BRKDCN-2957
Speakers: Davis Creemer (Cisco), Joshua Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271890761001z4dM
Data Center Migration is becoming a common and critical task for many companies around the world, whether it is a move to a new co-lo or a transition to a new DC fabric. In this session we will look at the challenges in bridging DC networks, and provide successful strategies for effective migration. We will cover challenges of Layer 2 Extension and strategies around asymmetric routing. Examples will include migration between similar and dissimilar fabric types including classical 3-tier architectures, ACI, and VXLAN EVPN.

### Data Center Network Design for the Media and Entertainment Industry - BRKDCN-2924
Speakers: Chris Lapp (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271888830001z9FM
The media broadcasting and entertainment industry is going through a massive transition as it moves from legacy SDI to IP networks for live production. The network built to carry this workflow must offer reliable transport of video and audio streams along with distribution of timing using precision time protocol. This session will help educate network admins on how to build the network by leveraging Cisco's non-blocking multicast and will introduce the Cisco IP fabric for media. The session will also go beyond production and cover network design for other use cases such as playout, contribution, and other file-based workflows which are relevant to the media industry.

### Data Center Operations Maintenance and Migration Best Practices - BRKDCN-2958
Speakers: Anis Edavalath (Cisco), Arvind Durai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271890950001zHYg
This session will cover the best practices and solutions that help plan the change window and migrations with minimal disruption to the existing production environment. Attendees will understand the solutions to deal with planned and unplanned outages in ACI, VXLAN, and traditional VPC environments. The session will also cover the capabilities and features of the Nexus platform that assist in isolation strategies, image management, performance monitoring, and hardware migrations. Attendees will also be introduced to migration strategies for modernization, scaling, and lifecycle management.

### Data Center Security Overload - Architecting Networks for AI Scale - CENDCN-1379
Speakers: Craig Connors (Cisco), Neil Anderson (World Wide Technology, Inc), Murali Gandluru (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592612027001XJMt
This session will show how Cisco is transforming network architecture by integrating advanced security and services directly into the network fabric. Discover how this innovative approach optimizes network performance, strengthens security, provides actionable insights, and reduces costs. We'll demonstrate how Cisco Hybrid Mesh Firewall and Splunk Distributed Analytics transform traditional trade-offs into competitive advantages, enabling you to build networks that are simultaneously faster, more secure, and easier to manage. Leave with concrete strategies to evolve your infrastructure beyond legacy constraints and deliver the performance and protection your organization demands.

### Data Center and Campus Design: Innovations in Power and Cooling Systems - CENGRN-2100
Speakers: Denise Lee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592614754001XeoP
Cisco is at the forefront of shaping the future of energy, playing a critical role in innovating and transforming the energy landscape. We believe we must sustainably design and future-proof energy grids, buildings, networks, data centers and technology for whatever energy requirements are around the corner - whether that's AI or whatever comes after. Cisco understands the urgency of designing and future-proofing energy systems with new innovations in power and cooling solutions. As technology evolves, so too must our energy infrastructure, so that we can meet emerging demands efficiently and sustainably.

### Data Driven insights Leveraging the Power of Hypershield Telemetry - BRKOPS-2344
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271986409001zzaM
Cisco Hypershield provides a next-generation solution which integrates security both into the host and workload, as well as embedded into the network fabric — and it also provides a wealth of data which can be leveraged for analytics, security, and observability. What happens when you take advantage of this data to drive next-generation outcomes leveraging analytics platforms like Splunk? Come to this session to find out! The dynamic duo of Errol Roberts and Dave Zacks, both Cisco Live Distinguished Speakers focused on Hypershield, will explore the ins and outs of Hypershield deployments — examining the capabilities that Hypershield offers, and outlining how to go about deploying Hypershield to create the inherently secure, self-qualifying network infrastructure to support your most critical applications — and tying Hypershield in with powerful analytic platforms like Splunk for unmatched visibility and security analytics. Attendees at this session will be taken on a tour of what Hypershield consists of, exploring the data sets that are generated at each level of the stack, from the host to the workload, and through the network. Come to this session to see the next generation of data driven outcomes in areas such as AI-enabled segmentation, distributed exploit protection, workload-level insights, and network-based enforcement recommendations, leveraging critical technologies such as eBPF and other telemetry agents and available platform integrations!

### Data resiliency powered by AI - Cisco solutions you can leverage - BRKOBS-2005
Speakers: Robert Mandelbaum (Splunk / Cisco Systems, Inc.), Leila Reyhani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271980299001zKB8
Cisco's investment in AI-powered observability and security solutions provides valuable options for customers who prioritize data resiliency and protecting their data in their infrastructure from evolving cyber threats. The ability to proactively identify and respond to potential breaches, leveraging AI, is a significant value proposition. In this session, we explore with customers how AI solutions have evolved, highlight some of the key capabilities that AI solutions offer today, and demonstrate how key cisco capabilities can be used to enhance data resiliency. Helping them to understand the ways cisco offers on monitoring their LLM deployments internally and externally.

### Day 0 to Day N with Meraki Dashboard - DEVNET-1220
Speakers: Shweta Palande (Cisco), Oren Brigg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271911636001zXlv
In part 1 of this session we will learn how to Create, Configure and deploy Meraki networks that includes security appliances, switches, and wireless APs. Learn the basics of organization and network creation and how to harden your networks through firewall and policy configuration. Once your networks are deployed see how you can use the Dashboard to monitor your networks and Meraki Insights to optimize your deployments. In the part 2 of the session, we will learn how APIs can be used to confidently and repeatedly deploy changes across multiple sites using different tools of automation such as Cisco Workflows, Python scripts, IaC tools like Ansible or Terraform. In addition, we will demonstrate how easily webhooks can be setup to support event driven monitoring. Finally, learn how APIs can be used to build consolidated dashboards for what your organization cares about. This session will help you get started with essential things you need for configuring your Meraki Network from Day 0 to Day N with the power of APIs and simplicity of Meraki. This is a hour and 45 minute double session.

### Decoding Site Reliability Engineering Through Catalyst Center - BRKOPS-2343
Speakers: Bansari Trivedi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988796001zNKn
With the ever-increasing demand for visibility, observability, and compliance, the expectations on operations teams have never been higher. One of the biggest challenges now is effectively maintaining infrastructure and inventories while ensuring reliability. As customers modernize their infrastructure to meet the needs of AI, the role of Site Reliability Engineering (SRE) has become critical in navigating this complexity. How can you leverage automation and AI-driven insights to streamline and fast-track the operational journey of devices using Catalyst Center? This session will focus on providing strategies to integrate Catalyst Center into your SRE lifecycle. You'll gain practical guidance on using automation, optimizing network management, and ensuring continuous improvement in technology, infrastructure, and IT processes. By leveraging these insights, you'll empower your team to not only maintain infrastructure but drive efficiency, reliability, and innovation at scale.

### Deep Dive into Cisco's Use of QUIC, MASQUE and OS Native Capabilities to Deliver Frictionless Zero Trust Access - BRKSEC-3027
Speakers: Vinny Parla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012757001zOOu
Zero Trust has not yet reached its full adoption potential in the market, largely due to the degree of friction for both end users and IT administrators. Cisco's design goal is to develop Zero Trust solutions that frustrate attackers, not users. The experience should be as seamless and easy-to-use as turning on a Wifi connection. In this Tech Talk, we explore technologies that can help us deliver on this frictionless vision in collaboration with ecosystem partners such as Apple, Google, and Samsung. This session will examine industry standard protocols such as MASQUE as well as other technologies like WebAuthN, passkeys, and private 5G access that will eventually make Frictionless Secure Access as ubiquitous as Wifi in the enterprise and home. The session will also provide for an overview of native OS clients from Apple & Samsung as well as the Cisco Zero Trust Access module built into Cisco Secure Client, and how they leverage industry standards such as MASQUE and QUIC to deliver a seamless Zero Trust Access user experience.

### Deeper Insights with 2Ring Historical Reporting for Webex Contact Center - VILCCT-1010
Speakers: Ossamah Shabbir (2Ring America, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271862534001za4t
World Premiere! Get an exclusive first look at the highly anticipated 2Ring Historical Reporting add-on for Webex Contact Centers. Be among the first to sign up for a free public preview offer! PLUS, discover why so many Webex Contact Centers already rely on 2Ring Dashboards & Wallboards for powerful real-time reporting and alerting. Learn about its core benefits, recent feature additions, and upcoming AI-centric enhancements. If your contact center is already on Webex Contact Center or planning to migrate soon, this is a session you don't want to miss.

### Definitive Intermediate System to Intermediate System (IS-IS) - BRKENT-2009
Speakers: Elvin Emilio Arias Soto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933027001zWYm
IS-IS is a link-state routing protocol commonly deployed in service provider networks as well as in enterprise and data center environments, thanks to its exceptional flexibility. Besides regular IPv4/IPv6 routing, IS-IS is a vital component of many technologies including OTV, FabricPath, Shortest Path Bridging, ACI, or SD-Access. Due to its OSI heritage, IS-IS is not as easy to grasp as native IP IGPs, even though it ranks among the best-designed routing protocols ever. This session aims to be a definitive IS-IS resource and targets service providers, enterprise and data center network engineers and operators, as well as IS-IS enthusiasts. The session will cover the in-depth protocol details of the database flooding mechanics, Designated Intermediate System (DIS), Link-state Packets (LSP), levels, areas, network types, narrow and wide metrics, and Type-Length-Values (TLVs) making it easy to understand IS-IS comprehensively. The session focuses mostly on IOS-XE and IOS-XR, but will also touch NX-OS.

### Deliver Exceptional Employee Experiences with AI-powered Webex Suite - PSOCOL-1029
Speakers: Nandita Gupta (Cisco), Anwaar Al Zireeni (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271849551001zSxq
Webex Suite is a comprehensive, AI-powered collaboration solution with 8 powerful workflows, built for Today's modern work. Join us in exploring how our collaboration platform brings high fidelity, context, and automation with maximum flexibility to everyone, on any device. With an open ecosystem of AI integrations and seamless compatibility across various SaaS tools, data sources, and custom workflows, Webex Suite is redefining collaboration by harnessing the power of AI to enable and empower people and teams to do their best work together, anywhere. Get a peek behind the curtain with an in-depth session that explores our latest innovations transforming the workplace and enhancing collaboration. You don't want to miss this session!

### Delivering on the Promise of the AI-Ready Campus and Branch: Smart, Secure, and Scalable Networks - KDDNWT-1000
Speakers: Greg Dorai (Cisco), Lee Peterson (Cisco), Aruna Ravichandran (Cisco), Jeff Paynter (Duke University Health System Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591953291001p10G
You've seen our vision, and you feel the impact AI is having on your network. Now, dive deep into how you can put our Cisco Live announcements to work, today. In this technical keynote deep dive, we will unveil the architecture and innovation required to deliver a truly AI-Ready Secure Campus and Branch network. See live demos of new products, infrastructure blueprints, and better ways to secure your organization against AI- and quantum-led threats. We will also introduce the Cisco Unified Branch, automating networking operations across routing, switching, wireless and security, delivered as code via validated design best practices. Bringing it all together is a simple, sophisticated, and AI-powered approach to management. Whether you've built your network on Catalyst, Meraki, or a mix of both, Cisco's platform will simplify operations and enable continually assured performance at every hop. Don't miss this opportunity to hear from product leaders how they have built innovations into these new products and are creating a stronger foundation for the Secure Campus and Unified Branch.

### Delivering the Best Healthcare Experience from Your Splunk Platform with Intelligence from NETSCOUT - CNCOBS-2001
Speakers: Ray Krug (NETSCOUT), Oleg Kostukovsky (Splunk)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271975464001zM7f
NETSCOUT AI Insights harnesses the power of packet data, transforming it into intelligent actionable metadata beyond overwhelming data streams and flows. By integrating with Splunk, this unified platform empowers IT teams to quickly identify and resolve issues more efficiently with fewer resources, significantly cutting downtime and outages in critical healthcare systems ensuring they are reliable, safe, and secure and deliver an improved patient experience.

### Demystifying Wi-Fi Throughput in Meraki Environments - BRKTAC-3004
Speakers: Brian Swanson (Cisco Meraki)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272019794001z9Ug
Join me in a deep dive of Wi-Fi throughput related concepts. We'll explore data rates, PHY technologies, spatial streams, and more. Learn about how these concepts tie together with throughput and where they intersect with the user experience. As a bonus, I will show you how to leverage the Meraki Dashboard to utilize these concepts to better support your users.

### Demystifying cloud security architectures - BRKSEC-3024
Speakers: Anubhav Swami (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012370001zIUH
Applications and workloads are deployed across diverse environments, presenting challenges in developing a security architecture that delivers unparalleled security, agility, scalability, and cloud-agnostic solutions for all your infrastructures. This session will confidently guide you through designing and architecting a secure cloud environment using Cisco Security solutions, including Secure Workload, Multicloud Defense, Hypershield, Isovalent (Cilium and Tetragon), and Secure Firewall.

### Demystifying the Role of AI in Your Cisco Wireless Deployments - BRKEWN-3007
Speakers: Vishal Desai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271939836001ztgb
Whether your wireless network runs on simplified IT management through Meraki Cloud or leverages the richness of wireless features with on-premises Cisco Catalyst Center, your wireless network is only as good as your ability to optimize it. In today's world, filled with many AI/ML applications for essential and ubiquitous services like Wi-Fi, it only raises the question of how AI/ML can really help deliver stable and yet best-in-class experiences to meet capacity needs, and maintain SLAs for your 5GHz and 6E wireless clients. But models generated by AI/ML are only as good as your data lake! With the right data and the right approach, it can multiply tenfold the efficiency of your network operations, your management and troubleshooting, but if you don't know how to use it, it is just like a laser saber without a battery!! In this session, you will learn about under-the-hood details of powerful Applied AI-based applications available for both cloud-managed and on-premises Cisco wireless platforms. You will also learn Applied AI is enabling closed-loop optimizations that transform your wireless networks, maximizing client experiences, and making network operations more efficient by leveraging AIOps to automatically tune your wireless networks with tailor-made config recommendations based on the unique RF signatures, all of this done without compromising your privacy.

### Demystifying the World of Passkeys - BRKSEC-2202
Speakers: Clayton Ballreich (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272002145001zkrp
Pop-up windows, fingerprint icons, symbols, keychains, profiles, code scans, device managers...when did logging in get so complicated? Users are confused by all the login option variations; administrators are confused by various terms and technologies like WebAuthn, and password-less. In response, the security industry has coined the term passkey, which is being pushed as the ultimate replacement of the password, but what is a passkey, really? During this session, participants will learn the technologies that make up passkeys, how they are secured, stored, shared, and used, and what vendors are delivering when they advertise a passkey solution. Participants will also gain confidence to implement passkeys quickly and at scale. Additionally, this session will cover the rapid evolution of passkey implementation and show practical examples of how the Cisco Security portfolio can help implement, use, broker and increase passkey adoption. Experience managing authentication is expected for this session.

### Deploy FTD and FMC on Google Cloud Using Terraform - DEVNET-2983
Speakers: Jeroen Wittock (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271908512001zmJl
In this lab, attendees will be guided through the steps to deploy FTD firewall and FMC management center on Google Cloud Platform using Cisco's terraform provider. We will deploy an FTD and an FMC. We'll register the FTD in FMC so that we can manage the firewalls with Terraform. And finally we will push policy to the firewall with Terraform managing the FMC. This will clarify how Terraform with Cisco Firewalls could be used in the context of policy as code, security as code, DevSecOps, or simply how you can use Terraform to automate managing your firewalls.

### Deploying Catalyst and Meraki to Support Any User At Any Location - BRKENS-2611
Speakers: Darren Leisen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921455001zNL9
Organizations of all sizes must provide modern services for all their workforce, whether in a large city or an isolated remote location only accessible by float plane. With the advent of low-cost and widely available satellite/5G connectivity, the demands on shared services networks have never been greater. Attendees will gain insight into refactoring distributed WAN, MAN, and campus networks using Meraki and Catalyst platforms where they best fit. The Meraki Dashboard will be showcased using existing Catalyst switching and new Wi-Fi 7 APs for branch sites connected by Catalyst SD-WAN. Participants will also follow the journey of collapsing dedicated metro area networks into a zero trust policy-driven network fabric used by multiple departments, each with unique security needs. Presenting this session is Darren Leisen, a Solutions Engineer with 20+ years in healthcare, finance, energy, and public sector organizations who directly designed and supports the network deployments this session examines. Attendees will see how to connect and protect every device across their sites and triage issues using assurance and AI. Come to this session to see how hybrid Catalyst and Meraki deployments can be leveraged to build your own solutions!

### Deploying Cisco Catalyst Center with CICD - DEVNET-2176
Speakers: Keith Baldwin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271901726001zPsy
This session expands your knowledge and delves into CICD and how pipelines may be leveraged with Cisco Catalyst Center (formerly Cisco DNA Center). We will discuss REST API and how to leverage templates and external data sources in conjunction CICD pipelines. Here we will demonstrate the use of a realistic set of predefined Rest-API collections, and templates and an external data source in a controlled environment for the following tasks, utilizing CICD pipelines: Build Hierarchy Assign Settings, Credentials and Telemetry Device Discovery Retrieving Network Inventory Template and Project Deployment This session builds your knowledge in utilizing Rest-API with CICD pipelines and Ansible for orchestration over Catalyst Center.

### Deploying IPv6 Routing Protocols: Specifics and Considerations - BRKIPV-2418
Speakers: Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271955909001za5u
Even though all major IPv6 routing protocols are rooted in their well-known IPv4 counterparts, they all come with their own unique set of idiosyncrasies. And when faced with the task of deploying an IPv6 routing protocol along with its IPv4 variant, there are often multiple ways of doing it - but the best choice is not always obvious. The goal of this session is to discuss the specifics of IPv6 support in OSPFv3, IS-IS, EIGRP, and BGP in IOS XE. For each of these protocols, we will do a quick IPv6-focused refresher, and then focus on the protocol's unique IPv6 traits (and quirks). We will also look at how the protocol supports the co-existence of IPv4 and IPv6, and if there are multiple options to choose from, we will discuss the pros and cons of each of them. To benefit the most from this session, it is highly recommended to have a working knowledge of routing protocols in general.

### Deploying MPLS/SD-WAN Gateways for a Secure and Agile Access Network - BRKMPL-2257
Speakers: Chad Hill (Cisco), Patrick Evangelista (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271969483001zNz9
SD-WAN is an essential technology that drives the success of modern networks. Leading enterprises increasingly turn to SD-WAN for its unparalleled cost-effectiveness, robust security, agility, flexibility, and superior network performance. This session will highlight how service providers can maximize these benefits by seamlessly interconnecting SD-WAN with MPLS networks using Inter-AS options. Participants will delve into compelling real-world use cases and discover how SD-WAN effectively meets urgent connectivity needs while also providing flexible solutions for rural, mobile, and transient locations. Additionally, we will explore the exciting potential of integrating SD-WAN with SRv6 networks for a native IPv6 transport solution.

### Deploying Nexus Dashboard in Your Organization - BRKDCN-2914
Speakers: Matthias Wessendorf (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271888449001zDgv
This technical breakout will provide an end-to-end view of deploying and operating Cisco Nexus Dashboard, which provides unprecedented simplicity by integrating operational services to manage customers on-premises and in cloud and hybrid fabrics through a single dashboard. You'll learn that by using the Cisco Nexus Dashboard, IT operations teams can seamlessly navigate all aspects of infrastructure lifecycle tasks from initial configuration and capacity planning to running and troubleshooting the entire IT infrastructure. Understanding how an infrastructure is deployed for usage of new tools and methodologies in your organizations is one side, but effectively operating the infrastructure is the other side. This session will review some common tasks and activities for deploying and operating Cisco Nexus Dashboard for day-to-day operations.

### Deploying Production AI with NVIDIA AI Enterprise on Cisco Secure AI Factory - CNCENT-2005
Speakers: Konstantin Cvetanov (NVIDIA), sicong ji (NVIDIA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271926687001zYCZ
This session provides a technical overview of the design and implementation of Enterprise AI platforms for the era of Agentic AI. The talk explores various GenAI deployment methods such as NVIDIA NIM microservices and Retrieval Augmented Generation (RAG) optimized and certified to run on the Cisco Secure AI Factory with NVIDIA. To enable these production workflows in a customer environment we also cover topics such as infrastructure sizing, orchestration, and MLOps. Attendees will gain practical insights on how to leverage the NVIDIA AI Enterprise full stack to accelerate their business with AI.

### Deploying SD-WAN in Air Gap Networks (Defense, Manufacturing, Utilities, Transportation, etc.) - BRKIOT-2911
Speakers: Rodney Smith (Cisco), Mohamed Bahardeen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271953573001zKtY
This session will equip participants with the knowledge to deploy Cisco SD-WAN overlay networks in full and patrial air gap networks requiring isolated UE/CPE devices without cloud or internet access. Topics include key architectural elements for on-premises SD-WAN control, zero-touch provisioning steps and requirements, industrial platform selection criteria, and the benefits SD-WAN provides. The discussion will also highlight the enhanced security SD-WAN delivers including granular segmentation, encrypted communication, real-time threat detection, and simplified policy enforcement. Additionally, we will cover how to deploy containerized applications like industrial asset visiblity tools (Cyber Vision) and remote access solutions (Secure Equipment Access) via SD-WAN. Lessons learned from real-world customer deployments will provide actionable insights.

### Deploying VPNs over Segment Routed Networks Made Easy using Crosswork - BRKMPL-2131
Speakers: Krishnan Thirukonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271961343001zSTd
With segment routing, a software-defined network (SDN) approach to program paths for transport services such as layer 3 and layer 2 VPN becomes possible, enabling new approaches for managing transport networks based on segment routing. In this session, a review of the requirements and capabilities for an SDN approach for transport networks is discussed. This is followed by a description of the Cisco solution for multivendor SDN controller for transport networks to deploy and manage VPN services over SR-TE using MPLS or SRv6, using the Cisco Crosswork Network Controller (CNC). The main use cases covered by CNC will be described and a walkthrough of UI- and API-based workflows to create VPNs, SR-TE/SRv6 policies, and bind layer 2/layer 3 VPNs to these policies will be shown. Additionally, advance capabilities to do tactical bandwidth management and monitor service health will be discussed. The goal of this session is to understand how to bring an SDN approach to managing transport networks and understanding the Cisco solution for it.

### Deploying Your First Cisco SD-Access Project - BRKENS-2824
Speakers: Sergey Nasonov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924767001zYd1
So, you got your first SD-Access project and do not know where to start? This session will explore what it takes to plan, design, and implement a typical SD-Access project for an imaginary company. During this presentation, we will discuss the lessons learned from previous deployments, typical misunderstandings, and evaluate design options and the migration approach from traditional networking to fabric. The session is going to cover scope and effort estimates, risk management, external dependencies, build, and migration techniques. Wired and wireless migration considerations will be examined, as well as ISE and Cisco Catalyst Center roles and functions. This session is aimed for solution architects getting their hands dirty with SD-Access.

### Deploying an AI/ML Hybrid Cisco and Azure Infrastructure for Advanced AI Use Cases - BRKCLD-2944
Speakers: Jeff Teeter (Cisco), Matthew Quarisa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271847283001z2em
In today's digital landscape, integrating AI and ML into enterprise operations is essential for staying competitive and driving innovation. This session explores deploying a hybrid Cisco and Azure infrastructure to support advanced AI/ML use cases, such as ChatGPT, sustainability initiatives, smart buildings, and public safety applications. Participants will gain insights into creating secure and scalable AI/ML environments leveraging Cisco and Azure technologies, as well as Splunk as an operational intelligence platform. This comprehensive session offers a deep dive into how hybrid AI infrastructure can address business challenges in sustainability, public safety, securely integrating ChatGPT with enterprise data using Retrieval-Augmented Generation (RAG), and various company workflows. Additionally, the session will cover the Cisco AI-Driven Secure Enterprise Data Architecture, which ensures robust data protection and operational efficiency. Participants will learn to harness these technologies to create impactful AI systems, enhancing organizational efficiency and resilience, and ensuring their organizations remain at the forefront of technological innovation.

### Deploying the Webex App to your Organization - BRKCOL-2198
Speakers: Shane Long (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271856819001zplG
The Webex App unifies multiple collaboration workloads into a single modern user interface. This session will focus on the deployment of the Webex App to your organization with a focus on admin controls for installation and login/lifecycle management. While we will touch on all workloads available in the Webex App, we will focus on calling - specifically Unified CM based caling. We will also look at some of the recent AI capabilities delivered for the Webex App with an angle of deployment consideration.

### Deployment of Micro-Segmentation in Cisco NX-OS VXLAN EVPN Fabrics with VXLAN Group Policy Option (GPO) - BRKDCN-2633
Speakers: Max Ardica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884455001zrLo
In traditional data center environments, security enforcement for protecting applications/workloads is typically implemented using perimeter firewalls and other security inspection devices. However, this approach is not effective against the advanced nature of modern attacks, which have an attack surface that spans the entire data center, affecting both east-west and north-south traffic flows. This session introduces the use of micro-segmentation with security groups and security group ACLs in Cisco NX-OS VXLAN EVPN-based data center fabrics. This feature, also known as VXLAN Group Policy Option (GPO) (IETF draft: draft-smith-vxlan-group-policy-05), can provide application-specific policies to tightly control the communication of application workloads regardless of where they reside within the network. The first part of the session covers the functional component of the Cisco GPO implementation, both for a control and data plane perspective. The second part discusses the most common use cases for the deployment of this micro-segmentation option, including service chaining improvement and simplification.

### Deployment of VXLAN EVPN Gateways with Cisco ACI for the Interconnection of Heterogeneous Data Center Fabrics - BRKDCN-2634
Speakers: Max Ardica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271884651001zqS7
In recent years, the use of the VXLAN EVPN technology has become the de-facto standard for the deployment of data center fabrics. Cisco leverages this technology for its two flavors of fabric (and multi-fabric) architectures: Cisco ACI and Cisco NX-OS VXLAN EVPN. As a consequence, customers are very often challenged with the requirement of interconnecting those heterogeneous fabrics, both for co-existence or migration purposes. This session introduces the use of a VXLAN EVPN gateway functionality in a Cisco ACI fabric to establish native Layer 2 and Layer 3 connectivity with standard-based VXLAN BGP EVPN fabrics. The session covers the functional components and the control and data plane mechanisms, required to implement the VXLAN EVPN gateway functionality in an ACI fabric. It will also discuss how to interconnect pre-existing (brownfield) heterogeneous fabrics, a functionality usually referred to as "namespace normalization" and how to provide end-to-end micro-segmentation support between ACI and VXLAN EVPN fabrics through the integration of VXLAN EVPN gateways with the VXLAN Group Policy Option (GPO) technology. This session is a companion of breakout BRKDCN-2933, and the expectation is that attendees already have at least a basic understanding of Cisco NX-OS VXLAN EVPN technology in order to get the best out of this session. Also, it is highly recommended to attend BRKDCN-2602 before coming to this session.

### Design and Deploy Cisco Cloud Managed Enterprise Wireless Networks - BRKEWN-2046
Speakers: Justin Loo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271940433001zCjV
Are you thinking of going to a Cloud native Management Solution for your Campus? Are you worried that the current distributed data plane solutions will not meet your needs of a large roaming domain? This session is for you! Come and learn how to design for scale and performances leveraging the new Meraki Campus Gateway (MCG) while enjoying the simplicity and ease of use of the Meraki Dashboard for Cloud Management

### Design and Deploy Cisco Network Detection and Response with Cisco Breach Suite - BRKSEC-2248
Speakers: Hanna Jabbour (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009583001zHJg
Network Detection and Response (NDR) tools are critical components for any SOC or NOC and provide a great value for both users. Designing and deploying an NDR to provide complete visibility across hybrid network is key for successful and smooth day to day operation. This session will provide details on how to design and deploy Cisco NDR solution Network Analytics (NA) in a hybrid environment. You will learn all the components (new and old) and how they fit in your network to provide visibility into workloads on-prem and in the cloud as well as users and devices locally or remotely. The participants will learn how to integrate the different telemetry sources and their contribution into the analytics including Firewall, Network, endpoint and Cloud data. This session includes details on NA architecture as well as configuration guidelines based on requirements and uses cases.

### Design, Automate, and Simplifying VXLAN EVPN Multi-Site Architectures with Nexus Dashboard Federation - BRKDCN-2988
Speakers: Parth Patel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892076001ziUB
With the exponential growth of Applications, Enterprises and Service Providers must create Scalable Data Centers. This has led to the deployment of Data Centers, large and small, spread across geographies, with IT requirements to interconnect them for reasons such as High availability, Disaster recovery, and Scale. VXLAN BGP EVPN Multi-Site allows inter-connecting loosely coupled VXLAN sites to build hierarchal overlays to provide secure Multi-Tenancy and Mobility at Scale. In this session, attendees will first learn different Design options and Automation workflows of VXLAN EVPN Single-Site and Multi-Site using Nexus Dashboard. Next, we will introduce Nexus Dashboard Federation, powered by One-Manage, which provides a unified platform to join, automate, and manage multiple Nexus Dashboard clusters. This centralized control enables seamless VXLAN EVPN Multi-Site deployments across Multi-Cluster fabrics, offering a scalable and automated solution to extend Layer-2 and Layer-3 services.

### Design, Deployment, and Management of Network Fabrics - BRKSPG-2227
Speakers: Phil Bedard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271968514001zARa
In this session, we will explore the evolution of provider network designs over the last 30 years, and the state of the art deploying modern network fabrics. Network fabrics provide full mesh connectivity between endpoints with efficiency, scale, and advanced assurance capabilities. We will look at common applications and data sources connected to the network fabric and how best to design the network to support them as well as future applications. We will also cover best practices on deploying the networks and how best to manage and assure the network fabric infrastructure.

### Design, Validate and Certify your Wireless Streaming Telemetry Deployment - BRKEWN-1108
Speakers: Rafael Ceara Batlle (Cisco), Salil Prabhu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271938059001zo9h
This session will focus on the design, monitoring, and alarming of the wireless infrastructure with streaming telemetry and the process that the Cisco Wireless engineering team follows to validate and certify real use cases to scale as expected on production. We will cover different aspects that wireless engineers must take into account to ensure the network can grow as the business demands more traffic and compute to observe in real time what is happening in the network. Topics that will be discussed: Scalable streaming telemetry deployment Consumption of wireless APIs based on customer use cases How to scale your telemetry infrastructure in/out based on network demand

### Designing Access and Core Switching Architectures with Meraki - BRKENS-1402
Speakers: Brennan Martin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271969862001zQzA
Catalyst and Meraki are turning up the cloud power with Cloud-Native IOS-XE, bringing new platforms and new features to your enterprise networking tool belt. This session introduces the new access and, for the first time, core switching platforms available to address your network challenges, as well as powerful Catalyst features coming to the cloud for the first time. Participants will get to see how all of the new features and platforms can be used to solve problems, while improving performance and manageability at scale.

### Designing Enterprise Wireless Networks for Challenging Environments - Tales from the Wi-Fi Crypts - BRKEWN-2054
Speakers: Al Dumdei (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941220001zkQk
Challenging environments drive innovative solutions. In this session we will break down a number of challenging design requirements, discuss options for solutions, how we solved them, what best practices apply to these solutions, and look forward to incorporating additional spectrum by going to 6GHz and leverage Wi-Fi 7 features. Example challenging environments include: Voice in Healthcare — roaming and multicast. Dealing with very large and dynamic networks such as Higher Education (aaa, mdns, optimized timers, dealing with large crowds moving with schedule). What makes Wi-Fi work well in "large public venues"? Dealing with challenging RF Environments (manufacturing, warehouses, industrial) In this session, you will improve your skills with best-practice wireless architectures, solutions to difficult installations, and optimized design process and configurations for on-premises, cloud, and hybrid solutions. Wireless design process and design options are continually evolving, and the number of options has been greatly expanded. We will dig into multiple complex design environments from real-world deployments and see how we solve these challenges of scale, unique environmental conditions, network requirements, and management using various architectures. Remember, your wireless design sets the stage for how well your network will perform, how well you will be able to manage your wireless network, and ultimately what your client's perception is of your wireless network.

### Designing High Availability for Your Data Center with Resiliency - BRKDCN-2947
Speakers: Samer Theodossy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271890181001zAvb
This session will examine data center network design fundamentals and considerations for improving high availability, impacting an organization's daily activities by minimizing network disruption. It will cover key concepts, methodologies, and deployment recommendations, including network topology analysis and best practices. Starting with overall high-availability topics, the session will delve into device-level recommendations and network design concepts. It will address system-level high availability, service-level high availability, and network-level availability with scale and redundancy.

### Designing Highly Available Networks using Catalyst 9000 Series Switches - BRKENS-2095
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271920479001z69t
This session will cover new and existing high-availability features introduced in IOS-XE on Catalyst 9000 Series switching platforms. We will discuss how you can achieve high availability in your network through various stages in the design lifecycle. During the initial design, we will discuss the benefits of features like StackPower, power resiliency modes, StackWise-480, and StackWise Virtual. After the design phase, we will discuss features like GIR, extended fast software upgrade (xFSU), patchability, and ISSU that will help maintain resiliency during the operational phase. We will then conclude by covering how you can efficiently leverage all the high-availability features in different network designs and achieve maximum uptime and resiliency.

### Designing Secure & Scalable Meraki Networks with Single-Sign On & Role-Based Access Control - BRKOPS-1016
Speakers: Jose Valdez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271970633001zWkV
As your deployment grows, designing an efficient and secure framework to manage dashboard administrators and permissions becomes increasingly crucial. In this session you will learn best practices to integrate Role-Based Access Control (RBAC) and SAML Single Sign-On (SSO) as a construct for dynamic access policies. Discover how to: - Architect a seamless SSO and RBAC integration for scalable administrator provisioning and dynamic permissions. - Enhance security with multi-factor authentication (MFA) to ensure robust network protection. - Explore real-world design scenarios and strategies that elevate the security and efficiency of your Meraki deployment.

### Designing and Deploying Cisco SD-Access with BGP EVPN - BRKENS-2650
Speakers: Raj Kumar Goli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271923819001znjR
The Cisco SD-Access solution now encompasses BGP EVPN as a control plane for network segmentation. Join us in this session as we explore intent-based workflows tailored for designing and deploying a BGP EVPN fabric using the powerful Cisco Catalyst 9000 Switching platforms. Additionally, we'll cover the intricacies of provisioning layer 3 and layer 2 virtual networks along with enabling multicast services and exploring various external handoff options.

### Designing the Ultimate Wi-Fi 7 Network with Cisco APs & Ekahau - CNCEWN-2000
Speakers: Matt Starling (Ekahau)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271937471001z3HA
This session dives into the technical considerations for designing high-performing Wi-Fi 7 networks using Cisco's cutting-edge APs and Ekahau's powerful tools. We'll explore the key features of Wi-Fi 7, such as Multi-Link Operation and 320 MHz channels, and discuss how to address design challenges like channel planning and interference management. Learn how to leverage Ekahau's AI Pro and Sidekick 2 to optimize your network for Cisco's Wi-Fi 7 capabilities, ensuring seamless integration of 6 GHz while maximizing performance and capacity. Real-world scenarios will provide practical insights to help you build the ultimate Wi-Fi 7 network.

### Deterministic Traffic Control with Cisco Meraki SD-WAN - BRKENT-1545
Speakers: Charles Lynch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271970056001zJ19
Join us to understand Meraki's performance based VPN routing implementation, known as SD-WAN Routing for VPN Transmissions. In this session we will analyze common scenarios in which transport underlay paths can experience degradation which can be measured and acted upon. We will explicitly explore implementations of SD-Hub Routing which will mitigate the variance of loss, latency, jitter, and uni-directional forwarding.

### DevNet and Automation Certifications and Learning Update - CISCOU-2056
Speakers: Mubasher Nawaz (Cisco), Francois Caen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841198001ztQw
The future is now: Network automation and NetDevOps are essential skills for today's network engineer, requiring up-to-date training and the right certifications to showcase your expertise. In this session, we will explore Cisco's DevNet and Automation certification paths, highlighting significant upcoming changes to the portfolio and major updates in Python and automation training. This session will answer all your questions as you prepare for your automation certification journey from Associate to Expert.

### Developing and integrating with Cisco XDR - DEVNET-2236
Speakers: Matt Vander Horst (Cisco), Christopher Van Der Made (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271911823001zMSq
New Description: Join us for an exciting session on enhancing Cisco XDR with custom integrations and content. Custom and community integrations allow you to enhance XDR's functionality by importing additional security event data, providing new dashboards, enabling custom response actions, and more. Custom workflows for XDR automation allow you to customize your incident investigation and response processes, among other things. And, for the first time, we'll share how you can bring your own data into XDR's data warehouse, using the open standard OCSF. Finally, we want to build a robust community around XDR integrations and content, so we'll also discuss our community features and new XDR Connect portal, all designed to facilitate seamless collaboration and innovation with our DevNet community!

### Development of Cisco XDR Integration Modules and Dashboard Tiles - DEVNET-2006
Speakers: Brennan Bouchard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271897919001zuIu
Cisco's XDR is built upon a collection of APIs which can be used to integrate your 3rd party security products, automate the incident response process, and manage threat intelligence and security context data in a single location. In this lab, you will learn how to develop XDR integration modules and dashboard tiles using Python Flask and REST APIs. After completing this lab, you will have the tools and framework to develop any 3rd party solution into XDR.

### Digital Network Twin for end-end topology lifecycle - DEVNET-2303
Speakers: Saad Ahmad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271903830001zPvk
Learn how to protect your business from costly network outages by mastering network configuration simulation. This session will teach you how to use Cisco Modeling Labs (CML) to create a virtual network, leveraging Cisco images for accurate simulations. We'll demonstrate how to build network topology via Infrastructure as Code(IaC) using Terraform, automate configuration using Ansible, test/validate using PyATS and finally integrate into CI/CD pipelines using Gitlab. This allows you to thoroughly test changes and ensuring a smoother and more reliable production environment

### Digital Resilience in the AI Era: Strengthen Your Business and Workforce - PP-1312
Speakers: Scott Herpolsheimer (Cisco), Sweetie Browne (Cisco), Stephanie Hagopian (CDW)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271948251001zUQ4
The integration of AI into business processes is not just an advantage — it's a necessity. Learn how your organization can effectively harness AI to empower your workforce and gain a competitive edge to support your customers. Gain insights into Cisco's methodology for building AI capabilities across our workforce, weaving in AI as a seamless part of our tools and solutions through the lens of security. We'll also hear from one of our partners on how their AI strategy is embedded into their workforce to drive customers outcomes. Unlock the full potential of AI to drive your organization toward a future of intelligent automation and help your customer innovate.

### Digital Resiliency Unlocked: Power Sustainable, Secure, and Inclusive Communities - PP-1304
Speakers: Xiang Liu (Rutgers University), John Paul Morgan (Morgan Solar Inc.), Guy Diedrich (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271947468001zRmk
Celebrate a decade of digital transformation with the Country Digital Acceleration (CDA) program, which powers sustainable, secure, and inclusive communities. Discover how Cisco's AI-driven technologies can enhance your operational efficiency and security, revolutionize public transportation systems globally, and bridge the digital skills gap. Explore how our solar-powered office solutions, developed in partnership with Morgan Solar, can help you achieve net-zero emissions and optimize energy use with cutting-edge technology. Gain insights into scalable, repeatable use-cases from CDA that can be tailored to any solution or vertical, offering you the tools to gain a competitive edge and unlock the value of digitization to lead in a connected, efficient, and secure world.

### Discover and Build with Webex Service Apps: A Guide for Webex Developers - DEVNET-2134
Speakers: Joe Zanini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271900559001zr6Y
In today's fast-paced business environment, seamless automation is key to staying ahead. Discover the power of Webex Service Apps in transforming your Unified Communications infrastructure. As business trends shift towards continuous, user-independent automation, this session will guide you through everything you need to know to get started with Webex Service Apps. Join us for an end-to-end exploration where you'll: • Unlock the Potential: Learn how Webex Service Apps can help you build resilient, user-independent applications. • Understand Key Differences: Distinguish between Service Apps and standard integrations, and see why Service Apps are essential for business continuity. • Gain Practical Insights:Dive into hands-on examples and demos that showcase the setup and implementation of Webex Service Apps. By the end of this session, you'll leave equipped with actionable ideas and the knowledge to enhance your business automation strategy. Don't miss this opportunity to elevate your Webex developer experience with cutting-edge solutions! This session is ideal for web developers, IT administrators, and third-party developers who are new to Webex Service Apps and are interested in building applications for Webex customers. No prior experience with Webex Service Apps is required, but a basic understanding of web development and OAuth 2.0 principles is recommended.

### Discover the invisible world of wireless with spectrum analysis - BRKEWN-1011
Speakers: Nicholas Swiatecki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271937858001zL8V
In today's wireless-first world, understanding spectrum analysis is the first step towards mastering your wireless network. Spectrum analysis involves examining the radio frequency (RF) spectrum to identify and manage interference sources,. This session will explore the basics of spectrum analysis, the products and solutions Cisco provide for this, as well an overview of other wireless tools available. Attendees will learn how Cisco Clean Air Pro identifies and mitigates interference, ensuring robust and reliable wireless connectivity in 2.4, 5 and 6 GHz, whether you are deploying on-prem or cloud managed Cisco wireless networks.

### Dive into GenAI and agentic AI best practices for Security and Observability - BRKOBS-1011
Speakers: Lipyeow Lim (Cisco), Vedant Dharnidharka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271978175001zbmC
Have you wondered how to unlock the full potential of AI to accelerate security and observability outcomes? In this technical presentation, engineering leaders from Splunk AI will discuss the latest innovations in AI and showcase how AI-driven capabilities can improve security postures, business performance reliability, and team productivity. Take a deep dive into the GenAI architectures, agentic AI technologies, and the system design principles that power these capabilities as we bring AI to enterprise organizations.

### Diverse Virtualization Deployment Strategies with Cisco UCS: VMware, Red Hat, Azure, Nutanix, and More - BRKCOM-2460
Speakers: Jeff Nichols (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861960001zJtd
In today's dynamic IT landscape, organizations require flexible and scalable deployment options to meet their diverse computing needs. The Cisco Unified Computing System (UCS) offers a multitude of deployment alternatives designed to optimize performance, simplify management, and accelerate business outcomes - all without requiring infrastructure silos or unique operational models. Join us for an engaging session where we will delve into various deployment models, including: VMware vSphere: Understand how to effectively deploy and manage VMware vSphere on Cisco UCS, leveraging best practices for virtualization efficiency and reliability. Red Hat OpenShift Virtualization: Discover the benefits and strategies for deploying Red Hat OpenShift Virtualization, ensuring seamless integration and a natural extension to the cloud-native Red Hat OpenShift platform. Bare Metal Deployments: Learn about the advantages and key considerations for deploying bare metal servers on Cisco UCS to achieve maximum performance and control. Microsoft Azure Stack HCI: Gain insights into deploying Azure Stack on Cisco UCS, enabling hybrid cloud solutions that extend Azure services to your on-premises environment. Cisco Compute for Hyperconverged with Nutanix: Explore how to streamline AI workloads and enhance performance with our integrated hyperconverged solutions. And More We will share practical insights and best practices to help you select and implement the most suitable deployment models for your organization. This session will equip you with the knowledge and tools to leverage the full potential of Cisco UCS in optimizing your IT infrastructure.

### Do You Know Where Your Data Is? A Deep Dive on Cisco Secure Access CASB and DLP and How to Protect Your Locations, Data and Users - BRKSEC-2143
Speakers: Nitin Kumar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272000357001zPxh
Do you know where your data is? As cloud adoption is on the rise, so are bad actors preying on companies and users. This session will provide a technical overview of Cisco Secure Access' CASB and DLP offering which is a core part of Cisco's overall SASE strategy. Cloud Access Security Broker (CASB) provide the initial visibility to cloud app usage. Are your users only using business approved apps sanctioned by your company, or are they using unapproved apps to share and collaborate? This is what CASB is designed to find out. Umbrella also features DLP capabilities to monitor and enforce data for all web traffic. This is a core tenant of security and you'll learn how you can best protect your sensitive data from ever leaving the perimeter.

### Don't AI networks design themselves? - BRKCRT-3999
Speakers: Rick Bauer (Cisco), Zig Zsiga (Cisco), Mark Holm (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271836444001zKcZ
Network design is an important discipline, also for AI/ML networks. These networks must be well-designed to provide the AI/ML application(s) the platform they need to perform optimally. This is why the AI Infrastructure elective within the CCDE program was created; to allow network professionals to showcase their skills in designing AI-enabled networks. While gold-plating is not usually something you want to do in your design, conquering the CCDE with the AI Infrastructure will gold-plate your career! Join this session to learn more on how you can add the AI Infrastructure badge to your Cisco badge collection in addition to earning the coveted CCDE certification.

### Don't Just Connect, Grow Your IoT Business with Cisco IoT Cellular Connectivity Management - BRKSPG-1002
Speakers: Pedro Ruiz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963677001zyYE
From operating autonomous vehicles, to managing manufacturing robots, to tracking life-saving vaccine shipments, cellular IoT is transforming the way we work and live. Today there are over two billion cellular IoT connected devices worldwide, and the global cellular IoT market will exceed $18.2 billion by 2027. To successfully launch and manage thousands of devices in the field, organizations need to adopt new technical and operational approaches to allow them to scale faster, operate smarter, and protect better. In this session, you will learn how the key capabilities of Cisco IoT Control Center can enable you to rapidly innovate and expand your IoT business by delivering better customer experiences while lowering costs and streamlining operations.

### Driving Business Value with Technology: A Proven Framework - CTF-1038
Speakers: Doug Haynes (Cisco), Marcello Ishida (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271945068001zeDj
Today's IT leaders face a daunting challenge: harnessing the power of emerging technologies to drive real business impact. The sheer volume of innovation can be overwhelming, making it difficult to identify strategic opportunities and craft compelling narratives. Have you ever had to plan technology investments in your organization? What about serving different lines of businesses, each of them having its own metrics and key performance indicators? Are you able to articulate your company technology strategy for the next 2/3/4 years nice and easy? Well, you are not alone. Welcome to our world! In this session, the participants will learn a collaborative approach to bridge the gap between technology and business. Attendees will see how to: . Decode the Tech Jargon: Simplify complex technical concepts into clear, actionable insights. . Align Tech with Business Goals: Identify strategic opportunities and create compelling business cases considering multi-architecture domains (enterprise networking, security, applications, data center & cloud, collaboration, IoT, AI). . Craft Your Digital Narrative: Develop compelling stories to engage stakeholders and secure buy-in. . Foster Innovation: Cultivate a culture of innovation and continuous improvement.

### Driving Innovation with AI for Security and Observability - BRKNWT-2401
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973697001zxtC
AI is the present - and future - of how we enable deeper and broader insights for security, observability, and analytics for real-world networks, applications, and business processes. Attendees at this fun, engaging session will see the latest innovative developments in Cisco's AI/ML solutions across multiple domains, examine options for how you can enable AI in your own organization, and experience getting AI into your own hands - literally! Presenting this session is the dynamic trio of Patrick leMaistre, Errol Roberts, and Dave Zacks, all Cisco Live Distinguished Speakers as well as huge proponents of AI/ML across Cisco, and with our customers and partners. Come to this session to understand, see, and experience the future of AI in action!

### Driving Innovation: Leveraging Cisco Splunk for Intelligent Transportation Systems - BRKXAR-2031
Speakers: Erling Hoie (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271868705001ztyk
Cisco Splunk can significantly enhance Cisco Edge Intelligence by providing real-time insights and advanced analytics. By ingesting and analyzing data from edge devices, such as IoT sensors, cameras, and network devices, Cisco Splunk can enable timely decision-making and automated responses. This session provides insights to how Cisco Splunk can analyze sensor data to predict equipment failures, optimize network performance, and improve security. See how Cisco Splunk empowers organizations to harness the power of their edge data, driving innovation, improving operational efficiency, and making our roadways safer.

### Driving Social Impact in the AI Era - PP-1309
Speakers: Charu Adesnik (Cisco), Paul Wendel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949024001zezA
72% of nonprofit organizations view AI as a strategic priority for future development according to a Worldmetrics.org 2025 report. But 45% do not feel prepared to implement AI solutions effectively. As non-profits and community organizations look to scale in the AI era, technology and digital expertise are more critical than ever. At Cisco, we see extraordinary opportunities for growth and innovation by building AI technology — and the future-ready skills to harness it — into our Social Impact initiatives and partnerships. This session is tailored for those looking to understand what it takes to succeed in the AI revolution and champion impact anywhere and everywhere. you'll learn how Cisco is teaming up with local leaders, customers, and partners to invest in the digital futures of 40 communities around the world over the next 10 years. you'll come away with ideas on how you can leverage your technical and AI expertise to drive value for non-profit and social impact organizations — and how we all can create connected, resilient communities that thrive in the AI revolution.

### Driving the Future: Enhancing Safety for Emergency Responders with Cisco at the Edge - BRKIOT-2028
Speakers: Jason Potts (City of Franklin, TN), Mark Knellinger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271953176001zVxd
Explore the transformative power of Emergency Vehicle Preemption (EVP) and the future of connected vehicles through Cellular Vehicle-to-Everything (C-V2X) technology. Hear from city officials including, a City Manager, a Fire Chief, and Chief Engineer about a city's real-world experiences with EVP systems that have reduced emergency response times and improved traffic flow. Gain insights into the technical and operational aspects of EVP, including integration with existing infrastructure and the role of advanced technologies in ensuring seamless and secure communication. Hear a compelling success story of EVP implementation and its impact on public safety and traffic efficiency. Discover the future of connected vehicles and C-V2X technology in creating smarter, safer cities. Learn how real-time data processing and analytics enable a fully connected transportation ecosystem, showcasing a vision for a smarter, safer, and more efficient transportation network.

### Duo Identity Security: Protect your users and applications with SO MUCH more than MFA! - BRKSEC-2879
Speakers: Jeff Groesbeck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272011566001zqB6
Learn how Duo has evolved into Duo Identity as a powerful Identity Security solution. We'll learn how to configure and use Duo's newest features to not only protect your users and application, but also identify threats you may not have been aware of. We will start with a new Duo account and build an Identity Security solution from the ground up! We'll configure exciting new features such as true passwordless, multiple IdP support in Duo SSO, user attribute syncing, passwordless windows logon, and other new Duo advancements utilizing Duo's new directory or IdP functionality.

### Dynamic Network Defence: Automating Traffic Engineering based on ThousandEyes Insights - BRKOPS-1009
Speakers: Kemal Sanjta (Cisco), Mike Hicks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985210001zLeA
DDoS attacks and BGP hijacks have long plagued our networks, causing operational chaos, monetary losses, and reputational damage for affected organisations. Despite their prevalence, mitigating these threats often involves reactive, time-intensive processes that rely on manual, usually delayed, execution of relevant methods of procedure (MOPs). Even routine network performance issues, like packet loss or latency, frequently take hours to troubleshoot and resolve, leaving users and stakeholders frustrated. In this talk, we will demonstrate how to leverage the power of ThousandEyes insights to automate the resolution of common operational issues. This includes switching to alternative providers upon detecting detrimental network conditions like packet loss and latency spikes, handling the unpredictable nature of DDoS attacks, and automating responses to BGP hijacks. All of that within the minutes, rather than hours as it was traditionally the case. Our demo-heavy talk will show how to reduce Mean Time to Resolution (MTTR) from hours to minutes, empowering your team to maintain service continuity and to deliver operational excellence.

### EIGRP Operations: The Usual Suspects - BRKENT-2050
Speakers: Steven Moore (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271931300001zMSU
If you operate a network with EIGRP, then you need to know the who, what, where. This introductory session will take a very focused look at common situations and scenarios to help you speed up your triage and resolution. While this is not a class in how to troubleshoot, it absolutely will help you know where to look, and how to quickly identify the most common culprits. This course assumes a base level of EIGRP knowledge and IP Routing.

### EVPN Deep Dive with IOS-XR Configuration Examples for Service Provider Metro and Data Center - BRKMPL-2253
Speakers: Jiri Chaloupka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966405001zdvz
This EVPN deep-dive session will explain EVPN (BGP) control plane in detail together with configuration examples for each use case, such as service provider metro (access) or service provider data center, and how EVPN can help integrate these two parts of the network together. The last part of the session will cover integration with existing services. This session will be real Deep Dive to technology.

### EVPN Fabric in the Real World: Securing Critical Infrastructure in Finance and Aviation - BRKENS-2655
Speakers: Daniel Cantor (Fiserv), Ekta Ghosh (Adani Airports Holding Limited), Rahul Kachalia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921837001zgvo
Join us for a high-impact executive session that takes you inside two of the most demanding digital transformation stories in the world; where secure, intelligent networking is not just a luxury, but a necessity. From the boardroom of Fiserv, a global financial service technology, to the control tower of Adani Airport, one of Asia's busiest airports providing worldwide connectivity, the Cisco Enterprise networking solution with EVPN Fabric has become the foundation for a new era of secure, scalable, and always-on infrastructure. Financial and aviation leaders from both organizations share a vision of successful transformations of agile and fully-automated environments—reducing downtime, strengthening cybersecurity postures, and enabling rapid innovation. This session will reveal how Cisco's Catalyst networking solution and EVPN Fabric isn't just a product and technology choice—it's a strategic shift. Discover how network modernization aligns with business goals, regulatory requirements, and operational efficiency to deliver tangible results across the enterprise. If you're focused on digital resilience, regulatory readiness, and long-term scalability— this conversation with industry leaders is not one you want to miss.

### Earning Your CCNP Enterprise Certification: What You Need to Know - BRKCRT-2008
Speakers: George Koukis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271834520001zCAh
Are you an enterprise network professional ready to take your career to the next level? Do you want to develop your skills and increase your opportunities for advancement by certifying your expertise? If you answered "Yes", this session is for you!

### Efficacy 101: How to Detect, Protect, and Remediate against Email-based Threats - BRKSEC-2245
Speakers: Sergio Pinto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009391001zkJa
Attackers are amongst the most sneaky and creative people out there! They spend their entire days figuring out the best way to trick and lure end-users. Fortunately, so do we! Cisco Secure Email Solution uses many technologies, solutions, and techniques to understand attacks, making sure we only allow legitimate emails through and stop anything suspicious or potentially malicious. Being able to detect BEC types of attacks, Phishing, Scamming, Ransomware, and other attacks, require different techniques to detect, prevent, protect, and remediate against. Email Security is a cornerstone of any Enterprise Security strategy, being a leading vector of attack for an overwhelming 90%+ of all security exploits. In this session, you'll understand the latest techniques we use to detect potentially malicious content, namely how we detect, protect, and remediate against malicious URLs, malicious files, user and brand impersonation, phishing, and many other types of attacks!

### Efficiency in Every Packet: A Study in Segment Routing Automatic Self-Correction Capabilities - BRKMPL-1205
Speakers: Tiago Lugarini Silva (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271965617001ze9W
This study delves into the realm of networking innovation, focusing on Segment Routing's automatic self-correction capabilities. By examining the self-healing mechanisms embedded within Segment Routing protocols, this research illuminates the capacity of networks to autonomously adapt and correct routing issues in real time. These up-to-date 2023 findings are based on customer experiences and unveil the potential for improved network efficiency, reduced downtime, and enhanced reliability. This exploration sheds light on a promising avenue for network optimization, where each packet paves the way for a more resilient and responsive digital infrastructure.

### Effortless Service Integration: Implementing ePBR for Optimal L3 Service Chaining in VXLAN Networks - TACDCN-2016
Speakers: Emmanuel Abel Fierro Luna (Cisco), David Martinez Aguilar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271881733001z3yl
In the realm of modern networking, the need for seamless service integration and efficient traffic management is paramount. Enhanced Policy-Based Redirect (ePBR) offers a groundbreaking solution for achieving L3 service chaining and redirection without the overhead of extra headers, thereby minimizing latency and maximizing network performance. Attendees will gain insights into how ePBR enables application-based routing through its flexible, device-agnostic approach, ensuring optimal service delivery without compromising application performance. Join us to discover how ePBR can transform your network infrastructure, streamline service integration, and elevate your VXLAN fabric to new heights of efficiency.

### Elevate Every Call with AI-Powered Webex Innovations and Cisco Cloud Calling - PSOCOL-1030
Speakers: Amey Parandekar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271849749001zHsj
Now is the time to move to the cloud, and Webex Calling makes it easier than ever with AI-powered features that transform business communication. In this session, we will explore: Webex Calling Customer Assist: Discover how this new feature empowers all employees, including frontline and mobile workers, to efficiently manage customer interactions using AI-powered tools, all from the Webex app. Every call becomes faster, smarter, and more efficient, ensuring exceptional services and stronger customer relationships. Webex Go: Learn more about our mobility solutions and how they enable seamless communication from anywhere, allowing your team to stay connected and productive on the go. Simplified Management: See our latest offerings that offer greater flexibility and control over your communication systems. Join us to see how understand the difference AI can make in your business operations by enhancing customer service, boosting mobility, and streamlining management.

### Elevate Your Customer Experience with AI & Automation - VILCCT-1012
Speakers: Cameron Hayden (Eleveo)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271862917001zjxV
Discover how Eleveo empowers contact centers to elevate customer and agent experiences while staying ahead of regulatory demands. Get a first look at the 2025 roadmap and learn how Eleveo's flexible deployment options — on-premise, hybrid, or cloud — deliver tailored solutions for your business. Key Takeaways: • Unlock AI-driven workforce optimization for proactive compliance • Automate quality management with Generative AI and an internal knowledge base • Boost agent performance with enhanced scorecards • Explore enhanced digital channel APIs for seamless integrations • Get an exclusive preview of Eleveo's 2025 innovations

### Elevating customer and associates experience HCLTech client case study- Elevating customer and associates -- experience through network initiativesthrough network initiatives - CNCDCN-3000
Speakers: Shanmugam Sundaram (Ahold Delhaize)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271878814001zLvP
Due to the complex nature of our client's environment managing multiple retail brands and around 2000+ stores across the USA, their data center lacked visibility and automation on policy enforcement. HCLTech positioned Cisco ACI as a solution to provide centralized policy-based architecture to improve network management. As a Managed services partner, HCLTech is also helping the client with implementing Webex contact center for improved collaboration.

### Elevating the Security in your SD-WAN - BRKENT-2708
Speakers: Jeff Fanelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271934763001zBc9
In this session, we will explore Cisco's robust secure SDWAN capabilities in the Catalyst, Meraki MX and Secure Firewall branch platforms. The most common deployment use cases of each will be covered, in an effort to guide customers to the perfect capabilities match for their environment.

### Embrace the Upgrade: Automating Firmware at Scale for Meraki and Cloud-Managed Catalyst Devices - DEVNET-2619
Speakers: Jose Valdez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271905973001zY11
As your network grows, efficiently managing firmware across multiple locations becomes crucial. This session will explore how Meraki APIs can enable you to effectively manage firmware at scale from 20, to 100, to 1,000 locations and beyond. You will also discover how automated firmware management, testing and promotion can empower your team to embrace change and better enable your organization's mission. In this session, you will learn how to: - Utilize Meraki firmware management APIs to view, schedule and automate firmware upgrades - Define and enforce custom software version requirements for both Meraki and Cloud-Managed Catalyst devices - Design and implement automated testing protocols for testing and promoting new firmware versions - Leverage no-code solutions to accomplish the same outcomes

### Empower Your Meraki SD-WAN: Unleashing Identity-based Unified Security and Zero Trust with Cisco SASE - BRKENT-2124
Speakers: Kenneth Pinto (Cisco), Avinash Ramesh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933609001zotB
Explore Cisco's journey into the unified Secure Access Service Edge (SASE) powered by Secure Access at its core. Unveil the seamless fusion of Meraki Software Defined WAN (SDWAN) and SASE, converging network-as-a-service and security-as-a-service into a singular, cloud-managed powerhouse. Key takeaways: • Cisco SASE enhanced headend and a comprehensive architectural overview interconnecting Meraki SDWAN, Catalyst SDWAN and third-party IPSec sites • Transitioning from a standalone Meraki SDWAN to a dynamic SASE architecture • Distributed enforcement of policy across on-prem and cloud SASE using a singular centralized management console leveraging a new framework - organization-wide group policy • Evolution from Umbrella SDWAN solution (SIGraki) to unified SASE with Cisco SASE Licensing packages • Client-based and clientless Zero Trust (ZTNA) with advanced posturing and policy enforcement for private application access Demos spotlighting SASE use cases - from design and deployment to monitoring.

### Empower Your Network with Segment Routing and MPLS Network Migration - BRKMPL-2177
Speakers: Thomas Peiyao Wang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271961730001zdXs
This session will present how segment routing helps network simplification, SR and MPLS coexistence, SR migration, and SRv6 evolution. The session introduces the co-existence of MPLS and SR-MPLS in the same network domain and how to eventually migrate to a fully programmable Segment Routing Traffic Engineering (SR-TE) network. Session participants will also learn segment routing IPv6 fundamentals, path protection, on-demand SR policy, and the benefits of SRv6 evolution. Most importantly, participants will learn the steps on how to migrate from heavy signaling MPLS to a scalable and stateless SR/SRv6 network.

### Empowering Businesses with Secure, Private and Sovereign AI: A Guide to Deploying Large Language Models - DEVNET-2708
Speakers: Jock Reed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271906754001zkFI
The success of large language models (LLMs) such as OpenAI's ChatGPT, Anthropic's Claude 2, and Google's Bard has indisputably sparked a renaissance in AI utilization across businesses. The ability to harness these powerful technologies is enticing, yet there remain understandable concerns about data security, sovereignty, and accessibility that need addressing. Enter a brave new world where you have control over your AI's data and infrastructure. This session provides a deep dive into deploying LLMs with open-source technologies on cloud-native infrastructure, fostering a ChatGPT-like interactive AI experience that is both private and secure. While the prospect of using and controlling your own LLM is enticing, the path to realizing it isn't without challenges. Join us as we unveil the nitty-gritty of managing your LLM on cloud or on-premise infrastructure. Gain insights into the trade-offs in terms of engineering time, costs, and performance, preparing you to navigate the potential pitfalls and unexpected hurdles. But we won't stop at just helping you deploy your models. This session will explore the steps you can take to safeguard the APIs and software that interact with your LLM services. By the end, you will be equipped with the knowledge to bring more control and privacy back to your users and developers, revolutionizing the way your business leverages AI technology.

### Empowering Cisco Technology with Singlewire Solutions - VILCOL-1062
Speakers: Ken Rosko (Singlewire Software)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271847678001zMBy
During this session, experts from Singlewire Software will offer actionable insights into how adding our InformaCast software to Cisco technology can offer enhanced threat detection, notification, and incident management capabilities. In this session you'll learn how to: Leverage the "action button" on Cisco 9800 phones using InformaCast. Integrate Meraki MT sensors with InformaCast to activate notifications. Tie InformaCast into Webex Calling for paging, notifications, and more. Position InformaCast and Cisco technology to help K-12 schools meet Alyssa's Law requirements. This session will also cover Singlewire's visitor management solution, Visitor Aware, which is now available on Solutions Plus.

### Empowering Communities with Responsible AI: Driving Secure, Inclusive Digital Transformation - IF-1026
Speakers: Daryl Thomas (Cisco), Scott McGregor (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949593001zjtx
In today's rapidly changing digital landscape, the role of responsible AI is evolving to meet the needs of diverse stakeholders-from students and small businesses to municipalities. In this session, discover how Cisco is leveraging AI to not only secure networks but also create scalable, inclusive solutions that empower communities. Join Scott McGregor, Director of Community Enablement at Cisco, and Daryl Thomas, Business Operations Manager at Cisco, for an inspiring look at how Cisco's technologies and innovative partnerships are transforming anchor institutions like Denmark Technical College and Claflin University in South Carolina, and Rust College in Mississippi. Learn how these collaborations are expanding secure internet access, building cyber-resilient ecosystems, and launching tailored upskilling programs that prepare students and local residents for in-demand careers. Attendees will walk away with actionable insights into how investing in community resilience creates a win-win for society and business alike.

### Empowering Enterprise AI: Leveraging Retrieval Augmented Generation(RAG) with Cisco UCS and NVIDIA AI Enterprise - BRKCOM-1049
Speakers: Paniraja Koppa (Cisco), Hang Yu (NVIDIA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271859300001zKwq
Retrieval Augmented Generation (RAG) offers a dynamic approach to enhancing the accuracy and reliability of Large Language Models (LLMs) with facts fetched from external sources. It fills the gap in how LLMs work for enterprise applications. This session will provide overview into the RAG framework, offering attendees a roadmap to successfully implement a RAG pipeline within their enterprises. Learn how to harness Cisco UCS's robust computing and storage solutions to design high-performance RAG pipelines tailored for enterprise needs using NVIDIA AI Enterprise.

### Empowering Health Systems with WebexAI + WebexCC for Smarter Console and AI-Orchestrated Touchpoints - VILCCT-2001
Speakers: Cody Clark (SpinSci)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271863292001zedt
Operator consoles serve as the “air traffic controllers” of modern health systems, ensuring critical communications flow efficiently between patients, providers and departments. However, legacy console platforms often struggle to integrate with today’s Unified Communication (UC) and Contact Center as a Service (CCaaS) solutions, creating gaps in connectivity and care coordination. SpinSci, a leader in digital patient engagement workflows trusted by health systems serving 40 million lives, is redefining the operator console. By merging its proven patient engagement technology with modern communication infrastructure (WebAI, WebexCalling, Webex CC, Webex Contact), SpinSci introduces the next generation Smarter Operator Console – a fully integrated platform that enhances operational agility, improves patient access, and supports real-time decision making. This session explores how a modernized operator console can unify digital and voice channels, streamline care navigation, and deliver a frictionless experience for both staff and patients. Join us to see how health systems can future-proof their front-door strategy with intelligent, data-driven engagement at scale.

### Enable Zero Trust Network Access for Industrial Networks with Cisco Secure Equipment Access - BRKIOT-1005
Speakers: Alexey Zaytsev (Cisco), Andrew McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271952364001zvWG
Industrial Network operators rely on 3rd party vendors to maintain equipment in their network. Can operators trust them to access their network securely? Zero Trust Network Access (ZTNA) is a security service that verifies 3rd party vendors and users, grants access to specific applications based on identity and context policies. By not allowing access to an entire network, ZTNA lowers the impact of a breach, reduces business visibility on the public internet, and minimizes security risk. Cisco Secure Equipment Access (SEA) not to be confused with Cisco's Secure Access, is a purpose built solution for ZTNA by allowing remote access into Industrial networks to ensure remote employees & vendors only access the devices that they have been given permission to access. This session explains the ZTNA solution, how it differs from a traditional VPN solutions, and how Cisco's SEA tailors' connectivity to OT environments.

### Enabling Agentic AI by Securing and Simplifying IT Infrastructure Management - CNCGEN-1014
Speakers: Douglas Wadkins (Opengear)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271943178001zEyr
As IT infrastructure grows more complex, the ability to securely manage and analyze data across diverse environments has become essential. Join Douglas Wadkins, Chief Technology Officer at Opengear, as he explores how enabling secure observability and seamless data access ensures AI-driven tools have the critical information needed to operate effectively. This session will highlight how Opengear's solutions deliver immediate value by enabling converged observability across physical and virtual infrastructure. Discover how this secure access to critical data allows organizations to: * Leverage agentic AI with complete visibility into IT environments * Run accurate simulations before deploying automation, preventing unintended consequences * Access critical data to power AI-driven decisions and future automation initiatives Join us for an insightful discussion on how Opengear helps organizations build the secure, data-driven foundation needed to unlock the full potential of agentic AI.

### Enabling SP transformation through Autonomous Networking - BRKSP-2133
Speakers: Daniele Ceccarelli (Cisco), Emerson Moura (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967949001zqkx
Our market is undergoing the biggest transformation in the history of telecommunications. Increased competition and heightened expectation from their customers mean it's now time for some radical changes. This transformation gives rise to a more simplified, automated, programmable and intelligent network layer whose characteristics are encompassed in the industry drive around Autonomous Networking. A more detailed description of the objectives and desired outcomes of Autonomous Networks and how these contribute towards Cisco's three pillar vision around Network Simplification, Autonomics with Data Intelligence and Service and AI- Ready Connectivity. These 3 pillars will be explored and customer examples and use-cases will be described showing the Cisco differentiation in each area. The first 2 pillars will describe Cisco developments and innovations that enable the network simplification and also delves into the evolution from automation to autonomics with increased importance of data intelligence. The third pillar will identify some of evolving "service factory" solutions which are being developed to address the direct needs of Service Providers' customers. The session will describe the Cisco SP Network as a Service (Naas) framework and some use-cases specifically around the B2B segment which includes aspects of Enterprise connectivity, trusted services and the integration of aaS-based services such as Cisco Mobile Services Platform (MSP). The final section will describe industry initiatives with a description of the two catalyst projects use-cases which are currently been driven with our customers and partners through TM Forum. The first is Game X : Elevating the customer experience via self-governed converged networks— with operators including STC, Colt and Verizon. The second one is Accelerating Dynamic Network Marketplaces which includes our Network-as-a-Service (NaaS) framework and includes operators such as BT, Etisalat and Telecom Argentina.

### Enabling Smarter Workplaces - BRKCOL-2265
Speakers: Vanessa Sulikowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853775001zFcG
The last few years has seen major changes in the way we work, including the cadence of people in, and the activities undertaken in the workplace. This is leading to changes in the capabilities and requirements we now have of our workplaces. This session will look at how we can use sensor derived data to enable smarter more effective workspace experiences to provide real-time visibility of available space, the intersection of workplace techniques and technology to provide more efficient workspace usage and management, space booking intelligence and data driven workspace optimization insights. We will delve into creating smarter workplaces by leveraging Cisco Spaces smart workspaces for space visibility, emerging space booking, wayfinding and smart room automation. Alleviating workspace inefficiencies through adhoc spaces usage technology and intelligent room booking enhancements and automation. While capturing extensive workspace analytics and insights including comprehensive room occupancy data and environmental metrics for continual workspace optimization.

### Enabling cloud and premise deployments with CUBE - BRKCOL-2312
Speakers: Hussain Ali (Cisco), Omer Ilyas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857020001zR24
CUBE Enterprise has been Cisco's flagship on-premises session border controller (SBC) on the routing platform for over two decades. This session will begin with a recap on CUBE and configuration best practices for first-time session attendees . This will be followed by new features introduced as part of various v14.x releases. Additionally, it will cover high-capacity premises-based PSTN option for Webex Calling along with site survivability support for Webex Calling. Lastly, we will discuss config changes required on the Local Gateway (LGW) to support co-location with Survivability Gateway (SGW).

### Enabling the Network as a Sensor: Getting data out of the network - BRKENT-2345
Speakers: Matthew Robertson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271932235001zEOE
Starting at the input interface this session will explore how firstly configure network telemetry (NetFlow, IPFIX and ETA) and how to get it to Cisco analytics solutions such as Cisco Secure Network Analytics (SNA) and Cisco XDR. This session will cover telemetry exporters such as the catalyst 9300, Meraki MX and Meraki MS390, the evolution of the Encrypted Traffic Analytics solution, Cisco Telemetry Broker's role in moving telemetry and touch upon the analytics SNA/XDR performs with the telemetry.

### End to End Segmentation with Cisco Catalyst SD-WAN and ISE - BRKENT-2166
Speakers: Nikolai Pitaev (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271931679001zAby
With the increased sophistication and number of network attacks, controlling the ability for threats to move laterally throughout the network is more important than ever. In this session you will learn how: The combination of SD-WAN and ISE will allow for flexible end-to-end macro and microsegmentation of users, devices, and applications. ISE can assign secure group tags (SGTs) based on user/device identification, SD-WAN propagates those SGTs across the WAN, and policy can be created to control access to resources. Integration with ISE allows security policy in SD-WAN to match on user identity instead of traditional attributes like IP addresses. This session will be targeted for an audience with a baseline understanding of SD-WAN and segmentation concepts. The session will consist of a combination of presentation and demonstration. The presentation will focus on the details of the different integrations and segmentation options. The demo will focus on how to enable the integration, enable SGT propagation, and build policy.

### Endpoint profiling and segmentation using AI endpoint Analytics and Cyber Vision for next generation SD Access manufacturing plants - BRKENS-2836
Speakers: ILAN Nagalingam (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271922226001zBAM
In large manufacturing networks, IoT devices present management and security challenges. As such customers embark on the journey towards deploying SD Access, the first step in securing and segmenting IoT devices is knowing what endpoints are connected to the network. Endpoint context plays a key role in identifying IT and IoT devices in a connected enterprise network. This session will discuss how to integrate Cisco Catalyst Center with ISE and Cisco Cyber Vision to identify and profile the IOT endpoints. This session will also discuss how to create granular profiling policies by integrating ISE and Cisco Cyber Vision and automatically deploy new security policies in the network in scale. We will cover aspects of how and where to use Endpoint analytics native to Catalyst center and where to use Cyber vision. We also cover the various deployment options around where in the network to place the cyber vision agents or do data plane inspection to facilitate endpoint analytics. We also talk about how customers can migrate their existing deployments to SD access fabric as they move from static IP based policy management to more intelligent group based policy enforcement.

### Enhance your Digital Resilience by Integrating Cisco ThousandEyes with Splunk Observability Cloud - BRKOBS-2020
Speakers: Gerardo Arrambide (Cisco), Mike Gonzalez Escobedo (ThousandEyes)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271981527001zWki
Are you ready to improve your observability strategy and manage digital resilience? In this session you will learn how to integrate Cisco ThousandEyes with Splunk Observability Cloud, this integration will provide comprehensive visibility across your network and application layers, facilitating efficient troubleshooting and performance optimization within your organization. The session will cover the integration steps and will provide you with common use cases for proactive monitoring and observability in a single integration. Attendees will have a better understanding of how to integrate ThousandEyes with Splunk Observability Cloud to have a comprehensive insight into their IT environments

### Enhancing AI Infrastructure with Isovalent Cilium: Advanced Observability Solutions - BRKCLD-2021
Speakers: Ravi Jandyala (Cisco), Sundar Srinivasaraghavan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271846140001zv7A
This session delves into how Isovalent Cilium enhances observability in AI infrastructure to deliver unparalleled insights and performance optimization. To effectively troubleshoot, protect, and maintain performance for AI workloads, organizations adopting Generative AI require deep visibility into application behaviors and network interactions. In this session, we will deep dive into the integration of Cilium within AI infrastructure and explore observability capabilities through Hubble. Whether you're an IT professional or a network architect, this session will equip you with the tools and knowledge to harness the full potential of observability in your Cisco AI deployments.

### Enhancing Cloud-Native Security: Isovalent's CNI Innovations in Kubernetes - BRKSEC-2891
Speakers: Dirk Stoeckmann (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272004868001zKLv
In this presentation, we introduce Isovalent's products Cilium, Tetragon, and the underlying eBPF technology. We explain how these tools address the network and security challenges of modern cloud-native applications. Cilium revolutionizes networking in Kubernetes clusters, while Tetragon provides deep insights into the security and behavior of applications. Both are based on eBPF technology, which allows dynamic code insertion into the Linux kernel without the need for recompilation. We will also provide an outlook on how Cisco Hypershield will utilize these products as part of a decentralized security architecture in the future.

### Enhancing Customer Experience from within: Using the Cisco AI Assistant to transform experiences - PSOCOL-1035
Speakers: Chang Chang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271850703001z35K
AI is changing the way agents and supervisors are interacting with customers to drive better experiences and efficiency gains. With the Cisco AI Assistant, customer-facing teams are empowered with instant access to relevant information, suggested responses, and task automation to elevate performance and the quality of every interaction. In this session, we'll uncover: - Some of the many ways AI-powered assistance drives impactful outcomes in the contact center - How AI-powered analytics can help supervisors identify friction across customer journeys and opportunities to improve agent engagement - How AI is streamlining agent processes to deliver speed, accuracy, and personalization that directly correlates to better customer experiences

### Enhancing DevOps with MLOps and MLSecOps - Guardrails around AI powered Applications deployment - BRKCLD-1006
Speakers: Jatin Sachdeva (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845001001zYnE
With the widespread adoption of Large Language Models(LLM) and Machine learning(ML) organizations are evolving from DevOps to MLOps lifecycle. MLOps helps in blending Artificial techniques(AI) with DevOps practices. In order to streamline these processes several Open-Source ML platforms might be deployed which helps in model building, training and evaluation for cloud-native applications. With the efficiency and scalability achieved with MLOps it becomes important to understand the different risks it might pose. This session will start with introducing basic components of LLM application and then highlight on the core components of MLOps and how security threats in MLOps platforms and LLM applications can become a gold mine for attackers. This session will then drill down to MLSecOps framework in securing threats around MLOps platform and providing security guardrails around LLM powered applications.

### Enhancing Digital Resilience with AI-Driven Visibility and Insights - PSOCX-1023
Speakers: Jason Coleman (Cisco), Maddie Speakman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272015327001zIZn
In a world where every business is an always-on digital business, the complexity of networks, data centers, and security infrastructures is only increasing. Complexity fosters risk, making visibility and insights essential to achieving the necessary digital resilience.? Join us to explore the transformative power of AI-driven visibility and insights. We will then show how Cisco Customer Experience is at the forefront, utilizing AI to correlate signals and deliver highly personalized insights. These insights empower organizations to take proactive actions, effectively bridging the gap between expected and actual infrastructure behaviors. You will gain valuable knowledge of how to achieve strategic control over their IT environment throughout its lifecycle, resulting in reduced risks and enhanced digital resilience. ?

### Enhancing End-User Productivity with Network Assurance - PSOENT-1028
Speakers: Nikitha Panasamudra Shashidhar (Cisco), Marko Tisler (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928618001z5Rn
Providing an excellent end-user experience is priority #1 of network management, and it's at the core of what we do at Cisco Networking. Assurance capabilities providing end-to-end visibility, AI-driven intelligence, and proactive operations are integrated across the Cisco portfolio. Learn how new innovations such as ThousandEyes Traffic Insights, client simulation testing, and AI-integrated configuration tracking are contributing to Cisco's broader vision toward helping NetOps leaders achieve the goals of excellent digital experiences for all users.

### Enhancing Network Automation with Event-Driven Architecture - DEVNET-1640
Speakers: Kareem Iskander (Cisco), Akhila Pamukuntla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271896318001z0zL
In today's fast-paced network environments, it's crucial to respond quickly and automatically to keep things running smoothly and securely. In this session, we will explore how to implement an event-driven architecture that seamlessly integrates NetBox for network management and documentation, Splunk for real-time data analysis and alerting, and Cisco Cloud Networking for robust network functionality. You will discover how to harness the power of these tools to create an agile network management system where events in NetBox trigger automated actions and alerts in Splunk, boosting overall network efficiency and reliability. We will: Explore the key motivations behind adopting event-driven architectures for network automation Delve into the inner workings of NetBox Events Demonstrate the practical application of Splunk, highlighting Cisco Meraki Dashboard and NetBox Events in action

### Enhancing Network Operations with Observability: Strategies for Real-Time Insight - BRKOPS-2418
Speakers: Quinn Snyder (Cisco), Kareem Iskander (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271986614001zIqG
In the rapidly evolving landscape of network management, achieving operational excellence requires advanced tools and strategies. This session delves into how Splunk's observability solutions empower Network Operations (NetOps) teams with the technical capabilities to maintain high-performing, reliable networks. Attendees will explore how Splunk collects and analyzes multiple streams of data, including syslog, Model-Driven Telemetry (MDT), NetFlow/IPFIX, and SNMP from network devices. This comprehensive data ingestion allows for real-time visualization of network issues, enabling NetOps teams to identify traffic patterns, latency, and performance bottlenecks swiftly. Additionally, leveraging Splunk's platform for automated remediation via automation webhooks offers a transformative approach to proactive network management. Discover how to utilize Splunk's machine learning algorithms for predictive analytics, accelerating incident resolution and driving continuous improvements in network operations.

### Enhancing Network Security with Cisco Catalyst 9000 Switches - BRKENS-2610
Speakers: Ama Owusu-Hammond (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271923628001ztdU
In today's rapidly evolving network environments, security is paramount. This session will dive deep into the robust security features offered by Cisco Catalyst 9000 switches, helping organizations build resilient and secure network infrastructures. Attendees will learn how to effectively leverage built-in security capabilities to protect their networks from modern threats as well as advanced security solutions. This session will provide actionable insights and best practices to fortify your Catalyst 9000 deployment. Join us to discover how to stay ahead of emerging threats and ensure your network remains both agile and secure.

### Enhancing Plant Floor Security to Reduce MTTR at General Motors - CSSIOT-3000
Speakers: Scott Fassett (Cisco), Jorge Ramirez (General Motors)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271951167001zgDv
Join this session to learn practical strategies for improving plant floor security and minimizing downtime in manufacturing settings. General Motors is tackling challenges like limited visibility into network traffic and endpoints, along with a shortage of skills and training, to secure its global plants. With the implementation of Identity Services Engine (ISE) for policy management and the deployment of Catalyst Industrial Ethernet (IE) solutions, IP67 switches, and Catalyst Center, GM is achieving increased efficiencies and a strong ROI. By segmenting networks, GM aims for faster recovery from potential cybersecurity incidents, reducing the blast radius and minimizing Mean Time to Repair (MTTR). GM will speak to what's next and their future goals to prevent future incidents, including integrating solutions like Splunk. This session is ideal for those interested in enhancing their manufacturing operations and boosting overall efficiency

### Enhancing Security and Compliance: Automating Certificate Management for Cloud-Registered Video Devices - BRKCOL-2053
Speakers: Seble Mengesha (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271852058001zcJ5
With the growing deployment of cloud-registered video devices in public sector and enterprise environments, it is crucial to ensure compliance with an organization's security standards. This session aims to explore methods for securing and hardening video endpoints through the automated enrollment and renewal of customer-signed certificates for services such as 802.1x and HTTP web services. Participants will gain insights into certificate enrollment methods using standards-based protocols like SCEP or EST, utilizing xAPI/CLI, the CE-Deploy tool, and the new features available in Control Hub. The methods discussed and the demos presented in this session help video device admins gain productivity by removing the manual, error-prone, and cumbersome process of installing and renewing customer-signed certificates.

### Enhancing Wildlife and Environmental Conservation with IoT and Connectivity Solutions - CSSIOT-1020
Speakers: Sophie Maxwell (Connected Conservation)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271873916001zCni
The Connected Conservation Foundation is transforming wildlife and environmental conservation through advanced IoT technologies and digital infrastructure, across 15 countries. This session will showcase how the deployment and integration of wide-area network connectivity, sensors and high-resolution satellite imagery are giving field teams a real-time, 360-degree view of remote landscapes. Where key technologies from Cisco are crucial in protecting endangered species from poaching and threats of climate change, fostering resilient ecosystems and local communities. Notable achievements include an increase in Kenya's rhino population, a reduction in poaching incidents and empowering communities in natural resource management.

### Enhancing Zero Trust: Elevate Workforce Security With Identity Verification - VILSEC-2036
Speakers: Sasha Dobrolioubov (Persona), Devon Lawler (Persona)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271993261001zhRN
With deepfakes and AI-powered social engineering on the rise, attackers can mimic employees with alarming accuracy to slip through onboarding, support, or recovery processes undetected. The question becomes: how do we really know who's requesting access? This session will dive into how companies can safeguard against Today's threats and enhance workforce security with a Know Your Employee (KYE) program powered by Persona and Cisco Duo. We'll cover: The anatomy of a modern identity attack using deepfakes How KYE can be operationalized from onboarding to recover Technical strategies for integrating Duo + Persona into Zero Trust architecture

### Enhancing the Value of Cisco XDR with NETSCOUT Deep Packet Inspection (DPI) - VILSEC-2035
Speakers: Thomas Bienkowski (NETSCOUT)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271993067001zA0n
The value of Cisco Extended Detection and Response (XDR) lies in its ability to unify and streamline threat detection, investigation, and response across multiple security layers. In this presentation, We'll discuss the certified integration of NETSCOUT's Omnis Cyber Intelligence with Cisco XDR. NETSCOUT Omnis Cyber Intelligence is a Deep Packet Inspection (DPI)-powered Network Detection and Response solution that enables Cisco XDR customers to detect network-based threats, add network context to notable events, and conduct rapid DPI-based investigation of Cisco XDR Incidents.

### Ensuring Reliability: The Essential Role of Observability Tools in Business-Critical Applications - CTF-1035
Speakers: Michael Baba (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271976247001zklL
Today, ensuring the reliability of business-critical applications is essential. Businesses rely on applications to deliver services internally to maintain their day-to-day and externally to deliver services to their customers or partners. This session will highlight how observability tools will help you maintain application performance and minimize downtime. Participants will explore the challenges of diagnosing issues in business-critical applications without specialized tools, including slower resolution times and an increased risk of disruption. You will then see the added value a complete observability practice brings to your business. Participants will see value in: . Testing System Availability: You will understand the importance of monitoring system availability to quickly detect and resolve connectivity issues that could affect your critical services while using ThousandEyes as an example. . Monitoring Application Performance: You will see how observability tools will help track backend application performance, identify bottlenecks, and optimize efficiency to ensure smooth user experiences while using Application Dynamics as an example. . Correlating Logs and Data: Finally, you will discover how tools that correlate logs from multiple systems will help you detect issues faster and perform more accurate root cause analysis while using Splunk as an example. By leveraging observability, you will be able to proactively manage application performance, reduce risks, and ensure the continuous availability of mission-critical services. This session will show you why observability is vital for modern IT

### Enterprise Architecture for Webex Contact Center: Designing for Business Success - BRKCCT-2504
Speakers: Carles Duz Palau (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866000001zDhF
In Today's rapidly evolving digital landscape, organizations must design their contact centers with a structured, outcome-driven approach to stay competitive. This session will explore how Enterprise Architecture (EA) methodology can be leveraged to design and optimize your Webex Contact Center for measurable business success . Through the lens of a customer case study , we will take you through a customer lifecycle of transformation from digitization to the introduction of AI-powered self-service and finally, the evolution of human agents through AI-driven assistance . Learn how to align technology, processes, and strategy to enhance the Customer Experience (CX) and achieve tangible business outcomes. This is a intermediate level session where technology meets strategy to deliver exceptional customer experiences and business results .

### Enterprise Network Automation Strategy, Framework, Best Practices and case studies - BRKATO-2107
Speakers: Anis Edavalath (Cisco), Azharuddin Mohammed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833014001zvd5
This session will focus on building an Enterprise automation Journey Map for customers . All the component elements required in building a secure automation environment covering different technology domains like Datacenter, Campus , WAN , Security and Cloud will be evaluated. A recommendation based on the real time customer success stories will be shared allowing the attendees to gain insights to design a unique automation strategy. We will cover a reference architecture framework, which can be consumed by customers to bring on Infrastructure as code approach in to the enterprise Intent Based network

### Ethernet Evolution and Challenges in the world of AI - BRKNWT-2504
Speakers: Kapil Mehta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973129001zVr1
Ethernet is essential to everything we do in the networking realm. Over the years, it has undergone significant evolution through numerous upgrades. As innovation continues, Ethernet faces new challenges and opportunities for advancement. In this session, you will learn about the history of Ethernet, its major changes, and the current challenges it faces in AI switching infrastructure due to RDMA & elephant packet flows. You will become familiar with some of the solutions for these challenges from Cisco, and highlight solutions/innovations being standardized by the Ultra Ethernet Consortium.

### Ethernet Fabrics for AI clusters - powered by Silicon One and Nexus, an ultra high performance, scalable & non-blocking ethernet fabric. - BRKCOC-3005
Speakers: Christopher Stokes (Cisco), Laxmi Samyukta Vellanki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837748001ziSd
Network infrastructure practitioner session based on a Cisco-on-Cisco story explaining the best practices to be followed on preparing and building a non-blocking ethernet fabric for AI workloads. This session will cover the technology stack used, key configuration considered, challenges faced while building the network infrastructure to deliver a 256 GPU compute form for AI workloads.

### Evaluating and Improving Defenses With MITRE ATT&CK - BRKSEC-2227
Speakers: Mike McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272008811001zHbE
Security architectures can pose complexity and cast doubt. How can we be certain that the solutions we have acquired are adequate? How can we know they are configured properly to cover the many vectors of attack? Cisco, and much of the industry, have taken to using frameworks like MITRE's Adversarial Tactics, Techniques, and Common Knowledge Database (ATT&CK) to help objectively assess those solutions and their coverage of the attackers that an environment is most likely to encounter. An entire ecosystem of tools are now available for every stakeholder involved in protecting an environment. In this session, participants will follow along as we follow an example threat from identification to gap analysis and validation of mitigations and learn about how we can use ATT&CK to dispel our fears, reduce our risks, and improve our security. Together we'll: Discover the benefits of learning from the mistakes of others Learn and see how to use MITRE ATT&CK to evaluate their blind spots See demonstrations of how to build a threat picture, derive coverage mapping, validate coverage with MITRE Caldera, and more!

### Event-Driven Network Automation with NetBox and Ansible - CISCOU-2055
Speakers: Rich Bibby (NetBox Labs)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841013001ztI7
In this session, learn how NetBox as your Network Source of Truth and Event-Driven Ansible combine to ensure your network is always operating as per your intended state. See how you can update your intended network state in NetBox using Branching and Change Management features and then have EDA automatically take action on these changes, providing a seamless and reliable automation process for your network operations. Learn how event-driven automation workflows in EDA are triggered by NetBox events and data demonstrating a streamlined, automated approach to network and infrastructure management.

### Everything in one place: Introduction to Splunk IT Service Intelligence (ITSI) - PSOOBS-2000
Speakers: Matthew Hanlon (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977399001zc4K
Are you looking for that mythical "single pane of glass"? Are you also looking to reduce your MTTI and MTTR? Join us to learn how Splunk IT Service Intelligence (ITSI) can help you gain complete visibility across your entire estate - from applications to infrastructure, business services, network service health and more. Learn how Splunk ITSI applies AI and machine learning to help teams find issues, isolate problem domains - "Is this a network issue?" and fix them faster. Don't miss out on the exciting innovations and integrations the team is planning for the future.

### Evolution of the Transport Network Architecture in the age of 5G, 6G and AI - BRKSPG-2133
Speakers: Shahid Ajmeri (Cisco), Roberta Maglione (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271964645001zmol
The rapid expansion and inorganic growth, technological convergence, network densification, and the exponential growth in connected devices are making it increasingly difficult to manage and operate networks with traditional methods. Future networks must be intelligent and agile, leveraging Artificial Intelligence (AI) to autonomously make decisions while providing clear rationale and explanations to enable true zero-touch operations. AI is now a critical enabler of business value, driving improvements in performance, efficiency, customer experience, and unlocking new revenue opportunities. Once primarily a differentiator for hyper-scalers, AI is now being widely adopted across enterprises worldwide. As AI deployments grow and become more distributed, telecom service providers play a pivotal role in delivering the necessary connectivity and edge infrastructure to support these workloads. However, to support the evolving network topologies and traffic patterns, telecom networks must adopt a significant transformation. This session will discuss how Cisco Agile Services Networking solution is helping service providers to transform their network architecture, optimizing it for flexible service deployment and ensuring a resilient, high-quality user experience.

### Evolve your Zero Trust Architecture: A Case Study with Cisco IT - BRKSEC-2892
Speakers: Sanjeet Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272005061001zCi7
Join us as we explore Cisco IT's real-world implementation of Secure Service Edge (SSE), emphasizing their journey from cloud-based VPN solutions to a comprehensive ZTA model. This transition was not without its challenges, and we will discuss the hurdles faced and lessons learned during the migration process. By examining actual business problems and technical capabilities addressed through this transition, participants will gain a nuanced understanding of the benefits and complexities involved in adopting ZTA. Through this session, attendees will be equipped with practical knowledge to guide their own organizations in transitioning to a more secure and efficient application access strategy.

### Evolving Perimeters and Universal(Hybrid) Zero Trust with Cisco Secure Firewall - BRKSEC-2170
Speakers: George Koikara (Cisco), Anu M Chacko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001364001zslN
In recent years, the idea of a network perimeter has significantly changed. The growth of hybrid work and the increased use of cloud-based applications have rendered the traditional perimeter concept obsolete. Nowadays, corporate networks are not restricted to a single physical location. Users accessing corporate applications can be either onsite or remote, making both groups potential security risks. Consequently, security policy enforcement has shifted from being concentrated at a single firewall on the network perimeter to being distributed throughout the entire infrastructure, including on-premises, cloud environments, and edge networks. Organizations now face the task of implementing consistent, comprehensive security measures to protect data, no matter where it is stored or accessed. The Zero Trust Network Access (ZTNA) model allows organizations to enforce strict access control policies, ensuring that users can only access the specific resources for which they have authorization, whether they are connecting from a secure, on-premises environment or an untrusted remote location. In this framework, a user logging in from an insecure environment might use a cloud-delivered gateway to access applications, while an onsite user would gain access through an internal firewall. This hybrid model, supported by Cisco Secure Firewall and Cisco Secure Access, offers organizations the flexibility to apply Zero Trust principles across various access scenarios. Session Overview: This session offers participants deeper insights into the Hybrid Zero Trust Network Access (ZTNA) approach, supported by Cisco Secure Firewall and Cisco Secure Access. Attendees will learn to: • Secure both remote and onsite access with a unified Zero Trust model. • Implement granular access controls based on user roles, location, and device posture. • Utilize advanced threat detection and protection for both on-premises and cloud resources.

### Exclusive Q&A with Chuck Robbins: Moderated by Fletcher Previn - ITLGEN-2061
Speakers: Fletcher Previn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959423001z1Jl
Join Fletcher Previn, Cisco's CIO, for a conversation with one of Silicon Valley's top leaders, Cisco Chairman and CEO, Chuck Robbins. Chuck will answer your questions submitted on social media around topics such as leadership, the future of work, innovation and technology, and more. This session is an exclusive for IT Leadership program.

### Experience effortless technical support with Cisco's AI enhanced TAC - PSOCX-1018
Speakers: Bhaskar Jayakrishnan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272014338001zJ83
Discover how Cisco's Technical Assistance Center (TAC) is transforming to provide you with a seamless, AI-enhanced support experience backed by technical expertise you can count on. Learn about the AI-powered innovations that help you quickly access a range of resources to resolve issues faster - getting you consistent, high-quality support with every interaction. We are bringing intelligent support features directly into Cisco product portals, to help you navigate complex issues effortlessly, give you proven troubleshooting recommendations, and instant, context-sensitive assistance tailored to your unique requirements. Join us for an exploration of effortless technical support with personalized recommendations, proactive guidance and predictive capabilities.

### Experience the Unified Nexus Dashboard - PSODCN-1009
Speakers: Karishma Gupta (Cisco), Arthur Scrimo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271880376001z7Ob
In this session, you'll learn about the value of the Cisco Nexus Dashboard and the real-world problems the platform can solve. We'll discuss high-level Nexus Dashboard architecture, the unification of services under one Nexus Dashboard product, and connectivity to Cisco ACI. This session will introduce network management, fabric controller, insights, and orchestration, all under a single Nexus Dashboard instance.

### Experiences, Amplified: How AI Can Fuel Better Employee, Customer and IT Experiences for Future-Proofed Workplaces - KDDCOL-1000
Speakers: Snorre Kjesbu (Cisco), Monty Tan (GetixHealth), Aruna Ravichandran (Cisco), Jay Patel (Cisco), Doss Tychicus (AIDS Healthcare)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591953659001pVZU
Imagine a world where employees can work together seamlessly from anywhere, and customer interactions are deeply personalized. Where AI Agents handle routine tasks, and AI Assistants support more meaningful, human interactions. The growth of AI is creating new possibilities with technology - and we're just beginning to see the benefits. Despite this, to realize the true value of AI, it needs to deliver better experiences. Experience sets employee productivity and customer delight apart from being just another technology trend. In this session, Snorre Kjesbu, Senior Vice President and General Manager of Collaboration, Employee Experience, and Jay Patel, Senior Vice President and General Manager of Collaboration, Webex Customer Experience, will explore the future of work and how Webex, supercharged with AI and the full power of Cisco's portfolio, fuel amazing experiences for employees and customers, driving better business outcomes?

### Explore AI Agent Capabilities: Revolutionizing Digital Interactions and Network Management - DEVNET-2427
Speakers: Oleksii Borysenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271905386001zKRo
In the rapidly evolving landscape of digital interactions and network management, AI agents are transforming the way we engage with technology. This presentation explores the technical core and industry use cases of AI agents, highlighting their core capabilities such as autonomous operations, goal-driven behavior, adaptive learning, and environmental awareness. As these agents become crucial in handling sensitive tasks, robust AI Defense policies are essential to protect them from prompt injection and privacy risks. Additionally, we will discuss the role of Large Language Models (LLMs) as a central controller or "brain" for agents, enhancing their functionality and decision-making capabilities. The presentation will also cover AI agent tools that significantly boost model capabilities, and provide a comprehensive cost estimation for AI agent deployment, ensuring informed decision-making in adopting these transformative technologies.

### Explore Digital Channels With Webex Connect and Webex Contact Center (WxCC) - CTF-1031
Speakers: Shikhar Choudhary (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271849165001zrvo
Leverage powerful CPaaS capabilities of Webex Connect along with Webex Contact Center to utilize the potential of Digital Channel capabilities for your customers. This session will go through basics of Apple Business Messaging, Facebook Messenger and Chat integrations and show how easy it is to set them from ground up.

### Exploring Generative AI: A Beginner's Guide to Concepts and Practical Applications? - BRKGEN-1031
Speakers: Jerel Howell (Cisco), Gaurav Khanna (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271946278001zamz
Curious about AI but unsure where to begin? This beginner-friendly session demystifies foundational AI concepts and equips you with practical insights to leverage generative AI. We'll start by building a shared vocabulary and unpacking key terms like large language models, algorithms, transformers, attention mechanisms, and diffusion. Clear explanations and relatable examples will help you grasp how these technologies function and why they matter. ? Through hands-on examples, we will explore real-world examples of how AI is being used Today'such as creating personalized text and image content. These examples will help solidify the concepts and vocabulary introduced earlier. This session will guide you in identifying opportunities to incorporate AI tools into your daily activities and professional workflows, even if you have no prior experience with AI or programming. Bring your curiosity and join us to discover how generative AI can be used in practical and impactful ways.

### Exploring NGSVL troubleshooting tools on 9500X and 9600X - TACENT-2023
Speakers: Kristen Taylor (Cisco), Kayleigh McMillion (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271929391001zilO
Dive into the exhilarating world of Next-Generation Stackwise Virtual (NGSVL) technology within Cisco's groundbreaking C9500X and C9600X series. In this immersive session, we will unravel the secrets of effectively understanding, diagnosing, and troubleshooting this next-gen technology. Explore the intricacies of diagnosing and resolving issues within Stackwise Virtual, gaining valuable insights into the powerful commands that will equip you to tackle any challenge with confidence. Prepare to master NGSVL on the C9500X and C9600X, as you'll acquire the skills necessary to troubleshoot and maintain these cutting-edge systems.

### Exploring Practical AIOps Use Cases for Enterprise Networks with Splunk - BRKOPS-2256
Speakers: Jason Shoemaker (Cisco), Scott Lake (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988606001ziB7
Keeping networks reliable is getting tougher, but combining model-driven telemetry with the power of AIOps can be a game-changer. In this session, We'll show how to tap into your network's telemetry data using Splunk to improve monitoring, apply machine learning models to detect unusual behavior, and enable AI-powered automation. You'll walk away with ideas to help you: Use model-driven telemetry on Cisco devices to get actionable insights. Apply machine learning to network data with Splunk's Machine Learning Toolkit (MLTK). Build AI-driven closed-loop automation to diagnose and remediate network faults We'll guide you through hands-on demos: setting up telemetry with YANG models, visualizing data in Splunk, building ML models from historical data, and triggering automated repair actions with AI agents. you'll also get access to a GitHub repo and remote lab so you can keep experimenting after the session. No matter what tools your team uses today, you'll head home with practical ideas and resources to kick-start your AIOps journey.

### Exploring YANG Data Modeling: A Guided Session using NSO - DEVNET-1882
Speakers: Aayushi Mahajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271897500001zlOz
Struggling to wrap your head around YANG? In this session, We'll simplify the core concepts of YANG and demonstrate its application through Cisco Network Services Orchestrator (NSO). Whether you're preparing for certifications or working with automation, this session will help you navigate YANG with ease and confidence. By attending this session, you'll: Master the Essentials of YANG : Learn the foundational principles of YANG through a guided demonstration in NSO, designed to reinforce key concepts with practical, real-world examples. Boost Your Skillset for Network Automation : Gain critical YANG knowledge that will elevate your ability to work with network automation, improving your practical expertise and certification readiness. Cultivate a Strong Learning Foundation : Discover how experimenting with YANG in the NSO environment sets the stage for mastering more advanced automation techniques. Join us for a session that offers a clear understanding of YANG, culminating in a live demonstration that will boost your network automation skills.

### Exploring the Future of Multi-Modal AI: Integrating Text, Audio, Images, and Video - AIHUB-1970
Speakers: Prapanch Ramamoorthy (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866567001zWGh
One of the key ways in which generative artificial intelligence has started innovating and growing, is in the area of multi-modality. Multi-modal AI models enable systems to understand and generate diverse types of data including text, audio, images, and videos, thereby opening new avenues for applications across industries such as healthcare, entertainment, education, and more. This session, hosted by Prapanch Ramamoorthy and Patrick leMaistre who are both Cisco Live distinguished speakers, will provide an overview of multi-modal AI models, their underlying technologies, and their transformative potential. Participants will get to delve into the architecture and functioning of these models by getting at a fun, and still educational, live demonstration of various modalities of open source models that one can run locally.

### Exploring the Inner Workings of OSPF - BRKENT-2088
Speakers: Elvin Emilio Arias Soto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271933226001zmlN
Open Shortest Path First (OSPF) is a link-state routing protocol commonly deployed in enterprise, data center, and service provider environments. Thanks to its exceptional flexibility and feature richness, OSPF underpins routed IPv4 and IPv6 networks all around the world. This session aims at dispelling the perceived complexity of OSPF and demonstrating its simple-to-understand foundations. We will look at selected in-depth protocol details, including the OSPF packet types, adjacency formation, link-state database synchronization, link-state advertisements, use of areas and their types, and path selection, making it easy to understand OSPF comprehensively.

### Exploring the Paradigm Shift in Security: AI and Quantum Cryptography's Influence on Zero Trust - BRKXAR-2008
Speakers: Cindy Green-Ortiz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271869838001zJYS
Target Audience: CXOs, Organizational Leaders, Security, Networking, Applications and Operational Professionals Session Overview: This session will delve into the transformative impact of AI and Quantum Cryptography on the Zero Trust security model. As organizations increasingly recognize the necessity of a zero trust approach, this session will guide attendees through the next steps in implementing or advancing zero trust segmentation within their organizations taking into account these paradigm shifts. Key Takeaways: Understanding Zero Trust, AI and Post-Quantum Cryptography Theory: brief overview of zero trust principles and their importance in today's security landscape. Practical Implementation: Transition from theory to practice with strategies for beginning or enhancing zero trust segmentation journey. Real-World Examples: Learn from real-world scenarios illustrating successful implementations and common pitfalls to avoid. Strategic Insights: Attendees will gain insights into identifying gaps in their current security posture and actionable steps to advance their zero trust initiatives. Why Attend? Broaden Your Perspective: Gain a comprehensive understanding of zero trust and its critical role in modern security strategies. Actionable Strategies: Leave with a clear roadmap for implementing zero trust segmentation tailored to your organization's unique needs.

### Extend the Enterprise to the Cloud: AWS Cloud Integration with Enterprise SD-WAN - BRKXAR-2015
Speakers: Lee Sudduth (Cisco), Praveen Poojary (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271870033001ztMh
Public clouds play an increasingly important role in enterprise WAN networking. In this session, Cisco Cloud OnRamp for IaaS with AWS cloud integration will be presented. By integrating AWS VPCs directly with the enterprise SD-WAN, Cloud OnRamp for IaaS bridges the gap between cloud-based applications and SD-WAN networking. This session will explore multiple design options to provide application integration, cloud auditing, and other advanced capabilities, including designing, securing, and scaling, the cloud as well as best practices. This session focuses on how to extend your enterprise network into AWS with the Cisco Catalyst 8000V Edge Router. Participants will learn solution design and deployment best practices.

### Extended Detection with Cisco XDR: Data, Native Detections and Incident Generation - BRKSEC-2178
Speakers: Matthew Robertson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001764001zawJ
Exactly what is an extended detection? This session will deep dive into the data and analytics pipeline in Cisco XDR and explore how Cisco XDR collects, synthesises, and analyses data to arrive at a detection of maliciousness, and creates a correlated and extended incident. Covering multiple telemetry sources including network, endpoint, email and identity, this session will explore how analytics can bring these detections together and deliver on the XDR objective and accelerate your security operations.

### Extending CML: Terraforming the Lost City - DEVNET-3008
Speakers: Quinn Snyder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271909291001zZGX
Now that Cisco Modeling Labs (CML) is API-enabled, the automation possibilities of ephemeral lab infrastructure are endless. However, if we truly want to turn our CML instance into a component of our DevOps-driven lives, we need to insert it as part of our network build pipelines. This session will show how using CML, Terraform, and some open tooling -- we can build a continuous-delivery pipeline right from our source code manager of choice, with full change records as part of our pull-request (PR) workflows.

### Extending Webex Contact Center with Flow Designer Extensibility - DEVNET-2915
Speakers: Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271907911001zRdo
Unlock the full potential of your contact center with Webex Contact Center Flow Designer Extensibility. This theater session provides an in-depth look at how to extend the capabilities of the Flow Designer using advanced features such as subflows, flow templates, flow and global variables, custom connectors, HTTP activities, screen pops, surveys, and custom events for virtual agents. Participants will learn how to work with data in Flow, utilize flow storage, and implement business rules engines to create more dynamic and responsive contact center solutions. You'll leave this session with ideas to help you understand how to extend the Flow Designer with advanced features, implement custom connectors and activities, and leverage flow storage and business rules engines to enhance your contact center operations. This session is ideal for developers and IT professionals with experience in Webex Contact Center. Join us to gain valuable insights and practical knowledge on extending the Flow Designer to create more efficient and effective contact center workflows.

### Fabric Networking in the Campus: What's the fuss and what are the choices? - BRKENS-2700
Speakers: Sergey Nasonov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924007001z2lO
This session will explore the major drivers behind the adoption of fabric-based networking. We will contrast two technologies available to customers: LISP-based Software-Defined Access and Border Gateway Protocol Ethernet Virtual Private Network (BGP EVPN). The session will cover how each technology works, as well as the design considerations associated with both technologies that directly impact wired and wireless devices in the campus. Participants will gain insights into the two solutions, enabling architects and engineers to make a suitable choice to meet their organisation's requirements.

### Factory of the Future: Fairlife & Operational Efficiency - CSSGEN-1012
Speakers: Erick Conrad (Fairlife (The Coca-Cola Company))
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271873723001zqsh
In this session, learn how Fairlife, a Coca-Cola company, is revolutionizing dairy production through a new cutting-edge facility in Webster, New York, designed to meet Coca-Cola's production & sustainability goals. This state-of-the-art plant focuses on optimizing efficiency and minimizing environmental impact by partnering with Cisco to implement a fully collapsed IT/OT architecture. By integrating Cisco's advanced solutions including Enterprise Networking, Data Center, Observability, and Security technologies - Fairlife aims to significantly reduce carbon emissions and enhance operational sustainability. The facility also features automated warehousing and autonomous guided vehicles to boost operational efficiency. Join us in exploring how innovative technology can redefine sustainability in production.

### Fast track to Post-Quantum Security - VILSEC-2037
Speakers: Antonio Sanchez (Quantum Xchange)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271993455001zjVR
Advances in quantum computing create an existential threat to the cryptographic foundations of Today's digital infrastructure. In this session participants will learn more about preparing their infrastructure for a post-quantum. This includes: An overview of the quantum landscape and associated threats Ideas for a successful migration strategy Key things to ask vendors when evaluating solutions Understanding of Encryption or Post Quantum Cryptography (PQC) is recommended.

### Find the problem faster, A Technical Deep Dive into Splunk Observability Cloud - BRKOBS-2006
Speakers: Heath Johnson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271982505001z2vS
Do the Application Admins blame the network team for application issues? Are you drowning in a sea of complex interdependent infrastructure? Do trouble tickets just get passed around between different teams? Do you have so many tools for monitoring that you don't know where to look anymore? Join us for a comprehensive technical deep dive into Splunk Observability Cloud, where we explore how to navigate the complexities of modern application architectures. As digital transformation accelerates, the need for robust Infrastructure and application monitoring solutions becomes paramount. This demo heavy session will show the key features of Splunk Observability Cloud, showcasing how its AI-powered capabilities enable organizations to find & fix issues faster, ensure reliability and take control of your data & costs. You will walk away understanding how aggregating Logs, Metrics, and Traces will give you the magic decoder ring for your applications and infrastructure. You will see how fast Splunk can find the problem inside your highly complex Infrastructure. You will understand how Splunk eliminates the noise and helps make your clouds highly resilient.

### Fine Tuning your LLMs with NVIDIA-powered UCS-X and Hugging Face APIs - DEVNET-2081
Speakers: Allie Brenner (Cisco), Bruno Franca (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899417001zWA5
Fine-tuning a large language model (LLM) is crucial for adapting it to specific tasks or domains, thereby improving performance and accuracy. This process enhances the model's ability to generate more relevant and context-specific responses, making it effective for specialized applications. In contrast, Retrieval-Augmented Generation (RAG) boosts performance by using external knowledge sources, suitable for scenarios requiring the most current or specialized information without changing the model's core parameters. Both methods are important and should be employed based on the focus. In this workshop, you will learn how to fine-tune an LLM using PyTorch and the trainer API. To evaluate if fine-tuning was effective, attendees will measure the accuracy of the LLM before and after the fine-tuning. This workshop will explore writing Python code to leverage NVIDIA's GPUs to fine-tune the LLM running on Cisco's UCS-X series hardware.

### Five Enterprise Strategies for Optimizing Wi-Fi Performance and Reliability - VILEWN-2000
Speakers: Anil Gupta (Wyebot)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271937276001zWci
As reliance on wireless networks for business-critical operations expands, optimizing Wi-Fi performance becomes essential for maintaining productivity. This session explores five proven strategies that enterprise IT teams are implementing alongside their Cisco infrastructure to enhance wireless reliability and resilience. You'll leave with ideas to help you gain comprehensive client-side visibility, proactively identify potential issues, and reduce troubleshooting time across your network ecosystem. The session includes real-world examples of how AI-powered optimization techniques complement your existing Cisco infrastructure. Live demonstrations will showcase how these strategies provide deeper insights into the true end-user experience for more reliable wireless networks.

### Fortifying Meraki API access with OAuth 2.0 - DEVNET-2346
Speakers: Oren Brigg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904805001zRFS
As cloud-managed IT solutions continue to evolve, integrating secure and scalable authentication mechanisms is more crucial than ever. This session on OAuth integration with Cisco Meraki is essential for anyone looking to stay ahead in modern network management. After the session, you will: Understand the fundamentals of OAuth 2.0 and its role in securing API access Learn how to configure and deploy OAuth applications within the Meraki dashboard Discover best practices for token management and API security You'll leave this session with insights on how to enhance your network management capabilities using Meraki's APIs. This session is ideal for Meraki admins leveraging Meraki APIs. Whether you are a novice or have some experience, this session will provide you with the knowledge to create robust OAuth integrations. The session includes detailed explanations, real-world examples, and expert insights, ensuring you are well-prepared to implement OAuth integrations efficiently and securely.

### From Asset Chaos to Framework Compliance: Mastering CIS and NIST CSF Requirements - VILSEC-2034
Speakers: Joseph Alapat (Liongard)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271992871001zh0l
Effective cybersecurity starts with knowing what you're protecting. Asset management is the foundation of both the CIS Controls and the NIST Cybersecurity Framework (CSF), enabling the visibility needed to assess risk, prioritize actions, and maintain compliance. This session explores how IT and security teams are automating asset inventory and configuration tracking to align with CIS Controls and key NIST CSF functions. Learn how automation helps maintain real-time visibility, detect unauthorized changes, and reduce manual effort across complex environments. What you'll take away: Actionable guidance on aligning your asset management practices with CIS and NIST CSF requirements Real-world examples of how to use automation to maintain accurate inventories and reduce audit fatigue Best practices for integrating asset intelligence into your broader security and compliance strategy Leave with a clear understanding of how foundational asset management fuels stronger security, simplified audits, and better cyber resilience.

### From Chaos to Clarity: How Collaboration Observability Powers Enterprise Performance - VILCOL-2023
Speakers: Garrett Gladden (Kollective Technology)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848609001zFP2
Join us as we unveil our groundbreaking Collaboration Observability app in Splunk — a solution that transforms the way enterprises monitor and manage their Collaboration experience. In this session, We'll explore why experience monitoring may even outshine traditional service availability metrics, dive into the role that collaboration workstreams play in modern enterprise environments, and demonstrate how simplifying tier 1 support can serve as the "canary in the coal mines" for network health. Our deep-dive discussion will cover: The Primacy of Experience Monitoring: Discover why measuring end-user experience delivers a more comprehensive insight into system performance than conventional service availability monitoring alone. Learn how subtle shifts in user experience can preemptively flag issues before they escalate into full-blown service disruptions. Collaboration Workstreams as Enterprise Lifelines: Understand the pivotal role that dynamic collaboration channels have in driving productivity and innovation within organizations. We'll explore how streamlined communication channels and collaborative processes are not just support functions, but core drivers of business success. Simplifying Tier 1 Support with Observability: Learn how making tier 1 support for collaboration dead simple is not just a technical goal — it's a strategic imperative. We'll illustrate how our Collaboration Observability app acts as an early warning system, delivering real-time insights into network health and performance, and ensuring rapid resolution of potential issues. Whether you're a seasoned IT professional or a business leader seeking to optimize collaboration tools, this session will equip you with the insights and strategies needed to transform your enterprise's approach to observability. Discover how Splunk and Kollective's joint innovation is turning complexity into clarity, and learn how to leverage these insights to enhance overall operational excellence.

### From Circuit Boards to the Data Center: Troubleshooting Techniques for Infrastructure Engineers - CISCOU-2068
Speakers: Chuck Stickney (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271843273001zHvo
Services are down, packets seem to be spillin' on the floor. On days like these, it rains and it pours— you're under pressure. Explore troubleshooting theories and methodologies derived from electronics technicians and apply them to IT infrastructure. Learn systematic techniques to efficiently identify and isolate faults, enabling rapid service restoration with minimal guesswork.

### From Code to Conversations: Building Mistral AI Agents for Cisco Devices - CISCOU-1060
Speakers: Alexander Stevenson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840637001zEVC
This session provides clear analysis of and instruction on using Mistral's generative AI platform to simplify and enhance Cisco device management workflows. It includes a detailed walkthrough of Mistral's API architecture, infrastructure, and tooling, showing how to create a task-specific AI Agent from scratch. Participants will learn how to aggregate Cisco device outputs, analyze them with Mistral's API and models, and generate actionable insights to enhance Cisco workflows. Finally, the session highlights why Mistral is a strategic partner for Cisco, focusing on its frontier large language models (LLMs), deploy-anywhere capabilities, and custom AI services that support scalable enterprise use cases. Key Takeaways: Participants will gain a deep understanding of Mistral's API architecture and how to build task-specific AI Agents. You will discover the potential of Mistral-powered AI to drive operational efficiency and enhance Cisco device management through a detailed walkthrough of Python code. Explore the continued evolution of intelligence and interaction, examining how AI and technology are transforming across technological, linguistic, physical, and ethical dimensions.

### From Complexity to Clarity: Simplifying & Securing Campus Networks in the AI Era - CENENT-1411
Speakers: Nick Edwards (Cisco), Matt Gillies (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592613479001X1C0
In a world of more - more users, devices, technologies, cyber adversaries, stakeholders, and expectations - operating networks of any size can be complex. When you have thousands of devices to manage across a global infrastructure, scaling securely is nearly impossible. Everyone is going to need to scale. No one can afford downtime or a costly mistake. Yet the era of AI is unlike any before. The networks of today will not be able to handle the new and evolving requirements. A new architecture for the Campus is needed. 1) Hardware built for the AI era: high performance, low latency, high bandwidth, and power efficient. 2) Security infused into the network from foundational hardware to the application layer with quantum-resistant encryption technologies to safeguard against current and future threats. 3) AI across the lifecycle keeps operations simple so you can scale more easily with fewer resources. Onboard easily, define policies, upgrade with minimal disruption, and gain comprehensive insights across both owned and unowned infrastructure.

### From Data to Action with ThousandEyes Traffic Insights: End to End Synthetic Monitoring Meets NetFlow - BRKOBS-2019
Speakers: Bernie Clairmont (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272017090001z6xP
Cisco ThousandEyes Traffic Insights enhances enterprise network visibility and assurance by integrating NetFlow with synthetic monitoring. Learn how ThousandEyes Enterprise Agents can collect and parse NetFlow. See how to analyze NetFlow using ThousandEyes Traffic Insights and identify the root causes of network issues, such as increased load from specific applications or high traffic volumes from individual users. Learn about customizing alerts, NetFlow dashboards, and how to isolate application traffic. This integration of flow and synthetic data enables network teams to swiftly pinpoint and resolve issues, improving mean-time-to-resolution (MTTR) enhancing end-to-end digital experience assurance by turning your network data into action.

### From VLAN Sprawl to Adaptive Policy: Simplifying and automating Network Segmentation with TrustSec and Network-as-Code - BRKXAR-2034
Speakers: Gowtham Tamilselvan (Cisco), Jay Tiwari (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871199001zmON
Combining Cisco TrustSec with adaptive policy transforms network design by decoupling security policy from the underlying network infrastructure. This approach centralizes policy management while leveraging security group tagging (SGT) for consistent policy propagation and enforcement across diverse devices. By integrating network-as-code principles, security policies can be provisioned seamlessly across platforms: Meraki-as-code for cloud-managed Meraki devices, ISE-as-code for centralized policy management, and SD-WAN-as-code for Catalyst edge routers. This session presents real-world use cases of SGTs in enabling efficient network segmentation across Catalyst and Meraki devices. Attendees will learn how these solutions help reduce the number of subnets and VLANs in branch networks without compromising segmentation. The session also showcases enhanced security enforcement, streamlined device provisioning, and improved policy management through automation. This CX-led case study highlights the practical benefits of TrustSec and adaptive policy in achieving simplified, secure, and scalable network designs.

### From Verification to Access: Strengthening & Automating Workforce Identity with Persona & Cisco Duo - CNCSEC-1009
Speakers: Bobby Baek (Persona)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271990738001zbY0
In a world where users, devices, and data move fluidly across platforms, identity has become the key to access and the primary target for attackers. To stop modern identity threats, especially with the emergence of GenAI and deepfakes, organizations need to proactively identity verification throughout the user journey to address scenarios where MFA alone may not provide sufficient assurance of a user's identity. In this session, we will highlight how Persona and Cisco Duo are helping organizations stay ahead of identity-based threats. By embedding identity verification directly into Duo's access workflows, you can prevent unauthorized users from gaining a foothold during onboarding, account recovery, or elevated access scenarios.

### From Zero to (Super)Hero - Mastering Browser Synthetics using ThousandEyes Transaction Tests - CTF-1029
Speakers: Mauro Caballero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271975868001zAXS
Are you responsible for the end-to-end user experience of your company's web applications? Are you looking to finally stop the blame-game between network and application teams? Are you interested in automation but you just don't know where to start? This session will focus on delivering the foundations you need to monitor your web applications using browser synthetics. You will learn the basics of web page elements and how to use ThousandEyes' Transaction Tests to automate and get insights out of a simulated user interaction.

### From Zero to Hero - How to successfully implement Data Center Automation using Service as Code - BRKATO-2000
Speakers: Peter Charpentier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271832824001zlbg
Is your Data Center struggling to keep up with the rate of change requested by the business? Are you struggling to find the right strategy for implementing Data Center automation? Do you have somewhat implemented automation, but still have questions? Then this session is for you! Automation has become a critical core element of the modern Data Center to drive consistency, speed, and efficacy. Just like public clouds, Data Centers are much more dynamic with workloads adapting to changing needs, increasing technologies, people and processes. Together, we'll dive not only into the technical implementations and challenges, but also into practical experiences and lessons learned from automation projects with multiple customers. We will share organisational challenges, such as siloed organisations and personnel not being comfortable with automation and digitisation within the company. We will address how these challenges can be overcome, as well as describe different ways that the automation can be approached, depending on where you and your company are on the data center automation journey. This session will take us through the journey of successfully deploy Day0, Day1, and Day2 automation to your Data Center using a model driven approach - implemented using tools like Git, Terraform, CI/CD pipelines, and augmented by Gen AI to enhance validations. Though this session will focus on automation for Cisco ACI and Firewalls, the technologies can still be applied for other technologies and platforms. Please join us for a fun, interactive, and informational time.

### From Zero to Model-Driven Telemetry Hero - DEVNET-1952
Speakers: Bartosz Luraniec (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271897711001zWMK
Model-Driven Telemetry (MDT) allows for near real-time measurements of operational data from networking devices. Performing advanced monitoring can trigger remedial tasks that usually require human intervention. Introducing MDT solution offers companies the opportunity to reduce the cost associated with large IT departments and to allocate human resources more strategically, focusing on proactive activities rather than reactive. The session will describe the architecture of an analytics platform and demonstrate how streaming telemetry can be used in an environment of Cisco IOS-XE and IOS-XR devices. The participants will have the opportunity to learn how to collect data from devices, analyze it and visualize in near real-time using open-source tools.

### From Zero to Multi-Cloud Hero in 60 Minutes - BRKCLD-2409
Speakers: Pedro Antunez (Cisco), Matthew Howlin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271846727001zqwM
As the session begins, the timer will start - and the countdown to Multi-Cloud success will begin. You will see that it is possible to deploy a Multi-Cloud setup in 60 minutes. Whilst the automation pipelines flow, attendees will be guided through exactly what is happening in real time. First up, deployment of an on-premises Cloud Platform, achieved through Infrastructure-as-Code and cross-domain orchestration of Application Centric Infrastructure (ACI), Virtual Machines and Kubernetes. Second, we extend to the Public Cloud using Cilium, deploying a microservice application across our Cloud locations. We will then monitor the distributed application with Hubble.

### From zero to NetDevOps hero: automate YOUR use cases! - DEVNET-1191
Speakers: Marc Nufrio (Cisco), Tim Glen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271894558001zmjp
You know you need infrastructure automation. You've heard of Ansible, Git, Python, Terraform, and so many other tools. You're overwhelmed by the long road ahead, and don't know where to start in your environment. Starting from your actual pain points, this session will teach you guiding principles around identifying, building and automating your use cases, and then scaling these use cases. Cisco's automation examples may not be your real-world use cases. That's why this session will walk you through real network automation examples to teach you a process you can take away and re-use.

### Future Proofing Workplaces: Cisco's Network Architecture for the AI era - ITLGEN-2069
Speakers: Anurag Dhingra (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271958018001zu65
The AI revolution is reshaping network demands, requiring infrastructures that can handle higher data loads, growing security risks, and sophisticated AI threats. To meet these demands, Enterprises are challenged with modernizing their workplaces, and ensuring they are ready for anything. This is the Future Proofed Workplace - optimizing a new way of working and delivering flexible, secure solutions. Join this session to hear how Cisco's next-generation networking products combine across switching, routing, wireless, and Industrial IoT — along with collaboration and assurance — to address these demands and deliver enhanced performance, advanced security, and streamlined management. Attendees will see demos of Cisco's newest product launches to help organizations leverage AI while ensuring strong security and efficient operations. And you'll see how future proofed workplaces will empower you to navigate the complexities of the AI era with confidence.

### Future of AI-Powered Enterprise Networks - CNCNWT-2008
Speakers: Lalit Madan (Infosys Limited)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971975001zetu
The explosive growth of AI demands a network infrastructure shift in two perspectives. “Networking for AI” focuses on building high-bandwidth, low-latency, scalable networks for AI workloads, requiring advancements in hardware and protocols to handle massive data flows, ensuring resilient, secure, and efficient networks. “AI for Networks” leverages machine learning for network management, enabling intelligent automation, anomaly detection, predictive maintenance, and optimized resource allocation. This session explores the critical interplay of AI and networking for organizations navigating the evolving landscape of technology.

### Future of Enterprise Inference - CNCGEN-2001
Speakers: Kevin Swope (Intel Corporation)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271943558001zjmq
As AI continues to expand into the Enterprise inference is becoming a key workload, understanding how to effectively inference across on device, edge, and data center is paramount to creating a well balanced approach and optimizing your TCO.

### Future-Proofed Workplaces - From AI Hype to Reality - ITLGEN-2053
Speakers: Keith Griffin (Cisco), Jen Yokoyama (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271956675001zCET
Generative AI offers tremendous opportunities for the workplace, but also comes with risks. This session will cover the application of AI to enable hybrid work and best practices to enable adoption of AI using Cisco's responsible AI framework.

### Future-proofing Campus Switching for WiFi7 - BRKENS-2608
Speakers: Minhaj Uddin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271921267001zpFS
As the demand for faster and more reliable wireless connectivity continues to grow, Wi-Fi 7 emerges as a groundbreaking technology poised to transform network performance. This session explores innovative switching solutions designed to future-proof network infrastructures and fully leverage the capabilities of Wi-Fi 7. Participants will gain insights into the latest advancements in switching technologies that ensure seamless integration, enhanced scalability, and optimal connectivity. Join us to discover strategies that not only address current networking challenges but also anticipate future needs, paving the way for a robust and efficient wireless environment.

### Future-proofing Industrial and Critical Infrastructure Networks for Cybersecurity and AI - PSOIOT-1019
Speakers: Bryan Tantzen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271951563001zs6n
Operational Technology (OT) networks that support critical and industrial infrastructure are at a critical inflection point. Increasing cybersecurity threats, rising operational complexity, and a global shortage of skilled labor threaten their stability and efficiency. Simultaneously, the growing need for data-driven capabilities, AI-ready infrastructure and digital resilience demands modern, scalable, and secure networks. This session explores the opportunity to accelerate IT/OT collaboration, how to identify the right strategic solutions and partners and highlights the operational and financial benefits IT/OT collaboration delivers. Attend this session to learn more about how: • Cybersecurity urgency and AI readiness are driving OT network modernization • Early movers are seeing significant operational and financial benefits • How OT security, multi-network application observability, IT/OT collaboration, cloud-based management and AI optimized networking are transforming industrial operations.

### Gain Call Center Queue Insights with Queue Analytics for Webex Calling - VILCOL-1063
Speakers: Jason Forehand (ISI Analytics)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271847865001zFaa
As organizations transition from on-premises UC solutions like Cisco UCM to Webex Calling and other cloud platforms, robust queue analytics become crucial for business success. Join our CEO, Jason Forehand, for an insightful discussion on queue analytics. This session will demonstrate how to leverage ISI Analytics' queue analytics to enhance your call center operations with Webex Calling, and other platforms, catering to organizations that utilize multiple UC environments. Key Takeaways: • Optimize Your Migration Strategy: Learn how to seamlessly transition to cloud platforms while maintaining operational efficiency. • Boost Collaboration and Efficiency: Discover how queue analytics can improve collaboration and streamline your call center operations. • Explore Key Features and Benefits: Understand the unique advantages of ISI Analytics for Webex Calling Audience Expectations: This session is tailored for business line managers looking to enhance their call center operations. No advanced technical knowledge required. Special Elements: Experience live demos and hear customer success stories that showcase the transformative impact of queue analytics on collaboration and productivity.

### Gain Control of AI's Impact on Network Traffic and User Experience - AIHUB-2013
Speakers: Paul Thompson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271975073001zZr1
AI traffic behaves differently to most other traffic types and needs a different approach when it comes to monitoring and assurance. Before AI applications go live, vast amounts of training data needs to be reliably moved around the network. Once AI applications move to production, continuous monitoring of the network layer and the supporting protocols needs to happen automatically. The ultimate goal is to ensure that end users have a reliable and responsive experience with any AI application they interact with. In this session, you will learn how Cisco Provider Connectivity Assurance and cross-architecture integrations with other related Cisco platforms can determine what network traffic is due to AI, its impact on the WAN and Data Center, and assurance for operations of AI applications throughout the network.

### Gain Scalable, Deep Visibility into Network Traffic with Cisco Nexus Dashboard Data Broker - BRKDCN-1614
Speakers: Mallikarjuna Rao Mudigonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271882488001zI2X
Visibility into network and application traffic has become increasingly important in our modern data centers. Network visibility is integral to network security, compliance, troubleshooting, and capacity planning. Custom monitoring solutions cannot cope with the explosive growth of data center networks. In order to match the port density and port capabilities of the data center, monitoring networks must also leverage those same switches used in the production network. Cisco Nexus Dashboard Data Broker (NDDB) is an automated, intelligent packet brokering solution that can scale with your data center. NDDB provides a software-defined, programmable solution that can aggregate, filter, and replicate network traffic using SPAN or optical TAPs for network monitoring and visibility. This solution offers a simple, scalable, and cost-effective solution that is well suited to customers who have a need for monitoring large amounts of traffic or business-critical traffic. This session will cover the following: Introduction to Nexus Dashboard Data Broker TAP and SPAN aggregation use case In-line monitoring use case Integration with other Cisco products Demonstration of the NDDB interface Product Demo

### Gaining insights and cross-layer visibility utilizing ThousandEyes, Terraform, and GitHub. - DEVNET-2053
Speakers: Edwin Salazar (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271898662001z6iH
For a comprehensive digital experience for your customers, it's crucial to consider all aspects of the digital experience supply chain: application availability, usability, and dependency. Understanding how the Internet and external factors influence your web application uptime is key. It requires visibility into routing, end-to-end paths, performance (such as latency or loss), and hop-by-hop metrics. A high-level and technical introduction to the solutions used will be carried out, followed by a live demonstration of the results obtained in performance measurements. The implementation and benefits of Cisco ThousandEyes technology are combined and complemented with tools used in DevOps, such as Terraform and GitHub.

### Game On: How Acuative Keeps Cisco Networks Up, Secure, and Affordable - VILENT-2001
Speakers: David Kay (Acuative)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271872147001zalC
Skip the slides — join a high-energy, Kahoot-style session where quick answers win prizes and practical insights. In just 15 minutes, Acuative will show how we help enterprises crush downtime through FISMA-certified services, 4-hour MTTR field techs, secure network design, and wholesale connectivity pricing. What sets us apart? Our ability to bring together the full power of Cisco's technology stack into customized solutions that actually work in the real world — keeping networks up, costs down, and customers ahead. Play to win. Leave with strategies you can act on now.

### Gen AI: Jumpstarting Outcomes - CNCDCN-1018
Speakers: Michael Hommer (NetApp)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271875868001zCiO
AI is the current tech innovation. But how do you translate innovation into meaningful business impact. This session will highlight how NetApp and Cisco can help jump start Generative AI projects from concept to functioning reality. With FlexPod AI, customers can spend less time building and more time leveraging Generative AI models to move their businesses forward.

### GenAI Your Way: Reimagine Network Troubleshooting - BRKOPS-3822
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271990358001zVa9
Join us as we reimagine network troubleshooting with Generative AI (GenAI)! Traditional troubleshooting can be a time-consuming and complex process, requiring expertise and manual effort. What if you could simplify the process by building your own AI-powered solution using open-source models? In this session, we'll explore how GenAI will transform network troubleshooting, freeing you to focus more on on issue-solving. It will reduce the time spent on data collection and analysis of the network configuration, operational state, and logs. You'll discover how to leverage GenAI to gain real-time insights into network issues, extracting with ease valuable details from large datasets, for a faster issue resolution. We'll review the core concepts to build your AI platform, including Retrieval Augmented Generation (RAG), vector representations and databases, Large Language Models (LLMs), Function and Tool Calling. Prior experience with GenAI and LLMs is beneficial, but not required. Demos and complete open-source GenAI solution sample code will be included. Don't miss this opportunity to reimagine network troubleshooting - GenAI Your Way!

### GenAI in Action! See how we transform Customer Experience with our AI Agent and deliver on business outcomes - BRKCCT-2018
Speakers: Ramy Riad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271864674001z5kI
The future of CX is being revolutionized by AI and Cisco is uniquely positioned to help customers realize this vision with a unified AI fabric across the Webex Suite. In this session we will take you on a journey to address core challenges contact center leaders are facing today: transforming self-service to be more than a knowledge bot, equipping agents to focus on more complex issues, and bringing together diverse channels and complex fulfillment systems in an orchestrated journey. We will share customer insights, demonstrate how this is helping them achieve their ROI, discuss AI Maturity Models... and of course, bring it all to life through technology demos. Come and join us!

### General Electric's Success: Scalable, Secure and High-Performance Data Centers with Nexus 9000 - CSSDCN-1400
Speakers: Daniel Morgan (General Electric Company), Swetha Chunduri (Cisco), Rob Gastrich (General Electric Company)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271875100001zffw
Join us to explore how General Electric transformed their network infrastructure to drive innovation and operational excellence. Discover how GE leveraged the Cisco Nexus 9000 Series switches, powered by NX-OS, along with the Cisco Nexus Dashboard, to accelerate network provisioning, enhance visibility, and streamline management. This session will highlight the company's journey in integrating Cisco's cutting-edge Nexus portfolio to build a robust, scalable network capable of supporting its complex global operations. Learn how these solutions enabled GE to simplify workflows, improve operational efficiency, and maintain a competitive edge in today's fast-paced digital landscape. Don't miss this opportunity to hear from Senior architects from GE spin-off companies and learn how Cisco's innovative solutions empower them to shape industries and drive digital transformation.

### Generative Technical Support: AI Driven Problem Solving - CISCOU-2060
Speakers: David White (Cisco), Mohammed Hamzeh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841775001zilp
In this session, we'll dive into how TAC is leveraging Generative AI through our Cisco AI Assistant to efficiently solve real-world technical support cases. You'll see firsthand how this AI Assistant intelligently analyzes support files, interprets images, and applies learned knowledge to resolve issues quickly and accurately. We'll also explore how the system continuously learns from interactions with human engineers, ensuring it gets smarter with each solved case.

### Get Out of the 90s: Modern Troubleshooting with Cisco APIs and Splunk - DEVNET-2879
Speakers: Juulia Santala (Cisco), Francois Caen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271907717001ziWr
Are you fed up with your users blaming the network every single day? Do you waste vast amounts of time chasing down root causes across too many platforms? Your Cisco infrastructure is full of real-time data, telemetry, alerts and APIs. Yet your monitoring is stuck in 1999, with a classic mix of SNMP interface graphs, a pile of syslogs, and emails nobody reads. Is anybody even catching SNMP traps anymore? Become the hero of your network's story! In this session, you will learn how to utilize the APIs already available in your network to access troubleshooting data and telemetry from multiple sources, combine them in a meaningful way, and take better action faster. This session will take you on a multi-platform adventure full of demos, covering how Cisco solutions such as Catalyst, Meraki, ISE, and Splunk can be brought together for easier monitoring and troubleshooting. Let's sprinkle some magic on your use cases with a little help from your network's APIs!

### Get into Git! The Advanced guide to Git commands - DEVNET-2123
Speakers: Kareem Iskander (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271900177001zw2R
Git clone, git add, git push. Been there, done That! This session will skip the introduction of git and get to the more advanced git tutorials, things like Merging vs. Rebasing and Advanced Git logging. I will cover topics that take you to the next level of your git skills! Join in the fun, and let's Git it!

### Get operational insights quickly with natural language queries for the Splunk Platform - BRKOBS-1021
Speakers: Jeff Wiedemann (Cisco), Nick Ma (Cisco), Mohit Verma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271979528001z1My
Discover how the Cisco AI Assistant unlocks operational data insights in the Splunk Data Platform using natural language queries. Learn to simplify complex data analysis, accelerate decision-making, and empower teams with intuitive, AI-driven exploration. This session reveals how conversational queries enhance visibility, streamline workflows, and deliver actionable intelligence from your operational data effortlessly.

### Getting SASE with Umbrella and Meraki - Understand best practices for simple and flexible integrations between Meraki and Umbrella - BRKSEC-2238
Speakers: Chris Riviere (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272002337001z4A8
Learn about the latest integrations with Umbrella and Meraki now available as Secure Connect Foundation. These simple integrations allow for extremely flexible deployments in your environment. Select the security tier that best aligns with your organization's requirements, from Meraki MR/MX - DNS integration to DNS integration with selective proxy. In addition, learn how seamlessly you can extend your Meraki network into Cisco's security cloud to unlock a comprehensive set of SSE features. This session will dive into the details of each integration—covering simple setup, enhanced attribution, and streamlined management—while clarifying when to leverage each option and the benefits they deliver.

### Getting Started with Event Analytics: Turning Alerts into Actions - BRKOBS-1014
Speakers: Hitesh Kalluru (Splunk), Annette Sheppard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271978753001zzQP
Overwhelmed by constant alerts across a myriad of monitoring tools? Struggling to identify service-impacting issues? In this webinar, see how Event Analytics inside Splunk IT Service Intelligence gives IT Operations teams the visibility and insight to stay ahead of critical incidents. We'll showcase how to kickstart alert correlation and achieve fast time to value with incident response following an easy step by step process. We'll also discuss how to minimize alert noise at the source and prioritize the most important issues first with historical KPI data analysis and ML-Assisted Thresholding (powered by Splunk AI) giving you an understanding of where AI and machine-learning is enhancing the effectiveness of problem identification and upcoming capabilities to look forward to. Whether you are just starting or want to optimize your current strategy, join this session to learn: Approaches to aggregate events and reduce alert noise with out-of-the-box content How to identify issues and avoid false positives before they impact your business Ways to accelerate incident investigation and response

### Getting Started with Firewall Decryption: A New, Streamlined Approach for Advanced Protection - BRKSEC-2160
Speakers: Bill Spry (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272000560001zmiJ
In today's landscape, where nearly all traffic—including malicious traffic—is encrypted, firewall decryption is essential for optimal inspection and protection of users and applications. The upcoming release of Cisco Secure Firewall introduces an innovative interface that overcomes traditional challenges, paving the way for seamless enterprise decryption. Discover how easy it is to create a decryption policy using the new interface, featuring intuitive controls that meet compliance and performance needs. Additionally, leverage new Machine Learning-powered capabilities to focus decryption efforts on the riskiest traffic.

### Getting Started with Routed Optical Networking - BRKMSI-1002
Speakers: Alan Liew (Cisco), Emerson Moura (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966786001zMFP
If you haven't heard about Routed Optical Networking or if you heard about it but still struggle to understand why it's such a big step towards building more cost effective, simple and efficient networks, this session is for you. You will learn the fundamentals of the Routed Optical Networking, the key technology components and the basic design principles that will help you collect the most benefits of this breakthrough networking architecture.

### Getting Up and Running with Open-Source Local LLMs on UCS - with NVIDIA and AMD - AIHUB-2102
Speakers: Dave Zacks (Cisco), Patrick leMaistre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271913161001z0WI
Many organizations need to deploy local LLMs leveraging private, confidential data - using on-premises compute resources, leveraging Generative AI systems enhanced with RAG (Retrieval Augmented Generation). The Cisco UCS platform provides a number of key advantages for such deployments, including X-Fabric for unrivalled flexibility. Come to this session to explore how Cisco UCS can be used with both NVIDIA and AMD GPUs to accomplish this goal - and see for yourself the benefits that this solution provides. Hosting this session is the dynamic duo of Dave Zacks and Patrick leMaistre, both experienced Cisco Live speakers as well as AI enthusiasts. Come to this session for a fun, engaging and fast-paced exploration of using open-source LLMs, RAG, and Patrick's own custom toolkit to drive LLM projects that you can deploy within your own organization!

### Getting Webex Administration Troubleshooting Under Control in Control Hub - BRKCOL-3017
Speakers: Paul Stojanovski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857981001zmxl
Whether you're deploying the Webex Suite, recently migrated your Webex site, or are aiming to get a better understanding of Webex administration, Control Hub is your home. It is the single pane of glass for Webex administration. As Control Hub continues to expand, understanding how to effectively troubleshoot aspects of administration becomes critical. This session will delve into critical areas of Webex administration that generate TAC cases. Expect to learn more about: Troubleshooting users and groups Troubleshooting Webex site and org features Leveraging troubleshooting tools such as Analytics, Reporting, & Troubleshooting (Logs) You can expect to come out of this session with the understanding of what drives the most Webex TAC cases.

### Getting the best out of Webex Calling ... when migrating from Unified Communications Manager - BRKCOL-2084
Speakers: Johannes Krohn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853003001zhrs
Webex Calling offers a comprehensive enterprise-grade feature set to address a wide array of business requirements. When migrating to Webex Calling from Unified Communications Manager focusing too much on replicating Unified CM features 1 for 1 on Webex Calling will lead to a suboptimal solution. This session helps to understand the challenges and offers guidance on how to get to an optimal Webex Calling deployment while reducing the implementation effort by using existing tools that gather Unified Communications Manager configuration data to drive the Webex Calling setup. In this session we will highlight superior capabilities of Webex Calling, discuss fundamental differences between Unified Communications Manager and Webex Calling and compare capabilities of both calling solutions. We will also give an overview of existing tools to support the migration. Some experience with both, Unified Communications Manager and Webex Calling, are a prerequisite. This session does not cover Webex Calling Dedicated Instance.

### Getting to know the Splunk Data Platform - your Intelligent Data Fabric for Cisco and beyond - BRKOBS-1016
Speakers: Shalabh Goyal (Cisco), Yogesh Sontakke (Splunk, a Cisco company)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271979149001zUxf
Now more than ever, business decisions and success depend on high-value data. Splunk is leaning into this vital approach to fuel your success and give customers more options than ever before to define their data's value. In this session, we will show how new features in Splunk® Cloud Platform can filter low-value events, redact sensitive information, convert logs to metrics for observability and even route to multiple destinations based on value, and then run analytics on your data in Splunk or elsewhere. Get ready to accelerate your data's value!

### Getting your Basics right - Cisco DevNet Automation Journey Kickstart - DEVNET-1714
Speakers: Siddesh Nayak (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271897094001zc5y
This is an introductory session intended for Network engineers, Devops engineers and SRE's aspiring to commence their network automation journey with Cisco devnet. The session will cover all the basics, tailored to include the necessary topics to implement a network automation code using python to interact with any Cisco devices and kickstart your devnet journey with ease At the end of this session, participant will have strong foundational knowledge of: 1. Python and linux essentials to follow the presentation content. 1. Formats for data modellling language and use-cases - JSON,XML,YAML 2. NetConf and RestConf concepts,differences and use-cases 3. Concept of Data modelling with YANG in network automation 3. PYANG and Yangsuite with example of real world use cases for building xml query for Netconf. 4. Step by step method to develop a python code to connect to a device, retrieve the configurations and make configuration change to a device using Netconf. 5. Overview of POSTMAN tool. 6. Step-by step method to use POSTMAN to validate restconf api to interact with Cisco platforms. 7. How to work with GIT and GIT hub with demo of committing your first devnet code to Git Hub 8. Navigating the Cisco Devnet documentation page for API/Sandbox usage to interact programmatically with all supported Cisco platforms.

### Goodbye Legacy, the Move to an IPv6-Only Enterprise - BRKENT-2008
Speakers: David Prall (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271931106001zxXn
This session is for those who currently have IPv6 deployed in a dual-stack environment and are looking to transition from dual stack, to IPv6-mostly, and on to IPv6-only. IPv6 was chosen as the recommendation for the IP next-generation protocol in RFC 1752 in January 1995. Many RFCs since have delivered updates and enhancements. The specification RFC 1883 was published in December 1995, becoming RFC 8200 (STD 86) in July 2017, making IPv6 an internet standard. Just as we've said goodbye to legacy protocols IPX/SPX, DECnet, AppleTalk, and others, it is now time to say goodbye to IPv4. The most significant mandate is Memorandum M-21-07 in November 2020, titled "Completing the Transition to Internet Protocol Version 6 (IPv6)." They set a timeline for 80% IPv6-only completion by September 30, 2025, end of fiscal year 2025. In this session, we will focus on the move from dual-stacked IPv4 and IPv6 enterprise infrastructure to an IPv6-only infrastructure. What do we need to know before we make the move? What about IPv4-only enclaves? We will look at NetFlow as the picture of truth and NAT64/DNS64 as the transition gateway(s).

### Green Security: Automating Threat Response and Access Control for a Sustainable Cyber Defense - AIHUB-2012
Speakers: Jetsy Mathew (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271830753001zobs
This session explores the Triple-A Security approach—Access, Actions, and Accountability—and how automation can streamline these critical security elements while minimizing environmental impact. We'll dive into how Cisco XDR, Cisco Secure Firewall, and Cisco Threat Response work together to automate access control, streamline threat detection and response, and provide real-time accountability. By leveraging these tools, attendees will learn how to create a greener, smarter cybersecurity strategy that not only enhances security but also reduces resource consumption and operational overhead. Join us to discover how automation and the Triple-A principles can help you build a more secure, efficient, and sustainable future for your organization.

### Groq: An AI Success Story - Deploying High-Performance, and Low-Latency AI Networks Using Cisco Nexus 9000 - CSSDCN-2005
Speakers: Swetha Velamuri (Cisco), Cameron Ferdinands (Groq)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879213001zkhz
Groq delivers rapid AI inference both in the cloud and in on-premises AI compute centers by adopting a software-first approach to designing AI hardware. This success story illustrates how Groq utilizes Cisco Nexus 9000 Series switches and NX-OS to enhance the speed of iteration, driving a new wave of innovation, productivity, and discovery. In this session, discover how Groq leverages Cisco Nexus switches to achieve scalability, high bandwidth, low latency, and effective congestion management, all of which are critical for AI inference. Additionally, learn how Cisco optics accelerate network performance and reduce costs through innovations in optical technology and manufacturing. As a result, Groq is able to deliver the highest quality and fastest throughput for AI inference at a more affordable price point and with improved energy efficiency.

### Harness AI to Accelerate Time to Value with Cisco UCS - PSODCN-1010
Speakers: Eugene Kim (Cisco), Mahesh Natarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271880581001z9XI
Are you considering adopting AI to innovate, improve efficiency, make better data-driven decisions, reduce costs, or enhance customer experiences? Discover how Cisco UCS servers and validated solutions help get your data center AI-ready. Explore new UCS X-Series options and the complete portfolio of UCS servers and solutions that power AI workloads, including new model training, fine-tuning, and inferencing. Get ready to deploy AI solutions with the industry-leading security and performance you need.

### Harness the power of AI and digital channels to modernize your customer experience - BRKCCT-2017
Speakers: Shadab Abbasi (Cisco), Emerik Giorgetti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271865435001zz4T
Join us for an insightful session where we will explore how the combined power of AI and digital channels transforms customer service experiences. In Today's fast-paced landscape, leveraging Contact Center services such as social media and rich messaging is essential for staying competitive. Attendees will discover innovative approaches to harnessing digital channels and AI technologies to enhance and personalize customer journeys, increase satisfaction, and build lasting relationships. Don't miss this opportunity to gain valuable insights on how to apply these best practices to your own organization and elevate your customer service to new heights.

### Harnessing AI: How Splunk Leverages AI and Integrates with Cisco AI Defense - BRKSEC-2801
Speakers: Rene Aguero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003697001zqkQ
Discover how generative AI and large language models (LLMs) can revolutionize your security investigations. This session explores the future of AI in security operations and shows how it can streamline complex tasks, making them more accessible—even for SOC analysts with little to no Splunk experience. Learn how AI can empower your team to handle sophisticated incidents with greater speed and efficiency. Explore Splunk's AI Assistant as well as the Cisco AI Defense integration with Splunk. If you're ready to see how AI can transform your security workflows, this session is a must.

### Harnessing Generative & Agentic AI for Employee & Customer Experiences - AIHUB-1512
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848972001zZhT
A new wave of generative and agentic AI capabilities is set to transform how we work and engage with customers. From productivity features like meeting summarizations, highlights, and action items to autonomous customer service, AI is being deployed to improve employee and customer experiences alike. Join us to explore effective strategies for operationalizing AI, minimizing risks, and ensuring your business is ready to embrace the opportunities AI brings in an effective and secure way.

### Harnessing the Meraki Cloud Dashboard Day 0 to Day N with Terraform and Event Driven Ansible - BRKOPS-2188
Speakers: John Shea (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988190001zUXj
Meraki provides an intuitive and easy-to-use Click OPs platform managed through the cloud, with rich API capabilities for almost every aspect of the network. In this session, we will bring Meraki and Terraform together using Infrstructure as Code concepts to enable particpants to streamline their workflows, infrastructure management more efficient, scalable, and reliable with validated feedback post configuration deployment. Participants will see how to operationalize Terraform for cloud management, and provide insightful use cases for: - Quickly transition from Click OPs to IAC without having to rebuild your configurations. Attendees will experiance: Building networks at scale while maintaining individual state with a common codebase. Managing elements such as Security, Wireless, and Switching and their underlying features, with reusable modules - Consistency to make sure your Meraki networks are deployed as defined, and that configuration drift is identified and remediated Inventory Management Using Event Driven Ansible for capturing Configuration Change notifications for verification, logging, and creating automated follow up actions. and much more so join us as we bring the power of Cloud Networking together with the power of robust automation, and take your Infrastructure as Code journey to the next level!

### Harnessing the Power of Packets: The Single Source of Truth for Network Observability - CNCDCN-2011
Speakers: Iain Kenney (cPacket)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271876443001zRVi
In this session, you'll learn why packet data is the single source of truth and how leading organizations use cPacket's industry-leading solutions to leverage timestamping, integrated application decoders, and sustained line-rate capture to ensure 100% packet accountability. Discover how our flexible architecture supports hybrid-cloud environments, reduces Mean-Time-to-Resolution (MTTR), and optimizes tool efficiency for seamless network operations.

### High-Density Wi-Fi Design, Deployment and Optimization - BRKEWN-2087
Speakers: Josh Suhr (Cisco), Matt Swartz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941615001zaKG
Join us for an enlightening session highlighting advanced strategies and techniques for configuring and optimizing high-density Wi-Fi networks in today's most demanding environments such as stadiums, conference centers, auditoriums, and more. We will explore a wealth of practical tips, tricks, and tools, alongside invaluable real-world insights on leveraging the latest Cisco Wireless Access Points, Antennas for both cloud-managed, hybrid and on-prem deployments to deliver a seamless and reliable user experience. With the advent of Wi-Fi 7, we will also discuss how this next-generation technology can further enhance network performance and capacity. Don't miss this opportunity to elevate your understanding and expertise in cutting-edge wireless solutions.

### How Catalyst SD-WAN Analytics & Insights Powers Faster Mean Time to Innocence! - BRKENT-2351
Speakers: Sai Suchandan Reddy Marapareddy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271934186001ztj9
Cisco Catalyst SD-WAN builds a secure, unified connectivity over any transport and provides simplified operations with centralized management, policy control and application visibility across the enterprise network. Observability and Analytics are becoming one of the key differentiators for operational efficiency and there is no better place than the networking infrastructure to provide that visibility into user traffic and application performance which can help operations team to identify whether user experience is affected by Network or Application performance issues. In this session, we will take a closer look into the latest enhancements to Cisco SD-WAN analytics, which provide various historical insights and future predictions into applications and network performance. Through real-world use cases and demos, We'll highlight how Cisco SD-WAN Analytics offers granular insights into Applications performance, and combined with Network Wide Paths Insights (NWPI) & ThousandEyes to accelerate Mean Time To Innocence!

### How Cisco IT Tackled Network Observability and Feeds the Hunger for AI - BRKCOC-2035
Speakers: Manny Garcia (Cisco), Jon Heaton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837003001zuuO
In this session you'll learn how Cisco IT solved its needs, and how you can solve yours, for Network Observability and enabling Network data to be included in AI capabilities. Chapter 1: Impetus for Change: Cisco IT taking on our own operations, why we did that, what gaps we had to fill. Share the Need to gather any and all instrumentation for observability and feeding into AI (lots of examples, Netflow, Syslog, etc. Third is our desire for Cisco on Cisco stories for Splunk and Thousand Eyes Chapter 2: What we did... and you can too: Under tight timelines built the infrastructure, tooling, processes to gather, augment, present and notify. Chapter 3: Results/Demo Chapter 4: What's next: Correlation, User Experience (particularly Thousand Eyes), AI Use cases

### How Cisco build AI readiness IP Backbone with 8000 Series - BRKMSI-3000
Speakers: Rob Piasecki (Cisco), Ruben Lopes da Fonte (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963072001z05e
How Cisco is building AI Infrastructure to Webscalers. During this setion, you'll undertand requirements, technology RoCEv2, PFC and ECN. How to configure in details on IOS-XR, how to check via CLI PFC and ECN working, providing the right design for it.

### How Comcast Business and Cisco Meraki Deliver Advanced Network Solutions at Scale - CNCNWT-2007
Speakers: Joseph Austin (Comcast Business Communications, LLC)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971770001zwcq
For over a decade, Comcast Business has been at the forefront of deploying Cisco solutions, forging a robust partnership that has revolutionized the network technology landscape. In this presentation, we’ll delve into the collaborative journey between Comcast Business and Cisco and how the partnership has led to innovative solutions tailored to meet the evolving business requirements of multi-site businesses. Learn how Comcast Business, leveraging Cisco's cutting-edge technology, has deployed scalable solutions for some of the most challenging business environments. With deep technical understanding of Cisco Meraki, Comcast Business has helped businesses operate more effectively with faster deployments, greater scalability, and more reliable networks. Looking forward, Comcast Business and Cisco Meraki will be bringing feature-rich secure networking solutions to smaller-market businesses, making networking evolution more attainable. • The digital business needs driving the need for network modernization and scalability • Comcast Business and Cisco Meraki – partnership, innovation and history of large-scale deployments • Customer use case: How Comcast Business deployed Cisco Meraki at 10,000+ locations • Comcast Business and Cisco plans to broaden availability of their joint networking solutions offerings

### How It's Made: Cisco Secure Access - BRKSEC-2885
Speakers: John Rauser (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272004678001zvyX
In today's dynamic digital landscape, ensuring secure and reliable access to applications and data is paramount. With Cisco Secure Access we provide a cloud-delivered Security Service Edge (SSE) solution that enables unified connectivity with robust security controls and a seamless user experience grounded in Zero Trust principles. This session offers an in-depth exploration of Secure Access and its underlying technologies and architectures. Attendees will gain a unique look "behind the curtain" into how SSE is build and maintained at scale, including the engineering and operational strategies that underpin Cisco's approach to delivering cloud solutions. You will learn how Secure Access effectively safeguards users and resources using highly reliable, secure and resilient systems that your business can trust and depend on.

### How RedSky is Enhancing Emergency Response in Cisco Calling Environments - VILCOL-1064
Speakers: Dennis Penaranda (Everbridge RedSky), Adam Vedas (RedSky)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848048001zEQy
As today’s work environments become more mobile and complex, ensuring every 911 call includes the right location and reaches the right responders is essential. In this session, learn how RedSky’s E911 solutions, offered through Cisco’s OEM partnership, support reliable, compliant 911 calling in both Webex Calling and Cisco Unified Communications Manager (CUCM). You’ll also hear how Horizon Assist™ extends visibility into emergency events, helping safety teams stay informed and ready to act. What participants can expect to take away: • How RedSky enables location-aware emergency calling across Cisco platforms • A look at recent enhancements that make E911 management easier for IT and telecom teams • Ways Horizon Assist™ supports safety teams in other locations with real-time visibility, alerting, and routing This 15-minute session delivers a high-level overview of product updates, use cases, and real-world applications. Designed for IT, telecom, and network professionals working within Cisco ecosystems.

### How Steve Madden Accelerated Threat Response with Cisco XDR - CENSEC-1035
Speakers: AJ Shipley (Cisco), Kamran Siddique (Steven Madden, LTD)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592612572001XO9N
In today's threat landscape, security teams are under pressure to do more with less - fewer people, more alerts, and increasing complexity across IT environments. Traditional detection and response tools often fall short in delivering the speed, visibility, and simplicity modern teams need. Join us to explore how Cisco XDR is changing the game for security operations. You"ll hear directly from a customer about their journey to a more efficient and effective SecOps model - and how Cisco XDR helped them reduce noise, accelerate investigations, and improve outcomes.

### How a Network Digital Twin Ensures Post-Change Continuity for a Global Company - CNCOPS-2004
Speakers: Mike Lossmann (Forward Networks)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271983665001zrUW
Join this session to learn how a global HR software company uses the Forward Networks Digital Twin to ensure that network changes do not disrupt connectivity.Before implementing Forward Networks, the company did not have a standardized change process and frequently endured weekend-long conference calls trying to diagnose issues caused by simple changes. Now, with a standardized process and pre- and post-change verification processes, these calls are a thing of the past. Join this session to learn how to protect your weekend, and your network!

### How to Adopt Zero Trust using SD-Access and Default-Deny without Tears - BRKENS-3810
Speakers: Raphael Lienard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271922425001zA5g
In this session, you will learn how to leverage the full potential of Cisco SD-Access within a Zero Trust Architecture. Discover all the requirements and best-practices before breaking the network by turning the default security policy from Permit IP to Deny IP. You will also get insights on how to combine Cisco Telemetry Broker and Splunk to create a TrustSec live-log dashboard.

### How to Be a Network Engineer in a Artificial Age? - CISCOU-1053
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271836629001z48Y
'I'm sorry Carl, I'm afraid I can't do that.' Are we approaching the time when the network might decide it knows better than the engineer at the console? Are we on the cusp of a new age of network engineering - THE ARTIFICIAL AGE? It is certainly a time of excitement, ideas, and maybe a bit just a tiny big of fear. That's okay, that is what it means to be a network explorer and we are totally here for it. Join this session where we consider how AI fits into programmability, automation, and NetDevOps.

### How to Become the Data Center Operations Hero with Nexus Dashboard - BRKDCN-2637
Speakers: Joe Piperata (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885047001zH90
Today's data centers are multi-vendor and involve various complexities, making incident investigation and resolution quite challenging. Rapidly and accurately identifying and addressing issues across your data center switching, hypervisor, and applications is made possible by integrating solutions from multiple vendors under one umbrella. In this session, you will learn how Nexus Dashboard provides best-in-class data center operations, allowing you to easily identify and resolve performance and security issues, all serving to maintain business critical infrastructure and application uptime and availability. You will learn the ease with which Nexus Dashboard can be integrated with Cisco and third-party solutions to achieve the level of visibility desired by the operations teams. You will also learn about the more advanced features of Nexus Dashboard, highlighting the solution's ability to function as the cornerstone of your day two operations strategy. Not all heroes wear capes, but all data center operations heroes use Nexus Dashboard. Prior experience with Nexus Dashboard is not required.

### How to Build a CCNA Certification Practice Lab - BRKCRT-2024
Speakers: Joe Rinehart (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271835102001z2sg
For many in the IT industry, the Cisco Certified Network Associate certification is the entry point to a career in networking. While more advanced certifications such as the CCNP and CCIE get a lot of fanfare, the skills gained at the associate level are foundational and pave the way to greater accomplishments. Success on the exam requires more than just rote memorization; candidates must demonstrate finesse regarding configuration tasks as well. To facilitate that, those pursuing the CCNA will need to utilize a lab environment, in order to use hands-on practice. This session will lead candidates through ways to build their own environment.

### How to Build a Secure Multi-Cloud Environment with Cisco Secure Workload and Multicloud Defense - BRKSEC-2421
Speakers: Dirk Stoeckmann (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010386001z9Hy
Join this session on Cisco Cloud Security and protect your Cloud with precision. We will delve into the cutting-edge world of cloud security. With cloud computing dominating the digital landscape, safeguarding data and applications is non-negotiable. In this breakout, we'll explore a layered approach to fend off cyber threats and unauthorized access. Discover how to fortify public cloud environments using Cisco Multicloud Defense, securing the Ingress/egress and achieving robust segmentation between virtual networks. Elevate your cloud security with Cisco Secure Workload and embrace micro-segmentation strategies for comprehensive application protection. Immerse yourself in practical use cases and master the art of operating on a policy model for seamless defense. Don't miss this opportunity to enhance your cloud security knowledge and safeguard your organization's future. Register now for an empowering journey into cloud defense excellence.

### How to Combat Complexity and Enhance Security Visibility and Strengthen Attack Surface Management - VILENS-2001
Speakers: Tim Woods (FireMon)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271918770001zUGQ
The role of IT security is constantly evolving, especially in Today's hybrid enterprise environments.When reporting to the C-suite, it is essential to include not only how the company manages change visibility and complexity but also how it ensures the security policies that govern these systems are well-maintained and effective. Cybercriminals often exploit misconfigurations, human errors, and exposed vulnerabilities — issues that can arise from both unnecessary complexity and poor policy hygiene. These vulnerabilities often go unnoticed in complex, rapidly changing environments. In this presentation, we will discuss strategies to reduce complexity while enhancing security visibility, particularly through the lens of attack surface management. A critical aspect of managing the attack surface is maintaining clean and well-managed enforcement security policies. Real-time Life Cycle Management of network security policies help eliminate gaps in coverage, misconfigurations, and outdated controls that threat actors frequently target. By combining policy hygiene with automation and comprehensive change visibility, organizations can reduce the opportunity for exploitation and proactively secure their ever-expanding attack surface.

### How to Identify & Mitigate Cybersecurity Vulnerabilities with NVIDIA Blueprints - DEVNET-1299
Speakers: Hang Yu (NVIDIA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271894940001zkL4
This session will walk through the capabilities and application of the NVIDIA Blueprint for container vulnerability analysis using NVIDIA NIM microservices and the NVIDIA Morpheus cybersecurity AI framework.

### How to Prepare for the CCNP Enterprise Advanced Routing Concentration Certification - BRKCRT-2016
Speakers: Muhammad Aamir (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271835487001zZXH
Are you an Enterprise routing professional and considering pursuing CCNP Enterprise certification? Do you need a deeper understanding of the technical topics covered to prepare the Advanced Routing concentration exam? If you answered "Yes," this session is for you!

### How to Seamlessly Automate NX-OS and ACI Networks through Nexus Dashboard - BRKDCN-1615
Speakers: Max Alvarado (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271882683001zQoS
As the world evolves, technologies evolve as well. The more tools you have, the harder it becomes to maintain, operate, and troubleshoot LAN and SAN networks. In this session, learn how to achieve automation and observability for all with a practical approach. We will cover different use cases and provide demos to normalize how you provision, manage, and secure connectivity services across multiple sites and locations. By leveraging Nexus Dashboard and its services you can automate and operate network consistently.

### How to Setup a Nexus Hyperfabric from Scratch - BRKDCN-2907
Speakers: Ramses Smeyers (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271887512001zUx4
Imagine a fully functional Nexus Hyperfabric where virtual and physical workloads are happily communicating, where leafs are talking BGP and where everything is pretty. We are going to take that fabric and "write erase" it all before your very eyes. We will then rebuild it completely together step by step and bring it all back to its fully working state!

### How to Successfully Champion an IT Project - Learn the Language of Executive Decision Makers - BRKGEN-1008
Speakers: Patrick Bodin (WWT), Jerel Howell (Cisco), Tim Anderson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271946089001zXl6
Have you ever felt like you are speaking a different language than your leadership? Do you find it difficult to translate the importance of a budgetary request that has been declined? Would you like to learn how to document a technical need in such a way that it is understood by the non-technical executives who must approve your request? You are not alone! This session will equip you with the language and processes necessary for you to understand your relevance to the business and turn you into an IT Hero!! The knowledge you gain will elevate you from being a good engineer/architect to a valued IT Strategist. This session will include a bonus section from a guest speaker about the impact of AI on the landscape of IT, both from an architecture and leadership perspective, and what you should be doing now to remain relevant in the coming years.

### How to build AI agents for automating networking software development - AIHUB-1013
Speakers: Randy Zhang (Cisco), Shamin Aggarwal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912969001zPOQ
Agentic AI is the #1 on the top 10 tech trends in 2025 according to Gartner. Through AI agents, we can construct an autonomous system to perform complex tasks and make decisions with little human interventions. A great application of such a system is automating networking software development. In this talk we will provide a gentle introduction to AI agents and share practical details how to build AI agents for developing an enterprise grade software project. The talk is based on a white paper of a similar topic (https://medium.com/@randyhzhang/building-ai-agents-to-automate-enterprise-level-software-development-a-practical-perspective-cef0c40d80e7). We will cover agent framework and model selection, handling token limits, tool calls and other topics. Attendees will walk away with a clear understanding of agentic AI and how to start and optimize an agent based project to better meet their software development requirements.

### How to get the most from your fiber network ? - BRKMSI-2006
Speakers: Sushin Suresan Adackaconam (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271962879001ztED
This session aims to keep you up to date with what is new in the optical fiber industry. The following topics will be discussed: New types of fiber and why we need them ? Options to buy capacity today between Waves, Spectrum, Dark Fiber and Managed Optical Fiber Network (MOFN). How this is evolving with Pluggable Coherent Optics. Monitoring and sensing fiber infrastructure Quantum Networking and how fiber is important

### How to improve digital channels customer interactions with video - DEVNET-2701
Speakers: Victor Vazquez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271906554001zJUl
Organizations across all industries are seeking to enhance customer service with a growing demand for video communications with experts. In cases where the end customer is involved, it is crucial that the solutions are user-friendly and allow for the utilization of their preferred digital channel. We invite you to join us in this session to discover the key SDK features and programmable capabilities of Webex Instant Connect, and to gain insights on how you can seamlessly integrate video conversations into your digital channels using our low-code Webex Connect (CPaaS) platform.

### How we make TAC Engineers Super-Human - AIHUB-2014
Speakers: David White (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272013947001zj0B
Cisco's TAC engineers are the best in the industry - not just because of the knowledge they possess, but also from the tools they leverage. Come hear how we make our TAC engineers Super-Human by leveraging Generative AI models and data infusion to solve customer issues faster. Not only will you get a peek behind-the-scenes of HOW we do it, but you will also learn about the AI Assistants that Cisco exposes to our Customers and Partners - and how they can be used to make YOU super-human.

### Human, After All: The Future of Design + Research in Tech - PP-1310
Speakers: Travis Isaacs (Cisco), Kristin Harvey (Cisco), Cheryl Couris (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271947864001zPKX
In this era of advanced AI and automation, the value of a human-touch is unmistakable. Join Webex design leaders to learn how designing thoughtful, innovative experiences leads to better products, more satisfied customers, and a stronger, more skilled workforce. This session will focus on the everlasting role of humanity and creativity through real case studies and examples of how to deeply understand your customers and solve for their hardest problems — optimizing for unique human behaviors to win hearts, minds, and market share. Join us to explore how to leverage curiosity and a continuous commitment to learning from user behavior.

### Hybrid Mesh Firewall: Overcoming the limitations of traditional firewalling - PSOSEC-1026
Speakers: Chris Consolo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271995371001zgxr
As AI demands evolve, organizations are adopting a more holistic approach to firewalling across their hybrid enterprises. With threats becoming more sophisticated, applications growing increasingly complex, and management surpassing human scale, traditional firewalling methods are no longer enough. Discover how Cisco's Hybrid Mesh Firewall solution goes beyond conventional approaches, unifying environments and integrating fine-grained security controls to protect applications wherever they reside.

### Hypershield in a Nutshell: What it is and how it works - CISCOU-2059
Speakers: Dave Zacks (Cisco), Errol Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841579001z9k2
By now, you have almost certainly heard about Hypershield. However, have you wondered what makes it tick - the technologies like eBPF at it's foundation, and why these innovations are important for the future of security? If so, this is the session for you! In this session, we will explore the "inner workings" of Hypershield from the ground up. Attendees at this session will leave more informed not just about Hypershield, but how you can leverage these new innovations in your own network and app deployments. Presenting this session is the dynamic duo of Dave Zacks and Errol Roberts, both Distinguished Engineers as well as Cisco Live Distinguished Speakers. Come to this session to learn all about Hypershield and how you can use it!

### I didn't know ACI could do that! - Case Study with BEALLS and SHI - CNCDCN-2010
Speakers: Arthur Hilman (BEALL'S INC), Daniel Vargas (SHI International), Keith Starks (BEALL S INC)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271878620001zGQW
Update on recent changes with Cisco Data Center Fabrics covering new products and deployment modes, as well as an ACI Customer Case Study with BEALLS and SHI.

### IPv6 - What Do You Mean There Isn't a Broadcast? - BRKIPV-1616
Speakers: Fish Fishburne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271955149001zSXi
Super new to IPv6? Trying to wrap your ahead around the basics like how this all works without using broadcast and what the heck that "solicited-node multicast" thing is? If this describes you and your current knowledge of IPv6 and you want to try to "put the puzzle pieces together," then this session is definitely for you. This session dives into all this by bringing to life Fish's very popular seven-part blog series "Understanding IPv6" (https://networkingwithfish.com/understanding-ipv6-the-journey-begins/). By the end of this session, you will be able to better "see" how the underlying puzzle pieces fit together in order for two IPv6 addresses in the same subnet to be able to "talk" with each other without ARP.

### IPv6 Groove: Get By with a Little Help from My Friends! - CISCOU-1038
Speakers: Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271838319001zlqe
Join us for a 30-minute journey through the world of IPv6, set to the upbeat rhythm of The Beatles' classic, "HELP!" Discover how IPv6, the essential upgrade from IPv4, is like the friend you call on in times of need—addressing space exhaustion and enhancing network capabilities. We'll break down the core concepts of IPv6, such as its expanded address space, improved routing, and built-in security, using relatable analogies and a splash of musical flair. Whether you're a network pro or just curious, this session promises to educate and entertain, showcasing how IPv6 is the helping hand for the digital age.

### IPv6 Networking in a Cloud Native World - BRKIPV-2186
Speakers: Josh Halley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271955529001zF8k
Learn the best practices involved in optimising, scaling and maintaining IPv6 deployments in your micro services based environments, from on-prem to the cloud. This session will provide an overview of the key differences and nuances involved in IPv6 dual stack and single stack deployments, and how the environments can be best optimised to ensure are reliable and observable end-to-end architecture.

### IPv6 Security in the Local Area with First Hop Security - BRKENT-3002
Speakers: Eric Vyncke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271934956001zIll
A big difference in the security between IPv4 and IPv6 are the layer-2/layer-3 interactions, as DHCP is optional in IPv6 and ARP is replaced by Neighbor Discovery Protocol (NDP). Legacy IPv4 attacks such as ARP or DHCP spoofing have their equivalent in IPv6. Cisco has developed techniques for many years to secure this interaction in the local area (WLAN, LAN, SD-Access, Meraki, ACI, etc). This session explains the attacks and how Cisco can help protect your networks with short demonstrations. A good knowledge of IPv6 is required, especially NDP.

### IPv6-Enabled Wi-Fi Access: Design and Deployment Strategies - BRKEWN-2834
Speakers: Vinay Saini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271939444001zKmF
As networks transition to IPv6 and shift their services, careful planning, evaluation of services, and migration procedures are essential. Wi-Fi is the predominant access medium for a diverse range of client devices. Therefore it is crucial to design, configure, and comprehend the features and traffic patterns for both dual-stack and pure IPv6 Wi-Fi scenarios. This session focuses on understanding IPv6 communication flows and the various features of the Catalyst WLAN controller with IPv6. It will also discuss common design scenarios for Data and Guest IPv6 wireless, considering different client mixes including Apple iOS, Windows, and Android devices. Additionally, the session will explore IPv6 wireless in conjunction with Cisco SD-Access.

### IPv6: The Internet's Best Kept Secret - CTF-1400
Speakers: Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272019019001zHst
This presentation seeks to shed light on IPv6, often dubbed as the "Internet's Best Kept Secret". Despite being designed to replace the widely used IPv4 and address its limitations, IPv6 has experienced surprisingly low adoption rates. This presentation will explore the reasons for this paradox, focusing on the seamless functionality of IPv6 that often keeps its usage hidden from the end user.

### IPv6:: It's Happening! - BRKIPV-2191
Speakers: Nathan Sherrard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271955719001zv6v
IPv6 has had a long and winding history, with many organizations ignoring it. Yet in recent years its use has exploded, and we are now at a point where everyone needs to take it seriously and get ready for an IPv6-only future. If you're looking at the steps toward enabling IPv6, and are wondering where and how to start, this is the session for you. We will look at recent adoption trends and government mandates that are forcing the issue, do a walkthrough on the protocol itself, and finally explore some best practices around addressing plans and transition technologies. This session is targeted for enterprise, commercial, and public sector customers who are only just beginning their IPv6 adoption. We will not be discussing issues relating to service provider and mobile network providers. No IPv6 knowledge is required to attend, though basic familiarity with IPv4 networking is assumed. If you attended the TECIPV Technical Seminars, you do not need to attend this session.

### IR Migration Assurance: Simplifying Webex Calling Migration - VILOBS-2000
Speakers: Dave Murphy (IR)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271974661001zFbC
Migrating to Cisco Webex Calling can be complex, with risks of service disruptions, inefficiencies, and dissatisfied users. Join Cisco expert, Dave Murphy, from IR to learn how IR Migration Assurance eliminates these challenges by providing: Enhanced visibility: A real-time, unified view of your UC&C ecosystem across on-premises and cloud platforms. Detailed analysis: Granular insights into migrationprogress, user experience, and voice quality. Risk reduction: Predictive insights and actionable analytics to avoid delays and disruptions. Efficiency gains: Streamlined operations with data from legacy and new platforms in a single interface. Cost control: Optimized licensing to prevent unnecessary expenses. IR Migration Assurance equips businesses with the tools to manage their migration confidently, ensuring a seamless transition to Webex Calling while maintaining operational excellence.

### ISE APIs in Practice - Better Endpoint Profiling with Network Packet Analyzers - DEVNET-2292
Speakers: Taylor Cook (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271903051001zMDx
Do you struggle to identify endpoints in your network to apply your security policies? Do you have a problem with randomized MAC addresses or USB network adapters that obfusicate the device behind it? Or do you just want more data on devices you've only generically identified? Then this session is for you! Cisco ISE has long supported integrations with 3rd party systems to ingest additional contextual data for endpoints to enhance Network Access Control policy decisions. These integrations can be built using either ISE's Platform Exchange Grid (pxGrid) or the growing library of ISE OpenAPIs. This session will provide an overview of a free, open-source ISE integration built using packet analyzers to inspect network traffic and gain additional context for profiling endpoint devices. You will receive an overview of ISE APIs and existing publicly available toolsets, as well as learn how to use analyze live traffic across various protocols to learn more about devices on the network. This session will then showcase how to combine information learned from traffic analysis with the ISE platform to improve network policies. Participants are encouraged, but not required, to have a basic understanding of Python, REST APIs, Wireshark, and network packet structure (OSI model).

### ISE Automation: From Zero to Hero - DEVNET-2279
Speakers: Barry Yuan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271902861001zkWH
Are you ready to take your Cisco Identity Services Engine (ISE) management to the next level? Join us for an in-depth session on ISE automation through APIs, where you'll learn how to streamline, simplify, and secure your network access control and identity management processes. In this session, you'll discover how to: • Automate ISE administration to reduce manual effort and operational complexity • Enforce consistent security policies to improve compliance and mitigate risks • Quickly respond to security threats by integrating ISE automation into your security workflows Whether you're new to ISE automation or looking to refine your skills, this session will take you from zero to hero with real-world use cases and practical demos. Don't miss out — unlock the full potential of ISE automation today!

### ISE Deployment Improvements - Tips and Tricks - BRKSEC-2347
Speakers: Katherine McNamara (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009975001zLr2
Are you preparing for your first ISE deployment? Have you inherited an ISE deployment? This session focuses on giving best practices when it comes to the preparation, deployment, maintenance, and optimization considerations a customer should think about to ensure a successful ISE deployment. Like any technology, its easy to over complicate it over time so my hope to educate you the tips and tricks that will make your ISE deployment easier to manage. We will examine how to avoid some of the common pitfalls that I commonly see people fall into with their ISE deployments and "cheats" to make it easier. The session will also include common design pitfalls to avoid when planning out how ISE will be deployed using real world examples and how to lower the administrative overhead of an ISE deployment. At the end of the session, attendees can expect to have a better understanding of how to prepare their environment and their staff for an ISE deployment. This session is targeted at Network and Security Engineers, who are tasked in deploying or managing ISE.

### ISE Your Meraki Network with Group Based Adaptive Policy - BRKSEC-2100
Speakers: Alex Burger (Cisco), Thomas Howard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272007052001zyd8
Learn the latest about how you can better protect your network with the latest developments in software-defined segmentation capabilities from Cisco Identity Services Engine (ISE) and your Cisco Meraki network. Meraki wired and wireless devices have had Adaptive Policy capabilities for several years but it was difficult to synchronize with the TrustSec/Software Defined Access (SDA) tags and security group ACLs defined in ISE until now. We will show you how to configure your various Meraki network devices with Adaptive Policy, synchronize the TrustSec Matrix in ISE to the Meraki Dashboard, and authenticate your Meraki networks with ISE.

### Identity Based Attacks, a Red Team/Blue Team Experience - BRKSEC-2164
Speakers: Nic Conroy (Cisco), Ned Zaldivar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272008040001ztQn
In this session, we will showcase the concept of Identity Based Attacks starting with a red teaming demo leveraging various tools, techniques and tactics in order to effectively demonstrate how Identity based attacks are some of the most prevalent attacks in Today's Security Landscape. We will then move to showcase the blue team perspective and leverage tools in order to show alerts, policies, procedures and hands on cyber operational techniques which reduce or mitigate risk towards identity-based attacks. This session will showcase Cisco Duo, Identity Intelligence, XDR ITDR, and other Cisco Tools.

### Identity Intelligence Demystified - BRKSEC-2162
Speakers: Aaron Woland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272007848001zKlI
"Why hack in when I can log in?" The market is abuzz with the talk of Cisco Identity Intelligence (CII), which comes to Cisco via the acquisition of Oort. What is identity security all about? What types of attacks and risks are we seeing in the wild? What we see in the real world has shown us that organizations have more than one Identity Providers (IdP) like Okta, Micrsoft EntraID and Duo SSO, but the security team isn't getting a complete or holistic view across the different IdPs. Come join Distinguished Engineer, Aaron Woland, as he talks all about identity threats and Cisco Identity Intelligence. How it is part of Cisco XDR and Duo Security, integrations, how it relates to the Identity Services Engine (ISE) and most importantly how to improve your Security Posture by getting a hold of the identity related threats.

### Identity Under Siege: Strategies for Today's Threats - BRKSEC-2880
Speakers: Andy Winiarski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272011764001zLey
Identity-based threats are all the rage!! No matter which threat summary or breach report you read, identity is involved in approximately 80% of the attacks. From straightforward account take-overs, cookie theft, and session hijacking to on-prem attacks like Kerberoasting; the number of tactics to consider and mitigate continue to multiply. This session will provide an in-depth exploration of the current identity threat landscape, highlighting recent high-profile breaches and the sophisticated attack techniques employed by adversaries. The session will also emphasize the significance of identity protection and hygiene, detailing best practices for maintaining secure identities and minimizing vulnerabilities. Furthermore, we will discuss advanced threat detection strategies that enable organizations to swiftly identify and respond to potential identity threats before they escalate. We will look at open standards and frameworks coming down the road that will enable security platforms and organizations to react more quickly and effectively to threat signals in identity. Join us to learn how to effectively safeguard your organization's identities against today's complex threat landscape, leveraging cutting-edge solutions and expert guidance.

### If You Don't Have a Security Reference Architecture, You Must Get One! - BRKSEC-1240
Speakers: Jerry Lin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271998573001z0Hg
This breakout session will explain Cisco's latest security reference architecture covering the most common solutions that customers are deploying. Solutions such as Zero Trust, Secure Access Service Edge(SASE), Compliance, Security Operations with eXtended Detection & Response(XDR), Vulnerability Management, third party non-Cisco integrations, and others will be explained in terms of customer use cases. Demos of these covered solutions will be shown to highlight each outcome. Attendees should walk away from this session understanding how the Cisco Security Reference Architecture can help them or even identify any potential gaps in their existing environment, even if they have a mixed vendor environment today.

### Impact of AI Traffic in Transport Networks - BRKSPG-1180
Speakers: Virginia Teixeira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963873001z5j7
Artificial Intelligence (AI) is set to revolutionize every industry and the way users interact with the digital world. It's still early phases of AI adoption and still unclear what are the deployment models and AI technics that will become more prevalent. However, it's already apparent that AI traffic patterns are different from traditional internet traffic and that the use of AI frameworks such as RAG (Retrieval-Augmented Generation), grounding, AI agents and AI distribution to the edge, will have an impact on transport network design considerations. This session includes an analysis of the AI traffic characteristics for a set of AI use cases, and their impact on WAN and DCI design requirements.

### Implementing OAuth 2.0 Authorization for Webex Integrations - DEVNET-2675
Speakers: Joe Zanini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271906362001zx3E
OAuth is a powerful way to allow users to grant permission over their accounts to third parties. Join the Webex Developer Evangelism team for a walk-through of how to create an OAuth flow so your Webex Integrations users can authorize your app to run on their accounts or simply authenticate with Login with Webex.

### Implementing and Troubleshooting AI Data Centre Networking Infrastructure - BRKTRS-2006
Speakers: Kapil Mehta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271936135001ziky
Implementing and operating AI data centres are the key challenges for the industry. In this session, you will learn about a high-level overview of various types of AI/ML data centre networking infrastructure solutions and gain a deep understanding of implementing and troubleshooting them, with visibility of AI workloads implementing via the Nexus Dashboard.

### Increase Your Networking Insights with Splunk Platform and Intelligent Data Fabric - BRKOBS-1020
Speakers: Hanlin Fang (Cisco), Nisarg Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271979339001zZ9o
Ever wondered how you can get better insights into your networking data? Splunk can help. What can you do better with Meraki, Nexus, Catalyst and Arista data? Learn about the new set of gold standard technical add-ons (TAs) simplifying the integration of Cisco Networking and Splunk, and networking apps available in Splunkbase. Get a glimpse of the future of Splunk intelligent data fabric and see how you can drive better insights into networking and operational technology (OT) data via Splunk, without learning SPL.

### Industry Standard Streaming Telemetry with Cisco NX-OS - DEVNET-2235
Speakers: Gerard Sheehan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271901912001z6GD
Come and learn about the latest way to monitor the health of devices and activity in your network: Streaming Telemetry. See how simple it is to deploy in NX-OS and integrate with Open Source solutions to consume and visualize the data. Also watch how anomalies can generate alerts, and how the data can be integrated with messaging buses and AI/ML applications!!

### Infrastructure as Code (IaC) for Dummies (or How I learned to love automation and programmability) - DEVNET-2297
Speakers: Matt DeNapoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271903239001z3VO
In this session, Matt (the dummy) will share his lengthy experience in DevNet with automation and programmability of Cisco platforms. Ansible, Terraform, and Python oh my! Part story telling, part practical application, he will dig into all of the pertinent experiences he's gone through and some of the pitfalls and successes he's seen. In addition, Matt will call out areas where the dummies like him don't need to worry about EXACTLY how things work, but also where it is helpful to pull back the curtain a bit. When attendees leave this session, hopefully they will be on their way to not being dummies (if they even were), but at minimum they will have had a good 45 mins of thinking —if this dummy can get this stuff to work then so can!

### Infrastructure as Code for NXOS and NDFC with Ansible - BRKDCN-2946
Speakers: Matt Tarkington (Cisco), Mike Wiebe (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889990001zVHq
In this session, we'll explore how Ansible and NXOS can be used to provide various automation and orchestration capabilities to operate your VXLAN EVPN data center fabric using Infrastructure of Code (IaC) principles. Ansible is widely adopted and used across the industry as a foundation for IaC, which uses established best practices for software development and applies them to your network. Network configuration is stored in a structured manner using a source control management system like GitLab and becomes the source of truth for making network changes. In the session, we will walk through getting started with a development environment for Ansible and the Ansible NXOS collection. Next, we will define an Ansible playbook structure using available NXOS modules. We will then show you how you can store your Ansible playbook(s) in GitLab as a source of truth and build a CI/CD pipeline to push network configuration changes. The focus will then transition into how you use the same Ansible environment and IaC concepts to manage your VXLAN EVPN fabric using Nexus Dashboard Fabric Controller (NDFC) and corresponding Ansible collection. NDFC is the management controller for all NXOS-enabled deployments and offers a robust northbound-REST API for Ansible modules to leverage. Finally, we will build upon our GitLab CI/CD pipeline to make network changes to our NDFC-managed fabric.

### Infrastructure as Code for Network Operations: An Executive's Guide for Achieving 100% Change Success - ITLGEN-2051
Speakers: Jesse Reed (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271956283001z0kK
To stay competitive, businesses need rapid transformation without risking service disruption. Humans are the leading cause of network-related service interruptions. Infrastructure as Code (IaC), using open-source principles and Cisco best practices, can modernize and automate network operations. Many teams already use IaC for cloud, but network operations still rely on legacy methods. This session will explore achieving change five times faster by integrating IaC and AI into your network operations. Learn how Cisco has implemented IaC, and digitized the continual knowledge of 20k Cisco engineers to ensure 100% change success. All IT leaders are encouraged to attend.

### Infrastructure as Code with AI: The Foundation for AIOps - PSOCX-1020
Speakers: Jesse Reed (Cisco), Michael Kaemper (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272014728001z1We
In today's world, where artificial intelligence is placing unprecedented demands on your network, security, and data center, IT must achieve new levels of availability and performance. This session invites you to explore how industry leaders are harnessing the power of AIOps and infrastructure-as-code methodologies to achieve digital resilience and proactively implement changes five times (5X) faster, achieving a remarkable success rate of over 98%+. Discover how you can utilize DevOps strategies combined with AI to streamline your operations, design, deployment, testing, and change processes, positioning your organization at the forefront of technological advancement.?

### Infrastructure for Agentic AI: Architecting Scalable Secure Multi-Model Systems - BRKCOM-1126
Speakers: Brian Shlisky (Cisco), John Cuneo (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271859493001zbtZ
Interest in Agentic AI architectures has surged as organizations explore how these advanced systems can transform business processes and interactions. Agentic AI refers to a type of AI design where multiple autonomous agent models work together and communicate to achieve complex goals. These architectures enable dynamic problem-solving, task delegation, and adaptive learning by mimicking human-like decision-making across various tasks. This session will focus on the practical implementation of Agentic AI architectures using an 8-GPU server, showcasing how multiple agent models can seamlessly converse and collaborate within a high-performing environment. Attendees will learn how to maximize GPU resources for training and inferencing workloads while maintaining the flexibility to run diverse agent interactions simultaneously. The dense GPU server architecture provides the computational power necessary for supporting the resource-intensive demands of agentic AI, enabling real-time decision-making, large-scale model deployments, and seamless orchestration across tasks. . A key focus will be on Cisco's AI Defense capabilities, designed to secure communications between models within an Agentic AI framework. AI Defense ensures that sensitive interactions and decision-making processes remain protected from external threats or breaches. Fosters trust and reliability, enabling businesses to scale their AI operations with confidence. By leveraging scalable, easy-to-manage infrastructure, advanced GPU servers, and secure communication protocols, businesses can unlock the full potential of AI, delivering powerful agent interactions while ensuring efficiency, data security, and operational control. Participants will leave equipped with strategies to embrace the exciting opportunities of Agentic AI while staying aligned with their organizational goals.

### Infrastructure for the Next Ten Years - CNCCLD-2004
Speakers: Dan Ciruli (Nutanix, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271844810001zwJm
The technology landscape for infrastructure is changing faster than ever. The move from VM-based deployments to cloud native, Kubernetes deployments has changed how software and infrastructure get deployed. The rapid ascent of AI has had major impacts on what the hardware in the data center looks like. And the mere existence of the Cloud has changed what developers and operators expect out of infrastructure. In this session you'll hear how you can ensure that your data center is ready to meet those challenges as you define the infrastructure for the next ten years.

### Innovating with Webex for Developers - CISCOU-1033
Speakers: Phil Bellanti (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271838134001zYlq
Discover the art of the possible in this introductory session as we explore Webex APIs, integrations, and bots. We will showcase how these developer tools can enhance collaboration by unlocking new opportunities and efficiencies in Webex Meetings, Calling, and Messaging. Attendees will learn through inspiring examples across different industry verticals and gain insights into applying these technologies to drive innovation within their organizations.

### Innovations in Silicon and Software: Defining the Next Generation of Enterprise Technology - BRKARC-2093
Speakers: Dave Zacks (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271917809001zEmD
Ever wonder what's "under the covers" in Cisco platform architecture? Come to this session to explore what's next in Cisco's Enterprise product portfolio, exploring the latest advances in silicon hardware, modular software, and end-to-end solutions. This session will examine the current state-of-the-art in ASIC, platform, and software design, and examine the many use cases to which Cisco networking and security technologies are being applied. Presenting this session is the dynamic duo of Peter Jones and Dave Zacks, both Cisco Distinguished Engineers as well as Cisco Live Distinguished speakers. If you are interested in what makes Cisco products and platforms "tick," this is the session for you!

### Innovations on Cisco Campus Switching for Sustainability and Energy Management - BRKENS-2099
Speakers: Veera Bhaskar Mutyala (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271920676001zgt5
This session covers Catalyst 9K Switching innovations for sustainability, focusing on energy efficiency and regulatory compliances. Topics include new power savings features, 90-watt PoE, DC microgrid designs, and smart building capabilities. Through IOS-XE and Catalyst Center, we'll demonstrate how analytics and automation support ESG goals, energy savings, and improved reporting.

### Innovative Authentication: Beyond Passwords - BRKSEC-2584
Speakers: Stefan Duernberger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010780001zHEa
In today's fast-changing digital world, keeping user authentication secure is essential. In this session, we will delve into the role of passkeys in enhancing authentication security, focusing on their implementation and benefits. We will then explore OAuth 2.0 and OIDC, examining how these protocols facilitate secure and seamless user authentication across platforms. Attendees will gain insights into Google Device-Bound Session Credentials (DBSC) and Cisco Duo Passport, highlighting their innovative approaches to identity security. Finally, we will conclude with an overview of Shared Signals and Events, emphasizing their importance in maintaining a secure and responsive authentication environment. This session is ideal for Security Architects and Administrators aiming to deepen their understanding of modern authentication methods and their application in a Zero Trust architecture.

### Inside DevNet: See How We Built AI Agents So You Can Do It Too - DEVNET-2322
Speakers: Cody Kai Hartsook (Cisco), John Parello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904019001zOcG
Join John Parello, Principal Engineer of AI Strategy and Hall of Fame Speaker Cody Hartsook, Software Engineer of AI Strategy, How do developer advocates build and use AI Agents for themselves!? In this We'll go through our journey in agent-building at DevNet.This session gives developers and the community an inside look at how DevNet uses its own resources to create and roll out agents. These innovations help streamline operations and make building new agents easier. In this engaging session, you'll discover the types of agents we've developed, learn about the potential for reusing these agents, and explore the specific SDKs. We'll introduce you to our internally developed tools, crafted for model selection, agent creation, and agent-agent communication. Additionally, we'll demonstrate how OpenTelemetry is integrated for comprehensive monitoring and how we're working with the AGNTCY open source collective

### Inside the AI-Ready Secure Network: Powering the Future-Proofed Workplace - KDDENT-1000
Speakers: Lee Peterson (Cisco), Lawrence Huang (Cisco), Austin Lin (Cisco), Lizzie Parker (Cisco), Nick Edwards (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591952188001pdO6
AI is fundamentally changing the dynamics of campus and branch networking-driving explosive growth in traffic, with new AI agents doing human-like work, but operating at machine speed and scale. At the same time, new requirements for collaboration and customer experience are pushing today's architectures to their breaking point. Networks designed for yesterday's environments can no longer meet the performance, security, or operational demands of an AI-driven enterprise. In this technical deep dive, Cisco will showcase a new architecture designed for the AI-Ready Secure Network-engineered from the ground up to support the scale, speed, and complexity of modern AI workloads. Learn how purpose-built, low-latency, high-throughput wireless, smart switching, and secure routing can deliver performance and protection at scale. Beyond these powerful new products, Cisco leaders will also showcase live demos of new automation and operational simplicity, powered by AI across every domain. Don't miss this opportunity to see live how Cisco is re-engineering the enterprise network for the AI era-purpose-built, proven, and ready for what's next.

### Installation Considerations for Modern High-Performance Networks - CNCOPT-1001
Speakers: Corey Lacaire (Legrand)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271990545001z4ym
Historically, applications have used only part of the performance bandwidth available. Because of this, and the fact that standards are not enforceable by law like codes, there is a growing mindset that "standards are only guidelines and best practices" that can be implemented when convenient. With data center center speeds racing toward 1.2 Tbps and beyond, optical budgets are shrinking. This panel of industry experts will discuss the implications of common installation shortcuts on modern applications including PoE, smart buildings, and high-speed fiber optic systems. By understanding these issues, we can ensure the integrity of the system through proper installation processes.

### Integrating Webex Contact Center Agent Functionality into Web Applications with the WxCC SDK - DEVNET-2082
Speakers: Arun Ganeshan (Cisco), Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899610001zNXq
As the demand for efficient and customizable contact center solutions grows, the Webex Contact Center Agent SDK provides developers with powerful tools to enhance their web applications. This session will introduce you to the SDK's capabilities, allowing for the creation of lightweight and customizable widgets that seamlessly integrate with existing systems. you'll leave this session with ideas to help you build efficient custom widgets, integrate WxCC into existing applications more effectively, and leverage the SDK's flexibility to meet business needs. This session is designed for developers with a basic understanding of web application development. Join us to discover how the WxCC Agent SDK can transform your integration strategies and enhance your application's capabilities.

### Intelligent Network Observability at Scale with Cisco AI and Automation - BRKATO-2003
Speakers: Fany Vargas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271832089001zdPe
Modern networks require advanced observability to maintain performance and uptime. This session explores how Cisco's AI-driven automation and observability solutions provide deep insights into network and application performance at scale. Learn how Cisco customers use these tools to automate root cause analysis, optimize user experiences, and enhance operational efficiency. Attendees will gain practical knowledge on implementing intelligent observability workflows that deliver actionable insights across large and complex networks. Session modules: 1. Observability Challenges in Modern Networks? 2. Observability Measurements? 3. Scalable Observability Architectures? 4. Automation for Observability? 5. Demo: Cisco AI-Powered Observability? 6. Demo: Transform Network Observability with AIOps? ?

### Internet Peering Design and Deployment - BRKMSI-2005
Speakers: Phil Bedard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271962684001zCAB
The founding of the Internet over 50 years ago was driven by a need for network interconnection. Today all institutions with connectivity to the Internet are doing so through peering and interconnection. Internet peering today includes connectivity to CDNs, public cloud, SaaS providers along with the traditional bi-lateral peering to other enterprises and transit. This session will present the most important trends in peering today covering traffic distribution, security, peering automation, and peering optimization. The best practices presented can then be applied to how enterprises and service providers deploy their peering and interconnect networks.

### Intersight Fundamentals: Private Cloud Infrastructure from a Field Engineer Viewpoint - BRKCLD-1666
Speakers: Justin Blinn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845756001zXG6
The Cisco Intersight platform offers a cloud operating model which enables faster delivery, streamlined operations, and ongoing optimization of infrastructure. This platform manages on-premises Cisco Unified Computing System (UCS), hyperconverged (HCI) clusters and third-party infrastructure. In this fundamentals session, participants will gain an understanding of the Intersight platform's components and capabilities, how it securely interfaces to its platform targets, and the business value outcomes it can provide. Real-world use cases of the Intersight platform will be discussed and demonstrated, making this an interactive session. By the end of the session, participants will have an understanding of the Intersight architecture, the components of the operating model along with use cases and scenarios that can be addressed with Intersight operations.

### Intersight Monitoring and Metrics: Bringing enhanced visibility to infrastructure - BRKCOM-2033
Speakers: Eugene Minchenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271860253001z6W4
As the complexity of modern datacenters increases, the challenges of troubleshooting and gaining a clear understanding of your infrastructure become more demanding. Join us for an insightful session where we leverage Cisco Intersight's advanced monitoring capabilities to gain real-time visibility into our servers' operations, and retrospectively analyze past events to uncover critical insights. Have you ever wondered how much energy your servers are consuming? Need to assess if additional capacity is necessary? Curious about potential network issues affecting performance? We will address these questions and more, equipping infrastructure and operations (I&O) managers with the knowledge to meet aggressive Service Level Objectives (SLOs) and Service Level Agreements (SLAs). Intersight Monitoring has undergone significant advancements over the past year, introducing a range of new features designed to further simplify your daily operations such as anomaly detection, forecast and threshold alerts. We'll provide a concise overview of existing monitoring functionalities before delving into the latest enhancements. Our session will not only demonstrate how these features operate but also guide you through the setup process, ensuring you can optimize them for your specific environment. Join us to unlock the full potential of Intersight Monitoring and transform the way you manage your datacenter's performance and efficiency.

### Intersight Unlocked: Strategies and best practices to get the most out of Intersight - BRKCOM-2116
Speakers: Chris Gascoigne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271860630001zXIp
Cisco Intersight is an extremely powerful infrastructure operations platform that is used by many organisations today. However, most users are only scratching the surface of what they can do with Intersight. In this session, participants will learn strategies and techniques they can use to get more out of their Intersight investment by leveraging integrations, automation, orchestration and no-code API interfaces to improve their operational processes.

### Introducing the Cisco Telemetry Broker (CTB) - DEVNET-2340
Speakers: Ajit Thyagarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904610001zhj2
The Cisco Telemetry Broker optimizes your telemetry pipelines for the hybrid cloud. It vastly simplifies the consumption of telemetry data for our customers' business critical tools by brokering hybrid cloud data, filtering unneeded data, and transforming data to a usable format for optimal consumption by the various analytics tools. In this Lab, the participant will learn how to set up the Cisco Telemetry Broker to route telemetry in multiple formats from example sources to multiple destinations and track the end-to-end flow of telemetry through the Telemetry Broker.

### Introduction to ACI - BRKDCN-1601
Speakers: Chris Merkel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271882294001zRaY
Not sure what Cisco ACI is? Looking for a starter session to understand the architecture, nomenclature and capabilities of ACI? How it can transform your data center? Join this session to get a crash course in ACI!

### Introduction to AI Infrastructure - CISCOU-1058
Speakers: Chris Gascoigne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840264001zq2T
The AI hype is real today and there is lots of discussion around AI infrastructure speeds and feeds, but have you ever wondered "Why? What is it about AI workloads that needs high powered GPUs, 400/800G networking and scale-up interconnects?" If so, join this session to learn about the fundamentals of AI training and inferencing and why (and in what circumstances) they have different infrastructure requirements than traditional applications.

### Introduction to Campus Network Design and Multilayer Architectures - BRKENS-1500
Speakers: Jakub Matela (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271922617001z9aI
Understanding how to design a campus network that is scalable, reliable, and aligned with modern needs is a critical skill for Today's network professionals. In this session, We'll introduce the core concepts of multilayer campus architecture and show you how to design and plan your network using the best practices outlined in Cisco Validated Designs (CVD). Whether you're working with small or large networks, this session will guide you through: • The key building blocks of a multilayer campus network. • How to choose the right design model for your needs. • Practical tips to get the most from CVD recommendations. This session is perfect for those with a solid understanding of LAN switching and routing basics (CCNA-level) and provides a strong foundation for exploring more advanced topics. Start here to learn the fundamentals, gain practical design insights, and prepare to optimize your campus networks for the future For those ready to take the next step, BRKENS-2500: Advanced Campus Network Design: Multilayer Architectures and Next-Gen Protocols, builds on this knowledge to dive deeper into advanced protocols, design strategies, and next-gen integrations.

### Introduction to Infrastructure as Code for ACI using Ansible - BRKDCN-2606
Speakers: Thomas Renzy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271883494001zoV3
Infrastructure as code (IaC) allows you to define via data structures, the configuration of your network. Ansible has become an industry standard automation tool used to manage large scale compute stacks and network devices. Cisco Application Centric Infrastructure (ACI) is Cisco's premier API-based data center network architecture with 100% API coverage. The combination of these, allows you to operationalize your network with security , accuracy and speed . In this session we will cover: Best practices to setup Ansible for ACI operations How best to organize your data structures to allow for growth and reaching infrastructure as code state Pitfalls to avoid from lessons learned working with Ansible and large data-sets

### Introduction to Infrastructure as Code for ACI using Terraform - BRKDCN-2607
Speakers: Jorge Gomez Velasquez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271883684001zthW
Infrastructure as code (IaC) allows you to define via data structures, the configuration of your network. Terraform has become a standard in the cloud to manage large scale deployments of many different type of resources. Cisco Application Centric Infrastructure (ACI) is Cisco's premier API-based data center network architecture with 100% API coverage. With the Terraform and ACI automation capabilities in Terraform you can configure ACI easily in a fashion that can lead to secure, accurate and fast configuration changes. In this session we will cover: Best practices to setup Terraform for ACI operations Understand the different ACI specific Terraform resources available Pitfalls to avoid from lessons learned working with Terraform and some of it's unique powerful toolsets.

### Introduction to NDFC: Simplifying Management of Your Data Center - BRKDCN-1619
Speakers: Pavan Jaya (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271882874001zs33
Cisco Nexus Dashboard Fabric Controller (NDFC), formerly known as Data Center Network Manager (DCNM), is the network management platform for all NX-OS (Nexus switching)-enabled deployments, spanning EVPN-VXLAN single and multi-site fabrics, classic LAN architectures, IP fabric for media, storage networking deployments, and our newly AI/ML networks for the Cisco Nexus-powered data center. This session will serve as an introduction to NDFC, providing an overview of the product while highlighting the main features of the latest NDFC 12 release. With the upcoming Nexus Dashboard 4.x release, NDFC becomes an integral part of Unified Nexus Dashboard. No more separate applications. In this session, we will briefly look at Nexus Dashboard, NDFC installation, and various deployment options with ND. We will then move on to LAN fabric mode for VXLAN EVPN and classic LAN fabric. The focus will be on best practice template-based provisioning capabilities with built-in configuration compliance and the myriad deployment scenarios. We will also walk through Day 2 features like compute visibility using virtual machine manager (VMM) integration, the switch dashboard, and real-time topology search. No prior knowledge of NDFC is required.

### Introduction to Nornir: Pythonic Network Automation - CISCOU-1056
Speakers: Jason Belk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271839884001z0bm
Discover how Nornir, a powerful, pluggable, multi-threaded Python automation framework with built-in inventory management, helps network engineers efficiently operate collections of devices. Using pure Python instead of domain-specific languages (such as Ansible's YAML-based modules) simplifies automation, improves troubleshooting, and integrates easily with existing tools and libraries, streamlining your network automation journey. Attend this session to start leveraging Nornir for more maintainable and scalable network automation.

### Introduction to SRv6 uSID Technology - BRKMPL-2203
Speakers: Jakub Horn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966207001zvJ6
This session will provide an overview of the SRv6 uSID technology and use cases. The session will demonstrate the application of SRv6 uSID building blocks on real use cases like L3 VPN, Flexible Algorithm, and traffic engineering.

### Introduction to Segment Routing and SRv6 - BRKMPL-1207
Speakers: Leonir Hoxha (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271960957001zGfF
Multiprotocol Label Switching (MPLS) has been the backbone of scalable and efficient networks for decades. However, its reliance on maintaining per-flow state in the network core limits scalability and increases operational complexity. Segment Routing (SR) revolutionizes MPLS by encoding path information into segment identifiers (SIDs) directly within the packet headers, removing the need for complex signaling protocols like LDP or RSVP-TE. This introduction level session delves into how SR extends and enhances MPLS, providing simplified operations, improved scalability, and seamless integration with traffic engineering paradigms. Taking these innovations further, SRv6 integrates the principles of SR into IPv6, utilizing its abundant address space and native extensibility to enable advanced use cases such as network slicing, application-aware routing, and service chaining. Attendees will explore the underlying mechanics of SID encoding, segment routing policies, and SRv6 network programming. This session provides technical insights and the fundamental building blocks of SR and SRv6. Attendees new to SR and SRv6 technology are the target audience.

### Introduction to VXLAN: The Future Path of Your Data Center - BRKDCN-1621
Speakers: Richard Licon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271883070001zRMQ
Learn more about VXLAN and delve deeper into it. This session will cover what VXLAN is, how it works and the problems it solves. The need for flexibility in the data center opens the door to network overlays. Several standards have been proposed and implemented to enable virtualized networks to be layered over a physical network. The data center network needs to be flexible enough to support workloads that can move from one host to another, and for new services to be deployed rapidly. VXLAN is one such technology that provides massively scalable virtual network overlays on top of existing IP infrastructures. This session will include 101s and packet walks as we cover the insides of VXLAN. No prior knowledge of VXLAN is required. A basic understanding of unicast and multicast routing protcol is needed, along with an understanding of MP BGP.

### Investment Protection with Catalyst 9000 Series Switching & Wireless: A Competitive Edge - BRKARC-1012
Speakers: Meghan Kachhi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271916435001znL9
Constant hardware refreshes every few years and struggling to keep up with campus networking trends are draining resources and hindering innovation. Join this session to understand how Catalyst 9000 Series switching and wireless solution provide unparalleled investment protection. Discover how Catalyst 9000's innovative design, modularity, and architectural flexibility enables you to adapt to evolving business needs without costly overhauls. Explore how future proofing is powered from ASIC, fixed/modular platforms, architecture, high availability and all the way to flexible management options. Key takeaways: - Understanding the value proposition of Catalyst 9000 for investment protection - Learning how to adapt to newer trends & technologies - Discovering strategies for keeping your business highly available and managing it flexibly With this interactive session, we can have discussion on how Catalyst 9000 switching and wireless safeguards your investment compared to the competitive offerings out there.

### Is VPN really dead and replaced by Zero Trust Network Access (ZTNA)? - BRKSEC-1015
Speakers: Gustavo Medina (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271997760001zWYg
Join us for an insightful 60-minute breakout session where we will explore the differences between traditional Virtual Private Networks (VPN) and Zero Trust Network Access (ZTNA) solutions. While some may claim that VPNs are obsolete, we believe that each technology has its strengths and weaknesses. In this session, we'll provide a comprehensive comparison of VPN and ZTNA and help you understand how each approach can be leveraged to achieve a secure architecture based on Zero Trust principles. We'll also highlight real-world use cases to help you make an informed decision about which solution is right for your organization. Don't miss out on this opportunity to gain new insights into the world of cybersecurity and learn how to integrate the latest security technologies into your infrastructure.

### It's Cats vs Rats Going Hybrid! Attack and Defense in the Cloud - BRKSEC-2485
Speakers: Hakan Nohre (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010588001z4J6
Cyber security is a cat and mouse game - a constant evolution of new ways to attack and defend. The cloud transformation may bring many benefits, such as reduced cost and increased agility, but it also increases the attack surface for determined adversaries. New technologies including - AI technologies - can be used by both sides. In this breakout we will look at the new possibilities to attack and defend. The intended audience are Security and Networking Architects. Some understanding of cloud concepts such as IaaS and PaaS is expected.

### It's not shocking to learn about FMP - CTF-1044
Speakers: Ross Sweetzir (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271919320001z4Fa
Get ready to electrify your network! In this session, We'll explore how Panduit's Fault Managed Power (FMP) and Cisco Catalyst UPoE+ switches join forces to deliver power where you need it. With up to 90W per port, they'll power up your IoT devices, smart lighting, and more effortlessly. Say goodbye to power headaches and hello to lower cost power delivery, simplified setups, fault tolerant delivery, and next-level safe connectivity.

### It's your Data Center, you automate your way - DEVNET-1839
Speakers: Roma Bhansali (Cisco), Arun Arunkumar (Cisco), Venkat Krishnamurthy (Cisco), Sunil Gudurvalmiki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271897297001zts1
API is the new currency. Automation is the game in town. And we are here to help. Please join Cisco's engineering leaders to hear how they are building APIs to help Nexus customers automate their data center networks. The panelists will discuss the APIs and abstractions at Nexus switch layer, APIC and Nexus Dashboard controller layer and integrations into frameworks like Ansible and Terraform. You will also learn about the engineering philosophy about the APIs and how engineering processes have evolved to an API first approach to produce world class APIs.

### Itau Unibanco Bank Assures Digital Resilience with ThousandEyes - CSSOBS-1015
Speakers: Diego Turi de Oliveira (Ita? Unibanco), James Parnham (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271874700001zQm2
For the largest banking institution in Brazil, Itaú Unibanco, digital resilience is a critical factor in maintaining operations for its 70 million customers in more than a dozen countries. This includes assuring uptime across its global offices and even their operations in the Amazon. The partnership with Itaú and Cisco ThousandEyes has already resulted in a large MTTI reduction. ThousandEyes monitors Itaú's Webex collaboration suite integration, ITSM, banking partner connections, and more than 2800 remote branches to assure the highest level of user experience. Itaú has also integrated ThousandEyes into Splunk to further correlate business metrics. During this session, presented by Diego Turi, IT Manager for Itaú Unibanco, session attendees will learn about: • How Itaú is delivering an enhanced user experience with ThousandEyes • The benefits of monitoring Webex with ThousandEyes • How Splunk and ThousandEyes work together to illuminate key business metrics

### Jamf and Cisco: Integrated, Enterprise Solutions for Securing Apple Devices - VILSEC-1057
Speakers: Tim Knox (Jamf), Sam Weiss (Jamf), Aaron Woland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271992293001zygE
The way employees work has evolved, and they expect seamless user experiences with enhanced security across every device and connection. In this session, learn how Jamf and Cisco are partnering to help organizations succeed with Apple. We'll show how Jamf brings the best-in-class Apple user experience to enterprises leveraging Cisco's robust security stack, with a special focus on Cisco Secure Access, Cisco Duo, and Cisco XDR and Cisco ISE. Discover how our integrated solutions ensure secure, frictionless access for end users, and confidence for IT and Security teams. See how Jamf-managed Apple devices help enforce compliance with internal policies and regulatory frameworks, and how Cisco integrates with Jamf to ensure a positive end-user experience on Apple devices. Together, Jamf and Cisco enable secure, productive, and context-aware mobility. Together, Jamf and Cisco deliver the trusted Apple experience users expect, backed by Cisco-powered security teams need.

### Journey Data Services Unleashed: Proactive Customer Engagement with Webex Contact Center - BRKCCT-2689
Speakers: Tarek Ayadi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271864868001z0R4
Discover how Journey Data Services (JDS) transforms customer engagement by delivering a 360-degree view of the customer and enabling proactive, AI-powered interactions. This session explores how businesses can leverage JDS within Webex Contact Center to automate outbound campaigns, drive seamless omnichannel experiences, and empower agents to take real, authorized actions. Learn how data-driven insights fuel smarter customer journeys and unlock new possibilities in AI-driven customer experience.

### Keeping Up on Network Security with Cisco Secure Firewall - BRKSEC-2236
Speakers: Nicholas Carrieri (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272009009001z0If
The network security death rumors are highly exaggerated, and Cisco Secure Firewall is the best proof of all. Whether you are an experienced Firepower aficionado, or someone who is open to trying something new, this session will get you the fix. From app security, to blazing-fast new hardware platforms, to maintaining visibility in the world of pervasive TLS encryption, there is something for everyone to get at least a little excited about.

### Keeping Up with Zero Trust - BRKSEC-2176
Speakers: Jerry Lin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272008617001ztQg
Enforcing Zero Trust least privilege access has failed to delivered a simple user experience. Come see the updated Zero Trust requirements that will help you get Zero Trust back on track. This session will cover the top most commonly deployed use cases (i.e. ZTNA) that spans from user to workload/data/application(north-south traffic) and workload/data/application to workload/data/application (east-west traffic). Demos of each use case showing the user access experience and the administrator's experience will be provided. Attendees will walk away understanding that the Zero Trust journey must include holistic access policies that span end-to-end.

### Keynote: Innovation in Action - KEYGEN-1002
Speakers: Patrick Milligan (Ford Motor Company), Liz Centoni (Cisco), Oliver Tuszik (Cisco), Vince Kellen (UC San Diego), Carrie Palin (Cisco), Harrison Chase (LangChain)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1748956425383001aEIK
By harnessing the power of AI, we can drive growth and build a better world. Join Cisco's leaders as they discuss innovation in the AI era with a focus on customer experience, use cases, and how Cisco is here to help you and your organization navigate it all.

### Kickstarting a Culture Shift: Evolving Teams Alongside AI - ITLGEN-2059
Speakers: Rebecca Stone (Cisco), Nic Penny (Hilton)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271957436001ztPz
Today's technology leaders face a dual challenge: harnessing cutting-edge innovations while nurturing the teams that drive them forward. In an era where tech must enhance—rather than overshadow—human connections, join an insightful discussion on how to align innovation with human-centric leadership for sustainable success, featuring: Nic Penny, Sr. Director of Global Network Engineering, Hilton - Hear a unique perspective on guiding a global hospitality brand through transformative tech advancements, while preserving the brand's commitment to exceptional guest experiences. Rebecca Stone, SVP of Global Revenue Marketing, Cisco - With extensive experience leading SaaS teams through rapid growth, hear insights essential for any organization seeking to navigate technological change with teams that adapt and thrive. Together, they'll provide actionable insights on creating cultures that not only accept but thrive on technological change.

### Knock, Knock. Who is There Behind your Firewall? - All About Identity on Cisco Secure Firewall - BRKSEC-2590
Speakers: Christopher Grabowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272010974001zA2Z
This session provides a comprehensive walkthrough of identity feature set of Cisco Secure Firewall. Participants will learn how to apply user and resource identities in the firewall policy obtained with available methods: SAML, RADIUS, LDAP, pxGrid, TS Agent, CSDAC, and more. Understand the flavours of user and resource object types along with active and passive authentication flows: captive portal, remote access VPN, 802.1x, Zero Trust Access and PassiveID. Familarity with Cisco Secure Firewall feature set is required.

### Kubernetes (K8s) Infrastructure Connectivity for the Modern Data Center - BRKDCN-2663
Speakers: Camillo Rossi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885982001zT0I
Kubernetes platforms serve as the cornerstone of cloud-native applications, with the process of bootstrapping a Kubernetes cluster now simplified to just a few commands. However, selecting and configuring an appropriate Container Network Interface (CNI) remains a complex yet critical task for establishing a scalable and reliable Kubernetes infrastructure. With a variety of CNI solutions available, determining which ones integrate most effectively with Cisco NX-OS and ACI is essential for making informed design choices. In this session, we will delve into the capabilities of Cilium and explore strategies for seamless integration with Cisco ACI and NX-OS based fabrics. We will discuss methods for implementing network segmentation, Service LoadBalancing and demonstrate how to enhance visibility across container and network environments. This exploration aims to empower attendees with the knowledge to optimize their Kubernetes networking configurations, ensuring robust and efficient infrastructure.

### LISP based SD-Access vs BGP EVPN Fabric -- Real World Lesson Learned from Two Large Scale Airport Networks - BRKENS-2835
Speakers: Sunil Pareek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271922033001zSgJ
Today Customer can deploy their Campus Network using SD-Access with LISP as control plane or they can deploy the Network using BGP EVPN. This session will cover real world experience with these two technologies through their actual deployments in two large Airport Networks. We will discuss pitfalls, gotchas and practical lessons learned from the planning phases, to design, implementation, and post-implementation supports so you can make your fabric journey a success, irrespective of choice. Topics discussed will be applicable for other verticals as well. Why Attend? This is your opportunity to gain valuable insights, proven strategies in deployment approach, and practical takeaways from experts with first hand experience.

### Lab Up For Success With Cisco Modeling Labs - BRKCRT-2059
Speakers: Francois Caen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271835298001zFuW
No matter what Cisco certification you're preparing for, you know you need to do more than just read the book to be successful. You need to practice. You can scour the internet looking for used gear, but when you get it, you still need the space to rack it, not to mention the power and cooling. Cisco Modeling Labs (CML) is a tool that provides you the virtual gear you need to practice for several Cisco certification exams with almost limitless topology possibilities. What's more, you can "plug" packet sniffers in with just a few clicks, introduce link problems, and even connect to physical kit you do have. In this session, we will explore how you can use CML to setup your own home labs. We'll dive into features such as traffic generation, packet capture, and external connectivity. Example topologies will be shared for a few scenarios to kick-start your studying and set you up for success.

### Langgraph: The Secret to Building Intelligent Agents - CISCOU-3005
Speakers: jesus Illescas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271844031001zdeL
In this lecture, we will explore Langgraph, a powerful tool for constructing intelligent agents. We will take an overview into what Langgraph is, its utility, and the various components it offers. Attendees will learn about the concept of graphs, their significance, and how they can be leveraged in building sophisticated systems. The session will include a demonstration of Langgraph Studio, showcasing its integration with network devices. This 30-minute session aims to provide a comprehensive understanding of Langgraph and its practical applications.

### Learn How Cisco's Virtual Demand Center Enables Webex Contact Center AI - BRKCCT-1513
Speakers: Daryl Thomas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271864280001zJLl
In this session you will learn how Cisco's Virtual Demand Center is enabling Webex Contact Center AI and Webex Connect (CPaaS) capabilities to support omni-channel sales interactions for our customers and prospects. We will provide you with insight on WXCC deployment strategies, Omni-channel best practices, integration considerations with external platforms and the use of hyper-personalization. Details will be provided to share how the VDC is using the "AI Agent Studio" to help construct workflows using AI agentic frameworks for voice, chat and email channels. Why Attend? - Practical information to avoid and mitigate technical and business challenges - Gain exclusive insights into how Cisco uses its own platforms to harness the power of AI, creating an efficient and innovative demand generation engine.

### Learn Through Example: Preparing for the DevNet Professional Exams DEVCOR and ENAUTO - BRKCRT-2022
Speakers: Jason Belk (Cisco), George Koukis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271835679001zv9z
Are you preparing for the DevNet Professional Exams DEVCOR or ENAUTO? Are you looking to unpack and understand core programmability concepts from these exams such as APIs, NETCONF/YANG and CI/CD? Learn from two expert instructors taking multiple real examples and live demos to demystify the concepts that often cause network engineers trouble when preparing for the DevNet Professional DEVCOR and ENAUTO exams. You will learn: - Tips and tricks configuring API calls for several network platforms - Practical and plain explanation of how NETCONF/YANG works - Troubleshooting best practices

### Learn about Cisco's Security Cloud solution: Secure Access - CISCOU-1054
Speakers: Jim Durkin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271839497001zSBm
If you're transitioning your security infrastructure to the cloud, this session is designed for you! We'll provide an in-depth look at Cisco's Security Service Edge solution—Cisco Secure Access. In this session, We'll explore the key components of Secure Access, highlighting both traditional and modern deployment scenarios for safeguarding your users and internal resources. Our focus will be on three key use cases: VPNaaS, Private Application Access (ZTNA), and Secure Internet Access. Additionally, We'll cover topics relevant to the CCNP Security exam, making this session especially valuable for those pursuing the 350-701 SCOR exam.

### Learnings Behind the Biggest Network Outages: Using ThousandEyes insights to improve IT resilience - BRKAPP-2021
Speakers: Angelique Medina (Cisco), Mike Hicks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272016108001zCWb
Organizations rely on a complex web of services to deliver essential digital experiences for customers and employees. While outages are inevitable, effective identification and resolution can differentiate you from competitors. Understanding the entire delivery chain and maintaining visibility into all components is crucial. During an outage, users often have limited information and may rely on past experiences, which can lead to incorrect conclusions about the issue and hinder decision-making. This session will showcase real-world examples of how large-scale analysis can pinpoint issues, identify responsible parties, and assess the business impact, highlighting the necessity of leveraging data for ongoing business continuity.

### Lessons Learned from Migrating ACI Customers from Traditional Firewall Insertion to PBR - BRKDCN-2659
Speakers: Hakan Palm (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885794001zSIc
Have you implemented ACI or are you interested in implementing it and would like to see how to take the next step to start leveraging ACI's features to segment your data center and insert firewalls in a much more scalable and smarter way? This session will take you step-by-step through how real-world customers migrated from their old traditional design in ACI with VRFs, EPGs, and traditional firewall insertion between the VRFs that were directly mapped to the old Nexus topology they migrated from, to modern topologies with firewall insertion using PBR ready to migrate to ESGs and to provide microsegmentation where needed. Content has been updated to show how yet another of the customers allows the LAN backup traffic to bypass the firewall in a multi-tenant multi-VRF environment.

### Lessons Learned: Zero Trust Implementation for "Smart" Architectures - BRKXAR-2029
Speakers: Patrick Lloyd (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271868335001zf11
The pursuit of micro segmentation is enough to keep most CISO's up at night. Knowing that devices with significant security vulnerabilities need to exist on the network further influences the need to segment the network, and protect critical assets. Utilizing the Zero Trust Model published in "Zero Trust Architecture" this session covers lessons learned in the planning, design, and implementation of "smart" technologies, buildings, and cities. Use cases such as connecting HVAC systems, MRI machines, and manufacturing technology to the network are used as illustrative examples. Focus for this presentation is on easing complexity, maintaining security of the network, easing enforcement, and realizing ROI quicker. Methods developed from lessons learned in various verticals will be presented, the application of which is to ensure that devices on the network are properly eased into micro segmentation, while still maintaining successful operation. This session will cover what methods are used when security is of the utmost importance, and segmentation of both vertical and lateral threats is a requirement. Knowledge of ISE, SNA, and TrustSec recommended, but not required.

### Lessons in Failure from a Self-Taught Developer - BRKGEN-1011
Speakers: Colin Lacy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271945271001znVJ
Learning to code isn 't just hard—it 's a journey filled with challenges, late nights, and moments of doubt. Platforms like Cisco U. and Udemy provide amazing tools, but they can 't make the concepts click for you. That 's a battle you face head-on. In this session, I 'll share the raw, unfiltered story of my career transformation—the stumbles, faceplants, and all the moments I thought I 'd never recover from. I 'll talk about those frustrating nights when nothing worked, tutorials I couldn 't even set up properly, and the constant fear that I 'd never measure up as a developer. This is a 16-year journey told through tattoos, boxing rings, burnout, and an ever-growing list of programming languages. It 's a reminder that failure isn 't just part of the process—it is the process. If you 're struggling to learn technical skills, feeling overwhelmed, or wondering if you'll ever "get it," this session is for you. You 're not alone. No coding experience is required—just a willingness to laugh (and maybe cringe) at some of my more embarrassing moments along the way.

### Let's Deploy Catalyst Center Global Manager (CCGM): Single Pane of Glass for Multiple Catalyst Centers - BRKOPS-2492
Speakers: Shai Silberman (Cisco), Prabhjit Singh Bagga (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271986826001zP0b
Are you managing multiple Catalyst Centers deployments across global sites? Then you must be facing complexities in managing multiple controllers, user logins, roles, and different workflows in UX/UI of all the controllers. The Catalyst Center Global Manager (CCGM) offers network administrators a single pane of glass view to simplify management and troubleshooting of devices and endpoints throughout the network. In this session, you will learn step-by-step how to: 1. Deploy CCGM on VMware ESXi. 2. Integrate multiple Catalyst Center controllers into CCGM for a unified Site and Device Inventory view. 3. Monitor the health of networks, clients, devices, and SD-Access, including P1/P2/P3 issues, using CCGM. 4. Seamlessly cross-launch into Catalyst Center from CCGM without additional authentication. 5. Utilize global search to locate clients or devices by IP address, serial number, MAC address, software version, and other metadata. The session will also feature live demonstrations of all these steps.

### Level Up Your AI Game: Upskill to be an AI Pro - PSOCRT-1101
Speakers: Kareem Iskander (Cisco), Lacey Caldwell Senko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833757001zP3v
Looking to upskill on AI? We've got you covered. From prompt engineering to AIOps, join us as we outline the top AI skills needed — from entry to expert — as you navigate your roles in the new world of tech. You'll learn what skills you need and where you can learn them. So, join us for a fun-filled session packed with insights, challenges, and a sprinkle of Cisco U. learning magic that will leave you ready to level up in the ever-evolving IT landscape.

### Level Up Your Network Service Provisioning with Intelligent Integrations for Cisco Services as Code - BRKATO-2002
Speakers: Aman Sardana (Cisco), Steve Holl (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271831900001z64U
Cisco Services as Code allows your organization to define its network infrastructure state and treat all elements as software code that is versioned controlled for management at scale. Automation and DevSecOps methodologies expedite the provisioning, configuration, testing, and deployment processes to enable you to seamlessly operate and optimize your network, backed by 24x7 technical support. In this session, learn how additional intelligent integrations enhance your infrastructure as code network management practice through: Using Cisco AI Assistant to reduce the technical knowledge needed for configuration and troubleshooting during network change execution. How integration with Cisco ThousandEyes allows for service-level observability and intelligence throughout the execution of your change. See how to integrate your ITSM, such as ServiceNow, with the git execution pipeline, for a fully integrated enterprise change management experience.

### Leverage agentic AI to transform your Observability practice - BRKOBS-1002
Speakers: Umang Agarwal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271981721001zh3H
Uncover the transformative potential of agentic AI in enhancing observability across digital systems. This session delves into how autonomous agents enable proactive issue detection, deliver near real-time insights, and optimize performance in intricate infrastructures. Explore best practices for designing and implementing agentic AI observability solutions that ensure scalability and adaptability. Gain actionable insights to elevate visibility, strengthen resilience, and streamline monitoring efficiency, empowering your organization to stay digitally resilient.

### Leverage the Power of Splunk Using the Latest Cisco Security Integrations - BRKSEC-1800
Speakers: Colin Gibbens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271999561001zVcx
Discover how Splunk empowers your security strategy by seamlessly integrating with Cisco solutions to deliver actionable insights. This session goes beyond the basics, showing you how to leverage Splunk's advanced analytics to strengthen your cybersecurity posture. See real-world applications of the platform and learn how it fits into your IT and security operations to enhance visibility, accelerate threat detection, and boost overall resilience. If you're looking to harness data for smarter, faster security decisions, this session is a must-attend.

### Leveraging Cisco Security APIs for threat hunting - DEVNET-3098
Speakers: Oxana Sannikova (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271909878001zIWD
This session is intended to help organizations in investigating computer security incidents by providing practical guidance on performing threat hunting activities using Application Programmable Interfaces of respective Cisco Security solutions. Specifically, the session describes practical examples of how to automate alerting and operationalize threat intelligence to initiate threat hunting and provides advice regarding different capabilities and features to automate forensics gathering. Its purpose is to inform attendees of various technologies and potential ways of using them in performing threat hunting and incident response activities.

### Leveraging Digital Twin for Advanced Network Management with Cisco Catalyst Center - BRKOPS-2442
Speakers: Christopher Beye (Cisco), Abhay Kaviya (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271989180001zg3x
In the evolving landscape of network management, the integration of Digital Twin technology offers unparalleled capabilities for monitoring, managing, and optimizing network infrastructures. With increasing network complexity and the severe business impact of outages, testing and simulating network configuration deployments has become essential. This session will explore how to create and utilize a computer-simulated model, or Digital Twin, that replicates your network's operating environment, devices, configurations, and traffic flows using Cisco Catalyst Center and Cisco Modeling Labs (CML). Key points include: Introduction to Digital Twin Technology: Understanding the fundamentals and benefits of Digital Twin in network management. Cisco Catalyst Center Integration: How to harness the power of Cisco Catalyst Center to build and manage a Digital Twin of your network. Creating a Network Digital Twin with CML: Step-by-step process to simulate your network using Cisco Modeling Labs. Simulating Cisco and Non-Cisco Networks: Efficient simulation leveraging real Cisco images to create a reliable virtual copy of your network. Advanced Monitoring and Optimization: Techniques for leveraging your Digital Twin to enhance network performance, predict issues, and optimize configurations. Automated Testing with CI/CD Pipelines: Building an automated testing workflow that reliably tests new configurations before deploying them in production, mitigating the risk of downtime due to bugs and configuration errors.

### Leveraging Tools to Successfully Migrate from UCM to Webex Calling Multi-Tenant - BRKCOL-2079
Speakers: Steven Fly (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271856245001zs2p
Moving your UCM calling platform to Webex Calling can feel like a big undertaking. However, if you follow a methodical process and leverage Webex and Cisco partner tools, you can reduce some of the work, effort and stress. In this session we will review a 3-phase approach to move your calling from UCM to Webex Calling MT. We will highlight key activities and how you can reduce the effort or improve the process to complete them by using existing Webex tools. We will also highlight some of the key partner tools that you can use as well. You will leave this session with the understanding of what is required to move to Webex Calling and the tools to help you get there.

### Listen to your network - use Webhooks to have your network let you know there is a problem. - CTF-1037
Speakers: Michael Lipsey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271984426001ztn2
APIs are the new SNMP, it's easy to build integrations from Cisco monitoring tools into your chat platforms or even into your Helpdesk ticketing software so that when there is a problem - it gets directly to the person on your team who is tasked with that are of supporting your infrastructure. Wireless problems get directed to those folks who support wireless, authentications problems can be directed to the authentication team, VPN issues can be alerted to the Helpdesk so that when users call in with a problem, the Helpdesk is already aware of it.

### MCP for DevOps: Unleashing the Power of AI and Model Context Protocol in Dev/Net/SecOps - DEVNET-3047
Speakers: Shannon McFarland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271909689001zGdT
Discover how the open source project, Model Context Protocol (MCP), redefines DevOps, NetOps, and SecOps by seamlessly integrating AI-driven context awareness into modern workflows. In this session, We'll unveil MCP's architecture and demonstrate how it simplifies complex automation challenges while dramatically accelerating workflows for Cisco solutions. Through real-world use cases—including integrations with GitHub, Ansible, CI/CD pipelines, and Cisco technologies—you'll see firsthand how MCP empowers teams to enhance efficiency, reduce complexity, and unlock the full potential of their DevOps ecosystems. Join us to learn how to harness MCP to transform your automation strategy and stay ahead in an AI-driven world.

### MFA Made Easy: Unlocking full potential of ISE-DUO integration - TACSEC-2019
Speakers: Leanny Salazar (Cisco), Dakota Brown (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271996977001zbYE
In a world where security is critical, having an extra layer of protection is essential. In this session, you will learn how to integrate Cisco Identity Services Engine (ISE) with DUO to provide a comprehensive Zero Trust Network Access solution. The session will also include troubleshooting tips and a demo to enhance your understanding and deployment of this solution. Attendees should come away with the confidence to successfully implement multi-factor authentication for their TACACS+ and VPN use cases.

### MLOps- The new branch in DevOps - DEVNET-1371
Speakers: Nikhil Ghodki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271895531001zTWg
The session will explore the transition from DevOps to MLOps as organizations adopt Large Language Models (LLMs) and Machine Learning (ML). MLOps integrates AI with DevOps practices to streamline processes. The session will cover the key components of MLOps using a sample application, demonstrate model training, and conclude with showcasing the deployment of an ML model in a production pipeline.

### MORE Programmability Skills for Engineers Who Don't Want to Code - BRKOPS-1238
Speakers: Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985603001zLbz
Who doesn't love a sequel?!? Well we are back with more programmability skills that don't require a single line of Python code that every network engineer can benefit from. I'm sure you've heard of Infrastructure as Code, but did you know that someone else already wrote the actual 'code'? Looking for a way to automate complex workflows and systems? This session will explore no code options for just that purpose. But where will you test and experiment these new skills? If only we could simulate the network... guess what, you CAN! And of course why concern yourself with writing code when there is AI around every corner - we'll explore some ways that artificial intelligence can help with the daily work of a network engineer.

### Make Your Network Future Ready: Wi-Fi 7, Cisco Spaces, and URWB - PSOENT-1022
Speakers: Lacey Jackson (Cisco), Dave Benham (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271927624001zUe9
Upgrading your wireless network is crucial to meet Today's demands for speed, reliability, and intelligence. In this session, explore Cisco Wi-Fi 7, Cisco Spaces, and Ultra-Reliable Wireless Backhaul (URWB). Gain insights on assessing your network's readiness, deploying real-time location tools, and ensuring reliable connectivity in any environment. Leave with a clear plan to future-proof your wireless strategy.

### Make a Wireless Engineer's Life Easy by Using Automation to Troubleshoot and Analyze Logs - BRKEWN-3002
Speakers: Surendra Bangalore Gurumurthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271942227001zgJe
This session focuses on how to leverage automation to collect required data and how it can be used to analyze and derive actions. Think about random client connectivity issues, VoWLAN one-way audio issues, or random access points dropping off from the network. When you open a Technical Assistance Center (TAC) case, the first thing the TAC engineer asks for is the data/debug/packet captures, etc. After this, the ball is in your court to collect data. The main purpose of this session is to cover the different KPI metrics we have on the system, discuss the different ways to automate log collection and analysis (WLC/Catalyst Center/scripts/Walkme), and provide customer use cases showing how automation helped.

### Making Catalyst SD-WAN Easy: Operational Simplification and User Experience - BRKENT-1313
Speakers: Nikolai Pitaev (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271930730001zlZn
Cisco Catalyst SD-WAN (formerly Viptela) builds a secure, unified connectivity over any transport and provides simplified operations with centralized management, policy control, and application visibility across the enterprise network. This introduction-level session will showcase how SD-WAN operations are made easier and more efficient with the introduction of new features and an enhanced user experience starting from 20.12 Release. They address customer challenges in the areas of onboarding, configuration, user interface, troubleshooting, visibility, and AI. Participants will become familiar with the new, intuitive, and consistent User Interface and will learn a fresh approach to configuration and guided workflows based on configuration groups, improved visibility, AI Assistant and new troubleshooting tools like Network Wide Path Insights (NWPI). Also, a Conversion Tool from configuration based on device and feature templates (aka UX 1.0) to UX 2.0 based configuration using configuration and policy groups will be presented. Several live demonstrations will be shown.

### Making Network Automation Easy with Playbooks - CNCATO-2006
Speakers: Stephen Correale (LogicVein)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271830559001zKUN
Network administrators and IT professionals, get ready to streamline your workflows like never before! LogicVein's latest feature, Playbooks, is set to transform how you handle repetitive tasks and complex network operations. REAL-WORLD APPLICATIONS • Configuration backups across multiple devices • Security compliance checks and reporting • Software updates and patch management • Network health monitoring and alerting Playbooks: a powerful new addition to LogicVein products. Designed to simplify and automate even the most intricate network management tasks. Join us for a quick overview and learn how to use Playbooks for your network.

### Making the Internet a Better Place by Participating in the IETF - BRKGEN-1385
Speakers: Eric Vyncke (Cisco), Prapanch Ramamoorthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271946476001zH6Z
Ever wondered how innovation for the Internet works? The IETF is the main place where a community of engineers that come together to share ideas and innovate. It can be daunting to think of developing and writing standards at first but know that this is a journey. Everyone is welcome at the IETF, this is free, and there is something for everyone to do and to learn. The presentation will be a unique and fun conversation between a veteran and a newcomer at the IETF to provide attendees with varied perspectives. Come to this session to learn about the IETF, the kind of work that happens there, and how you can get started with your journey at the IETF.

### Making the Shift: A Practical Guide to Selecting the Right FIDO Security Key for Your Workforce - VILSEC-2040
Speakers: Kaushik Mahadeokar (FEITIAN Technologies US)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271993832001zXFy
As organizations move toward phishing-resistant authentication, one of the biggest hurdles is knowing which FIDO2 security key works best for different roles, devices, and user environments. In this session, We'll break down FEITIAN's diverse hardware portfolio i.e. from biometric keys to iOS-compatible models and help attendees understand real-world use cases for each. Whether it's frontline workers, hybrid users, or executives needing biometric assurance, this talk simplifies the FIDO key selection process and empowers organizations to deploy with confidence.

### Malware Execution As A Service: A Deep Dive into CSMA Advanced File Analysis - BRKSEC-3101
Speakers: Jesse Munos (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272006224001z6fV
In this session, you will learn about the advanced file and malware analysis features available to Cisco Secure Malware Analysis (Threat Grid) users, and how to leverage them to best gain insight and intelligence into the threats your adversaries are deploying against you. You will learn usage of the portal and the API for tasks ranging from threat hunting to automated threat intelligence retrieval. These functions are beyond what you are already getting from your existing automated CSMA usage via products like ESA, WSA, Firewall, Secure Endpoint, etc. You will leave the session with an understanding of how to use CSMA to detonate malware in our network instead of yours, and above all, gain additional insights into the file-based threats that target you.

### Malware Exposed: Understanding Tactics and Behaviors - CISCOU-2063
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271842329001ziQH
In today's digital landscape, understanding malware is crucial. This session explores how malware operates and the tactics used by cybercriminals. Participants will learn about behaviors like code obfuscation and lateral movement. You'll gain insights into malware mechanics to better anticipate threats. Designed for security professionals with foundational cybersecurity knowledge, this session includes case studies like Ryuk ransomware to illustrate common tactics.

### Manage FTD and FMC with Ansible - DEVNET-2984
Speakers: Jeroen Wittock (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271908704001zdxr
In this session, we will show how to use Ansible to manage Cisco firewalls directly, or by using FMC. You will learn the basics of Ansible by diving in and using provided Ansible Playbooks. Attendees will learn about the benefits of using automation tool such as Ansible with Cisco firewalls. This will clarify how Ansible could be used in the context of policy as code, security as code, DevSecOps, or simply how you can use Ansible to automate managing your firewalls.

### Managed XDR Provided by Port53, Powered by Cisco - Real-Time Response Leveraging AI - VILSEC-1053
Speakers: Omar Zarabi (Port53 Technologies Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271992097001zPE6
By providing a holistic view of threats and real-time telementry accross your technology landscape, XDR delivers the correct information necessary for effective threat management.

### Master Wireless Network Management at Scale with Cisco Workflows - BRKOPS-2049
Speakers: Clint Sorensen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985996001z2a3
Are you struggling to maintain standardized networks at scale? Are you prepared to deploy new networks meeting the latest wireless security standards? Cisco Workflows offer a revolutionary approach to tackle these challenges, providing IT administrators with a powerful set of tools to orchestrate automation of management tasks. Join us to discover how Cisco Workflows can help you with the following: - Manage large-scale wireless networks, streamline operations to enhance network reliability and performance. - Implement best practices to adapt to evolving wireless and security standards. - Orchestrate standardized configuration changes for both cloud-managed Meraki and on-prem deployments. Whether you are looking to optimize existing network operations or prepare for the networks of tomorrow, this session will provide the knowledge and tools necessary to streamline management of your wireless networks with confidence and efficiency.

### Master the Art of Application Hosting on IOS-XR - DEVNET-2470
Speakers: Rahul Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833204001ztyZ
Cisco IOS-XR routers offer the capability to host applications alongside their routing functionalities, allowing seamless operation without impacting routing performance. This session provides an in-depth guide to application hosting on IOS-XR, covering everything from understanding the hosting environment to the step-by-step deployment process. Attendees will gain hands-on experience through a live demonstration, where an application is deployed and its functionality verified on an IOS-XR router. This session is designed to equip participants with the expertise needed to deploy applications effectively on IOS-XR platforms.

### Master the Move: Migrating VMs to OpenShift Virtualization in 60 Minutes! - BRKCLD-1013
Speakers: Stefano Gioia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845378001zTwS
Ready to migrate your VMs into the OpenShift ecosystem? In this session, we'll cover everything you need to know about migrating existing VMs to OpenShift Virtualization and explore effective planning strategies to ensure a seamless transition. We will also discuss post-migration and day 2 operations, offering practical guidance on managing, scaling, and optimizing your workloads within OpenShift. Whether modernizing your infrastructure or exploring OpenShift for the first time, this session will equip you with actionable insights to ensure a smooth and secure VM migration. Note—This is not a networking session.

### Mastering AI Monitoring: Optimize and Protect Your GenAI Stack with Splunk AppDynamics and Observability Cloud - BRKOBS-2013
Speakers: Luca Relandini (Cisco), Courtney Dragoon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271982692001zwp2
Dive into the future of AI application monitoring with Splunk AppDynamics and Observability Cloud. Discover how to keep your GenAI applications compliant and optimized by proactively managing performance and costs. Our advanced solutions provide comprehensive LLM stack monitoring, empowering you to correlate model and application performance. Rapidly detect anomalies, refine deployments, and ensure high-quality model outputs to boost the reliability of your AI-driven applications and the underlying infrastructure (e.g. Cisco AI Pod). Key highlights include: Monitor OpenAI API calls to secure the performance and reliability of AI-powered apps, adhere to corporate AI guidelines, and achieve cost efficiency. GPU Monitoring: Drive efficiency and manage costs with in-depth insights into your GPU infrastructure. Vector Database Monitoring: Maintain database health within the application context. Langchain Support: Ensure smooth and efficient workflows for your complex language models.

### Mastering API Troubleshooting: Practical Tools and Techniques for Complex Environments - DEVNET-2710
Speakers: Matt DeNapoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271906951001zSu0
As Meraki APIs become increasingly critical for integrating monitoring, security, and provisioning tools, they also grow in complexity. And with this complexity come unique troubleshooting challenges, often making it feel like you're searching needle in a haystack. In this session, We'll simplify the art of API troubleshooting through hands-on examples, you'll get practical experience with advanced diagnostics, log analysis, and error monitoring. We'll walk you through real-world troubleshooting methods that help identify, diagnose, and resolve performance and connectivity problems in Meraki APIs. Join this session to become a more effective problem-solver, and keep your integrations running smoothly!

### Mastering BGP: A Deep Dive into Basics and Design Best Practices for BGP and L3VPN - BRKMPL-2103
Speakers: Mankamana Mishra (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271961150001zejj
This exclusive session will provide a comprehensive understanding of Border Gateway Protocol (BGP) fundamentals and best design practices. This session aims to empower network engineers, administrators, and architects with the knowledge and skills needed to optimize BGP implementations for robust and efficient network connectivity. It covers understanding BGP fundamentals, BGP deployment scenarios (MP-BGP, L3VPN), scaling BGP networks, BGP security best practices, case studies, and design best practices.

### Mastering Cisco UCS: Innovations, Best Practices and Troubleshooting - BRKCOM-2456
Speakers: David Soper (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861768001zkoW
You have a Cisco server environment up and running, or you are evaluating doing so? First, we will discuss recent innovations in UCS hardware and management software. Then we are going to help you ensure a reliable environment by talking about best practices for configuring and using your servers. Finally, we are going to wrap the session up by looking at how you can troubleshoot your already deployed environment.

### Mastering Data Automation for Troubleshooting: Leveraging EEM and Python Scripts - TACENT-2029
Speakers: Arturo Obregon Gutierrez (Cisco), Jeff Riehle (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271930544001zKD6
Automate Collecting Data for Effective Network Troubleshooting with Cisco EEM and Python Scripts. As networks grow in complexity, effective troubleshooting becomes a critical skill for minimizing downtime and maintaining operational efficiency. Join our 30-minute session to explore how Cisco's Embedded Event Manager (EEM) and Python scripts in Guest Shell can enhance your troubleshooting capabilities. Learn how to leverage Cisco EEM to monitor network events and execute custom troubleshooting actions. Discover how to use Python scripts in Guest Shell to collect real-time data and perform advanced diagnostics, empowering you to resolve issues faster and with greater precision. Ideal for network engineers, this session focuses on practical strategies for improving troubleshooting workflows and strengthening network resilience. Gain actionable insights to expand your troubleshooting toolkit and tackle challenges with confidence. Key Takeaways: • Basics of Cisco EEM for real-time event monitoring and troubleshooting. • Use Python scripts in Guest Shell to perform advanced diagnostics, • Strategies for integrating EEM and Python to address complex network issues. • Improve troubleshooting efficiency to reduce downtime and ensure network reliability. Strengthen your troubleshooting expertise with these powerful tools and techniques!

### Mastering Day 2 Operations of Cisco Nexus Hyperfabric - TACDCN-2014
Speakers: Prashanth Krishnappa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271881357001zXfn
As organizations deploy Cisco Nexus Hyperfabric to power their data centers and mission-critical workloads, maintaining optimal performance beyond initial deployment becomes essential. This presentation explores best practices for managing Day 2 operations, including assertions, continuous monitoring, troubleshooting, telemetry, and lifecycle management. Attendees will gain insights into strategies that ensure system resilience, improve operational efficiency, empowering them to maximize the value of their Hyperfabric infrastructure.

### Mastering Generative AI: How Cisco is Empowering the Future with LLMs - BRKXAR-2019
Speakers: Robert Barton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271870237001zBdY
Generative AI and LLMs have captured the world's attention, but how they work remains a mystery for many. In this session, we will break down the core building block of modern Generative AI. We will explain how LLMs are designed and trained, and how they have been implemented in some of the most common tools, such as ChatGPT, Claude, and LLaMA. We will explore how Cisco is unlocking the potential of GenAI and LLMs across our portfolio, from Cisco Security Cloud, to Enterprise Network systems, to Webex.

### Mastering Growth Without Breaking the Bank: Your Guide to Scaling with Splunk� Observability Cloud - BRKOBS-2007
Speakers: Navtej Singh (Splunk, Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271980509001z4G4
In the era of exponential data growth, managing observability costs while scaling your infrastructure is no longer optional—it's essential. This session dives into practical strategies for reducing metric cardinality, archiving low-value metrics, and leveraging usage analytics to optimize your observability workflows. Discover how to analyze data usage, apply cost-effective rules for metrics management, and make informed decisions to scale confidently without overspending. Participants will gain actionable insights into Splunk's Metrics Pipeline Management and Archived Metrics, as well as learn how usage analytics can uncover optimization opportunities. With real-world examples, including Atlassian's journey, We'll explore how these solutions enable reduced telemetry costs, improved efficiency, and smarter scaling. Whether you're an engineer or IT leader, this session will equip you with the tools to align observability with your growth ambitions.

### Mastering Hands-on Labs: Unlocking the Power of Cisco Modeling Labs (CML) with Skillable - CISCOU-1064
Speakers: Moe Riyami (Cisco), Cory Gibson (Skillable), Mark Mangelson (Skillable)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272018055001zQiL
Cisco Modeling Labs (CML) is an essential tool for network simulation, aiding engineers in certification preparation and real-world scenarios. However, managing CML at scale involves challenges like licensing and lab automation. This session will show how Skillable enhances CML delivery, facilitating structured, automated learning experiences. We'll demonstrate Skillable's integration with CML, supporting scalable labs, automated assessments, and dynamic feedback to improve certification and training processes. Attendees will experience how interactive labs can enhance CCNA, CCNP, and CCIE exam prep, optimize study methods, and utilize CML for scalable simulations.

### Mastering Kubernetes Troubleshooting: Pro Techniques for Peak Performance - TACOBS-2000
Speakers: Arpitha Devlapally (Cisco), Abhi Bajaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977589001zMDO
"Kubernetes, the world's second-largest* open-source project after Linux, continues to reshape how organizations deploy and manage containerized applications. By 2027, Gartner* predicts that over 90% of global enterprises will be running containers in production, making fast, effective troubleshooting a mission-critical skill. In this session, you'll gain insider expertise from Cisco Support SMEs on diagnosing and resolving real-world Kubernetes issues, with a deep dive into the AppDynamics Cluster Agent. Learn how to identify common misconfigurations, optimize performance, and accelerate root-cause analysis using powerful observability tools. What you'll take away: - Master key troubleshooting techniques to quickly detect and fix Kubernetes issues. - Leverage AppDynamics monitoring to streamline diagnostics and boost efficiency. - Implement battle-tested best practices to maintain a high-performing, resilient Kubernetes environment. Join us for this high-impact session and take your Kubernetes troubleshooting skills to the next level! "

### Mastering Operating System Installation with Intersight: Step-by-Step Guide and Troubleshooting Best Practices - TACDCN-2015
Speakers: Neil Martin (Cisco), Francisco Zeron (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271881542001zdHG
In this session, you will learn how to seamlessly install any of the supported operating system using Cisco Intersight through a clear, step-by-step process. We will dive into most common issues that can disrupt the installation process. Attendees will gain practical insights on identifying root causes and applying effective troubleshooting techniques. Whether you are new to Intersight or seeking to improve your operational efficiency, this session will equip you with the tools and knowledge to streamline OS deployments and swiftly resolve installation challenges

### Mastering Telemetry: Streamlining Data Collection with OpenTelemetry and Splunk Observability Cloud - DEVNET-2039
Speakers: Renato Quedas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912394001zwOd
In this talk, participants will delve into the complexities and challenges of managing multiple OpenTelemetry agents for gathering telemetry data locally and transmitting it to a remote backend. We will explore common issues such as data loss, latency, and resource contention, and illustrate how these can hinder your observability goals. Attendees will then discover how the OpenTelemetry Collector can streamline and enhance the telemetry process by providing robust, centralized telemetry signals that address these challenges effectively. Finally, we will showcase how Splunk Observability Cloud's Dashboarding and Alerting capabilities can be employed to monitor the health and reliability of your telemetry pipelines, ensuring quick insights and proactive issue resolution. Join us to gain the knowledge and tools to optimize your observability strategy and maintain robust telemetry pipelines.

### Mastering Tenant Automation: Cisco Security Cloud Control APIs for MSPs - DEVNET-2939
Speakers: Aaron Hackney (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271908318001zE61
A Managed Service Provider's journey with any product typically involves designing automated systems to onboard a customer, manage their operations (including upgrades), and monitor the service in order to proactively handle issues as and when they arise. In this talk, we will show you how Cisco Security Cloud Control's APIs, built from the ground-up for MSPs, can help you design a streamlined solution at scale to offer a managed Cisco Secure Firewall solution as a service to your customers. We will first look at the tenant creation and service provisioning APIs that allow you to go from zero to a managed customer environment with a cloud-delivered Firewall Management Center and Multicloud Defense in a matter of minutes. We will then walk through APIs to onboard your customer's firewalls into your environment and start managing their policies, and about how you can react quickly to security advisories by upgrading all of your customers' firewalls using just a set of simple APIs. Finally, we will look at monitoring APIs that you can hook straight into your own alerting system so that you're always one step ahead of any problems.

### Mastering Webex Calling: Everything You Need to Know - BRKCOL-2043
Speakers: Vladimiro Lerena (Cisco), Jose Gregorio Linero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271855468001zCGJ
Join us for an enlightening session where we will dive deep into the world of Webex Calling. This session will uncover the extensive benefits and innovative features that make Webex Calling the premier choice for modern communication. Gain a solid understanding of its core functionalities and learn how to effortlessly integrate this solution into your organization. We will highlight the advanced capabilities that distinguish Webex Calling, focusing on how to optimize its use through the intuitive Control Hub. Discover how to leverage sophisticated analytics and exceptional troubleshooting tools, seamlessly enhanced by ThousandEyes, to elevate your operational efficiency. Our cutting-edge operating systems, PhoneOS guarantee a seamless user experience. In just a few clicks, unlock powerful functionalities such as comprehensive call recording, advanced call queuing, an attendant console, and diverse PSTN access options. Experience firsthand how Webex harnesses the power of AI to revolutionize calling, setting a new standard in communication. Don't miss this opportunity to see how Webex is redefining the future of communication technology.

### Mastering the Upgrade to CUCM Version 15: Innovations, Troubleshooting, and Seamless Transition - BRKCOL-2082
Speakers: Edgar Rodriguez Aguilar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271852630001zMtD
In today's fast-paced communication world, keeping your infrastructure and software up-to-date is more important than ever. Join us for an engaging session on CUCM version 15, the latest breakthrough in Unified Communications Manager. You'll discover its innovative features and essential system requirements. you'll learn effective strategies for upgrading from any prior CUCM version to version 15, ensuring a seamless transition. Our lab demonstrations will showcase the most efficient upgrade and migration methods, making the process straightforward. You'll also gain the skills to identify and troubleshoot common challenges during the upgrade, allowing you to confidently navigate a successful upgrade or migration.

### Maturing from NetOps to Network Observability: How to use Splunk, ThousandEyes, and Meraki for true end to end observability - BRKOBS-1015
Speakers: Chris Crocco (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271978953001zPjP
Network Observability should be more than just additional monitoring using existing processes and solutions; it should empower your teams to understand what is happening across the enterprise to drive network performance and ensure better experiences. But how do you get started, and how is this really different than traditional Network Operations? In this session, we will show how to use the Splunk Enterprise, ThousandEyes, and Meraki together to deliver truly different experiences to your network teams and how the to get started in maturing your NetOps practice.

### Maximize Your 9800 Wireless Controller Capabilities: Troubleshoot 802.1x and Gain Radius Fragment Control with MTU Adjustments - TACENT-2025
Speakers: Jaydeep Patel (Cisco), Carlos Socorro (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271929785001zw5u
Security takes the lead for enterprises wireless, driving the customer to choose one of the secured method 802.1x with EAP protocols. This process involves client-side and Radius server certificates exchanges which are larger in size. As certificates fragments travel from wireless clients to radius server through CAPWAP, and then Radius, they often face challenges in tunnels or firewalls and get dropped. Let's deep dive into troubleshoot of EAP and radius packets and learn how to utilize the new WLC feature to modify MTU for Radius Packets to gain control over fragmentations.

### Maximizing Your Cisco TAC Experience: Enhancing the Customer Experience with Faster, Effective Resolutions - TACCX-1001
Speakers: Cherian Gheevarghese (Cisco), David Grup (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272015519001zy8I
Optimize your experience with Cisco's Technical Assistance Center (TAC) by mastering key strategies for effective engagement and resolution. This session will provide expert guidance on navigating TAC resources, utilizing proper contact channels, and understanding critical processes to accelerate issue resolution. Additionally, learn how to address complex technical challenges through clear direction, expert insights, and actionable recommendations. Equip yourself with the knowledge and confidence to streamline support interactions and achieve the best outcomes for your business.

### Maximizing the Value of your Cisco Solutions with Personalized Technology Adoption Plans - PSOCX-1021
Speakers: Josh Suhr (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272014928001z0Mb
Are you unlocking the full potential of your investments in Cisco products and solutions? Do you wish you had a crystal ball to help you make the most of the technologies you already have? If these questions intrigue you, join this session to explore a groundbreaking approach powered by telemetry and generative AI to swiftly maximize the value you can derive from your Cisco solutions. This approach starts with your specific goals and takes you on a dynamic and personalized adoption journey to achieve your desired outcomes and discover new possibilities. Empower your organization like never before.

### Media & Time Sensitive Networking with C9K Switches: Converging Time Sensitive Applications & Devices onto Ethernet - BRKENS-2094
Speakers: Randeep Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271920280001zcMO
In this session, we will discuss how you can leverage Precision Time Protocol to build a network that can onboard time sensitive applications or devices onto an existing Ethernet Network. We will discuss technical details, supported features, limitations, and design considerations around the PTP & AVB Solution on Catalyst 9000 switching platforms.

### Meraki Automation Your Way: Three Automation Tools, One Data Model - DEVNET-2273
Speakers: Steven Carter (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271902479001zZEH
In this session, we explore how using a single data model can simplify network automation in Meraki environments. This data model serves as a common foundation to push configurations to both managed and monitored devices, using either Terraform, Ansible, or Python for delivery. By focusing on efficient data movement to API endpoints, we minimize the need for extensive coding. Additionally, we emphasize separating configuration data from the underlying code, enabling reusability and enhancing DevOps workflows. This approach reduces complexity, streamlines automation, and allows for consistent, scalable network management across diverse Meraki environments.

### Meraki Cloud Networking for the CLI Wired Brain - BRKTRS-2008
Speakers: Jason Clark (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971392001zbn0
You receive a call about a network issue, you pull up the Meraki Dashboard but are not sure where to begin. You think to yourself "If I only had CLI" I would know where to start. You may be interested to moving to Cloud Networking, but you are unsure you can live without CLI. You may have wondered using a dashboard makes you a less efficient troubleshooter. Change can be scary, but with the Meraki Dashboard, it doesn't have to be. This session is about evolving CLI skills and mindset to a Cloud Platform approach. Focused on unleashing the power of Meraki Dashboard's end-to-end visibility, digital experience assurance, tools and APIs to troubleshoot and simplify operations.

### Meraki MX Next-Gen SD-WAN and SD-Internet Connectivity Dual-Stack - BRKENT-2176
Speakers: Cassio Luis Reis Gomes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271931865001zzRv
This session provides a detailed exploration of the Meraki SD-WAN solution, emphasizing its functionality in both IPv4 and IPv6 environments. Participants will gain practical insights into deploying Meraki MX for SD-WAN and SD-Internet using the BGP routing protocol for IPv4 and IPv6, including techniques to manipulate prefixes effectively. The session will cover best practices for deploying SD-WAN in large networks with high availability, focusing on scalability and reliability with BGP. Additionally, participants will learn how to leverage the Meraki MX for Internet access, utilizing the SD-WAN Plus license model to unlock advanced features such as SD-Internet and Web Application Health, in conjunct with BGP, Firewall and built-in security features. These features enhance user visibility, optimize the user experience, and strengthen network security. The session will also highlight the integration of the Cisco Meraki MX appliance with Cisco Extended Detection and Response (XDR), showcasing how this synergy improves threat detection and response capabilities. With its direct connection to the Internet, the Meraki MX becomes a more robust solution, empowering organizations to achieve superior performance and security in their SD-WAN deployments.

### Meraki Offline - Cloud Management without the Cloud - BRKTRS-2116
Speakers: Chase Gleason (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271970823001zzWx
Interested in Cloud Network Management, or already have it deployed? Are you concerned about what happens if your Cloud-managed device loses internet access? In this session, you will learn features that help keep Meraki-managed devices always cloud-connected, what network services are available (even when the cloud isn't available), and how to troubleshoot and configure Meraki devices when the internet is unavailable.

### Meraki Unleashed: Programmatic Access, Programmatic Action - DEVNET-2482
Speakers: Jon Hartman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271905575001zQAz
In this session, you'll learn about the data that can be programmatically harvested from the Meraki dashboard, how to collect it, leverage machine learning to gather insights, and interact with that data by leveraging AI. Modern networks and managed services require instant and automated control. Unleash the power of programmability and drive toward greater efficiency, fewer errors, more rapid action, and increased business value. You've outgrown the CLI, now it's time to outgrow the GUI!

### Meraki Wireless from a Troubleshooter Perspective - BRKEWN-2399
Speakers: Jakub Talalaj (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271939049001zlpX
The session will help you to unleash the Power of Meraki Wireless. Get an exclusive look into how Meraki's cutting-edge technology, powered by the robust Meraki Cloud, assists to pre-emptively identify client issues and root causes, before end-users realize them. This informative session promises not just theoretical knowledge but practical insights and tips that can be immediately applied to your daily work. Come, explore the future of wireless networking, and equip yourself with the skills needed to create efficient, seamless, and reliable wireless environments. Your journey to mastering the Meraki Wireless begins here.

### Meraki as Code - DEVNET-2084
Speakers: Snezana Mitrovic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899796001zgbF
Learn to simplify and modernize network management with Meraki as Code in this session. Leverage Terraform and the Meraki API to define and configure network resources, manage versions with Git, and automate deployments using CI/CD pipelines. By the end of the session, you'll see how to deploy a fully functional Meraki network in just minutes and gain practical insights into applying DevOps principles to streamline operations. Perfect for professionals ready to scale network deployments efficiently and adopt modern practices in network automation.

### Meraki for the U.S. Federal Government: What You Should Know - BRKARC-2097
Speakers: Larry Woods (Cisco), Chris Hocker (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271971015001znfw
Cisco Meraki has achieved FedRAMP certification for use in the U.S. Federal Government. This session will cover the Cisco Meraki FedRAMP offering, its capabilities, and the hardware options best suited to meeting Federal requirements. Furthermore, we will cover the architectures that best address Federal use cases, IPv6 readiness, deployment scenarios, and what features/products we plan to bring in the future!

### Methodology into Enterprise Architecture: From Conception to Action - BRKXAR-2038
Speakers: Anagha Kelkar (Cisco), Arul Jagadeesan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871388001z9JY
Enterprises are evolving and innovating at a rapid pace. Quantum leaps in the volume of data, distributed users, and applications, along with the adoption of SaaS and Multicloud services, increase the demand on today's IT organization. Architecture plays a vital role in any organization by taking a proactive and comprehensive approach to meet strategic business vision and outcomes. Identifying the design criteria and aligning tools, people, and processes to work cohesively with future capabilities is critical to business. In this session you'll learn the elements and methodology behind an enterprise architecture, how defining an enterprise architecture supports your teams and your customers, how to get started, and what you can build.

### Micro-segmentation Where and When You Need It -- Applications, Workloads, Networks, and Outcomes - BRKNWT-2503
Speakers: Dave Zacks (Cisco), Vivek Santuka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271972936001z7S8
One hears again and again that enabling micro-segmentation is a critical – indeed, a key – component of an overall security architecture. But how can this important capability be enabled – what are the technologies, deployment architectures, and use cases for micro-segmentation? Come to this session to find out how this key set of capabilities can be a great fit in your own network and workload deployments! In this session, we will explore the role of micro-segmentation in network and application security, controlling lateral movement and protecting critical assets. We will delve into Hypershield, Cisco's newest and most advanced solution providing autonomous segmentation and distributed exploit protection, leveraging an AI-native security platform with kernel-level visibility and enforcement. And most importantly, we will showcase how these capabilities can be leveraged to segment wherever segmentation is needed in an organization. Presenting this session is the dynamic duo of Vivek Santuka and Dave Zacks — two Cisco engineers with a shared passion for network-enabled, workload-aware security and visibility solutions. Come to this fun, engaging, and informative session to see and understand how micro-segmentation will play a key role in your secure application and network future!

### Migrate from Your Existing Network to VXLAN EVPN - BRKDCN-2951
Speakers: Yianni Thallas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271890566001zWou
Still running STP/vPC or FabricPath? This session will provide data center migration strategies from these legacy protocols to the Cisco VXLAN EVPN next-gen data centers, which help mitigate issues with these protocols and provide users with automation and visibility. The session will cover migrations of FHRPs in addition to coexistence of FHRP and Anycast Gateways, moving workloads, and migrating external layer 3 connectivity from a classic network to the new VXLAN EVPN network. By the end of this session, participants will leave with the knowledge and prerequisites in order to migrate to the Cisco next-generation data centers. Participants should have a basic understanding of VXLAN EVPN prior to joining this session.

### Migrating IP phones from Unified Communications Manager (on-premises) to Webex Calling (cloud) by a TAC Engineer - BRKCOL-2064
Speakers: Joe Martini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271852251001zZu5
This session will provide an in-depth understanding of how to migrate between Enterprise Firmware used with Cisco Unified Communications Manager (CUCM) and Multiplatform Firmware used with Webex Calling for the Cisco IP Phone 7800 and 8800 Series. The purpose of converting firmware is to help migrate customers who already have existing phones. Participants will learn about migration automation tools within Control Hub as well as the Cloud Upgrader (upgrade.cisco.com) from a TAC engineer and co-developer to maximize your success rate by avoiding common mistakes. Topics covered include: What Is a Phone Migration Phone Eligibility Migration Licensing Firmware Conversion

### Migrating to Multi-Cloud and CloudNative environments using Cisco CX Best Practices ensuring optimal experience for your consumers - BRKCLD-1769
Speakers: Peter Charpentier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845947001zeiw
Transforming an IT landscape to multi-cloud cannot be done overnight -- as it is a journey. How your resources are used, on-premises and/or cloud, are important topics to consider to achieve a successful multi-cloud strategy. The architecture of Virtual Machines vs Containers, is also important when migrating to a multi-cloud setup. This session covers both the methodology and technical aspects of multi-cloud migration-based Cisco CX best practices and how ThousandEyes can help to ensure success, and keep the optimal experience. The session will show how to securely connect on-premises to public cloud and how workloads can be migrated to cloud and back to on-premises, but also with an overview on how running as cloud-native services (containers) will help workload mobility. When migrating applications to cloud, user experience should always remain the same. We will also cover some troubleshooting aspects, and show the steps to understand how to try and pinpoint a problem, and root cause analysis. This can be achieved by using ThousandEyes, as it enables monitoring and analyses user experience, performance, and stability of applications regardless of the deployment model. These will also help to track user experience and impact, and how things can be addressed quickly.

### Mission Critical OT Network Best Practices Using Private-5G Wireless Services - BRKSPM-3581
Speakers: Derick Linegar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271969290001z8F3
Private cellular deployments covering 4G and 5G connectivity are rapidly becoming a valid approach that provides private wireless services for a variety of enterprise customers and their use cases today. But where private 5G can really shine is in providing mission-critical services, leveraging deterministic radio behavior, QoS, and low latency-based connectivity services to finally enable wireless operational technology (OT) connectivity. Based on OT-oriented security and OT traffic separation framework, this new approach requires a new set of engineering best practices that are critical for a successful deployment. This session will review these best practices and provide examples for a private 5G-based deployment for the purpose of onboarding and operating mission-critical wireless OT infrastructure.

### Mitigating Performance Impacts of Cisco Secure Endpoint - TACSEC-2022
Speakers: Andrew Koelbel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271997566001zyct
The current nature of the threat landscape requires that endpoint detection and response (EDR) solutions, such as Cisco Secure Endpoint, investigate every facet and activity on an endpoint. Unfortunately, this necessary action can impact endpoint performance and cause high resource utilization. This session will discuss how to mitigate any performance impacts caused by Cisco Secure Endpoint through methods such as exclusions and policy tuning.

### Mitigation of Adversarial Attacks on Generative AI with Cisco's AI Defense - BRKSEC-1554
Speakers: Keith O'Brien (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271999158001z1ey
This session explores the evolving security landscape of generative AI, with a focus on threat models specific to large language models (LLMs). We will examine key security frameworks, including the OWASP Top 10 for LLMs and MITRE ATLAS, to provide a structured understanding of potential risks. The talk will feature demonstrations of real-world threats derived from OWASP's research, illustrating how adversaries can exploit generative models. Finally, we will introduce AI Defense and how it can be used to mitigate these threats and provide security visibility to enhance the security of LLM deployments.

### Model Driven Environments in Practice: The Sandbox story - DEVNET-2301
Speakers: Eddie Corban (Cisco), Mike Mackay (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271903432001zit4
When Sandbox first started, automation, and more specifically automation tooling, was in it's infancy. Since those dark days it's changed. Sandboxes and how we build our environments needed to change as well. From process and tooling to customer experience and reusability we had to take a hard look at ourselves and decide, are we leading the charge or are failing to walk the walk that we promote. The answer was both - we were using the cool tools, Ansible, SDK's, Terraform etc. But using these technologies is only the start of the process, how do we bring these all together into a single platform and allow reuse. We were not following a GITOPS process and we were definilty !DRY (Don't Repeat Yourself) We needed a full, pragmatic, rethink of how we worked and then apply that to our own business. Then we can honestly stand up and say "This is how we do it, it may not work for you but it works for us and maybe it will give you ideas that you can apply" And by the way, it's hard work. But every step forward does not result in a never ending tech debt cycle.

### Model it Up: Building Networks with Cisco Modeling Labs - BRKOPS-1104
Speakers: Matt Leuschner (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985409001zu2w
Are you new to Cisco Modeling Labs (CML) and trying to figure out how to get started? Do you want to know what types of network topologies you can build? Are you unsure of the hardware resources you need to run the CML instance? This session will explore how you can take advantage of the features available in CML to model very simple to fairly complex networks. Attendees will walkthrough the steps to build their first lab and how to setup console, terminal, or GUI access to their nodes. You will see examples of the different topologies that can be designed in CML, understand the system requirements to run those topologies, and how to maximize the number of nodes in your labs. Finally, attendees will explore how to use CML to perform packet captures and verify their network simulations are operating as expected.

### Modern Authentication Explained to the Network Professional - BRKSEC-2144
Speakers: Aaron Woland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272007458001zzm1
Identity Security is all the rage (again). However the identity attacks look quite a bit different than they used to. To understand the modern identity landscape, you have to start to understand these crazy concepts like "Single-Sign-On" (SSO), what on earth OIDC is, and how come "cookies" are so important. However, the more things change, the more they stay the same, too. AAA: Authentication, Authorization & Accounting does not mean 'RADIUS'. Those of us in Network Security are usually familiar with 802.1X and authenticating to networks for wireless, wired, and even VPN. AAA is a fundamental and foundational security principle, not a product. Those concepts are universal and still apply when you hear the 'new' authentication protocol types like: OAuth, SAML and OIDC, as well as terms like FIDO and WebAuthN. This session focuses on explaining modern web-based authentication protocols & teaching about them in a way that compares & contrasts them to network security authentication methods. In other words: come learn about the latest in identity attacks (like session hijacking, and MFA fatigue) and the latest in authentication protocols and how to understand them with your networking background. If you know all about SAML & OAuth already, but don't understand 802.1X or EAP - this session is also for you! Aaron Woland, an expert leader from Cisco's Duo Security business, will entertain you while educating you on this important and growing area of security.

### Modern Data Center Security: Consistent control for traditional and cloud-native Kubernetes applications - PSOSEC-1030
Speakers: Ant Ducker (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271996168001zLUC
In many organizations, Kubernetes-based applications coexist — and sometimes interdepend — with traditional application components. However, Network Security teams may not always be aware of these modern applications or recognize that Kubernetes can function as a nested data center within their existing infrastructure. Explore the fundamentals of Kubernetes applications, how they compare to traditional applications, and how Cisco can provide common ground between Network Security and DevOps teams in order to achieve consistent security policy and control, regardless of the way an application is hosted within the Data Center.

### Modern Network Design Is More Complex Than Ever, Leverage AI as Your Cheat Code to Survival - BRKXAR-1008
Speakers: Nick Armstrong (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271867569001z5pT
AI is writing code and changing the design decisions we need to make. Leverage the strengths of AI for complex on-prem, cloud, and multicloud architectures. Discover the ways that AI is fundamentally changing IT system design for enterprise and critical systems. Take a peek behind the curtain to see how Cisco is redefining its product offerings. You'll leave this session understanding how AI is influencing the industry to avoid designing a system that will be obsolete by the time it is screwed into a rack. Whether you are a salty engineer or an aspiring architect, join us in this session and step into your next design meeting with more information and greater insight.

### Modern approaches for IOS XE network device management on Cat9k - DEVNET-1110
Speakers: Jeremy Cohoe (Cisco), Ashil Parekh (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271911434001zx7O
If you manage any number of IOS XE devices directly then this session is for you because it will very quickly make you an expert in the operating system's Day0-N features so that you can manage the network more efficiently. Day0 includes the long standing ZTP Zero-Touch provisioning but when encryption is required end-to-end then the Secure ZTP features can be used. A comparison and benefits of each will be demonstrated Day 1 API with a focus on the tooling to enable success regardless of NETCONF or RESTCONF & Ansible or Terraform. What are the best practices when moving away from the CLI and leveraging automation? What about Atomic config replace operations? Day 2 Telemetry helps transition from slow SNMP to enhanced speeds with YANG to demonstrate the top sustainability usecases. Day N shows the ping and traceroute livetools and other features for keeping the operational costs low by using the built-in automation capabilities.

### Modernising virtualisation with Kubernetes, KubeVirt and Cilium - CISCOU-2067
Speakers: Dan Finneran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271843086001zyKI
Infrastructure is an ever evolving landscape, as we moved from bare metal to virtualisation we're now seeing a shift to containerisation with Kubernetes. Like the move to virtualisation we are again in a position where new technology silos are appearing in the datacenter, with no clear inter-operability between the technologies. This session will cover three technologies, Kubernetes, KubeVirt and Cilium and how these projects together can provide a virtualisation platform that is managed by the Kubernetes orchestrator. This new cloud native platform provides the opportunity to harmonise the management and operations of both containers and virtual machines through one control plane.

### Modernizing Private WAN Architecture for Critical Networks Infrastructure - BRKSPG-2063
Speakers: Roberta Maglione (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271964451001zeWX
Several large Enterprises, like financial institutions, and Public Sector entities, like government agencies, military forces, transportation and utilities companies, have the need to evolve their own Private WAN infrastructure to obtain better controlled performance, increased scale, enhanced security, and flexibility at a lower cost. Attend this session to learn more about how to modernize and optimize this critical network infrastructure with advanced technologies like Segment Routing, Routed Optical Networking and security capabilities available on fixed and modular, high density and power efficient routing platforms

### Modernizing Your Data Center for the Future and AI - PSODCN-1007
Speakers: Todd Brannon (Cisco), Gerald Richard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879975001zSSO
The rapid pace of AI innovation is pushing organizations to quickly embrace new data center technologies. Your infrastructure choices will impact the scope and success of your initiatives. In this session, we'll help you understand the implications of those choices and highlight where Cisco can support you — whatever the shape of your AI ambitions. We'll also discuss Cisco innovations in data center compute and networking to help you identify your path forward.

### Modernizing Your On-Premise Contact Center & Exploring Transition Options to the Cloud - BRKCCT-1512
Speakers: Mike Turnbow (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271864083001zxzu
This session is crafted primarily for Cisco Contact Center Express (CCX) users, with additional insights for those using Contact Center Enterprise (CCE). Dive into the available tools and strategies that can help modernize your CCX platform and prepare for a seamless transition to Cisco Webex Contact Center. We'll explore key topics such as feature parity and roadblocks that may be hindering some customers from moving to the cloud. Learn about current solutions for migrating from CCX and how Cisco's extensive cloud features can position your contact center at the forefront of customer service innovation. Additionally, this session will highlight the hybrid features available to CCE customers, demonstrating how these can enhance your Enterprise Contact Center experience. By leveraging cloud capabilities and AI-powered enhancements, discover how to achieve greater scalability and flexibility in your existing setup. Join us to uncover how Cisco can support your journey towards a more advanced and efficient contact center.

### Modernizing your Contact Center Enterprise (UCCE/PCCE/WxCCE) with Cloud and AI - BRKCCT-2031
Speakers: Joe Wong (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271865622001zYaF
Come learn how Cisco is investing in modernizing Contact Center Enterprise (UCCE/PCCE/WxCCE) with cloud services to include AI, digital engagement, and centralized, web-based management. This session will show you how we are doing this and what business value-add services and features (AI and cloud) are available now and in the near future. The goal is to help you all determine what is the best Cisco contact center solution for you, whether that it is our on-premise with a hybrid architecture or moving to one of our full cloud offerings.

### Monetize and Simplify: Accelerate Profitability with Mobility Services Platform - PSOMSI-1000
Speakers: Mike Van Horn (AT&T), Krishna Chirala (Cisco), Amrit Nijjer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959989001zHC3
See how the Cisco Mobility Services Platform enables enterprises and mobile network operators (MNOs) and mobile virtual network operators (MVNOs) to deploy and scale managed 5G services across the enterprise to simplify operations, lower investment risk, and make infrastructure future-ready. This session explores the strategic advantages of Mobility Services Platform, enabling you to rapidly deploy and scale high-value managed digital services, including IoT solutions and public and private 5G-as-a-Service offerings.

### Multi-Cast with EVPN, Segment Routing, and Traffic Engineering - BRKMPL-2123
Speakers: Mankamana Mishra (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271965816001zbmn
Segment Routing (SR) is an industry-standard approach aimed at simplifying transport network, including traffic engineering and management across multiple domains. Ethernet VPN (EVPN) serves as a widely adopted overlay solution for Layer-2 extensions when L3 VPN serves as an overlay solution for IPv4 and IPV6 private services. This session offers a comprehensive exploration of multicast service delivery within EVPN and L3VPN networks. It delves into transport and services multicast delivery methods, covering both distributed protocols Multicast tree computation and controller-based approaches. Additionally, the session will focus on deploying multicast over the SRv6 transport network, providing a clear path forward for integrating multicast in SRv6 environments.

### Multi-Tier Fabrics: Network Designs for the Modern Data Center - BRKDCN-2999
Speakers: Marina Ferreira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892264001zRcH
Have you ever asked yourself what "Clos" is or where that leaf/spine thing comes from? If yes, this is the right session for you. We are going to cover fat-tree, Clos, and leaf/spine designs and expand beyond just the spine layer. We will spend some time on the super-spine and hyperscale plane designs, as well as how you can cost-effectively use 400G/800G and where fixed vs. modular switches make sense. Finally, let's also review self-organized routed fabrics for cloud-native applications.

### Multicast Routing in Nexus 9K NX-OS VXLAN BGP EVPN Data Center Fabrics - BRKDCN-3638
Speakers: Ambrish Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271887127001zZ84
Data centers host servers that host various multicast applications such as collaboration, multimedia, video streaming, conferencing and market data streaming in high frequency trading networks. As video traffic is the highest bandwidth-consuming application in the network, it is imperative to implement architectures that most optimally forward traffic for multicast within the data center for east-west traffic and exiting/entering the data center for north-south traffic to/from external networks. This unique advanced-level session introduces Tenant Routed Multicast (TRM) routing in a VXLAN BGP EVPN fabric. The session will address the following questions: What problem does Tenant Routed Multicast address, and what are its benefits? What are the layers of the VXLAN BGP EVPN TRM network? How do the control and data planes work in a network with TRM configured? What are the ways to deploy RP? It is assumed the audience has a strong background in VXLAN BGP EVPN technology, MP-BGP, and fundamentals in IP multicast routing concepts such as PIM, and IGMP. You will leave this session with an introductory-level understanding of the TRM feature in VXLAN fabrics, applications, and architecture.

### Multicast Solutions for MPLS Networks - BRKMPL-2291
Speakers: Jennifer Valentine (Cisco), Gregory Johnson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966595001zwSn
An extensive analysis of the various technologies and solutions to support Multicast in MPLS networks. Topics will include: Rosen, MLDP, LSM, MVPN (common profiles), P2MP TE, and Segment Routing Tree SID (MPLS data plane). This session will provide detailed overviews of the various solutions, tradeoffs, and where/when each solution is most appropriate. Each solution will be shown with simple and understandable examples that will facilitate attendees' ability to compare and contrast each one. Detailed configuration examples will also be provided for each solution.

### Mythbusting: How to fix improper spam call labels - CNCENS-1013
Speakers: Lauren Brockman (Bandwidth)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271918201001zh6v
Have your business calls been labeled “Spam Risk” or “Scam Likely?” The industry is cracking down on fraudulent calling. But this introduces another problem: tightening restrictions can sometimes impact legitimate businesses with improperly assigned call labels. How do you fix this? Many emerging solutions already advertise a “silver bullet” against any improper call labeling. We’re here to set the record straight and break the tough news—there is no silver bullet. In this session, we’ll discuss the rise of call labeling and debunk common myths. Find out: Where do spam labels come from? Does A-level STIR/SHAKEN attestation stop call labeling? Do branded calling solutions override call labels?

### NOC Panel - BRKNOC-1001
Speakers: Andy Phillips (Cisco), Andrew Gutierrez (Cisco), Scott Neumann (Cisco), Luis Fernando Pastrana Revilla (Cisco), Wentao Fan (Cisco), Aron Donaldson (Cisco), David Twersky (Cisco), Jason Froehlich (Cisco), Allen Clark (Cisco), Benjamin Logan (Cisco), Roney Daniel (NetApp), Kristopher Gabrielsen (Cisco), Richard Furr (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272020194001zkNa
Have you ever wondered what is involved in building and tearing down a network in the span of a week? Our panelist will talk about the CiscoLive! network and the technologies in use, as well as the Network Operations Center that manages it. We'll discuss what worked, leading practices that we followed, and statistics from the event. This is a must-see panel for anyone involved in operating a network, especially one that has to move with agility and adapt constantly. We hope you have more than a few days to build and fine tune your network; but even so, you will benefit from hearing what we did, how we did it and what we learned all over the course of the week. We will have panelists addressing Routing, Switching, Wireless, Network Management, Data Center and Security.

### NXOS Troubleshooting using Nexus Dashboard Insights - BRKDCN-2674
Speakers: Ivan Kovacevic (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271886564001zELB
This session will demonstrate how to troubleshoot Nexus Fabric using NDI's Day 2 ops capabilities. We will demonstrate how these tools fit into your troubleshooting tool belt and show through practical examples how you can use them on a daily basis, with special attention to NetOps/NOC temas. Tired of spending hours and hours on troubleshooting? We're looking forward to meet you and show you a different way.

### Natural Language Processing (NLP) using Python - DEVNET-2160
Speakers: Matt DeNapoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271901536001zhfT
NLP is the subset of AI that interprets human language. In this session, we'll first cover the foundations of NLP and its practical applications in modern networking. In the second half of the session, we'll demonstrate how to get started with NLP using popular Python libraries. This session assumes no prior knowledge of NLP, though basic knowledge of Python is helpful.

### Navigating IoT Connectivity and Managed Services with AT&T and Cisco - CSSIOT-1200
Speakers: Mike Van Horn (AT&T), Doug Robichaux (Cisco), John Wesloski (AT&T Business)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271874112001zut2
Join us for a fireside chat exploring the powerful collaboration between AT&T and Cisco. This is an opportunity to learn how Cisco's IoT Control Center manages over 130 million devices, enhancing services for U.S. enterprises and expanding reach to over 200 countries, while advancing public safety through FirstNet. It will also cover AT&T's comprehensive managed services, which streamline network operations and ensure seamless connectivity across diverse portfolios. This chat offers insights into how these innovations meet the demands of millions of connected devices with efficient service delivery and lifecycle management.

### Navigating the Future of Cybersecurity: AI, Quantum-Resistant Cryptography and Zero Trust - ITLGEN-2055
Speakers: Cindy Green-Ortiz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271956865001zrnX
As IT leaders, the rapid evolution of technology presents both opportunities and challenges. In this session, we will explore the transformative potential of AI in enhancing cybersecurity, the critical role of Zero Trust architecture, and the emerging necessity of quantum-resistant cryptography. AI is revolutionizing cybersecurity by enabling advanced threat detection and response capabilities. However, it also introduces new vulnerabilities, such as adversarial attacks that can compromise AI models. We will discuss strategies to mitigate these risks and leverage AI to prioritize threat hunting and enhance cyber intelligence. Zero Trust architecture is becoming essential in a world where traditional perimeter defenses are no longer sufficient. We will delve into the principles of Zero Trust, emphasizing the importance of verifying every access request and continuously monitoring for threats. With the advent of quantum computing, current cryptographic methods may soon be obsolete. We will explore the development of quantum-resistant cryptography and its implications for securing data in the future. Join us to gain insights into these critical areas and prepare your organization for the next wave of cybersecurity challenges. This session is designed to equip IT leaders with the knowledge and strategies needed to navigate the complex landscape of AI, Zero Trust, and quantum-resistant cryptography.

### NetDevOps with Agentic AI - CNCATO-1015
Speakers: Gayathiri Sreekumar (HCLTech)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271830229001z3Lw
AI-driven operations can streamline troubleshooting, reduce MTTR and enhance operational efficiency. Whether you are a network engineer, DevOps practitioner, or IT leader, this session will provide valuable insights into integrating AI into your network operations toolkit. Experience the future of intelligent networking.

### Network Detection and Response with Cisco Secure Network Analytics - BRKSEC-3019
Speakers: Matthew Robertson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012176001zgcw
This session will explore the visibility and detection capabilities of Secure Network Analytics (Stealthwatch), deep diving into machine learning and the multiple analytic engines in the system including how they work, and how to best leverage the resulting observations to detect and respond to suspicious and malicious activity in the network. Examples of threats detected using the system will be explored as well as how to leverage XDR for extended detection, investigation and response. The target audience for this session are network and security administrators and analysts interested in learning how to best incorporate network detection and response technologies into their security operations centre.

### Network Engineering in the era of Microservices - BRKCLD-2023
Speakers: Jorge Gomez Velasquez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271846338001z7I1
Microservices networking is a crucial aspect of modern software architecture, enabling seamless communication and coordination between microservices in a distributed system. In this session, you will delve into Cilium's powerful traffic management capabilities, including L7 routing and identity-based policing within a Kubernetes cluster. We'll also explore Hubble, a component of Cilium's ecosystem that provides observability — an essential troubleshooting tool for network engineers working with Kubernetes. By the end of this session, you'll have the knowledge and confidence to navigate the dynamic world of Kubernetes microservices, optimizing network performance with Cilium's advanced features. Don't miss this opportunity to upskill and stay ahead in the rapidly evolving landscape of network engineering and microservices!

### Network Simulation as Code with CML and Terraform - DEVNET-2722
Speakers: Ralph Schmieder (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271907143001zYw6
With the introduction of the CML2 Terraform provider, automating a network simulation and driving it via code has never been easier! This session presents Git, Terraform and CML, tying them up nicely to demonstrate a practical and powerful (virtual) "infrastructure as code" approach. At the end of this session, you'll understand how to automate the entire lifecycle of virtual network infrastructure, leveraging Terraform and CML.

### Network Telemetry and AI for Network Incident Response - DEVNET-3707
Speakers: jesus Illescas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271910459001z6p5
In this session, you will learn how to use open source tools and LLM to monitor and react to network incidents. You will see how to develop a solution that collects telemetry data from network devices and applications, and how to use a LLM to analyze the data and help you troubleshoot issues.

### Network as Code - Kick-Start Your Automation with ACI - BRKDCN-2673
Speakers: Daniel Schmidt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271886380001zE0y
Infrastructure-as-Code (IaC) is becoming the prevailing approach to building, managing, and operating infrastructure. In this session, you will learn how to leverage Nexus-as-Code with its easy-to-use, opinionated data model to instantiate Cisco Application Centric Infrastructure (ACI) fabrics in minutes. ACI resources can be defined in human-readable configurations that can be versioned, reused, and shared. Adding CI/CD helps standardize and enforce a change process. All of this provides a solid baseline to develop further automation.

### News and Updates to Webex Security Mechanisms - BRKCOL-2279
Speakers: Marc Dionysius (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853962001zLS7
As organizations rely more on digital collaboration tools, it is crucial to have secure and compliant communication platforms. The presentation will explore the latest changes to the security mechanisms provided by Webex that are specifically designed to fulfil security and privacy requirements and allow you to deliver a robust solution that guarantees both. This session aims to educate customers and partners about news and updates to those mechanisms, as well as the overall security and privacy benefits offered by the most secure collaboration solution available today.

### Next-Gen Customer Experience: Exploring Webex Contact Center's AI Capabilities - CTF-1039
Speakers: Meenakshi Sundaram Kandasamy (Cisco), Joshua Zuke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271863486001zGfP
With the rapid advancements in AI and large language models, we invite you to discover the next generation of Customer Experience AI capabilities embedded within Webex Contact Center. During this session, attendees will gain a comprehensive understanding of all AI features set available within the platform. We will showcase key functionalities such as Webex AI Agents, AutoCSAT, Call-drop Summaries -along with their practical use cases, configuration guidance, implementation best practices, and considerations for effective troubleshooting and data collection. Participants will leave the session with well-rounded knowledge of overall AI feature sets, how to effectively configure, use AI capabilities in Webex Contact Center on demoed features to enhance agent productivity, elevate customer experiences, and streamline support operations.

### Next-Gen Hyperconvergence: Cisco Compute and Nutanix Innovations Unveiled - PSODCN-1011
Speakers: Jeff Mercier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271880783001z7WW
Join this session to learn about new product introductions, innovative AI solutions, and groundbreaking management integrations between Cisco and Nutanix, providing enhanced visibility and insights into the industry's most complete hyperconverged solution. Discover how the latest innovations in the Cisco Compute Hyperconverged with Nutanix solution simplify the purchase, deployment, management, and support of hyperconverged and disaggregated infrastructure.

### Next-Gen Network Monitoring: Using Streaming Telemetry with Splunk - DEVNET-2645
Speakers: Rahul Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833387001zDgu
In modern network management, streaming telemetry is emerging as a powerful alternative to traditional SNMP for real-time monitoring of network devices. This session will explore how to effectively consume and analyse streaming telemetry data using Splunk, a leading platform for data analysis and operational intelligence. Participants will learn the process of ingesting, visualising, and leveraging telemetry data in Splunk to gain deeper insights into their network performance. Whether you're managing a small network or a large-scale infrastructure, streaming telemetry is now a critical component for effective monitoring and troubleshooting of network devices.

### Nexus One: An architecture for your Cisco Datacenter of tomorrow - BRKDCN-2602
Speakers: Max Ardica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271883299001zymK
Cisco Nexus One is a new architecture and technical solution that allows you to integrate your Nexus VXLAN/EVPN fabrics with ACI. Allowing for seamless traffic flow between the two architecture and managed from a single management location that is built with an automation and orchestration focus to simplify your network operations. Join us for this session to introduce you to this new approach which offers scalability, integration and operational efficiency.

### NorthWest Natural Gas Optimizes IT Operations with Nexus Hyperfabric - CSSDCN-1002
Speakers: Majed Alwineyan (Cisco), Bryan Harlow (NorthWest Natural Gas), Brian Boyanovsky (Insight)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271872524001zMNB
In today's rapidly evolving technological landscape, NorthWest Natural Gas is embracing Cisco Nexus Hyperfabric to optimize IT operations, enhance network efficiency, and deliver greater value back to the business faster. By leveraging Hyperfabric's advanced capabilities, NorthWest Natural Gas can respond to business changes in a more agile and adaptive way. This session highlights Cisco's cloud-managed architecture, which simplifies complex tasks and empowers teams of all skill levels to efficiently design, deploy, and monitor their network infrastructure, driving innovation and operational excellence.

### Nutrien's Network Strategy to "Feed the Future" with Wi-Fi 7 and Cisco connectivity solutions - CSSEWN-1100
Speakers: Mark Murray (Nutrien), Brock Richards (Nutrien)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271873340001zZEA
Nutrien, one of the world's largest potash, nitrogen, and phosphate producers for crop fertilizers, operates in vastly different, complex and difficult environments for network connectivity. Nutrien relies on seamless, secure connectivity for business operations and supporting their cloud first strategy. With Cisco connectivity solutions like Wi-Fi 7, Private 5G, Cisco Ultra-Reliable Wireless Backhaul (URWB), powered by Cisco Catalyst Switching and Industrial IoT solutions, Nutrien provides reliable connectivity for: -Mines connecting sensors, works for safety, large equipment in hundreds of miles of underground shafts in an extremely ruggedized environment -Offices connecting business operations and application developers at unprecedented speeds -Rural retail outposts connecting customers and processing orders through cloud-based applications -Manufacturing and production operations connecting critical equipment This session provides firsthand insights into Nutrien's transformative cloud-first journey with Cisco connectivity solutions supported with AIOps. This session will highlight key challenges overcome, current deployment insights and a look into future innovation plans for Nutrien. Participants will gain an understanding of how Cisco connectivity solutions can be deployed in various landscapes and environments to provide secure, ubiquitous connectivity to operations.

### OOB Everywhere! How Advanced Console Servers Enhance Network Automation, Cybersecurity & Resilience - CNCENT-2002
Speakers: Eric Weiss (Lantronix)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271925550001zAa3
For years console servers were just an insurance policy — remote access to gear to save network admins a trip. Today advanced console servers are a necessary extension of network management, providing reliable automation and speeding troubleshooting. Leave this session with ideas for your network, including: Learn how AI-driven out-of-band management can spot issues faster, automatically solve many of the basic problems that take up most of your time and give you the tools you need to fix complicated ones more quickly. See how to bring all your network infrastructure (in the MDF, IDF, data center, everywhere) under the same management umbrella for easier, more secure day-to-day operations. Understand the unique reasons out-of-band management can lock down your network security and help you recover after a breach. See it all in action at the Lantronix stand where We'll be running live demos on real gear.

### ORDR AI for Total Cisco Visibility, Security, and Policy Automation - VILSEC-1041
Speakers: Craig Hyps (ORDR)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271991127001zfuO
Join ORDR as we show how to get the most out of your Cisco network and security investments. ORDR is a next-generation AI-driven cloud platform that seamlessly integrates with multiple Cisco ISE/SDA, DNA/Catalyst Center, Meraki, Firewall, Spaces, and Prime deployments to deliver unparalleled : Asset visibility for all IoT, OT, IoMT, IIoT, IT as well as agentless and unmanaged devices Integrations with 200+ network, security, DC, cloud, asset, SIEM, VA, and EDR vendors Dynamic discovery and classification with rich context infused into your existing Cisco solutions Advanced security insights to automated threat response and remediation workflows Dynamic generation of optimized policies to accelerate segmentation and Zero Trust projects

### ORDR AI: The Fast Track to Cisco Segmentation and Zero Trust - VILSEC-1043
Speakers: Craig Hyps (ORDR)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271991317001zQSF
Join ORDR as we demonstrate how to efficiently achieve your segmentation and Zero Trust goals in record time with Cisco ISE, SDA, Meraki, and Cisco Firewalls. ORDR AI automates endpoint discovery with dynamic classification and risk assessment. Next, ORDR afterburners kick in to dynamically generate and provision segmentation policies and automate threat response. In this session you will learn how to fast track Cisco segmentation projects to: Auto-classify every device on your network with granular detail including IoT, OT, IoMT, IIoT, IT as well as agentless and unmanaged assets Auto-update Cisco ISE with the rich device profiles and context needed to secure every endpoint — including those that lack authentication Auto-group and tag devices in Cisco ISE, Meraki, and Firewalls based on business requirements Auto-assess risk for all devices and dynamically contain threats Streamline device onboarding and 3rd-party integrations with Cisco ISE/SDA, Firewalls, Meraki, Spaces, and more

### OSPF LSA Types Made Simple - CISCOU-2058
Speakers: Peter Paluch (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841390001zy2i
Link State Advertisements (LSAs) are a favourite topic when it comes to discussing Open Shortest Path First (OSPF) details of operation, and deservedly so: Mastering any advanced topic in OSPF depends on mastering LSAs, ranging from profoundly understanding area types, filtering and summarization, network types, through the ability to interpret the link-state database, to truly making OSPF workings crystal clear and intuitive. Have you been through a truly captivating and understandable explanation of LSAs and their types, though? For once, let's explain the LSAs and their types the right way - a way that is illustrative, intuitive, and makes the explanations stick as the LSAs become your second nature!

### OT Security: Splunk + Cisco = Better Together - BRKIOT-1007
Speakers: Chris Duffey (Cisco), Andrew McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271952772001zJQq
In the modern industrial landscape, securing Operational Technology (OT) is crucial for protecting vital assets. This presentation will explore key OT security practices, highlighting the powerful combination of Cisco's Cyber Vision and Splunk working better together to create a defensible architecture and mature cybersecurity program. Cisco Cyber Vision provides comprehensive visibility, monitoring, threat detection, and vulnerability management in industrial environments, and enables segmentation. This data is seamlessly sent to Splunk for further analysis. Splunk's ability to ingest data from any system empowers organizations to achieve comprehensive security across both IT and OT environments. This capability also empowers organizations to correlate and integrate diverse data sources, enhancing the resilience of industrial environments with complete visibility.

### Observability at TorIX: Custom Telemetry Solutions on Next-Gen Campus Switching - CISCOU-1059
Speakers: Jeremy Foran (Blue Flag Consulting), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840452001zIRa
The Toronto Internet Exchange is one of the larger global Internet Exchange Points and a critical interconnection point for many organizations. The in-production telemetry visualization solution includes comprehensive insights into the Enterprise Network using next gen campus switches and the Model Driven Telemetry (MDT) feature. This solution from Blue Flag Consulting translates real business questions into actionable visualizations to help answers questions like "What is the hourly error rate for production switches in San Diego" and "What is the total bandwidth this month for ISP traffic? Topics include configuring telemetry subscriptions and securely sending telemetry data through the telemetry stack: Telegraf, InfluxDB, and Grafana. Join us and elevate your Enterprise Networking with the latest campus switching and explore the vast array of telemetry capabilities and visualization insights!

### Observing GenAI-Infrastructure: You Can't Protect What You Can't See - DEVNET-3310
Speakers: Shannon McFarland (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271910070001z3LN
In this ultra-fast-paced world of AI and Cloud Native, knowing what is running, where, and what it is doing is challenging. Managing and protecting workloads is incredibly difficult if you can't see what is happening. In this technical session, discover how open source projects like OpenTelemetry, Cilium with eBPF, Tetragon, and others can enhance observability and security for Generative AI (GenAI) infrastructure like Agents. Through practical demonstrations, attendees will gain actionable knowledge on deploying these tools to ensure GenAI workloads are both performant and secure.

### Observing and Validating Multi-Agent LLMs in the Wild: You Can't Fix What You Can't See - PSOETI-1112
Speakers: Tushar Agrawal (Cisco), Mayank Gupta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271914326001zA2t
Multi-agent LLM applications fail on up to 65 % of real-world tasks because their logs are fragmented and their success metrics undefined. Current tracing tools are single-agent-centric, leaving engineers to hand-stitch data, debug for weeks, and battle stalled compliance reviews. We introduce MAS-Schema 1.0 and the Open Source SDK — a lightweight, framework-agnostic stack that turns raw telemetry from LangChain, Llama Index, AutoGen, or custom code into audit-ready insights. A translator normalizes events into the schema, a recomposition engine rebuilds execution graphs, and a compute module outputs Observability metrics along with Eval metrics.

### Offices that Everyone Loves: Smart Tech for Inclusive Spaces - PP-1307
Speakers: Stephen Brown (IWBI - International WELL Building Institute), Christian Bigsby (Cisco Systems, Inc.), Brian Tippens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271948830001zm4g
Wondering how to make your office a place where everyone feels welcome and productive? Join Cisco's experts in real estate and in social impact & inclusion to see how Cisco blends cutting-edge tech with design to meet the needs of Today's workforce. We'll share real-life examples of Cisco offices, demonstrating how to create spaces that spark innovation and collaboration while being mindful of accessibility, personal preferences, and wellbeing. Leave with practical tips on using technology to boost comfort and productivity, helping you create a workplace that's ready for the future. Register and stay for "(PP-1313) Virtual Tour: Tech & Sustainability in Cisco's Modern Offices" immediately following this session. you'll get a chance to step into the future of work with a virtual tour of one of Cisco's cutting-edge offices, where technology and energy efficiency come together to create the ultimate modern workplace.

### Open-Source GenAI Bot for Catalyst Center - DEVNET-3000
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271909098001z0hm
Are you looking to simplify network management using Cisco Catalyst Center REST APIs and Generative AI, to transform your existing network automation Apps? Participants will learn how to develop a Cisco Catalyst Center open-source AI ChatBot. We will step-by-step build the AI platform, reviewing the options to use real-time or near-real time datasets, retrieved with API calls to Catalyst Center. We will review different LLM models and data transformers and find one that meets your technical requirements and enterprise policies. The ChatBot allows network engineers to easily find relevant information using natural language, filtering only what is important. The GenAI open-source Bot will transform how we manage network infrastructure, enriching and simplifying network management tasks. The attendees will receive the Python open-source code for a complete AI system, that may be used in their labs for future testing and development.

### OpenRoaming Under the Hood - BRKEWN-2037
Speakers: Bart Brinckman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271938662001zxfw
OpenRoaming enables an automatic and secure Wi-Fi experience for everyone, everywhere. After this session, you will have a full understanding of how OpenRoaming works and how to configure it in your network. We will cover the following topics in detail: - Understanding how OpenRoaming works under the hood, from the automatic Wi-Fi network discovery to the secure federation of network providers and identity providers that enable global scalability - Configuring OpenRoaming on Catalyst and Meraki, exploring all the options, and understanding and resolving common issues - Leveraging your Wi-Fi network for indoor coverage for Mobile Service Provider users - Becoming an identity provider (IdP) with Cisco Spaces SDK

### Opening Keynote: Vision for the Future - KEYGEN-1001
Speakers: Chuck Robbins (Cisco), Jeetu Patel (Cisco), Carrie Palin (Cisco), DJ Sampath (Cisco), Kevin Weil (OpenAI), Alan Rosa (CVS Health)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1748956425634001aGnQ
In this can't-miss keynote, hear from Chair and CEO, Chuck Robbins, Chief Product Officer, Jeetu Patel, and other leaders as they unveil ground-breaking innovations to connect and protect all aspects of your organization in the AI era. AI-ready data centers. Future-proofed workplaces. Unparalleled digital resilience. It all happens at Cisco Live 2025.

### Operational AI: Practical Application of GenAI in the Stack - CENDEV-1997
Speakers: Shannon McFarland (Cisco), Matt DeNapoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592614572001XcmB
This technical presentation examines how Generative AI (GenAI) can be leveraged to accelerate automation adoption in IT and developer operations. We first will investigate how GenAI can be used the lower the barrier to entry for organizations looking to employ automation in their infrastructure management. Then we will move "up the stack" and see how cloud native application architectures can take advantage of agentic frameworks to optimize deployments and mitigate issues. The focus will be on GenAI's role in advancing automation, streamlining CI/CD processes, and its emerging function in predictive analytics for operational efficiency. Attendees will gain insights into GenAI's practical applications, implications for infrastructure as code (IaC), and the future of collaborative human-AI development environments. The session aims to equip technical professionals with a clear understanding of GenAI's impact on their field and actionable knowledge on leveraging these advancements within their practices.

### Operational best practices to deploy and Manage Cisco Compute Hyperconverged with Nutanix clusters - BRKCOM-1111
Speakers: Ana Montenegro (Cisco), Brian Everitt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271861375001zMKa
Considering an CCHN cluster deployment but unsure which flavor to choose and how to deploy and manage your cluster? This session is designed to guide you through the essentials, helping you choose the right type of cluster depending on your business needs. Attendees will gain insights into the best practices for installing the cluster and day-two operations such as expansion and upgrades will gain the knowledge needed to ensure the CCHN cluster is efficient, scalable, and manageable from Intersight.

### Operationalizing AI for Contact Center: Best Practices & Responsible AI - BRKCCT-1514
Speakers: Keith Griffin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271864479001zUMo
As artificial intelligence continues to revolutionize customer experience, integrating AI technologies into your contact center can be both a game-changer and a challenge. This session provides a comprehensive guide to operationalizing AI effectively, including best practices for AI implementation, data security protocols, and techniques for fostering a culture of innovation while maintaining compliance.

### Optical Networking Fundamentals - BRKOPT-1007
Speakers: Kent Dailey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967367001zUKu
Are you intimidated by high-capacity optical networks and want to understand how they are applicable in your network? In this session, we will explore the core components of DWDM (Dense Wavelength Division Multiplexing) systems and demonstrate how high-speed coherent optics can help meet your bandwidth and networking needs. We'll also highlight Cisco's Optical Networking solutions, including the Cisco NCS 1000 Product Families, which offer scalable, high-performance, and flexible optical transport. Discover how Cisco's innovative optical technologies can simplify your network operations and provide seamless scalability to accommodate growing data demands.

### Optimizing ACI Data Center with AI-Powered Infrastructure as Code - AIHUB-2010
Speakers: Nandakumar Arunachalam (Cisco), Samuel Mendenhall (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271877231001z3jg
Explore the dynamic fusion of Infrastructure as Code (IAC) and AI, designed to expedite the adoption in Application Centric Infrastructure (ACI) in data center environments. You will delve into real-world examples through live demonstrations where AI augments IAC including provisioning, declarative configuration changes, and day-to-day administration. Leaving this session, you will have a clear picture of how the combination of AI and IAC can increase productivity, and reduce risk in your data centers. Join us for a grounded exploration of how Cisco ACI and AI can revolutionize infrastructure automation without compromising credibility.

### Optimizing AI-Ready WAN Infrastructure with Microsoft and Cisco - CSSENT-2100
Speakers: Sarav Subramanian (Microsoft), Ruben Lopes da Fonte (Cisco), Gaisin Rustam (Microsoft)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1758668928353001AbVz
Join Microsoft and Cisco to learn how AI-ready infrastructure is being developed in Azure WAN using RDMA (Remote Direct Memory Access) for enhanced network performance. RDMA provides high throughput, low latency, and lossless data transfers with minimal CPU load. They will share strategies for managing congestion using techniques like Priority Flow Control and Explicit Congestion Notification to tackle oversubscription and microbursts, ensuring smooth data flow. It is an opportunity to hear insights into the challenges and innovations as Microsoft and Cisco advance AI network infrastructure to meet future needs.

### Optimizing Edge Infrastructure with Intersight: Deploy, Manage and Monitor Compute at Scale - BRKCOM-2023
Speakers: Eric Williams (Cisco), Mansi Garg (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271859877001zIVs
In Today's cloud and AI era, it is imperative for businesses to have the ability to quickly, efficiently and securely deploy and manage their infrastructure anywhere and everywhere. This session explores best practices and provides a comprehensive approach for managing edge infrastructure at scale with Intersight. Learn how it simplifies onboarding, automates lifecycle operations, and improves visibility across locations. With Intersight, businesses can ensure consistent workloads, secure infrastructure and reduce downtime, allowing teams to focus on delivering exceptional customer value.

### Optimizing Security and Agility: Leveraging SD-WAN Capabilities in Cisco Secure Firewall Threat Defense - BRKSEC-2086
Speakers: Alejandra Paez Castro (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272006630001zufB
Struggling with complex branch connectivity and security across distributed organizations? Discover how Cisco Secure Firewall Threat Defense SD-WAN capabilities enable both robust security and agility. This session dives into practical solutions for branch connectivity, demonstrating secure routing of application traffic directly to the internet (DIA), intelligent selection of optimal egress paths based on real-time link metrics, simplified branch-to-hub communication using DVTI and the new features introduced in firewall version 7.6, SD-WAN Wizard (for simplified deployments and routing configurations of VPN topologies) and Device Templates (for provisioning of branch devices with pre-provisioned configurations). Through insightful demo, attendees will gain a clear understanding of how these features work in action.

### Optimizing Troubleshooting Efficiency with AI and Splunk Observability - BRKOBS-2009
Speakers: Isha Gandhi (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271980916001zHHR
As modern IT environments grow increasingly complex, the need for efficient troubleshooting solutions has become paramount. Traditional manual methods of diagnosing and resolving system issues are often time-consuming, error-prone, and insufficient for real-time problem resolution. Join us to learn how Artificial Intelligence (AI) with Splunk Observability helps optimize troubleshooting processes and significantly enhance operational efficiency. In particular, we plan to focus on how Splunk's observability, powered by machine learning and advanced analytics, can detect issues faster across infrastructure, applications, and networks; and can help identify the root cause quickly. One would learn key features such as anomaly detection, intelligent alerting, and auto-remediation workflows in detail. This session will provide both technical and strategic insights for practitioners looking to leverage AI in Splunk Observability to enhance troubleshooting workflows and improve overall system reliability.

### Outliers That Matter: Turning Noise into Strategy - CTF-1043
Speakers: Deepti Bhutani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271984815001zOZa
Outliers are often seen as statistical noise—exceptions to be filtered out. But in high-performing organizations, these anomalies are becoming a strategic asset. This session uncovers how outlier detection, powered by modern observability and AI-driven analytics, can surface hidden issues, predict failures, and uncover business-critical insights.Discover how shifting your perspective from filtering out anomalies to embracing them can reshape your strategy.

### Outsmart identity attacks - PSOSEC-1028
Speakers: Prabhu Barathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271995784001zxxk
In 2024, identity attacks emerged as a predominant threat, as highlighted in the Talos Year in Review report. Threat actors increasingly leveraged identity-based attacks, favoring simple login methods over complex techniques like exploiting vulnerabilities or deploying malware. This session will explore the challenges in adopting phishing-resistant MFA techniques, such as passwordless authentication, which promise enhanced security but face significant implementation hurdles across diverse workforces. We will delve into the complexities of deployment and security vulnerabilities within key workflows. After examining the challenges, the session will propose a comprehensive approach to achieving end-to-end phishing resistance. This includes not only the authentication process but also enrollment, fallback procedures, and help desk interactions. Attendees will gain insights into practical solutions that expand deployment possibilities and strengthen every aspect of authentication against sophisticated identity-based threats.

### Over-Ruled: Under the Hood of the Cisco Secure Access Rules API - DEVNET-2255
Speakers: Yaron Caspy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271902290001zWAO
What's in an Access Policy? The Secure Access Rules API includes an incredibly powerful set of REST API endpoints. In this session, we will look at the different objects which make up an Access Policy Rule, understand how they can be put together, and look at use case implementation. Bring your use cases as we take a look at how you can programmatically accomplish them.

### Overlay Multicast in SDA: Effortless Deployment for multicast-based Applications - TACENT-2028
Speakers: Ivan Lagunes (Cisco), Vineetha Potu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271930362001zD0M
In today's rapidly evolving network landscapes, deploying overlay multicast in Software-Defined Access (SDA) environments has become essential for efficient data distribution. This session offers a comprehensive exploration of the dependencies and requirements necessary for successful implementation and deployment of overlay multicast solutions. Participants will gain valuable insights into the two distinct flavors of multicast: Headend replication and native multicast, understanding their unique advantages and applications. Additionally, the session will elucidate the differences and diverse applications of Layer 2 flooding versus overlay multicast, empowering attendees to make informed decisions on deploying applications such as Dante, IPTV, mDNS, and BACnet. Join us to enhance your expertise and ensure your multicast strategies are optimized for current and future networking demands. This is an invaluable opportunity for professionals seeking to elevate their network deployment capabilities.

### Packet Buddy - Chatting with your PCAPs, via the Cloud or Locally on Your Own Machine! - AIHUB-2000
Speakers: Dave Zacks (Cisco), Prapanch Ramamoorthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271926126001z8AP
This session will showcase a fun and innovative solution that allows attendees to chat, via a variety of Large Language Models (LLMs), with their own Wireshark packet captures. Ask the LLM what kind of traffic you have - what errors it sees - or use it to delve into and understand packets and packet flows better! The choice is yours. This engaging and entertaining session is hosted by the dynamic duo of Prapanch Ramamoorthy and Dave Zacks, both Cisco Live Distinguished Speakers as well as enthusiasts for AI and it's use in network, security, and analytics applications. Prapanch and Dave will show you what this capability can do, and more importantly, how you can set it up and use it in your own deployments. Come to this fun, interactive session to see how using our open-source "PACKET BUDDY" solution can get an LLM chatting with your own packet captures!

### Packet Journey inside Catalyst 9000 Switches - BRKARC-2100
Speakers: Jaroslaw Gawron (Cisco), Ivan Shirshin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271917024001z5NT
The Catalyst 9000 series is the backbone of modern enterprise networks, supporting everything from traditional campus deployments to advanced SDA and EVPN overlays. To ensure seamless performance and effective troubleshooting, network engineers need a clear understanding of packet forwarding—both at the hardware and control plane levels—and the right tools to analyze network behavior. In this session, We'll demystify packet flow analysis by introducing key IOS-XE diagnostic tools that help verify the actual forwarding path of a packet and confirm how the switch processes different types of traffic. you'll gain hands-on insights into: - Capturing live packet flows for in-depth analysis - Understanding data-plane forwarding decisions - Examining control-plane traffic Whether you're troubleshooting complex networking issues or performing routine maintenance, these tools will elevate your troubleshooting skills and help you resolve challenges with confidence.

### Packets in Space: Networking for the Final Frontier - CISCOU-1057
Speakers: Lexie Cooper (Blue Origin), Eric Peterson (Blue Origin), Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840075001zf1I
Networking on Earth is hard enough—but what happens when your infrastructure is moving at thousands of miles per hour, facing extreme conditions, and failure isn't an option? This moderated Q&A with two —rocket network engineers— explores the challenges of designing mission-critical networks for rockets and spacecraft, from ensuring real-time telemetry to handling wildly low latency requirements. Learn how traditional networking prin're a long-time network engineer or just space-curious, get ready for a dive into the most extreme environment for networking: the final frontier.

### Paving the path for Autonomous Network Planning using APIs and AI Agents - DEVNET-2302
Speakers: Julia Palomino (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271903621001zIYw
The purpose of this session is to provide an update on the powerful Predictive-AI tools of Crosswork Planning. We will also discuss the features of its extensible and flexible Network Model, which serves as the foundation for AIOps. In addition, we will dive into the Crosswork Planning python-based API libraries that aid in automating the extensibility and execution of simulation tools. This includes an overview of the new Crosswork Planning SDK component. Lastly, we will walk you through the workflow and provide a demonstration of how Crosswork Planning and AI Agents can be integrated to automate various planning scenarios. This will showcase the agent's ability to reason and respond upon user requests.

### Pest Control! Catching bugs and vulnerabilities in your network's foundation. - CTF-1041
Speakers: Andrew Dunsmoor (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271984619001zDgC
What's hiding in your basement? Undiscovered bugs are a leading cause of unplanned network downtime. Meanwhile, software vulnerabilities represent an unaccounted risk in most enterprise environments. Diagnosing your network's exposure to disclosed software bugs and vulnerabilities can be a laborious task that is often neglected. This session demonstrates how Catalyst Center can provide regularly scheduled "home inspections" so that network teams can make informed decisions about when to patch or upgrade their network device software.

### Pig-in-the-Middle - TLS Decryption and Encrypted Visibility Engine Deep Dive on Cisco Secure Firewall - BRKSEC-3320
Speakers: Christopher Grabowski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272013550001zkig
Join this engaging and insightful Breakout Session that delves into the core concepts of TLS/QUIC decryption and the Encrypted Visibility Engine on Cisco Secure Firewall. - Curious to see a real malware sample intercepted by the Encrypted Visibility Engine? - Want to grasp TLS 1.3 and QUIC function, and how your firewall can decrypt these protocols? - Eager to learn the step-by-step process of how firewalls decrypt TLS and QUIC, and how to formulate a secure, manageable decryption policy? - Heard about the upcoming challenges with QUIC and interested in how a machine-learning-based Encrypted Visibility Engine can help? - Enjoy interactive demos, quizzes, and polls? - Interested to hear about the latest enhancements in crypto toolbox of Cisco Secure Firewall? If you answered yes to any of these questions, join this session to elevate your technical knowledge and enhance your cryptography skills.

### Planning and Designing Successful Cloud Calling Deployments with Webex Calling - BRKCOL-2787
Speakers: Johannes Krohn (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271854528001z4vn
Customers and Partners considering a cloud calling deployment based on Webex Calling need to tackle a number of decisions including PSTN selection, location planning, dial plan design, call routing, integrations with existing call control systems and mapping business requirements to Webex Calling features. In this session, the participants will get guidance on all of the above and, in addition, in this session some of the latest features of Webex Calling are covered. This session does not cover Webex Calling dedicated instance.

### Platform Engineering: Building Golden Paths for Modern Applications using Cisco Technologies - BRKCLD-2226
Speakers: Jara Osterfeld (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271847102001z5dW
Platform engineering and Spotify's "golden paths" are the new kids on the block. We talked DevOps, we talked SRE, and now we talk platform engineering. Why? Because managing modern application environments is complex, and the more solutions we find, the more challenges seem to arise. In this session, we will take a closer look at what platform engineering is, and build golden paths for deploying and maintaining VMs, Kubernetes clusters, and Generative AI applications. The focus of this session is on building a toolchain and workflow using Cisco and open-source technologies with the goal to deliver standardized services and to create a first set of opinionated best practices for application developers to consume enterprise-managed cloud infrastructure.

### Power Security Operations with Cisco XDR - PSOSEC-1029
Speakers: Sri Karnam (Cisco), Calvin Chai (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271995978001z7IM
Whether you are an IT leader with security response on your long list of duties, a network security engineer getting blindsided by incidents originating outside of your control, or running a SOC that just can't keep up, the Cisco XDR team has been innovating and building to your use cases. In this session, we'll review how we're adapting to the constantly shifting threat landscape, catch you up on the latest updates, and give insights into where we see the platform going as we integrate with the world's leading security operations solution.

### Power of the Platforms: Bridging It All Together with Cisco Collaboration Cross Architecture Integrations - BRKXAR-2021
Speakers: Rafat Kuraishi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271867951001zO5v
In today's cloud-native landscape, organizations consistently operate within hybrid environments, prioritizing optimal user experiences. This session will explore how cross-architecture integrations with Cisco Control Hub can achieve operational excellence . Participants will discover how five distinct platforms Meraki, ThousandEyes, Cisco Spaces, Cisco Secure Client, and Splunk integrate with Cisco Control Hub to deliver real-time workspace utilization, comprehensive network path observability and assurance, and the capability to process structured and unstructured data for insightful dashboard creation.

### Power the SOC of the Future with Splunk - CENSEC-1201
Speakers: Keith Keimig (Regeneron Pharmaceuticals, Inc.), Tony Paterra (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749748037962001fnOq
Learn how to supercharge your security operations by combining the power of Splunk and Cisco. This session will show you how to streamline threat detection, investigation and response, empowering your team with automated workflows to stop lateral movement in the network. Discover how to leverage Splunk's powerful analytics and data management capabilities and Cisco's network visibility to enable faster, more efficient investigations and responses.

### Power the SOC of the Future with Splunk Security and Cisco - BRKSEC-2800
Speakers: David Dalling (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271983472001z5a2
Learn how to supercharge your security operations by combining the power of Splunk Security and Cisco. This session talk will show you how to streamline threat detection, investigation and response, empowering your team with automated workflows to stop lateral movement in the network. Discover how to leverage Splunk's powerful analytics and data management capabilities and Cisco's network visibility to enable faster, more efficient investigations and responses, giving your security operations the agility needed to stay ahead of evolving threats. If you're ready to enhance your security team's capabilities and elevate your organization's security posture, this session is for you.

### Powering Autonomous Networks: AI, Observability, and the Future of Connectivity - CENSPG-1017
Speakers: Jason Teller (Cisco), Gurudatt Shenoy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592613282001XxG5
As organizations navigate the next era of AI and digital transformation, they are faced with increasing pressure to streamline network operations while meeting the growing demand for higher performance, security, scalability, and AI use cases. This session will explore the critical role of network simplicity in addressing the complexities of modern infrastructure. With AI as the driving force, we'll showcase how AI-powered automation, assurance, and observability enable enhanced visibility and faster, data-driven decision making leading to self-optimizing, autonomous networks. Combined with that, we'll spotlight Cisco innovations around multi-agentic AI frameworks, predictive and prescriptive AI analytics, and cross-domain data-intelligence that help accelerate network simplicity, enhance digital resiliency, and drive strong network autonomy. Together with our customers, we'll demonstrate how these technologies are not only transforming operational models but also setting the stage for next-gen secure global connectivity.

### Powering the AI-Ready Data Center: Secure, Scalable Infrastructure to Accelerate Innovation - KDDDCN-1000
Speakers: shawn jaacks (DSU), Jeremy Foster (Cisco), Gurudatt Shenoy (Cisco), Michael Israel (New England Patriots/Kraft Sports & Entertainment), Kevin Wollenweber (Cisco), Cameron Ferdinands (Groq), Tom Gillis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749591953476001ppJC
We're in an unprecedented era of innovation, where AI, cloud computing, IoT, and digital streaming are redefining what's possible while pushing networks to deliver greater bandwidth, scalability, and agility than ever before. In this session, discover how Cisco's AI-ready infrastructure and full-stack solutions are transforming the way service providers and enterprises connect and scale. Learn how you can build seamless, secure and AI-ready data centers that can turn challenges into strategic advantages. Cisco infrastructure is built not just for AI, but for everything your business needs to succeed in this bold new era of connectivity.

### Powering the Secure WAN of the Future with Cisco 8000 Series Secure Router - BRKXAR-2027
Speakers: Jason Yang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271870627001zLS0
Cisco Secure WAN is leading the way in WAN transformation, where security and networking converge. This session will introduce Cisco 8000 Series Secure Router and explain how it builds a strong foundation for the Cisco Secure WAN architecture. We will discuss the key innovations and distinct advantages of Cisco 8000 Series Secure Router, how they directly benefit your use cases and deployments, and we will also cover product migration.

### Practical LEOsat Deployments - Technologies Use Cases and Outcomes - BRKNWT-2505
Speakers: Kemal Sanjta (Cisco), Dave Zacks (Cisco), Ian Procyk (Cisco), Oliver Boehmer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973885001zygZ
Low Earth Orbit satellite constellations have revolutionized network deployment options, enabling connectivity to any point globally with high-bandwidth, low-latency, and excellent reliability. Have you looked at LEOsats and wondered how they can be leveraged in your own network designs? If so, this is the session for you! In this session, we will explore practical, real-world examples of LEOsat deployments — the good, the bad, the (sometimes) ugly, and the hard-won lessons along the way from design to employment and ongoing use. We will also explore some of the leading-edge research in this space (no pun intended!) and showcase how your own LEOsat deployments can be optimized, using a variety of Cisco SD-WAN technologies as well as host-based enhancements and controls. Presenting this session is the dynamic duo of Oliver Boehmer and Dave Zacks — both Cisco engineers with a passion for all things space-related! Come to this fast-paced, fun, and interactive session to hear the latest breaking news in LEOsat deployment options, and see how LEOsat technologies, along with the latest Cisco enhancements, can play a key role in your current and future network deployments!

### Preparation Guide to Emergency Comms and Networking using Amateur Radios (HAM) - BRKGEN-1012
Speakers: Jimmy Alignay (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271945461001zSe2
This session delves into the transformative role of packet radio in the evolution of IP networking and its enduring relevance in the amateur radio community. We begin by exploring the creation of packet switching, originating from ALOHANET,ARPANET to the modern Internet. What happens when you can't leave your family, there are no roads, no cell, no water, no power, and you need help from first responders in the area. We examine the critical role of emergency communications (EMCOMM) with the use of amateur radio to Cisco networking. Share use cases from recent hurricanes Helene/Milton 2024, emphasizing when a disaster hits foundational communication channels are needed to bring up Network Operations and services. We will share tactical deployments to real-world success stories, this section underscores the importance of integrating amateur radio with networking technologies for public safety. The technical innovations behind IP networking over packet radio are then explored, showcasing how amateur radio operators have embraced and contributed to the field of network engineering. Finally, we turn to modern amateur radio and Cisco networking, outlining how newcomers can start, and examine practical applications of Layer 2 and Layer 3 technologies based on the OSI Model. This segment offers use cases and other alternative network communications integrate with Meraki and Cisco route switch along side Starlink and linking other CLUS sessions eg. NERV Truck.

### Prepare for DevNet Associate with CI/CD and GitHub Actions - BRKCRT-1005
Speakers: Kourtney Barnes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271834135001zAa8
Tired of repeating the same build, test, and deploy steps? Let's get into "action" to go from hours to minutes with on-demand CI/CD. Provisioning and managing tools like Jenkins, GitLab, and AWS CodeDeploy can become overwhelming and take developers away from doing what they love, CODE! In this session, we will discuss how GitHub and GitHub Actions can tackle CI/CD without moving away from your codebase in GitHub repositories. You'll learn key differences between GitHub Actions and other popular CI/CD tools to determine if this tool is the best fit for your needs. You'll get to witness how utilizing Git and the widely used YAML syntax, can build out pipelines to perform those repetitive tasks and eliminate copy and paste errors. This session will help prepare you for the DevNet Associate and DevNet Professional Exams!

### Prepare for the Enterprise Automation (ENAUTO) Certification - BRKCRT-2014
Speakers: Quinn Snyder (Cisco), George Koukis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271834709001zY6R
Are you preparing for your Enterprise Automation Specialist Certification? The ENAUTO certification prepares you for implementing Enterprise automated solutions, including programming concepts, Python programming, APIs, controllers, and automation tools. Led by the Exam Program Manager Leader and a Technical Advocate; this Technical Breakout session will provide you with guidance on the ENAUTO blueprint, what areas to focus on when preparing for the ENAUTO exam, as well as show you sample questions and preparation tips. We will focus on key design principles, technologies, and concepts essential for successfully completing the certification.

### Preparing for AI-Ready Infrastructure with Silicon One - ITLGEN-2065
Speakers: Martin Lund (Cisco), Eric Knipp (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271957639001zrbG
AI is having a transformative impact across industries and will inform nearly everything we do in the coming years. Over 80% of organizations plan to implement AI within the next two years. Are you ready? Martin Lund and Eric Knipp will talk about the value of AI-ready infrastructure for organizations, how Silicon One helps unlock AI capabilities across the IT stack, and why performance and flexibility are key to mastering AI readiness. This session will reach far beyond GPUs and servers to look at the capabilities that AI can deliver when we expand from the data center to the edge of the network and beyond. you'll leave understanding the role AI-ready infrastructure and silicon plays in your IT investments and how to navigate AI strategy decisions for the future.

### Preparing for Global Mega Sporting Events - CSSGEN-1010
Speakers: Tim Lake (Cisco), Franz Regul (Bpifrance), Teri Takai (eRepublic), Kamal Sadarangani (LA28)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271873536001zczk
As the world reflects on the success of mega events and looks forward to LA28, this fireside chat will feature former and current leaders from the Olympic and Paralympic Games. The discussion will highlight key lessons learned, Smart City initiatives, and the role of innovative technologies in transforming host cities. Leaders will also emphasize the importance of partnerships with cities and venues to deliver world-class experiences and generate global excitement. Attendees will gain insights into how past games and Los Angeles are driving innovation and collaboration to create impactful, world-class events for athletes, attendees, and global audiences alike.

### Public Key Cryptography - From RSA and EC to Post-Quantum - BRKSEC-3129
Speakers: Frederic Detienne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272013147001zIx9
In this session, we will explain how public key cryptography works, what are the challenges posed by quantum computers and, ultimately, we will look into quantum-resistant algorithms. This session is industry-level. We will not focus on a specific type of product or application - instead, this is a general culture session meant to offer a solid basis into the jargon and technicalities of cryptography. The type of knowledge needed to take good decisions (or to delay decisions). Expect some maths to be displayed but mostly expect a lot of fun and enlightenment.

### QKD Impact on Optical System and PQC Solution - BRKOPT-3086
Speakers: Maurizio Gazzola (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915852001zFgK
The coming of Quantum Computing is placing a threat to current PPK implementation. Market is offering Quantum key Distribution as a possible solution. This breakout will show what are the implications for an optical transport network to Host Quantum Channels. We will also provide an overview about Cisco strategy focused on PQC.

### Quantum Networking: How Cisco is Building Tomorrow's Infrastructure, Today - BRKETI-2009
Speakers: Reza Nejabati (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915278001zpFn
In this presentation, you'll get a primer on Cisco's vision and strategic approach to developing practical quantum networking solutions. Specifically, we will explore how Cisco's quantum networking technology serves as a foundational fabric for quantum data centers, paving the way toward scalable quantum computing capable of solving complex problems beyond classical systems. Additionally, We'll walk through Cisco's research and development roadmap in quantum networking, highlighting significant milestones in hardware innovation, specialized components, and advanced software technologies tailored for quantum networks. The session will also include demonstrations of hardware prototypes and showcase the operational capabilities of Cisco's quantum network control software and simulation platform, giving you a glimpse into your future Quantum networking design.

### Quantum Safe Cryptography (and why you need it) - BRKSEC-2175
Speakers: Craig Hill (Cisco), Andrew Benhase (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001573001zfA7
This session will be an introduction for customers who need to learn about Quantum Resistance, Readiness, and ultimately a Quantum Safe network that protects their data in transit. We will show the customer what their path looks like for how to achieve a future implementation of Post Quantum algorithms for their existing IKEv2/IPSEC, and TLS 1.3 based operations, including what they can do today to meet readiness mandates.

### RADKit: Automate your network securely and efficiently - BRKOPS-3065
Speakers: Frederic Detienne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271990163001zWtg
RADKit is the new Cisco SDK used by Cisco Customer Experience (CX), including TAC and Professional Services, to securely and remotely manage or troubleshoot any type of device class (Data Center, Security, Collaboration, Enterprise or Service Provider). With RADKit, you can manually and programmatically address your network through SSH, REST APIs, NETCONF/YANG, SNMP, web UIs, remote desktop, and more. In this session, we will introduce RADKit in depth: its architecture, security features, user interface, CLI, and API. Learn about RADKit, and use it for yourself or to effortlessly expedite your TAC Service Requests. Slideware will be reduced to the minimum necessary, and numerous live demonstrations will be provided. We will code on stage. These examples will help you understand the span of control of RADKit, its ability to tap into almost any data source, and how it can empower your network operations teams through automation and ready-made procedures. Multiple practical use cases will be shown, covering day-to-day management, troubleshooting, and remediation.

### Red Hat and Cisco: Accelerating modernization together in the AI era - CNCATO-1014
Speakers: Sean Cavanaugh (Red Hat)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271830947001zN0k
Many organizations are balancing IT operational priorities such as effectively managing networks to the edge, and implementing new virtualization strategies without disruption—all while you stand up new, ground-breaking AI or AIOps solutions. By combining versatile Red Hat automation and application platforms with Cisco network, compute and edge solutions, you can stay resilient while you implement next-generation solutions. Hear how Ansible Automation Platform can help you meet AI or AIOps goals, including with Splunk. See how we together offer a better approach to managing virtualization, and how you can automate operations to the edge. Red Hat and Cisco are ready to help you in this changing IT landscape.

### Redefine your AI/ML networks with Cisco Silicon One - AIHUB-1004
Speakers: Ramesh Sivakolundu (Cisco), Yaron Agami (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271876631001zOB1
The network that many organizations have used in the past for high-performance computing (HPC) cannot scale to meet the demands of AI/ML. As an industry, we must evolve our thinking and build a scalable and sustainable network for AI/ML. Cisco Silicon One is helping the industry meet rapid large-scale buildouts of AI/ML that networks. Power your AI/ML networks and configure the network to deploy standard Ethernet, enhanced Ethernet, or scheduled Ethernet to achieve best-in-class characteristics for each use case.

### Redefine your AI/ML networks with Cisco Silicon One - PSODCN-1005
Speakers: Ramesh Sivakolundu (Cisco), Yaron Agami (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879785001z9UT
Discover how Cisco Silicon One advances AI/ML networks with its innovative silicon architecture. This session will introduce Cisco Silicon One, delve into its role as the foundation of AI/ML clusters, and highlight Cisco's unique contributions to these networks. Learn about the differentiators that set Cisco Silicon One apart, including its superior bandwidth, low latency, and energy efficiency, all tailored to meet the demanding needs of AI/ML applications.

### Redefining Wi-Fi to Deliver Near-zero Latency and Uninterrupted Roaming - PSOIOT-1020
Speakers: Andrea Orioli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271951768001zP4z
Join us to discover how we are pioneering a new era of wireless connectivity, redefining Wi-Fi to be not just fast, but ultra-reliable, with near-zero latency (<10ms), seamless handoffs, and uninterrupted service. Our solution doesn't just improve Wi-Fi - it reinvents it as the foundation for the future of industrial and business-critical wireless connectivity. By eliminating reliability concerns, Cisco expands Wi-Fi's role beyond offices and homes into factories, smart cities, and autonomous operations.

### Reduce downtime & accelerate investigations with AI for Observability - BRKOBS-1024
Speakers: Annette Sheppard (Cisco), Sahinaz Safari (Splunk / Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271982113001zpgm
Have you ever spent hours triaging an incident in a high-pressure situation? Consider the cost — not just in effort but critical downtime for your customers. Every minute saved reduces stress and restores service faster. Discover how the AI in Observability, can streamline your detection and triage and significantly reduce the mean time to detect and resolve an issue. Join us to learn how you can transform your observability practice with AI.

### Reduce risk without compromising application delivery and workflow efficiency - PSOOBS-1113
Speakers: Douw Steyn (Cisco), Kashyap Merchant (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977009001zLQ2
Businesses compete in a dynamic landscape as applications become increasingly complex, cloud technologies accelerate development cycles, and security threats grow daily. Safeguarding applications against malicious threats is crucial but can slow innovation and complicate workflows. Secure Application provides a ready-made solution leveraging your existing Splunk AppDynamics APM agents to protect against evolving cyber threats while operating faster. Join us to discover how Secure Application automatically detects and blocks incidents at runtime, delivers crucial visibility into runtime vulnerabilities, and empowers your teams with real-time exploitation risk insights to address vulnerabilities proactively. Learn how the Secure Application and Splunk Security integration helps you meet organizational security SLAs by streamlining workflows between Application and Security teams to ensure rapid triaging and remediation of emerging exploits.

### Reimagine customer experience with Proactive Journeys: Connect with customers when they want, how they want. - PSOCOL-1034
Speakers: Brian Heikes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271850515001zo0C
Imagine you could anticipate your customers' needs before they realize they even need the support. It's possible with proactive journeys and AI-powered proactive, two-way customer communications. In this session, learn about the transformative impact of proactive journeys and how they help to deliver a truly connected customer journey. Using the Webex Connect cloud communications platform, orchestrate highly personalized, conversational messaging to engage with your customers when they want, how they want and on their channel of choice. Join this session to learn how companies can: - Centrally automate and orchestrate proactive, two-way customer interactions - Build end-to-end customer journeys using APIs and low code tools - Combine innovations in AI and automation to deliver highly connected journeys, leaving customers feeling understood and valued

### Resilient Healthcare Technology: From Transactional to Strategic Enabler - CNCXAR-2000
Speakers: Richard Durost (Froedtert ThedaCare Health), Eli Tarlow (CDW)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866976001zqQh
Every healthcare technology dollar must now justify its existence through operational improvements, system reliability, and patient care outcomes. This session reveals how forward-thinking healthcare organizations are leveraging strategic partnerships and the CDW Pillars of Care framework to transform technology infrastructure—both on-premises and cloud-based—into a strategic enabler of resilient digital health initiatives. CDW Technology Strategist, Eli Tarlow, and Froedtert ThedaCare CISO, Rich Durost, will guide you through how moving beyond transactional vendor relationships to strategic partnerships can deliver reliable, secure technology investments that provide both protection and performance across your entire care continuum. From establishing cyber-resilient infrastructure that ensures 24/7 availability to securing EHR modernization projects with built-in redundancy and preparing for AI-driven diagnostics with fault-tolerant architectures, discover how resilience-by-design and security-by-design principles—supported by strategic partnerships—can actually accelerate your digital transformation while reducing total cost of ownership and ensuring continuous patient care delivery regardless of your deployment model.

### Resilient Networks: From Prevention to Recovery - BRKSPG-2695
Speakers: Marius Stoica (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271964838001ztls
In today's digital landscape, network uptime and performance are essential for business success. This session explores the critical components of operational excellence in network operations. Learn how to elevate your network from reactive to proactive by implementing best practices for software consistency, proactive audits, and intelligent automation. Discover strategies to optimize network performance, minimize downtime, and ensure business continuity through effective incident response and maintenance planning. By adopting an holistic approach to network management, you'll gain the tools and knowledge to build a resilient, high-performing network that drives business growth and customer satisfaction.

### Rethink Your Edge Routing Architecture - BRKSP-2275
Speakers: Emerson Moura (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271968140001zGPO
This session will look at industry and technology trends and discuss how they can be applied to design novel edge routing architectures. It will explore how the availability of high-performance, more power efficient silicon and router designs, paired with optics and automation software, opened the door to designing new edge routing systems that are simpler, more cost-effective, and future-ready, while delivering the rich services and strict SLAs that are required for value-added and business-critical services. The session will also discuss how this shift aligns with other trends that have been forcing the push of services edge functions closer to end users and applications. Together, these industry trends and innovations, can bring many technical and business benefits to service providers that are looking at modernizing their edge routing architecture for the long term.

### Revolutionising the Cruise Experience: AIDA Cruises and Cisco's Innovative Partnership - CSSENS-2000
Speakers: Anis Edavalath (Cisco), Gordon Poppe (AIDA Cruises), Diogo Almeida (AIDA CRUISES)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271872709001zTsa
Discover the transformative partnership between AIDA Cruises, Carnival Corporation's German entity, and Cisco, as they redefine guest experiences on the high seas. This collaboration showcases Cisco's state-of-the-art networking solutions using Catalyst 9000 platform, providing a resilient and secure architecture that supports connectivity with Starlink and satellite providers. Learn how location analytics and OpenRoaming capabilities enhance guest satisfaction through advanced services. Explore the role of Meraki cameras and sensors in promoting sustainable cruising practices, and see how Cisco's video endpoints create hybrid workspaces, appealing to the "bleisure" traveler. This initiative highlights the integration of automation and security across all operations, setting new benchmarks for innovation in the cruise industry.

### Revolutionize customer experience with Webex AI-powered innovations. - PSOCOL-1033
Speakers: Andrew Cammer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271850323001zjls
In the rapidly expanding AI landscape, organizations are faced with a plethora of options to enhance customer experience (CX). This session will reveal strategies for gradual AI adoption, focusing on areas that quickly maximize value for both customers and the business. Learn how Webex Customer Experience solutions enable organizations to create AI-powered, connected customer journeys across voice and digital channels. Join us to learn more on: - Leveraging AI and automation at different points across a customer's journey - How to achieve the right balance between assisted and unassisted support to boost contact center efficiency and CX outcomes. - The transformative potential of proactive communications and digital messaging.

### Revolutionizing CX with Cisco's Webex AI Agents: Strategies, Use Cases, and Insights - BRKCCT-1023
Speakers: Stefan Zeidenberg (Cisco), Devon Meerholz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271865245001zJ0g
In Today's AI-driven landscape, enterprises are racing to harness transformative efficiencies. But what does AI mean for you, and why should it matter? This session explores Cisco's latest innovation in conversational AI: the **Webex AI Agent**. you'll gain insights into autonomous agent capabilities, comparing **knowledge base-driven interactions** with **task-oriented slot fulfillment**, and receive guidance on when to use autonomous agents versus scripted ones to maximize value. **Key Takeaways**: - Understand the capabilities and future-proofing potential of a One Cisco approach through AI. - Learn how the Webex AI Agent integrates with Webex Contact Center (WxCC) and Webex Connect to act as a force multiplier in your CX strategies. - Explore real-world customer stories and use cases demonstrating the benefits of early adoption of Webex AI Agents. This session is ideal for professionals looking to enhance their understanding of conversational AI and its strategic applications in customer experience. No prior experience with WxCC or Webex Connect is necessary, though familiarity with either voice or digital communication flows may enhance your understanding. Join us to discover how Cisco's Webex AI Agents can help your enterprise stay ahead in the age of AI and deliver exceptional CX.

### Revolutionizing Data Centers with Cisco Nexus Hyperfabric: A Cloud-Managed Fabric-as-a-Service Solution - CTF-1048
Speakers: Michelle Jardim (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271879404001z7vv
Join us for an in-depth exploration of Cisco Nexus Hyperfabric, a cutting-edge cloud-managed data center fabric-as-a-service solution. This session will showcase how Hyperfabric simplifies the design, deployment, and management of data center fabrics, enabling IT generalists, application teams, and DevOps professionals to achieve predictable and repeatable outcomes. Learn about its purpose-built vertical stack, which integrates hardware, software, and cloud controllers to deliver high-performance Ethernet fabrics with zero-touch provisioning. Discover how Hyperfabric scales seamlessly across global data centers. Whether you're modernizing your data center or building AI-ready infrastructure, this session will provide actionable insights to transform your operations.

### Revolutionizing Industrial Operations: Unveiling the Power of AI in IIoT with Cisco Solutions and Emerging Industry Trends - BRKIOT-2721
Speakers: Casca Kwok (Cisco), Kevin Wood (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271953371001zIGH
Discover how AI and IIoT are transforming industries, increasing efficiency, and inspiring innovative solutions. Learn how Cisco is leading the IIoT revolution by enhancing predictive maintenance and data analytics. Our session will highlight the high performance of Cisco's industrial products for edge AI, improved operational efficiency through their switch family's software, and reliable connectivity for Edge AI deployment. We'll also cover the latest trends in AI and IIoT. Join us to explore the dynamic intersection of AI and IIoT with Cisco's pioneering solutions.

### Revolutionizing Physical Security with AI-Driven MV Cameras - AIHUB-2016
Speakers: Ollie Gerrard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271969671001zUJO
In Today's rapidly evolving security landscape, leveraging AI to enhance physical security has become a game-changer. This session explores how AI-powered MV cameras are redefining security operations by enabling advanced capabilities such as real-time threat detection, behavior analysis, and proactive incident management. Attendees will gain insights into how AI can automate routine tasks like video monitoring, empower security teams with actionable insights, and ensure compliance with data privacy standards. Join us to learn best practices for deploying AI-driven solutions across various environments, from corporate campuses to retail spaces. We'll also dive into cross-architecture integrations that maximize the value of MV cameras, ensuring a seamless approach to protecting people and assets.

### Rewriting the Tech Playbook: Empowering Unconventional Talent for Success - CTF-1030
Speakers: Tia Stackle (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271844222001z1rY
In today's tech industry, unconventional paths are creating new opportunities for individuals at all levels to make their mark. This session will explore how non-traditional educational journeys, including Cisco certifications, can lead to remarkable achievements in the tech world. You'll uncover the critical role of sponsorship, gain actionable insights, and discover innovative strategies to forge your own unique path to success. And yes, AI will be part of the conversation! Join us for an inspiring and practical session filled with tools to break barriers, ignite your potential, and take your tech career to the next level.

### Riding the IPv6 Wave: Network Operations in an Increasingly IPv6 world - BRKIPV-2005
Speakers: Jeffry Handal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271955336001zFsX
By several accounts, IPv6 is now the predominant IP version. What does this mean for your business? Are you ready to dive in? In this session, we will embrace network deployment and operations in an IPv6 world, operating in dual-stack to start with an eye on an IPv6-mostly (or even IPv6-only) objective. We will cover the building blocks to achieve connectivity, policy, and visibility leveraging cloud, on-premise platforms, or both, taking advantage of Cisco's diverse portfolio. We will illustrate best practices and design recommendations while highlighting architectures and IETF activity to help enhance your operational landscape, so you, too, may ride the IPv6 wave. Session pre-requisites: good understanding of the IPv6 protocols (e.g., from the TECIPV technical seminars or BRKIPV-2191 "IPv6: It's Happening!"). Note that an IPv6-only session is also available: BRKENT-2008 "Goodbye Legacy, the Move to an IPv6-Only Enterprise."

### Roll Your Own AI-assisted Investigations in Cisco XDR - DEVNET-2387
Speakers: Ben Greenbaum (Cisco), Christopher Van Der Made (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271905193001zRCU
In this session, we will discuss an exciting AI-assisted automation project in Cisco XDR. After the session, you will be equipped to do this yourself as well, and even customizer it to your liking. This project aims to augment Security Analyst efficiency by easing access to common information resources, and then offloading the task of consulting and analyzing the resulting dataset to an AI agent. Every Security Analyst has a collection of "quick lookup" tools to determine ancillary information about an investigation subject, whether that's the geographic location of an IP address or the registered owner of a domain or the manufacturer of a network card that has a specific MAC address. None of these tools are natively supported in XDR at this time. We will address this gap with a simple and easily customizable tool that fits into the existing open XDR framework. This will allow you and your team to easily pivot out to specific resources of their choosing that will show them the desired data on the selected observable. We will then go a step further and fetch those resources for them, displaying the information and a generated summary in the XDR UI and saving them those clicks in the first place. In the course of investigating an Incident, which may have many observables, we will then have an LLM do a meta-analysis of all of the collected data and look for patterns, anomalies, or other red flags and items of concern in the gathered context.

### SD Access: Troubleshooting the Fabric - BRKTRS-3820
Speakers: Michel Peters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271936510001zbnQ
The fabric, as built and monitored by Cisco Catalyst Center (formerly Cisco DNA Center), is based upon a number of key technologies. This session is a deep dive into those technologies as they are being used and what issues are commonly seen when deploying SD-Access, as well as how they could troubleshoot from the device perspective. Troubleshooting techniques for CTS, LISP, VXLAN, and packet forwarding will be discussed and demonstrated, showing how things can be investigated from a device perspective. Attendees are expected to have a good understanding of SD-Access.

### SD-Access in Action: Trusted Outcomes Across Education and Finance- Featuring UC Riverside & CIBC Bank - BRKENS-1805
Speakers: Kanu Gupta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271919506001zUGR
Join this power-packed session to hear firsthand from two leading organizations—UC Riverside and CIBC—on how Cisco SD-Access is transforming their networks for secure, scalable, and simplified operations. In the first half, UC Riverside's CIO shares their decision-making journey: why they chose SD-Access over other fabric architectures, how it aligned with their Zero Trust security strategy, and the tangible benefits realized across campus. In the second half, hear from CIBC Bank, an early SD-Access adopter operating one of the largest global campus fabrics—with over 10,000 devices across 2,000+ sites. Learn how the Bank is leveraging SD-Access to fuse security into the network itself, enabling enterprise-wide microsegmentation, simplified operations, and impactful business outcomes. This session offers practical insights into how SD-Access is being deployed at scale to enable secure segmentation, policy automation, and operational efficiency across industries.

### SD-WAN as Code - DEVNET-1016
Speakers: Andrea Verrengia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893787001zkWF
Cisco Catalyst SD-WAN is designed to streamline the operational workflows and take the complexity out of network configurations. At the heart of this transformation is automation, a crucial element in the journey towards network simplification. In this session, participants will learn how to use the SD-WAN as a Code, a powerful automation framework based on Terraform, to configure the network 'as code.

### SDAVC Missclassification troubleshooting - TACENT-2024
Speakers: Cynthia Lizbeth Gomez Gomez (Cisco), Ian Estrada (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271929591001zbrL
Overview on SDAVC together with NBAR NBAR Cache - Entry Creation/Classification Process Demo demonstration of miss classification issue

### SONiC Architecture and Deployment Deep Dive - BRKMSI-2004
Speakers: Jiri Chaloupka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967174001zlt7
First part of this SONiC Architecture and Deployment Deep Dive session will explain SONiC Operating System (OS) architecture in detail together with examples of SONiC with Cisco Silicon One NPU / Data Plane. Second part of this session will focus on deployment examples and will explain when SONiC should be consider for deeployment including AI frontend and backend network.

### SR Flex-Algo: The Future of Intelligent Traffic Engineering in SR and SRv6 - BRKMPL-2129
Speakers: Steven Blasiol (Cisco), Matt Breneisen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966015001zbjA
Are you preparing or planning for a session to learn about the benefits of Segment Routing Flexible-Algorithm (SR-FA) for the Traffic Engineering of IPv4 and SRv6 service? Well, then this is the session for you. SR-FA is a powerful approach to modernizing network Traffic Engineering (TE). It can really simplify the way traffic is routed by giving network engineers more control over path selection without needing complex protocols. The presentation will then showcase concrete use cases. For SR IPv4, we will examine scenarios such as providing differentiated services based on traffic type and optimizing paths for specific applications. Transitioning to SRv6, we will delve into its enhanced capabilities, including network partitioning, service chaining, and integration with other network functions. Real-world examples and configuration snippets will illustrate the implementation and benefits of Flex-Algo in both SR IPv4 and SRv6 deployments, highlighting its potential to simplify network engineering, improve resource utilization, and enhance service delivery.

### SR-TE 101: Driving a New Traffic School of Thought - BRKMPL-1203
Speakers: Bryan Lawrimore (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271965420001zXc5
Momma always says, "MPLS traffic engineering is hard!" Well, not anymore. In this session, you will get a quick overview of Segment Routing and a taste of the many ways it can be used to steer traffic through your underlay. Then you'll see how you can easily create services and engineer them to do your bidding as their packets traverse your network by using Crosswork Network Controller 7.0. A demonstration of CNC will be driven while showing participants just how easy traffic engineering can be to deliver in an SR-MPLS network. Topics covered will include Segment Routing, SR-TE, Circuit Style-SR (CS-SR), Flex-Algo, and SR-Path Computation Element (PCE).

### Scale and Enhance Wireless for the Enterprise - PSOENT-1018
Speakers: Travis Schlafke (Cisco), Stefani Johnson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271926875001zElA
Scaling and modernizing wireless networks across large campuses brings challenges in flexibility, performance, and centralized management. The Campus Gateway from Cisco Wireless offers a breakthrough solution for seamless, scalable connectivity, whether your network is fully cloud driven or you're exploring cloud options. Discover how Campus Gateway addresses evolving campus demands, boosts network agility, and integrates into Cisco's wireless vision to deliver transformative value for modern enterprises.

### Seamless Data Center Deployment with Cisco Intersight Infrastructure Automation: A Real World Example - BRKATO-1008
Speakers: Jeff Comer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271832454001zhSZ
Customers today face significant challenges, including a lack of automation, regulatory compliance, governance, and consistency across operations and deployments. These issues are compounded by labor-intensive manual tasks and processes that span multiple domains and teams within an organization. In this session, we will dive deep into how the Cisco Intersight Infrastructure Service Automation (formerly Intersight Cloud Orchestrator (ICO)) addresses and resolves these challenges. Additionally, we will showcase a real-world example of how ICO was implemented at a customer site to automate their data center operations from infrastructure to application deployment, enhancing efficiency and compliance.

### Seamless Transition: Key Differences and Migration Strategies from Palo Alto to Cisco Next-Generation Firewalls - BRKSEC-2083
Speakers: Kyle Barnes (Cisco), Jeff Walker (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272000158001zRWq
Join us for an insightful session, "Seamless Transition: Key Differences and Migration Strategies from Palo Alto to Cisco Next-Generation Firewalls," where we explore the transformative journey of a real-world customer who successfully transitioned their network security infrastructure. Presented from the perspective of Cisco Customer Experience (CX), this session will highlight the critical distinctions between Palo Alto and Cisco NGFW, focusing on advanced security features, performance enhancements, and operational efficiencies. Through a detailed customer case study, we will illustrate the step-by-step migration process, including the planning, execution, and post-migration phases. Learn about the challenges encountered, the solutions implemented, and the tangible benefits realized from making the switch. Gain valuable insights into best practices, common pitfalls to avoid, and the comprehensive support provided by Cisco CX to ensure a smooth and effective transition. This session is ideal for IT professionals, network administrators, and security experts looking to upgrade their firewall solutions with confidence. Discover how Cisco NGFW can elevate your security posture and how Cisco CX's expertise can guide you through a seamless migration journey.

### Secure Endpoint : Unveiling Latest Key Features! - BRKSEC-1544
Speakers: Filipe Lopes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271998958001zZ74
In today's digital landscape, Endpoints are a primary target for cyber attackers seeking entry into corporate networks. As threats evolve, traditional defenses are no longer sufficient. Attackers deploy advanced techniques, including ransomware, fileless malware, and zero-day exploits, to infiltrate systems and exfiltrate sensitive data. Join us to explore the latest threat landscape and discover cutting-edge strategies for endpoint protection. Learn how we Prevent, Detect, Respond, and Protect against sophisticated attacks with technologies such as behavioral analysis, machine learning, and real-time threat intelligence. This session will guide you through integrating advanced endpoint security measures that go beyond traditional antivirus solutions, ensuring robust protection across all devices. Enhance your security posture by leveraging the latest innovations in endpoint detection and response, and empower your organization to stay ahead of potential threats.

### Secure Firewall Branch Automated and Scaled: Zero to Hero in 60 mins - BRKSEC-2981
Speakers: Barry Yuan (Cisco), Dinesh Moudgil (Cisco Systems, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272006029001zFE2
Step into the future of network security and efficiency with this demo-packed session, designed for anyone eager to master Secure Firewall and SD-WAN automation. Whether you're just starting or looking to elevate your expertise, this session will equip you with practical knowledge and tools to optimize your infrastructure. Discover real-world use cases and scenarios as we delve into Secure Firewall deployments, policy automation, and performance optimization. Learn how to harness APIs and automation tools to simplify operations, reduce manual efforts, and build scalable, secure SD-WAN environments. Walk away with the skills to drive security and efficiency like a pro.

### Secure Firewall Clustering deployments and recent enhancements - BRKSEC-2266
Speakers: Carol Trincia Dsouza (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272002530001z3Iz
This session delves into clustering deployments for firewalls, exploring implementations in both public and private cloud environments. It will cover inter-site clustering, intra-chassis clustering, and multi-instance clustering, providing a comprehensive understanding of these architectures. Additionally, the session will examine interface modes in clustering, dynamic routing, and VPN integration, along with the role of ACI in clustered deployments. Attendees will also gain insights into cluster configurations across various firewall models, as well as recent enhancements in cluster health monitoring via FMC and the backup and restore capabilities for clustered firewalls.

### Secure Firewall SDWAN 7.7 in 4-steps - CTF-1046
Speakers: Bruno Fagioli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271867167001zID4
This presentation showcases the improvements of Cisco Secure Firewall 7.7 specifically for SDWAN technology. We are going to talk about the underlying technology that enables Firepower SDWAN such as differences between policy-based x route-based VPN, what is SVTI, DVTI and ECMP as well as how Secure Firewall 7.7 employs dynamic routing in a hub-spoke topology. At the end, you will notice that Secure Firewall 7.7 abstracts most of the complexity into 4 simple steps to get your SDWAN up and running. I will see you there.

### Secure Firewall in ACI - BRKSEC-2992
Speakers: Fabien Gandola (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272011977001zIWK
In modern data centers, it is crucial to be able to insert, deploy, and operate next-generation firewalls (NGFWs) as easily as possible. This session won't make you a service insertion ACI expert nor a Cisco Secure Firewall expert in just 90 minutes. Instead, this session aims to explain and demonstrate how Cisco Firepower Threat Defense (FTD) can offer more than just any NGFW in ACI. We will first introduce very quickly the necessary key concepts on ACI to insert an NGFW, followed by the shortest Cisco Secure Firewall introduction ever. We will then cover the most common ways to insert NGFW nowadays, focusing mostly on service graphs leveraging L3 PBR. Finally, we will hit the key part of the session with few a key points that FTD brings to the table: The advantages of leveraging clustering, especially in multipod deployments The role of dynamic objects in FTD and how they can help accelerate enforcement, especially if leveraged by Cisco Secure Dynamic Attribute Connector (CSDAC) Integration with Cisco Secure Workload using FTD, for both policy and virtual patching The ability to automatically remediate with the remediation module in Firewall Management Center (FMC) The session is targeted at customers who already using FTD in ACI and wish to improve their integration, as well as those interested in implementing ACI and looking to learn about FTD insertion capabilities.

### Secure Networking & Segmentation for Multicloud Architectures - BRKDCN-2930
Speakers: Brenden Buresh (Cisco), Joe Piperata (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889208001zURu
This session will focus on how to design and build secure network connectivity and segmentation for multicloud data center architecture. First, we'll review best practices for single fabric and multi-site VXLAN designs. Next, we'll introduce the pivotal role the network plays to enable segmentation highlighting the tools and capabilities a VXLAN network fabric provides. Then we'll explore group policy and how this simplifies and extends security capabilities to address both north-south and east-west traffic flows in the data center. We will review how network-attached security devices integrate in data center designs to provide in-depth stateful security controls and address more stringent regulatory and compliance use cases. Then, we will expand beyond on-premises data centers to include connectivity to multiple public clouds leveraging SD WAN cloud onRamp for branch-to-cloud, DC-to-cloud, and cloud-to-cloud use cases. Finally we'll describe how to extend network segmentation integrating MultiCloud Defense to provide cloud-native enforcement controls for ingress and egress connectivity between VPCs, regions, clouds, and the Internet.

### Secure Operations for an IPv6 Network - BRKSEC-2044
Speakers: Eric Vyncke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271999753001z4UM
Nowadays, IPv6 is in all networks as all hosts have IPv6 enabled by default. While network operators are experienced with secure operations in the IPv4 world, what are the specific challenges and techniques to be used to securely operate an IPv6 network? This session, by one author of RFC 9099, will present the main differences between IPv4 and IPv6 with respect to security, how to prevent attacks, what about extension headers, inventory, user attribution, and event correlation in a dual-stack network (from Data Center to wireless network). A good knowledge of IPv6 will be assumed.

### Secure the Network Edge against the DDoS Attacks! - BRKMSI-1001
Speakers: Raja Kolagatla (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271962099001z21O
Latest DDoS trends indicate that L3-L4 attacks have increased, with 20% year on year in Q2 2024 and the average attack size of the L3-L4 attacks doubled since 2022. Traditional DDoS solutions can't scale with the above trends, making it prohibitively expensive for Service Providers to maintain large sized DDoS Scrubbers, in more distributed in tune with evolving Networks. Service Provider networks have also become the hotbed for the threat actors and also stand second in the targeted industry too. This serves as a wakeup call for the Service Providers, to fortify the core networks to become threat free. Cisco Secure DDoS Edge Protection is is an industry's first true on-box and CFO-Friendly solution, that stops DDoS attacks at the Service Provider Network Edge, with projected TCO savings up-to 83%, in comparison with traditional scrubber based solutions. Cisco Secure DDoS Edge Protection on routers detects and mitigates attacks autonomously in real time, optimizing the performance of low-latency applications. Goal of the session is to provide the high level architecture overview of the Cisco Secure Edge Protection solution, delve deeper into the use cases, showcase the TCO savings, provide customer success stories with this new innovative solution.

### Secure your AI clusters and applications with Isovalent and Trivy! - DEVNET-1541
Speakers: Tim Miller (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271896129001z8Vs
Many AI security discussion focus around securing the prompts sent to LLM models and validating their output. However, these AI applications and agents are generally built as cloud native applications running as containers on Kubernetes! In addition to the GenAI related attack vectors, customers must still apply Kubernetes security fundamentals for the unique set of security concerns in these cloud native platforms. This session will showcase open source technologies to proactively assess application vulnerabilities (Trivy), define policies to ensure only trusted workloads are deployed (Admission Policies), provide a zero trust networking foundation (Cilium), and monitor in real time for suspicious activity (Tetragon). Code examples will be provided to help the attendee fast track their journey. These techniques are drawn from industry certifications and can help the attendee in their exam preparations.

### Secure, Assured Service Delivery and Networking for the AI Era - PSOMSI-1001
Speakers: John Cardani-Trollinger (Cisco), Tim Hu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271960185001zF3i
See new Cisco Agile Services Networking security features that address AI data demands for service providers. As AI generates more data to be processed, transported, and accessed across locations and devices, network architecture security must be reconsidered. Agile Services Networking offers a secure, responsive, and autonomous network environment to support dynamic AI traffic. Learn how our new integrated security features protect service delivery networks and fuel new revenue opportunities.

### Secure. Streamline. Scale: The Power of a Unified Endpoint Management Platform - CNCATO-2007
Speakers: AJ Singh (NinjaOne)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271831139001zJYi
Fragmented IT tools create friction, delays, and vulnerabilities. In this session, we'll explore how leading organizations are shifting from scattered toolsets to streamlined, consolidated platforms. You'll discover how organizations are automating repetitive tasks, improving endpoint security, and driving measurable efficiencies. If your current IT operations feel reactive and overloaded, this is your blueprint for regaining control.

### Securing AI Agents and Agentic RAG Implementations - AIHUB-2001
Speakers: Omar Santos (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271926315001zrfV
AI agents are now everywhere! Retrieval-Augmented Generation (RAG) has also evolved to be a part of most AI-powered applications. These AI implementations offer powerful capabilities but introduces new security challenges. In this presentation you will learn about the best practices for safeguarding these intelligent systems. We will explore the unique threats facing autonomous AI agents, including vulnerabilities related to privilege access, prompt injection, data poisoning, and unauthorized access to sensitive information. We will dissect the security implications of agentic RAG implementations, where AI agents orchestrate the retrieval and utilization of external knowledge. A key focus will be on securing Model Context Protocol (MCP) implementations, examining methods to ensure the integrity and confidentiality of information exchanged between language models and external data sources. You will gain practical insights into implementing relevant security capabilities to build resilient and trustworthy AI agent and agentic RAG systems.

### Securing Applications, Simplifying Workflows: Cisco + Splunk Better-Together - BRKOBS-1025
Speakers: Kashyap Merchant (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271979906001zSBL
As modern applications increasingly rely on open-source code, vulnerabilities are growing at an alarming rate (742% YoY), creating a major challenge for security and application teams. This session will demonstrate how Secure Application and Splunk Security bridge the gap between these teams, providing real-time vulnerability detection and threat prioritization based on risk and impact. you'll learn how the integration helps reduce false positives, streamline workflows, and ensure rapid triage and remediation of emerging exploits. With a simplified deployment model that leverages existing APM agents, this solution ensures seamless coverage across both hybrid and on-prem applications, empowering teams to work in sync and meet organizational security SLAs. Join us to discover how this unified approach drives faster response times and strengthens your application security posture.

### Securing Cisco Collaboration: TLS 1.3 - TACCOL-2013
Speakers: Charlie Wiley (Cisco), Luis Martinez Botello (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271850890001zU95
"Elevate your expertise by diving into TLS 1.3 in Collaboration and learn about the benefits and advantages of using this secure protocol. Immerse yourself in dynamic, real-world scenarios that unravel the complexities of certificates and Cisco device integration. You'll acquire practical troubleshooting techniques and learn how to configure TLS settings to secure your environment."

### Securing IIOT environments: Protect against cyberthreats, improve network segmentation, and enable full visibility into industrial networks - CTF-1051
Speakers: Josh Brink (Cisco), Sophia Gudenrath (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271994783001zjl0
Cisco Cyber Vision is a cutting-edge solution designed to secure industrial operations by providing unparalleled visibility into Industrial Control Systems (ICS) and Operational Technology (OT) environments. It enables organizations to identify all connected assets, understand their communication patterns, and assess their security posture. By embedding visibility capabilities directly into industrial network equipment, Cyber Vision eliminates the need for additional security appliances, simplifying deployment and reducing costs. Its advanced monitoring capabilities help detect vulnerabilities, segment networks, and enforce cybersecurity policies, ensuring operational continuity and resilience. Furthermore, Cyber Vision integrates seamlessly with Cisco's security portfolio and third-party tools, enabling IT and OT teams to collaborate effectively in building a unified cybersecurity architecture that protects both industrial and enterprise networks.

### Securing Industrial Networks: Where Do I Start? - BRKSEC-2096
Speakers: Francesca Martucci (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272006841001zesT
Operations Technology is increasingly moving to standard based networks and protocols and therefore it is mandatory that Cybersecurity is embedded within every OT implementation. Within this session, we will see how we can apply Zero Trust principles in an OT environment: how we can ensure proper visibility of the devices connected, how we can enforce the correct level of segmentation, and lastly how we can get visibilty of potential threats and the options to mitigate them. We will see how an integrated architecture can make a difference in the capability to identify, analyze and respond to threats in a proper and efficient manner. This session is intended for engineers, architects and professionals responsible for designing and securing OT systems.

### Securing Spaces: Meraki MV, Genea, and the Power of IoT - BRKIOT-1516
Speakers: Yale Ohh (Cisco), Matthew Marston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271970439001zunu
With security breaches rising 72% since 2021 and human error accounting for 88% of cybersecurity incidents, integrating advanced surveillance and access control is crucial. This session explores how Meraki MV Cameras and Genea's access control create a robust security framework for Today's challenges. You'll gain insights on: • Integrating access control events with video feeds for faster incident response • Maximizing efficiency through Vision Portal's seamless integration • Leveraging APIs and webhooks for enhanced security integration Participants will also see a live demo to experience the technology in action. This session is ideal for IT professionals and security personnel with a basic understanding of network architecture. Discover how these cutting-edge technologies can transform your security strategy and create a more robust framework.

### Securing Webex Meetings - Privacy, Confidentiality and Security Options for Meetings in a Virtual World - BRKCOL-2876
Speakers: Paulo Jorge Correia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857405001zF6e
Come along to this breakout session if you want learn more about Webex Meetings Security e.g.: How, as a Webex administrator, you can secure Webex Meetings for users in your organization How, as a Webex meeting host and scheduler, you can secure your Webex Meetings Security features and recommendations for Scheduled Meetings and Personal Meeting Rooms Deepfakes - Meeting participant identity and identity verification Blocking Recording Bots and unwanted users Webex Secure Meeting Types : Standard, Private, End to End Encrypt - and the benefits and trade off of each meeting type Recently introduced features e.g. Block by domain Participant Label controls Upcoming new features: Webex 1:1 End to End Encrypted Calls Zero Trust Webex End to End Encrypted Meetings - with support for Trusted On Premises meeting participants and services Post Quantum Cryptography

### Securing Wireless Networks with Cisco Identity Services Engine and Access Manager - BRKEWN-2047
Speakers: Carlos Alcantara (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271940627001zVGE
Unlock the full potential of your Cisco Wireless Network with Cisco Identity Services Engine (ISE) or Meraki Access Manager integration. This session will guide you through the essentials of designing, deploying, and troubleshooting a secure wireless environment. Discover how to seamlessly integrate Catalyst and Meraki wireless solutions, efficiently manage network and wireless users, and enhance authentication processes. Dive into advanced topics such as network segmentation, Scalable Group Tags, and Adaptive Policy to strengthen your network security framework. Whether you're looking to secure users or endpoints, this session provides the insights and tools you need to build a robust and secure wireless network architecture.

### Securing Your AI Journey -- AI Defense Automation - DEVNET-2277
Speakers: Barry Yuan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271902672001zGtt
AI is transforming businesses, but are you securing it the right way? As AI adoption skyrockets, so do the security risks — prompt injection, model poisoning, data leakage, and more. Whether you're consuming AI as a SaaS service or building your own models, securing your AI workloads and data is non-negotiable. Join us for an exclusive deep dive into AI Defense, and its API capabilities, that empowers you to automate AI security at scale. Learn how to detect and mitigate AI threats in real-time, AI red teaming and creating guardrails, enforce security policies dynamically, and integrate AI security into your DevOps pipeline. This session is packed with insights, demos, and practical use cases to help you future-proof your AI strategy. Don't leave your AI unprotected — automate, defend, and stay ahead of threats!

### Securing Your Azure Virtual WAN with Cisco Secure Firewall - BRKSEC-2163
Speakers: Anubhav Swami (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272000761001zj6l
Azure Virtual WAN provides is a public cloud architecture that brings together networking, security, and routing functionalities in your Azure environment. Simple to deploy and scalable, Azure Virtual WAN is rapidly growing in popularity. The session begins with a thorough exposition of Azure Virtual WAN, and how traffic is engineered. Then this session focusses on deploying and configuring a Cisco Secure Firewall into this architecture to secure ingress, egress, and east-west traffic.

### Securing the Edge: Collaboration Certificates and Ciphers - BRKTAC-3000
Speakers: Jerson Gamboa (Cisco), LT de Leon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272019218001zi4X
With the need for hybrid environments, and remote work, there is an ever increasing threat to edge Collaboration solutions. In this session we will focus on the critical role of edge certificates and ciphers play in securing your Collaboration devices and applications. Attendees will learn tips about effective certificate management and how certificates and ciphers are used to secure data transmission. Please join us in this session to gain actionable insights to enhance the security of your Collaboration deployments whether cloud or on-prem.

### Securing the Olympics: The Cybersecurity Architecture for Paris 2024 - BRKSEC-1383
Speakers: Piotr Jarzynka (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271998759001zn3E
The Olympics and Paralympics Games are the largest and most significant sporting events globally, necessitating an advanced and comprehensive cybersecurity framework to ensure their security and success. Designing a robust cybersecurity architecture for securing the competitions involved a holistic approach to protect against emerging threats. By focusing on governance, prevention, detection and response, the event was safeguarded against a wide range of cyber threats. Discover the advanced blueprint implemented during the Paris 2024 Olympics. This session highlights the lessons learned and best practices used. You will gain a deeper understanding of the architecture securing the Olympics and the technical solutions that protected the games.

### Security Cloud Control: Navigating Through Onboarding and Event Logging Challenge's - TACSEC-2021
Speakers: Bashar Alsaeed (Cisco), Leonel Matus Climaco (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271997360001z8Wc
This session will focus on effective approaches to overcoming onboarding challenges related to Firepower Threat Defense (FTD) and Adaptive Security Appliance (ASA), utilizing both on-premises and cloud-based connectors. Participants will gain valuable knowledge on troubleshooting event logging while ensuring smooth integration and operation of security devices. The discussion will also cover the use of Cloud-delivered Firepower Management Center (cdFMC) logs. The attendees will discover how to use these tools to effectively address common onboarding and logging challenges, improving their ability to manage and secure network devices.

### Security Journey of a Router: Design to Deployment & Beyond - BRKSPG-2868
Speakers: Rakesh Kandula (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271968705001z2ot
In today's dynamic threat environment with increasing attacks on networks, it's important to build a trustworthy network from the ground up and be able to maintain trust over the lifetime of the devices. This session presents the security journey of a Cisco router, starting from development, factory, deployment to production and beyond. A host of operational security features are presented that help maintain the same level of trust over the years. Most of the features presented will be based on IOS-XR routers but the same will apply to other Cisco products too. Counterfeit hardware is another major issue for operators and the session includes a demo on how users can verify the hardware identity at zero cost. In addition to the threats posed by current technologies, operators must safeguard the networks from future threats posed by Quantum Computers. The session will demystify the threat to various aspects of security from Quantum Computers and presents a roadmap to the future.

### Security Unleashed: How Talos and Cisco Secure Firewall leverage Machine Learning for cutting-edge protections - BRKSEC-1042
Speakers: Bill Spry (Cisco), Andrew Blunck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271998176001zT1H
As the threat landscape rapidly evolves, staying ahead of emerging threats is increasingly challenging. Cisco addresses this head-on by leveraging Machine Learning to enhance the protections in Cisco Secure Firewall and to empower the Talos research teams. In this session, we'll explore tools like the Encrypted Visibility Engine and SnortML, industry-leading features for threat protection. We'll also offer a behind-the-scenes look at how Talos uses Machine Learning to uncover new threats worldwide.

### Security Without Sacrifice: The Modern Banking Infrastructure Blueprint - CNCSEC-1011
Speakers: Jermaine Mason (WINTRUST FINANCIAL CORPORATION), Stephanie Hagopian (CDW)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271994212001zqwP
Discover how financial institutions can navigate the competing demands of security, performance, and operational efficiency in today's banking environment. This session reveals the practical architecture decisions and technology integrations from Cisco ACI micro-segmentation to full-stack observability with AppDynamics, Splunk, and ThousandEyes that enable secure application delivery with limited IT resources. Join Wintrust and CDW experts as they share implementable strategies for building visibility-driven security that scales with your business.

### Security for AI: Addressing threats with AI Defense - PSOSEC-1027
Speakers: Aamer Akhter (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271995581001z0h3
AI is transformational, but the development and use of AI-powered applications expose companies to new security and safety risks that traditional cybersecurity solutions don't address. Cisco AI Defense is a purpose-built solution designed to protect the development and use of applications in a multi-cloud, multi-model world. This session will cover an overview of threats across the AI lifecycle, share pioneering AI security research, and demonstrate how AI Defense mitigates safety and security risks. Learn how AI Defense removes security blockers and enables your company to innovate fearlessly with AI.

### Security superpowers with eBPF and Tetragon - BRKSEC-2167
Speakers: Liz Rice (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272001166001zXE7
eBPF is a powerful kernel technology that provides a platform for building infrastructure tools in networking, observability and security. This session is a deep dive into the Tetragon open source project, which powers security observability and enforcement in Hypershield, and an exploration of Tetragon's use of eBPF. Tetragon uses tracing policies defined in YAML to define the potentially malicious events that it will report on, or optionally prevent. In this session you will learn how these Tetragon policies relate to eBPF programs attached to a variety of event types. You will see how Tetragon can use multiple eBPF programs to —follow— a series of individual events to pinpoint a specific behavior that is likely to be malicious. you'll also see how Tetragon minimizes the overhead of security observability by in-kernel event aggregation and filtering. If you have seen other —Introduction to eBPF— sessions, attend this session, packed with demos, to take your knowledge of eBPF for security to the next level.

### Security, VMware and AI - Oh my! - CNCDCN-2009
Speakers: Michael Hommer (NetApp)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271878427001zHmp
The pressures on IT are ever increasing and having to balance productivity, security and innovation may seem like a no win situation. Hear how Cisco and NetApp through FlexPod can reduce compromise and increase results with Zero Trust infrastructures, VMware optimization and modernization as well as Enterprise class AI.

### Segment Routing Innovations in IOS XE - BRKENT-2520
Speakers: Jason Yang (Cisco), Sumant Mali (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271934380001zpsr
Segment Routing is a key capability sought by Critical Network Infrastructure, global enterprises, and service provider networks today to build a 'Network as a Fabric' for service creation. IOS XE Enterprise Routing platforms have long supported SR-MPLS alongside IPsec, NAT, firewall, and DPI capabilities for edge deployments. IOS XE software is now being enhanced with Segment Routing IPv6. This session will introduce SRv6 capabilities in enterprise routing products, highlight the top SRv6 use cases and solutions, and discuss the latest innovations in Cisco SD-WAN (overlay) and SRv6 (underlay) integration.

### Separating hype from reality, real world use cases of AIOps and Assurance for wireless within Catalyst Center - BRKEWN-2029
Speakers: Kara Muessig (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271938457001zXL0
This presentation will focus on real-world scenarios demonstrating how AI-Ops within Catalyst Center helps harness the vast data generated by enterprise wireless networks and convert it into actionable insights. We will see how Catalyst Center's AI-Ops facilitates end to end troubleshooting by first filtering out unnecessary noise and then utilizing 360 views, intelligent capture and spectrum analysis to get to root cause. We will explore how wireless assurance can answer the age old question of "how well is my wireless network performing" through long term trends, health and insights. Lastly we will distinguish between the hype verses reality of AI in IT operations to understand what items AI cannot solve for and how to design around that.

### Setting the Stage for ISE Deployment Success: A Guide to Effective Planning - BRKSEC-2660
Speakers: Francesca Martucci (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272011173001zKsK
This session focuses on the preparation work that a customer should perform in order to ensure a successful ISE deployment. Like any technology, a deployment cannot be successful unless the proper planning and design isn't done first. We will examine best practices to follow in order to avoid some of the common pitfalls while preparing for an ISE deployment. At the end of the session, attendees can expect to have a better understanding of how to prepare their environment and their staff for an ISE deployment. This session is targeted at Network and Security Engineers, who are tasked in deploying ISE successfully.

### Simple Leaf/Spine with a Touch of ToR - Network Designs for the Modern Data Center - BRKDCN-2967
Speakers: Brenden Buresh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271891328001zdlf
This session will step back and review the rationale behind classic 3-tier data center design and some of the deployment history in conjunction with virtual port channel (vPC) technology. We will review the challenges that have arisen with 3-tier data center designs and how those architectures are now evolving to overlay based fabric buildouts. We will outline how the data center requirements are transitioning to accommodate changing traffic patterns based on modern application development and how that's driving overlay fabric solutions. We will introduce VXLAN EVPN as the primary overlay fabric solution being deployed in the data center and how it's best suited to modern data center use cases. We will start with single fabric VXLAN EVPN designs and expand that to multi-site data center deployments where we are engineering for high availability, fault tolerance, and optimal performance characteristics.

### Simple VXLAN/EVPN Fabric Setup with Nexus Dashboard - BRKDCN-2929
Speakers: Marc Belle-Isle (Cisco), Christian Capitan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889023001zeeV
VXLAN provides network capabilities and architecture scale that is not possible with traditional VLANs. With expanded use cases and increased scalability come challenges in how to best deploy and manage VXLAN-based fabric networks. NDFC provides a deep and rich set of features to tackle these problems, providing automation and analytics that can drive efficiency and scalability. In this session, we will provide an overview of how NDFC can alleviate operational hurdles with the deployment of NX-OS fabrics. We will start with initially standing up a single fabric either as a new greenfield environment or integrating a preexisting brownfield setup in a very condensed timeframe. We will review creating a multi-fabric design, enabling external connectivity and providing layer 4-layer 7 service node stitching. We will explore configuration change control, snapshot, and rollback, and how we address compliance use cases. Finally, we will outline how intelligent analytics can be leveraged to provide advanced visibility and insights for day-to-day operations.

### Simplified, Automated, and Proactive IT Workflows with the AI Assistant - PSOENT-1025
Speakers: George Mokdessi (Cisco), Marcus Sarmento (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928235001zLqZ
The Cisco AI Assistant is redefining how organizations utilize AI to streamline their operational workflows so they can deliver optimal digital experiences. In this session, discover how cross-platform AI optimizes troubleshooting and enhances visibility across owned and unowned environments. See the AI Assistant in action across Meraki and ThousandEyes as we quickly identify and resolve complex issues with ease.

### Simplifying Networks with Cisco Ecosystem Solutions - PSOENT-1021
Speakers: Ana Nennig (Cisco), Josh Collier (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271927426001zAlm
Hybrid work, IoT, AI, and distributed data are driving network complexity, leading to fragmented solutions and limited IT visibility. Learn how Cisco's ecosystem partnerships simplify management, enhance performance, and enable scalable, unified network infrastructures — helping businesses adapt quickly and efficiently.

### Simplifying Operations and Upgrades on Your Nexus Switch using Modular NXOS Software - BRKDCN-2639
Speakers: Samer Theodossy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271885235001zJkR
This session will start with a discussion of the NX-OS overall system architecture and discuss upgrade procedures and best practices on Nexus switches for both the stand-alone and ACI product lines and what the best approaches are to take. Customers want ease of operations on their systems with Cisco software, and one of the biggest areas is upgrades and changing versions of software. Cisco's goal is to focus on best-in-class high availability. In-Service Software Upgrade (ISSU) is a major table-stake feature that requires coordination and patching. Customers want the ability to choose the software components based on deployment scenario and hardware they are using and there is a need to provide a more modular software to accommodate these goals and help bring lower memory footprint to Nexus switches. We will see how the Nexus architecture lends itself to the modular/optional design and will discuss how this helps with creating an NXOS software image that is more lean and provides a smaller memory footprint. In addition, this will lead to asynchronous delivery of features/fixes which can be deployed on the system. With the introduction of feature optionality, we will discuss how this provides the flexibility to remove unused RPM packages and how to install/uninstall an optional RPM package on the system.

### Simplifying Security Automation With Cisco Umbrella And Cisco Secure Access APIs - DEVNET-2325
Speakers: Oleksii Borysenko (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904207001zqZd
Cisco Umbrella, a leading product in enterprise network security, adopts an API-first strategy that equips users to automate their daily security routines and proactively counter cyber threats, enhancing their network security capabilities. This session will enable the participants to: Play with Umbrella and Secure Access APIs in a sandbox to solve real-world use cases; Simplify DNS Policy Management With New Umbrella Tagging APIs; Programmatically manage API Keys; Improve efficiency and detect issues with the Umbrella API usage report;

### Simplifying User Onboarding with Modern Phishing-Resistant Passwordless Authentication - VILSEC-2038
Speakers: Kaushik Mahadeokar (FEITIAN Technologies US)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271993642001z4u2
Organizations are moving away from using traditional OTP/HOTP tokens and adopting FIDO-based authentication methods. FEITIAN, as a partner of Cisco, is helping lead this change by offering passkeys that are tied to hardware, improving both security and user experience. Learn how passkeys can be integrated into organizations from SMB to Enterprise. This session will demystify the enterprise adoption of passkeys, providing attendees with practical knowledge on how FEITIAN's solutions, in conjunction with Cisco Duo, empower organizations to achieve secure authentication, paving the way for a future of enhanced digital security.

### Sizing Compute Resources for Large Language Models - AIHUB-2659
Speakers: Rob Browne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271877426001zzoE
This session will provide insights and guidelines on how properly sized compute resources for Large Language Models (LLMs) are essential for optimizing performance, managing costs, and ensuring scalability. This process involves selecting the right hardware components to meet the specific demands of LLMs, balancing efficiency and budget considerations. Understanding these requirements enables effective deployment and future-proofing of AI infrastructure.

### Small Team, Big Impact: How to Navigate Disasters with Cisco Crisis Response - PP-1308
Speakers: Erin Connor (Cisco Crisis Response), Eric Knudson (Cisco), Matt Runyan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271947666001zYLC
Curious about how a small team can make a huge difference? Hear from the Cisco Crisis Response team to learn how the private sector plays a crucial role in disaster and emergency communications, through smart planning, rapid resource deployment, and Cisco technology solutions. We'll cover recent responses in the US, like Hurricane Helene in North Carolina, and worldwide. Key topics include: - Evaluating and managing customer and government inquiries. - Nationwide mobilization of personnel and equipment. - Technology and cybersecurity strategies during disaster contexts. - Resource and equipment management.

### Solving the Network Visibility Gap with AI: Optimize Digital Experience in Any Environment - VILOBS-1000
Speakers: Eric Camulli (7SIGNAL, Inc)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271974465001zrJm
Even with powerful tools like Cisco Meraki, Catalyst, and DNA Center, IT teams still face blind spots — especially at the edge, where Wi-Fi and endpoint issues impact digital experience. This session introduces how AI-powered monitoring from 7SIGNAL complements Cisco infrastructure by providing visibility into device-level behavior and wireless conditions that traditional tools can't see. you'll leave this session with ideas to help you: Extend Meraki and Catalyst insights to the edge with endpoint telemetry and real-time diagnostics Reduce Mean Time to Resolution (MTTR) with AI-driven root cause analysis Improve performance for remote workers, healthcare, manufacturing, and high-density environments This session is ideal for network engineers and IT operations teams using Cisco platforms.

### Solving the Segmentation Puzzle with Secure Workload! - BRKSEC-2161
Speakers: Jorge Quintero (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272007650001zshB
In a world of application workloads deployed anywhere, at any time, and with multi-cloud solutions, applying network security controls is no longer a trivial task. The policy control toolset just keeps growing, with multiple enforcement points in the network to protect our application workloads using different approaches such as the host firewalls, network firewalls and SDN controllers, or cloud-based in the form of security groups. With different teams managing each policy control and usually working in organizational siloes, there is no wonder why it often leads to inconsistent islands of policy controls across the environment. Secure Workload has been solving this puzzle, by defining a common policy model across all of these enforcement points (host-based, network-based and cloud-based) harmonizing all policy controls into an effective Zero-Trust Segmentation policy. This session will navigate through the Network/NetSec team lenses on how you can leverage Secure Workload to define a common policy model for your applications using agent and agentless approaches to protect your application workloads regardless of their form factor (baremetal, VM or container) or location (on-prem or multi-cloud).

### Splunk + Meraki Integration for Enhanced Network Visibility and Security - DEVNET-1342
Speakers: Shweta Palande (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271895141001zG2E
Join us for a technical deep dive into the powerful integration of Splunk with Cisco Meraki, where we'll demonstrate how the Splunk Add-on for Cisco Meraki provides comprehensive network observability and security monitoring. Through live demonstrations, you'll see how this add-on collects and analyzes data from Meraki's REST APIs and webhooks, delivering rich insights into network performance, security, and device health. We'll explore sample visualizations and custom dashboards that empower you to make data-driven decisions. Key takeaways include understanding how to leverage CIM-compatible knowledge for seamless integration with Splunk Enterprise Security and other Splunk solutions, as well as customizing data collection through scheduled API polling and real-time webhooks to meet specific monitoring needs.

### Splunk IT Service Intelligence (ITSI) - a Unified View for Network Service Health - BRKOBS-2008
Speakers: Isha Gandhi (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271980714001zGqO
In Today's fast-evolving digital landscape, one thing remains constant: "It's the network problem!" Ensuring seamless network performance is crucial for maintaining business success. Join us for an in-depth look at how Splunk IT Service Intelligence (ITSI) helps network and IT operations teams gain actionable, real-time insights into the health of their network services. By integrating data from diverse network domain controllers—such as ThousandEyes, Cisco Catalyst, and Meraki—into a single unified interface, ITSI accelerates issue detection, streamlines root cause analysis, and provides predictive health monitoring. This session will also showcase how ITSI's advanced machine learning and analytics capabilities empower network engineers and operators to quickly identify anomalies, minimize downtime, and ensure optimal network performance, helping improve user experiences and drive business continuity.

### Splunk Observability: A Unified Solution for End-to-End Visibility and Troubleshooting Across Applications, Infrastructure, and Networks - BRKOBS-1013
Speakers: Bill Grant (Cisco), Tapan Shah (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271978561001zUdN
Join us to explore how Splunk delivers a comprehensive, integrated solution designed to provide end-to-end visibility and proactive troubleshooting across critical technology domains, including applications, infrastructure, and networks. In Today's dynamic IT environments, where distributed systems span on-premises and cloud infrastructures, monitoring and resolving performance issues can be complex and time-consuming. Splunk's integrated platform breaks down silos, enabling organizations to gain real-time insights from a single pane of glass. By correlating data across diverse environments, it empowers IT, Network and DevOps teams to detect, diagnose, and resolve issues faster, improving operational efficiency and user experience. Join us to discover how Splunk Observability delivers powerful analytics, continuous monitoring, and streamlined workflows to enhance the reliability and performance of your critical systems—whether on-prem or in the cloud.

### Splunk and OpenTelemetry for Centralized Insights to Address Your Sustainability Goals - BRKGRN-1022
Speakers: Aman Sardana (Cisco), Steve Holl (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271946864001zxjr
"Seventy-five percent of organizations will have implemented a data center infrastructure sustainability program driven by cost optimization and stakeholder pressures by 2027." (Gartner, 2023) Is your company challenged with meeting these goals, but you are unsure what measurement systems to use, and how to derive actionable insights from the data? In this session we will explore some capabilities, standards, and trends that offer direction in this emerging field. You will learn how to: Ingest sustainability metrics from Cisco—platforms & cloud providers into a central data analytics system, leveraging frameworks such as OpenTelemetry (OTel). Aggregate data formats across device types, into common a format for analysis & insights. Use Splunk Sustainability Toolkit to derive actionable insights from your data, including anomaly detection, correlation, and prediction. How Cisco CX can help you achieve your sustainability goals.

### Sports, Technology & Service: A Conversation with Monumental Sports & Entertainment on Empowering Communities - IF-1036
Speakers: Ted Leonsis (Monumental Sports & Entertainment), Brian Tippens (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271950179001zD9u
Join Brian Tippens, Cisco's SVP and Chief Social Impact & Inclusion Officer along with Ted Leonsis, CEO of Monumental Sports Group for an inspiring discussion on how the intersection of technology, sports, and purpose-driven leadership can drive meaningful change. As the owner of the Washington Wizards, Capitals, and Mystics, and the founder of Monumental Sports & Entertainment, Leonsis has leveraged his platforms to create lasting social impact—from education and youth development to empowering Veteran communities. Tippens and Leonsis will discuss how doing good has shaped their approach to business, investing, and community engagement. This session will explore: How sports franchises can serve as catalysts for social change, uniting communities and uplifting youth. Why corporate leadership must embrace social responsibility, and how aligning profit with purpose leads to sustainable success. The role technology can play in advancing social change Don't miss this opportunity to learn how vision, influence, and strategic giving can turn ambition into action and create a legacy that transcends the game. With insights from his journey as a tech and pioneer (AOL, Revolution Growth), sports mogul, and dedicated philanthropist, Leonsis challenges audiences to rethink how industries can collaborate to build a more equitable future. And with decades of experience in Big Tech and Social Impact, Tippens will help the audience reimagine how social impact, technology, and entertainment can work together to create an inclusive future.

### Starlink Security Advanced - BRKSEC-2173
Speakers: Andrew Benhase (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272008421001zJTI
Building on top of the entry level BRKSEC-2037 breakout, this session will dive much deeper into network designs using Starlink (or other LEO Internet providers when available) using technologies such as Cisco SD-WAN, Cisco Secure Client and the use of native IPv6 over satellite. In addition, we will dive deeper into the options for remote site operations (kits) using Meraki MX/MR, Cisco ESR 6300 and/or Catalyst Micro-Switches for Edge connectivity including some designs for direct DC power for all equipment and what the power requirements are to operate over extended periods.

### Starting Strong in Offensive Security: Cisco's Ethical Hacking Path - CISCOU-1049
Speakers: Kyle Winters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271838693001zcfM
Embark on your offensive security journey with an introduction to the free Cisco Networking Academy course on Ethical Hacking. This session will introduce the Cisco Certificate in Ethical Hacking, detailing the skills and knowledge you will gain through the program. Participants will experience live demonstrations from the Networking Academy course, showcasing key ethical hacking tools and techniques. This session is perfect for those eager to explore ethical hacking and embark on a journey to become a proficient cybersecurity professional. Basic networking knowledge is recommended to maximize your learning experience.

### Stop Chasing Alerts. Start Fixing What Matters -- Automatically - CNCOBS-2003
Speakers: CIARAN RYAN (IBM)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271975661001ze6y
In a world where every second of app downtime costs revenue and reputation, waiting to react is no longer an option. Automated app-centric network observability gives you laser-sharp visibility into how network issues impact application performance and instantly turns those insights into automated fixes. No more noise. No more delays. Just faster resolutions, better user experiences, and operations that run on autopilot. Discover how automation + observability can help you predict, pinpoint, and proactively resolve issues across environments before they hit your business.

### Strategies for Passing the DCCOR (350-601) Exam - BRKCRT-2018
Speakers: Joe Rinehart (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271834909001zKEA
The Implementing and Operating Cisco Data Center Core Technologies Exam covers many complex topics with significant technical depth, and thus incredibly challenging. To achieve the CCNP Data Center and/or qualify for the CCIE Data Center Lab Exam, passing this test is an absolute requirement. The goal of this session is to map out the necessary strategies and resources that candidates must master to succeed in passing the exam.

### Strategies for a Quantum-Safe Security Transition - BRKETI-1007
Speakers: Tim Rowley (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271914897001zaUr
As quantum computing technology rapidly advances, it poses a significant threat to current security systems by potentially breaking widely used cryptographic algorithms. This makes understanding and preparing for quantum threats essential for maintaining data confidentiality and integrity. In this strategy-focused session, we will explore the impending challenges of quantum computing on security and provide practical guidance for operators to prepare effectively and plan for transition to quantum-safe encryption. You'll leave this session with ideas to help you: • Understand the current quantum threat landscape and its implications for cryptography. • Explore available quantum-safe cryptographic options and strategies for implementation. • Prepare a plan to transition to quantum-safe encryption based on exposure and risk priority. This session is designed for IT professionals and security operators with a foundational understanding of cryptographic principles. Participants will gain insights to help them navigate the transition to quantum-safe security readiness effectively.

### Streamline Migration to Webex & Automate Ongoing Management - VILCOL-2029
Speakers: Antoine Perrier (Kurmi Software)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848789001z02t
For large enterprises, migrating from on-prem collaboration to the cloud can be a complex, months-long process—often leaving them struggling with visibility across systems, increasing chances of service disruption and operational challenges. This session explores strategies for efficiently moving to Webex Calling, highlighting the various approaches that Kurmi offers to simplify migration while providing visibility and control of all systems. You'll learn how to: • Automate discovery, perform data assessment, and prepare your migration • Centralize management of hybrid unified communications setups (on-premises solutions, Webex Calling (Dedicated Instance & Multi-Tenant), and others.), contact centers (Webex CC, PCCE, etc.), and other third parties (SBCs, compliance recording, e911, etc.) • Streamline and automate day-to-day management • Monitor performance throughout This session provides insights and practical knowledge for IT professionals and decision-makers to lead UC migration projects confidently.

### Streamline Your Industrial Routing with Catalyst SD-WAN - BRKIOT-2586
Speakers: Dan Madey (Cisco), Pete Kavanagh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271954748001zR5Y
Industrial customers around the world are adopting a software-defined approach to their network architectures to improve the reliability and efficiency of their operations. Market transformations like Industry 4.0, digitization, shrinking operational budgets, and expanding cyber threats are driving engineers to drastically improve how their systems are connected, orchestrated and secured. A modernized and secure industrial network is crucial for this evolution. In this session, you will learn how to leverage Catalyst SD-WAN and SD-Routing with the Cisco Catalyst IR1101, IR1800 and IR8340 Rugged Routers to help you reach the next level of secure and intuitive operation in your industrial networks. Vertical architectures covered will include Utilities, Roadways, Rail, and Oil and Gas.

### Streamline Your Success: Automating OT Services with Cisco Catalyst Center Best Practices - BRKIOT-2016
Speakers: Hailu Meng (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271953961001zItn
The Operations Team in your industrial networks (eg: manufacturing) are trying to improve overall equipment effectiveness (OEE), quickly introduce new product (NPI), and prevent product line shutdowns due to cybersecurity attacks. This session will show you how to transform the OT network infrastructure with your IT expertise to meet these business requirements. In this session, you will learn how to leverage Cisco Catalyst Center to deploy at scale popular OT services deployment such as Secure Equipment Access and Cyber Vision. You will also learn best practices for implementing industrial protocols, QoS, and managing your OT network with Cisco Catalyst Center.

### Streamlining Fiber Installation with Direct Mating Breakouts - CNCDCN-1020
Speakers: Ribal Btaddini (Legrand)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271876055001zMfj
Discover how Legrand's acclAIM fiber solution drastically reduces installation time and complexity with direct mating connections. Understand how this ultra high-density solution enables sustainable scalability and flexibility, doubling the density compared to LC connectors, without expanding the data center footprint.

### Supercharge Threat Detection with Cisco XDR and Identity Intelligence - DEVNET-2863
Speakers: Ahmadreza Edalat (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271907525001zEyV
See how Cisco XDR and Cisco Identity Intelligence work together to transform identity signals into powerful security insights. Through streamlined automation workflows and webhook integrations, identity-related alerts flow directly into XDR—enriching context, tightening detection, and accelerating response. Join us for a step-by-step walkthrough of the integration in action, and discover how effortless and effective identity-driven threat detection can be.

### Sustainability and AI: Strategies for the Future of Compute and Networking - BRKGRN-2005
Speakers: Faisal Azizullah (Cisco), David Stanford (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271945891001zJhp
When planning a new data center or upgrading an existing one, numerous factors must be considered to advance sustainability and efficiency. In this session, key considerations such as energy consumption, space utilization, heat generation, CPU core optimization, and advanced cooling strategies for IT equipment will be explored. By leveraging advanced tools, we aim to craft state-of-the-art computing platforms that meet contemporary demands. A real-world case study will illustrate how these strategies have been successfully implemented, providing concrete evidence of their impact on energy efficiency and cost reduction. This session will equip you with practical strategies for improving energy efficiency, optimizing total cost of ownership, and leveraging AI-driven tools to enhance performance. Join us to gain expert knowledge and actionable insights to stay ahead in the evolving landscape of data center design.

### Sustainability and Circular Design in Cisco's Newest Products - BRKGRN-1625
Speakers: Kelsi Doran (Cisco), David Stallings (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271945655001zlwl
As an IT decision maker, are you being asked to reduce your infrastructure's impact on the environment, all while keeping costs down, maintaining performance, and supporting increase AI/ML workloads? If so, we want to introduce you to circular design—which can help to keep your hardware in service longer, lower your energy consumption, reduce e-waste, and preserve natural resources. To understand this concept, we will demonstrate some of Cisco's newest generation products to learn how they incorporate Circular Design Principles—such as more efficient power supplies, reduced plastic content, foam-free packaging, and more. Cisco has a goal to design 100 percent of new products and packaging using Circular Design Principles by the end of its 2025 fiscal year, and you will learn how the concept of circular design can help you address your business and sustainability goals. The session will include a live, engineer-led demo of how Cisco's Circular Design Principles are being applied to Cisco's newest products.

### TAC and Engineering on Cisco Secure Firewall Threat Detection Performance - Performance Profiling tools, Tuning and Best Practices - BRKSEC-3274
Speakers: Foster Lipkey (Cisco), Costas Kleopa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272013348001zshf
Unlock the full potential of your network security with expert guidance at Cisco Live! Dive into the dynamic world of firewall optimization, where the mantra "set it and forget it" becomes a tale of the past. Join us for a compelling breakout session where we transform routine maintenance into a strategic advantage for your network's defense. Experience the thrill of mastering your firewall's performance as we equip you with insider knowledge on configuring threat detection, leveraging the collective wisdom of Cisco's TAC and Engineering teams. Discover the latest innovations that allow you to proactively identify and resolve performance issues with surgical precision. This session promises a treasure trove of real-world scenarios, showcasing the immediate impact of applying these tools and best practices. You'll walk away with a robust set of strategies to enhance your firewall's effectiveness and ensure it operates at the zenith of its capabilities. Key Takeaways: Embrace the most effective firewall performance best practices validated by Cisco TAC and Engineering Explore cutting-edge features that revolutionize monitoring and profiling, giving you a crystal-clear insight into your firewall's health Learn through practical examples how to seamlessly integrate these practices and tools into your security framework for optimal performance Join us for an interactive journey to elevate your firewall maintenance from routine to remarkable, and become the vanguard of your network's security at Cisco Live! Please note: This is not an introductory session. It is expected that attendees have deployed Cisco Secure Firewall using the Snort Threat Detection featureset.

### Talking with Giants: A Conversation with Some of the Key Contributors to the Development of Cisco and the Internet - BRKNWT-1413
Speakers: LJ Wobker (Cisco), Mark Townsley (Cisco), Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271972558001z5t3
Ever wanted to hear from some of the key engineers who built Cisco and the Internet? Didn't think it could ever happen? In this deep-dive, interactive, and fun technical give-and-take geek-out session, we will host two of Cisco's top technical talents - to talk about the how and why of the decisions they made, and to get their insight into what's coming next. Dave and Peter, two Distinguished Engineers and Distinguished Speakers will be your moderators, and gently steer the conversation. Join us for a fun, interactive, intimate, and fast-paced session with some of the giants of networking!

### Tap the full power of Generative AI in Splunk using AI Assistants and the Machine Learning Toolkit - BRKOBS-2014
Speakers: Damian Herrick (Cisco), Jeff Wiedemann (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271982889001zC0Z
The rise of Generative AI (GenAI) is reshaping how we approach problem-solving, productivity, and innovation. This session covers the foundational and emerging concepts driving GenAI, with a focus on its practical application in Splunk. In this session we'll go deep into how Splunk has applied these concepts to build an AI Assistant that produces the most accurate and personalized SPL queries from natural language prompts. And, how you can apply these same concepts to harness the full power of generative AI in Splunk. Join us to navigate emerging best practices and learn how to integrate them seamlessly into your Splunk workflows.

### Tech Mavericks: Crafting a Stellar Tech Career with Passion and Persistence - IF-1034
Speakers: Tia Stackle (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949993001z8sD
In today's tech industry, diverse paths are paving the way for new leaders. This session is tailored for both hiring managers trying to improve their team and individuals looking to make their mark as unconventional talent in the tech field. Participants will discover how Cisco certifications and other non-traditional educational paths can lead to extraordinary achievements in the tech industry. you'll learn about the pivotal role sponsorship plays, and the value of hiring managers who see potential beyond resumes. you'll walk away with actionable insights and innovative strategies to carve out your own unique path to success. (And yes, we will be talking about AI!) This session promises insight, inspiration, and practical advice on breaking barriers and innovating leadership to connect everything securely, making anything possible.?

### Ten Reasons why you think you need an Optical Network, but you don't ! - BRKMSI-2000
Speakers: Christian Schmutzer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271962293001zoqG
Optical transmission technologies are important to deploy your network over and squeeze as much capacity as possible out of your fibre infrastructure. However do those networks need to be so complicated? Are complex ROADM systems and OTN switching really needed? In the end we carry IP/Ethernet traffic, why not use a IP/MPLS network? ... In this session we will shed light on ten reasons people give for why this won't work 1. Latency 2. Bandwidth commitment 3. Co-routing 4. Transparency 5. Low cost 6. Protection & restoration 7. Performance monitoring 8. OAM (fault indication) 9. Security (encryption) 10. Capacity / spectral efficiency ... and discuss if it really doesn't or in fact does workl!

### The AI Enablement Framework: Year 2 of Cisco's Journey - AIHUB-2011
Speakers: Daryl Thomas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271836816001zmb5
In this session, we will share Year 2 insights and experiences from Cisco's journey to enable AI across the organization. Building on our AI Hub presentation at Cisco Live 2024, we will highlight our progress, challenges, and lessons learned, showcasing how the Cisco Demand Systems & Data and Virtual Demand Center (VDC) teams are leveraging AI solutions through the "AI Enablement Framework," anchored by Cisco's AI Readiness Index. What You'll Learn: Participants will gain a deeper understanding of our transformative journey from 2023/2024 to today. We'll explore how the "People, Process, and Platform" model was integral to selecting, resourcing, and enabling AI solutions while adhering to Cisco's Security & Trust principles, AI Governance policies, Procurement standards, and leadership across Cisco BridgeIT, Product Management, and Sales & Marketing.

### The Best AI Device You Don't Have - ITLGEN-2050
Speakers: George Bentinck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271956097001zKcy
What if you could quantify physical aspects of your organization as well as you could for digital ones? Cisco's MV Smart Cameras process more than a billion inferences a day for customers with Far Edge AI. Scaling to any size with no servers, no GPUs, and no video in the cloud, this enables your security camera to become a sensor for the enterprise. This session will cover why Far Edge AI is critical for IT organizations wanting to avoid their projects stalling in proof of concept. It will cover the state of the art in Far Edge AI, real world examples of customer solutions, and an outlook on the future of accelerated AI workloads in the distributed enterprise.

### The Engineer Experiences for Cisco Nexus Hyperfabric - DEVNET-1454
Speakers: Lionel Hercot (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271895936001zhyr
In this session, we will go over the different user experiences that Cisco Nexus Hyperfabric, Cisco's SaaS-based Data Center Networking solution, offers for Engineers managing it to best suits their needs. We will focus on the automation and programmability capabilities offered by the solution so you can find the right experience for your needs. We will cover experiences from API to Inventory-driven and much more. Join us for an exploration of Hyperfabric automation capabilities and prepare yourself to get in the Hyperfabric journey!

### The Fastest Path to Successful AI Deployment - CNCDCN-2008
Speakers: Craig Waters (Pure Storage)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271876250001zqpE
Delivering on the promise of AI-driven business growth remains challenging; Mostly because the infrastructure itself has been complicated, expensive, and fraught with pitfalls like massive power requirements and the need for specialized skill sets. But if you're a Cisco UCS user, we have great news for you! With Pure Storage & Cisco's FlashStack AI PODs you can leverage proven Cisco Validated Designs to quickly deploy pre configured AI solutions using the same FlashStack servers and Intersight management you already know, with the same IT skills you already have and you can run AI simultaneously in FlashStack alongside your conventional workloads. Join us and learn more about how Pure Storage can help you on your AI journey.

### The Future of AI: Sustainability, Security, and Inclusion - IF-1025
Speakers: Saumya Dubey (Cisco), Chelsea Racelis (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949400001zuJP
How can Artificial Intelligence shape a future that is more sustainable, secure, and inclusive? Discover how to leverage inclusive design principles to transform technology. By fostering diverse teams, utilizing high-quality data, and applying innovative design strategies, we can effectively address bias in large language models (LLMs). This session explores the role of AI-driven insights in overcoming key challenges and unlocking new capabilities for building more secure and sustainable technical solutions. Through tangible examples, We'll demonstrate how our customers and partners play a crucial role in creating a digital future that benefits everyone. This session welcomes all —moving beyond buzzwords to deliver practical insights that inspire real-world impact.

### The Future of Agentic AI with MCP - CISCOU-2070
Speakers: Arjun Sambamoorthy (Cisco), Robert Barton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271843657001zUUC
Agentic AI is reshaping how network and security operations will be managed. Central to this is the emerging Model Context Protocol (MCP). In this session, you will learn important concepts of Agentic AI systems, their building blocks, and how MCP is giving a new framework to accelerate and scale deployments.

### The Future of Energy and the Influence of AI - PP-1301
Speakers: Kelsi Doran (Cisco), Steven Santini (Schneider Electric)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893399001z2H6
As AI and other factors drive up energy demand, businesses must adapt their strategies to respond to rising costs, regulatory shifts, and increasing pressure to meet sustainability and compliance requirements. Companies that modernize their IT infrastructure with digital technologies can improve efficiency, cut costs, future-proof their operations and unlock new efficiencies. This session will explore how businesses can turn the energy challenge into a competitive advantage, leveraging digital innovation to drive energy efficiency, cost savings, and growth in an AI-powered world. We will look at the innovations and infrastructures available today and discuss how digital technologies can play a role in energy security in the future.

### The Future of Manufacturing: Secure, Reliable, AI-Ready Network Architecture - BRKIOT-2720
Speakers: Prasham Maniar (Cisco), Alice Masini (Cisco), Arun Siddeswaran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271954949001zexG
Dive into validated AI-ready, reliable and secure industrial architectures in our expert-led session. Discover the latest Cisco innovations in Industrial Switching and Ultra Reliable Wireless Backhaul and learn how the Cisco Connected Factory solution enables industrial companies to build a unified, converged, and rugged network connecting plant operations with business systems. This provides a foundation for AI, industrial wireless for AGVs/AMRs, and cybersecurity initiatives. Enriched with technical insights on validated reference architectures, best practices, and real-world case studies, this session is tailored for customers developing network solutions for control networks in manufacturing and other industrial environments, aiming to enhance visibility, increase efficiency, and strengthen security with a defense-in-depth approach. Join us to shape the future of your company's network architecture!

### The Future of Reskilling for AI - ITLGEN-2054
Speakers: Chris Rowen (Cisco), Alex Pujols (Cisco), Annie Hardy (Cisco), Kristin Wisnewski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271959232001znEt
To truly reskill a workforce takes more than online courses: it takes collaboration between teams, strategic pathways to evolving careers, and a learner-centered approach. In this conversation, Annie Hardy, Global AI Architect, will be joined by Alex Pujols (VP of Engineering, Global Partner Engineering), Kristin Wisnewski (VP, IT Design), and Chris Rowen (VP of Engineering, Collaboration AI) in a conversation that delves into the diverse ways different teams have reskilled workers with increasingly important digital skills. Leave with a better understanding of divergent approaches to evolving the teams for the age of AI, and with actionable next steps to take back to your own company.

### The GenAI Journey: From Machine Learning to the Agentic Internet - BRKETI-1005
Speakers: Ivan Padilla Ojeda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271914705001zAue
In the dynamic landscape of enterprise operations, the integration of Generative AI heralds a transformative era of innovation and efficiency. This cutting-edge technology empowers businesses to not only analyze and understand data but to also create novel solutions and content. Cisco is introducing its new service allowing the secure access to all these GenAI resources, providing the IT departments with all the necessary tools for policy, control and billing. Cisco streamlines the integration of Retrieval-Augmented Generation processes, enabling enterprises to enhance their content creation capabilities by blending learned data with real-time information and creating a dynamic and responsive approach to generating context-aware content

### The Hitchhiker's Guide to Troubleshooting IPv6 - BRKENT-3340
Speakers: Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271935338001zB0V
Are you about to deploy IPv6 in your enterprise network? Afraid that you do not have enough experience yet? Don't panic. In this session, we will cover easy mistakes being made, the various states of an address, RA throttle host aAttachment, NPv1 and NP2, and we'll dig into Wireshark.

### The Hour of Networking - DEVNET-1414
Speakers: Andrea Verrengia (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271895735001zjNg
Have you ever tried to explain to a child what do you do for living? Right... it's hard. This session will make your life easier! We will experience network automation from a different angle, we'll build a game to introduce children to networking! After this session, you will be able to schedule and deliver your own 'Hour of networking' with your community and start building a bridge between our daily job and our future generations. Join this session if you willing to see something different and if you want to play a role in child education.

### The Inner Workings of QoS for Wi-Fi 7 Networks - BRKEWN-2060
Speakers: Robert Barton (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941425001zVqa
This session will guide you through the fascinating but complex subject of QoS for wireless LANs, with a special emphasis on the foundational elements that will allow you to effectively deploy QoS in your wireless LAN. The session will begin with a discussion of the underlying wireless QoS standards, including IEEE 802.11e and WMM. Next, we will do a deep-dive into the innerworkings of QoS for Wi-Fi 6 (802.1ax) and Wi-Fi 7 (802.11be), and how these differ from legacy QoS. This session will examine end-to-end QoS design principles and how to correctly align these to the challenges presented by the wireless QoS standards. We will examine QoS deployment recommendations when using Cisco Wireless solutions

### The Intelligent Network: Demystifying AI's Impact on Enterprise Operations - CNCNWT-1009
Speakers: Jeff Ehrenhart (ConvergeOne)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271972369001zPLt
Ready to take your enterprise network operations to the next level? Join Jeff Ehrenhart and his C1 team as they demystify how advisory assessment services pave the way for impactful AIOps adoption. They'll break down the complexity of modern networks and showcase how strategic assessments uncover bottlenecks, explore predictive maintenance, define security elements, and document resource allocation. Through real-world insights, they'll show you how to move from reactive troubleshooting to proactive, AI-driven strategies. Learn how to build towards an intelligent, automated approach that boosts efficiency, cuts costs, and strengthens resilience. Don't miss this engaging session designed to demonstrate how AIOps can empower your team and transform your operations with confidence and clarity.

### The Internet of Agents: Building an Open and Interoperable Agentic AI Ecosystem - BRKETI-1009
Speakers: Guillaume De Saint Marc (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271915084001zCYa
As AI evolves from isolated, hosted models into networks of specialized agents working together, we face a fundamental infrastructure challenge. The proliferation of agentic frameworks raises barriers to interoperability across the Internet which threatens the potential of this transformative technology. Drawing from Cisco's legacy of building the foundations of the Internet, Outshift is leading an industry collaboration to develop the Internet of Agents - a suite of infrastructure technologies that will shape the future of agent AI applications at scale. This session will discuss the challenges facing multi-agent applications, introduce this new architecture, and showcase how these open, interoperable standards and services are crucial to innovation in the age of AI.

### The Journey to Terabit Transport Solutions - BRKOPT-2019
Speakers: Maurizio Gazzola (Cisco), Lorenzo Ghioni (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271967559001zpZL
This session aims to describe how Cisco is leading the rush to the terabit transport era and how we are doing so by leveraging automation to make things simpler rather than more complex. The latest innovations with Open Line System (NCS 1010), WDM Transport (NCS 1014), and Digital Coherent Optics will be presented, along with some real-life examples of deployments that showcase our leadership in this space.

### The Latest in Cisco Secure Access (SSE) Innovation - BRKSEC-2285
Speakers: Jonny Noble (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272002725001z3N1
Join this session for a closer look at the latest innovations in Cisco Secure Access, including our leading ZTNA client-based and clientless capabilities, simplified policy management, and a unified client that removes the frustration of secure connections for your hybrid workforce. The session will dive into details of recent innovations such as Hybrid ZTA, AI Access, CII integration with Secure Access, policy assurance, enterprise browser, One-SASE, and the latest cloud infrastructure updates. We will also touch on other areas of value-added incremental features, integrations, AI-based innovations, and other differentiation that have been provided to Secure Access customers over the last few months.

### The Network of the Future is Here - Let's Automate your IPv6 deployment with Python! - BRKOPS-2223
Speakers: Juulia Santala (Cisco), Nicole Wajer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988387001zybL
IPv6 marks a new horizon in the world of networking, promising limitless IP addresses and enhanced network performance. It is time to embark on this journey - but let's do it the right way from the beginning: using automation! In this 90 minute breakout you will learn how to plan your IPv6 transition and how to use Python to automate setting the plan into action. You will learn about the must knows of IPv6 as well as useful Python libraries that can help you on this journey, and see practical real life Python examples of deploying IPv6 configurations in your network. Workflow decisions such as automated testing and sources of truth will also be covered. This session is designed for network engineers who have a need to start implementing IPv6. The session's target audience has little or no prior experience with Python automation and is fairly new to IPv6 as well.

### The New CDO Public API - DEVNET-1281
Speakers: Aaron Hackney (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271894748001zY1c
In this session, we introduce the new CDO Public API, a RESTful API built from the ground-up to simplify, streamline, and automate your network security operations. The CDO Public API is targeted at people who need to perform automated, often repetitive configurations and manage security policies at scale across multiple tenants. Our new API provides a simplified, documented user experience. As part of this session, we will demonstrate using the public API to: Set up a fully working CDO tenant with devices onboarded. Monitor baseline configurations across their entire security portfolio, and quickly pinpoint when, how, and by whom changes were made to their security posture. Upgrade their devices. Execute arbitrary CLI commands across multiple CDO-managed devices. Monitor Remote Access and Multi-factor Authentication events. We will additionally touch upon how you can elevate the level of abstraction of your automation using SDKs, our Terraform provider, and our Ansible collection.

### The New Digital Substation: More Efficient, More Secure, and Ready for Demanding Modern Grid Applications - BRKIOT-2015
Speakers: Dan Madey (Cisco), Marcus Smith (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271953765001zzhr
The new Substation Automation solution architecture overhauls the substation network to drive out costs, improve security, and support demanding new smart grid applications, while reliably providing control and visibility of substation operations. In this session, we will review the updated network and security architecture, which is enhanced with new industrial routing (IR8300) and switching (IE9300) infrastructure, runs industrial cybersecurity with Cisco Cyber Vision, supports multiple WAN options including SD-WAN, and deploys software-defined network management with Cisco Catalyst Center (formerly DNA Center) and Catalyst SD-WAN Manager (formerly vManage) to reduce maintenance effort, increase uptime, and simply and consistently deploy the network. The solution has rich cybersecurity features, such as establishing an Electronic Security Perimeter for critical substation systems, deploying TrustSec-based micro-segmentation, and providing the visibility of substation devices and protocols with Cyber Vision.

### The New, Encrypted Protocol Stack Taking over the Internet and How to manage User Quality of Experience - BRKSPM-2024
Speakers: Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271969091001zE6e
Network traffic is transitioning from TCP to QUIC very fast, QUIC being 50% of total traffic and doubling every 18 months. QUIC, with HTTP/3, DoH, and eSNI/ECH, obfuscates the traffic between applications and changes flow behavior with applications now disintermediating the network. Application visibility is eliminated by this stack, congestion management transitions to the application and the key assumptions SP networks are built on are rapidly being obsoleted. In this session, we will show how this protocol stack is constructed and evolving, its behavior in terms of both visibility and flow control, and the impact it has on infrastructure elements. We will also discuss the techniques SPs can use to keep pace with it, enabling better traffic visibility, QoE, and efficient use of 5G spectrum and other scarce resources.

### The Next Generation Workplace Done Right: Liberty Mutual and Cisco Spaces - CSSEWN-1010
Speakers: Vincent Kasabian (Liberty Mutual)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271872901001zgae
Like many organizations today, Liberty Mutual, a leading insurance provider, sees the value of in person collaboration, and building culture in the workplace. They also recognize the needs of the office, and the expectations of the workplace, have changed dramatically. Vin Kasabian, senior wireless architect, will explain how Liberty Mutual has strategically and effectively leveraged their investments in WIFI6 and Cisco Spaces to build a bridge between technology and real estate teams. He will explain how the teams can now make data and analytics driven decisions around workplace designs- decisions such as office layouts, room designs, even the type of equipment to outfit a given space, all derived from user and occupancy trends. Learn how Vin and the team have gained additional insights from existing standards with the introduction of Spaces into the environment.

### The OT Security Journey: Network Visibility, Segmentation, and Investigation/Response - BRKIOT-2029
Speakers: Kevin Holcomb (Cisco), Andrew McPhee (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271954341001zhPy
Protecting industrial assets from cyber threats is of paramount importance in today's world. This is very much a journey and not a destination. Join this session to traverse the journey from gaining visibility into your OT network, segmenting the network to reduce lateral attacks, and investigating/responding to incidents. You will learn how to use products such as Cisco Cyber Vision, ISE, Secure Firewall, and Splunk to help improve OT security posture.

### The Power of Cisco SD-Access LISP Fabric: Simplified Deployment to Advanced Use Cases - Part 1 - BRKENS-1804
Speakers: Mahesh Nagireddy (Cisco), Devi Bellamkonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271923017001zVPu
Join us for an action-packed, demonstration-driven session focused entirely on the deployment of Cisco SD-Access LISP Fabric. This two-part series is designed for professionals with prior knowledge of SD-Access, diving straight into real-world deployment workflows using the controller — no theory, just hands-on execution. Through demonstrations, we will showcase step-by-step deployment processes, best practices, and advanced configurations to help you streamline your SD-Access fabric implementation. BRKENS-1804 -Part 1 BRKENS-2804 - Part 2 Part 1: Deploying a Scalable & Secure SD-Access Fabric • Automate network setup with LAN automation & zero-touch switch onboarding. • Integrate Catalyst Center with Identity Services Engine (ISE) for seamless policy control. • Execute the overlay bring-up process for end-to-end connectivity for wired and wireless hosts. • Implement group-based policy segmentation for optimized security. Part 2: Advanced Deployments & Real-World Scenarios • Demystify the LISP pub/sub control plane.. • Implement dynamic default border and active backup internet solutions. External access using LISP extranet deployment. • Demonstrate Multi-Catalyst Center and ISE integration for enhanced management. • Ensure success with a comprehensive verification process. This session is purely focused on demonstrations—no theoretical discussions. If you're ready to see SD-Access LISP Fabric in action and gain practical expertise in real-time, this is the session for you! Join us to learn from real-world customer experiences and elevate your understanding of Cisco SD-Access design and deployment best practices. And remember, laughter is the best protocol!

### The Power of Cisco SD-Access LISP Fabric: Simplified Deployment to Advanced Use Cases - Part 2 - BRKENS-2804
Speakers: Mahesh Nagireddy (Cisco), Devi Bellamkonda (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271924197001zFWZ
Join us for an action-packed, demonstration-driven session focused entirely on the deployment of Cisco SD-Access LISP Fabric. This two-part series is designed for professionals with prior knowledge of SD-Access, diving straight into real-world deployment workflows using the controller—no theory, just hands-on execution. Through demonstrations, we will showcase step-by-step deployment processes, best practices, and advanced configurations to help you streamline your SD-Access fabric implementation. BRKENS-1804 -Part 1 BRKENS-2804 - Part 2 Part 1: Deploying a Scalable & Secure SD-Access Fabric • Automate network setup with LAN automation & zero-touch switch onboarding. • Integrate Catalyst Center with Identity Services Engine (ISE) for seamless policy control. • Execute the overlay bring-up process for end-to-end connectivity for wired and wireless hosts. • Implement group-based policy segmentation for optimized security. Part 2: Advanced Deployments & Real-World Scenarios • Demystify the LISP pub/sub control plane.. • Implement dynamic default border and active backup internet solutions. • External access using LISP extranet deployment. • Demonstrate Multi-Catalyst Center and ISE integration for enhanced management. • Ensure success with a comprehensive verification process. This session is purely focused on demonstrations—no theoretical discussions. If you're ready to see SD-Access LISP Fabric in action and gain practical expertise in real-time, this is the session for you! To get the most out of this session, we suggest attendees brush up on the Cisco SD-Access architecture through our previously recorded sessions, BRKENS-2810,BRKENS-2811,BRKENS-2814 available in the Cisco Live On-Demand Library. Join us to learn from real-world customer experiences and elevate your understanding of Cisco SD-Access design and deployment best practices. And remember, laughter is the best protocol!

### The Power of Extending SD-WAN to OT Networks - PSOIOT-1041
Speakers: Jenifer Piccioni (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271951966001zNsh
SD-WAN can make it easy to unify your management and security across the enterprise and operational edge. Whether it's traffic intersections, utilities substations, windfarms, and more - with Cisco IIoT, businesses can achieve greater visibility, control, and efficiency in their industrial operations, while reducing downtime, and improving safety. If you are using SD-WAN in the enterprise, it's a small step to extend to the industrial space with our Catalyst industrial routers. Come and see how this shared management experience delivers the robustness and simplicity you need to easily and securely manage your IT and OT networks as one.

### The Quantum Revolution is Closer Than You Think: How Cisco is Building the Future While Securing Today's Networks - CENETI-1031
Speakers: Vijoy Pandey (Cisco), Anthony Grieco (Cisco), Bill Gartner (Cisco), Ramana Kompella (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592612749001X64Z
Quantum computing is rapidly evolving from theoretical science to practical reality, with Cisco leading the charge to accelerate development through networking innovation. As quantum threats loom on the horizon, organizations face a dual challenge: preparing for transformative quantum opportunities while protecting existing infrastructure against quantum-enabled attacks.? This dynamic panel discussion explores Cisco's comprehensive quantum strategy. You'll leave this session with insights to help you: Discover Cisco's Quantum Network technologies powering the next generation of quantum computing? Learn how Cisco's quantum networking approach enables building Quantum Data Centers for scaling out quantum computers to support practical applications? Explore real working innovations from Cisco's Santa Monica Quantum Labs? Understand the implications of practical quantum computing for your organization's long-term strategy. Join our distinguished panel featuring executives from our Cisco Quantum Lab, Cisco Research and Cisco Optical Systems & Optics as they debate quantum's real-world timeline and demonstrate Cisco's practical approach. Basic understanding of networking principles recommended, but no quantum physics experience required!?

### The Software-defined Factory Enabled by SDA - BRKIOT-2299
Speakers: Thomas Kampa (Audi AG), Erika Franco (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271954529001z4F0
This presentation explores the application of Software-Defined Access (SDA) technology in industrial automation environments. It aims to provide a comprehensive understanding of when SDA is a suitable choice, its limitations, and practical guidelines for deploying SDA in industrial automation networks. The session will feature Audi, showcasing their innovative approach to virtualizing Industrial Automation and Control Systems (IACS) hardware. By leveraging hyperconverged infrastructure and SDA, Audi is creating efficient virtual environments that connect seamlessly to the plant floor. We will cover: Common Deployment Models Industrial Network Management with Catalyst Center Operational Considerations Known limitations Audi Use Case By the end of this session, you will understand how to introduce SDA in manufacturing and gain a clear vision of what the factory of the future could look like.

### The Streaming Data Pickle in Observability Cloud Detectors - TACOBS-2002
Speakers: Katie Johnson (Cisco), Renzo Cafferata (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977983001zu05
This technical learning session delves into the intricacies of Splunk Observability Cloud detectors, focusing on the pivotal streaming concepts of minimum delay, maximum delay, and minimum resolution. I will explain how these parameters play a crucial role when analyzing incoming data streams, and how they can alter alerting behavior. This session will equip you with the essential tools and insights to effectively analyze and optimize your own detectors. Additionally, it will guide you on how to efficiently gather information to engage support services, ensuring you receive assistance when necessary.

### The Swiss Army Knife of Cloud Native Networking - BRKCLD-1012
Speakers: Raymond De Jong (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271845187001zhhH
Join us to explore how Cilium, powered by eBPF, enhances multi-cloud and multi-tenancy networking capabilities. In this session, we will dive deep into Cilium's advanced features, including BGP, Load Balancing, LB IPAM, and Network Policies, showcasing how they deliver secure and scalable networking solutions. Discover how Cilium allows for efficient routing and connectivity between Kubernetes clusters and external networks and you'll learn the setup and configuration of BGP with Cilium including its adaptability to different network topologies. Additionally, learn about Cilium Load Balancing capabilities, which offer high availability for applications. Understand its integration with LB IPAM and how it enables platform engineers to configure multi-tenancy routing with multiple IP pools for assigning Load Balancer IPs. Whether you are a Platform or Network Engineer, this session will equip you with the knowledge and tools to optimize your Kubernetes networking architecture with Cilium.

### The Three States of Network Compliance Testing (Live!) - CISCOU-2069
Speakers: Palmer Sample (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271843463001zJ1v
Desired state, configuration state, operational state. Three terms that we are all familiar with as network engineers, but how do they translate to an automated world? In this session, we will discuss the relationship between the three network states and how automated testing can make your life easier. Practical demonstrations will be performed using a variety of tools, and participants will be exposed to the benefits and drawbacks of different testing approaches.

### The Ultimate MS Teams Upgrade: Unleashing the Power of Cisco Video for Microsoft Teams - CTF-1033
Speakers: Chris Fowler (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271849354001zkUn
Transform your Microsoft Teams meetings with Cisco's premium video solutions! This dynamic session reveals how to create exceptional meeting experiences across conference rooms, huddle spaces, and personal workspaces. In this action packed session, you'll discover: . Seamless Integration Secrets: Master multiple pathways to Teams meetings (WebRTC, CVI, MTR) and choose the perfect approach for your environment . Architecture Deep Dive: Explore the powerful MTR on Cisco devices architecture that delivers superior experiences . Admin Superpowers: Leverage Cisco Control Hub alongside Teams admin to unlock advanced capabilities your IT team will love . Smart Spaces Revolution: Transform ordinary devices into intelligent room sensors for game-changing workspace analytics Don't miss this opportunity where you'll learn from real-world success and walk away with immediately applicable skills!

### The Value of the CCNA for EVERY Engineer - Yes that Means You! - BRKCRT-1004
Speakers: Bryan Byrne (Cisco), Hank Preston (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271833945001zzHa
In the ever-evolving world of technology, it's crucial for engineers to stay ahead of the curve and possess a diverse skillset to thrive in the ever-changing landscape. While specialization is essential, the ability to understand and interact with networking fundamentals is a valuable asset across all disciplines. This is where the Cisco Certified Network Associate (CCNA) certification comes into play. The CCNA certification is the industry standard for networking fundamentals, providing a comprehensive understanding of networking concepts, protocols, and technologies. Whether you're securing the network, enabling collaboration or just living the cloud the CCNA can provide you with knowledge to make you a more well-rounded engineer.

### The Webex Cloud Platform: Infrastructure, Data Residency and Connectivity - BRKCOL-2990
Speakers: Stefano Giorcelli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857786001zSsF
Have you ever wondered what's really inside the Webex cloud-shaped icon you often see in network diagrams? Do you want to understand how Webex reliably delivers cloud Collaboration services to customers around the world? Come and join us for a guided tour of the Webex cloud platform and learn about the following topics: geographic distribution of Cisco Webex data centers and Webex services how Cisco Webex data centers (and IaaS providers used by Cisco) are built to deliver specific services types of availability models for Cisco Webex workloads cloud-native platform layer shared Webex services (identity, analytics, key management service, speech and language AI) how your provisioning choices determine data residency for different types of personal data where and how the Cisco Webex backbone interfaces with the public Internet (including some information on IPv6 support) how the Webex network edge is structured and what connectivity options are available to customers and partners

### The next Horizon for Splunk APM: creating the best tool for any environment and any infrastructure - BRKOBS-2011
Speakers: Deena Shanghavi (Cisco), Charlie DeMarco (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271981136001zkcB
Discover how Splunk Observability APM realizes the vision of comprehensive observability across your entire application and infrastructure landscape. This presentation will showcase a single platform solution for monitoring n-tier and microservices architectures, as well as diverse infrastructure environments including VMs, cloud, and Kubernetes. Learn how new features empower you to proactively identify and resolve critical business issues, minimizing downtime and maximizing performance. Live demonstrations will highlight these capabilities.

### The power of two: Simplifying Cisco Hyperconverged deployment expansions and management using Intersight Cloud Management and Nutanix Prism Central - BRKCOM-2026
Speakers: Rupesh Chakkingal (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271860067001z5eY
By 2025, Gartner predicts that half of all enterprise data will be created and processed beyond traditional data centers and clouds, with edge computing projected to surge by 75%.This shift towards hyper-distributed IT demands innovative approaches to infrastructure deployment, management, and operations in our hybrid multi-cloud landscape.The Cisco-Nutanix partnership addresses these challenges while unlocking new opportunities through a powerful integration of Cisco Intersight and Nutanix Prism Central (Power of Two). This solution establishes a unified cloud operating model for distributed infrastructure. In this session, we'll explore comprehensive lifecycle management capabilities, including initial cluster deployment and expansion, cluster upgrades and newly added capability - Nutanix Prism Central as an Intersight Managed Target allowing new Day-1 management capabilities in Intersight.This exclusive integration sets the foundation for continued innovation between Cisco and Nutanix, paving the way for exciting future developments.The session was also cover the overall integrated support model and experience. For anyone designing distributed infrastructure solutions across data centers and edge computing environments, this session is essential

### ThousandEyes and Webex Assure Seamless Collaboration for Insight Global - CSSCOL-1005
Speakers: Marko Tisler (Cisco), Chris Cavendish (Insight Global)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271872332001zsWA
In the moments that matter, like recruiting the next top talent for your company, you need collaboration tools that work. Insight Global wants every collaboration experience in their company to be seamless and represent the quality of their HR and staffing services. Insight Global relies on Cisco Webex for crystal-clear calling, lifelike video, and instant communications. They assure these experiences with Cisco ThousandEyes, proactively monitoring their owned and unowned networks to help resolve issues before they impact their employees and customers. Join this session to hear how ThousandEyes and Webex power user Chris Cavendish, Network Operations Manager at Insight Global, works to proactively assure all collaboration experiences including: clear communication with Webex Calling, hybrid work with Webex Meetings, and engaging office experiences with RoomOS on Cisco devices

### ThousandEyes: Assurance in Focus - BRKOBS-1017
Speakers: Christopher Hunt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272016505001z9lo
With your network and the internet's escalating complexity, does troubleshooting often feel like an overwhelming search for a needle in a haystack? What if you could be warned of an impending issue before your users notice? In this session we will show how Cisco ThousandEyes can help by providing deep, end-to-end visibility extending through your networks and across the internet. This insight ensures your most important business functions perform optimally, significantly reducing downtime, and helping you deliver exceptional experiences to customers and users. In this session you can expect to see real world demos, discuss practical use cases, and walk through the many seamless integrations across the entire Cisco portfolio providing insight into Enterprise networking, Wireless, Meraki, Collaboration, Security and Observability. We will also reveal some of the exciting new innovations, and even a sneak peak into the roadmap. Come to our session to see firsthand why ThousandEyes is the gold standard for digital experience assurance and how you can put it to work, saving valuable time for you and your business.

### Topology Aware Network Configuration Automation Using Multi-agent LLM framework with GraphRAG - BRKATO-2200
Speakers: Debashis Kundu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271832274001zawZ
In this session, we'll explore the power of multi-agent workflows in automating network configuration life cycle management using GenAI's framework. We'll demonstrate how to leverage multiple agents working together to streamline the process from generating config templates, pushing to Git, and creating Cisco NSO XML templates, all the way to testing and deploying changes to production based on user input. Join us as we dive into the world of multi-agent workflows for infrastructure as code and discover how this innovative approach can simplify your network configuration management, reduce errors, and increase efficiency.

### Transform your Network Automation Apps with GenAI - DEVNET-3419
Speakers: Gabi Zapodeanu (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271910266001zbds
Are you looking to simplify network management using Generative AI and Catalyst Center APIs, to transform your existing Infrastructure-as-Code Apps? Participants will learn how to innovate, enhancing existing network automation apps using Generative AI, to transform and simplify network management. We will review practical ways to integrate GenAI with your apps calling Catalyst Center APIs, for faster network management, at scale. The session will start by introducing the audience to AI code generation capabilities, using the Python SDK and Ansible playbooks for Catalyst Center. The second part of the presentation will review Function Calling and how to create a Natural Language interface for your current network automation app stacks. The use cases will explore the options to use Cloud based or on-prem LLM models. Demos and Python sample code are included.

### Transforming Communications: Cisco IT's Strategy with the Webex Collaboration Suite for Enhanced Calling and Contact Center Solutions - BRKCOC-2670
Speakers: Bill Chhor (Cisco), Mary Mazon (Cisco), Dan Thomson (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837560001zEF7
This session explores Cisco's internal strategy for transitioning from Cisco on-premise telephony (Unified Communications Manager, UCM) and PSTN services to Webex Calling and Cloud PSTN including our Cisco's contact center environment. It highlights the unique challenges, benefits, and procedures involved, while showcasing key improvements driven by Cisco IT to aid customers in similar migrations.

### Transforming Communities: Innovative Connectivity in Cary and Los Angeles - CSSEWN-1019
Speakers: Nicole Coughlin (Town of Cary), Dan Caroselli (City of Los Angeles), Gary DePreta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271873091001zh05
Join this fireside chat with Town of Cary and the Los Angeles Bureau of Street Lighting to explore how strategic technology partnerships empower communities through innovative connectivity solutions. The Town of Cary will share how leveraging Cisco technologies - such as Catalyst Switches, DNA and Security Enterprise Agreements, and Webex - to achieve scalable IT solutions and service excellence in their community park. Additionally, LA Bureau of Street Lighting will discuss their Community Connectivity Initiative, which uses streetlight poles to provide wireless access in underserved areas, is enhancing city services and public safety. This chat will highlight the transformative power of Cisco technologies in creating future-ready communities. Discover how multi-architectural infrastructure can revitalize communities, impacting education, business, and the local workforce.

### Transforming Contact Center Efficiency and Customer Satisfaction Through Enhanced Agent Experience - BRKCCT-2688
Speakers: Chandramouli Vaithiyanathan (Cisco), Janani Ramakrishnan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271866192001zvM9
The landscape of customer service is currently undergoing a significant transformation towards a realm of intelligent and personalized service delivery. Within this paradigm shift, the pivotal role of the Agent in crafting exceptional customer experiences cannot be overstated. This session delves into the evolution of customer service ecosystems, emphasizing the indispensable role of Agents and supervisors as architects of positive interactions. Participants will explore the customization of agent desktops, exploring a wide range of gadgets drawn from our extensive library. Additionally, attendees will gain insights into leveraging cutting-edge AI features such as agent wellness and auto-response capabilities to streamline operations and enhance customer satisfaction. Join us as we explore the future of CX, where empowered agents, supported by advanced technology, drive unparalleled levels of customer satisfaction and loyalty

### Transforming Enterprise Networks with Cisco SD-Access: Real-World Strategies from CDW - BRKENS-1806
Speakers: Puneet Duggal (CDW Canada), Kanu Gupta (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271919703001z5ce
Enterprise networks are facing unprecedented demands—from the explosion of connected devices and zero trust security mandates to the need for simplified, scalable operations. Cisco's Software-Defined Access (SD-Access) offers a modern network fabric designed for streamlined management, enhanced security that scales for future demands. In this session, CDW—one of Cisco's top partners—shares real-world insights from SD-Access deployments across industries like utilities, sport venues and large enterprises. We'll walk through the full SD-Access journey—from early visioning to successful implementation and adoption. Learn how to overcome common deployment challenges such as legacy integration and license justification, using CDW's proven adoption framework to accelerate deployment and minimize risk. We'll also explore advanced SD-Access use cases powered by open APIs, including integrations with security tools, IoT platforms, Data Loss Prevention (DLP), and digital twins. Key Takeaways: - Why SD-Access is the optimal solution for modern enterprise networks - CDW's structured framework to simplify, de-risk, and accelerate deployment - Real-world metrics that demonstrate SD-Access ROI—and why delaying can cost more than acting now

### Transforming Health Organizations for the Digital Era: A Comprehensive Approach with INFRAM and Cisco Solutions - BRKXAR-2030
Speakers: David Chen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271868520001zYN6
As healthcare organizations encounter growing demands for digital solutions, cybersecurity, and digital transformation, the Infrastructure Adoption Model (INFRAM) offers a comprehensive framework to align IT investments with clinical, financial, and operational objectives. This alignment ensures that systems, like EHRs such as Epic, meet clinical requirements. Cisco Software-Defined Access (SDA) and other cross-architecture solutions complement INFRAM by automating networks, mitigating risks, and providing comprehensive visibility.

### Transforming Healthcare at Keck Medicine of USC, UCLA Health, and Northwestern Medicine - CSSSEC-1001
Speakers: Christian Aboujaoude (Keck Medicine of USC), Adrian Finemel (UCLA Health), John Brow (Northwestern Medicine), Mary Swigart (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271875679001zORT
Join us for a healthcare fireside chat showcasing how leading institutions like Keck Medicine of USC, UCLA Health, and Northwestern Medicine are revolutionizing their network infrastructures and security posture with Cisco technologies. Keck Medicine of USC will bring insight into how they are enhancing network security and management using Cisco Identity Services Engine and Catalyst Center, implementing advanced segmentation and automation. UCLA Health will discuss their transition to Cisco Software-Defined Access, which modernized their network with policy-driven automation, boosting security, and scalability. Northwestern Medicine will share their experiences in enhancing patient data security and operational efficiency through strategic micro-segmentation initiatives. This panel offers real-world insights and strategies for successful technology integration in healthcare, setting new benchmarks for innovation and efficiency.

### Transforming IT Across Industries with Cisco Meraki - CSSENT-1105
Speakers: Matthew Landry (Cisco), Annika Snead (Hibbett Sports), Ryan Naef (Tuff Shed), Dawn Armstrong (HumanGood)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271875297001zB13
As IT demands grow across industries, organizations seek simplified and scalable solutions for effective management. This session unites leaders from HumanGood, Tuff Shed, and Hibbett Sports to discuss their transformative journeys with Cisco Meraki. Attendees will learn about the benefits of standardizing and simplifying IT operations through cloud-based platforms, enhancing network performance, and ensuring scalability and security across multiple locations. The discussion will provide practical strategies for leveraging Cisco Meraki to optimize IT infrastructure, reduce costs, and improve operations, offering insights applicable to diverse environments.

### Transforming Network and Data Center Infrastructure for AI: Enabling the Future of Enterprise - BRKNWT-2507
Speakers: Vinay Saini (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271973320001zho2
As artificial intelligence (AI) continues to evolve, its infrastructure requirements are drastically reshaping enterprise IT environments, data centres, and network connectivity. The increasing demand for AI-powered applications, real-time processing, and vast data storage necessitates a transformation in how we think about network architecture, data centre capabilities, and network bandwidth. This session will explore the key infrastructure changes needed to support AI workloads, with a particular focus on: Data Centre Evolution : How AI-driven workloads demand more specialised hardware (e.g., GPUs, TPUs), energy efficiency, and greater scalability, and how organisations can upgrade their data centres to meet these demands. The session will cover design , configuration, and optimisation methods to handle GPU-to-GPU communication (RoCEv2) in the most efficient manner for training and inferencing tasks. Network and Security: The session will also explore strategies to optimise enterprise LAN and WLAN infrastructure for improved user experience in AI inferencing use cases. Additionally, it will highlight essential security considerations when integrating AI/GenAI technologies into your environment. In summary, this session will provide you with key insights, decision-making guidance, and technology awareness to support your AI adoption journey.

### Transforming application visibility into actionable business intelligence with Splunk AppDynamics - BRKOBS-1010
Speakers: Hoppy Shaw (Alaska Airlines), Sunder Parameswaran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271981915001zoql
Monitoring increasingly complex n-tier application environments can be daunting, but correlating application performance to tangible business outcomes can be impossible without the right observability solution. AppDynamics helps your team overcome these challenges and strategically align IT operations with key business goals through unparalleled visibility and insights to understand application behavior and its impact on business objectives. Discover how AppDynamics transforms application visibility into actionable business intelligence, driving improved decision-making and enhanced organizational success. Learn how the latest innovations in AppDynamics detect performance bottlenecks proactively with AI-directed troubleshooting, pinpoint issues in user experience with new Session Replay features, and unlock complete visibility of your AI stack through enhanced LLM monitoring capabilities

### Transforming your code into a Work of Art! - DEVNET-1090
Speakers: Shaun Roberts (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271894366001z3UR
Step into the future of automation with XDR Automation! This dynamic session will guide you through the transformation of traditional Python code into streamlined, low-to-no-code workflows with Cisco's powerful XDR Automation system. Designed for all levels of engineers, this session offers a deep dive into how XDR Automation can help you simplify complex tasks, eliminate repetitive code, and create intelligent automation processes—all with minimal coding. You will learn general orchestration principles as you see how easy it is to move from one language to another. you'll gain practical insights and have hands-on examples showing how to turn your code into a true masterpiece of automation. Come and work towards elevating your code to create powerful workflows with real-world application.

### Transition to a New Hypervisor & Build AI Infrastructures Simultaneously with Red Hat OpenShift and Cisco UCS - BRKCOM-2214
Speakers: Boris Aelen (Cisco), Michael Hrivnak (Red Hat)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271860812001z6Rf
Three big disruptions in our IT sector are all coming together; Application modernization by containerization Finding VMware alternatives Building AI infrastructure Red Hat OpenShift is the platform of the future that runs all virtualized, containerized and AI workloads! Now is the time to learn about OpenShift and the best server platform in the world to run it on, Cisco UCS with Intersight. This session is delivered by Red Hat and Cisco together and demonstrates how to deploy and operate OpenShift Container Platform with unique integrations between Red Hat and Cisco. We focus on the technical capabilities from both platforms that will simplify your daily operations and help you deploy a secure and future proof compute platform to run your existing virtualized workloads. This session is specifically built for VMware admins to learn about OpenShift Virtualization but will prepare you for running containerized and AI workloads in the future.

### Trip Through Your Wires - An Attacker's Hazardous Journey - BRKSEC-3026
Speakers: Mike McPhee (Cisco), Jaeson Schultz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272012565001zlNr
Do you know (and appreciate) the "A day in the life of a packet" sessions? Here is a day in the life of a Threat Actor. We start with a detailed threat analysis of an operation based on threat research and MITRE's ATT&CK to look into how the threat actor's actions and tools looks from the inside out and how they try to bypass today's security measurements to fly under the radar. With the knowledge collected in each step of the journey, we will use various methods to detect or mitigate the threat from within your environment. We will discuss the tactics used, the indicators found, and the impact on the victim in a recent threat. By the time the session closes, we'll all have the skills we need to better explain the adversary's behavior, the detections that uncover it, and the actions to mitigate it effecively. This session is targeted at security engineers and ambitious NetSec practitioners, or anyone who wants to learn how to tell better non-fiction cybersecurity stories.

### Troubleshoot Catalyst 9800 Wireless Controllers - BRKEWN-3628
Speakers: Javier Contreras (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271942600001zpOU
This session covers troubleshooting tips and tricks for working with Cisco Wireless. From Cisco Catalyst Center (formerly Cisco DNA Center) Assurance to the Catalyst 9800 Series and Catalyst access points themselves, learn where to look and what to look for to resolve most common issues.

### Troubleshoot Cisco Secure Client Network Visibility Module (NVM) with XDR - BRKTAC-3002
Speakers: Alex Hidalgo Noriega (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272019602001zIhR
Gain insights into resolving telemetry ingest issues with the Cisco Secure Client's NVM module just as a TAC engineer would, by looking at it from both the client's and the cloud collector's perspective. We will cover the essentials of NVM, potential issues that may arise within each component of the configuration, and how the data collected by NVM contributes to XDR's capability to provide in-depth insights about user network communication, processes, and more.

### Troubleshooting ACI access policies Fault F0467 - BRKTAC-3001
Speakers: Luis Contreras (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272019409001zx1o
Does your fabric have and number of F0467 faults and is still working as expected and you wanted to keep it that way? In this session we will explore the different troubleshooting scenarios to address the most common cause of access policies configuration issues and the implication on best practices implementation on ACI environment.

### Troubleshooting Like a NGFW TAC Engineer: Learning How to Troubleshoot Traffic Problems Within Your Network - TACSEC-2017
Speakers: Megan Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271996580001zcqX
In the realm of Next-Generation Firewalls (NGFW), traffic issues are among the most prevalent challenges encountered. Whether stemming from incorrect NAT configurations or ACL blocks, there are numerous strategies to identify the root cause of traffic disruptions. This session will delve into the essential tools for troubleshooting traffic problems, including "system support trace debug," "packet-tracer," and "captures." We will explore the optimal scenarios for utilizing each tool and how to effectively interpret the data they provide. Additionally, we will collaboratively analyze examples from lab recreations to pinpoint the underlying issues. By the conclusion of this presentation, participants will possess the skills to troubleshoot network and traffic issues with the proficiency of a TAC engineer.

### Troubleshooting MTR Onboarding and Navigator Pairing - TACCOL-2015
Speakers: Mathew Michael (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271851266001zpvW
In this session, we will look at the MTR Onboarding, software versions that allow successful MTR onboarding and Navigator pairing process on the RoomOS layer as well as MTR. You will leave this session with an understanding of the MTR onboarding and Navigator pairing process and troubleshooting common related faults.

### Troubleshooting Microsoft Teams Webex Calling Integration - BRKCOL-3018
Speakers: Josh Hammonds (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271854909001z5h8
Customers who choose to utilize Microsoft Teams for messaging and Webex Calling for their calling infrastructure often need help understanding the complexities of the integration. In this session, we will take a deep dive under the hood of the integration and give administrators who utilize both Microsoft Teams and Webex Calling tips and tricks to ensure they know where to look and what to do to solve some of the most commonly seen issues with the integration.

### Troubleshooting Multi-Homing in a BGP EVPN VXLAN Fabric for Enterprise network - TACENT-2026
Speakers: Tolon Malabekov (Cisco), Fernando Martinez Gomez (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271929980001zsyH
This troubleshooting documentation/presentation will help customers to troubleshoot the VXLAN Multihoming issues.

### Troubleshooting Multicast: The "Usual Suspects" - BRKENT-2264
Speakers: Fish Fishburne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271932049001zaHk
When troubleshooting a multicast environment, it is typically the "usual suspects" that are the culprits. In this session, we will dive into what these "usual suspects" are and how you can use that knowledge to troubleshoot in multicast environments much more efficiently.

### Troubleshooting Offline Meraki Nodes - TACOBS-2001
Speakers: Karla Cisneros Galvan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271977782001zUvt
The most common issue Meraki support engineers handle daily is offline devices. Having addressed hundreds of cases reporting this issue, we have identified the most frequent reasons that cause Meraki devices to become unreachable. Join us to learn about these causes and discover effective solutions.

### Troubleshooting SD-WAN IPsec SIG Tunnels - TACENT-2027
Speakers: Alain Perez (Cisco), Tushar Uttamrao Jagtap (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271930169001zB5t
In the Cisco SD-WAN solution, IPsec Secure Internet Gateway (SIG) tunnels provide secure and seamless connectivity to cloud security services. However, misconfigurations, authentication issues, and connectivity problems can prevent successful tunnel establishment, leading to degraded network performance. This session will walk through the IPsec SIG tunnel establishment workflow, highlight common failure points, and demonstrate effective debugging techniques. Attendees will gain a structured troubleshooting methodology for diagnosing and resolving tunnel issues between Cisco SD-WAN and cloud security services. Real-world failure scenarios will be analyzed with a focus on root cause identification and best practices to restore secure, high-performance SD-WAN connectivity.

### Troubleshooting Strategies for Cisco Catalyst Center & SD-Access - BRKTRS-2821
Speakers: Mariusz Kaźmierski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271936321001zsTD
Are you spending too much time troubleshooting Cisco Catalyst Center or SD-Access? Join this session to sharpen your troubleshooting skills, explore the latest tools and techniques, and discover key enhancements in Cisco Catalyst Center 2.3.7.x and 3.1.3. Whether you're tackling issues solo or working alongside Cisco TAC, this session will equip you with the knowledge and strategies to diagnose and resolve problems more efficiently—helping you minimize downtime and maximize network performance.

### Troubleshooting Webex Authentication and Provisioning - BRKCOL-3117
Speakers: Paul Stojanovski (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271858367001zyLu
Webex administration is continually evolving. If you're thinking about deploying Webex, growing it, or are interested in avoiding a call to TAC, this session will help you understand the most common pitfalls customers run into when managing Webex. The content will be based on the most common challenges customers face when opening TAC cases around the following topics: Directory integrations such as Directory Connector and Entra ID sync (includes understanding troubleshooting approach, available logs, and sync issues) Group synchronization issues and migration challenges Single sign-on configuration issues and certificate updates (includes understanding a SAML assertion, SSO auth flow, and login issues)

### Troubleshooting Webex Calling Local Gateway (LGW) Connectivity Issues - TACCOL-2018
Speakers: Kyle West (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271851870001z12F
"Attendees will learn how Webex Calling Control Hub determines the status of a Local Gateway (LGW) trunk, through the exchange of Session Initiation Protocol (SIP) Option Keepalive messages, how the different status states map to the SIP signaling exchanged between the two systems and finally, how to troubleshoot some of the more common problems as reported by customers to Cisco TAC. Additionally, attendees will learn what commands to collect from the Local Gateway CLI, how to interpret the output and use it to solve connectivity issues. "

### Troubleshooting Webex Scheduling on Webex app or Cloud devices - BRKCOL-3019
Speakers: Josue Jonathan Vizcaino Huape (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271855096001zeJb
Webex Scheduling leverages users to schedule, edit and manage meetings directly on their Webex app or in Conference rooms and it is important to have a the service correctly deployed with less error gaps to reduce the impact. In this session you will see the most common errors received by Cisco TAC and how to quickly revert the service down in your Premises. You will also learn how to get room mailbox details On-premises while troubleshooting onboarding issues. Leaving this session you will now know how to reduce the time to resolution for your users and improve your Cisco Webex Scheduling needs.

### Troubleshooting as you know it -- is over. - AIHUB-1903
Speakers: Lizzie Parker (Cisco), Mohamed Abouelseoud (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271983853001zBar
Cisco is unveiling a new generation of AI capabilities designed to transform how NetOps teams see, solve, and share problems. No more swivel-chairing across dashboards. No more escalation ping-pong. No more guesswork. Just AI that assists, accelerates, and automates-across your entire network

### Troubleshooting common issues when deploying a virtual Firepower Threat Defense (vFTD) instance on Amazon Web Services (AWS) - TACSEC-2016
Speakers: Shelby Wesnitzer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271996388001zeOQ
This session provides a practical walkthrough for troubleshooting common issues when deploying a virtual Firepower Threat Defense (vFTD) instance on Amazon Web Services (AWS). During the session attendees will learn how to configure essential AWS prerequisites, including Virtual Private Cloud (VPC) and Elastic Compute Cloud (EC2) components necessary for a manual deployment and gain troubleshooting skills to independently resolve common issues, enhancing their ability to manage deployment challenges effectively.

### Troubleshooting the Cisco Catalyst 9000 Series Switches - BRKTRS-3090
Speakers: Michel Peters (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271936886001zjWW
This session covers troubleshooting of the Cisco Catalyst 9000 series hardware and the Cisco IOS XE operating system that powers it. It demonstrates various tools and techniques available on this platform to troubleshoot CPU, memory, resources, packet forwarding and packet drops. Last, but not least, this session will show some of the next generation of troubleshooting methodologies enabled by Cisco IOS XE software and discuss how users can use these methods to troubleshoot their networks quickly and effectively. First-hand knowledge of the Cisco Catalyst 9000 product is expected. This session covers the Catalyst 9200, 9300, 9400, 9500 and 9600 range of switches, but it does not include Catalyst 9x00 series access points or the Catalyst 9800 series wireless LAN controllers.

### Troubleshooting the Most Common Voice Issues in Webex Contact Center - TACCOL-2014
Speakers: Meenakshi Sundaram Kandasamy (Cisco), Joshua Zuke (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271851077001zM5E
"Voice issues in Webex Contact Center (WxCC) can impact call quality, agent productivity, and customer experience. This session presents structured troubleshooting methods to address challenges like static, audio problems, and RONA errors in WebRTC configurations, along with additional tips for troubleshooting outdial call flows. Discover how to utilize Analyzer's reports to effectively isolate, diagnose, and plan resolutions. Implementing these strategies can significantly enhance agent performance and customer satisfaction. Attendees will acquire practical techniques to swiftly identify and address voice challenges, empowering them to enhance operational effectiveness in their contact centers."

### Troubleshooting the Webex App Login - BRKCOL-3001
Speakers: Josh Hammonds (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271854715001zI3w
Webex is the premier Collaboration client that offers messaging, calling, meetings, and presence in a single client. While these features are all great individually, none of them matter if your users cannot log in to Webex. Thousands of users worldwide experience Webex login issues daily, and most of these problems are preventable. Please join my session; we will focus on the causes for the most commonly seen login problems to Webex and how to correct them. Leaving the session, you will be an expert at troubleshooting the Webex login process for the Webex app and know what to look for when actively troubleshooting.

### Tuki Migrate: The Future of Cloud Calling Migrations - VILCLD-1024
Speakers: Eric Olson (Tuki)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271844609001zQJD
Cisco Customers, Partners, and Technology Integrators. • Learn how to meet the challenge of moving your Enterprise UC customers to the cloud with AI & Automation. • On-prem to Webex Calling Dedicated Instance & Multi-Tenant Platforms • Hybrid migrations and management — On-premise/Cloud/Cisco & Other UC Platforms • Empower your team with a solution to migrate and manage even the most complex UC environments at scale At the end of this session you will understand: • How you can migrate from Cisco and other on-premise UC platforms to the CLOUD at your own pace • How you can manage your hybrid UC environment from pre-migration through post migration • Reduce migration Time & Costs by more than 80% with Tuki Migrate

### Tune your Cisco Wireless networks for Roaming clients and demanding Real-Time applications...with some help from AI! - BRKEWN-2926
Speakers: Jerome Henry (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271939639001zcRI
Are you running a Cisco Wi-Fi network? Great news! Thanks to a unique partnership with Apple, Samsung, Intel, and other great names in the client device ecosystem, Cisco Wi-Fi has features that allow your clients to tell you how they are performing, and for your access points to optimize the experience of your Wi-Fi clients, including those in the hands of users who move and roam all day long between APs, and including those that run real-time and demanding applications and for which increased latency of jitter means disastrous experience. Join us in this session, where you will learn what these unique features are, and how to tune your Cisco Wi-Fi network to offer a seamless experience to all your clients, mobile phones, tablets, IoT and laptops.

### Turbo charge your ACI Segmentation and Visibility - BRKDCN-2959
Speakers: Fabien Gandola (Cisco), Steve Sharman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271891139001z19F
Ever wonder what would happen if you put an English ACI guy, and a French security guy on stage and ask them to design a secure ACI fabric ? Join our session to learn best practices, and how to leverage ACI capabilities and security services in order to fulfil the requirements of both DC and security teams whilst keeping application owners happy.

### Turbocharge your services: Rapid end to end Automation with Infrastructure as Code! - BRKOPS-2142
Speakers: Markus Harbeck (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271988003001ziKy
Are you concerned automation is risky and unpredictable? Are you worried about being locked into proprietary automation tools? Do you want to turbo your network? You are exactly right here! This dynamic session ventures into the transformative paradigm of services delivery with infrastructure-as-code (IaC) principles, referred to Services as Code. Defining a reusable blueprint for automation, standardizing the automation across all your IT domains to simplify your operations. Services as Code (SaC) delivers this outcome while also embracing open source. The session will explore how SaC and IaC for ACI, SD-WAN, and SDA supersedes traditional manual operations. We demonstrate how teams will be empowered to instantiate, deploy, and adjust services with speed and consistency. Participants will gain a deep understanding of how SaC and IaC promotes DevOps methodologies, enhances productivity, minimizes errors, and fast-tracks deployment timelines. The automation of processes leads to more reliable and scalable IT infrastructures, as changes can be tested, versioned, and rolled out in a controlled manner following CI/CD principles. Join us at the forefront of technological advancement as we unravel the secrets behind the seamless integration for SaC and IaC. The future of IT infrastructure is here are you ready to embrace it?

### Turbocharging Automated Network Testing with Generative AI - BRKXAR-2032
Speakers: Christopher Hart (Cisco), Andrea Testino (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871010001zs8L
Enterprise networks demand rigorous testing for every change, yet manual testing cannot scale to meet today's rapid deployment needs. While automation helps, developing comprehensive test coverage traditionally requires significant engineering resources and time. This session demonstrates how AI transforms network testing practices. Participants will learn how to leverage generative AI to rapidly create and scale test automation, reducing test development time from days to minutes while improving consistency and coverage. Through live demonstrations, we'll show how AI assists in writing test requirements, developing test scripts, and predicting change outcomes in network environments.

### Turn AI to ROI with a Solid Data Foundation - CNCDCN-1021
Speakers: Marcus Maddox (Hitachi Vantara)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271878240001zUY9
Achieving AI success starts with a strong foundation. From identifying the best use cases to building a secure, efficient, and reliable data platform ready to handle AI’s demanding workloads. Cisco and Hitachi Vantara provide the critical building blocks for your AI data platform. With a proven track record in meeting the mission-critical needs of top organizations worldwide, the path from AI to ROI is clear and actionable. Join us and learn how to jumpstart AI success and unlock its full potential for your business. ​You will learn how Hitachi Vantara is incorporating new Cisco technologies into its AI data platform solution. You will hear from Jeremy Foster, Cisco SVP and General Manager Compute how Cisco is lighting up the GPU server world with their latest UCS entry.

### Turn Your Security Policy Into Code and Make Your Weekends More Enjoyable - DEVNET-2076
Speakers: Brennan Bouchard (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899032001z8f0
Deploying and updating security policy has always been risky business. This is typically why most policy changes are done during maintenance windows over the weekend. What if there was a better way to develop, test and deploy security policy in an environment before being pushed to production. Would that be of interest? In this session, we introduce Security as Code where you will learn how to dynamically update and deploy security policy into the application pipeline using Ansible and Terraform, giving you that warm and fuzzy feeling that your weekends won't be rudely interrupted.

### Uncover the Secrets of Cisco Live's NOC: FlexPod, Splunk, and More - CISCOU-2064
Speakers: Chris O'Brien (Cisco), bobby oommen (NetApp)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271842519001zbyo
Join us for an in-depth exploration of the Cisco Live Network Operations Center (NOC), where cutting-edge technology ensures seamless mission-critical operations. This session will reveal the robust infrastructure behind the Cisco Live network, emphasizing the integration of Cisco and NetApp® ONTAP® components. Discover how Cisco UCS, Nexus, and NetApp MetroCluster® combine in a FlexPod® configuration to create a resilient environment capable of supporting all essential applications. Additionally, learn how Splunk monitoring enhances operational visibility and performance, enabling proactive management and swift troubleshooting. This session provides valuable insights into leveraging Cisco's solutions to elevate your IT strategies.

### Under the hood of IOS-XE EVPN/VXLAN on Catalyst 9000 - BRKENS-3840
Speakers: Dmytro Vishchuk (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271925346001zwnA
Ethernet VPN (EVPN) has become de-facto an industry standard for data center fabrics and L2/L3 VPN connectivity in service provider. EVPN functionality was also expanded into Campus networks, to address the drive of network operators toward simplicity and automation with a unified inter-domain connectivity technology. This session covers in detail packet path in the Fabric in case BUM, bridged and routed flows with verification of the Fabric states and deep explanation of the CLI outputs of the show commands for relevant components. Focus of the session is to build deep knowledge of EVPN "mechanics" on Catalyst 9000 and a clear understanding of the process of packet forwarding and related verification methods.

### Understanding Hyperfabric: a Groundbreaking Cloud-Controlled Data Center Network Solution - BRKDCN-2944
Speakers: Dan Backman (Cisco), Minako Higuchi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271889798001z7ut
What is an ideal cloud-controlled data center network solution? One that makes it easy for anyone to deploy reliable fabrics anywhere. In this lively session, you will get a first-hand view of an upcoming solution that re-imagines every phase of the process - design, order, deploy, validate, monitor, and upgrade. And we will reveal novel capabilities the solution embeds including an abstracted & managed underlay, plug & play deployment, built-in assertion-based health monitoring, and the elimination of on-box CLI. Join us to see this Cisco innovation in action.

### Understanding Identity Based Networking Services IBNS 2.0 - BRKCRT-3002
Speakers: Rafael Leiva-Ochoa (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271836250001z82L
This session will help the attendee understand, and configure IBNS 2.0 on a Cisco Switch to prepare for the SCOR 1.1 exam.

### Understanding Packet Flow and Troubleshooting RFID Tag Location Tracking with Cisco Spaces - TACENT-2021
Speakers: Bryan Belliard Mota (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928997001zp7h
This session will cover how the AeroScout Location Engine (ALE) integrates with Cisco Spaces, as well as how to troubleshoot various issues. The Stanley AeroScout Real-Time Location System (RTLS) leverages existing wireless infrastructure to track AeroScout Tags and Wi-Fi devices. Cisco Spaces is the most common integration used for location tracking. Additionally, we will provide troubleshooting guidance and validation tips to ensure proper data flow and accurate location updates for deployment.

### Understanding RF in a Wireless First World - BRKEWN-2048
Speakers: Mark Krischer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271940820001zrUq
Would you like a better understanding of RF and how it impacts the design of Wireless Networks? Do you like knowing the "how" and the "why"? Wireless networks function within the electromagnetic spectrum, presenting unique challenges distinct from those of wired networks with their shielded cables. This session will demystify the core principles of RF networking and how it operates as the physical layer in 802.11 WLANs. We'll also delve into the latest 6GHz wireless regulations and their impact on next-generation Wi-Fi 6E and Wi-Fi 7 technologies Equip yourself with the knowledge to engineer robust wireless networks capable of supporting the most intensive real-time applications in a Wireless First World

### Understanding Wireless Security and the Implications for Secure Wireless Network Design - BRKEWN-2104
Speakers: Mark Krischer (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271941802001zNla
This session will explore secure wireless network design with a key focus on the latest Wi-Fi and WPA standards. Mobility brings unique challenges to network security, such as the need for strong authentication and support for secure fast roaming. Participants will learn how 802.11 addresses these requirements and will explore the changes WPA3 brings and the implications for wireless deployments. This session will also explore how Catalyst Center and Meraki Dashboard expand on wireless security standards with rogue access point detection and location, and advanced wireless intrusion detection and prevention. The intent is to provide a deeper understanding of wireless security capabilities from the perspective of the attacks they defend against.

### Understanding and Troubleshooting HTTP Proxies in the Webex Environment - BRKCOL-3020
Speakers: Paul Anholt (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271858177001zxLi
When many customers deploy Webex into their organization, they often face questions about how the individual Webex components interact with their HTTP proxy servers. In this session, we will explore the interactions between HTTP client interactions between Webex devices, Webex App, and Webex Hybrid Services with their upstream HTTP proxies. Attendees will gain insights into the clients proxy configuration and design, how they handle TLS certificates, and learn troubleshooting techniques for proxy-related issues. This session will cover practical troubleshooting and log analysis, address the most common issues as seen by Cisco TAC, and present real-world case studies providing participants with the knowledge needed to manage their Webex deployments in environments where HTTP proxies are used.

### Understanding the Core Webex Calling Multi-Tenant Features - BRKCOL-2081
Speakers: Steven Fly (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271856438001zf2x
Are you looking to move to Webex Calling Multi-Tenant and looking to understand what core calling services and features are available in the solution? In this session we will review the core Webex Calling features like call queues, auto attendants, hunt groups, call park/pickup, recording, etc. We will discuss when to use each one and also look at some examples of how similar UCM features can be configured in Webex Calling to accomplish the same goal. You will leave this session with a better understanding of all the features and when/where you can implement them to meet your needs.

### Understanding, Identifying and Resolving Congestion in a UCS Converged Infrastructure - BRKCOM-2657
Speakers: Ed Mazurek (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271862160001zkzJ
The UCS X-Series Modular System and UCS B-Series Blade Servers are in reality large converged Ethernet networks. When they connect upstream to Fibre Channel fabrics such as MDS they are joining the SAN and can be a significant point of congestion. As with any lossless network, when congestion occurs it can spread from the point of congestion back to the source of the data. That can have drastic negative effects on performance. Because these UCS systems converge lossless FC/FCoE and RoCEv2 with regular IP/Ethernet, traffic of one type may affect the other types. Although this congestion is from the typical three causes, namely slow-drain, over-utilization and bit errors, identifying and resolving congestion requires a unique understanding of the UCS systems, the points of congestion and the command sets necessary to troubleshoot. Additionally, there have been recent diagnostic enhancements to the UCS system to allow for much better historical troubleshooting. This session will be an in-depth presentation of this topic.

### Unified Access and Aggregation with Cisco Routed PON - BRKSP-1169
Speakers: Tejas Lad (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271963478001z6TZ
Service providers are heavily investing in broadband deployments using passive optical network (PON) technology to cater unprecedented demands of end users. Billions of dollars have been funded by government organizations to bring broadband to everyone. With 10 gigabit symmetrical PON (XGS-PON), service providers are looking to converge business, mobile backhaul, and residential services onto a common platform and architecture. Cisco's routed PON solution reduces the footprint and power of the optical line terminal (OLT) to a small form-factor pluggable (SFP) that can be hosting in Cisco's NCS-based platforms running IOS-XR. Cisco NCS platforms are widely deployed as access and aggregation, and integrating the XGS-PON pluggable brings tremendous operations and cost advantages. In this session, you will learn the different components of the XGS-PON system and its integration into Cisco's converged SDN transport using segment routing and EVPN. The session will cover the shift in PON technology and deep dive into Cisco routed PON with both residential and business use cases. We will keep the session interactive with live demos showcasing the deployment and benefits of the solution.

### Unified Observability: Maximizing Value through Technology, People, and Processes - BRKOBS-1110
Speakers: Lukasz Ciukaj (Cisco), Mirek Karczmarz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271982304001z5H9
In today's complex IT environments, achieving observability excellence requires a well-integrated practice that combines multiple tools with effective processes and governance strategies. This session targets customers using AppDynamics, Splunk, and ThousandEyes across departments. We will cover advanced integration techniques, best practices, and real-world use cases to show that observability is a practice, not just a technology or solution. You'll learn to seamlessly integrate these tools, providing observability across various types of applications and other systems while fostering continuous improvement and collaboration. We'll also discuss governance strategies to ensure compliance and alignment with business objectives, highlighting the role of a Technical Governance Framework in driving success. This framework promotes consistency, accountability, and strategic alignment in observability efforts. By establishing a leading observability practice, your organization will enhance digital resilience, allowing for quick recovery from challenges. Whether your goal is to improve performance, reduce downtime, or gain operational insights, this session offers strategies and frameworks for IT excellence.

### Unified Platform Management with Cisco Networking Subscription - PSOENT-1029
Speakers: Divya Sawhney (Cisco), Benson Lao (Cisco), Gayathri Devi Viswanathan Nagendran (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928806001zYMW
Join us for an insightful session where experts reveal the benefits of a Cisco Networking Subscription. Discover how our innovative model simplifies network management and streamlines your operations. Don't miss the opportunity to learn about a more integrated, efficient network experience.

### Unified Wireless for Industries: From Wi-Fi to Private 5G and Beyond - BRKSPG-2045
Speakers: Matthias Falkner (Cisco), Gino Corleto (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271964068001z9EC
Have you ever wondered why there are so many wireless technologies available, and why some seem to overlap? Choosing the right wireless technology - or combination of technologies - can be challenging, especially as more business-critical processes rely on them. With digitization and wireless mobility closely linked, understanding our wireless toolbox is essential. In this session, We'll explore key wireless technologies like Wi-Fi 6/6E/7, CURWB, and Private 5G. We'll dive into real-life use cases to determine when each technology is most appropriate. Additionally, we'll discuss the importance of security, highlighting a unified policy approach and the best practices for integrating these technologies into your existing OT/EN networks and policies.

### Unifying Detection, Response, & Investigation with Data Security Strategies - VILSEC-2028
Speakers: Damien Philip (Cohesity), jim walker (Cohesity)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271992683001zHn1
When you are in the midst of a cyberattack, the speed of your response matters. Nowadays, the median ransomware variant can encrypt 100,000 files in just 43 minutes. Every second counts as you scramble to minimize the extent of data loss and disruption to business-critical applications. Cyber resiliency is top-of-mind for Cohesity and Cisco so the development of an adaptive and automated data protection capability built on Cisco XDR and Cohesity DataProtect platform enables customers to significantly reduce their risk of data loss in a cyberattack using real-time threat intelligence sharing and an accelerated threat response approach. At the earliest signs of ransomware, Cohesity DataProtect will preserve potentially infected virtual machines for future forensic investigation while simultaneously protecting data and workloads in the rest of the environment. As a result, InfoSec teams are intrinsically more proactive in data protection, ensuring they have a quick recovery point in case the threat proves to be real. Learn about how this capability will enable your organization to detect earlier, automate responses, accelerate investigation and enable recovery to a known good state.

### Unifying On-The-Move Wireless Networks Across 5G, Wi-Fi, and Satellite for Emergency Services using SRv6 - BRKSPG-2046
Speakers: Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271964258001zV1D
Unified wireless communications is another way of describing an infrastructure model that offers ubiquitous IP connectivity over any underlying infrastructure, focusing primarily on wireless technologies, with private 5G and Wi-Fi being the most common, but not exclusive. In this session we will describe a system co-developed with BWI, the IT services provider to the German armed forces, that creates such an infrastructure across private 5G, Wi-Fi, and satellite while being extensible to all other wireless and wired technologies using IP and routing as the unifying layer. This allows BWI to offer a common transport infrastructure to all applications in a reliable and access-agnostic manner. Any available spectrum can be utilized by the applications. In partnership with the BWI CTO, we will discuss the application of such an infrastructure to the critical/emergency communications domain by showing how this can be integrated into a fully mobile system that can be dropped in and deployed ad hoc, with easy extensibility for dynamic geographical coverage. The system has full automation and full lifecycle management in any field situation, with self-healing connectivity as a key characteristic.

### Universal ZTNA Reimagined: Pioneering the Future of Cisco Secure Access and Cisco SASE - PSOSEC-1025
Speakers: Prabhu Barathi (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271995175001z1ht
In today's increasingly distributed IT environment with users everywhere and thousands of IOT devices to secure, you need the ability to efficiently enforce and monitor least privilege access across this hybrid environment. However, as digital transformation accelerates and hybrid work models become the norm, traditional Zero Trust Network Access (ZTNA) implementations face new challenges, including scalability, user experience, and integration with evolving architectures and so many Zero Trust projects stall out. In this session, learn about Cisco's Universal Zero Trust Network Access solution, our expanded approach that fuses networking and security to redefine ZTNA and SASE as we aim to address its current limitations and lay the foundation for a secure, efficient, and scalable zero-trust platform.

### Unleash Network Potential: Master QoS and Forwarding with Cisco 8000 - BRKMSI-2001
Speakers: Santosh Sharma (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271966983001za4Z
The Cisco 8000 Series routers, powered by Cisco Silicon One and IOS XR software, offer high-density, high-performance routing with a unified ASIC architecture. The Cisco 8000 Series routers are engineered to meet modern networking challenges with exceptional scale, performance, and efficiency. In this session, participants will explore QoS and Forwarding architecture in Cisco 8000 series routers. Participants will gain an understanding of the QoS architecture, Virtual Output Queue (VOQ) implementation, packet forwarding architecture, and hardware resources. The session will also cover practical troubleshooting, end-to-end packet flow, best practices, and effective health monitoring techniques. The session will empower network professionals to maximize the capabilities of Cisco 8000 Series routers, enhancing connectivity and performance.

### Unleashing AI for cognitive security operations - PSOCX-1022
Speakers: Suresh Chaurasiya (Cisco), Jasjeet Singh (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272015126001z8bU
In today's AI-powered landscape, the rise of sophisticated AI-enhanced cyber threats necessitates the adoption of advanced technologies and countermeasures to safeguard your users and assets. Join us to explore how you can enhance your security posture and accelerate threat detection and response by employing AI, including agentic flows, to achieve cognitive security operations. With AI and the power of Cisco's security portfolio, you can go beyond automating known signatures to dynamically protecting against "new threats." We'll show you how to leverage Cisco's integrated security products, automation, AI, and machine learning, collectively in the right ways for optimal security efficacy, productivity, and cost.

### Unlocking Competitive Advantage with Insight: Leveraging Modern Infrastructure for Success - CNCGEN-1013
Speakers: Michael Moore (Insight)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271942794001zmHO
Cisco's infrastructure solutions, in collaboration with Insight, serve as the foundational backbone for innovation in today's rapidly evolving digital landscape. By providing robust, scalable, and secure networking infrastructure, Cisco enables organizations to harness the power of advanced technologies such as cloud computing, the Internet of Things (IoT), and artificial intelligence (AI). Insight complements this by offering tailored strategies and expert guidance that help organizations optimize their Cisco network investments. This network-centric approach facilitates seamless connectivity, enhances data accessibility, and supports the integration of cutting-edge applications, driving operational efficiency and business agility. As organizations increasingly rely on digital transformation to remain competitive, the partnership between Insight and Cisco empowers them to innovate faster, respond to market demands, and create new opportunities for growth. By establishing a reliable, secure and flexible network, Insight and Cisco lay the groundwork for future advancements, ensuring that businesses are well-equipped to navigate the challenges of tomorrow while maximizing their potential for success.

### Unlocking Data with Generative AI: From Natural Language to SQL - CISCOU-2053
Speakers: Kourtney Barnes (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271840823001zanW
In today's data-driven world, accessing and analyzing information is critical. Crafting complex SQL queries for non-technical users or even developers can be demoralizing and time consuming. In this sessions, you will see how Generative AI combined with a chatbot can make this daunting task simple and conversational. Attendees will experience how natural language inputs can be seamlessly translated into generated SQL queries allowing users to receive responses without requiring technical expertise. This session will also include a live demonstration of a Generative AI-powered chatbot generating a SQL queries in real time. Through the demonstration attendees will gain insight on utilizing AI models to handle diverse query types in an AI-driven data operation. The demonstration will dive into the core principals of Generative AI, practical implementation strategies, and integrating with a Large Language Model (LLM) and a database.

### Unlocking Day2Ops Excellence: Nexus Dashboard Innovations for ACI & NX-OS N9K Fabrics - BRKDCN-3924
Speakers: Camillo Rossi (Cisco), Domenico Dastoli (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271892636001zbxS
In most data center networks, operational paradigms are primarily reactive, leaving operators scrambling to resolve business-impacting network, security, and compliance issues long after they occur. Imagine having a powerful, intelligent assistant that alerts you to potential problems in your network and guides you in resolving them before they affect your business. In this session, discover how to harness the capabilities of Nexus Dashboard (ND) to proactively identify and address issues within Cisco Application Centric Infrastructure (ACI) or NX-OS fabrics, transforming your approach from reactive to proactive.

### Unlocking Edge Power: Controlling and Transforming Telemetry with OpenTelemetry Collector Pipelines - DEVNET-2145
Speakers: Renato Quedas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271912583001znDe
In an era where real-time insights drive competitive advantage, processing telemetry data at the edge can significantly enhance performance and responsiveness. Join us for an engaging session on leveraging OpenTelemetry Collector's Processors to efficiently handle telemetry data directly at the edge. This session will delve into the OpenTelemtry Collector Pipelines and practical applications of edge processing, showcasing how it can control and transform the telemetry you sent to any observability backend, including Splunk. Participants will explore various processors, understand configuration best practices, and discover how telemetry data is processed and represented in the the—OpenTelemetry Protocol (OTLP) before it's sent to a backend. This session will equip you with the knowledge and tools to harness the full potential of telemetry processing on the edge with OpenTelemetry. Don't miss the opportunity to transform your telemetry strategy and gain a robust framework for future-proof observability.

### Unlocking Human-Centered Leadership with AI - ITLGEN-2052
Speakers: Scott Herpolsheimer (Cisco), Marissa Afton (Potential Project)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271956490001zFvX
With the power, promise, and potential of AI, leaders have an extraordinary opportunity to leverage it to enhance the way they lead. In this session, we will explore " The AI-Enabled Leader" framework—walking through several practical examples of how AI can help leaders to do hard things in a more human way, share practical tips and strategies to enhance leadership effectiveness through AI, and learn how to harness the power of AI ethically and responsibly.

### Unlocking Multi-Cloud Performance with ThousandEyes Cloud Insights - PSOENT-1026
Speakers: Alistair Scott (Cisco), John Brinley (Huron Consulting Group Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271928430001zl9t
Discover how ThousandEyes Cloud Insights offers deep visibility into cloud-native traffic and configuration changes. Learn how to monitor multi-cloud infrastructure health to ensure seamless, reliable, and high-performance digital experiences.

### Unlocking Next-Level Performance: Explore the Latest Innovations in Splunk AppDynamics - PSOOBS-1112
Speakers: Courtney Dragoon (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271976812001z4QE
Get ready to supercharge your 3-tier application monitoring with Splunk AppDynamics! In this dynamic session, We'll be exploring key updates that will put you ahead of the curve. Discover how our powerful LLM Monitoring and Session Replay features are setting new standards in troubleshooting and user optimization. Here's what We'll dive into: LLM Monitoring: Unlock full visibility into your AI stack with metrics for GPUs, Langchain, and Vector DBs, ensuring your models perform at their peak. Session Replay: Skip the guesswork'replay user sessions to pinpoint issues and enhance user experiences in real-time. Smart Agent Auto-Deployment: Let our smart agent handle the heavy lifting, automating discovery and deployment to keep you focused on innovation. Anomaly Detection for Infrastructure and Databases: Stay ahead of the game with AI-powered anomaly detection that proactively spots performance hiccups.

### Unlocking the Automation Power in Catalyst Center for Wired and Wireless Networks - BRKOPS-2697
Speakers: Lila Rousseaux (Cisco), Adam Radford (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271989777001zjSX
Cisco Catalyst Center empowers Campus and Branch networks with powerful Assurance and Automation c apabilities. While many network administrators start their journey with Assurance for its immediate value, the real transformation lies in embracing Automation . Automation not only saves time but also reduces errors caused by manual tasks and enhances security through consistent configurations. Traditionally rooted in I ntent-Based Networking, Catalyst Center's automation capabilities are now expanding with the Campus Automation framework . This evolution simplifies automation, making it accessible for both greenfield and brownfield environments. The session will include a section on templates as part of the Automation framework. API's for both templates and Campus automation will also be covered to support the move to an Infrastructure as code model for configuration. Join us to discover how Catalyst Center's enhanced automation advancements can streamline operations and unlock new levels of efficiency for your network both wired and wireless.

### Unlocking the Future: Introducing Cisco's Industrial Networking and IoT Essentials - BRKIOT-1006
Speakers: Bob Clay (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271952570001z5L7
The field of IoT allows us to connect billions of things, acquire their data, and make better business decisions. In this one-hour session we will explore what is important to industrial operations along with relevant features for industrial networking and security. We will conclude with an overview of the latest innovations being announced for industrial switches, routers, wireless and security.

### Unlocking the Power of Edge Computing and AI: Challenges, Use Cases, and Cisco's Edge Compute Solutions - BRKCOM-1009
Speakers: Ronnie Chan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271858733001zwHq
In an increasingly interconnected world, the edge is where data transforms into action. Edge computing is transforming industries by enabling real-time insights and intelligent decision-making closer to the source of data. But what exactly makes edge so powerful, and how can organizations unlock its full potential? Join us for an engaging session that explores the transformative possibilities of edge computing, showcasing real-world use cases across industries such as retail, healthcare, and manufacturing. Participants will gain insights into overcoming common deployment challenges and learn how Cisco's portfolio of compute solutions empowers organizations to operationalize intelligence at the edge. This session is designed for IT decision-makers and technical professionals with an interest in leveraging edge technologies to drive business outcomes. Whether you're new to the edge or ready to optimize your deployments, this session will provide strategies to succeed.

### Unmanaged No More: Elevating Zero-Trust Security in Dynamic Environments - VILIOT-2006
Speakers: Peter Lund (CLAROTY INC., MEDIGATE BY CLAROTY)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271950769001zsS4
The rising connectivity of XIoT in healthcare and manufacturing increases network breaches. Organizations require continuous unmanaged device detection, rapid vulnerability response, and robust security. This session details how Claroty xDome and Cisco ISE together establish Zero-Trust for cyber-physical and other unmanaged XIoT devices. This integration enforces security policies, enhances network segmentation, and substantially lowers exposure risks, boosting cyber and operational resilience.

### Unpacking the Big Bag of Architecture Wisdom - BRKXAR-2130
Speakers: Michael Fries (Cisco), Matt Engle (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271871578001z3lR
Bringing over 50 years of architecture experience, Mike and Matt will provide a conversational approach to architecture that accounts for where the ivory tower gets flattened by reality. Pulling from their greatest successes (and epic failures), they will share practical tips on how to maximize the value of architecture in the modern organization. Emphasizing the pillars of People, Process, and Technology with all the underlying Governance, we will explore real world challenges that limit the value of architecture and provide prescriptive steps to overcome those challenges. By taking a comprehensive view of implementation, we will explore the importance of Automation, Operations, Resiliency, and Ethical AI. Coming out of this session, you will have a framework and techniques that can be implemented to immediately begin realizing your target state architecture.

### Untangle the multi cloud maze and simplify hybrid cloud connectivity with Catalyst SDWAN - BRKCLD-1512
Speakers: Saswat Praharaj (Cisco), Michalina Słomiańska (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271846913001zALI
Struggling with the networking complexity of multiple cloud providers? Join us to break down VPC networking constructs across AWS, Azure, and Google Cloud-and see how Cisco is trying to unify these disparate environments. Then, discover how Catalyst SD-WAN, with its Cloud OnRamp for Multicloud features, simplifies hybrid connectivity and management. Whether you're a network engineer, architect or an executive, you'll gain practical insights and strategies to untangle the multi-cloud maze and streamline your hybrid cloud networking.

### Untangling the Complexity of UC Management: Real-World Solutions for Real-World Challenges - VILCOL-1065
Speakers: Todd Remely (Unimax)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271848229001zEWK
Managing Today's UC environments is tougher than ever - multiple platforms, limited resources, and constant change. This session dives into the three biggest pain points UC and telecom teams face - and how to solve them. Learn how to streamline UC administration, gain actionable call data recordding (CDR) insights, automate workflows like provisioning, and safely offload routine MACDs to Tier 1 support. We'll also tackle the headache of phone number management with a smarter approach to DID administration. Whether you're running a single UC platform or a multi-vendor environment, you'll leave with practical strategies for simpler, more effective UC management.

### Upgrade Branches in Minutes, not Months - PSOENT-1020
Speakers: Arpitha Shetty (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271927243001zlU4
More is demanded from the branch than ever before: more predictable performance and bandwidth for thirsty apps, more cybersecurity to protect against the latest sophisticated threats, more sustainable infrastructure, and support for the latest wireless connectivity. And all this across hundreds if not thousands of locations. Learn how Cisco Unified Branch can programmatically slash the time taken to upgrade routing, security, wireless, and switching infrastructure across branch locations at huge scale. The result? Futureproofed modern branches with the latest technology stack and unified management to streamline operations and improve experience.

### Use Your Experience to Empower the Next Generation: Teach and Inspire with Cisco Networking Academy - CISCOU-1700
Speakers: Rick Graziani (Cabrillo College and UC Santa Cruz), Hank Preston (Cisco), Telethia Willis (Cisco), Patrick Gargano (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272018248001ztH3
What if your expertise could inspire the next generation of tech leaders? Join us for an engaging session to discover how you can make a lasting impact through Cisco Networking Academy, one of the world's longest-running and most impactful free skills-to-jobs programs, transforming 24.2 million learners in 191 countries over the past 26 years. Find out how you can sign up for more information to connect with local Academies, teach, and share your passion for networking, cybersecurity, and AI to help shape the future workforce. Whether you're a seasoned professional or eager to give back, this session will show you the first steps to join a global movement driving innovation and opportunity. Your knowledge can change lives—be a part of the impact!

### Ushering in a New Era of 5G Innovation with Cisco's Multi-Use Case Mobility Services Platform (MSP) - BRKSPM-2341
Speakers: Derick Linegar (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271965230001zxWI
Today there are hundreds of mobile core networks around the world that are individually deployed, configured, integrated and operated with almost the same functionality, in hundreds of permutations. A radical new approach is required to drive adoption and monetization of new technologies such as 5G stand-alone (SA) with the flexibility required by both Service Providers and Enterprises. Cisco's multi-tenant Mobility Services Platform (MSP) has been designed to address this challenge and allow Service Providers and Enterprises alike to benefit from state-of-the-art tech practices to deliver growth and develop new business models. In this session, you will learn about Cisco's Mobility Services Platform (MSP) and how its "as-a-Service" approach differs from traditional on-prem and managed services models. You will also discover key real-life Use Cases across multiple domains including private 5G, IoT, B2B, MVNE/O, FWA, etc and the way these Use Cases are enabled through modern API-driven programmability in line with TM Forum specifications, combined with an AnyG Converged Core and simplified operations. Understanding of Mobile Packet Core technologies is recommended.

### Using Ethernet for AI Networking - CISCOU-2061
Speakers: Peter Jones (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271841957001zlTN
The emergence of GenAI is driving an un-precedented investment in AI focused data centers. InfiniBand is the incumbent networking technology, but the industry wants standards based technologies to drive efficiencies. What will it take for Ethernet to succeed in this emerging enormous market?

### Using Terraform to Automate your Meraki Deployment - DEVNET-2080
Speakers: Michael Lipsey (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271899220001zBrb
The Meraki Dashboard is a wonder tool to easily deploy a large scale network including SD-WAN, Wireless, and many features and functionality. The challenge when you have many networks in on organization or multiple organizations to manage, configure and monitor is that even with the ability to use templates and clone networks - you might not want to do just that. Using Terraform you can leverage the best of both worlds, configure and deploy through the Dashboard API to get each and every network exactly the way you want it while also maintaining the ease of use and operational simplicity of the Meraki Dashboard. In this session will walk through how to do just that, we'll show benefits of automation via terraform vs the standard capabilities in the Meraki Dashboard.

### Using ThousandEyes to CYB - DEVNET-2048
Speakers: Marc Nufrio (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271898476001zMCI
Making changes to a production network can feel like walking a tightrope - one misstep can have a big impact. In this session, We'll explore how to use the ThousandEyes APIs to automate network monitoring and proactively detect operational issues. you'll learn how to set up automated checks to verify network health, identify potential mishaps in real-time, and reduce downtime - so you can deploy faster, and with confidence. Get ready to take control with the power of automation!

### VXLAN BGP EVPN Multi-Site - BRKDCN-2913
Speakers: Lukas Krattiger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271888263001z4dg
This session will cover the evolution of Cisco's approaches for efficiently connecting separate VXLAN BGP EVPN fabrics. We'll start by introducing the difference to multi-pod and multi-fabric, with the goal of understanding the evolution to the VXLAN multi-site approach that represents the optimal and recommended way to interconnect separate VXLAN EVPN islands. VXLAN provides an excellent encapsulation and EVPN provides extensive capabilities as a control plane. With VXLAN and EVPN, we have excellent capabilities for data center fabric deployments with an integrated layer-2 and layer-3 approach. With the maturity of the control and data plane, new capabilities for interconnecting multiple fabrics is experiencing growing interest with VXLAN BGP EVPN. Note: This session is exclusively focused on NX-OS stand-alone VXLAN EVPN and does not discuss the multi-pod and multi-site solutions offered with Cisco ACI.

### VXLAN EVPN Shared Border designs and automation - BRKDCN-2665
Speakers: Yianni Thallas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271886176001zpJe
In this session participants will understand why a shared border is needed and how to connect external devices like firewalls, and external routers. To achieve a single point of enforcement and deterministic flows for multi-site enabled fabrics. By the end of this session, participants will leave with the knowledge and prerequisites to implement a shared border design. This session will also cover how this can be automated using Nexus Dashboard Fabric Controller. Participants should have a basic understanding of VXLAN EVPN prior to joining this session.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966
Speakers: Lukas Krattiger (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271893016001zKXr
This session focuses on a day in the life of a VXLAN EVPN packet. How we route and bridge and how multi-destination traffic is handled. This session will help you to understand what happens on the ingress VTEP all the way to the egress VTEP and beyond.

### Virtual Tour: Tech & Sustainability in Cisco's Modern Offices - PP-1313
Speakers: Bob Cicero (Cisco), Andy Smith (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271949210001zaRS
Step into the future of work with a virtual tour of one of Cisco's cutting-edge offices, where technology and energy efficiency come together to create the ultimate modern workplace. Tailored for IT leaders, workplace managers, and sustainability champions, this session offers an inside look at how Cisco integrates smart workplace technologies to create efficient, innovative office environments. you'll gain practical insights on how to use data and automation to optimize office space, reduce operational costs, increase energy efficiency, and support hybrid workstyles. Don't miss this chance to future-proof your workplace and lead the charge in workspace innovation.

### Virtual Workforce Network Engineer -- NTT DATA's Agentic AI Platform - CNCATO-2008
Speakers: Daniel Dollinger (NTT DATA), Stephen Smith (NTT DATA), Matt Brady (NTT DATA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271831328001zDw2
The future of Autonomous Agents is here, powered by NTT DATA and Cisco. Join to explore how NTT built an advanced Agentic AI platform to augment infrastructure engineers in network operations and other critical infrastructure disciplines across the Cisco ecosystem.

### Voice Security for Cisco: Protecting UC & CC from Vishing, Social Eng, GenAI-Based Attacks - VILSEC-1048
Speakers: Roger Northrop (Mutare, Inc.)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271991511001zTzA
Voice is an increasingly targeted threat vector. In fact, many of the largest, most high-profile breaches began when cybercriminals successfully used the business telephone for initial access. Organizations who have invested in Cisco UC, UCaaS, CC and CCaaS have options for enterprise-class voice security. You can eliminate nefarious and nuisance calls at the network edge, at the inception of the call flow. This Session is relevant to Cisco customers / prospects, Cisco partners, and others throughout the Cisco ecosystem who are looking for a proven voice security solution, purpose-built to address the unique nature of voice-based attacks. Mutare's voice security platform protects Cisco Unified Communications Manager (CUCM), Cisco Unified Border Element (CUBE), Cisco Unity Connection, Webex Cloud Contact Center and Webex Calling.

### We're sensing something new here - CTF-1047
Speakers: Ross Sweetzir (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271985011001zwHO
Unlock powerful insights with the visualization of Operational Technology (OT) data. This session showcases how to aggregate data from Meraki sensors, Cisco Room devices, Cisco Spaces, third-party sensors, and more via the Splunk Edge Hub and Operational Technology Intelligence. See how seamless integration and real-time analytics bring indoor environments to life, optimizing air quality, occupancy, and operational efficiency all in one intuitive dashboard.

### Webex Calling Multi-Tenant Architecture - BRKCOL-2698
Speakers: Owen Friel (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271857217001zFla
This session pulls back the covers on the Webex Calling Multi-Tenant Architecture and will provide in-depth information on the technical details of key Webex Calling capabilities. This session will give customers and partners insights into how Webex Calling operates, and give them the information they need to understand how Webex Calling provides secure and reliable services. Topics will include: Global topology: what services run in what geographic regions? Data residency: where is my data stored? Media: how is media routed and processed for my globally distributed users? AI: how do Webex Calling AI features work? Where is my data processed? High availability: how does HA work? What happens on failures? Security: how is my media and data at rest and in transit secured?

### Webex Contact Center Developer Overview - DEVNET-1699
Speakers: Arun Ganeshan (Cisco), Adam Weeks (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271896894001z8ir
This conference session provides an in-depth overview of developing for Webex Contact Center, focusing on the utilization of APIs, Agent Desktop Widgets, and SDKs. Participants will learn how to leverage these tools to enhance the functionality and customization of their contact center solutions, optimizing agent productivity and customer experience.

### Webex Contact Center Unleashed: Embark on Transformational Journey of CX - BRKCCT-1024
Speakers: Zack Taylor (Cisco), Carlos Guadamuz (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271863678001zaQj
Unlock the potential of your customer engagement strategy with our comprehensive session on Webex Contact Center. Did you know that businesses leveraging advanced contact center solutions experience up to a 30% boost in customer satisfaction? Whether you're new to Webex or keen on the latest updates, this session is your gateway to mastering its capabilities. Explore key features like proactive contact delivery, AI-driven self-service, and intelligent routing. Dive into real-world examples to understand how these tools revolutionize customer interactions. Tailored for both technical and business audiences, this introductory to intermediate session promises valuable insights for CC managers, administrators, and CX experts eager to enhance their customer experience strategies.

### Webex Control Hub - Configuring and Troubleshooting Microsoft Azure Active Directory Wizard App - TACCOL-2016
Speakers: Josh Amsden (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271851472001zaqe
"Setting up the Entra ID (Azure AD) Wizard App streamlines the onboarding and user management processes within Control Hub. This session will guide you through the steps to: • Grant tenant-wide admin consent to an enterprise application in the Microsoft Entra Admin Center. • Add the Cisco Webex app from the Azure app gallery. • Assign users to the application in Entra ID. • Collect Entra ID/Azure AD logs for troubleshooting. We will also cover how to troubleshoot and resolve common integration issues, including: • Azure AD Integration Error: “Requested Resource Was Not Found” By the end of the session, you'll be equipped to effectively configure, manage, and resolve issues related to the Microsoft Azure Active Directory Wizard App."

### Webex Customer Experience Solutions: Unlock the full potential of AI for your CX - BRKCCT-1022
Speakers: Holger Esser (Cisco), Sara Santos (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271865057001zP8i
The integration of Customer Experience (CX) and Artificial Intelligence (AI) is driving one of the most transformative shifts in today's technological landscape, offering unprecedented opportunities for businesses of all sizes to create exceptional user experiences. AI is enhancing every layer of the Customer Experience stack, from proactive customer journeys and AI-powered virtual agents to tools that assist human contact center agents. In this session, participants will explore Cisco's innovative approach to leveraging AI in the Customer Experience domain. Beyond just the products, we'll delve into the key areas of focus that enterprises must address to maximize value and achieve a strong return on their AI investments. Through feature demonstrations and real-world use cases, attendees will gain insights into the AI capabilities of Webex Customer Experience Solutions, understand Cisco's overarching AI strategy, and learn about other essential elements for successful AI implementation.

### Webex Data Management, Control, and Loss Prevention - BRKCOL-2126
Speakers: Matthew Jordy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271856625001zg94
Webex provides organizations with a full suite of cloud collaboration services enabling users to communicate and share content with other users both inside and outside the organization. With this collaboration comes risk and Webex customers must ensure that their organization's sensitive data is secured and protected from unauthorized access and loss. This session examines organization data management and control topics for Webex deployments including: Built-in data control and data retention capabilities of Webex Webex APIs for monitoring and controlling organization data External compliance platform integrations for data loss prevention (DLP), eDiscovery, legal hold, and archiving To illustrate key concepts and operations, these topics will be demonstrated using Webex organizations and integrations to external compliance platforms including: Cisco Cloudlock and Theta Lake. Attendees should have some familiarity with Webex collaboration services and the Webex Control Hub management and administration portal.

### Webex Edge Connect Design and Deployment for Webex Meetings, Calling and Dedicated Instance - BRKCOL-2094
Speakers: Richard Murphy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271853205001zzh2
Webex, a highly advanced cloud platform, is continually evolving and improving. Webex Edge Connect enables access to the Webex backbone for Meetings and Calling services via a private network peering link. In this session, we will explore the Edge Connect solution, discuss critical design considerations for each architecture type, share deployment best practices, and present the latest updates to the offering. Prior basic knowledge of Webex Meetings and Calling products is essential to fully comprehend the session's content.

### Webex Workforce Optimization -- Built for the modern contact center - BRKCCT-1025
Speakers: Rajiv Krishnan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271863880001zd67
This session shall provide an overview of the powerful Webex Workforce Optimization (WFO) suite of applications which includes Quality Management, Workforce Management and Analytics. You will also learn about Webex WFO Insights, the new AI-powered contact center business intelligence tool. As you would be aware, to enable companies to provide efficient, effective, customer-focused service in the contact center, supervisors must have the tools they need to manage team performance. Join me in this session to understand how Webex WFO transforms the supervisor experience, giving supervisors access to more data and more powerful tools in simplified and flexible views so they are better equipped to lead their teams in delivering exceptional customer experiences. You will learn how the Webex WFO solution empowers agents with intuitive self-scheduling options and performance assessment. The overall direction with respect to Webex WFO shall also be shared.

### What's the NAC with ACI...? - CISCOU-2065
Speakers: Steve Sharman (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271842705001zG5y
Don't know your EPG from your BD? Confused by Contracts and Filters? No idea on how to define and build your Tenants? Are Access Policies melting your mind? Do you want to watch the presenter break out into a cold sweat whilst doing a live demo? In this short presentation we'll recap on all the ACI terminology and build a network from scratch using Nexus as Code - all live with no smoke and mirrors

### Where Sustainability and Affordability Meet - PP-1300
Speakers: Justin Cashman (Cisco), Stephen Kelly (NTT Data Inc), Mary de Wysocki (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271947068001zXRo
Sustainability, efficiency, and affordability can coexist with innovative solutions like Cisco Refresh and Cisco Green Pay offering long-term cost savings and environmental benefits. Cisco Refresh offers fully certified remanufactured products at a reduced cost compared to new equipment. The program also has other benefits — for example, by purchasing Cisco Refresh switches or IP phones, customers can achieve at least a 60% reduction in embodied carbon emissions compared to equivalent new products. Cisco Capital enables companies to get access to Cisco technology through flexible payment and support for the products throughout its lifecycle. Cisco Green Pay offers predictable payments, free product returns, and access to Cisco's technologies that can support companies with their sustainability goals. Finding the right balance between cutting-edge technology, sustainability, and limited budgets can be tough. That's why programs like Cisco Refresh and Cisco Green Pay are designed to support organizations of all sizes — learn how to get technology solutions and business outcomes, faster and more efficiently.

### Why Packet Capture Is Essential for Effective Incident Response and Threat Hunting - VILSEC-1049
Speakers: Michael Morris (Endace)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271991702001zdMO
Security teams are overwhelmed with alarms coming from many tools in your security infrastructure. The challenge is sorting out the false positives from the real threats. Analysts need reliable evidence to confidently report and remediate issues. Finding ways to accelerate incident response times is imperative to stay ahead of threat actors. This session will explain: Why many leading SoC teams are integrating Endace's always-on network packet capture with Cisco XDR, Cisco Firewall Threat Defense, Cisco Network Analytics, Splunk, or Splunk SOAR for simplified user workflows and more conclusive investigations. How network packet data dramatically increases a SOC team's productivity and accuracy in threat investigations. Illustrate investigating real-life attacks to demonstrate the efficiency gained with EndaceProbes in your security infrastructure.

### Why The Best Leaders Don't Need to Be "Technical" - ITLSTS-2100
Speakers: Somer Shively (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271958585001zlmH
So often in technical organizations, promotion to leadership comes with demonstration of strong technical understanding. But being a people-leader has nothing to do with your technical know-how, it has everything to do with your ability to be empathetic, drive outcomes over outputs, and coach others. The best teams have leaders focused on the team culture instead of just the team deliverables. The best leaders are rarely technical experts. They are people experts! But how can you lead when you don't have all the technical details? In this session, you'll learn strategies for how to build a strong team culture, discuss tangible examples of how to empower your people's growth, and how it all ties to together to drive outcomes that will ensure your team delivers the right technical outputs without you having to know all of the details.

### Why You Shouldn't Fear Upgrading Your ACI Fabric: The Handbook! - BRKDCN-2910
Speakers: Joey Ristaino (Cisco), Takuya Kishida (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271887890001znXX
The Cisco Application Centric Infrastructure (ACI) architecture provides a single dashboard to manage hundreds of switches within your data center. This allows for a simple and seamless upgrade workflow, since everything can be automated or initiated from one place: the APIC controller. However, without knowing what happens "under the hood" when an upgrade is started, planning and executing a successful ACI upgrade may feel more like "shooting from the hip." This session aims at removing that doubt by providing a concise overview of what is happening to the APICs and switches as they undergo a software upgrade. Furthermore, this session will cover best practices and provide tools you can leverage to do "health checks" and audits of the pre-upgrade environment. This ensures that known issues are caught beforehand rather than during the upgrade, thus mitigating failure and enabling success. With this knowledge, you will have the utmost confidence in how to perform your ACI upgrade successfully, on time, and without heartburn.

### Why You Shouldn't Fear Your Firewall Upgrade: The Evolution and How-to Guide - BRKSEC-2929
Speakers: John Payne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272005646001zfZX
The Cisco Secure Firewall Management Center (FMC) provides a singular view for management of your Cisco Firewalls while ensuring ease of operations with a simple and seamless upgrade workflow for both FMC and Secure Firewalls. This session aims to remove doubt and complexity when approaching the topic of upgrades and Cisco Secure Firewall. Furthering the discussion, this session will cover where upgrades started and end up at how the upgrade procedure has evolved within the vast feature-set available in FMC. In this session, you will also learn why you should take advantage increased quality and functionality from upgrading.

### Why does the enterprise need the Cisco Secure AI Factory with NVIDIA? - AIHUB-1115
Speakers: Marty Jain (NVIDIA)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271877039001zYC0
Enterprises are witnessing a rapid evolution of AI-from perception-based models to generative AI, now advancing to agentic AI capable of reasoning, extending into physical AI. The rise of agentic AI and reasoning models impacts all enterprise lines of business including IT, customer experience, product design, supply chain, etc. Implementing agentic AI in production requires a different approach to address the complexities of the data center infrastructure, software stack, and security, to be able to produce intelligence at scale. Such demands necessitate an "AI Factory" that offers superior TCO, is energy efficient, manifesting via a validated accelerated computing full stack architecture to deliver fastest time to business value, with security embedded at each layer. Join this session and hear how the Cisco Secure AI Factory with NVIDIA delivers the foundational AI platform for all enterprise AI needs. Don't miss seeing the Cisco Secure AI Factory with NVIDIA come to life with AI demos in the Cisco showcase.

### Wi-Fi 7 is Here - Are you Ready? - BRKEWN-2025
Speakers: Anand Gurumurthy (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271940044001zjZz
Wi-Fi standards continuously evolve to cater to the needs of the latest applications and use cases. The next generation of Wi-Fi, i.e Wi-Fi 7, has created a lot of buzz, and is set to enhance wireless connectivity with unprecedented speeds, ultra-low latency and very high efficiency. As this next-generation standard emerges, organizations must be prepared to leverage its full potential. This session will explore the key advancements of Wi-Fi 7, that includes 4K QAM, 320 MHz channel width, Multi-Link Operation, Preamble Puncturing, Multi Resource Units, and how these features will impact network performance, scalability and security. We'll also discuss the necessary infrastructure updates, security updates and strategies to ensure a smooth transition. Join us to discover how Wi-Fi 7 can elevate your network capabilities and learn about the steps you need to take to stay ahead.

### Wi-Fi Mounting: Having the Right Mount Matters - CNCENS-1014
Speakers: John Pearce (Hubbell)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271918392001zWzt
In Today's interconnected world, the efficiency of Wi-Fi networks is crucial for seamless communication in both business and personal settings. One often overlooked aspect of Wi-Fi network optimization is the selection of the appropriate mount for access points. This presentation will explore the critical factors to consider when choosing mounts for Wi-Fi access points to ensure robust network performance, security, and compliance with aesthetic and regulatory standards.

### Wireless Network Automation with Cisco Catalyst Center - BRKEWN-2306
Speakers: Vasant Nagarajan (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271938854001z2Kf
As Prime Infrastructure approaches end of life, it's time to migrate to Cisco Catalyst Center. This session aims to help attendees understand the Wireless Prime parity features and how Cisco Catalyst Center simplifies the provisioning of different aspects of the wireless network through intuitive workflows. The session will also showcase the visibility provided by Cisco Catalyst Center into the Wi-Fi deployment, which delivers instant value after a successful migration. The following topics will be covered: How to automate the data migration into Cisco Catalyst Center Understanding the Wireless Prime Parity Features in Cisco Catalyst Center How to easily bring up sites that are completely based on business intent, as well as managing your existing wireless infrastructure Understanding advanced configuration aspects (Guest Anchor, HA- SSO, N+1, Mesh, RLAN) How to easily perform AP Refresh/RMA and configure AP parameters using reusable AP templates

### Women in Tech: Building Connections Builds Careers - CENGEN-1910
Speakers: Kenya Asli (City of Baltimore), Carrie Palin (Cisco), Marcus Moffett (Cisco), Riley Zelczak (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1749592614394001XmvT
Join us for a lively conversation about the tech industry- from inspiring women who've navigated the path from early roles to global leadership at Cisco and beyond! Whether you're just starting out or looking to level up, our panelists will share real experiences, practical advice, and the support systems that helped them succeed and pave the way for an inclusive future for all. Walk away with insights, practical tips, and new connections to help you grow your skills and make your mark in the industry! Moderated by: Marcus Moffett.

### Working with Cisco ISE pxGrid APIs - DEVNET-2038
Speakers: Viktor Bobrov (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271898289001z8Z7
Cisco ISE comes with a robust information sharing Platform Exchange Grid (pxGrid) framework. This session will cover architectural advances in pxGrid 2.0 and show how developers can easily build integrations using the new client-less - WebSockets & REST interface. You will learn how to connect to a pxGrid server, retrieve information, discover and subscribe to available pxGrid topics. We will cover newest additions to pxGrid capabilities including pxGrid Direct and push capabilities This session will also guide you through pxGrid on Cisco DevNet to get you started developing integrations using pxGrid. We will introduce a CLI client to quickly interface with pxGrid framework without writing a single line of code.

### You Won't Believe How Splunk Built This Mind-Blowing Plugin for Microsoft Security Copilot - DEVNET-2336
Speakers: Wayne Brown (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271904395001zAa5
In this session, we'll explore the reasons behind why Splunk's partner engineering organization built a plugin for Microsoft Security Copilot. We'll dive into the use cases behind the engineering effort, take a look at the artifacts used

### Your AI Adoption Journey: Accelerate and Maximize Al Value - PSOCX-1019
Speakers: Jack Hampson (Cisco), Carlos Pereira (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272014535001zD1U
AI is set to revolutionize technology and transform businesses. However, with AI becoming a buzzword, distinguishing real advancements from hype can be challenging. In this session, we'll examine real-life examples from both Cisco and customers as they embark on their AI adoption journey. We'll start by discussing how to prioritize use cases with clear business potential and ROI. Then, we'll explore assessing the feasibility of these cases quickly, focusing on data processing, model development, and integration. We'll also cover building AI solutions, including validation, proof of concept, and deployment, highlighting key insights on workflows, model choices, and security. Finally, we'll show how you can adopt, optimize, and maintain AI solutions to maximize value. You'll gain practical insights, learn from real-world experiences, and discover best practices and tools to help your organization leverage AI effectively.

### Your Cloud Needs Real-Time Observability - PSOOBS-1110
Speakers: Don Benne (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271976433001zhd7
The wrong cloud monitoring strategy could be costing your business. Cloud architectures introduce additional complexity into your environment that traditional tools and approaches weren't built to handle. This often results in slowed troubleshooting and skyrocketing MTTRs, which put business-critical services at risk, increased storage costs, and lost team productivity. Your cloud needs an observability approach that is faster and more flexible. In this session, We'll share how standardizing data collection, adjusting your data management strategy to include cost-efficient metrics, and real-time analytics delivered by Splunk Observability Cloud can help you optimize your cloud and microservices observability to keep your digital systems resilient. We will cover: - Leveraging out-of-the-box content and real-time alerts for quicker incident response - Standardizing data collection and correlating logs and metrics for easier troubleshooting

### Your Journey Towards AI Infrastructure Sustainability - BRKGRN-1019
Speakers: Chih-Tsung Huang (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271837931001zXK8
At first glance, AI Sustainability may seem to be an oxymoron. But as you look deeper, Sustainability and AI can be quite harmonious. This session will walk through examples of how Cisco is an enabler of AI Sustainability and best practices for your journey towards it with the Cisco ecosystem. Materials covered are: (1) AI infrastructure stack (AI frameworks, AI management, AI computing, AI fabrics); (2) AI Sustainability solutions; and (3) Our path forward together.

### ZTNA - Private resource end to end troubleshooting - TACSEC-2020
Speakers: Jaikishan Yadav (Cisco), Jeff Richmond (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271997171001zakN
Zero Trust Network Access (ZTNA) is a modern security framework that ensures secure access to private resources by verifying every user and device before granting access, regardless of their location. Cisco's Secure Access ZTNA solution is designed to protect sensitive data and applications by implementing a zero-trust model for resource access. However, issues with accessing private resources can arise due to misconfiguration or network problems. This abstract focuses on troubleshooting techniques for resolving access issues within a Cisco Secure Access ZTNA environment.

### Zero Trust Access: Enterprise Browsers and Secure Client - BRKSEC-2882
Speakers: Christian Clasen (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272004091001zpGa
Cisco is enhancing it's approach to Zero Trust through two new innovations: direct Integration with Google's Chrome Enterprise Browser, and enhancements to the Secure Client ZTNA module that will allow it to secure internet connectivity in addition to private application connectivity. This session will explore how and why Enterprise Browsers are an important part of SSE strategy, and how the technical pieces fit together between Cisco Secure Access and Google's product. It will then discuss the exciting evolution of the ZTNA module that will enable a more comprehensive roaming security solution.

### Zero Trust Evolution Using the Latest Emergent Technology - BRKSEC-2930
Speakers: Anthony Sabella (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272005835001zTvP
As cyber threats continue to evolve, companies are considering the use of new emergent technology to bolster Zero Trust posture. We will explore how advancements in Quantum encryption, AI/ML, IAM, eBPF and more are working their way into Enterprise networks and ultimately influencing the evolution of Zero Trust maturity. We'll also dive into how Cisco is harnessing these advancements in their latest solutions.

### Zero Trust Security for Cloud & Beyond with Cisco Hybrid Mesh Firewall - BRKSEC-2787
Speakers: Nadir Lakhani (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750272003506001zCbW
Securing modern infrastructures in an era of distributed applications and dynamic networks requires a reimagined approach. Cisco's Hybrid Mesh Firewall delivers a highly distributed security fabric, centrally managed through Unified Management, to protect applications across any deployment. This session explores the shift from traditional perimeter security to a micro-perimeter model, tackling challenges in hybrid cloud, containers, and software-defined networks. It highlights AI-driven security's role in countering evolving threats while showcasing real-world use cases that emphasize the need for unified policy management. As complexity grows, seamless integration and consistent governance become critical. Learn the architecture, design principles, and real-world applications of Cisco's Hybrid Mesh Firewall & how it strengthens cyber defences, streamlines processes, and addresses the challenges of securing hybrid cloud, containers, and software-defined networks.

### Zero Trust: Secure the Workplace with Cisco Software-Defined Access - BRKENS-1851
Speakers: Keith Baldwin (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271919890001zSj1
Attackers use a variety of methods to compromise targets, often causing significant business disruption. To combat this issue, Cisco has developed a comprehensive solution: Software-Defined Access (SD-Access). This platform provides a foundational pillar for automating network-segmentation capabilities and allowing users to establish micro-perimeters for users, devices, and IoT networks. SD-Access meets the strict zero-trust requirements by establishing trust, enforcing trust-based access, continuously verifying trust, and responding to changes in trust. In this session, attendees will gain an understanding of the challenges posed by traditional networks and how SD-Access fabric architecture overcomes these issues with a policy-driven approach. Additionally, attendees will have the opportunity to hear from a peer who will share their experience on how this solution solved their zero-trust needs.

### Zero-Trust Unlocked: Safeguarding Unmanaged Devices in a Connected World - VILIOT-1005
Speakers: Steve Baum (CLAROTY)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271950573001zary
As connectivity across managed and unmanaged devices and networks grows in healthcare and manufacturing verticals, network breaches are increasing in both frequency and severity. In the face of these challenges, organizations require new solutions that constantly detect new, unmanaged devices connecting to the network, speed-up response times for vulnerable devices, and maintain a defensive security posture in order to achieve better cyber and operational resilience. In this session we explore how Claroty xDome integration with Cisco ISE unlocks approaches for Zero-Trust for cyber-physical systems (CPS) to enforce policies, deliver network segmentation, and significantly reduce exposure-based risks for the enterprise.

### eBPF, what it is? and why is so cool - DEVNET-1686
Speakers: jesus Illescas (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271896513001zSR9
eBPF (Extended Berkeley Packet Filter) is a groundbreaking technology for running sandboxed programs in the Linux kernel without altering the kernel source code or requiring a system restart. This session will highlight the importance of eBPF and its key use cases. You'll leave this session with ideas to help you: • Implement network monitoring and security measures. • Enhance system observability. Designed for participants with a foundational understanding of Linux internals, we will demonstrate eBPF's capabilities in containerized environments like Kubernetes, supported by open-source projects such as Cilium. Join us to understand how eBPF can revolutionize DevOps and SRE practices. Understanding of Linux internals is recommended.

### gRPC, gNMI, gNOI... Oh My! An Enterprise Network Automation Journey - BRKDEV-2017
Speakers: Jeremy Cohoe (Cisco), Story DeWeese (Cisco)
page: https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1750271910835001zrju
How many Google API micro services are there on Cisco IOS XE, and what are their capabilities? At the end of this session not only will you be able to answer this question with confidence but you will also have a deep understanding of the solutions and real world use cases that are enabled as part of the Google Network Management API. But what about Model Driven Telemetry? What are the best practices for mutual TLS authentication and collection of large amounts of telemetry data ? This session covers the complete Programmability & Automation lifecycle of the Cisco Catalyst 9000 when managed using gRPC, gNMI and gNOI... oh my!

