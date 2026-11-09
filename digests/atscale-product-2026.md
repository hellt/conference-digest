<!--
conference: @Scale: Product 2026
source_url: https://atscaleconference.com/events/product-2026/
generated: 2026-11-09
registry_key: atscale-product-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# @Scale: Product 2026

A calibration note up front: @Scale: Product 2026 is Meta's product-engineering conference (a merger of the old Product, RTC, Mobile, and Video events) under an "AI-native" theme. There is **no content here on datacenter networking, cloud infrastructure, or Kubernetes** — that material lives in the sister @Scale: Networking and @Scale: Systems & Reliability 2026 events. What this program does offer, and why it's still worth a scan, is a concentrated set of production reports on **AI agents running operations and quality loops at hyperscaler scale, with measured outcomes** — squarely in the PM's "LLMs and agents / ML for infrastructure operations" interest. No full papers or slides were available for this event, so every write-up below is based on the published abstract; the linked featured articles (where they exist) are the place to go deeper. Sessions with no abstract at all (Keynote, World Models for Robotics, Agentic Product Safety, AI compression for AOM, How to Discover the Future) were skipped, as was the Intel Xeon session, which reads as a vendor pitch for Xeon/AMX-based media pipelines.

## Core

### The future is products that grow themselves!

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-14)

Jubin Chheda (Meta)

- **Why**: The closest thing at this event to agents operating on infrastructure economics: an autonomous system that finds and ships compute-efficiency wins, with quantified production results. Directly relevant to agentic systems applied to operations and cost.
- **What**: Wally, a self-learning loop of agents at Meta — an optimizer, verifier, and learner — that identifies opportunities to save CPU or GPU cycles, verifies the change for correctness and safety, runs a public A/B test, and launches the winners. Claimed results: thousands of public tests, a 30% success rate, and several million dollars saved. (from abstract only)
- **How**: A closed loop: the optimizer proposes changes, the verifier gates them on correctness/safety, a live A/B test validates them on real traffic, and the learner updates the harness based on wins and fails — so the loop itself improves over iterations.
- **Where applicable**: Meta-scale production with a mature experimentation platform. The loop architecture (propose → verify → A/B → learn) is general, but the 30% success rate and dollar savings depend on Meta's traffic volume and A/B infrastructure. It assumes a public-facing product with enough users for statistically meaningful experiments — not directly portable to internal-only enterprise environments.

### From On-Call to Always-On

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-6) · [Materials](https://atscaleconference.com/from-on-call-to-always-on/)

Sumeet Arora (Meta)

- **Why**: The continuous maintenance loop — discover, triage, fix, verify before users report — is the SRE problem the PM knows well. This is one of the few talks explicitly framed around transferable design principles for delegating that loop to agents.
- **What**: How AI agents can support an always-on product maintenance loop: discovering and triaging issues, proposing fixes, and verifying outcomes, plus the engineering challenges behind such systems — providing the right product context, coordinating specialized agents, driving work to completion, and measuring quality. Includes a model for expanding autonomy as reliability improves while keeping engineers in control of consequential decisions. (from abstract only)
- **How**: A pipeline of specialized agents spanning discovery → triage → fix proposal → verification, with an autonomy ladder tied to demonstrated reliability and human sign-off retained for consequential decisions.
- **Where applicable**: Explicitly positioned as generalizable design principles rather than a Meta-only system — the talk's stated takeaway is "practical design principles for bringing agentic maintenance into your own engineering workflows." The hard parts (product context, agent coordination, quality measurement) scale with org complexity but are not Meta-specific.

### Ship Fast, Break Nothing: How AI Tests What AI Builds

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-7)

Sophie Zeng (Meta), Sreeja Thummala (Meta)

- **Why**: A production look at "AI validating AI-built code" at extreme scale — LLM-driven test generation and LLM assessors running inside the quality gate across hundreds of millions of lines of code. Relevant to anyone building or evaluating agentic dev tooling.
- **What**: Meta's Just-in-Time (JiT) Catching Test system: AI autonomously generates tests *designed to fail*, surfacing bugs before code lands, and LLM-based assessors decide which catches deserve human attention. Deployed across hundreds of millions of lines of code, claimed to proactively prevent serious production failures. (from abstract only)
- **How**: Two-stage mechanism — code-change-aware generation of adversarial "catching tests" that are constructed to expose latent bugs, followed by LLM assessors acting as the human-attention filter so the volume of machine-generated catches doesn't swamp engineers.
- **Where applicable**: Depends on Meta monorepo scale (hundreds of millions of LOC) and deep CI integration; the pattern of adversarial test generation plus LLM triage is general and reproducible at smaller scale, but the effectiveness numbers cited are Meta-specific.

### Preview Player Reliability and the Agentic Defense Loop on Edits

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-22)

Ravi Shah (Meta), Bhumi Sabarwal (Meta)

- **Why**: One of the few fully agentic operations loops at the event with a hard measured outcome: agents catching regressions, triaging alerts, and attributing failures to specific diffs — the alert-to-root-cause loop every ops team runs manually today.
- **What**: Reliability work on Meta's Edits media-preview experience across iOS, Android, and server, plus an AI-agent "defense loop" that catches regressions, triages alerts, and traces issues across client and server down to the offending code diff — often before the problem reaches production. Claimed result: preview playback failures improved by 88%. (from abstract only)
- **How**: Agents close the loop from alert → triage → cross-stack (client + server) trace → diff-level attribution, layered on top of full-stack reliability engineering; the loop runs continuously rather than on human dispatch.
- **Where applicable**: The product domain (media preview playback in Edits) is Meta-specific, but the mechanism — automated regression detection with cross-layer attribution to a specific code change — transfers to any system with good alerting and versioned code. The 88% figure is for this one product surface.

## Adjacent

### Chasing a Moving Target: Going AI-Native on Edits' Video Seek Engine

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-8)

Boris Baracaldo (Meta)

- **Why**: A well-described systems problem (video seek/scrub under continuous interrupting requests and mobile device limits) with a 10x measured improvement, plus a forward-looking "AI-native" refactor — a useful case study in engineering systems so coding and observability agents can extend them.
- **What**: An engine for serving frames during video scrubbing in Edits: handling a continuous stream of seek requests, abandoning stale work mid-flight, GOP-aware seeking off a keyframe list, finger tracking on backward scrubs while decode runs forward, and precision-for-speed trades where users can't perceive the difference. Delivered 10x improvement in seek latency and frames shown per second. The team is now refactoring toward portability and "agentic just-in-time observability," agent skills for extending the engine, and a vision of agents profiling production data and generating/experimenting with algorithmic variations. (from abstract only)
- **How**: Request-shaped adaptive behavior rather than any fixed seek policy — each scrub's speed, direction, and composition shape resolves keyframe distance, frame selection, and work-abandonment decisions differently.
- **Where applicable**: The engine is Edits/Meta-specific and mobile-constrained; the seek mechanics are general video engineering. The agentic layer is largely a stated vision rather than a validated result — treat it as direction, not a substantiated finding.

### ML Video Codec (MLVC): Research to Product

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-21)

Nabakumar Khongbantabam (Microsoft)

- **Why**: A rare research-to-product report for learned video compression in a mainstream product (Teams). The tradeoff map — latency, compute cost, hardware acceleration, compatibility, quality measurement — is the same one anyone faces shipping ML into an existing heterogeneous client fleet.
- **What**: The product and engineering considerations behind developing and scaling ML Video Codec (MLVC) in Microsoft Teams, and what it takes to turn a promising compression model into durable product impact. (from abstract only)
- **How**: Not detailed in the abstract; the framing centers on navigating tradeoffs between quality gains and the operational costs of ML codecs across diverse devices and network conditions.
- **Where applicable**: Microsoft Teams production environment; heavily dependent on device heterogeneity, hardware availability for inference, and codec compatibility constraints. Not an infrastructure talk — the transferable value is the decision framework, not the codec itself.

### Adopting AV1 for Real-Time Communication (RTC) at Scale

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-5) · [Materials](https://atscaleconference.com/adopting-av1-for-real-time-communication-rtc-at-scale/)

Yu-Chen (Eric) Sun (Meta)

- **Why**: A multi-year fleet-wide codec adoption story — codec selection, device eligibility, rate control, error resilience — structurally similar to rolling out any new technology across a heterogeneous fleet (new transport, new silicon, new protocol). The operational lessons (eligibility gating, gradual coverage expansion) transfer well.
- **What**: Meta's multi-year effort adopting AV1 for real-time communication: the technical and operational challenges of deploying AV1 and expanding coverage, and several technologies for improving AV1 call quality, including rate control and error resilience. (from abstract only)
- **How**: Not detailed in the abstract; a companion engineering blog post ("Adopting AV1 for real-time communication at Meta") is linked from the session and is the better source for mechanics.
- **Where applicable**: Meta's RTC fleet. AV1 deployment is gated by hardware decode coverage across the device fleet — silicon- and device-tier-dependent — so eligibility policy is as much of the story as the codec itself. The staged-rollout playbook generalizes to other fleet-wide technology migrations.

### Flywheel of Media Models & Product Velocity

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-16) · [Materials](https://atscaleconference.com/flywheel-of-ai-media-models-and-product-velocity/)

Rushaan Mahajan (Meta)

- **Why**: Once AI media models cross the photorealism threshold, evaluation — not generation — becomes the bottleneck. This talk is about VLM-based "Visual Judges" as evaluation infrastructure, an emerging pattern relevant to anyone building perceptual-quality gates for generative systems.
- **What**: The argument that log files and traditional metrics (which solved LLM evaluation) break for visual media — a pipeline can have zero software errors and flawless prompt adherence yet fail perceptually (bad camera crop, stuttering motion, plastic skin). The work puts VLM-powered Visual Judges into the stack to drive a flywheel that accelerates media products. (from abstract only)
- **How**: Perceptual quality assessment via visual-language models acting as automated judges, feeding product and user signals back into model-recipe iteration.
- **Where applicable**: Meta's media-generation products. The VLM-as-judge pattern is broadly applicable wherever perceptual or subjective quality needs an automated gate; the specific judge training and calibration details are Meta's.

### Beyond “Good Enough”: How deployments accelerate research at the Audio AI Frontier

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-30)

Shaheen Lavie-Rouse (ElevenLabs)

- **Why**: A crisp instance of the "benchmarks saturated, now what" problem: when word error rate stops discriminating, production deployments become the research signal. The concrete finding — a voice-identity vs. native-sounding tradeoff in dubbing — is a good example of deployment-driven research.
- **What**: ElevenLabs' learning loop across research, product, and forward-deployed engineering, aiming past WER at "emotional intelligence and taste." Their Reels dubbing work surfaced a trade-off between preserving the original speaker's voice and sounding native in the target language, and produced a new cloning-strength control to manage it. (from abstract only)
- **How**: Deployment telemetry and forward-deployed engineering feedback directly parameterized a user-facing model control (cloning strength) rather than a new benchmark.
- **Where applicable**: ElevenLabs' dubbing product; the specific tradeoff is audio-translation-specific, but the research-loop pattern (deployments reveal the next objective function) is general.

### Content Accessibility at Scale: AI Voice Translations at Meta

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-29) · [Materials](https://atscaleconference.com/learn-more-the-research-behind-ai-voice-translations-at-meta/)

Esra Cansizoglu (Meta)

- **Why**: The inference-side claims are what make this worth a look: streaming speech translation that improves accuracy *and* latency simultaneously (usually a tradeoff), plus a retrieval-side solution to cold start for dubbed content distribution.
- **What**: How Meta produces and distributes AI voice-translated Reels at scale — the streaming translation approach and the retrieval-side exploration that solves cold start so a dubbed render actually finds its audience. (from abstract only)
- **How**: Not detailed in the abstract; a linked featured article ("the research behind AI voice translations at Meta") carries the methodology.
- **Where applicable**: Meta Reels distribution; the streaming-inference and cold-start-retrieval patterns are relevant to any latency-sensitive serving system with a content-distribution front end.

### Rhythm - Anticipatory Intelligence for Organizations

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-24) · [Materials](https://atscaleconference.com/rhythm-ai-building-anticipatory-intelligence-without-breaking-information-boundaries/)

Sundararajan Subramanian (Meta)

- **Why**: Signals where enterprise AI is heading — anticipatory/predictive intelligence inside an organization — and the abstract is entirely absent, so this is a directory entry more than a digest pick; included because the companion featured article ("Rhythm AI: Building Anticipatory Intelligence Without Breaking Information Boundaries", authored by a Meta team including Jubin Chheda) suggests a substantive treatment of the hard constraint: doing this without violating information boundaries.
- **What**: No abstract published; title and materials only. (from abstract only)
- **How**: Unknown from the program; the featured article is the only substantive source.
- **Where applicable**: Unknown; treat as a pointer to the linked article rather than a talk with published content.

## Wildcard

### Fireside Chat: Designing for the Agentic Era

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-26)

Michael Martinez (Meta), Alex Cornell (Meta)

- **Why**: Not an infra talk, but it poses the question every product org building agents is now facing: when AI shifts from assistant to agent — acting rather than answering — what does design even mean, and is one product for everybody still coherent? Useful pattern-recognition for anyone PM'ing agentic systems.
- **What**: A conversation tracing Meta's Muse from inspiration to mainstream: what it took to make an agent feel universal, the use cases nobody predicted, and what happens when users control the experience. (from abstract only)
- **How**: N/A — fireside format; expect product-design reasoning rather than engineering results.
- **Where applicable**: Meta's Muse agent; conceptual rather than technical, but the assistant-to-agent design shift it describes is cross-industry.

### Live Panel: AI Generated Media Provenance at Scale

**Links:** [Abstract](https://atscaleconference.com/events/product-2026/#agenda-item-19)

Steve Dilla (Meta), Mohit Diwan (Meta), Sai Chandramouli (Meta), Karthic Veera (Meta), Alexandre Mourachko (Meta)

- **Why**: Provenance for AI-generated media is an emerging infrastructure problem — cryptographically signed content credentials at platform scale — and this panel gathers the product, Trust & Safety, AI Privacy, and FAIR perspectives in one place. Not a core-infra fit, but a subfield that will matter to anyone operating large AI content pipelines.
- **What**: No abstract published; participants and format only — a moderated panel (Dilla moderating; Diwan, Chandramouli, Veera, Mourachko as panelists) on establishing provenance for AI-generated media at scale. (from abstract only)
- **How**: Unknown from the program; panel format, no published methodology.
- **Where applicable**: Meta's platforms and policy environment; the underlying problem (credentialing AI-generated content end-to-end across creation, distribution, and display) is ecosystem-wide.

## Themes

- **Agentic operations loops with measured outcomes.** Wally (30% test success, millions saved), the Edits defense loop (88% failure reduction), and the always-on maintenance talk all describe agents moving from writing code to *operating* the discovery-triage-fix loop itself — with humans kept on consequential decisions. This is the event's strongest signal: the ops loop, not the code, is becoming the unit of automation.
- **AI validating AI.** The JiT Catching Test system and the defense loop both put AI on both sides of the quality gate — generating the failures and filtering which ones matter. The ship path is being rebuilt around agents, and the LLM-assessor-as-filter pattern (machine volume, human attention) recurs across talks.
- **Evaluation is the new bottleneck.** Once benchmarks saturate — WER for audio, resolution/prompt-adherence for video — the frontier moves to perceptual evaluation: VLM judges for visual quality, "taste" for audio. Expect evaluation infrastructure to be where the differentiation is claimed.
- **Deployments as the research driver.** ElevenLabs and Meta's voice-translation and media-model flywheel talks share a thesis: production feedback now reveals objectives and tradeoffs (cloning strength, cold start) faster than offline benchmarks, closing research-to-product into a loop.
- **Classic systems constraints still gate ML shipping.** MLVC and the AV1 RTC talk are both, at bottom, fleet-adoption stories: device eligibility, hardware acceleration coverage, latency, and compute cost dominate the research-to-product gap — a familiar shape to anyone who has rolled out new silicon or protocols.
- **Zero networking/cloud/K8s content here — by design.** This event's scope is product and media engineering; @Scale's Networking and Systems & Reliability 2026 events (August and June respectively) are where the PM's core infrastructure interests are served this cycle. This digest is worth a skim for the agentic-ops patterns, not for the core stack.
