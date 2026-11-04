<!--
conference: CfgMgmtCamp Ghent 2026
type: vendor
source_url: https://cfp.cfgmgmtcamp.be/ghent2026/schedule/export/schedule.json
generated: 2026-11-04
registry_key: cfgmgmtcamp-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# CfgMgmtCamp Ghent 2026

CfgMgmtCamp is a configuration-management / infrastructure-automation community conference, not a networking conference — so the network content below is the fraction of the program that speaks directly to network automation, cloud-native networking, and network security. Of the 15 pre-selected items, 14 made the cut; the embedded-init talk (crinit) was passed over as too niche for your focus. Note on sourcing: talk pages only repeat the abstract plus speaker bios (several also list slides the pipeline did not extract), so every write-up below is grounded in the abstract and speaker affiliation only — treat the "How" sections as the speakers' stated approach, not verified results.

## Core

### Automating Config Deployment with NetBox

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/RLFAJQ/)

Christopher Rössler, network engineer at the Berlin Commercial Internet Exchange (BCIX)

- **Why**: A real, production network-automation story from an Internet Exchange — exactly the physical-networking source-of-truth problem (scattered data across IXP Manager, NetBox, and running configs) that anyone running switch fabrics faces. No vendor pitch; this is an operator describing how they closed the loop from intended-state database to deployed switch config.
- **What**: BCIX's journey from hand-written switch configurations to a mostly automated pipeline centered on NetBox as the single source of truth, plus how that foundation now also drives maintenance prep and peering-platform announcements (from abstract only).
- **How**: A four-step pipeline: collect/normalize data into NetBox with Ansible; generate configs from Jinja2 templates; diff and validate actual vs. intended configuration; deploy to switches. The interesting part is reconciling IXP Manager (INEX's IXP operations platform) with NetBox so both agree with what's actually on the boxes.
- **Where applicable**: IX/peering-specific in its tooling (IXP Manager), but the pattern — consolidate sources of truth, generate, diff, deploy — is broadly applicable to any multi-tool network environment. Worth watching for how they handle intended-vs-actual drift detection in a fabric where consistency errors cause real outages.

### Inspecting your Kubernetes cluster with eBPF and Inspektor Gadget

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/FSWFQB/)

Soham Chakraborty, SRE at Sematext

- **Why**: eBPF-based in-cluster observability sits squarely in your cloud-native networking space: seeing TCP connections per pod, DNS requests, and syscall-level behavior in real time is the debugging layer under Cilium-style networking. Inspektor Gadget is the CNCF toolkit that makes eBPF debugging approachable without writing your own programs.
- **What**: A practical walkthrough of using Inspektor Gadget's gadget suite for real-time, in-cluster debugging — TCP connections by pod, DNS requests, syscalls, and traceloop, a syscall flight recorder for post-incident root-cause analysis (from abstract only).
- **How**: Inspektor Gadget dynamically instruments the Linux kernel with eBPF — no agent installation required — and the talk covers capturing gadget output in a parseable format for later analysis rather than staring at raw bpftrace-style output.
- **Where applicable**: General technique for any Kubernetes environment on modern kernels; the speaker is a Sematext SRE, so expect an practitioner's framing rather than a project-maintainer internals talk, and the eBPF intro portion will be 101 if you already live in this space. The flight-recorder (traceloop) pattern for intermittent network issues is the transferable idea.

### Reliable Network Backups & Restore with Ansible: Idempotent, Vendor-Neutral, — with AI/ML Diff Severity

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/8NZDMV/) · [Slides](https://cfp.cfgmgmtcamp.org/media/ghent2026/submissions/8NZDMV/resources/Cfgmgmtslides_sRktB6U.pdf) · [Recording](https://www.youtube.com/watch?v=0ke0l6_FFGo)

Rohit Thakur, Principal Engineer, Ansible Networking (Red Hat)

- **Why**: Network backup/restore is unglamorous but critical network-automation plumbing, and this goes deep into the operational pitfalls (device-native paths, transfer methods, idempotency across IOS/IOS-XR/NX-OS) that matter if you run Cisco gear. Caveat: the speaker is the Red Hat Ansible Networking content lead, so this is contributor-led but also adjacent to product marketing for Ansible Validated Content — evaluate the patterns, not the pitch.
- **What**: A battle-tested backup/restore workflow for Cisco IOS/IOS-XR/NX-OS with Ansible, plus a lightweight rules/ML approach to score the severity of config diffs (VLAN, ACL, BGP, interface changes) so review and rollback can be prioritized by risk (from abstract only).
- **How**: Concrete mechanics: absolute on-device paths (`bootflash:/`, `disk0:`, `/misc/config`) because network OSes don't expand `~`; SFTP/SCP via internal file servers; canonicalizing configs and SHA-256 hashing so backups only write on change; a single role interface across the three Cisco OSes; restore as stage → replace/merge → post-verify by hash. Diff severity uses feature extraction plus rules, with optional scikit-learn, running offline — no cloud dependency.
- **Where applicable**: Cisco-heavy estates specifically (the path and OS details are vendor-specific by design), but the idempotent-backup, hash-verified-restore, and diff-risk-ranking patterns are broadly applicable. The ML severity scoring is the speculative part — expect rules to do most of the work — but the idea of ranking network config diffs by blast radius is worth stealing.

### Modern Network Observability

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/GQYAVR/)

Christian Adell, Staff Network Developer at CoreWeave, co-author of *Modern Network Observability* (Packt)

- **Why**: Four-hour hands-on workshop on modern network telemetry — gNMI/streaming telemetry through to event-driven automation — taught by someone who builds large-scale network automation at CoreWeave, i.e., at GPU-cloud DC scale. This is the most directly relevant item in the whole program to physical/network telemetry work.
- **What**: Building a complete open-source network observability stack from scratch: collection and normalization (Telegraf), streaming storage (Prometheus), contextual dashboards (Grafana correlating metrics, traces, and topology), and event-driven pipelines (Kafka/NATS/webhooks) that trigger network automation from telemetry (from abstract only).
- **How**: Lab-based on Containerlab with Python >3.10 and Docker locally (or a DigitalOcean playbook), moving from raw gNMI/streaming telemetry to modeled, correlated, and reactive telemetry integrated into CI/CD and automation workflows.
- **Where applicable**: Broadly applicable — vendor-neutral, open-source stack on containerized lab topology. The event-driven automation angle (telemetry → Kafka/NATS → automated action) is the piece most programs skip and is directly relevant to DC fabric operations. Budget the full morning; it's a workshop, not a talk.

## Adjacent

### Overengineering my personal infrastructure with NixOS

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/A88MRQ/)

Lander Van den Bulcke, Open Source consultant at Inuits

- **Why**: Homelab-scale, but the networking content is real: WireGuard and GENEVE tunnels, Bird BGP peering into DN42, and fully declarative config for it all. DN42 is one of the few places to run experimental BGP outside production, and this is a worked example of the whole stack under Nix.
- **What**: A tour of a personal NixOS infrastructure: remote hypervisor install (nixos-anywhere), SSH-based remote disk unlock in initrd, impermanence with ephemeral root, VM management via microvm.nix, tunnel and BGP setup, and automated nameserver/Prometheus configuration (from abstract only).
- **How**: Everything as Nix declarations — microvm.nix for VMs, declarative WireGuard/GENEVE tunnels, Bird configured for DN42 peering, with monitoring automated end to end.
- **Where applicable**: Personal/lab scale — the ideas (impermanence, declarative tunnel/BGP config, nixos-anywhere provisioning) transfer to production NixOS estates, and DN42 itself is a general-purpose BGP playground anyone can join. Not a production case study; treat as techniques, not results.

### Beyond SHA Pinning: Security for CI/CD Pipelines

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/E9ANZ8/) · [Slides](https://cfp.cfgmgmtcamp.org/media/ghent2026/submissions/E9ANZ8/resources/Beyond_SHA_Pinning__Security_for_CI_CD_Pipelines__a7Smty9.pdf)

Andoni Alonso (Prowler) and Paco Sanchez

- **Why**: Pipeline supply-chain security is adjacent to your network-security remit but highly relevant to infrastructure-as-code hygiene: pipelines hold the credentials that touch your network configs, and the `tj-actions` incident is the recent case study.
- **What**: Practical strategies for securing CI/CD pipelines against supply-chain attacks — moving past SHA-pinning actions to attack vectors like repository misconfigurations that yield RCE just from someone opening a pull request (from abstract only).
- **How**: Threat-modeling the pipeline as a privileged component (code, infrastructure, secrets access), with actionable hardening steps against both common and lesser-known vectors.
- **Where applicable**: General, tool-agnostic security practices; speaker is from Prowler (cloud security vendor), so expect some product-adjacent framing, but the `tj-actions`-era attack surface discussion is timely regardless of tooling.

### OpenTelemetry Tracing, not just for webapps

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/88YNP8/)

Pieter Lexis, Senior Developer at PowerDNS

- **Why**: Contributor-led internals talk from a PowerDNS developer: how they added OpenTelemetry tracing to a DNS server *without* the OTel C++ SDK, and how trace context is propagated to downstream resolvers via DNS. If you care about DNS operations or about making non-HTTP infrastructure observable, this is a rare detailed treatment.
- **What**: The story of adding basic tracing support to PowerDNS, passing trace information to downstream servers via DNS, and visualizing the result in Jaeger — with explicit discussion of the protocol and code workarounds required (from abstract only).
- **How**: Custom (SDK-free) OTel instrumentation inside PowerDNS, trace-context propagation through DNS itself, and the "code and protocol hijinks" that skipping the official C++ SDK entailed.
- **Where applicable**: DNS-heavy environments generally; the implementation is PowerDNS-specific but the pattern — propagating trace context through a request-routing protocol rather than HTTP headers — is a transferable idea for any layered network service. This is one of the few talks here with genuine engineering detail promised.

### Static vs. Dynamic Secrets: What Are We Really Talking About?

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/RRDMZZ/)

Leon Krass, Technical Leader for HashiCorp Vault at SVA System Vertrieb Alexander GmbH

- **Why**: Secret lifecycle sits next to your identity/workload-identity interests — dynamic, short-lived credentials are the same philosophical ground as SPIFFE-style workload identity, and OpenBao (the open-source Vault fork) is where that ecosystem is heading post-license-change.
- **What**: A definitional and operational deep-dive into what actually counts as a secret, and the static vs. dynamic distinction — whether it's technical, operational, or philosophical — with a live demo of provisioning and rotation behavior (from abstract only).
- **How**: Live demo stack: OpenBao, Keycloak, PostgreSQL, OpenSSH — showing how secrets are provisioned and rotated in practice and what that implies for security and operations.
- **Where applicable**: General conceptual grounding, vendor-neutral in tools (OpenBao rather than Vault proper is itself a signal). More of a clarifying/terminology talk than a novel-technique talk; useful for calibrating how your org talks about secrets, not for new architecture.

### Crowdsec and Mikrotik integration

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/XBH3UZ/)

Michal Sochon (independent; platform/DevOps background)

- **Why**: Network security at the router: using a MikroTik as a CrowdSec enforcement point (bouncer). It's a small community fork, but the speaker promises real resource-cost numbers and usage graphs — the kind of end-user data most security talks lack.
- **What**: The story of forking and integrating cs-mikrotik-bouncer-alt: why it was forked, pros and cons, how much the solution costs in resources on the router, and real usage graphs from a working system (from abstract only).
- **How**: CrowdSec (distributed fail2ban-style detection across hosts) signals the MikroTik router to block via a community-maintained bouncer, extending mitigation beyond nginx/nftables/Kubernetes options into edge-router firewalling.
- **Where applicable**: Small/SMB and homelab-adjacent scale — MikroTik RouterOS specifically, explicitly unofficial (not affiliated with CrowdSec or MikroTik, "use at your own risk"). The detection-to-enforcement feedback loop pattern is general; the implementation is niche. Come for the resource-consumption numbers, not the roadmap.

### The Day Two Problem: Examining Decades of Infrastructure Automation Evolution

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/LLCCHN/) · [Recording](https://www.youtube.com/watch?v=WUanIbx8HE0)

Yair Etziony, Engineering Manager at AMBOSS

- **Why**: A strategic/historical framing of why every generation of automation tooling (Puppet → Chef → Ansible → Terraform → Pulumi → Crossplane) hits the same post-deployment wall — directly relevant to how you position network lifecycle management versus one-shot provisioning.
- **What**: A historical analysis of the recurring Day-Two blind spots across tool generations: drift correction, decommissioning, mystery infrastructure, and the persistent disconnect between automation state and observability, argued from 30 years of systems experience (from abstract only).
- **How**: Comparative analysis across tooling generations — how each handles state management vs. distributed coordination, and what treating infrastructure as dynamic systems rather than static code would imply.
- **Where applicable**: General industry analysis, no specific stack; it's a perspective talk rather than a technique talk, so its value is in framing (especially the automation/observability separation argument, which network teams feel acutely) rather than actionable mechanics.

## Wildcard

### We Built for Predictability; the Workloads Didn't Care

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/AGSYJ3/) · [Recording](https://www.youtube.com/watch?v=pq3Qxb26Nwo)

Michael Stahnke, VP of Engineering at Flox (previously CircleCI and Puppet leadership)

- **Why**: Not networking, but it names a fault line that will run through DC and network operations: AI/agentic workloads are probabilistic, and config-management-era guarantees (determinism, no drift, reproducible environments) don't transfer to the application layer. For anyone whose products promise predictable infrastructure, this reframes what you're actually selling.
- **What**: An argument that infrastructure's predictability model doesn't fail but is simply insufficient for probabilistic workloads — a perfectly reproducible environment can still behave differently run to run — and a framework for deciding what must stay deterministic versus where randomness is safe (from abstract only).
- **How**: Conceptual/operational reasoning rather than a mechanism: partitioning systems into deterministic foundations and probabilistic workloads, and adapting troubleshooting and reliability practices for "it depends" outcomes.
- **Where applicable**: General and early — this is a mental-model talk, not a tool or result. Relevant as strategic input to product thinking about AI-era infrastructure requirements.

### AI Native Infrastructure Automation: how I learned to stop worrying and love Claude

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/UGTUYH/)

Adam Jacob, CEO and co-founder of System Initiative, original author of Chef

- **Why**: Adam Jacob's talks reliably set the discourse for the automation community (Chef did for a decade), and this is the most direct signal at this conference of where agentic infrastructure automation is heading — squarely relevant to your agentic-identity interest, since agents that operate infrastructure need exactly the credentials and identity story you work on.
- **What**: How building an AI agent transformed System Initiative's product from the top down, with a promise to go deep on how and why it works, and what it means for infrastructure automation as a discipline (from abstract only).
- **How**: Not disclosed in the abstract beyond "AI-native" architecture at System Initiative; expect agent-driven automation mechanics and their operational implications.
- **Where applicable**: Vendor-founder keynote — System Initiative-specific by construction, with the usual founder framing (the abstract spends its first half preempting skepticism). Worth attending for direction, not for adoptable technique; read it as a leading indicator of agentic infra tooling, including its unsolved identity/authorization problems.

### Reactive Nix: Enabling Functional Reactive Configuration with mgmt

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/LCHTBT/) · [Slides](https://cfp.cfgmgmtcamp.org/media/ghent2026/submissions/LCHTBT/resources/slides_lHsfAcV.pdf)

Jannik Höfler, DevOps Engineer at Dev Specialists GmbH

- **Why**: A genuinely novel configuration-management idea: Nix evaluates to a static snapshot of desired state, and this work asks what happens if configuration is a *function over time* instead. It's a new point in the declarative/reactive design space, from the mgmt (functional reactive configuration management) ecosystem.
- **What**: The rx.nix (Reactive Nix) project — combining Nix's purely functional configuration model with mgmt's FRP runtime so systems stay declarative and reproducible yet react continuously to environmental change, instead of being frozen between builds (from abstract only).
- **How**: Nix models `system = f(configuration)` — a fixed value per build. FRP generalizes to `system(t) = f(configuration, environment(t))`: the config stays pure but depends on signals that evolve continuously; mgmt's runtime observes, reacts, and converges to declared state without re-evaluation.
- **Where applicable**: Research/frontier territory rather than production tooling — an exploration of what continuous convergence would mean for NixOS-style systems. Most interesting as a conceptual reframing of drift: instead of re-running to correct drift, the configuration itself is time-aware.

### Watch paint dry - Monitoring what doesn't change

**Links:** [Abstract](https://cfp.cfgmgmtcamp.org/ghent2026/talk/78VKZV/)

Ole Herman Schumacher Elgesem, Northern.tech (the company behind CFEngine and Mender)

- **Why**: A clever inversion of monitoring: alert on *changes to things that should never change* — DNS records, released-software checksums, tag commit SHAs, admin counts, unsigned commits — as a lightweight compromise-detection tripwire. It's a new open-source tool launch with a genuinely simple, transferable idea.
- **What**: The concept and open-source implementation (PostgreSQL-backed, modular) of monitoring invariants: anything whose change is itself the signal, tracked with full history so any change to a monitored variable raises an alert (from abstract only).
- **How**: Modular architecture with a PostgreSQL database tracking history and changes per monitored variable; new check modules are easy to add. Example invariants: number of script tags on your site, checksum of a release, number of org admins, your website's DNS/IP.
- **Where applicable**: Broadly applicable and lightweight — this pattern (change-of-invariant alerts) is orthogonal to, and composable with, existing monitoring, and is directly useful for supply-chain and account-takeover detection. Early-stage project from a talk launch, so expect rough edges.

## Themes

- **Network automation is consolidating around source-of-truth pipelines**: the strongest network content (BCIX/NetBox, Ansible backups, the observability workshop) all share one shape — a canonical data model (NetBox, Prometheus, validated content), generated config, and closed-loop verify/diff against reality. The interesting frontier is what happens *after* deployment (drift, diff severity, restore safety).
- **Telemetry as an automation input, not just a dashboard**: gNMI/streaming telemetry feeding event-driven automation (Kafka/NATS/webhooks → action) is being pitched as the standard next step for network ops, led by practitioners at hyperscale-adjacent operators (CoreWeave).
- **eBPF observability is now table stakes for Kubernetes debugging**: the Inspektor Gadget talk is the cloud-native-networking presence at this conference, and it's framed as practical tooling rather than novel research — a sign of maturity.
- **Supply-chain and CI/CD security is a persistent undercurrent**: SHA pinning, pipeline RCE, checksum-of-release and unsigned-commit monitoring, signed init configs — multiple sessions converge on verifying that what runs is what was intended, which is a short conceptual hop from your signed-workload/identity territory.
- **The AI/probabilistic turn in infrastructure**: two of the biggest-stage talks (Stahnke, Jacob) directly address agentic systems breaking the determinism assumption of config management — a discourse shift the automation community is clearly working through, with agentic-infrastructure identity and authorization still unnamed gaps.
- **Nix's limits as a research topic**: two independent sessions (Reactive Nix, the NixOS personal-infra talk) probe where static Nix evaluation ends — the reproducibility/drift tension that Reactive Nix tries to resolve with FRP is the same tension the Day-Two talk identifies across all tooling generations.
