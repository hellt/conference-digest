>>> HOW TO RUN THIS <<<
This is the digest prompt for cph-automate-2026. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/cph-automate-2026.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/cph-automate-2026.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, cloud
platforms, Kubernetes, and AI. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect); cloud infrastructure and operations (public and private
cloud, virtualization, compute/storage/networking, multi-tenancy, and
automation); Kubernetes and cloud-native systems (architecture and
operations, eBPF, Cilium, Kubernetes networking, Gateway API, service mesh,
IPAM, and BGP/datapath internals); and AI (AI/ML systems, LLMs and agents,
model training and inference, GPU/accelerator infrastructure, networking for
AI, and ML for infrastructure operations). Physical DC and WAN systems work is
CORE to this PM, not adjacent — do not down-rank a paper for being about
hardware, optics, or datacenter fabric.

Below is the program for CPH^Automate 2026 (Copenhagen). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

Judge each item by what it changes for a practitioner: novel techniques and
firmly substantiated results over incremental benchmark improvements, and
operational lessons, tooling, automation and postmortems that transfer across
environments over org-specific anecdotes or vendor pitches in disguise.
Treat strong empirical evaluation and real deployment experience as signals of
weight; treat unvalidated claims with caution. Note when a technique depends
on a specific operator's scale, topology or silicon.

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
  (networking, cloud, Kubernetes, or AI) as they work on them today.
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

## Search keywords

The site's search indexes topic keywords per page. After the Themes section,
append ONE fenced `json` code block - the pipeline reads it machine-side and
removes it before publishing, so it is never rendered - of exactly this shape:

```json
{"post": ["cloud", "ai"], "talks": {"<pick heading>": ["cloud", "ai-networks"], "<pick heading>": ["kubernetes", "cni"]}}
```

- "post": 3-6 topics this digest as a whole covers.
- "talks": one entry for EVERY pick you selected, keyed by its exact `###`
  heading string (copy it character for character, including any presenter
  part), with 2-4 tags naming what the talk is about - the technology or
  practice, not its tier or the conference.
- Tags are lowercase, hyphenated, single concepts. Use ONLY tags from this
  vocabulary:

- `ai` - artificial intelligence systems, applications and practices not covered by a finer AI tag
- `deepseek` - DeepSeek models, research, deployment and inference economics
- `openai` - OpenAI models, products, APIs and deployment engineering
- `anthropic` - Anthropic Claude models, agent SDKs and deployment engineering
- `z-ai` - Z.ai/Zhipu GLM models, open weights and deployment engineering
- `moonshot` - Moonshot AI Kimi models and deployment engineering
- `ai-networks` - networking for AI/ML training and inference clusters (job-level load balancing, collectives, topology-aware scheduling)
- `gpu-clusters` - GPU accelerator interconnects and cluster fabrics (NVLink, scale-up vs scale-out)
- `ml-for-networking` - machine learning applied to network operation (anomaly detection, traffic prediction, AIOps)
- `data-center-fabric` - physical data-center fabric design (topologies, CLOS, buffer management, congestion)
- `optics` - optical transport, transceivers, pluggables, DWDM, LPO/CPO
- `ethernet` - Ethernet as a technology standard (P802.3 work, speeds, PHYs)
- `cabling` - structured cabling, fiber plants, MPO/MTP, copper
- `power` - power delivery and efficiency in DCs (PUE, 48V, power sourcing equipment)
- `dpu` - data processing units, SmartNICs, offload and hardware offload in general
- `rdma` - RDMA, RoCE, InfiniBand, remote memory semantics
- `load-balancing` - traffic load balancing, ECMP/adaptive hashing, LB algorithms and architectures
- `packet-scheduling` - packet scheduling and queueing disciplines (PIFO, QoS schedulers, traffic management)
- `congestion-control` - congestion control and notification (ECN, PFC, DCQCN, L4S)
- `switching` - switch hardware and forwarding architecture (ASICs, buffers, pipelines)
- `silicon` - switch/NPU ASIC design, chip roadmaps, co-packaging
- `bgp` - BGP the protocol and its operation
- `routing-protocols` - routing protocol design and operation in general (ISIS, OSPF, BGP convergence)
- `segment-routing` - SR, SRv6, SR-MPLS and network programming with them
- `ipv6` - IPv6, its deployment and transition
- `mpls` - MPLS, labels, and LDP/RSVP heritage
- `peering` - peering business and practice, IXPs, interconnection agreements
- `interconnection` - data center interconnect and carrier interconnection
- `cdn` - content delivery networks
- `address-policy` - IP address and ASN allocation policy (RIR policy processes)
- `internet-governance` - regulation, standards bodies, and geopolitics of the internet
- `kubernetes` - Kubernetes architecture, operations, workloads and networking
- `cni` - container network interfaces and container networking plugins
- `containers` - containerization, images, runtimes
- `service-mesh` - service mesh (sidecars, eBPF meshes, mTLS between services)
- `cloud` - public and private cloud infrastructure, platforms and operations
- `cloud-native` - cloud-native patterns in general (CNCF ecosystem)
- `orchestration` - workflow and device orchestration, intent-based systems, network controllers
- `automation` - network automation (tooling, pipelines, source of truth, CI/CD for networks)
- `configuration-management` - managing device configuration at scale (config generation, drift, validation)
- `gitops` - GitOps workflows and version control practices
- `p4` - the P4 language and P4-programmable targets
- `linux-networking` - the Linux kernel networking stack (TC, netlink, drivers, offloads)
- `programmable-dataplane` - programmable data planes in general (PNA, portable switch OSes, pipes)
- `ebpf` - eBPF, XDP, and kernel bypass dataplanes
- `http` - HTTP and web protocols, QUIC
- `ipam` - IP address management and allocation
- `sdn` - software-defined networking, controllers, separation of control and data plane
- `network-security` - network security topics not covered by a finer tag
- `email-security` - email security and phishing (DMARC, spam, brand abuse)
- `malware-analysis` - malware, reverse engineering, botnet takedowns
- `threat-intelligence` - threat intel, IoCs, attack tracking
- `vulnerability-management` - vulnerability disclosure, patching, CVE economy
- `offensive-security` - offensive security, red teaming, exploit development
- `privacy` - privacy engineering, tracking, anonymity, privacy-preserving systems
- `censorship` - censorship, filtering, and measurement of Internet shutdowns
- `ddos` - DDoS attack and defense
- `anomaly-detection` - detecting anomalies and attacks in traffic
- `firewall` - firewalling and network policy enforcement
- `tls` - TLS, certificates, and protocol encryption
- `encryption` - encryption of traffic and data in general (MACsec, IPsec, E2E)
- `quantum-safe` - post-quantum cryptography and migration
- `quantum-networking` - quantum networking and entanglement distribution as infrastructure
- `pki` - public key infrastructure, certificate lifecycle
- `attestation` - remote attestation, measured boot, hardware roots of trust
- `zero-trust` - zero-trust architecture and microsegmentation
- `identity` - digital identity, identity ecosystems, ID standardization
- `authentication` - authentication methods and protocols (MFA, passkeys, WebAuthn)
- `authorization` - authorization, OAuth/OIDC, access control, policy engines
- `observability` - network observability tooling, telemetry pipelines, flow data
- `telemetry` - telemetry protocols (gNMI, streaming, INT)
- `measurement` - measurement methodology, probing, active/passive measurement studies
- `benchmarking` - benchmarks, testbeds, performance evaluation of systems
- `testing` - testing and verification of networks and configs (formal verification belongs here)
- `sre` - site reliability engineering practice, incident response, operations culture
- `capacity-planning` - capacity planning and forecasting
- `troubleshooting` - troubleshooting and root-cause analysis, outages and postmortems
- `dns` - DNS, resolvers, authoritative infrastructure
- `multicast` - multicast and broadcast replication
- `wifi` - wireless and mobility
- `mobile` - mobile and cellular networks (5G, roaming, RAN)
- `iot` - Internet of Things scale problems, LPWAN
- `cxl` - CXL and memory-fabric interconnects for pooled memory
- `time-sync` - time and clock distribution (NTP/PTP, GNSS timing)
- `spectrum` - radio spectrum policy and management
- `open-source` - open-source project practice and sustainability
- `standardization` - standards processes (IETF/IEEE) and documents
- `api` - APIs for network control (REST/gRPC, schemas, contract design)

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
conference: CPH^Automate 2026 (Copenhagen)
source_url: https://cph-automate.network/2026/schedule/
generated: 2026-11-14
registry_key: cph-automate-2026
-->

Then the digest as markdown: it starts with a single `#` heading that is the
digest's title, followed by the tiers as `##` sections, Themes as a final `##`
section, and then the keywords block.

- The `#` heading is the conference name and nothing else — e.g. `# IETF 123
  (Madrid)`. Never add anything after the name: no audience or type qualifier
  ("for a Networking / AI PM", "Operator", "Standards"), no tagline,
  and not the word "Digest".

============================ PROGRAM TEXT ============================

## Program

### What Should You Build When You Can Build Anything?
Speakers: Damien Garros
page: https://cph-automate.network/talks/what-should-you-build/ | slides: https://cph-automate.network/talks/what-should-you-build/Damien-Garros_CPH-Automate%20What%20should%20you%20build%20when%20you%20can%20build%20anything%20__compressed.pdf
Being able to build almost anything does not make decisions easier. It creates more possibilities, and therefore more difficult choices. Every time we ask, “Should we build this?”, we must also consider a “buy” option that AI is making better and faster. Most discussions focus on how AI helps individuals build their own tools. But we speak less about what AI means for the vendors competing with these tools. This is also an important part of the build-versus-buy decision. AI is changing the capabilities of both internal teams and software vendors, so the comparison between them is changing as well. In this talk, we will take a step back from the hype and consider what the software industry may look like after this transition. What will still be worth building ourselves? What will be better to buy? And what will be assembled from existing components? We will explore these questions in the specific context of network automation. What do these changes mean for our industry, and how will AI affect what network automation teams choose to build, buy, or assemble from existing components? The talk will not provide one answer that works for everyone. Instead, it will offer a framework—and better questions—to help you decide what to build, what to buy, and what to combine.

### Democratizing Network Automation: What We Learned Building an Open Automation Stack
Speakers: Göran Edin
page: https://cph-automate.network/talks/democratizing-network-automation-what-we-learned-building-an-open-automation-stack/ | slides: https://cph-automate.network/talks/democratizing-network-automation-what-we-learned-building-an-open-automation-stack/Goran-Edin_Democratizing%20Network%20Automation.pdf
Network automation is often presented as something reserved for the largest operators with dedicated automation teams and substantial budgets. This presentation tells the story of how a regional operator and Ductus took a different approach: focusing on a solid architectural foundation, an incremental delivery model, and open technologies to build a sustainable automation platform. The result isn’t just a successful implementation—it’s a demonstration that advanced network automation can be achievable for operators of all sizes.

### Transformation Through Community
Speakers: Andreas Bækdahl, Emil Commerou
page: https://cph-automate.network/talks/transformation-through-community/ | slides: https://cph-automate.network/talks/transformation-through-community/Andreas-Baekdal-CPH%20Automate.pdf
We turned a classic professional services organization into a curious automation-forward team. Network automation does not scale through tools and platform alone — we built a thriving network automation community in Wingmen Solutions through 6 individual threads: Platform: Remove developer friction. Learning: A curious space. Documentation: Tailored recipes for success. Support: Open door policy. Lab: Break while you make. Tools: Aim for good enough; just in time.

### Bootstrapping a Source of Truth in a Brownfield Environment: Field-Tested Patterns
Speakers: Constantin VURLI
page: https://cph-automate.network/talks/bootstrapping-a-source-of-truth-in-a-brownfield-environment/ | slides: https://cph-automate.network/talks/bootstrapping-a-source-of-truth-in-a-brownfield-environment/Constantin-VURLI_CPH.pptx
Going through the challenges of initializing a SoT in an already existing environment, a few design and implementation patterns to solve them (consolidating a by-spine with a few basic fields, aligning all referentials on this and then iterating on it, for example). Common mistakes and finally how to maintain it over time. It is based on my experience as a network automation consultant who designed and implemented a dozen SoTs (mostly NetBox and a few Infrahub instances) in diverse enterprise environments.

### JSON freedom or chaos; how to trust your data
Speakers: Bart Dorlandt
page: https://cph-automate.network/talks/json-freedom-or-chaos/ | slides: https://cph-automate.network/talks/json-freedom-or-chaos/json_freedom_or_chaos_cphautomate.pdf
Can you trust your data? In this talk we’ll take a real life use case where the flexibility desires and time have gotten the best of it. What happens when you deal with “freedom” data? How to go from this to a better future? It is a technical talk how we recognise changes are desired, validation is required for trust to grow. Pydantic and pytest are used to work towards a solution where failing fast is a main objective.

### Keeping ~2k IP Pools Filled with Just-in-Time Provisioning
Speakers: Kristoffer Larsen
page: https://cph-automate.network/talks/keeping-ip-pools-filled-with-just-in-time-provisioning/ | slides: https://cph-automate.network/talks/keeping-ip-pools-filled-with-just-in-time-provisioning/Kristoffer-Larsen-CPH-auto-JIT_provisioning.pptx
In a constantly changing network, efficient utilization of scarce IPv4 address space is critical. Learn how we closed the automation loop by leveraging NETCONF notification streaming to dynamically provision IP pools exactly when and where they are needed.

### Vibe-ops: Migrating production infrastructure with an AI agent
Speakers: Marcus Hoff
page: https://cph-automate.network/talks/vibe-ops-migrating-production-infrastructure-with-an-ai-agent/ | slides: https://cph-automate.network/talks/vibe-ops-migrating-production-infrastructure-with-an-ai-agent/Marcus-Hoff-vibe-ops-final.pptx
I migrated our whole infrastructure off VMware in two weeks with Claude Code as my pair-operator — Proxmox, an HA firewall pair, SSO, CI, monitoring, the lot. This is the honest story of what an AI can actually do in production ops, and the afternoon one firewall change took the entire network down with us outside.

### Memory has no changelog
Speakers: Ahmed Shawky
page: https://cph-automate.network/talks/memory-has-no-changelog/ | slides: https://cph-automate.network/talks/memory-has-no-changelog/Ahmed-Shawky_memory-has-no-changelog.pdf
We asked two route planners to write down how they route fibre and got back 98 sections — which turned out to describe routing by who owns the building , while the same engineers had for years actually been routing by what’s physically installed there . This is how we stopped asking people to remember, recovered the real rules by replaying historical decisions out of the inventory database, why the target turned out to be agreement rather than correctness, and the one line of code I invented by accident that got one in four trunk selections wrong without ever raising an error.

### Shift Left: Building Network Automation That Lasts
Speakers: Wim Henderickx
page: https://cph-automate.network/talks/shift-left-building-network-automation-that-lasts/ | slides: https://cph-automate.network/talks/shift-left-building-network-automation-that-lasts/Wim-Henderickx_CPH-Automate-ShiftLeft.pptx
Getting something automated is hard. Keeping it automated as networks, platforms, and business requirements evolve is even harder. Too often, automation is treated as the final step of a project rather than something that should influence how systems, data models, APIs, and operational processes are designed from the beginning. The result is brittle automation that requires constant maintenance, struggles to adapt to change, and eventually becomes more expensive to maintain than the manual processes it replaced. A shift-left approach encourages us to think about automation much earlier in the lifecycle. By considering automation during the design of services, APIs, data models, workflows, and operational practices, we can build systems that are easier to automate, easier to evolve, and easier to operate over the long term. In this session we share ideas and experiences that help move network automation from a collection of scripts to a sustainable engineering discipline.

### When Your Source of Truth Isn't Really Yours: Lessons from Cross-Team Integrations
Speakers: Niclas Skøtt Petersen
page: https://cph-automate.network/talks/source-of-truth-isnt-yours/ | slides: https://cph-automate.network/talks/source-of-truth-isnt-yours/Niclas-Sk%C3%B8tt-PetersenWhen%20Your%20Source%20of%20Truth%20Isn%27t%20Really%20Yours_Lessons%20from%20Cross-Team%20Integrations.pptx
What happens when another team integrates directly with your Source of Truth and their needs start limiting your ability to evolve your platform? In this talk, I will share lessons learned from operating a Source of Truth that supported critical business processes while also serving as a dependency for another team through a complex, poorly documented integration. Because the integration was tightly coupled and the consuming team had different organizational priorities, even small improvements to data models, processes, and workflows became difficult to implement. The session explores the challenges that arise when ownership, responsibilities, and priorities are not clearly separated between teams, and how these issues can slow down innovation and increase operational risk. I will also discuss practical approaches that helped improve collaboration and reduce complexity, including: – Creating simpler and more stable interfaces between teams – Clearly documenting ownership, expectations, and integration contracts – Implementing automated and continuous testing to detect breaking changes early – Reducing coupling to enable independent evolution of systems and processes Attendees will leave with actionable ideas for designing team boundaries and integrations that scale with both technical and organizational change.

### Laziness. A Blessing or a Curse?
Speakers: Urs Baumann
page: https://cph-automate.network/talks/laziness-a-blessing-or-a-curse/ | slides: https://cph-automate.network/talks/laziness-a-blessing-or-a-curse/Urs-Baumann_laziness.pdf
For decades we have discussed network automation, continually hoping the next tool or technology will solve it. Perhaps the issue is not the technology at all. Maybe we are just lazy. This speech questions a number of unpleasant assumptions concerning automation, AI, engineering culture and our obsession with the next exciting innovation. This speech presents an uncomfortable examination of the reasons why we could be the main obstacle to network automation.

