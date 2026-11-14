<!--
conference: CPH^Automate 2026 (Copenhagen)
source_url: https://cph-automate.network/2026/schedule/
generated: 2026-11-14
registry_key: cph-automate-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# CPH^Automate 2026 (Copenhagen)

CPH^Automate is a single-track network-automation conference, and the 2026 program is unusually coherent: roughly half the talks are, at heart, about the *data layer* of automation — sources of truth, schemas, and the history locked in operational databases — while AI agents appear both as pair-operators in production and as assemblers of automation stacks. For a PM whose interests span physical fabric, cloud/infra ops, and AI, the picks below are weighted toward talks with real deployment experience, honest failure stories, and transferable patterns.

## Core

### Memory has no changelog

**Links:** [Abstract](https://cph-automate.network/talks/memory-has-no-changelog/) · [Slides](https://cph-automate.network/talks/memory-has-no-changelog/Ahmed-Shawky_memory-has-no-changelog.pdf)

Ahmed Shawky — Lead Expert Scientist, Data & AI, Arelion (AS1299)

- **Why**: The best talk in the program, and the one that sits squarely on the PM's physical-infrastructure interests: automating *physical fiber cross-connect routing* at a Tier-1 backbone (80k km of own fiber, 350+ PoPs, thousands of cross-connect orders per year). It is also a rare, fully quantified case of mining operational rules from history instead of from expert documentation — directly relevant to ML-for-operations.
- **What**: Arelion's route planners wrote down their fiber-routing process: 95 sections — of which 47 were screenshots, and 40 paragraphs did little more than point at a picture. The document turned out to be *partial recall of a process they execute perfectly every day*, not the spec. The team stopped asking people to remember and instead replayed 100 historical orders: for each, they pulled what the engineer actually chose from the inventory system's history tables and reconstructed what was available *the day before they chose it*. Cross-tabulating choice against options made the real branching rules fall out. Validation ran on 48 tuning orders (46 of 48 defensible decisions, 96% agreement — and zero exact matches, because which position you take was never the decision) and then 160 live orders: 62% fully hands-off, 31% escalated to a human *by design*, 4 broke from upstream data gaps, and there was not one routing error in 160.
- **How**: The method is the contribution: (1) pin every source view to an as-of date of *decision date − 1* (13 views, one date — get this wrong and every derived rule is confidently garbage); (2) cross-tabulate actual choices against available options; (3) treat the expert document as a cross-check, not the source; (4) measure *agreement with expert judgment*, not correctness — a system that agrees 100% has memorized outputs, not modeled judgment; (5) show human reviewers only the *changed* decisions (152 orders became 55 reviewable questions). The talk's most instructive confession: the speaker invented a plausible tie-break rule ("prefer owned over rented trunks") that existed nowhere in the documentation, and it silently steered 24 of 91 trunk picks to trunks the documented rules would never have returned — all 24 returning success. Once in code, an invented rule is indistinguishable from a derived one.
- **Where applicable**: Arelion-specific (their inventory history tables, their fiber plant), but the technique — as-of reconstruction, agreement metrics, diff-based human review, and deliberately hunting for rules you invented — transfers to any brownfield automation where the real process lives in the database's history rather than in anyone's memory.

### Vibe-ops: Migrating production infrastructure with an AI agent

**Links:** [Abstract](https://cph-automate.network/talks/vibe-ops-migrating-production-infrastructure-with-an-ai-agent/) · [Slides](https://cph-automate.network/talks/vibe-ops-migrating-production-infrastructure-with-an-ai-agent/Marcus-Hoff-vibe-ops-final.pptx)

Marcus Hoff

- **Why**: A first-person account of an AI agent running production infrastructure work, on a problem many organizations face right now — the VMware exit. The PM's cloud/virtualization and AI-in-ops interests intersect exactly here.
- **What**: The speaker migrated an entire infrastructure off VMware in two weeks with Claude Code as pair-operator: Proxmox, an HA firewall pair, SSO, CI, and monitoring. Crucially, this is framed as the honest story — including the afternoon one firewall change took the entire network down with the team off-site. (from abstract only)
- **How**: Agentic AI used as a pair-operator across a full-stack migration rather than as a code-completion assistant; the abstract promises a candid accounting of what an AI can and cannot do in production ops. Technical mechanism details are in the slides, which were not available to this run.
- **Where applicable**: Small-team / single-operator infrastructure scale; results are tied to that context and to one migration, so treat it as a data point on agentic ops rather than a generalizable method. Worth watching for the failure story as much as the two-week timeline.

### What Should You Build When You Can Build Anything?

**Links:** [Abstract](https://cph-automate.network/talks/what-should-you-build/) · [Slides](https://cph-automate.network/talks/what-should-you-build/Damien-Garros_CPH-Automate%20What%20should%20you%20build%20when%20you%20can%20build%20anything%20__compressed.pdf)

Damien Garros — Co-founder & CEO, OpsMill (creator of Infrahub)

- **Why**: AI is changing both sides of the build-vs-buy equation — internal teams *and* vendors get superpowers — which makes this the strategic question for anyone owning an automation platform or roadmap. Unusually, the talk addresses the vendor side of the comparison, not just the builder side.
- **What**: A framework, not a case study. The slides argue: AI-driven productivity means vendor offerings will improve and get cheaper (prediction: price down, quality up) while customization becomes cheap enough that "everyone gets a custom build — a designer house for the price of a commercial one." The proposed path: (1) define the fundamental building blocks of an automation stack, (2) standardize the interactions between blocks (with OCP's rack-interface standardization as precedent), (3) build extensibility into every block (API, MCP, GraphQL, SDKs, plugins, agent skills), and (4) teach agents to assemble the blocks — "integrate what you can, build what you must."
- **How**: Build in layers; don't reinvent everything; standards make choice practical. The composition model treats the automation stack as standardized, extensible blocks that agents assemble on the operator's behalf.
- **Where applicable**: Conceptual and vendor-perspective — the speaker sells an infrastructure data-management platform, so the predictions should be read as one vendor's thesis about the market. The layering/standardization argument itself is broadly applicable to automation stack design.

### Democratizing Network Automation: What We Learned Building an Open Automation Stack

**Links:** [Abstract](https://cph-automate.network/talks/democratizing-network-automation-what-we-learned-building-an-open-automation-stack/) · [Slides](https://cph-automate.network/talks/democratizing-network-automation-what-we-learned-building-an-open-automation-stack/Goran-Edin_Democratizing%20Network%20Automation.pdf)

Göran Edin — CTO & Network Automation Architect, Ductus, with an unnamed regional operator

- **Why**: A real, deployed, open-source automation stack at a *regional operator* — direct evidence against the assumption that serious automation needs an enterprise-sized team. Includes concrete component choices and several lessons that transfer.
- **What**: The stack: NetBox as network source of truth (custom objects + L2VPN), Camunda 7 as business-process orchestrator, a Clixon controller for network abstraction (service-YANG / device-YANG), driving NETCONF/RESTCONF. The MVP deliberately targeted the MPLS core (L2VPN create/change/delete, CI/CD pipeline, service reconciliation) where operational complexity was highest. Key findings: "having NetBox was not the same as having the right model" — they rebuilt the information model (CFS/RFS/device layers) *before* scaling automation; the migration turned into data discovery, correcting inventory, configurations, and documentation; YANG/NETCONF gave a common foundation but "a standard interface does not guarantee standard behavior" — vendor-specific validation was still required; components were chosen to be replaceable (Camunda → Operaton or CIB seven); and AI shifted the engineers' role from writing code to steering AI (defining intent and constraints, validating outcomes).
- **How**: Architecture of source-of-truth + orchestrator + abstraction layer + external systems; incremental delivery; shared information models as the common language between business and engineering; automation as the *outcome* of good modeling rather than the starting point.
- **Where applicable**: Regional-operator MPLS core, so the service scope is telco-specific. The architecture and the model-first lesson transfer well to any mid-size operator or enterprise building automation on open components. Note the vendor co-presentation (Ductus) — but the deck reads as a case study, not a pitch.

### JSON freedom or chaos; how to trust your data

**Links:** [Abstract](https://cph-automate.network/talks/json-freedom-or-chaos/) · [Slides](https://cph-automate.network/talks/json-freedom-or-chaos/json_freedom_or_chaos_cphautomate.pdf)

Bart Dorlandt — independent consultant; founder, NLNAM

- **Why**: Every automation program eventually hits this wall: hand-maintained "freedom data" with no schema, no contract, and no trust. This is an engineering-grade treatment of the fix, with the actual validation code shown.
- **What**: A journey from massive hand-crafted JSON (fields accumulated since 2014, `true` vs `"true"`, values nobody can prove are unused) to validated, round-trippable data. The core technique is a three-way validation triangle: build Pydantic models incrementally over the existing data; prove round-trip fidelity by dumping the model back to JSON (`model_dump` with `by_alias`/`exclude_unset`) and diffing against the original with DeepDiff; and enforce *model hygiene* with pytest tests that flag optional fields that are never populated (i.e., probably obsolete) and mandatory fields that are always missing. JSON Schema generated from the models gives editor support. Pytest handles what Pydantic can't: conditional dependencies between fields and dataset-wide uniqueness (e.g., duplicate hostnames), with fixtures and parametrize covering multiple environments (prd/stg).
- **How**: Start strict (`Literal`/`Enum` over `str`, `ConfigDict(extra='forbid')` where feasible), use smart unions for known variations, split giant files into manageable typed pieces, fail fast in pipelines, and collect discrepancies as organizational decisions rather than silently patching them.
- **Where applicable**: Broadly applicable wherever JSON/YAML describes infrastructure — tooling is Python-centric (Pydantic/pytest) but the pattern is portable. The honest caveats are the real value: the ten-year problem (you can never prove nobody depends on a field) and cross-team skill gaps make this an organizational challenge, not just a technical one.

### Keeping ~2k IP Pools Filled with Just-in-Time Provisioning

**Links:** [Abstract](https://cph-automate.network/talks/keeping-ip-pools-filled-with-just-in-time-provisioning/) · [Slides](https://cph-automate.network/talks/keeping-ip-pools-filled-with-just-in-time-provisioning/Kristoffer-Larsen-CPH-auto-JIT_provisioning.pptx)

Kristoffer Larsen

- **Why**: IPAM under IPv4 scarcity is a live constraint in the PM's world, and this is a concrete event-driven closing of the automation loop rather than batch reconciliation.
- **What**: Dynamic, just-in-time provisioning of roughly 2,000 IP pools in a constantly changing network, using NETCONF notification streaming to provision pools exactly when and where they are needed instead of statically pre-allocating capacity. (from abstract only)
- **How**: Network events arriving via NETCONF notifications trigger pool provisioning — moving from static allocation toward reactive, demand-driven IPAM. Mechanism and scale details are in the slides, which were not available to this run.
- **Where applicable**: Networks with scarce IPv4 and frequent topological change; depends on devices/controllers supporting NETCONF notification streaming. Vendor and scale specifics not given in the abstract.

### Bootstrapping a Source of Truth in a Brownfield Environment: Field-Tested Patterns

**Links:** [Abstract](https://cph-automate.network/talks/bootstrapping-a-source-of-truth-in-a-brownfield-environment/) · [Slides](https://cph-automate.network/talks/bootstrapping-a-source-of-truth-in-a-brownfield-environment/Constantin-VURLI_CPH.pptx)

Constantin VURLI — network automation consultant

- **Why**: The brownfield source-of-truth bootstrap is the universal hard problem, and this draws on ~a dozen real implementations rather than one — the most pattern-dense SoT talk in the program.
- **What**: Design and implementation patterns for initializing a SoT in an already-running environment: consolidating a "by-spine" core with a few basic fields first, aligning all referentials onto that core, then iterating outward; the common mistakes to avoid; and how to maintain the SoT over time once it exists. Based on the consultant's experience designing and implementing about a dozen SoTs (mostly NetBox, a few Infrahub instances) across diverse enterprises. (from abstract only)
- **How**: Incremental consolidation-first — establish a minimal authoritative core, align everything to it, iterate — rather than big-bang data modeling. Slide detail was not available to this run.
- **Where applicable**: NetBox/Infrahub-centric, but the bootstrap patterns are aimed at diverse enterprise environments and should generalize to other SoT tools.

## Adjacent

### Shift Left: Building Network Automation That Lasts

**Links:** [Abstract](https://cph-automate.network/talks/shift-left-building-network-automation-that-lasts/) · [Slides](https://cph-automate.network/talks/shift-left-building-network-automation-that-lasts/Wim-Henderickx_CPH-Automate-ShiftLeft.pptx)

Wim Henderickx

- **Why**: Addresses the most common failure mode of automation programs — automation bolted on at the end of projects, becoming brittle and eventually more expensive than the manual process it replaced. A useful design-lifecycle counterpart to the SoT and data talks above.
- **What**: An argument for considering automation *early* in the lifecycle — during the design of services, APIs, data models, workflows, and operational practices — so systems are built to be automatable and evolvable, moving automation "from a collection of scripts to a sustainable engineering discipline." (from abstract only)
- **How**: Shift-left thinking applied to network automation: automation constraints shape data models and API contracts at design time rather than working around them afterward. The abstract offers ideas and experiences rather than measured results; the slides were not available to this run.
- **Where applicable**: General practice guidance, not tied to a specific environment — which is both its strength (broadly applicable) and its limitation (no substantiated case data in the abstract).

### When Your Source of Truth Isn't Really Yours: Lessons from Cross-Team Integrations

**Links:** [Abstract](https://cph-automate.network/talks/source-of-truth-isnt-yours/) · [Slides](https://cph-automate.network/talks/source-of-truth-isnt-yours/Niclas-Sk%C3%B8tt-PetersenWhen%20Your%20Source%20of%20Truth%20Isn%27t%20Really%20Yours_Lessons%20from%20Cross-Team%20Integrations.pptx)

Niclas Skøtt Petersen

- **Why**: Anyone whose SoT has become a dependency for other teams will recognize this: a tightly-coupled, poorly documented integration with a team that has different priorities can freeze your data model and workflows. A natural companion to the JSON-validation and SoT-bootstrap talks.
- **What**: Lessons from operating an SoT supporting critical business processes while another team integrated with it directly through a complex, poorly documented coupling — making even small model improvements difficult. The remedies presented: simpler and more stable inter-team interfaces, explicitly documented ownership and integration contracts, automated continuous testing to catch breaking changes early, and reduced coupling so systems can evolve independently. (from abstract only)
- **How**: Contract-first interfaces between teams plus CI detection of breaking changes — treating inter-team data dependencies with the same rigor as public APIs.
- **Where applicable**: The specific case is one organization's SoT platform, but the ownership/contract patterns generalize to any platform team with internal consumers. No quantitative results in the abstract.

### Transformation Through Community

**Links:** [Abstract](https://cph-automate.network/talks/transformation-through-community/) · [Slides](https://cph-automate.network/talks/transformation-through-community/Andreas-Baekdal-CPH%20Automate.pdf)

Andreas Bækdahl, Emil Commerou — Wingmen Solutions

- **Why**: A counterpoint to the tooling-heavy program: automation does not scale through platforms alone. The six-thread model is a compact, transferable framework for building automation capability in a services organization.
- **What**: How a classic professional-services org was turned into an automation-forward team through six deliberate threads: **Platform** (remove developer friction — IAM-integrated git, repo templates, formatters/linters, a publishing registry, secret management, runtime environments), **Learning** (a curious space), **Documentation** (tailored recipes — MkDocs/MkDocstrings), **Support** (open-door policy), **Lab** ("break while you make"), and **Tools** ("good enough, just-in time").
- **How**: A platform-plus-culture flywheel: lower the cost of participating, make breaking things safe, and stop gold-plating tooling.
- **Where applicable**: Wingmen Solutions-specific case, and the slides are a thin outline (the six threads with little elaboration), so depth is limited. The framework itself is org-agnostic; expect anecdotes rather than metrics.

## Wildcard

### Laziness. A Blessing or a Curse?

**Links:** [Abstract](https://cph-automate.network/talks/laziness-a-blessing-or-a-curse/) · [Slides](https://cph-automate.network/talks/laziness-a-blessing-or-a-curse/Urs-Baumann_laziness.pdf)

Urs Baumann

- **Why**: The program's only deliberate contrarian, and a signal worth noticing: after years of tool-hype (and a 2026 program otherwise full of AI agents and platforms), someone stands up to argue that the obstacle to network automation may be engineering culture itself. Not technical, but it names the current the rest of the conference is swimming in.
- **What**: A provocation questioning "a number of unpleasant assumptions concerning automation, AI, engineering culture and our obsession with the next exciting innovation" — the thesis being that we, not the technology, are the main obstacle to automation. (from abstract only; the extracted slides contain no substantive content beyond the title)
- **How**: Pure argument/culture talk — no technique, data, or deployment experience to evaluate.
- **Where applicable**: None technically. Value is as a framing device: read it against the build-vs-buy and vibe-ops talks to pressure-test how much of your automation gap is really a tooling problem. Low substance risk: if time is short, this is the first cut.

## Themes

- **The data layer is the battleground.** Five of eleven talks are fundamentally about sources of truth: brownfield bootstrapping, schema validation, cross-team SoT ownership, model-first platform building, and mining rules from inventory history. The field has clearly converged on "get the data right before writing the automation" — automation as the *outcome* of good data, not the starting point.
- **AI agents graduate from code assistants to operators.** Vibe-ops runs Claude Code as a production pair-operator (with a real outage story); Arelion mines rules from history; the Ductus stack has AI producing large parts of implementation with engineers steering intent and validation; Garros foresees agents *assembling* automation stacks from standardized blocks. The recurring division of labor: humans supply judgment and constraints, agents supply labor.
- **History beats memory for capturing process.** Arelion's replay method — reconstruct what was available at decision time and cross-tabulate what experts actually chose — is the program's most novel technique, and a template for any brownfield automation where documentation is partial recall.
- **Honest failure stories are in fashion.** The network-down afternoon, the 24-of-91 silently mis-steered trunk picks, automation costlier than the manual process it replaced — several speakers lead with their failures, and the strongest talks quantify them.
- **Small operators can now play.** An open stack (NetBox, Camunda, Clixon, Infrahub, Pydantic/pytest) at a regional operator is presented as direct evidence that enterprise-grade automation no longer requires enterprise-scale teams — with the caveat that "a standard interface does not guarantee standard behavior."
- **A self-critical current is forming.** The Laziness talk — and the skepticism underneath several others — suggests the community is starting to ask whether its tool obsession is the actual bottleneck.
