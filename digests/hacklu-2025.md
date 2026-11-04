<!--
conference: hack.lu 2025
type: security
source_url: https://pretalx.com/hack-lu-2025/schedule/export/schedule.json
generated: 2026-11-04
registry_key: hacklu-2025
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# hack.lu 2025

A 24-item pre-selection from the hack.lu 2025 program, triaged into Core / Adjacent / Wildcard. Note on depth: no extracted paper/slide text was available to this run, and the talk pages I fetched added only speaker bios — so every write-up below is grounded in the (often extended) abstract alone and is marked accordingly. The hands-on Suricata training and the standalone `laravel-crypto-killer` outline fragment were skipped as duplicating selected items; the Canon firmware-crypto talk was dropped as the weakest fit.

## Core

### OverLAPS: Overriding LAPS Logic

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/Y3DGVG/) · [Recording](https://www.youtube.com/watch?v=r-vsdcoFP2k)

Antoine Goichot (PwC Luxembourg)

- **Why**: LAPS is the mechanism most enterprises rely on to eliminate shared local-admin credentials across AD/Entra fleets. All prior research attacked it from the directory side; this flips to the endpoint, where the password actually lives — directly relevant to identity and endpoint posture.
- **What**: Client-side attacks against Windows LAPS ("LAPSv2") that let an attacker capture, manipulate, and rotate the local admin password on demand, using LAPS as a persistence mechanism on both on-prem and Entra-joined devices — a genuinely new angle, and by the same researcher who did the original 2017 LAPS abuse work. (from abstract only)
- **How**: PDB symbols plus light static analysis to understand LAPS internals; Frida dynamic hooking to intercept and control the password lifecycle; PoCs reproduced with Microsoft Detours for in-process hooks.
- **Where applicable**: Any Windows fleet running Windows LAPS or legacy LAPS; requires attacker code execution on the endpoint (a client-side precondition, not a directory compromise). General technique, not org-specific.

### Nightmare on NTLM street: Legacy’s Revenge

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/7KCT7N/) · [Recording](https://www.youtube.com/watch?v=jywvoot4bMs)

Marina Bochenkova

- **Why**: Microsoft announced NTLM family deprecation in June 2024; every identity and infrastructure team will live through this migration. This is a field report of actually doing it, not a deprecation-recap.
- **What**: A retrospective of disabling NTLM in a mid-sized enterprise — why it survives 24 years past its replacement (application development lag, flaws in the replacement paths, decision-making, underfunded IT), plus resources and lessons learned for completing the removal elsewhere. (from abstract only)
- **How**: Deployment methodology rather than exploitation: dependency discovery, organizational blockers, and remediation strategy for phasing out NTLM (and similar legacy protocols).
- **Where applicable**: Enterprise AD environments broadly; the case study is one mid-sized enterprise (org-specific experience), but the dependency classes it documents are general.

### Red Team Story: Offline SCCM backup secrets decryption

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/7FRGDY/) · [Recording](https://www.youtube.com/watch?v=ZcMEY47npX0)

Martino

- **Why**: SCCM/MECM is high-value, AD-integrated infrastructure, and its backups — often sitting readable on network shares — carry encrypted secrets. This is a common real-world exposure with no complete public walkthrough until now.
- **What**: The first concrete, end-to-end offline decryption of SCCM backup secrets with no access to a live SCCM server: the exact artifacts required, the encryption scheme, and a released script to reproduce the workflow. (from abstract only)
- **How**: Explanation of how SCCM backup-secret encryption works, which artifacts must be collected from a backup, and a step-by-step decryption workflow, demonstrated against the public GOAD SCCM lab.
- **Where applicable**: On-prem SCCM deployments where backup files are readable (network shares or other exposed locations); requires only read access to the backup artifacts. Vendor-specific to Microsoft SCCM.

### What's New in Suricata 8: Enhanced Detection and Performance

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/7NJXCF/) · [Recording](https://www.youtube.com/watch?v=NwWZBc1CFbM)

Eric Leblond, Peter Manev (OISF / Stamus Networks)

- **Why**: Suricata underpins a large share of open and commercial NDR deployments. Suricata 8's protocol expansion — notably DNS over HTTPS and LDAP — speaks directly to keeping wire visibility as DNS and directory traffic go encrypted.
- **What**: Release overview: new protocol parsers (LDAP, DNS over HTTPS, SIP, SDP, POP3, WebSocket), "transactional rules" that match traffic in both directions with a single signature, 100+ new keywords (entropy matching, domain transform, datasets with JSON context, ENIP, full DNS field matching, enhanced SMTP/EMAIL/FTP), plus performance/security work: vendoring and sandboxed Lua by default and the HTTP parser implemented in Rust. (from abstract only)
- **How**: Feature walkthrough with detection-engineering framing; a companion hands-on training at the conference covers the same features with malware PCAP traces.
- **Where applicable**: General NDR/IDS deployments — broadly applicable. The DoH and full-DNS-field parsing matters wherever recursive-to-DoH migration has blinded classic DNS monitoring.

### Palo Alto GlobalProtect : Remote Full Compromise Exploit Chain

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/XDHVWE/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/XDHVWE/resources/RemoteFullCo_bOdlp55.pptx) · [Recording](https://www.youtube.com/watch?v=3lQ5gxKTmw4)

Maxime Escourbiac (Michelin CERT)

- **Why**: The VPN client is the trust anchor of enterprise remote access. A same-network attacker achieving RCE and SYSTEM on Windows via the client is a realistic rogue-AP/hotel scenario, and the chain runs through broken certificate verification and root CA management — core PKI trust problems.
- **What**: Six CVEs in the Palo Alto GlobalProtect client (CVE-2024-5921, CVE-2025-0117, CVE-2025-0118, CVE-2025-0120, CVE-2025-0131, CVE-2025-2183) chained to full remote compromise: certificate-verification bypass to impersonate the VPN portal, arbitrary root CA insertion, HTA payload delivery through the embedded authentication browser for RCE, and privilege escalation to SYSTEM via the impersonation mechanism or weak system update. (from abstract only)
- **How**: Systematic weaknesses in certificate verification, root CA management, embedded-browser authentication, and client-server communications; the talk walks each step toward a full chain.
- **Where applicable**: Windows workstations running the GlobalProtect client; the attacker must be on the same network as the victim (not internet-remote). Vendor-specific to Palo Alto.

### No way to enable SSH access to your new router? The vendor might have something to hide

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/BDUTYD/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/BDUTYD/resources/dashevskyi_20_Uo4kCmD.pdf) · [Recording](https://www.youtube.com/watch?v=-ek5znxcMb0)

Stanislav Dashevskyi, Francesco La Spina (Forescout / Vedere Labs)

- **Why**: A rare documented case of a network-device vendor actively obstructing analysis — patched Lua compiler, hidden SSH backdoor — in OpenWrt-derived firmware, a class that spans much of the consumer and enterprise gear in real networks.
- **What**: Reverse engineering of a major (redacted) vendor's OpenWrt-based device OS: the vendor patched the Lua compiler solely to hinder static analysis; a "patched" backdoor survives in the restricted SSH service; and an authenticated OS command injection sits deep in a custom Lua module — together enabling full remote takeover of the device line. (from abstract only)
- **How**: Static and dynamic RE of OpenWrt-derived binaries, recovering the modified Lua compiler's behavior, and auditing the restricted SSH implementation and custom Lua modules.
- **Where applicable**: One vendor's device line (vendor-specific; name redacted in the program). The command injection requires valid credentials; the findings signal a broader audit need for proprietary firmware built on OpenWrt.

## Adjacent

### Silent Killers: Unmasking a Large-Scale Legacy Driver Exploitation Campaign

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/QSWNWS/) · [Recording](https://www.youtube.com/watch?v=PgowsteTZ7M)

Jiří Vinopal (Check Point Research)

- **Why**: A measured, large-scale proof that hash-based and allowlist-based driver defenses (including Microsoft's Vulnerable Driver Blocklist) can be defeated at industrial scale — important context for any endpoint defense stack.
- **What**: A 2025 campaign using 2,500+ uniquely modified but still validly-signed variants of Truesight.sys v2.0.2 (the RogueKiller anti-rootkit driver) to kill EDR/AV. Version 2.0.2 was chosen specifically because it retains the vulnerability while falling below the Microsoft blocklist's and LOLDrivers' coverage; PE structure was manipulated to change hashes while preserving the signature. ~75% of victims are in China, remainder in other parts of Asia; MSRC updated the blocklist on Dec 17, 2024 in response. (from abstract only)
- **How**: Phishing-distributed first-stage loaders (disguised as known applications) exploit a Windows driver-signing policy exception to load the legacy driver, deploy an EDR/AV killer module, and prep the machine for final payloads such as Gh0st RAT variants; C2 hosted in a public cloud's China region.
- **Where applicable**: Windows EDR/AV deployments relying on the driver blocklist; loading the driver requires admin-level execution on the victim (phishing initial access). Vendor-neutral lesson, Windows-specific mechanics.

### LOLBlue : Living Off the Land with Blue Team tools

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/WKQ8EM/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/WKQ8EM/resources/hack.lu-2025-_oNwuzOi.pdf) · [Recording](https://www.youtube.com/watch?v=XDFWsWIATxA)

Maxence Fossat, Antoine C (Synacktiv)

- **Why**: DFIR tools are pre-deployed, privileged readers of memory and protected files — inverting them into offensive LOLBins creates a detection blind spot squarely in the PM's network-security remit.
- **What**: A systematic review of forensic/collection tools (Velociraptor, KAPE, DFIR-ORC and lesser-explored others) repurposed for credential access and covert exfiltration, expanding the known LOLDFIR toolkit, plus detection opportunities and the events to monitor. (from abstract only)
- **How**: Analysis of how each tool accesses low-level filesystem/memory data, including abuse of Velociraptor's client/server architecture, with real-world scenarios demonstrating security-tool bypass.
- **Where applicable**: Any organization that deploys or pre-installs these tools; realistic in late-stage red team engagements after initial execution. General technique.

### Integrating Zeek With Third-Party Applications

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/FEBNLJ/) · [Recording](https://www.youtube.com/watch?v=WVSzEXo1_jE)

Christian Kreibich

- **Why**: Zeek is the other pillar of open NDR; this covers the runtime integration surface that turns it from a log producer into an active component of detection infrastructure.
- **What**: A tour of Zeek's live integration mechanisms — asynchronous intel ingestion, event exchange with custom services, web-API calls from JavaScript, runtime state load/save, and operational telemetry — with real-world applications including ML models, threat-intel platforms like MISP, and round-tripping network inventory data. (from abstract only)
- **How**: Walkthrough of each mechanism with relative pros and cons and example integrations.
- **Where applicable**: Organizations already running (or considering) Zeek; broadly applicable, though the tooling itself is Zeek-specific.

### Attacking The Developer Environment Through Drive-by Localhost Attacks

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/R8FMHK/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/R8FMHK/resources/driveby-1_k2a2Qig.pptx) · [Recording](https://www.youtube.com/watch?v=ZHPlhhINd5o)

Joseph Beeton

- **Why**: Punctures the "bound to loopback = invisible" assumption that underpins how developers run services — relevant to anyone whose engineers run K8s dashboards, dev servers, and tooling locally.
- **What**: JavaScript from any visited website can reach services bound to localhost via non-preflighted HTTP requests; abusing common Spring/Quarkus misconfigurations or newly found vulnerabilities yields RCE on developer machines (Quarkus, older Spring) and exfiltration of AI training models from MLflow. (from abstract only)
- **How**: Compromise a site developers use (or inject JS via ads / phishing to open a page), then cross-origin-request the localhost service; the talk details the browser mechanics, limitations, and what browser vendors are changing to close the class.
- **Where applicable**: Any machine running less-securely-configured local services, especially Java frameworks and MLflow; time-limited — browser vendors are closing this class, but it is live today.

### RomCom exploits Firefox and Windows zero days in the wild

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/V3GFCH/)

Damien Schaeffer

- **Why**: A fully documented, in-the-wild zero-click chain attributed to a Russia-aligned group — a reference-quality case study of browser sandbox escape plus OS privilege escalation.
- **What**: October 2024 discovery of a zero-click chain: a use-after-free in Firefox's animation timeline (code execution in the sandboxed content process, affecting then-current Firefox and Tor Browser) combined with an undocumented permissive Windows RPC endpoint executing code at medium integrity regardless of caller privilege — sandbox escape and EoP, ending in RomCom's backdoor. (from abstract only)
- **How**: Fake website redirects to the exploit server; successful exploitation drops and executes the backdoor with no user interaction. Mozilla patched in ~25 hours, Microsoft in early November; the talk covers RomCom's TTPs, victimology, and both exploits in detail.
- **Where applicable**: Victims were users of then-current Firefox/Tor Browser on Windows; both bugs are patched — the value is as an exploit-chain case study and a capability benchmark for a state-adjacent actor.

### Wyse Management Subversion : Taking over Dell's Wyse Management Suite

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/EB7SPU/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/EB7SPU/resources/2025.10.23-ha_LZLYCQx.pdf) · [Recording](https://www.youtube.com/watch?v=xNY-p8J9oQc)

Alain Mowat

- **Why**: Thin-client management suites are fleet-wide control planes — a server compromise is a fleet takeover — and this research includes a real cross-tenant break in a vendor-operated cloud.
- **What**: Vulnerabilities in Dell's Wyse Management Suite enabling device impersonation (recovering policies for arbitrary devices and decrypting their secrets), full compromise of the WMS server and configured remote repositories, and — in Dell's own cloud — cross-tenant exploitation reaching other tenants' data and assets. (from abstract only)
- **How**: The research began by examining how secrets in policies pushed to thin clients are encrypted; device impersonation flaws plus server-side vulnerabilities chain into fleet-wide control.
- **Where applicable**: Dell WMS on-prem deployments and Dell's multi-tenant cloud environment; vendor-specific, with the cloud findings the most severe.

### From YAML to Root: CI/CD Pipeline Attacks and Countermeasures

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/CGRNFY/) · [Recording](https://www.youtube.com/watch?v=YUbN6MuiuFM)

Hugo

- **Why**: IaC-driven self-service pipelines have widened pipeline access from a few admins to contributors and even external clients — this maps the resulting attack surface for exactly the cloud-native infrastructure the PM's world runs on.
- **What**: A demonstration that a standard contributor account can be escalated to full CI/CD and infrastructure compromise — RCE via pipeline-file manipulation and Terraform constructs (external data sources, custom providers/modules, provisioners), bypasses of provider/module blacklists and step filters, then cloud-credential theft and pipeline persistence — followed by a defensive playbook (secret handling, runner hardening, integrity checks, pipeline log analysis and IoCs). (from abstract only)
- **How**: Chaining misconfigurations and legitimate features in Azure DevOps / GitHub Actions with Terraform and Ansible, under realistic enabled protections.
- **Where applicable**: Organizations running self-service or multi-tenant CI/CD with IaC; broadly applicable to modern pipeline stacks.

### BoD: Bytes Over DNS

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/U3WC88/) · [Recording](https://www.youtube.com/watch?v=eh3BD7v8cZQ)

Didier Stevens

- **Why**: DNS remains the most reliable egress channel, and knowing which public resolvers forward arbitrary bytes changes the calculus for DNS egress policy.
- **What**: Some DNS servers (1.1.1.1 named) accept and forward any byte values inside DNS packets, enabling a C2 channel with higher throughput than hexadecimal encoding, despite label formats being nominally limited to letters/digits/hyphen. Scripts are shared for attendees to test resolvers of their own choosing. (from abstract only)
- **How**: Abusing permissive label handling in DNS implementations that accept more than the LDH character set.
- **Where applicable**: Any environment where clients can reach open recursive resolvers; a short overview-format talk — quick but practical.

### CLI ambush

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/73RXZR/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/73RXZR/resources/hacklu-2025-C_h8IkaqC.pdf) · [Recording](https://www.youtube.com/watch?v=2ogJ6LkvNGw)

William Robinet

- **Why**: The TLS/SSL toolkits administrators run by hand are themselves an attack surface — crafted ASN.1 input trapping the operator is a novel trust-boundary problem at the CLI/PKI layer the PM cares about.
- **What**: A vulnerability class common to various TLS/SSL cryptographic toolkits, triggered by crafted ASN.1 messages, demonstrated in the OpenSSL CLI and extended to other toolkits, with attack vectors that can trap unsuspecting administrators. (from abstract only)
- **How**: Crafting ASN.1 messages that expose handling issues in CLI applications, then walking through the discovered attack vectors.
- **Where applicable**: Any workflow where admins process untrusted cryptographic input (certificates, keys) via OpenSSL-like CLIs; general technique, toolkit-dependent.

### When Netflow meets Pcap - A network forensic approach.

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/ZJTDKJ/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/ZJTDKJ/resources/2025_hacklu_N_z4HAoDs.pdf)

Peter

- **Why**: The central tradeoff of network forensics — netflow scales but drops payload, pcap keeps payload but doesn't — addressed by merging the two; useful for anyone holding large-scale network telemetry.
- **What**: A workshop introducing an approach that merges netflow and pcap data: using the nfdump toolset to prepare and process large pcaps, enriching netflow with third-party information (geolocation, Tor), and searching for network artifacts, with hands-on real-data exercises. (from abstract only)
- **How**: Netflow theory and usage, an nfdump primer, large-pcap processing, enrichment, and artifact hunting.
- **Where applicable**: General network forensics / IR workflows; workshop format requiring basic Linux and command-line skills.

### Building an unmarshelling chain from hydrators

Speakers not listed in the program text (companion outline: "Exploitation by using laravel-crypto-killer")

- **Why**: A reproducible unserialize-to-RCE chain in one of the most-deployed PHP stacks, with a shipping product vulnerable by default, is a concrete at-scale risk worth understanding even outside web-appsec focus.
- **What**: A three-step Livewire (Laravel) chain to remote command execution given the `APP_KEY`: first a phpinfo leak via `FnStream` / `ShardedPrefixPublicUrlGenerator`, then RCE via `SerializableClosure` / `Queueable` / `BroadcastEvent` gadgets, and finally a rebuilt chain reaching a `Terminal`-initiated `exit` so the request completes normally (no error 500) for stealth. The whole process is automated in a new exploit mode of synacktiv's `laravel-crypto-killer`; invoiceninja ships a default `APP_KEY` and is vulnerable by default. (from abstract only)
- **How**: Gadget-chain analysis across GuzzleHttp, League Flysystem, and Laravel framework classes, with payload construction on Livewire's hydration mechanism.
- **Where applicable**: Laravel/Livewire applications where `APP_KEY` is known, leaked, or default; org-agnostic but framework-specific.

## Wildcard

### Instrumenting software builds to detect stealth backdoors and other curiosities

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/UZ87X9/) · [Recording](https://www.youtube.com/watch?v=9vN_I8WbfJg)

Hilko Bengen

- **Why**: Post-xz (CVE-2024-3094), detecting build-time tampering is an open supply-chain problem; this is a concrete attempt at build observability rather than signing/provenance paperwork.
- **What**: A Linux-based prototype toolset that instruments build processes (`./configure && make`, `cargo build`, `pip install`, CI) to generate and analyze lower-level build logs, inferring whether a binary was actually built from the presented sources and detecting abnormal compiler/linker use — with curious findings and limitations discussed. (from abstract only)
- **How**: Instrumentation of what actually happens during builds, then log analysis for source-to-binary correspondence and anomalous toolchain usage.
- **Where applicable**: Linux software builds generally; prototype maturity — a research direction and detection idea, not a deployable control.

### Lethal Language Models: From Bit Flip to RCE in Ollama

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/7MHDPF/) · [Slides](https://pretalx.com/media/hack-lu-2025/submissions/7MHDPF/resources/Lethal_Langua_uliyCuZ.pdf) · [Recording](https://www.youtube.com/watch?v=YjCHGWIGxbU)

Paul Gerste

- **Why**: First-cycle signal: AI inference infrastructure became a Pwn2Own target category in 2025. Every security org will soon own an LLM-runtime attack surface; this is early, systematic evidence of what it looks like.
- **What**: Research on Ollama (widely used for running Llama/DeepSeek-R1 locally) in the Pwn2Own Berlin 2025 context: the architecture, the GGUF model-file format, memory-corruption bugs in its handling, and a deep dive turning a bit-flipping primitive into arbitrary code execution on a vulnerable Ollama instance — ending with a live exploit demo and disclosure notes. (from abstract only)
- **How**: Analysis of how models are serialized to GGUF files and how their parsing yields memory corruption, then exploitation of one bug from bit-flip to full RCE.
- **Where applicable**: Anyone running Ollama with untrusted model files — the notable framing is that model files are a new "untrusted input" channel for memory corruption.

### Revisiting RAND’s Lost Monte Carlo Simulations: Sharla Perrine, Paul Baran, and the True Business Case for the Internet

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/8NMQUJ/) · [Recording](https://www.youtube.com/watch?v=FCdEhYVHvzw)

Trey Darley

- **Why**: The survivability math that justified building the Internet has never been re-run against today's centralized cloud topologies — a sharp question for anyone whose job is DC/WAN topology and resilience.
- **What**: A reintroduction of Sharla Perrine and Paul Baran's early-1960s Monte Carlo simulations (punched cards, octal assembly) that proved a distributed packet-switched network could survive attack — work later used to argue for ARPANET funding — plus a proposal to re-run the simulations under modern assumptions (traffic models, failure modes, time-synchronization shear effects in packet networks) to test whether resilience has quietly rotted as architectures centralized. (from abstract only)
- **How**: Historical reconstruction plus a proposed modern re-simulation using contemporary toolchains, comparing 1960s modeling assumptions with cloud-era reality.
- **Where applicable**: Conceptual / research-stage — a lightning talk proposing a research effort rather than presenting completed results; closer to the PM's core topology interests than a typical wildcard.

### 2038 is gonna be epoch!

**Links:** [Abstract](https://pretalx.com/hack-lu-2025/talk/TLVK3W/) · [Recording](https://www.youtube.com/watch?v=Vv4y4rrYDSM)

Pedro Umbelino, Trey Darley

- **Why**: Y2K38 is a slow-motion systemic event with a hard deadline (19 Jan 2038) and orders of magnitude more fielded systems than Y2K — and attackers don't have to wait for it.
- **What**: Controlled experiments documenting how IoT, ICS/OT, and embedded systems actually behave as they approach and cross the 2038 epoch threshold — failure modes where naively implemented state machines logically reverse time — with a classification framework, and the observation that a resourceful attacker can make "2038" happen any day via clock manipulation. (from abstract only)
- **How**: Exhaustive search and classification of failure modes across device classes in controlled lab environments, presented in plain language for both technical and policy audiences.
- **Where applicable**: Any system relying on 32-bit signed Unix time — especially long-lived embedded and OT equipment that must be pulled from the field, tested, and remediated over the next ~13 years; general, not org-specific.

## Themes

- **The legacy Microsoft identity stack is still the main event**: NTLM removal as a lived project, client-side LAPS abuse, offline SCCM secret decryption — the program keeps finding genuinely new angles in AD/Entra rather than moving past it.
- **Defenders' own tools and trust anchors are the attack surface**: DFIR tools as LOLBins, thousands of validly-signed driver variants killing EDR, a VPN client with broken certificate verification — signature validity and "trusted software" no longer imply safety.
- **Network detection engineering is shipping fast**: Suricata 8's protocol expansion (DoH, LDAP, SIP) and transactional rules, Zeek's integration surface, netflow+pcap merging — NDR tooling racing to preserve wire visibility as protocols encrypt.
- **The network edge is an under-audited endpoint**: OpenWrt-derived router firmware with vendor-hidden backdoors and a full GlobalProtect client compromise chain both treat "the device at the perimeter" as a rich exploitation target, embedded browsers and all.
- **New attacker surfaces being claimed systematically**: AI inference runtimes (Ollama/GGUF at Pwn2Own), self-service CI/CD with IaC, drive-by localhost — each talk documents first serious exploitation of a fresh surface the industry just adopted.
- **Time and resilience as security properties**: Y2K38 fielded-equipment experiments and the proposed rerun of RAND's survivability simulations — long-horizon systemic risks getting evidence-based treatment instead of speculation.
