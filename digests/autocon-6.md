<!--
conference: AutoCon 6
source_url: https://networkautomation.forum/autocon6
generated: 2026-11-23
registry_key: autocon-6
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AutoCon 6

**A note on sources:** the program material for this event lists titles, speakers, and session times only — no abstracts and no paper/slide/video links, so nothing could be fetched to enrich the write-ups. Everything below is inferred from the talk titles and speakers; each pick is marked accordingly. No results or figures are claimed beyond what the titles state. AutoCon is a network-automation conference, so most of the program is adjacent to your core stack by definition — the picks below focus on where automation, AI-for-networking, and validation practice intersect your interests.

## Core

### 60/40: How Meta Taught AI to Triage Its Own Network

Goutam Nalamati

- **Why**: This is the ml-for-networking item of the conference — an AI system doing network triage in production at hyperscale, exactly the intersection of your AI and network-operations interests. Large-operator production experience is the signal here, not a demo.
- **What**: Appears to cover Meta deploying AI to triage network events/failures at production scale; the "60/40" framing suggests a measurable split between what the AI handles and what escalates to humans. *(inferred from title only — no abstract in program)*
- **How**: Unknown from the program text; likely a pipeline combining telemetry, anomaly/event detection, and classification or LLM-based triage trained or evaluated on Meta's operational history. *(cannot be confirmed without the talk)*
- **Where applicable**: Almost certainly Meta-specific in its training data, topology, and tooling — treat the transferable value as the methodology and the human/AI division of labor, not the artifacts. *(assessment based on title and venue only)*

### From PoC to the NOC: A Multi-Agent Network Troubleshooting Platform at Internet2

Karl Newell

- **Why**: Multi-agent AI applied to network troubleshooting, moving from proof-of-concept to live NOC use — directly relevant to anyone thinking about AI agents in network operations. Internet2 is a real, complex research/education backbone, not a lab rig.
- **What**: A multi-agent platform for network troubleshooting that has progressed beyond PoC into NOC operation at Internet2. The "PoC to the NOC" framing promises the hard part: what it took to survive production. *(inferred from title only)*
- **How**: Presumably multiple cooperating agents (diagnosis, data gathering, remediation candidates) orchestrated over Internet2's telemetry and tooling. *(cannot be confirmed from program text)*
- **Where applicable**: R&E backbone context — different scale and culture from an enterprise or cloud DC, but the PoC-to-production journey and agent-orchestration lessons should transfer.

### Agentic Networking is here - Introducing the Tools and Techniques Required to be Successful

John Capobianco

- **Why**: The practical on-ramp talk for agentic AI in network operations — the "how do I actually do this" companion to the Meta and Internet2 stories. Directly relevant to your LLM/agents interests.
- **What**: An introduction to the tools and techniques required to make agentic networking work in practice. *(inferred from title only)*
- **How**: Likely covers agent frameworks, tool/function calling against network APIs, guardrails, and evaluation of agent behavior on network tasks. *(cannot be confirmed from program text)*
- **Where applicable**: Framed as generally applicable tools and techniques — useful as a survey of the current agentic toolbox; treat as an orientation talk, not a validated-results talk.

### Network Automation Agentified: Self-serving Network Deployments using AI Agents Soup to Nuts

Senad Palislamovic

- **Why**: End-to-end ("soup to nuts") AI-agent-driven deployment automation — the delivery side of agentic networking, complementing the troubleshooting-focused talks. Relevant to both your automation and AI-agent interests.
- **What**: Using AI agents to enable self-service network deployment — consumers of network capacity requesting and receiving changes without human intermediation, apparently covering the full pipeline. *(inferred from title only)*
- **How**: Presumably agents wrapping intent capture, validation, and automated provisioning on top of existing automation infrastructure. *(cannot be confirmed from program text)*
- **Where applicable**: The self-service model depends heavily on how well-defined your deployment patterns and guardrails already are — most viable where change types are standardized. The "soup to nuts" claim needs the talk's evidence.

### Human Driven AI: Who's Actually Driving Your Network's AI?

Ryan Booth

- **Why**: The counterweight talk to the agentic enthusiasm — who is accountable and in control when AI acts on the network. For a PM shipping AI-driven operations tooling, the human-in-the-loop question is a product question, not just a safety one.
- **What**: An examination of the human's role in AI-driven network operations — oversight, accountability, and who is really making the decisions. *(inferred from title only)*
- **How**: Likely a discussion of human-in-the-loop patterns, approval gates, and the failure modes of under- or over-trusting AI in network change. *(cannot be confirmed from program text)*
- **Where applicable**: Generally applicable wherever AI touches production networks; the quality depends on whether it offers concrete patterns versus opinion.

### Stop Funding Hallucinations: A Seasoned Technologist's Guide to Business Success with AI Evaluation

Eric Chou

- **Why**: AI evaluation ("evals") is becoming the gating discipline for shipping any AI feature, including network agents — this looks like the eval talk for the automation context. Relevant to your AI product work even outside networking.
- **What**: A practitioner's guide to evaluating AI — presumably measuring whether AI-driven automation actually works before funding or scaling it, and the business consequences of not doing so. *(inferred from title only)*
- **How**: Likely eval methodology applied to network-automation AI: test sets, accuracy/impact measurement, and tying evaluation to investment decisions. *(cannot be confirmed from program text)*
- **Where applicable**: Evals are a general technique; the network-automation framing should make the examples directly reusable.

## Adjacent

### Digital Twinning at Scale

Russ White

- **Why**: Digital twins of networks — simulation and modeling at scale — matter for change validation, capacity work, and increasingly as the safe environment in which AI agents can act. Russ White reliably brings architectural depth rather than vendor talk.
- **What**: Digital twinning of networks at scale — modeling a production network faithfully enough to be useful. *(inferred from title and speaker only)*
- **How**: Unknown from the program text; likely covers model fidelity, data sources for building twins, and what "at scale" costs computationally and operationally. *(cannot be confirmed)*
- **Where applicable**: The hard constraint is twin fidelity — a twin is only as good as the state and topology data feeding it, which ties it back to source-of-truth discipline.

### 2026 State of Network Automation Survey Results

Chris Grundemann

- **Why**: Annual survey data is one of the few cross-organization, non-anecdotal signals in this field — useful for benchmarking where automation adoption actually stands versus the conference's optimism.
- **What**: Results of the 2026 State of Network Automation survey. *(inferred from title only — no data available in program text)*
- **How**: Survey methodology across the network-automation community. *(cannot be confirmed from program text)*
- **Where applicable**: Broadly applicable as industry benchmarking; watch for sampling bias inherent in survey-of-practitioners methodology.

### Every Automation Demo Lies: What Building a Disposable Network Lab Platform Taught Me

Craig Johnson

- **Why**: The title is a good thesis — demos flatter automation that then fails on real devices. A disposable lab platform for testing automation is the CI/CD-for-networks story, which transfers across environments.
- **What**: Lessons from building a lab platform for spinning up throwaway network topologies to test automation before it touches production. *(inferred from title only)*
- **How**: Presumably containerized/ virtualized network OS images, topology-as-code, and ephemeral environments wired into automation pipelines. *(cannot be confirmed from program text)*
- **Where applicable**: Broadly applicable technique; fidelity to real hardware behavior is the known constraint (compare with the mock-devices talk below).

### Test Before You Touch the Network: Reproducing Real Device Behavior with Mock Devices

Pieter van Os

- **Why**: The complement to lab platforms: mocking device behavior so automation can be tested without the gear. Directly relevant to network CI/CD and to providing safe sandboxes for AI agents.
- **What**: Reproducing real device behavior with mock devices so that pre-deployment testing exercises realistic responses, not just happy paths. *(inferred from title only)*
- **How**: Presumably emulated device interfaces (CLI/NETCONF/API) with realistic state and error behavior for test scenarios. *(cannot be confirmed from program text)*
- **Where applicable**: General technique; the perennial risk is mock divergence from real firmware behavior — worth hearing how they keep mocks honest.

### From Failure to Recovery: Designing Resumable Network Upgrade Automation

Joseph Nicholson

- **Why**: Upgrade automation is where automation meets physical networks most dangerously. "Resumable" design — surviving mid-failure and recovering — is an operational lesson that transfers to any change-automation pipeline.
- **What**: Design patterns for network upgrade automation that can fail partway through and be resumed or recovered rather than leaving the network half-upgraded. *(inferred from title only)*
- **How**: Likely checkpointing, per-device state tracking, idempotent stages, and rollback/retry semantics. *(cannot be confirmed from program text)*
- **Where applicable**: Broadly applicable to brownfield upgrade workflows; specifics may depend on the speaker's platform mix.

### Deploying IPv6 doesn’t work without automation (but that is true with other stuff too!)

Ed Horley (Lightning Talk)

- **Why**: IPv6 deployment is in your wheelhouse, and the thesis — that v6 at scale is effectively impossible manually — matches long-standing field experience. A short but on-topic lightning talk.
- **What**: IPv6 deployment efforts fail without automation; the same dependency holds broadly. *(inferred from title only)*
- **How**: Unknown; likely practical argument from v6 deployment experience (address planning, dual-run, SLAAC/DHCPv6 handling at scale). *(cannot be confirmed from program text)*
- **Where applicable**: Any organization still treating IPv6 as a manual add-on.

### What Should You Build When You Can Build Anything?

Damien Garros (Closing Keynote)

- **Why**: With agentic AI lowering the cost of building almost anything, the scarce skill becomes choosing what to build. As a closing keynote from a longtime network-automation practitioner, this is likely a build-vs-buy-vs-reuse synthesis rather than a pitch.
- **What**: A framework (or at least a strong opinion) on prioritization now that AI makes building custom tooling dramatically cheaper. *(inferred from title and speaker only)*
- **How**: Unknown from the program text. *(cannot be confirmed)*
- **Where applicable**: Universally relevant to platform/automation teams; watch for whether it offers decision criteria or war stories.

## Wildcard

### The adoption gap is an accounting gap: how to measure what your automation returned

Jonathon Davis

- **Why**: A genuinely different framing: automation stalls not for technical reasons but because organizations can't measure its return. An economics/measurement lens on a field that over-indexes on tooling — the kind of reframe you wouldn't search for.
- **What**: The argument that the automation adoption gap is really a measurement/accounting gap, plus methods for quantifying what automation returned. *(inferred from title only)*
- **How**: Presumably attribution of automation outcomes to cost/velocity metrics that finance and leadership recognize. *(cannot be confirmed from program text)*
- **Where applicable**: Any organization whose automation program has plateaued despite working technology; org-culture dependent in execution.

### I 💖 YANG. Said No Python Developer Ever

Urs Baumann

- **Why**: The YANG-vs-Python culture clash is a real, under-discussed fault line in network automation — structured data models versus ad-hoc tooling. It signals where the interface between standards-based modeling and modern automation practice is heading.
- **What**: An exploration of why YANG meets resistance from Python-centric automation developers, and presumably what to do about it. *(inferred from title only)*
- **How**: Unknown from the program text — could cover YANG tooling pain, model-driven automation benefits, or bridging approaches. *(cannot be confirmed)*
- **Where applicable**: Relevant wherever gNMI/NETCONF/YANG model-driven automation meets script-based automation cultures — i.e., most enterprises.

### You Do It, I Do It, Teach It To Me: Using AI To Upskill Network Engineers in Automation

Erika Dietrick (Lightning Talk)

- **Why**: Using AI itself as the on-ramp for engineers learning automation — a meta-application that points at where LLMs change skills development, not just operations. Interesting signal on AI's second-order effects on the workforce.
- **What**: Using AI to teach network engineers automation skills, apparently a structured show-teach approach. *(inferred from title only)*
- **How**: Unknown from the program text — likely AI-assisted tutoring/code-review in an automation curriculum. *(cannot be confirmed)*
- **Where applicable**: Teams facing the skills bottleneck in automation adoption; broadly applicable.

## Themes

- **Agentic AI has arrived in network operations, and the field is past the demo stage.** Multiple talks (Meta's AI triage, Internet2's NOC platform, agentified deployments, Capobianco's toolkit) describe AI agents doing real triage, troubleshooting, and deployment work — the center of gravity of this year's program.
- **Trust, governance, and evaluation are the new gating questions.** "Who's actually driving," "stop funding hallucinations," and the human-in-the-loop talk form a cluster: the field's energy is shifting from *can agents do this* to *how do we prove it, bound it, and stay accountable*.
- **Test-before-touch is maturing into real infrastructure.** Disposable labs, mock devices, digital twins, and resumable upgrades all attack the same problem: change safety on physical networks. Pre-deployment validation is becoming a first-class discipline — and doubles as the sandbox AI agents need.
- **Source-of-truth and config discipline remain the unglamorous foundation.** Intended configuration, Nautobot federation, and the Excel horror story show that data quality still determines whether anything above it (including AI) works.
- **The bottleneck is increasingly people and economics, not tooling.** Mentorship, upskilling, who-builds-automation team questions, and the "adoption gap is an accounting gap" talk all point at organizational and measurement limits rather than technical ones.
