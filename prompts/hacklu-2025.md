>>> HOW TO RUN THIS <<<
This is the digest prompt for hacklu-2025. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/hacklu-2025.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/hacklu-2025.md
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

Below is the program for hack.lu 2025 (security). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a security program. Judge real-world impact and technical depth.
Up-rank original offensive or defensive research, vulnerability disclosures
backed by proof (working PoC, measured impact), and identity-related work
(Active Directory, cloud IdPs, authentication/authorization, token and session
security). Down-rank awareness/marketing talks and rehashes of known issues.
Note the affected systems and the realistic conditions required to exploit or
mitigate.

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
conference: hack.lu 2025
type: security
source_url: https://pretalx.com/hack-lu-2025/schedule/export/schedule.json
generated: 2026-11-02
registry_key: hacklu-2025
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## 2025-10-21 — Europe

### Hacking - 30+ years ago
Speakers: Walter Belgers
page: https://pretalx.com/hack-lu-2025/talk/93TYFR/
How did computer hacking and the hacking scene look like when the internet was still tiny, 30+ years ago? Since the internet exists, people have been trying to circumvent security. Whereas most people nowadays do so for financial gain, 30+ years ago the world looked different. The internet connected academia. The people hacking were students, almost the only people who had access. Not many system administrators were paying much attention to security and for hackers, breaking into sites such as that of NASA, were ways to gain a reputation. In this presentation, "one of the Dutch hackers" will take a look at the hacking scene in the late 1980s, early 1990s

### Anti-Forensics - You are doing it wrong (Believe me, I'm an IR consultant)
Speakers: Stephan Berger
page: https://pretalx.com/hack-lu-2025/talk/WHX9KY/ | slides: /media/hack-lu-2025/submissions/WHX9KY/resources/HackLu_Anti-F_kIQEIoR.pdf
In this talk, we’ll dissect common anti-forensics strategies—like USN Journal deletion, shellbag clearing, timestamp manipulation, and disabling access time updates—and reveal how they are often executed ineffectively or misunderstood.

We’ll explore practical examples, such as:

- Deleting the USN Journal (fsutil usn deletejournal /d C:) and why it’s rarely a perfect solution.
- Clearing shellbags to wipe file explorer history but failing to account for deeper registry artifacts.
- Time stomping (Get-Item "C:\path\to\file.txt").CreationTime = "2022-01-01 00:00:00) and how forensic tools detect inconsistencies.
- Disabling last access time updates (fsutil behavior set disablelastaccess 1) and its limited effectiveness against comprehensive timeline analysis.
- Wiping MFT free space (sdelete -z C:) while ignoring the traces left behind in unstructured data.

From registry edits like masking user account activity to configuring Windows EFS, we’ll examine why these techniques often fail against modern investigative workflows and how defenders use these “footprints of erasure” to uncover malicious intent.

Attendees will gain a comprehensive understanding of what works and what doesn’t and how to identify these techniques during incident response. Whether you’re an IR consultant, security analyst, or blue teamer, this talk offers actionable knowledge to outsmart adversarial anti-forensics tactics.

We use Python code to show how ‘clean’ evidence cleaning can be done, e.g., if only individual MFT entries are deleted or even if entries in the SRUM database are deleted or manipulated. This means it is not immediately obvious that the data has been manipulated, unlike when everything is deleted. In this talk, we'll dissect common anti-forensics strategies—like USN Journal deletion, shellbag clearing, timestamp manipulation, and disabling access time updates—and reveal how they are often executed ineffectively or misunderstood.

From registry edits like masking user account activity to configuring Windows EFS, we'll examine why these techniques often fail against modern investigative workflows and how defenders use these "footprints of erasure" to uncover malicious intent.

Attendees will gain a comprehensive understanding of what works and what doesn't and how to identify these techniques during incident response. Whether you're an IR consultant, security analyst, or blue teamer, this talk offers actionable knowledge to outsmart adversarial anti-forensics tactics.

### Confessions of a Linux Drama Queen: Incident Response When Hackers Try to Steal Your Spotlight
Speakers: Melina Phillips
page: https://pretalx.com/hack-lu-2025/talk/B3UDM8/
It's one of those mornings. You just crushed your early workout, feeling all kinds of invincible, you're halfway through your first sip of coffee, mentally planning your day, when your SOC team drops a bombshell: Suspicious activity has been detected on a critical system. Suddenly, it's not the caffeine waking you up, it's sheer panic!!

But let’s be real, cyber drama is inevitable. What separates the pros from the panicked is how we respond. In the Linux world, post-compromise activity isn’t just a mess; it’s a story waiting to be told. From tracking suspicious IPs and unexpected file creations to analyzing logs and identifying rogue services, our job is to piece together exactly what happened and how. 

Because let's face it, while trends come and go, resilience never goes out of style. Join me in this session as we turn the chaos into clarity and decode the drama, and maybe even add a little sparkle to incident response. 1. About Me

	2. Oops, they did it again - What hackers do after they break in.

	3. Hackers be like "Why are you so obsessed with me" - Understanding the attacker's goals. Pyramid of pain.

	4. Diamonds might be forever, but logs are a girl's best friend - Logs and other mitigation strategies.  XDRs are like a beauty bag, they can be customized with all your essentials (correlation searches) and pretty useful in case of an emergency fix! (Note: I will be showing relevant logs needed to detect post compromise activity).


	5. Getting our hands dirty.
Note: I will be providing demos for these:

	- Start With Your EDR Logs: Uncover the juicy secrets.
	• High Risk Folders: Check high-risk directories for changes, such as /tmp, /var, and /usr/local. Attackers often hide malware in these directories, so flag unusual folder activity.
	• IPs: Use commands like netstat, ss, or ip addr show to monitor unusual outbound or inbound IP connections. Watch for IPs that are outside your organization or connected to known malicious domains. If it feels shady, it probably is!

	- Shell History: Linux’s way of spilling the tea!
	• Focus on logs from /var/log/secure or /var/log/auth.log  to track shell access. Check for any unusual command executions that could indicate privilege escalation, file tampering, or lateral movement.

	-  Newly Created Services: When new isn’t always better.
	• Attackers may install services under false pretenses. Look for services you didn’t authorize by running systemctl list-units --type=service. If it looks out of place, it probably shouldn't be there! Think of new services like "syscleaner" or "tempd". Sometimes they might look really legit like LenovoAutoUpdater.sh.
	• Dive into configuration files in /etc/systemd/system/ or /etc/init.d/ for service details. If anything looks too good to be true, it probably is.

	- Remote Monitoring & Management (RMM): Legit or suspect?
	• Attackers love to piggyback on legitimate RMM tools like OpenSSH or VNC, but they’ll use them to control your environment. Review /var/log/secure and /var/log/messages for abnormal usage of these tools.

	- Kernel Modules: Spotting the cheap knockoffs.
	• Check for suspicious kernel modules that could indicate privilege escalation or unauthorized system access. Commands like lsmod or modprobe are your best friends for this. If you spot unfamiliar modules, that's a massive red flag!

	- Check Event Logs Like you're reading gossip!
	• Dig into /var/log/syslog  and  /var/log/messages for general system events. Anything out of the ordinary, like strange restarts or crashes, could be the result of a compromise.
	• Use journalctl to filter and search logs for specific keywords like "failed," "error," or "unauthorized." Think of this as going through the receipts, everyone leaves a trail!

	- Suspicious Locations: The wrong wide of the internet.
	• Keep an eye out for login attempts from unusual geolocations or times. The last and lastb commands can show you the recent logins and failed attempts.
	• Review ss or netstat for abnormal network traffic. If connections are being made to strange, distant locations, you’ve likely got a problem on your hands.

	- A glimpse into the past.
	• Attackers might leave traces of their activity in system caches, especially if they’re interacting with the GUI. Look for artifacts in /home/user/.cache/ or /root/.cache/ directories. Tools like strings can extract any useful text from these cache files, like sifting through old screenshots and desktop snapshots.

	- Monitoring Resource Use and DHCP Logs: Your digital paparazzi.
	• You can use tools like atop to monitor resource usage. Look for CPU or memory spikes that could indicate hidden malicious processes.
	• DHCP Logs: Use logs from /var/lib/dhcp/ or /var/log/syslog to check for network traffic anomalies or devices connecting to your system. An unfamiliar device could be the hacker’s backdoor.

	- Automate the Hunt: Keep it stylish.
	• Set up automated detection with tools like auditd or OSSEC to keep tabs on file changes, service modifications, and unexpected network activity. Automation is like having your personal stylist, everything stays polished while you focus on bigger things.
	• Use security frameworks like AppArmor or SELinux to limit the damage attackers can do. They’re your invisible bodyguards, protecting critical files from being tampered with.


	6. How to shut it down - Mitigation and response.

	7. Final Thoughts:

	- Audit your logs regularly - Think of it as your daily dose of gossip!
	- Baseline, baseline, baseline! - Know what "normal" looks like.
	- Automate where you can.
	- Hardening your systems - Why security is like a skin care routine.
	- Practice incident response drills.
	- Stay in style. Stay up to date.
	- Trust your gut.

### Containing the Threat: Analyzing cryptomining campaigns
Speakers: Bogdan Trufanda, Mihai Vasilescu
page: https://pretalx.com/hack-lu-2025/talk/W9DSRP/
This presentation focuses on container security, particularly addressing the tactics, techniques, and procedures (TTPs) used by cybercrime groups like TeamTNT to exploit container vulnerabilities. The presentation starts with container security fundamentals and common misconfigurations, followed by an examination of TeamTNT's malware, C2 infrastructure, and evolution. Attendees will learn best practices for hardening container environments and the significance of runtime security and continuous monitoring. The talk is intended for security practitioners, DevOps engineers, and IT professionals seeking to improve their understanding of real-world container security threats and mitigation strategies. Actionable recommendations for enhancing container security posture will be provided. Container technologies have revolutionized application deployment and scalability, but they've also introduced new attack surfaces for threat actors. This presentation delves into the tactics, techniques, and procedures (TTPs) employed by some of the notorious cybercrime groups, such as TeamTNT, in exploiting container vulnerabilities.
We'll begin with an overview of container security fundamentals and common misconfigurations. We'll demonstrate how TeamTNT has evolved their tactics over time, adapting to improved security measures and expanding their target scope. Attendees will gain insights into:
TeamTNT's malware and C2 infrastructure
Best practices for hardening container environments against similar attacks
The importance of runtime security and continuous monitoring in containerized environments
This talk is aimed at security practitioners, DevOps engineers, and IT professionals looking to deepen their understanding of real-world container security threats and mitigation strategies.
The presentation will provide actionable recommendations for security professionals to enhance their container security posture and stay ahead of emerging threats in this domain.

### LOLBlue : Living Off the Land with Blue Team tools
Speakers: Maxence Fossat, Antoine C
page: https://pretalx.com/hack-lu-2025/talk/WKQ8EM/ | slides: /media/hack-lu-2025/submissions/WKQ8EM/resources/hack.lu-2025-_oNwuzOi.pdf
It is not unusual for CERT/CSIRT/SOC teams to use collection and live forensics tools in their incident response workflow. Programs such as Velociraptor, KAPE or DFIR-ORC can legitimately access low-level filesystem data and memory for the purposes of extracting forensic artifacts.

In this talk, we will show how these tools can be abused for credential access and why they might be overlooked by security teams. We will also discuss detection opportunities and what events to monitor in order to effectively counter these techniques. Our talk introduces a comprehensive and novel perspective on the offensive use of Blue Team and forensic tools — an area that has seen limited but growing interest among threat actors and red teams. While a handful of drivers and utilities have been publicly identified for such purposes, our research expands the known toolkit by presenting a systematic review of underexplored DFIR tools that can be repurposed to access system memory or protected files. We analyze how these tools operate under the hood and demonstrate real-world scenarios where they can bypass security tools.

In addition to cataloguing and evaluating these capabilities, we introduce original research on the offensive use of pre-installed or commonly deployed forensic software for data extraction and covert exfiltration. We also provide actionable guidance on detection and defence strategies, addressing a blind spot in current security literature and detection frameworks. This talk bridges the gap between DFIR tooling and offensive tradecraft, challenging defenders to reassess their trust assumptions and tool visibility.

As a company which specializes both in red teaming and incident response, Synacktiv thrives on pushing the boundaries in offensive and defensive security. As such, this joint talk will use the personal experience of both speakers to explore a fun new technique in red teaming.

Whether using pure collection tools such as DFIR-ORC or KAPE, or (ab)using the client/server architecture of Velociraptor live-forensics tool, LOLBlue offers interesting alternatives in the late stages of a red team engagement.

### BoD: Bytes Over DNS
Speakers: Didier Stevens
page: https://pretalx.com/hack-lu-2025/talk/U3WC88/
Some DNS servers, like 1.1.1.1, will accept and forward any byte values inside the DNS packet.
This makes it possible to use DNS as a C2 channel with a higher throughput than hexadecimal encoding. Although the format of the labels in a DNS request are limited to just letters, digits and a hyphen character, there are implementations that allow more than that.
A small overview will be presented.

Scripts will be shared that allow attendees to do their own testing of the DNS servers of their choice.

### Red Team Story: Offline SCCM backup secrets decryption
Speakers: Martino
page: https://pretalx.com/hack-lu-2025/talk/7FRGDY/
A brief red-team story that takes you on a short journey into SCCM backup-secret decryption. This lightning talk demonstrates a complete offline method to decrypt SCCM backup secrets, lists the exact artefacts required for decryption, and provides a supporting script to reproduce the workflow for your future red team assessments. This lightning talk presents a real red-team case study focused on SCCM backup secret decryption. Using a public SCCM lab environment (GOAD SCCM), we demonstrate the complete offline process for decrypting SCCM backup secrets, without requiring access to a live SCCM server. Although the approach has been briefly mentioned in a few articles and tweets, it has never been shown concretely from start to finish. So, we went deep to clearly reproduce and document each step, making it easier for you to use it in your future red-team operations.

The technique is especially valuable when SCCM backups are found on network shares or other exposed locations, a scenario that is surprisingly common in real-world environments. We will explain how SCCM backup-secret encryption works, highlight the artifacts that must be collected, and present a step-by-step decryption workflow. To support this, we will also share a decryption script, enabling you to reproduce the process during your next assessments and SCCM hacking. Have fun, as we did!

### Detection coverage in today's blue team world
Speakers: Claus
page: https://pretalx.com/hack-lu-2025/talk/A33UYD/
This lightning talk will cover that the concept of 'detection coverage' is a utopia in both corporate and governmental entities, as almost no one has the tooling to provide any sort of quantitative data on their detection coverage.

Vendors and unserious CISOs/blue teams try to use the otherwise excellent MITRE ATT&CK framework to establish detection coverage, but the most that this framework does is point out potential blank spots The truth of the pudding for detection coverage is that if you ask ANY blue teamer that isn't using OpenTide what their detection coverage is, you're going to get at best a feeling-based qualitative answer such as 'I think so' 'I feel that we are' 'I believe that we are able to detect what we need to'. Because no one has the data to prove it. Before OpenTide, no framework existed to provide any sort of data-driven answer.

So, ultimately, NO ONE actually knows if they're able to detect what they need to be able to detect. Many try to mature this using red or purple teaming, or using vendors to supplement their detection coverage, but ultimately, unless you can map out threats at the level of granularity that 'Atomic red team' works at, you never really know.

### Fearless File Identification
Speakers: Quentin JEROME
page: https://pretalx.com/hack-lu-2025/talk/JU89ZD/ | slides: /media/hack-lu-2025/submissions/JU89ZD/resources/presentation_Hbk64SB.pdf
The ubiquitous `file` command, powered by the C library *libmagic*, is a cornerstone of file identification—but its use in memory-safe environments has always been a security trade-off. This lightning talk explores our ongoing effort to port *libmagic* to Rust, addressing the long-standing challenge of safely embedding file identification in modern, memory-safe applications. We’ll dive into the motivations behind this port: the inherent risks of running C parsers on untrusted input, and how Rust’s safety guarantees can mitigate these concerns without sacrificing performance. The project aims for near-full compatibility with *libmagic*’s rule format, ensuring seamless integration for existing users while unlocking new possibilities for portability across Rust’s supported platforms.

Attendees will get a sneak peek at the current state of the implementation, which already identifies common file types like MS-DOS executables, ELF binaries, and scripts. We’ll also discuss the roadmap, including plans to publish a Rust crate, complete a CLI tool equivalent to `file`, and create bindings for other languages.

### Hunting for Linux Extended File Attributes
Speakers: Xavier Mertens
page: https://pretalx.com/hack-lu-2025/talk/CMLHHF/
In this lightning talk will show how xattr's can be used to hide a payload, then I'll introduce a quick script that will help to find potentially malicious xattr's on a filesystem. In this lightning talk will show how xattr's can be used to hide a payload, then I'll introduce a quick script that will help to find potentially malicious xattr's on a filesystem.

### Incident reporting made easy, using Draugnet
Speakers: Andras Iklody
page: https://pretalx.com/hack-lu-2025/talk/ZDKXEN/
Draugnet is a relatively new OSS tool that facilitates the reporting of incidents, threat intel and other similar matters to an organisation (such as a CSIRT). This lightning talk aims to introduce the tool and quickly describe why anyone should care. Draugnet is a relatively new OSS tool that facilitates the reporting of incidents, threat intel and other similar matters to an organisation (such as a CSIRT). This lightning talk aims to introduce the tool and quickly describe why anyone should care.

### From Buzzword to Battlefield: The Cybersecurity Challenges of Smart Cities
Speakers: Marina Bochenkova
page: https://pretalx.com/hack-lu-2025/talk/FXR3DQ/
“Smart City” has been a trendy buzzphrase used by politicians, city planners, and tech companies for over a decade now — but their shiny promises gloss over dangerous realities.

Downtime and damages in municipalities due to cyberattacks regularly make the news, but we focus primarily on securing and recovering IT systems. Smart Cities by nature use a combination of IT and OT systems but have no established or holistic approach for managing overlapping risks to both. The consequences to security from varied stakeholders involved in Smart City planning and implementation go unexamined. Human hazards, vulnerable devices, and data management issues build on these to create diverse and creative attack paths for all sorts of threat actors.

Smart Cities present a ubiquitous and unique combination of risks which must be comprehensively assessed in order to improve procedural and operational security, reliability, and resilience. By reframing our understanding of what Smart Cities are, we can use and integrate pre-existing actionable strategies to prepare and defend against threats ranging from pandemics to nation-state attacks. As politically motivated cyberattacks expand in reach and collateral radius, we need to prepare our cities for when they become the next battlefield. This talk aims to expand our definition of Smart Cities; discuss the data, human, and technological risks that they face; and share resources on how to deal with them.

### Fake Jobs, Real Malware. Uncovering How Cybercriminals are Exploiting the Employment Market
Speakers: Ionuț Baltariu
page: https://pretalx.com/hack-lu-2025/talk/DPNKRE/
This session dives into a sophisticated recruitment scam run by the notorious Lazarus Group on LinkedIn and other job-related platforms. As revealed by Bitdefender Labs, we will uncover how the threat actors use complex methods to deliver malware into what looks like a coding assessment for a job offer. Using advanced social engineering, this scam campaign shows why it's important to stay alert and aware when using any digital service.

During this talk, we will follow the whole infection process, starting with the Javascript Loader & Infostealer, moving to Python scripts that ramp up the damage, and ending with a final payload that doubles down on data theft and connects to the Command and Control (C2) server via The Onion Router (Tor). Attendees will gain a comprehensive understanding of the tactics used by cybercriminals, the potential risks to your organization's security, and strategies to protect against similar attacks. In this session, we will take a deep dive into a sophisticated recruitment scam run by the well-known Lazarus Group on LinkedIn and other job-related platforms. We will start by analyzing the interaction between a Bitdefender employee and a fake recruiter on LinkedIn, while also explaining what the so-called recruiter is after and what are the known tactics that are used in these kinds of scenarios.
Given the fact that the scam is enabled by job-seeking developers that set out to finish the coding assessment given by the fake recruiter, we will continue with a bird’s eye view on the received code repositories. Among thousands of lines of code, stolen from public repositories, the threat actors hide an obfuscated Javascript snippet that begins the malware infection chain.

Moving forward, the complexity of the infection chain increases. A comprehensive breakdown of each step involved will be provided, with insights about malware analysis and the necessary protective measures to prevent infection:

- Downloading more malicious, self-unpacking Python scripts 
- Using public services to store information (e.g: pastebin)
- Downloading a malicious binary that doubles down the infostealing efforts, while also exfiltrating data through TOR

The presentation will end with conclusions and take aways, while also leaving plenty of time for Q&A.

### intelmq.ai - adding ML model support to intelmq
Speakers: Aaron Kaplan, Sebastian Wagner, Jürgen Brandl
page: https://pretalx.com/hack-lu-2025/talk/U3ZG7S/ | slides: /media/hack-lu-2025/submissions/U3ZG7S/resources/IntelMQ.AI_nVRHQIM.pdf
[IntelMQ](https://intelmq.org) is a great tool for automating structured IT security data feeds for CERTs: need to process all of shadowserver for a country? IntelMQ can easily do it. Need to alert on all vulnerable devices that shodan knows about? Sure! 

But what about unstructured text? Many reports (CTI reports) contain lots of relevant information (IoCs, TTPs, etc.), but often in prose or only in semi-structured formats (hidden in a table, etc.).
For information extraction, LLMs and other AI models (BERT, etc.) proved their merit already.

The presents will show how they extended intelmq to support 
these AI models and how the combination lends itself (semi-) automating a CTI analyst.

IntelMQ to MISP output included ;-) Integrating "AI" into deterministic data-flow frameworks such as IntelMQ has its challenges. For example, AI tends to give stochastic answers, which might be correct or - sometimes - might not be.
How to deal with these challenges will be also discussed.

### No way to enable SSH access to your new router? The vendor might have something to hide
Speakers: Stanislav Dashevskyi, Francesco La Spina
page: https://pretalx.com/hack-lu-2025/talk/BDUTYD/ | slides: /media/hack-lu-2025/submissions/BDUTYD/resources/dashevskyi_20_Uo4kCmD.pdf
The operating systems of many proprietary consumer- and enterprise-grade
networking devices do not allow for easy customization. Even when SSH access is
available, it often supports only a limited set of tightly controlled commands,
offering no way to install new binaries — or to understand what the existing
ones actually do.

The Internet is full of guides on “jailbreaking” proprietary routers — an
unfortunate necessity for users who want deeper control over the hardware
they've paid for.

In contrast, open-source router OSes like OpenWrt provide full SSH access. This
seemingly simple feature sends a clear message: “This device is truly yours, and
you're welcome to inspect or improve it — even find security bugs, if you're so
inclined.”

But what happens when a proprietary OS is built on top of an open one like
OpenWrt?

In this talk, we’ll take you on a journey through reverse engineering OS
binaries based on OpenWrt, used by a major vendor [REDACTED]. We were surprised
to discover that they had patched the Lua compiler for the sole purpose of
hindering static analysis.

We'll demonstrate several techniques for “owning” a line of devices from this
vendor — from rediscovering a "patched" backdoor in the restricted SSH service,
to identifying an authenticated OS command injection vulnerability buried deep
in a custom Lua module.

These findings could enable full remote takeover of the devices — so it’s no
wonder the vendor didn’t allow SSH access in the first place... N/A

### Oops, I Hacked It Again: Tales and disclosures
Speakers: Ignacio Navarro
page: https://pretalx.com/hack-lu-2025/talk/TYQJK3/
Breaking into supermarket systems, ticketing platforms, and more. I’ll share some of my latest hacking stories, showing how I found the vulnerabilities, reported them, and collaborated with the companies. We’ll dive into tools, the challenges of disclosure, the importance of being “ethical”, lessons learned and how these experiences help improve security and build trust between hackers and organizations. Description
=======

The talk is divided into 6 chapters. In the first one, I’ll relate what an Ethical Hacker is and what he does, and I’ll also prepare the audience for the upcoming hackings tales.

Chapter 2: Hacking tales. In this chapter I’ll talk about different ethical hacker stories that happened to me recently. Each story will have the technical part about how I exploit it and what I can do in the system, the way that I communicate it to the company and their responses.

The first story is a small update about my last talk(Insert coin: Hacking arcades for fun), where we can basically get all the customer data, charge money for free and emulate all debit cards. It affects more than 2.3k installations in more than 70 countries. But the most interesting part was the in-person meeting with the company.
Second story is about a large supermarket chain. After escalating in some web servers and getting root access, I had read/write access to the customer and employee database and was even able to modify product prices among other things.
The third one is about a ticket sales and distribution company. The results were similar, getting all the tickets, customers and employees, being able to generate some free tickets and getting admin access. But the way to get access was different, and the response from the company was the best, ending in a request for pentesting and a security talk to the entire company.
A transportation company, after some idors and business logic vulnerabilities were able to get all tickets, user data and generate free tickets.
The last tale, an e-commerce platform that allows businesses to create and manage their online stores: A bunch of exposed files, some .js files with the body of apis. After reading some code, we were able to login as any user in any business(Insurance, airlines, banks) including some CEO accounts.

Chapter 3: In this chapter I’ll dive into the different tools(90% open source) that I use on a daily basis, methodologies and the most common mistakes that we can find.

Chapter 4: Different types of disclosure. I’ll explain why this is important, from the point of view of hackers, companies and the community. Below I’ll show the way I always present my reports, following the examples used by my friends and others.
Also, in this chapter I'll show the normal responses from the companies and the way to handle it, cause in some cases it can be frustrating and even threatening.
To close the chapter I’ll talk a bit about BBP and VDP.

Chapter 5 will discuss the impact we can get from good feedback from companies, seeing how more companies have improved their security posture and relationship with hackers. Also, perhaps the most important part, personal growth, recognition and learning new methods/attacks in a real world scenario.

Chapter 6: Ending and conclusions. Part of the takeaways are to encourage new generations to do ethical hacking and help generate a good relationship between hackers and companies. The idea of ​​promoting the "ethical" part arises because unfortunately every day we see more cybercriminals selling user data and other confidential information of third parties. We have a responsibility to educate, identify and work on security vulnerabilities. 

Outline
=======

- Introduction
   - Whoami
   - Disclaimer
   - What's an “ethical hacker”?
- Hacking tales
   - Conclusion from the arcade company of last year
   - Large supermarket chain
   - Tickets sales and distribution company
   - Transport company
   - E-commerce platform
- Essentials
   - Tools
   - Methodology
   - Common mistakes
- Disclosures
   - Types
   - Why is it important?
   - My way to report
   - Other ways to report
   - Handling responses from companies
   - BBP/VDP
- Impact of ethical hacking
   - Feedback from companies who I hacked
   - Encouraging others to get involved in ethical hacking
- Conclusions
   - Takeaways
   - Q/A

### OverLAPS: Overriding LAPS Logic
Speakers: Antoine Goichot
page: https://pretalx.com/hack-lu-2025/talk/Y3DGVG/
Local Administrator Password Solution (LAPS) automates local admin password rotation and secure storage in Active Directory (AD) or Microsoft Entra ID. It ensures that each system has a unique and strong password.

In OverLAPS: Overriding LAPS Logic, we will revisit and extend our previous research (Malicious use of "Local Administrator Password Solution", Hack.lu 2017) by exposing client-side attacks in Windows LAPS ("LAPSv2"). After a brief overview of LAPS's evolution, from clear-text fields in AD with Microsoft LAPS ("LAPSv1") to encrypted AD attributes or Entra ID storage with Windows LAPS, we will explore the client-side logic of Windows LAPS. Unlike prior work that exfiltrates passwords only after directory compromise, we will focus on abusing LAPS to maintain presence on compromised endpoints, both on-prem and Entra-joined devices.

We will leverage PDB symbols and light static analysis to understand how LAPS works internally, then use Frida for dynamic hooking to capture, manipulate, and rotate admin passwords on demand. We will also reproduce Frida proof-of-concepts using Microsoft Detours for in-process hooks.

Attendees will gain practical insights into new attack vectors against Windows LAPS, enabling them to assess, reproduce, and defend against client-side attacks in their own environments. LAPS "v1" (legacy Microsoft LAPS) and "v2" (current Windows LAPS) have been studied by numerous people. 

However, past research has focused on attacking LAPS from the server side, i.e. recovering passwords from AD/Entra with high privileges on the infrastructure. 
This research takes a different approach: client-side approaches that grant users control over their own LAPS password, changing the LAPS password on demand.

This talk explores a new angle and shares practical techniques that hackers can experiment with and apply in their own work.

### Phishing detection using various parts of DNS ecosystem
Speakers: Piotr Białczak, Michał Hałoń
page: https://pretalx.com/hack-lu-2025/talk/EXYEBP/ | slides: /media/hack-lu-2025/submissions/EXYEBP/resources/hack.lu_2025_MRE6UFi.pdf
DNS gives a unique vantage point for phishing detection. In my presentation We will show how we use it at CERT.PL to search for phishing domains in .pl Top Level Domain, but also more universally as our contribution to the DNS4EU project – an entirely European DNS resolver. We will discuss using various parts of DNS ecosystem as observation points. Then show how we applied standard heuristics and machine learning/AI methods to get some good detection results. DNS (Domain Name System) is one of the cornerstones of the internet. Its various parts create a rather complex, interconnected ecosystem, with many observation points for phishing detection. Some of those are covered by CERT.PL monitoring systems as our contribution to the DNS4EU project – an entirely European DNS resolver.
In our presentation we will show our three approaches for phishing detection. Firstly, how we identify new phishing domains in .pl by looking into DNS registry data. Secondly, We will show how we monitor DNS requests at .pl TLD nameserver level for early phishing campaign detection. Thirdly, we will present how we analyze requests at resolver level in order to detect phishing at various TLDs.
We will discuss when we use rule based approach/heuristics, and when we decided to use machine learning/AI methods to boost our analytics. We will talk about pros and cons of our systems, and how good they are on phishing detection.

### RomCom exploits Firefox and Windows zero days in the wild
Speakers: Damien Schaeffer
page: https://pretalx.com/hack-lu-2025/talk/V3GFCH/
Last year, the Russia-aligned group RomCom used a zero-click exploit combining vulnerabilities in Mozilla and Microsoft products. This exploit allowed them to compromise computers without user interaction. The attack involved a fake website that led to the execution of RomCom's backdoor.

The first part of the exploit targeted Firefox and Tor Browser, using a bug to run code. The second part involved a Windows vulnerability that allowed RomCom to gain higher privileges and deploy their backdoor. Microsoft and Mozilla quickly patched the issues.

RomCom's use of these vulnerabilities shows their advanced capabilities. This presentation covers RomCom's tactics, the attack chain, and the technical details of the exploits, along with the fixes from Mozilla and Microsoft. In October 2024, we discovered, in the wild, a zero-click exploit that combines two previously unknown vulnerabilities: one in Mozilla products, and the other in Microsoft Windows. We attribute the exploit to the Russia-aligned group RomCom. This is at least the second time that RomCom has been caught exploiting a significant zero-day vulnerability, after the abuse of CVE-2023-36884 in June 2023 against Microsoft Word documents related to the Ukrainian World Congress and the NATO summit.

The compromise chain is composed of a fake website that redirects the potential victim to the server hosting the exploit, and if successful, the latter downloads and executes the RomCom backdoor. We don’t know how the link to the fake website is distributed; however, if the page is reached using a vulnerable browser, a payload is dropped and executed on the victim’s computer with no user interaction required.

Analysis of the hosted files revealed a weaponized vulnerability for the latest versions of Firefox and Tor Browser at that time. The bug is a use-after-free vulnerability in the animation timeline, allowing arbitrary code to be executed in the context of Firefox’s sandboxed content process. While we’re not certain whether RomCom developed or bought the exploit, the code demonstrates deep knowledge of Firefox’s internals. We reported this vulnerability to the Firefox team, who acknowledged it and released a patch in an impressive 25 hours.

In the meantime, we analyzed the second stage of the exploit and discovered a sandbox escape vulnerability in Windows. An undocumented and permissive RPC endpoint allowed execution of code at the medium integrity level, regardless of the privilege level of the calling process, resulting in an elevation of privileges on the system. RomCom exploited this bug to break out of Firefox’s sandbox and download further components in order to deploy the group’s backdoor. Microsoft released a security advisory and released a patch in early November.

Studying RomCom’s arsenal highlights a high level of sophistication and the group’s ongoing effort to arm itself with powerful capabilities. The combination of the two zero-day vulnerabilities allowed this threat actor to compromise computers without any user interaction. This presentation provides a comprehensive overview of RomCom, its usual TTPs, this compromise chain, and its victimology. We also include a detailed technical analysis of the exploits and the corrective measures implemented by Mozilla and Microsoft.

### From Achilles to NIS2: Slovakian Lessons on Proactive Cybersecurity and Vulnerability Disclosure
Speakers: Michal Rampášek, Alexander Valach
page: https://pretalx.com/hack-lu-2025/talk/SLSQAL/
CSIRT.SK’s cybersecurity approach emphasizes proactive vulnerability management through Achilles, system which performs non-invasive scanning of public administration systems to detect security flaws while minimizing disruption. This model enables real-time risk assessment without impacting system availability, in line with NIS2. To enhance threat-driven assessments, CSIRT.SK integrates cyber threat intelligence, mapping active threat campaigns to known exploits. This fusion of CTI and vulnerability scanning enables targeted security enhancements and faster mitigation of emerging threats.  
Further key NIS2 innovation at CSIRT.SK and its constituency, is structured vulnerability disclosure, where public organizations must publish clear guidelines for reporting security issues. This shifts responsibility from researchers to system operators, ensuring efficient triage and response while fostering trust with security researchers.  
The presentation showcases Slovakia’s model of scanning, contrasting it with alternative approaches, and provides actionable insights for CSIRT teams on scalable vulnerability assessment, ethical hacking engagement, and intelligence-driven security operations. The NIS2 directive allows CSIRTs to carry out active, non-intrusive scanning of publicly accessible networks and information systems of entities. In Slovakia, proactive vulnerability scanning is already a cornerstone of government unit CSIRT.SK activities within its constituency, exemplified by the Achilles project. The recently amended Slovak Cybersecurity Act further clarifies that all CSIRT units have the legal authority to conduct non-invasive vulnerability detection and assessments within their scope. These assessments explicitly avoid negative impacts on the networks, systems, or services being evaluated, maintaining a balance between proactive security and minimal disruption.
From the perspective of the Slovak CSIRT.SK, Poland's draft Cybersecurity Act under NIS2 introduces a more invasive approach, allowing Polish CSIRTs to bypass system protections for security assessments, resembling red teaming. For Slovakia to conduct similar assessments, clear legal frameworks (including mandates, consent protocols, and GDPR compliance), technical capabilities (such as secure testing environments and skilled personnel), and organizational structures (governance, risk management, and cooperation protocols) would be essential.
In the area of coordinated vulnerability disclosure mandated under Article 12 of the NIS2, Slovak law already contains an obligation for public organizations to publish rules for reporting vulnerabilities on their website. The idea behind this legal regulation is based on the fact that it does not directly oblige researchers but entities responsible for the operation of information systems and technologies of public administration. They are obliged to publish rules on how security research can be carried out and the procedure for responsible publication of vulnerabilities. We believe it is appropriate to issue a framework policy for responsible vulnerability disclosure as a generally binding legal act. In addition, it is appropriate to use proper reporting channels. For this purpose, it is possible to use the security.txt concept.
The vulnerability assessment process is intertwined with cyber threat intelligence, as it relies on up-to-date insights into emerging threats and adversary tactics. Threat intelligence analysts populate the MISP (Malware Information Sharing Platform) with data on threat actors, their tactics, techniques, and procedures (TTPs), as well as known vulnerabilities exploited in active campaigns. The vulnerability assessment team uses this intelligence to prioritize assessments, focusing on specific threat actor campaigns and the vulnerabilities they exploit, thereby enhancing proactive defense measures and risk mitigation strategies.
The presentation examines how these approaches reflect the broader goals of proactive cybersecurity and security research while addressing the challenges of harmonization and trust in public-private partnerships. Additionally, it concludes with recommendations for CSIRTs to balance proactive assessments with legal and ethical considerations, including developing clear testing policies, ensuring transparency with affected entities, and fostering collaboration through secure information-sharing frameworks.

## 2025-10-21 — Schengen 1 & 2

### API Underworld: Red Team Hacking Secrets
Speakers: Parth Shukla
page: https://pretalx.com/hack-lu-2025/talk/L8UDVY/
This comprehensive workshop is designed to provide participants with a deep understanding of API security, its challenges, and best practices to mitigate risks. Spanning six engaging sessions, the program begins with an introduction to API security and real-world breaches, highlighting the critical importance of securing APIs.

Participants will explore reconnaissance techniques, including using tools like Shodan and Google Dorking, to identify API endpoints. The workshop delves into common API vulnerabilities, such as SQL Injection and XSS, complemented by practical hands-on scanning with Burp Suite.

Additionally, the sessions cover OSINT (Open Source Intelligence) techniques with tools like Maltego, theHarvester, and Wayback, empowering attendees to gather intelligence on API targets. The program culminates with guided vulnerability exploitation exercises and a collaborative group activity to identify and exploit API flaws.

Concluding with a wrap-up session and an open Q&A, this workshop equips participants with the knowledge and skills to secure APIs effectively while fostering a hands-on learning environment Session 1: Introduction to API Security

Overview of API Security
Real-world examples of API security breaches
Importance of securing APIs

Session 2: Reconnaissance Techniques

Introduction to reconnaissance
Using Shodan for API recon
Google Dorking for API endpoints
Practical exercise: Recon on a sample API

Session 3: Identifying API Vulnerabilities

Common API vulnerabilities
Demonstration: SQL Injection, XSS on APIs
Hands-on: Scanning an API with Burp Suite

Session 4: OSINT for API Security

What is OSINT?
Tools: Maltego, theHarvester,Wayback
Practical exercise: Conducting OSINT on an API target

Session 5: Hands-On Vulnerability Exploitation

Step-by-step guide to exploiting API vulnerabilities
Practical exercises on various vulnerabilities
Group activity: Find and exploit vulnerabilities on a mock API

Session 6: Wrap-Up and Q&A

Recap of key points
Final thoughts and best practices
Open Q&A session for participants

### Crafting an Infoleak exploit - A Hands On tutorial
Speakers: Saumil Shah
page: https://pretalx.com/hack-lu-2025/talk/FZDEPW/
"You do not find infoleaks, you create them" -Halvar Flake
In this hands-on 2 hour workshop we will learn how a memory corruption bug can be turned into both an RCE as well as an Infoleak bug to bypass ASLR. Students will work with a memory corruption vulnerability in a popular web server and turn it into an infoleak bug. Memory corruption bugs don't always have to result in arbitrary code execution. Sometimes a memory corruption bug can be put to an entirely different purpose, in this case turning it into an Infoleak bug to bypass ASLR.

This workshop demonstrates how to make infoleak bugs happen seemingly from thin air. Students will work with a 12 year old vulnerability in a popular web server and turn it into a brand new Infoleak bug.

**Outline**
- Case study of an integer overflow bug in a popular web server.
- Understanding the chain of function calls and frames on the stack.
- Understanding the basis of an infoleak.
- Using GDB to hit trace black box binaries to analyse the sequence of function calls.
- Diverting the flow of functions after memory corruption to produce meaningful output.
- Populating the output with arbitrary values.
- Leaking the stack pointer address.
- Leaking libc base address.
- Putting the infoleak exploit together

The case study will be presented for X86 as well as ARM32 binaries.

*Theory* - 1 hour
*Exercise* - 1 hour

**Students will be provided with** a docker container with the necessary debugging and exploit development tools. Students are expected to bring a laptop with a working Docker installation.

### Kunai: From Zero to Ninja
Speakers: Quentin JEROME
page: https://pretalx.com/hack-lu-2025/talk/XGVKFA/
In this workshop, participants will learn everything they need to know to install Kunai and start monitoring their Linux environment to spot attackers or simply for fun.

In the first part, we will cover all the essential information about Kunai. This will include a quick walkthrough of the Kunai documentation, explaining what participants can expect from this tool. Simultaneously, we will conduct exercises to help participants become familiar with the tool, its command line, and configuration file.

In the second part, we will run exercises showcasing more advanced Kunai usage. This will include building custom detection rules to detect specific anomalies or malware, learning how to load Indicators of Compromise (IoCs) into the detection engine, and how to integrate Kunai with your favorite MISP instance. If time allows, we will also cover additional advanced topics. In this workshop, participants will learn everything they need to know to install Kunai and start monitoring their Linux environment to spot attackers or simply for fun.

### Part 1: Introduction to Kunai
- **Essential Information**: Cover all the essential information about Kunai.
- **Documentation Walkthrough**: Quick walkthrough of the Kunai documentation, explaining what participants can expect from this tool.
- **Hands-on Exercises**: Conduct exercises to help participants become familiar with the tool, its command line, and configuration file.

### Part 2: Advanced Kunai Usage
- **Custom Detection Rules**: Building custom detection rules to detect specific anomalies or malware.
- **Indicators of Compromise (IoCs)**: Learning how to load IoCs into the detection engine.
- **Integration with MISP**: How to integrate Kunai with your favorite MISP instance.
- **Additional Topics**: If time allows, we will also cover additional advanced topics.

## 2025-10-21 — Hollenfels

### Web forensic with Lookyloo
Speakers: Raphaël Vinot
page: https://pretalx.com/hack-lu-2025/talk/K8ACJX/ | slides: /media/hack-lu-2025/submissions/K8ACJX/resources/Hack.lu_2025_Sry7Cgd.pdf
We often talk of doing forensic on a filesystem, or in memory, but what about investigating how a browser interacts with a website? Lookyloo is a web interface that helps you to do exactly that. It also comes with a whole bunch of connectors to 3rd party services and makes it very easy to pivot on indicators to find phishing campaigns. This workshop will start by explaining how modern websites are often implemented. We will then give an  introduction of the tool and a demonstration of the modules. And continue with an introduction to the API and how to integrate it with your own tools.

### Detection Engineering with Sigma
Speakers: Thomas Patzke
page: https://pretalx.com/hack-lu-2025/talk/EEZ3PN/
[Sigma](https://sigmahq.io) is an open and generic format to share log detection signatures. In this hands-on workshop we learn how to write good Sigma rules by developing some for existing threats. It will cover simple rules for detection of single events as well as correlation rules for detection of event relationships. This workshop will cover the following topics:

* Introduction to the [Sigma detection format](https://sigmahq.io/docs/basics/rules.html).
* Don't reinvent the wheel: searching existing Sigma rules.
* Developing simple Sigma rules for single events.
* Developing [Sigma correlation rules](https://sigmahq.io/docs/meta/correlations.html) to detect event relationships.
* Validation of Sigma rules.
* Using LLMs to support Sigma rule development.

## 2025-10-21 — Vianden & Wiltz

### Flowintel - Flow your management
Speakers: Cruciani David
page: https://pretalx.com/hack-lu-2025/talk/7K3DUQ/ | slides: /media/hack-lu-2025/submissions/7K3DUQ/resources/presentation_GLlZI9F.pdf
Incident response and threat intelligence teams often face a paradox: vast amounts of information, yet no structured way to manage cases, tasks, and collaborative workflows. This leads to duplicated efforts, knowledge silos, and slower response times.
FlowIntel, an open-source case and task management platform, bridges this gap by providing analysts with a modern, flexible environment to organize investigations. In this workshop, participants will learn how to install, configure, and start using Flowintel.

By working on a sample case, the audience will be guided through the tool and discover its key features, including creating cases and tasks, assigning users, integrating with MISP in different ways, and much more.

### Payload Obfuscation for Red Teams
Speakers: Duncan Ogilvie
page: https://pretalx.com/hack-lu-2025/talk/AMCS8W/
In this workshop you will learn how to obfuscate your payloads with a custom VM. This will help to evade signature detections and make reverse engineering more difficult. The format will be a hands-on workshop and participants will walk away with new tooling they can try out in the field right away! In this workshop we will leverage the RISC-V architecture and the LLVM ecosystem to build a simple obfuscation pipeline. The VM interpreter code is small and once it is loaded, you do not need to allocate additional executable pages to execute arbitrary payloads.

Covered topics:
- Introduction to VM-based obfuscation
- Basics of the RISC-V architecture
- Compiling payloads for the RISC-V architecture
- Obfuscating the VM interpreter for evasion
- VM Hardening to complicate reversing the payloads (as time allows)
- Building a basic C2 framework (as time allows)

The bulk of the work will be done in a GitHub Codespace (Linux), which makes it easy for participants to get started. However, the final payloads need to be executed in a Windows VM (which you have to prepare beforehand).

**Note**: Participants need C programming and Linux command line experience to follow along with the workshop. Reverse engineering experience is highly recommended. The concepts covered in the second half of the workshop are quite advanced

## 2025-10-21 — Echternach & Diekirch

### Tech Duel: The Escape Battle
Speakers: Stijn Tomme, Dominiek Madou
page: https://pretalx.com/hack-lu-2025/talk/MJDURG/
In a 90 minute workshop 2 teams will compete. Each team consists of max. 5 persons. During the first 10 minutes they will receive a briefing on the mission. The countdown timer starts the mission (60 minutes)

## 2025-10-22 — Europe

### Tracking and documenting Threat Actors using MISP - A slightly different approach
Speakers: Csaba Barta
page: https://pretalx.com/hack-lu-2025/talk/GGT3WY/
A technical talk about a toolset that can be used to track and document threat actors in MISP This technical talk is about a development project involving a toolset that enhances MISP's ability to store and update Threat Actor profiles. The presenter will introduce the initial problem and describe the concept of the solution and the details of the implementation. Besides this the audience will see the toolset in action while the presenter goes through the lifecycle of a threat actor profile (e.g. initial creation, updates)

#### Agenda
- Initial problem statement
- Concept and technical details
- Demo with TA profile lifecycle (showing the toolset in action using an imaginary Threat Actor Profile)

### A pragmatic approach to build a threat landscape
Speakers: Thomas Patzke
page: https://pretalx.com/hack-lu-2025/talk/7XNVBR/ | slides: /media/hack-lu-2025/submissions/7XNVBR/resources/A_Pragmatic_A_EKeuPKC.pdf
Building an actionable organization-specific threat landscape for an organization is a challenging task. An useful format has to be chosen, information has to be collected and finally meaningful action should be derived from the created product. This talk describes a pragmatic approach to build such a threat landscape that can be used by various stakeholders and is built from openly available information as well as own observations of the operational security teams. Furthermore, possible follow-up actions are discussed as well as disadvantages and shortcomings of the approach. "What are the threats relevant for us?" is likely one of the most common question the threat intelligence team is asked for by the management as well as technical stakeholders. Answering the question is challenging. Just picking some random insights from recently read threat reports certainly doesn't gives a holistic view. Not all threats that were reported publicly are relevant for the own organization and the other way around, the own sector is possibly underrepresented in public reporting and some threats like ransomware are opportunistic and simply don't care about the sector they attack. There are lots of further questions, e.g. if the usage of a technique that is mentioned in a threat report from ten years ago is still relevant? And what's about the observations of the own operational security teams?

In this talk I will show a pragmatic approach with reasonable-effort for building a technical threat landscape that results in a MITRE ATT&CK map of techniques by utilizing different (open and private) sources and own observations. All techniques are mapped to a relevance that allows to focus further efforts to the most relevant techniques. Furthermore, I will show how this threat landscape can be used to support governance and purple teaming efforts.

The talk will be concluded with some experiences and statistics to answer questions like:

* How much of the techniques documented in ATT&CK are really relevant?
* Are there really irrelevant techniques?
* How often should so a thread landscape be updated?
* How much value do the used sources provide? Are they possibly biased?

### Exploring Threats Leveraging Blockchains
Speakers: Rascagneres Paul
page: https://pretalx.com/hack-lu-2025/talk/8A9RUW/
Why blockchain matters to Threat Intelligence? The presentation will try to reply to this question. The presentation will start by a quick presentation of the Ethereum decentralized blockchain and the smart contracts logic. Then, examples of malware abusing Web 3 will be described. The malware described during the presentation are linked to crimeware organizations as well as APT organizations. We will see why the attackers use Web 3, the advantage for them and the issues for the blue teams. Finally, we will cover the threat hunting opportunities and the tools that can be used to hunt for malware but also how to use block explorers such as etherscan.io or Arkham intelligence to track multiple blockchains and visualize transactions and addresses. Nothing to add I cover the entire agenda in the abstract. If you have any questions ping me.

### Reversing a Pay Phone for Fun but No Profit
Speakers: Inbar Raz
page: https://pretalx.com/hack-lu-2025/talk/UYUQFR/ | slides: /media/hack-lu-2025/submissions/UYUQFR/resources/Reversing_a_P_DaoVsGD.pdf | slides: /media/hack-lu-2025/submissions/UYUQFR/resources/Reversing_a_P_R1jso15.pdf | slides: /media/hack-lu-2025/submissions/UYUQFR/resources/Reversing_a_P_8vMXC2D.pdf | slides: /media/hack-lu-2025/submissions/UYUQFR/resources/Reversing_a_P_dTROcrP.pdf
The “Telecard” Israeli Payphones entered service in 1990, and at the height of their career there were 27,000 installed throughout the country. While most of them have already been removed from the streets, some remain in service in selected locations. Designed and manufactured at the late 80’s, they were nothing short of state-of-the-art embedded computer systems, capable of self-diagnosis and reporting. In this talk, we will explore one (or more) of those, from breaking into the chassis and all the way to code execution. Multiple challenges and multiple solutions make this a fascinating peek into an ahead-of-its-time device. In this talk I tell the story of how I decided to reverse engineer the Israeli payphone, which was nothing short of an engineering marvel for its time. The talk is laid out according to the MITRE ATT&CK tactics and shows how the same principles apply to fun projects and not just CNE.

### Slipping Through the Cracks: How Malicious Emails Evade Detection
Speakers: Elyssa Boulila
page: https://pretalx.com/hack-lu-2025/talk/7XPR8X/
Organizations increasingly adopt policies that encourage employees to report emails they perceive as potentially malicious. These user-submitted reports are typically reviewed by the Security Operations Center (SOC), which conducts in-depth analyses to determine appropriate response measures. This approach enhances organizational defenses by integrating human vigilance with expert investigation, thereby complementing existing automated threat detection systems. 

This study presents a comprehensive examination of phishing emails reported by users across five organizations over a span of several months. These messages are particularly stealthy since they were able to bypass all the automated checks in place, yet were identified by the employees, and confirmed as malicious by security experts. We extract and characterize the evasion techniques employed in these phishing campaigns and evaluate their level of sophistication. Our findings reveal that while these attacks are generally low in volume, they are highly targeted and carefully orchestrated, demonstrating significant forethought and strategic intent. Notably, these campaigns utilize advanced evasion tactics at the message level—including the use of corrupted QR codes — and cloaking relying on bot detection and browser fingerprinting techniques.  

The objective of this work is to deepen our understanding of the phishing landscape while taking into consideration the threats that slip through the cracks of advanced security filters. This talk will present the evasion techniques extracted from user-reported messages, along with an overview of our analysis infrastructure, CrawlerBox, designed to overcome cloaking tactics that exploit browser fingerprinting and bot detection challenges. CrawlerBox is made available as an open-source tool to assist other researchers in pursuing further studies.

### Silent Killers: Unmasking a Large-Scale Legacy Driver Exploitation Campaign
Speakers: Jiří Vinopal
page: https://pretalx.com/hack-lu-2025/talk/QSWNWS/
What if your trusted security solutions could be silently disarmed without warning? What if a long-forgotten vulnerability in a legitimate driver became the perfect weapon for attackers to bypass defenses and strike undetected?

In 2025, Check Point Research uncovered a sophisticated campaign leveraging over 2,500 unique variants of a vulnerable legacy driver to disable EDR and AV solutions. By abusing a loophole in Windows driver signing, the attackers successfully deployed a powerful EDR/AV killer module that bypassed Microsoft’s Vulnerable Driver Blocklist and evaded detection mechanisms, including those introduced by the LOLDrivers project.

To ensure stealth, the attackers carefully manipulated the driver’s PE structure, generating distinct hashes while preserving its valid signature — a move that allowed thousands of modified variants to remain undetected. Operating from a public cloud’s China region, the attackers targeted victims primarily in China and parts of Asia, with devastating precision.

Check Point Research’s findings prompted Microsoft to update its Vulnerable Driver Blocklist, neutralizing the exploited driver variants. This paper presents the campaign’s technical details, explores the evasion techniques in depth, and provides practical insights for defenders to mitigate emerging driver exploitation threats. Are your defenses prepared for attackers turning trusted code into a silent threat? - CPR uncovered a large-scale ongoing campaign involving thousands of first-stage malicious samples used to deploy an EDR/AV killer module in its initial stage. This module was first detected and recorded in June 2024. It was observed leveraging and exploiting more than 2,500 distinct variants of the legacy version **2.0.2** of the known vulnerable driver **Truesight.sys**, which is the RogueKiller Antirootkit Driver and part of Adlice’s product suite. This driver has a known vulnerability in versions below 3.4.0.

- The attackers exploited the legacy version 2.0.2 of the Truesight driver to take advantage of a Windows policy loophole (Exception in Driver Signing Policy), allowing the driver to be loaded on the latest versions of Windows OS. Notably, the attackers specifically selected the 2.0.2 version because it retains the vulnerable code while also bypassing the latest Microsoft Vulnerable Driver Blocklist and common detection mechanisms, such as those introduced by the LOLDrivers project, none of which detect this version.

- To further evade detection, the attackers deliberately generated multiple variants (with different hashes) of the 2.0.2 driver by modifying specific PE parts while keeping the signature valid. We detected over 2,500 validly signed variants of this driver.

- The attackers leveraged infrastructure in a public cloud's China region to host payloads and operate their C2 servers. Around 75% of the victims are located in China, while the remainder come from other parts of Asia (e.g., Singapore, Taiwan).

- The initial-stage samples act as downloaders/loaders and often disguise themselves as well-known applications. They are typically distributed via phishing methods, including deceptive websites and phishing channels in messaging apps. Along with the EDR/AV killer module, they are designed to prepare the infected machine to deliver final-stage payloads, such as Gh0st RAT variants.

- CPR reported this issue to MSRC, leading to an updated version of the Microsoft Vulnerable Driver Blocklist (available since December 17, 2024), effectively preventing all variants of the legacy driver exploited in this campaign.

### Smack my LLM up!
Speakers: Jindrich Karasek
page: https://pretalx.com/hack-lu-2025/talk/YXLGPP/ | slides: /media/hack-lu-2025/submissions/YXLGPP/resources/2025-HackLu-S_XwsUs06.pdf
This session dissects a real-world case study where an actor weaponized automation flaws in Meta’s LLM-based compliance system to hijack high-value accounts via orchestrated botnet abuse, prompt injection, and linguistic manipulation. The attacker exploited vulnerabilities in the very safeguards designed to protect users, triggering account suspension and negotiating “restoration” through AI-manipulated support flows.

This case is not an isolated incident—it is a signal of broader systemic risks that emerge when generative models and automation pipelines are integrated without robust adversarial testing. Beyond the technical compromise, the attack leveraged prompt engineering as social engineering, revealing the cognitive blind spots of model-aligned trust systems.

In response, I introduce foundational forensic linguistic techniques and NLP-based detection methods for identifying AI-generated text in compromised communications. By combining stylometry, perplexity analysis, and syntax anomaly detection in Python, we illuminate detection opportunities hidden in prompts and narrative structure. With few more tips from cloud security area to protect the LLM deployments.
The talk closes with a reflection on the ethical tensions in detecting synthetic media.

This talk will blend live demonstration, code walkthroughs, and operational insights from an investigation that didn’t just uncover an exploit—but a philosophy of misuse. In this talk, I present a forensic case study detailing how a threat actor compromised Meta’s LLM-driven moderation system to systematically hijack verified accounts, using prompt injection, linguistic manipulation, and automation loopholes to trigger platform-enforced takedowns and force ransom-based negotiations. The incident involved a globally active cybercrime network and exposed critical flaws in the trust models of cloud-native AI enforcement systems.

We will walk through the forensic process behind the investigation, analyze prompt-level exploit vectors, and demonstrate how attackers craft model-passing language to elicit beneficial outcomes from black-box systems. Moving from the operational to the analytical, I will also introduce Python-based techniques from forensic linguistics and stylometry that aid in detecting AI-generated text, model hallucinations, and adversarial prompt traces—applicable to both post-mortem analysis and real-time detection pipelines.

Finally, the talk explores the ethical grey zones emerging at the intersection of synthetic content detection, digital identity, and model-assisted enforcement. In the wrong hands, detection tools can become instruments of censorship or control—making it critical to understand both the how and the why behind these systems.

This is a talk for red teamers, detection engineers, AI researchers, and anyone standing at the fault line between automation and abuse.

Audience Takeaways:

Real-world attack path exploiting LLM-based automation in platform support

Techniques for detecting AI-generated text via forensic linguistic analysis

Python-based NLP tools for stylometry and prompt anomaly detection (will share my code)

Ethical considerations around AI-generated content detection in moderation and compliance

Operational guidance for improving LLM security posture in cloud deployments.

### Malware Investigation Pipeline: From Honeypot to Threat Intel
Speakers: Andreia-Irina Ocanoaia
page: https://pretalx.com/hack-lu-2025/talk/7RCD77/
This lightning talk is about **MIP (Malware Investigation Pipeline)** - an automated forensic pipeline designed to extract threat intelligence from Cowrie honeypot snapshots. MIP leverages Dissect for forensic artifact extraction, integrates with VirusTotal to validate suspicious files, and publishes confirmed IOCs to MISP. By automating this process, MIP enables faster and more consistent generation of threat intelligence for collaborative defense.

👉 https://github.com/andreia-oca/malware-investigation-pipeline Threat hunters are frequently faced with large volumes of compromised artifacts that demand fast triage and mitigation. Manual analysis often becomes a bottleneck, limiting the ability to respond effectively at a large scale.

MIP addresses this challenge by automating the end-to-end forensic investigation of QCOW2 disk images collected from Cowrie SSH honeypots. The pipeline extracts relevant forensic data using Dissect, validates findings against VirusTotal, and disseminates verified IOCs to MISP.

### May the world ever again experience such a Christmas night!
Speakers: Christophe Vandeplas
page: https://pretalx.com/hack-lu-2025/talk/TNJYVT/
. .

### Nmap Scanning, Fast and Slow
Speakers: Luc Gommans
page: https://pretalx.com/hack-lu-2025/talk/PAHBU9/
Anyone who ran Nmap with more than a few hosts will have had this experience where the estimated completion time was a few minutes, then days, then years. The tool seems unreliable and slow, why do we keep using it? This lightning talk teaches you how to get Nmap scan results in a quick and calculable amount of time Slides will be published on: https://github.com/x41sec/slides

*Update:* they have been published here: https://github.com/x41sec/slides/blob/master/2025-hacklu/hacklu2025_Nmap-scanning-fast-and-slow.pdf

### Port Mimic: It's a Trap! (And so is every other port)
Speakers: Jürgen Brandl
page: https://pretalx.com/hack-lu-2025/talk/K79YTL/
Port Mimic is a tool that lays out a trap by listening to every port on a given interface. For normal users it will be completely invisible, but as soon as a port scanner comes around, it will turn into a wild beast. ## How it works

Port Mimic uses nftables to set up a trap. It will listen to every port on the given interface and redirect the traffic to a honey port. As soon as a threshold of packets are received on trap ports, it will put the offender on a bad IP list and redirect all traffic to a our mimic program.

So what a attacker will see has nothing to do with the real target, think internet connect teapot or the worlds most welcoming database.

Ideally that will waste their time, alert defenders to set countermeasures or if the machine is connected to the internet, it will muddy the waters and make port scanners less reliable for target discovery.

Listening ports are excluded from the trap, so you don't have to worry about users being affected.

### Credits

This project is inspired by [portspoof](https://github.com/drk1wi/portspoof)

Major differences:
- This project is written in Python and uses nftables to set up the trap, so it doesn't require root or you fiddling with iptables.
- There is no need to manually exclude ports from the trap, it will automatically exclude the ports that are open on the interface.
- The mimic will cover your regular ports as soon as it detects a port scanner, so you don't have to worry about it.
- Instead of opening all ports, we will pretend to be something else, so an attacker will not notice or be alerted to our shenanigans (ideally).

### RANGE42 - An open source cyber range
Speakers: Benjamin Collas
page: https://pretalx.com/hack-lu-2025/talk/UJWRHX/
RANGE42 is an open source modular cyber range project built for real world readiness. Launched a few months ago, it aims to allow teams to design, deploy, and share offensive, defensive and other training environments through reproducible infrastructure-as-code setups.

This talk will briefly present the project's architecture, open-source components and lessons learned while building our collaborative and open source cyber training solution. Discover RANGE42, our open source cyber range project, started a few months ago, aims to turn your on premises infrastructure into realistic hacking and/or defense playgrounds within minutes. 
We'll briefly show what we've built, what we're doing and what we plan to do next.

### Meet Plum, the challenge of your own ASR for free
Speakers: Paul JUNG
page: https://pretalx.com/hack-lu-2025/talk/X9XNMG/
For a medium company, ASR (Surface Surface Reduction) is a good challenge. Of course, A lot of paid services, Shodan, Onyphe, Censis, Qualys...are available. But how to orchestrate your own simple and small recon for less than 25000€ yearly :) ?
Now.. With NIS2, How to do this if you are a National CSIRT. Plum is a young developpement of CIRCL D4 project. With simple agent deployement in mind. The goal of this lighting talk is to talk about the Luxebourgish IP space. 
I will Explain the Challenges of scanning the IP Space. and show some funny results and effective use case that we had after just 2 weeks of production.
But the real goal of this talk is to collect interest, need of people, and why not, some pull request too.

### Open source is a virus
Speakers: Philippe Ombredanne, Prabhu Subramanian
page: https://pretalx.com/hack-lu-2025/talk/PVSLFP/ | slides: /media/hack-lu-2025/submissions/PVSLFP/resources/slides_Jm7ZOU6.pdf
Discover how we hacked YARA and built rules to effectively detect open source software sources and binaries as if it were malware, using rules that you can generate on demand for fun and profit, and integrate software composition analysis with malware hunting! Former Microsoft CEO Steve Ballmer once said that Linux and open source was a cancer. But "developers, developers, developers !!!" know that Linux and open source are not a cancer, but a virus because you can use virus scanning techniques and tools to discover (vulnerable) open source software :)

We hacked YARA to build rules and more effectively detect open source software sources and binaries as if it were malware, generating rules on demand for fun and profit, and integrate software composition analysis with malware hunting!

### Security Monitoring and Response in Large Linux Environments
Speakers: Hendrik Schmidt, Hilko Bengen
page: https://pretalx.com/hack-lu-2025/talk/HBRVAC/
This talk delves into strategies and practices for large-scale security monitoring of Linux systems within enterprise environments. We will explore unique challenges posed by Linux-based infrastructures — from their highly diverse configurations to their widespread deployment across cloud and hybrid landscapes.

We will discuss how we have addressed the need for scalability in our tooling and why integrating our solutions into a SIEM or SOAR platform is critical for effective incident response. Additionally, we will explain why traditional EDR solutions fell short of meeting our requirements and how we instead built a customized, open-source-driven setup leveraging Auditd/Laurel and Velociraptor.

The presentation will begin with an overview of our threat-based logging and response strategy, followed by a deep technical dive into the customizations and enhancements we made to the aforementioned tools — many of which have been shared with the community. Special attention will be given to the asset identification features we added to Velociraptor, enabling us to efficiently operate and respond at scale within complex enterprise environments. .

### Digic8 Oracle
Speakers: laurent clevy
page: https://pretalx.com/hack-lu-2025/talk/3UEDY8/ | slides: /media/hack-lu-2025/submissions/3UEDY8/resources/d8_oracle_hac_VY8EEEp.pdf
# Digic8 Oracle
### Decrypting camera updates without knowing neither the key, nor algorithms (at first)

Since years, Canon cameras firmware has been enhanced by hackers, via the [CHDK] project for Powershot models and [MagicLantern] for DSLR/mirrorless ones, applied to DIY drone photography for example [DRONES].
Starting 2010, the Magic Lantern team is able to execute code by enabling an hidden Canon payload loaded from the SD card : autoexec.bin. Enabling this feature requires forging valid signatures for camera updates, and required the team to fully understand cryptography of these .FIR files. But since the EOS R camera launch in 2018, FIR cryptography changed and no one publicly explored this new FIR version. 

We will introduce the technical context as well as FIR file format version 4 (before 2018), then, we will use :
1 - the fact some recent Canon cameras (R, RP, R6) allow dumping their firmware via an embedded basic interpreter and 
2 - Unicorn emulation to decrypt easily camera update files of the same hardware (Digic) generation, because a unique key is used.

As a first step, emulation will allows access to FIR content (camera firmware updated code), without the need to understand neither the underlying cryptographic algorithms, nor keys : dumped code will be used "as oracle" by emulation. Then we will describe how is working decryption key generation for Digic 8, and finally the scheme of asymnetric signatures and how to verify them for both Digic 8 and Digic 10 cameras.

Two python tools will be released: **d8_oracle.py** to decrypt Digic 8 updates via emulation of dumped firmware, and **d810_verif.py** to verify FIR digital signatures, based on secp256r1 curve.
d8_oracle.py requires you first to dump yourself a firmware via CBasic or to obtain such camera dump via Magic Lantern community for example.

No decryption key neither firmware dump will be released with this talk. 

Laurent Clévy already reversed Canon picture authentication scheme (Original Data Decision in Canon terms) years ago, as well as a python tool to recompute signatures [ODD]. He also rediscovered FIR cryptography before 2018 and described it at BeeRump 2022 [BeeRump]. 

EOS, Digic and Powershot are Canon trademarks.

References:
* [CHDK](https://chdk.fandom.com/wiki/CHDK)
* [MagicLantern](https://www.magiclantern.fm/)
* [DRONES](https://ardupilot.org/plane/docs/common-chdk-camera-control-tutorial.html)
* [ODD](https://connect.ed-diamond.com/MISC/mischs-006/mecanisme-de-controle-d-authenticite-des-photographies-numeriques-dans-les-reflexes-canon)
* [BeeRump](https://www.rump.beer/2022/slides/camera_jailbreak_v2_green.pdf) The presentation will introduce the technical context: what kind of computing platform a recent DSLR/Mirrorless camera is, with several computing units (ARM, Xtensa...) and operating systems (Real time or not). 

Then previous hacking activities on this platform will be described, as well as recent work by Magic Lantern team on EOS R. Next step will describe how a camera update is done, using the FIR file format: 1 - verifiying digital signatures, 2 - decrypting a mini OS version, rebooting on it, then 3 - applying the software updates: writing them in Flash ROM and reboot to main software.

We will explain for the first time how the FIR format is providing confidentiality (AES encryption) and content authentication (based on digital sighatures). Before 2018, signature scheme was based on HMAC-SHA1 with complex key generation. Because the key material was inside firmware and Magic Lantern reversed the whole mechanisms, they were able to forge valid FIR signatures to later launch their payload 'autoexec.bin' in memory. But this changed in 2018 and release of the EOS R model. Do not be afraid, only high level cryptography concepts will be used.

It must be reminded that dumping the firmware of some cameras using an hidden Basic interpreter is possible on EOS R, RP (digic 8 hardware generation), and EOS R5 / R6 cameras (digic 10 hardware). This was discovered years ago on Powershots models. 

The original approach of this talk is to use a dump of the EOS R to decrypt, first, its own FIR updates, without doing deep reverse engineering. We use a trick -because it is more elegant- : by emulating the cryptographic functions embedded in the obtained firmware dump, as an Oracle, almost as black box. 

And because a same decryption key is used for all Digic 8 cameras, our trick will also work for another Digic 8 models. Then our python tool based on Unicorn emulation will be enhanced to also decrypt firmware updates records. This gives access to all Digic 8 camera updates content to port Magic Lantern or other hacking projects for cameras you do not own yourself. The python decryption tool based on emulation **d8_oracle.py** will be released before the talk.

No firmware dumps neither decryption key will be released along this presentation, you'll need to obtain a dump by yourself, which is easy, and we'll explain how.

Because we are not so lazy and you're hopefully curious, decryption and signature algorithms will be explained, and you'll be able to verify yourself ECDSA signatures for Digic8 and Digic 10 camera updates (FIR files) with a dedicated python tool : **d810_verify.py**. Evolution and improvements of the FIR features will also be compared.

Now we can emulate this ECDSA implementation, we can easily study it. Because unless a serious problem, as an asymnetric signature algorithm, it will be not possible to forge valid signatures for recent FIR updates without the private key, which make native code execution on recent camera a problem, as opposite as before 2018.

### The “S” in IoT: Tales from inside the IoT industry
Speakers: Will Moffat
page: https://pretalx.com/hack-lu-2025/talk/GLE99H/
We all know that the S in IoT stands for Security. Despite years of bad press and high-profile breaches, Internet of Things devices continue to hit the market with glaring security flaws. Why do hardware teams fall short? Why don’t consumers seem to care? And what can be done to improve the situation? This talk offers an IoT industry insider’s candid perspective on why the IoT industry treats security as an afterthought.

We’ll start with a review of the IoT landscape, drawing on input from experienced IoT developers in the consumer audio and toy domains as well as from IoT platform developers. We’ll examine the commercial and marketing pressures, the technical “best practices” and the obvious problems of time, money, and available talent.

Next, we’ll dive into a real-world case study: the design and development of a kids screen-free audio speaker developed by a Belgian IoT startup. We’ll explore key business and engineering decisions and their consequences. 

Finally, we’ll look at where the IoT industry is headed, what it would take to nudge it in the right direction, and how the cybersecurity community can help.

### The Parking Chronicles - A DIY Guide to Agents Detection
Speakers: David Sopas
page: https://pretalx.com/hack-lu-2025/talk/YMT98Q/
This talk dives deep into the murky waters of Bluetooth and BLE security. Think those harmless wireless signals are just minding their own business? Think again! David presents a real-world case study that challenges conventional thinking about privacy. He’ll share the unexpected hurdles he encountered while detecting parking municipal agents and his efforts to outsmart them while saving money. This session promises to leave you with a new perspective on the vulnerabilities of everyday wireless technologies. Bluetooth and BLE are everywhere - powering everything from smart devices to parking controllers agents. How secure are these invisible signals we rely on daily? In this talk, we’ll take a deep dive into the lesser-known risks of Bluetooth communication, using a real-world case study that challenges both privacy and device security. Join David as he unpacks his journey of detecting parking municipal agents, uncovering unexpected security challenges along the way. Using practical hacking techniques , this session will make you rethink how "safe" your wireless interactions really are. Whether you're a security professional or just someone who uses Bluetooth every day, you’ll walk away with new insights into how these signals can be detected and exploited.

### What Malware Leaves Behind: Analysing Forensic Traces of Ransomware
Speakers: Ankshita Maunthrooa
page: https://pretalx.com/hack-lu-2025/talk/FJ3JBL/ | slides: /media/hack-lu-2025/submissions/FJ3JBL/resources/Forensics_Pr_iwEob5q.pptx
This session explores the forensic remnants left behind by ransomware on an infected machine. Through a simulated malware infection in a controlled environment, we’ll demonstrate how to uncover the traces attackers leave in system artifacts. Using powerful open-source tools like Autopsy, RegRipper, and Velociraptor, we’ll walk through post-infection analysis, providing attendees with the techniques and insights to detect, correlate, and communicate ransomware behaviors. 
This session would be ideal for DFIR professionals, SOC analysts, and anyone looking to better understand the digital aftershocks of malware. Ransomware attacks have surged in both frequency and sophistication, but even after the malicious code has been executed and removed, remnants of the attack linger. 

This session will delve into the forensic analysis of a ransomware infection, using open-source tools to uncover what happens after the initial compromise.

Through a controlled lab scenario, we’ll simulate the infection of a Windows VM with ransomware, and then use a triage approach to collect and analyze digital artifacts that remain on the system. The primary focus will be on using Autopsy, RegRipper, and Velociraptor to uncover forensic traces and attack patterns, such as:
1. File remnants, including encrypted files, ransom notes, and deleted files.
2. Registry artifacts that could reveal malware persistence techniques.
3. Behavioral artifacts, such as network traffic and execution traces left by the malware.

The session will be split into two parts:

Part 1: Live Demo (5 minutes):
This will include a brief walkthrough of the infected machine, showing evidence of the ransomware attack such as the encrypted files and the ransom note.
It will also include a live demonstration using Autopsy or Velociraptor to extract critical forensic data from the infected system.

Part 2: Post-Infection Analysis (25 minutes):

This part will involve a deeper analysis of the system, explaining how these tools work together to detect and reconstruct the attack. It will answer several questions about post infection analysis like:

- How to correlate the findings across multiple tools (Autopsy’s file-level analysis, RegRipper’s registry examination, Velociraptor’s live endpoint queries).
-Mapping artifacts to attacker TTPs (Tactics, Techniques, and Procedures) using the MITRE ATT&CK framework.

By the end of this session, attendees will gain a solid understanding of what to look for when investigating ransomware incidents and how to use these open-source tools to piece together the story of the attack. Whether you're working in DFIR, SOC, or threat hunting, this talk will provide the practical skills to identify and analyze ransomware behavior through forensic investigation.

### Integrating Zeek With Third-Party Applications
Speakers: Christian Kreibich
page: https://pretalx.com/hack-lu-2025/talk/FEBNLJ/
The Zeek network monitor offers a range of mechanisms to interact with it while up and running. Examples include its ability to asynchronously ingest intel data, exchange Zeek events with custom-built services, call out to web APIs via Javascript, load and save runtime state, and produce operational telemetry. These features provide powerful means to integrate Zeek into an organization's cybersecurity infrastructure, taking it far beyond a mere
producer of network logs.

In this talk I will walk through these features, outline their relative pros and cons, and give examples of real-world applications they enable, including machine learning models, threat intel platforms like MISP, and "round-tripping" of network inventory data. This talk is ideal for users who have gained initial experience with running Zeek, and are looking to get more out of their deployment. Even if you've never used Zeek before, you'll gain a better understanding of what it can provide for your network detection & response infrastructure. (See abstract.)

### The cloud journey 2013-2025 of the European Commission
Speakers: Claus
page: https://pretalx.com/hack-lu-2025/talk/WSLDVZ/
This talk describes the European Commission approach to cloud adoption from 2013-2025 along with stories of the good, the bad and the ugly and how EC has iterated upon its risk appetite and security debt appetite over time. In this talk I will present both how public cloud adoption should be done in 2025 and how EC has done it since day 1 of our experimentation with public cloud starting in 2013. 

The talk will present how you can control the security debt you allow to be created and the plus/minuses of each type of approach.

Then the talk will present the new security framework/paradigm of EC in public cloud and how this has been put in place to address many of the real, measureable threats/risks of public cloud adoption.

### Kaitai Struct: a tool for dealing with binary formats
Speakers: Petr Pucil, Mikhail Yakshin
page: https://pretalx.com/hack-lu-2025/talk/9FBZYF/ | slides: /media/hack-lu-2025/submissions/9FBZYF/resources/Kaitai_Struct_eV3IjI3.pdf
Kaitai Struct is a tool for dealing with binary formats. Binary formats are everywhere: archive files, executables, filesystems, multimedia files, network protocols, etc. If your application needs to read data in a specific binary format, you need a parser that unpacks the bytes into meaningful data structures that you can work with. There are libraries doing that for popular formats, but what if there is no suitable library in your programming language for the format you need? Kaitai Struct has got you covered: it introduces a declarative domain-specific language (based on YAML) for describing the structure of arbitrary binary formats. Format specifications in this language are consumed by a compiler, which generates ready-to-use parsing modules in 12 programming languages (C++, C#, Go, Java, JavaScript, Lua, Nim, Perl, PHP, Python, Ruby, Rust). It is also possible to generate Java and Python modules that support both parsing and serialization (writing structures to bytes in the specified binary format). There are more than 180 format descriptions in the format gallery and hundreds more in various GitHub projects.

This talk will focus on visualization and dumping tools that are part of the Kaitai project: the console visualizer and Web IDE. They are invaluable for debugging file formats, reverse engineering and forensic analysis.

### Utilman & CMD
Speakers: Didier Stevens
page: https://pretalx.com/hack-lu-2025/talk/LKEYFD/
Long time ago, in 2004 (that's even before the first Hack.lu conference), Microsoft released a patch for utilman.exe.
Since then, utilman.exe pops up in security incidents. In 2004, a vulnerability (MS04-019 July 2004) in utilman.exe was revealed.
Turns out utilman.exe runs with SYSTEM privileges.
And any user can just start it by pushing the right keys.
This inspired me in 2006 to turn this feature into a backdoor on Windows XP and blog about it.
And since then, I've been involved in security incidents where this exact technique was used.
Let me share some examples ...

### 101: How to break IPS & SIEM
Speakers: Nicol Dankova
page: https://pretalx.com/hack-lu-2025/talk/MYVUFV/
This story for sure has not happened in a big company 6 years ago, but shares the story of one desperate Security Analyst, who has unwillingly, with help of the Fuckup Fairy, took down major part of security stack.
All the similarities to living people or existing brands are just coincidence or Illuminati :) Have you ever thought, how your situation may look like if:
- SIEM is blowing up & no ghostbusters around?
- NIPS follows RNG freestyle?
- No-one thought about back-ups, because they haven't been buzzwords yet?
And what about if all of this has happened at one moment? :)

### A quick retrospective of a student discovering programming & other failures
Speakers: Sami Mokaddem
page: https://pretalx.com/hack-lu-2025/talk/7FXZPN/
The title says it all .

### All Your CCTV’s are Belong to Us
Speakers: Xavier Mertens
page: https://pretalx.com/hack-lu-2025/talk/RQSWSG/
When we say to people that everything can be hacked and not put « smart » devices online, they don’t trust us. Fail! A true story where an organization has CCTV’s connected to the Internet and they were used to break in and lead to a full compromise with a nice gift: a ransomware.

### Phish Perfect: How I broke the thing while trying to protect it.
Speakers: Melina Phillips
page: https://pretalx.com/hack-lu-2025/talk/SJWVWP/
As a junior SOC analyst, you're responsible for protecting users from potential phishing attacks, so naturally, I did what any overly eager newbie would do, little did I know, internal threats are very much real and they not all stem from malicious intent. - SOC analyst or internal threat? When the call is coming from inside the house.
- Cast and crew: All the people involved, including the lady who nagged me and I didn't even work directly with.
- An oblivious girl's guide to threat hunting and phishing: Incident narrative.
- Save your tears for another day: Owning up to your screw ups.
- Embracing the suck: Lessons learned.

### Analysing the 1991 Lips Eloctro mechatronic lock
Speakers: Walter Belgers
page: https://pretalx.com/hack-lu-2025/talk/RZCBVH/
What happens when a hacker and lockpickers gets their hands on an old electromechanical lock? He's going to look at it of course! The talk contains desoldering, ROM dumping, decompiling and more. What happens when a hacker and lockpickers gets their hands on an old electromechanical lock? He's going to look at it of course! The talk contains desoldering, ROM dumping, decompiling and more.

### Suricata Lua Support
Speakers: Eric Leblond
page: https://pretalx.com/hack-lu-2025/talk/RBTA8A/ | slides: /media/hack-lu-2025/submissions/RBTA8A/resources/Lua_support_i_Cz2OxBC.pdf
History of Suricata Lua support. How it was the greatest thing ever and was not used. An history of Suricata Lua support. How it was the greatest thing ever for detection and custom output but did end up never used.

We will also see how it was also an open door on the system running Suricata.

And finally, will the new implementation fix the issue ?

### The beauty of vibe coding
Speakers: Andras Iklody
page: https://pretalx.com/hack-lu-2025/talk/ZPQFGH/
Trials and tribulations of trying to build an application exclusively via vibe coding Trials and tribulations of trying to build an application exclusively via vibe coding

### The cve-search design failure(s)
Speakers: Alexandre Dulaunoy, Cédric Bonhomme
page: https://pretalx.com/hack-lu-2025/talk/KRNUBT/
I developed cve-search some years ago, and I would like to share the challenges we faced, especially the design failures that ultimately led us to redevelop it as vulnerability-lookup.

I can certainly blame myself for some of these mistakes, but there are also others to blame along the way. I developed cve-search some years ago, and I would like to share the challenges we faced, especially the design failures that ultimately led us to redevelop it as vulnerability-lookup.

I can certainly blame myself for some of these mistakes, but there are also others to blame along the way.

### BurningPanda
Speakers: Ben (@polygonben)
page: https://pretalx.com/hack-lu-2025/talk/7JJNDX/
Each day, adversaries will attempt to exploit operational security failures of organisations, often to steal information or for financial gain. 

Thankfully, these failures are not exclusive to legitimate organisations or businesses. Adversaries often make the same mistakes, and in this talk, we will expose what can happen when such failures occur. What happens when a sophisticated threat actor makes a single, catastrophic, OPSEC failure? 

This session deep dives into the tradecraft of a threat group running an espionage campaign. We'll deliver a technical deep-dive of the recovered infrastructure:

* Emulating C2 - Analysing leaked Cobalt Strike and VShell databases and logs
* Initial Access - Use of novel SQL injection and exploiting vulnerable web-apps
* Tooling Breakdown - Dissecting web-shells and niche tooling
* Timeline - Mapping adversary activity to the timeline and MITRE

Learn how you can recover raw intelligence from the failures of a persistent, non-financially motivated adversary.

### The Heavy Shadow of Imposter Syndrome
Speakers: Tammy Harper
page: https://pretalx.com/hack-lu-2025/talk/TEJRGD/
I want to share my experience with imposter syndrome something many of us in cybersecurity have faced at one point or another, and how it has shaped my career, my approach to threat intelligence, and my relationship with the industry and the people I’ve come to trust and admire. With this talk, I’ll explore how insecurities and belonging coexist in our field, and how confronting that tension has become a source of purpose, empathy, and genuine expertise. The industry loves to celebrate mastery of the perfect exploit, the great attribution, the confident expert who always knows the answer. But for many of us, that confidence is a mask. 

I came into this field late, sideways, and what I was missing in credentials I made with a burning desire to learn a hunger and a work ethic. I didn’t have a degree, or the typical origin story of someone who always “knew they’d end up in security.” 

I arrived with a stubborn case of imposter syndrome. I tried to perform expertise to sound like I belonged among people that had already accomplished and knew so much.

The failure I want to share isn’t one specific catastrophic moment. It’s the slow erosion of your confidence that happens when you let the heavy shadow of imposter syndrome bear it's weight on you. 

Even the most fearsome gangs are performing too. They bluff, break things, and rebuild under new names just like most people in the industry.

In the end, this failure became the best teacher. Because the moment I stopped pretending to be the right kind of expert was the moment I started doing real work.

## 2025-10-22 — Schengen 1 & 2

### Reverse Engineering Ransomware: Hands-On Malware Analysis & IOCs Extraction
Speakers: Ankshita Maunthrooa, Ankshika Maunthrooa
page: https://pretalx.com/hack-lu-2025/talk/DZHMRR/
Ransomware remains one of the most prevalent and destructive forms of malware today. Understanding its inner workings is crucial for defenders and incident responders alike. This workshop will offer a deep dive into reverse engineering ransomware, focusing on practical methods for unpacking and analyzing malicious code.

The Reverse Engineering Ransomware: A Hands-on Workshop is designed to provide attendees with practical experience in analyzing a simulated ransomware sample. The workshop will begin with an introduction to ransomware and an overview of tools such as Ghidra, OllyDbg, x64dbg, Process Monitor, and Wireshark. Attendees will then engage in static analysis using Ghidra to examine the ransomware binary, followed by dynamic analysis in a safe virtual machine environment, where they will observe the malware’s behavior using debugging tools and monitoring software. The session will also cover extracting Indicators of Compromise (IOCs) and documenting the findings in a report. 

Throughout the workshop, attendees will be guided step-by-step, with time for questions, hands-on practice, and discussion. The workshop concludes with a Q&A session and provides additional resources and a whitepaper for continued learning.

Note: A simulated ransomware sample will be provided at the start of the workshop. Attendees are encouraged to bring a laptop with at least 16GB of RAM and a pre-configured VM environment to fully participate in the hands-on analysis. In this practical, hands-on workshop, participants will learn how to reverse engineer a ransomware sample in a controlled, safe environment. By using tools like Ghidra, OllyDbg, and x64dbg, attendees will gain first-hand experience unpacking, analyzing, and understanding the inner workings of ransomware. This workshop will guide participants through static and dynamic analysis techniques, providing valuable insights into malware behavior, payload delivery, and persistence mechanisms.

Here is a detailed breakdown of the session:
- Introduction and Set Up (5 mins)
This will include a brief introduction to the topic: What is ransomware, why is it important to analyze, and how reverse engineering can help with understanding and mitigating threats, with an overview of the tools used (Ghidra, OllyDbg, x64dbg, Process Monitor, Wireshark, Virtual Machines).

- Securely setting up the VM (10 mins)
This will take about 15 mins where attendes can set up their VMs securely along with basic guidelines on creating a safe environment to analyze malware in (e.g., sandboxed Windows VM).

- Introduction to the Ransomware Sample (5 mins)
This will involve a detailed overview of the simulated ransomware sample being used and we will also highlight the types of analysis methods the participants will perform (static vs. dynamic).

- Static Analysis (30 Minutes)
Here I will Introduce Ghidra for static analysis and guide attendees through the process of importing and analyzing the ransomware binary in Ghidra. We will discuss some key features like identifying functions, finding encrypted data, and examining sections of the binary.
We will then perform basic static analysis on the ransomware sample which includes analysis of imports, functions, and strings, encryption routines, command-and-control communication indicators.
Participants are strongly encouraged to follow along and ask questions through the live static analysis process. 

- Dynamic Analysis (30 minutes)
Here, we will quickly introduce x64dbg and OllyDbg for dynamic analysis and explain how these tools can be used to observe malware behavior in a running environment.

Participants will then be guided through launching the malware in the virtual machine, running it, and monitoring its behavior.
This part will explain how to capture memory, file system, and registry modifications during execution as well as show participants how to use Process Monitor to track file system and registry changes.
We will also introduce Wireshark for monitoring network activity during the ransomware’s execution, C2 changes are common during execution and identification of specific packets sent and received would be interesting to note. Attendees will also be taught how to identify key behaviors (e.g., encryption of files, registry changes, persistence mechanisms).

- Analysis and IOCs Extraction (10 mins)
This part will show participants how to extract key IOCs (file names, file hashes, registry keys, network traffic) from the analysis and discuss how these IOCs can be used for detection and response.
Briefly, we will also walk through the process of documenting the analysis and IOCs.
Participants are encouraged to take notes on what they observed and what could be potential signs of compromise.

- Wrap Up and brief QnA with Attendees (5 mins)
Any doubts to clarify for attendees and during the wrap up, attendees will be given a detailed white paper along with how reversing complex malware files like this ransomware works - covering set up of a secure VM to dissecting a malware sample using static, dynamic analysis on the sample and extraction of IOCs that can be used in the detection and response.

### iOS analysis using the Sysdiagnose analysis framework workshop - beginners guide
Speakers: David Durvaux, Christophe Vandeplas
page: https://pretalx.com/hack-lu-2025/talk/ZJSGJC/
Are you, or your organisation, concerned about potential compromise on your iPhone, iPad, or Apple Watch? This workshop equips you with the knowledge and tools to identify red flags on your iOS device. We delve into the world of sysdiagnose and explore methods to verify potential breaches.

This is the starter workshop, we invite you to also join the second deeper dive session with deeper analysis. This is an iteration of the workshop that was given at hack.lu 2024. This edition is now split in two sessions: one introductory session and one deep dive.

Are you, or your organisation, concerned about potential compromise on your iPhone, iPad, or Apple Watch? This workshop introduces you to some knowledge and tools to identify red flags on your iOS device. We delve into the world of sysdiagnose and explore methods to verify potential breaches.

During this workshop we will be:
- discussing some ways to know if an iOS device may be compromised
- explore which opensource tools exist to perform analysis
- generating a sysdiagnose file on an iPhone, iPad iWatch, ... (bring your own device)
- use multiple methods to collect the sysdiagnose (sharing, custom app, PyMobileDevice3, ...)
- use the open source sysdiagnose parser to convert the diagnostics data to something usable 
- explore what data it contains
- generate a timeline and load it in timesketch or splunk
- ...

## 2025-10-22 — Hollenfels

### Threat detection engineering with Suricata
Speakers: Eric Leblond, Peter Manev
page: https://pretalx.com/hack-lu-2025/talk/YKHLRJ/
This hands-on workshop provides an in-depth exploration of advanced techniques for maximizing network threat detection using Suricata. This session delves into critical areas such as effective utilization of metadata keywords, including MITRE and regular metadata, to enrich detection context. The workshop will also cover leveraging the Suricata Language Server (SLS) for rule development and optimization, including interpreting performance hints and implementing Continuous Integration (CI) for rulesets using SLS in batch mode. This hands-on workshop provides an in-depth exploration of advanced techniques for maximizing network threat detection using Suricata. Building upon core Suricata capabilities, this session delves into critical areas such as effective utilization of metadata keywords, including MITRE and regular metadata, to enrich detection context.
Participants will learn practical methods for achieving fast Indicator of Compromise (IOC) matching and strategies for managing multiple Suricata versions within diverse environments. The workshop will also cover leveraging the Suricata Language Server (SLS) for rule development and optimization, including interpreting performance hints and implementing Continuous Integration (CI) for rulesets using SLS in batch mode. Finally, live measurement of signatures performance will also be experimented with to see how it is possible to detect signatures impacting the overall performance of sensors.
This session is designed for cybersecurity professionals seeking to enhance their Suricata expertise and implement cutting-edge threat detection strategies. Attendees will leave equipped with actionable techniques and practical examples to improve their organization's security posture through better description.

### When Netflow meets Pcap - A network forensic approach.
Speakers: Peter
page: https://pretalx.com/hack-lu-2025/talk/ZJTDKJ/ | slides: /media/hack-lu-2025/submissions/ZJTDKJ/resources/2025_hacklu_N_z4HAoDs.pdf
Working with netflow data in incident handling has a big advantage, as it reduces the data size remarkably. This comes at the cost of loosing package payload information. What if we try to combine the best of both worlds and have a tool that does that approach?
The workshop explains this approach and gives the students real life hands-on examples. The workshop introduces a new type of network forensics with netflow and pcap. This workshop explains the approach to merge netflow and pcap data and presents the advantages.
The student will have the option for a hands-on experience to work with real data. 
It is expected that students have basic skills with Linux and the command line.

Topics:
- Theory and usage of netflow.
- Working with nfdump primer.
- Using the nfdump toolset to prepare and process large pcaps.
- Enrich the netflow data with 3rd party information. ( Geolocation, Tor)
- Search for network artefacts.

### In bed with Qubes OS - tips & tricks exchange party
Speakers: William Robinet
page: https://pretalx.com/hack-lu-2025/talk/KDUDVC/
I've been using Qubes OS in my professional life since 2017 (version 3.2).
With this workshop, I want to share my experience working daily with it, then initiate an exchange around the various topics involved, including security benefits and technical difficulties. When presenting at conferences, there is always someone who notices that I'm running Qubes OS on the laptop I use for presentations.
From that point, the subject of my talk or workshop is set aside and the rest of the discussion shifts around my usage of Qubes OS.
Let's use this workshop as an opportunity to talk about Qubes OS. You can bring your own Qubes OS setup, and we'll share our respective tips & tricks.

After a quick intro, I'll share some tips & tricks I use and I'll talk about some issues I'm still facing.

## 2025-10-22 — Vianden & Wiltz

### Back to basics - Exploring OpenSSH: hands-on workshop for beginners
Speakers: William Robinet
page: https://pretalx.com/hack-lu-2025/talk/GMJD3B/
This workshop is intended for novices who want to improve their practical knowledge and experience with OpenSSH. During this workshop, you will learn how to use the various tools from the OpenSSH suite. We will start with a presentation of the problems that are solved by OpenSSH, then we will dive into the details of its most important and useful features. Among the topics covered, we will discuss about remote host authentication, password and public key client authentication, key generation, local and remote port forwarding, forward and reverse SOCKS proxying, X11 forwarding, jumphosts, connection to legacy systems, and more.

Hands-on exercises will be proposed throughout the exploration of the tool suite using real-life scenarios. There will be space for questions and discussion.

Basic networking and Linux shell knowledge are required in order to follow this workshop. Each participant will need a Linux machine (on which they have root access) with Docker pre-installed and Internet access.

### New advanced network detection with Suricata 8
Speakers: Eric Leblond, Peter Manev
page: https://pretalx.com/hack-lu-2025/talk/WVSUHB/
Suricata is a high performance, open source network analysis and threat detection software used by most private and public organizations, and embedded by major vendors to protect their assets. Suricata provides network protocol, flow, alert, anomaly logs, file extraction and PCAP capture at very high speeds.

This hands-on training will focus on a few new and ground breaking detection additions of the new Suricata 8 release, like transactional rules, data/datajson sets, new protocols and keywords available such as entropy matching. Suricata is a high performance, open source network analysis and threat detection software used by most private and public organizations, and embedded by major vendors to protect their assets. Suricata provides network protocol, flow, alert, anomaly logs, file extraction and PCAP capture at very high speeds.

This hands-on training will focus on a few new and ground breaking detection additions of the new Suricata 8 release, like transactional rules, data/datajson sets, new protocols and keywords available such as entropy matching.

The training will also cover threat detection engineering by showing how the rules language can be used to add the maximum of useful context to the detection events. 

The training will cover actual use cases and the detection benefits of the new features in Suricata 8 alongside with examples that trainees can take away and readily implement at home or work.  The training will also showcase features that provide for substantial detection and deployment improvements in  terms of time and management in digesting shared threat intelligence. We will also review the new features and their benefits with actual malware pcap traces - providing direct mapping of some of the new features and their usability to actual detection. 

Attendees can expect to leave with new knowledge , actual use cases and detection deployment techniques that can be implemented right away to give an edge over the adversaries.

### Collaborative Detection Engineering with Rulezet: Building a Trusted Community for Detection Rules
Speakers: Cruciani David, Théo Geffé
page: https://pretalx.com/hack-lu-2025/talk/9D8WSE/
As threat landscapes evolve, managing and trusting detection rules has become as critical as creating them. Detection engineering teams struggle with rule duplication, inconsistent quality, false positives, and the lack of a trusted, community-driven repository to share validated rules.

Rulezet is an open-source framework and platform designed to address these challenges. It provides a unified way to normalize, validate, and manage detection rules across multiple formats while fostering a collaborative ecosystem where rule authors, analysts, and engineers can review, evaluate, and improve detection logic together. As threat landscapes evolve, managing and trusting detection rules has become as critical as creating them. Detection engineering teams struggle with rule duplication, inconsistent quality, false positives, and the lack of a trusted, community-driven repository to share validated rules.

Rulezet is an open-source framework and platform designed to address these challenges. It provides a unified way to normalize, validate, and manage detection rules across multiple formats while fostering a collaborative ecosystem where rule authors, analysts, and engineers can review, evaluate, and improve detection logic together.

In this 90-minute workshop, we’ll explore how Rulezet enables a community-based approach to rule management — from initial authoring to peer review, version control, and false-positive tracking. We’ll examine how the Rulezet core engine parses and validates rule formats, ensuring consistency and interoperability across detection tools. Participants will also learn how to extend Rulezet with new rule types, interact with its API, and contribute to the Rulezet.org community — a shared repository of trusted detection rules.

Through live demos and discussion, we’ll address practical aspects such as:

- How to reduce false positives through shared rule reviews and metadata enrichment.
- How to establish trust and transparency via verifiable rule origins and author reputation.
- How to evaluate parsing quality and conversion accuracy across formats (e.g., Sigma, YARA, Suricata).
- How to integrate community-reviewed rules into your SOC pipelines securely and efficiently.

Whether you are a detection engineer, SOC analyst, or open-source contributor, this workshop will show how Rulezet can help you build confidence in detection logic, enhance collaboration, and shape the future of trusted detection rule sharing.

## 2025-10-22 — Echternach & Diekirch

## 2025-10-22 — Fitness room

### yoga for geeks
Speakers: Georges Kesseler
page: https://pretalx.com/hack-lu-2025/talk/LAM9EX/
Get your day started with a nice intensive yoga session. Based on ashtanga yoga, this is a good physical exercise. Beginner friendly, no previous knowledge of yoga needed. Some yoga mats are provided, if possible, bring your own. Don't forget your towel! There will be no spritual chanting, energy flows or chakra opening. Just well executed exercises aimed towards IT engineers.

## 2025-10-23 — Europe

### Nightmare on NTLM street: Legacy’s Revenge
Speakers: Marina Bochenkova
page: https://pretalx.com/hack-lu-2025/talk/7KCT7N/
We know the world runs on legacy. We know it’s not supposed to. But when vendors or LinkedInfluencers command us to phase out old systems and protocols, it sometimes seems like their expectation-versus-reality connection is faulty. 

This talk will walk you through the ~adventure~ of disabling a recently-deprecated Microsoft authentication protocol with numerous security problems: NTLM. 

For decision-makers, this is an opportunity to better understand the struggles of on-the-ground IT and security teams trying to bring outdated systems in line with industry standards. For IT and information security peers, this presentation will share valuable resources and “lessons learned” for successfully phasing out NTLM (and similar thorns-in-sides) within their own organizations. Microsoft introduced NT Lan Manager in 1993 as a replacement for LANMAN, born in 1987. Just seven years later, they announced Kerberos as the default replacement for NTLM and instructed companies to stop using it. No one did. Now, in June 2024, Microsoft has announced the deprecation of the entire NTLM authentication protocol family, and even removed older versions from newer OS versions. 

Why is this legacy protocol still so widely used, 24 years after it stopped being the default replacement? The answer is a combination of factors, some of which this talk will explore:
- corporate communication and decision-making
- application development lagging behind security standards
- flaws in the replacement protocol
- underfunded, understaffed, and overwhelmed IT teams

Having completed this project in the IT environment of a mid-sized enterprise, this presentation will also discuss resources and lessons learned that could help get the job done elsewhere. It will also illustrate to those outside the field why IT and security are critical business functions, not cost centers.

### Compromising Threat Actor Communications
Speakers: Ben (@polygonben)
page: https://pretalx.com/hack-lu-2025/talk/ZXFEEV/
This talk exposes how a simple OPSEC mistake—a threat actor testing malware on his own production system—can unravel an entire cybercrime operation. By intercepting Telegram-based C2 communications, we’ll uncover the inner workings of infostealers, reveal infrastructure details, and discuss how these real-world insights can reshape threat intelligence and defensive strategies. In this talk, I will dive deep into a case study where a threat actor's critical OPSEC mistake—testing his own keylogging and infostealing malware on his production hacking machine—opened an unprecedented window into a live cybercrime operation. 

I will detail how intercepting Telegram-based C2 communications allowed me to obtain over 100 screenshots and logs that reveal not only the mechanics of the malware but also the underlying infrastructure and tactics of the threat actor. The presentation will cover the entire lifecycle of the malware’s communication strategy, from the initial setup using Telegram BotFather and the subsequent embedding of bot tokens in malware, to the automated analysis leveraging VirusTotal and custom YARA rules to hunt down samples communicating with Telegram’s API. 

I will explain how, through this process, I was able to extract and analyse bot tokens to forward stolen communications, map the associated backend infrastructure and link various elements of the operation to broader phishing and malware campaigns ran by the actor. The session will highlight both the technical aspects of exploiting trusted communication platforms like Telegram and the implications for threat intelligence, offering insights into how such vulnerabilities can be turned against adversaries to disrupt their operations and enhance proactive defence measures. 

This detailed exploration not only exposes the inner workings of a low-tier cybercriminal operation but also provides actionable lessons on the importance of robust operational security in defending against malware campaigns.

### Instrumenting software builds to detect stealth backdoors and other curiosities
Speakers: Hilko Bengen
page: https://pretalx.com/hack-lu-2025/talk/UZ87X9/
The backdoor that had been added to xz-utils by an unknown threat actor (CVE-2024-3094) may be seen as a wakeup call in that too little attention is being paid on what happens behind the scenes in our software build processes. When we type `./configure && make`, `cargo build`, `pip install` or similar chants into our terminals or CI pipelines, we expect that magic happens and that we get software artifacts that Just Work.
Given the right instrumentation tools, it is possible to observe what actually happens during the build process of most software packages and in most cases we can infer whether a binary has actually been built from the presented sources as we expect. It is also possible to detect abnormal uses of compilers or linkers.
I will present a Linux-based prototype toolset for generating and analyzing those lower-level build logs and discuss curious findings and limitations of the approach. .

### Attacking The Developer Environment Through Drive-by Localhost Attacks
Speakers: Joseph Beeton
page: https://pretalx.com/hack-lu-2025/talk/R8FMHK/ | slides: /media/hack-lu-2025/submissions/R8FMHK/resources/driveby-1_k2a2Qig.pptx
There is a widespread belief that services that are only bound to localhost are not accessible from the outside world. Developers for convenience sake will run services they are developing configured in a less secure way compared to how they would (hopefully!) do in higher environments.
By compromising websites developers use, just injecting JS into adverts served on those sites or just a phishing attack that gets the developer to open a web browser on a compromised page, it is possible to reach out via non pre-flighted http requests to those services bound to localhost, by exploiting common misconfigurations in Spring, or known vulnerabilities found by myself and others. I’ll demonstrate during the talk, it is possible to generate a RCE on the developer’s machine or other services on their private network.
As developers have write access to codebases, AWS keys, server creds etc., access to the developer’s machine gives an attacker a great deal of scope to pivot to other resources on the network, modify or just steal the codebase. The talk will go into detail about the underlying issues with this vulnerability type. How it is possible for Javascript loaded from a website can access localhost. What limitations there are and how this feature can be used to attack unsuspecting users, especially software developers. Including a way to gain Remote Code Execution on  Quarkus ( a popular Java Web framework ) Developers machines and older versions of Spring and a way to exfiltrate AI Training models from users of the popular machine learning software MLFlow, all found by me and there are likely many more similar issues out there.
Also what browser makers are doing about this class of vulnerability and how it will soon be no more, but for now is still a major, but relatively unknown attack vector.

### One day at the Internet Storm Center
Speakers: Xavier Mertens
page: https://pretalx.com/hack-lu-2025/talk/C9ZDAR/
Born in 2001, the Internet Storm Center (or ISC) is a volunteer-driven threat-monitoring and early-warning program that evolved out of Incidents.org and the DShield consensus intrusion-log project. Leveraging a distributed network of sensors that now contributes tens of millions of firewall and IDS records each day, the ISC correlates this data to track “storms” of malicious activity, publishes a real-time Infocon threat level, and releases daily “Handler Diary” blog posts and a short Stormcast podcast to brief defenders on the latest vulnerabilities, exploits, and malware campaigns. About 40 volunteer handlers spread across several countries analyze submissions, craft tools, and coordinate community response, making the ISC one of the longest-running open sources of actionable situational awareness for incident responders and network operators worldwide. During this presentation, I'll show you the data that we collect and make available to api, mainly through our API. I will also introduce our worldwide honeypot network (and how easily you can join it to share more data). The idea of this talk is to make people aware of the data we offer and how you can benefit from it in your day to day hunting tasks. How the ISC works, what are the tools we provide. And, if you're interested, how you can apply to become a Handler! I'll also demonstrate live (if Demo God is with me) some cool honeypot features we have.

### Field guide to physical attacks against full-disk encryption
Speakers: Edouard D'hoedt, Hayk Gevorgyan
page: https://pretalx.com/hack-lu-2025/talk/H8JV8A/
How safe is your “encrypted” laptop when someone walks off with it?

Full-disk encryption (in particular BitLocker) is now standard on Windows 11 machines, silently protecting everything from corporate endpoints to personal devices. But in the real world, does it truly hold up against physical access attacks?

This session is for defenders, red teamers, and anyone who’s ever been handed a laptop and told, *“Don’t worry, it’s encrypted.”* This talk is a 2025 field guide into practical techniques to bypass BitLocker, drawn from our own hands-on experience during real-world red team engagements, using publicly documented attack techniques.

We will focus on what actually works in the field, setting aside the techniques that are too hardware-specific, outdated and patched, or only achievable under lab conditions.

Along the way, we will break down how BitLocker works under the hood, covering key components like the TPM, boot process, and key management, and give context for the following attacks:

- TPM sniffing
- Direct Memory Access (DMA)
- Bitpixie

We will also take a reality check on more exotic vectors like cold boot attacks and Intel DCI. We will walk through where these techniques worked for us in practice, where they failed, and what challenges we encountered along the way.  

Red teamers will learn quick, effective methods for gaining initial access and privilege escalation on end-user devices. This will be supported by insights into tooling, setup requirements, reliability, ease of execution, and post-exploitation considerations.

Blue teamers will come away with a realistic view of the current risks and threat landscape, along with an overview of available mitigations, including those introduced by Microsoft and hardware vendors in recent years.

A live demo will illustrate the practical impact of one of the featured attacks and reinforce the importance of context-aware defenses.

### My other ClassLoader is your ClassLoader: Creating evil twin instances of a class
Speakers: Dimitrios Valsamaras
page: https://pretalx.com/hack-lu-2025/talk/CHMH78/ | slides: /media/hack-lu-2025/submissions/CHMH78/resources/My-other-clas_Djir1af.pdf
The class loader is a fundamental component of the Java Virtual Machine, responsible for dynamically loading classes into an application's memory during runtime. The functionality of class loaders is outlined by the abstract ClassLoader class, with the PathClassLoader and DexClassLoader being some common implementations in the Android OS.

In the context of data transfer and object management, dynamic class loading becomes particularly relevant when dealing with Serializable and Parcelable objects, as the ClassLoader implementation plays a crucial role in reconstructing them. However, while the Android security model enforces isolation among running processes, nothing prevents an application from creating and maliciously using objects of another app. In fact, the practice of storing application resources and their code in world-readable directories, eases this process, since it allows any app to "borrow" the context of another and create class loader instances that can be used to construct Java objects with potentially unsafe content.

Android developers often overlook this contingency, placing undue trust to Java objects received from untrusted sources. In a typical scenario, an application handles such objects, without proper caution regarding their encapsulated data. Depending on the use of this data, such an oversight can lead to unpredicted behavior and under some circumstances, it can have serious security implications.

In this study, we demonstrate techniques and explore how third-party applications, without requiring any permission, can leverage the outlined behavior to craft and dispatch parcelable Java objects with malicious content, to other applications. We further illustrate, using practical examples, the severe security implications that this may have, underscoring the necessity for more vigilant and comprehensive security practices in Android application development. Presentation Outline

- Java Class Loaders and their types: In this introductory part I am going to provide the audience with a clear, high-level understanding of Java class loaders, explaining their fundamental role in the context of a JVM. We will explore the diverse types of class loaders and touch on the parent-child relationship and delegation model that forms the basis of how they work. Additionally, given that Java reflection is an integral component of class loaders, I will conclude this section by providing an overview of this concept. This will include explaining its fundamental principles and demonstrating its basic applications in practical scenarios. 

- Android ClassLoader implementations: Here I am going to dive deeper into the specific implementations unique to the Android OS. The presentation will center on the most critical ClassLoaders in this context, including the PathClassLoader, DexClassLoader and InMemoryDexClassLoader and touch concepts like the Android's hidden API. 

- Parcelables and Serializable objects, in the context of inter-process communication: In this segment, I will explore the concepts of Parcelable and Serializable objects in Java, focusing on their implementation methodologies and key distinctions. My discussion will extend to their applications in inter-process communication, with a particular focus on security considerations tied to their usage. To illustrate this, I will highlight the CVE-2020-8913 example, providing a real-world context to the concepts discussed. 

- "Borrowing" other application's code: In this part, I plan to guide the audience through the methods available for importing code from other Android applications into an Android Studio project. We will look at how to effectively integrate external code, emphasizing the practical steps and considerations involved in this process. 

- Utilizing the /data/app Folder: While importing code from other apps at compilation time is feasible, this approach can often be complex and fraught with challenges, such as resolving package class conflicts. However, Android stores application resources and code in world-readable directories during the installation process, significantly simplifying the "borrowing" process, described above. One effective method involves using createPackageContext, which, when provided with a package name, returns a context identical to that of the named app at launch, including its resources and class loader. Based on this, I will demonstrate how to instantiate Java objects from another application's private domain, showcasing a more streamlined approach to leveraging external code resources. 

- Creating parcelable evil twins: As previously mentioned, a common oversight among Android developers is the public readability of their application's class loader, coupled with an implicit trust in parcelable or serializable objects from untrusted sources. In this segment, I will walk through real-world case studies where such blind trust has led to significant security vulnerabilities.  

- Closing remarks: As I conclude this briefing, I will highlight the need to avoid receiving and un-marshaling parcelable or serializable objects outside of an app's private sphere. While sometimes this practice may be unavoidable, especially with system-related objects, I will leave the audience with essential insights on how to effectively safeguard Android apps against such types of attacks.

### Building a pipeline to analyse iOS devices at scale
Speakers: David Durvaux, Christophe Vandeplas
page: https://pretalx.com/hack-lu-2025/talk/CMHBFT/ | slides: /media/hack-lu-2025/submissions/CMHBFT/resources/hacklu-confer_ovqSVMQ.pdf
# Building a pipeline to analyse iOS devices at scale

## Overview and Abstract

This talk will show how the DG DIGIT is bulding a pipeline to analyse devices at scale relying on 2 key pieces:
1. The sysdiagnose analysis framework developed jointly with CERT-EU.
2. A toolset to collect artifacts over the air via a self-developped App (in collaboration with an independent security researcher) or Computer app on a PC.  The self-developped app is now available on all EC-owned devices.

Globabally this is a part of a larger "mobile cybersecurity programme" which is a deliverable of the European Commission Cybersecurity Strategy.

The presenters will share with the audience hands-on experiences and share what works and what does not work with this approach.

Incident responders will leave the talk with a deeper understanding of Sysdiagnose and a novel tool in their IR arsenal. # Building a pipeline to analyse iOS devices at scale

## Overview and Abstract

This talk will show how the DG DIGIT is bulding a pipeline to analyse devices at scale relying on 2 key pieces:
1. The sysdiagnose analysis framework developed jointly with CERT-EU.
2. A toolset to collect artifacts over the air via a self-developped App (in collaboration with an independent security researcher) or Computer app on a PC.  The self-developped app is now available on all EC-owned devices.

Globabally this is a part of a larger "mobile cybersecurity programme" which is a deliverable of the European Commission Cybersecurity Strategy.

The presenters will share with the audience hands-on experiences and share what works and what does not work with this approach.

Incident responders will leave the talk with a deeper understanding of Sysdiagnose and a novel tool in their IR arsenal.

A detailed explanation of what we will present is outlined below.


## Intended audience

Incident handlers and forensic investigators. 


## Introduction

For a long time, the incident response analysis of iOS devices has been... essentially challenging. 

While an analyst is usually interested in understanding what the system was doing (system logs), typical acquisition tools usually imply collecting users' data. Thus, they are very privacy invasive and due to the amount of information often do not provide what the incident responder was looking for. Furthermore, the common way to get access to the full device is by exploiting Operating System (OS) vulnerability either by manual jailbreaking techniques or by using specialised (expensive) tools reserved for law enforcement. Both have the downside of breaking the integrity of the device. Therefore, the trust in the final state of it as well as the potential impact on certain OS artefacts.

### Enter Sysdiagnose...

This talk will focus on repurposing an Apple feature ("sysdiagnose") which was originally intended for diagnostic and debugging purposed for developers as well as for repair shops.  The Sysdiagnose process on Apple devices collects data on how the system behaves and is typically what an analyst wants to look at.

This approach was validated in 2021 by Amnesty Internal as a way to discover Pegasus on Apple devices.

### Scaling up...

Being able to analyse the sysdiagnose files was a first step, but like for law enforcement acquisitions, it lacks the automation of handling more than a handful of devices.  In this talk, we will also cover how we build our toolset to be able to cope with an significant amount of devices. To us, large scale analysis is key to identify APT compromission of phones.


## Collecting Sysdiagnose artefacts

Sysdiagnose is triggered by a user action and creates archives containing system information in various formats, such as:
* plist configuration files
* logs and output of commands
* sqlite databases with application histories
* etc.

The result can be extended by pushing extra profiles to the device that turn on extra debugging and enhance the content of the archive.


### Collecting Sysdiagnose archives on iOS

While the process is well described on Apple's website, we will quickly show how to start the acquisition process on an iPhone and how to copy over the dumps via a few different techniques ranging from AirDrop to typical forensic tools.


### Collecting Sysdiagnose archives on other Apple devices

While the research motivating this talk stems from the need to analyse iOS devices, in practice the features which we are looking at will be available throughout all of Apple OSes:
 * Mac OS (MacBook Air, MacBook Pro, Mac Pro, iMac...)
 * Watch OS (Apple Watch)
 * iPad OS (for tablets)
 * TV OS (Apple TV)
 * ...


### Collecting at scale

We will demonstrate how we have reach the next level by freeing ourselves from the usual toolset to build an automated pipeline.

The very first topic we tackled was to enable all potential actors with the required tooling to collect artefacts. Starting by:

- Empowering end users whose mobile devices are registered in our Enteprise Mobility Management (EMM) no matter where they are located, by making available a mobile App into our EMM Application Store to guide them into generating the sysdiagnose file and sharing it with us for analysis;
- (work in progress) And empowering IT Helpdesk with a computer application that will help them to support end users to collect extended diagnostic information (beyond Sysdiagnose) from their mobile devices and share it securely with us.


## Extracting information from Sysdiagnose archives and building a timeline

In this part we will present an Open Source analytical framework to extract all timestamped information from the Sysdiagnose archive in order to build a timeline in your favorite timeline analysis tool.  The framework was enriched over the last year with many new parsers and extended analysis modules.  

We today mostly rely on two ways to do a timeline analysis:
- via Splunk which allow to query all timeline at once;
- via Timesketch thanks due to a dedicated analysers.

We complement the absence of certain information in the timeline with dedicated analysers that focused on specific tasks.

The framework went under a complete refactoring since January 2024 and now includes
- 38 parsers (to parse specific logs contained in the sysdiagnose archive);
- 10 analysers (to conduct specific analysis)

We are also planning to offer a Jupyter Notebook to directly interact with the framework and equipped the analyst with a place to quickly build and test queries.


## Future Work
 
We will talk about needed further research and launch a call for collaboration.  All the tools demonstrated are or will be released under the European Public License (EUPL).


## Note

This work can be presented as a presentation or as a workshop empowering audience to play with the tool directly.

### ICRC's Trust and Safety: Armed Conflict
Speakers: Vitaly Savenkov
page: https://pretalx.com/hack-lu-2025/talk/K9YUQB/
The International Committee of the Red Cross (ICRC), which works to help the victims of armed conflicts across the globe, wants to pitch its engaging product - Trust & Safety: Armed Conflict - a browser game about exploring the difficult choices a social media company should make in a conflict and crisis situation. The International Committee of the Red Cross (ICRC) in collaboration with Leveraged Play and the Copia Institute present the "Trust & Safety: Armed Conflict" interactive game, which immerses players in the role of a Conflict & Crisis Team within a fictional social media company. It challenges users with complex, real-world-inspired scenarios that technology companies face when their platforms are used during armed conflicts. Players must make difficult decisions that impact local communities affected by the conflict, humanitarian actors that come to their aid, as well as the company’s public image and operational integrity.
 
The game ultimately aims to raise awareness on the various challenges that tech companies and broader ecosystem can encounter in times of conflict. It highlights the need to protect vulnerable populations, and to safeguard a space for neutral and independent humanitarian action, while underscoring the role of responsible digital governance.

### OpenTIDE - When TI made actionable drives your Threat Detection
Speakers: Remi Seguy
page: https://pretalx.com/hack-lu-2025/talk/NMTJJE/ | slides: /media/hack-lu-2025/submissions/NMTJJE/resources/Hack.lu_2025__fJtiGVM.pdf
With [OpenTIDE](https://github.com/OpenTideHQ), turn threat intelligence into actionable objects, drive and prioritise your Threat Detection graph and embrace Detection-as-Code If
 - you would like to manage your threat detection better than using a flat list of rules and some links to  ATT&CK techniques to be able to report using an ATT&CK navigator layer.  

- you would like to be sure that the top threat vectors relevant for your organisation are covered by detection and have the documentation maintained automatically.

-  you would like to embrace Detection-as-Code and **from a single place of truth** automatically deploy on your different platforms (including multi-tenants) 

have a look at [OpenTIDE](https://github.com/OpenTideHQ) and watch the lighting talks

### These Hackers Fucking Suck
Speakers: Ben (@polygonben)
page: https://pretalx.com/hack-lu-2025/talk/XUTHTZ/
This talk will show how we turned the tables on a few online criminals and used their mistakes against them. We'll share how we found these errors, the intelligence we gained, and how you can start hunting down sloppy cybercriminals yourself. In our day job, we're constantly responding to real-world attacks and observing the impact they have on businesses and individuals. But in our free time, we take the fight to the adversaries by hunting down their infrastructure, gathering intelligence, and alerting victims.

This talk will show how we turned the tables on a few online criminals and used their mistakes against them. We'll share how we found these errors, the intelligence we gained, and how you can start hunting down sloppy cybercriminals yourself.

### Tools to streamline creation of technical presentations
Speakers: Kirils Solovjovs
page: https://pretalx.com/hack-lu-2025/talk/7KJPK7/
This lightning talk introduces presentation-toolkit, a collection of Linux  command-line tools for creating charts, extracting colors, and processing images - designed to make presentation visuals reproducible, scriptable, and easy to integrate into developer workflows. In five minutes, I’ll show how these small utilities can automate the way we build and update technical slides.

I'll start by sharing tips to get an effective presentation setup going.

### Decrypting IIS Backdoor Traffic
Speakers: Didier Stevens
page: https://pretalx.com/hack-lu-2025/talk/QHN7WB/
A method will be presented to decrypt the HTTP(S) C2 channel of an IIS backdoor developed by an APT group reportedly linked to the People’s Republic of China. Encrypted C2 traffic can hide attacker activity in plain sight. This talk shows a practical method to decrypt the HTTPS communication of an IIS backdoor, revealing how the malware operates and how defenders can analyze it.

### 5 years collecting CyberSecurity tools
Speakers: Jonathan Scoupreman
page: https://pretalx.com/hack-lu-2025/talk/PRUKPV/
Over the last five years, our French-speaking cybersecurity community shared 730+ open-source tools from CTFs, conferences, blog posts, and daily work, but they became buried in Discord chat histories. This lightning talk introduces tooldump.eu, a centralized platform that transforms lost GitHub links into a searchable repository, making it easy to quickly find the right tool for any security task. Active cybersecurity communities face a common challenge: valuable tools shared during CTFs, conferences, conversations, and research get lost in endless chat logs. After five years of running a French-speaking cybersecurity community, our Discord held hundreds of tool recommendations that were nearly impossible to retrieve. I built tools.dysnome.eu to solve this. In this lightning talk, I'll show how I transformed our chaotic chat history into a structured database of 730+ tools, enriched with GitHub API metadata, enabling quick discovery through categories and tags. Find the right tool for your investigation or threat hunting needs in seconds, not hours of scrolling.

### Revisiting Widevine L3: DRM as a playground for Hackers
Speakers: Felipe Custodio Romero
page: https://pretalx.com/hack-lu-2025/talk/CKHV3K/ | slides: /media/hack-lu-2025/submissions/CKHV3K/resources/Widevine_Talk_F0t7Qr5.pdf
This presentation will provide an in-depth look at a legacy version of Widevine L3, Google's software-based Digital Rights Management (DRM) system. Despite its widespread use in streaming services, often for low-definition content where its software-only nature is deemed sufficient protection, Widevine L3 has faced numerous public compromises. We will demonstrate how partial emulation can be practically applied to perform Differential Fault Analysis (DFA), breaking the system's root of trust. The talk will conclude with a detailed walkthrough of deobfuscating the Widevine L3 codebase to enable the generation of custom keyboxes. I always wondered how exactly pirates are able to get their hands on the latest shows from major streaming providers. This curiosity led me on a deep dive into the complex world of Digital Rights Management (DRM).

For this presentation, I will focus on Widevine, Google's widely deployed DRM system, specifically its software-only version, Widevine Level 3 (L3), which is more accessible for analysis and has a history of public compromises. From a tweet by security researcher David Buchanan in 2019, I learned that Widevine L3's white-box AES implementation was susceptible to Differential Fault Analysis (DFA). This presented a unique opportunity to not only explore a real-world DRM system but also to gain practical experience in applying this powerful cryptographic attack. And while we are at it, perhaps we can gain some insights by reversing their legacy version that remain applicable to current implementations.

### The Human Factor: Psychological Safety in Cybersecurity Frontlines
Speakers: Cris Brafman Kittner
page: https://pretalx.com/hack-lu-2025/talk/FYMBWY/
Cybersecurity isn't just about technology; it’s fundamentally about people. Cybersecurity's human element is undeniable. It is not merely about firewalls and code; it's a human game.  Recognizing the link between psychology and psychological safety in cybersecurity frontlines, particularly within incident response, is crucial. Enough with the blame game! We need a culture where taking risks, sharing ideas, and learning from failures are actually rewarded and recognized for their contribution to an organizations’ overall success. 

Cultivating psychological safety can be challenging, especially in high-stakes environments like cybersecurity incident response. Building this environment isn't easy. It is not always fun. It means putting people before tech, and committing to strategies to prioritize people over technology and effectively, integrate psychological safety into onboarding, fostering a culture of trust and transparency from day one. By prioritizing psychological safety, organizations can unlock the full potential of their cybersecurity teams and significantly bolster their defenses against cyber threats. Recognizing the vital role of the  human factor, we unlock the true potential of our CSIRTs and build a stronger defense against new and emerging threats. Staying ahead of the curve in the constantly changing cyber warfare landscape requires an adaptive and resilient defense. This presentation will emphasize that cybersecurity is not solely about technology, but fundamentally relies on people. It will highlight the critical importance of psychological safety within cybersecurity incident response teams, advocating for a culture that values risk-taking, idea sharing, and learning from failures. The presentation will also discuss the challenges of cultivating psychological safety in high-pressure cybersecurity environments and offer strategies for prioritizing people over technology, integrating psychological safety into onboarding processes, and fostering trust and transparency. By recognizing the human factor in cybersecurity, organizations can unlock the full potential of their teams and establish a robust defense against evolving cyber threats.

### Livewire : remote command execution through unmarshalling
Speakers: Rémi Matasse, Pierre MARTIN
page: https://pretalx.com/hack-lu-2025/talk/DNNDLV/
Livewire is a full-stack framework for Laravel that streamlines the creation of
dynamic and interactive web interfaces by allowing developers to build
real-time features using PHP and Blade templates. In this talk, we will show
how to exploit the unmarshalling mechanism used by Livewire to instantiate
arbitrary objects in order to achieve remote command execution on
any Livewire instance as long as you are in possession of the APP_KEY of the
application. Additionally, we will present a new feature added to our publicly
available tool laravel-crypto-killer, which fully automates the generation of
the payload described during the presentation. ## Brief outline

- Introduction to Livewire
    - Livewire unmarshalling process
    - Synthesizers
    - Checksum
- Building an unmarshelling chain from hydrators
    - PHP magic methods
    - First step : getting a phpinfo
    - Second step: getting remote command execution
    - Third step : make the server flaw stop to stay sneaky
- Exploitation by using laravel-crypto-killer
    - Presentation of the freshly added exploit mode
    - Showing the exploitation process on an actual project : Invoice Ninja
- Conclusion and thoughts

## Detailed outline

### Introduction

Livewire has gained significant popularity among Laravel developers due to its 
simplicity and integration with Laravel's ecosystem. Additionally, strong community 
support and compatibility with Laravel features make Livewire an attractive choice 
for developers seeking to build modern, responsive web applications efficiently.

The application BuiltWith lists **676K instances of Laravel** currently live
websites ([BuiltWith-Laravel](https://trends.builtwith.com/framework/Laravel)), and among them **106K instances of Livewire** (15%)
([BuiltWith-Livewire](https://trends.builtwith.com/framework/Laravel-Livewire)). This makes Laravel one of the most used PHP frameworks 
in the world, and Livewire one of its most used plugins.

This presentation will show how to get a remote command execution by abusing
the unmarshalling process of any Livewire instance, as long as we are in
possession of the **APP_KEY** of the application.

#### Livewire unmarshalling process

In a Livewire-based environment, a component is a class managing both the data
and the rendering logic, enabling real-time updates through properties and
methods that interact with the view. In order to manage each component state,
Livewire uses an unmarshalling mechanism described as hydration and
dehydration.

The data structure follows a principle where the last child nodes are
instantiated first, enabling the instantiation of each parent node. This
approach allows for multiple objects to be instantiated and nested within one
another.

```
        +-- Grandchild 3
        |
        +-- Grandchild 2
        |
  +-- Child 2
  |
  |     +-- Grandchild 1
  |     |
  +-- Child 1
  |
 Parent
```

When a user interacts with a view, a POST request is sent to the server to update 
the component state. The request looks like this:

```
POST /livewire/update HTTP/1.1
Host: livewire.local
[...]

{
    "_token":"jMEN2kTQRrwSA5CgH5y8WWqbCpdb4Lx4iBznnlFD",
    "components":[
        {
            "snapshot":"{\"data\":{\"count\":null},\"memo\":{\"id\":\"Y6a883cdUFy82whZ10JW\",\"name\":\"counter\",\"path\":\"counter\",\"method\":\"GET\",\"children\":[],\"scripts\":[],\"assets\":[],\"errors\":[],\"locale\":\"en\"},\"checksum\":\"f56c273c0e4a3eaa5d7fdea9e7142c42d0e1128a8aee35e9546baffaa41870ac\"}",
            "updates":{},
            "calls":[
                {
                    "path":"",
                    "method":"increment",
                    "params":[]
                }
            ]
        }
    ]
}
```

In this request, two fields are particularly important. First, the
`components->snapshot` field contains all the serialized information needed to
restore the component's state on the server side, including the properties and
their values. Second, the `components->calls` field defines the list of methods
that need to be called on the component, along with any associated parameters.

Inside the `components->snapshot->data` field, properties are defined via
synthesizers. Synthesizers are identified through a special "**s**" field
inside the data structure. They are a powerful feature that extends Livewire’s
capability to handle more complex property types that cannot be serialized
natively, such as Eloquent models, Laravel collections, Carbon date instances,
or custom user-defined types. 

### Livewire synthesizers

Synthesizers provide a mechanism to define how these custom types should be
JSON-serialized (dehydrated) and JSON-deserialized (hydrated) when sent between
the client and server. This ensures that the state of these properties is
correctly maintained across requests. 

Here are some examples of default synthesizers:

* **str**: A Stringable object is hydrated and dehydrated as its string
  representation.
* **arr**: A simple PHP array is hydrated and dehydrated without transformation.
* **std**: A standard stdClass object is hydrated and dehydrated by treating its
  properties as an associative array.
* **clctn**: A Laravel collection is hydrated and dehydrated by converting it to
  and from arrays, **can be called on any object loaded in PHP**.
* Etc.

#### CollectionSynth

In the context of Livewire, many hydrators will allow a user to call constructors
on arbitrary object.

For example, the `CollectionSynth` class is used to manage how collection-like
objects are handled during the component dehydration and hydration processes.
Its role is to ensure that PHP collections (such as Laravel’s `Collection` instances) 
are properly reconstructed.

```php
 1   $child) {
10              $value[$key] = $hydrateChild($key, $child);
11          }
12          return new $meta['class']($value);
13      }
14  }
```

The `$key` (line 6) is set to the '**clctn**' value described earlier as the
synthesizer identifier.

When the `hydrate` method is called (line 8), it receives a `$value`, which
represents the serialized collection data sent by the user, a `$meta` array
containing metadata also controlled by the user, and a `$hydrateChild` 
callback used to individually process each embedded element of the collection. 
Once all elements are processed, a new instance of the original collection 
class is created using the reconstructed array by using `new $meta['class']($value)` 
**which is controlled by the user**, allowing an arbitrary object instantiation.

#### Checksum

A protection has been put in place, in order to make sure that users 
do not temper with the synthesizers and managed objects. Before sending
`update` requests, Livewire generates a checksum (or hash) based on the data
sent to the frontend. This checksum is created using the secure hashing
algorithm SHA-256 and the Laravel `APP_KEY`. It includes the data used to
validate their integrity.

The checksum is verified on each request sent by the user, so if the
data is modified, the checksum won't be correct.

But what if the `APP_KEY` was leaked? We already published research dedicated
to this subject: [Deep dive in Laravel
encryption](https://www.synacktiv.com/sites/default/files/2024-12/deep_dive_in_laravel_encryption.pdf),
and our conclusion was that many `APP_KEY`s are already leaked from GitHub, or
are default ones. Therefore, this chain of exploitation is in the continuity of
our previous work.

### Building an unmarshelling chain from hydrators

Thanks to hydration mechanisms, we identified a unmarshelling chain allowing
users to get remote command execution on any Livewire application, providing
the `APP_KEY` is in our possession. The three main steps leading to this RCE
will be detailed.

#### First step : getting a phpinfo

- Detailed chain
    - Analysis of the `GuzzleHttp\Psr7\FnStream` class sources
    - Analysis of the `League\Flysystem\UrlGeneration\ShardedPrefixPublicUrlGenerator` class sources
    - Payload building on Livewire

#### Second step: getting a remote command execution

- Detailed chain
    - Analysis of the `Laravel\SerializableClosure\Serializers\Serializable` class sources
    - Analysis of the `Illuminate\Bus\Queueable` Trait sources
    - Analysis of the `Illuminate\Broadcasting\BroadcastEvent` class sources
    - Payload building on Livewire leading to RCE
- Problem : the flow generates an error 500 even if the RCE is reached

#### Third step: make the server flow stop to stay sneaky

- Rebuilding the previously used gadget chain to continue the application flow
  after the `unserialize`
- Analysys of the `Laravel\Prompts\Terminal` class allowing to reach an `exit`
  call

### Exploitation by using laravel-crypto-killer

A module was developed to automate all the process inside
[laravel-crypto-killer](https://github.com/synacktiv/laravel-crypto-killer), a new `exploit` mode is available, fully 
automating the exploit payload generation detailed in this presentation.

Common Laravel based projects using Livewire are affected, such as [invoiceninja](https://github.com/invoiceninja/invoiceninja), 
which has a **default `APP_KEY`**, making it vulnerable to this exploit by default.

### 2038 is gonna be epoch!
Speakers: Pedro Umbelino, Trey Darley
page: https://pretalx.com/hack-lu-2025/talk/TLVK3W/
19 January 2038 at 03:14:07 UTC implementations relying on 32-bit signed integer representations of Unix epoch time will overflow, resulting in a system time of 20:45:52 UTC on 13 December 1901. (Unix epoch time is a concept more ubiquitous than Unix itself, this bug impacts a wide array of platforms.)

For most impacted systems, the result will be some chaotic breakdown of running state machine logic in which the flow of time logically reverses itself.

There are today orders of magnitude more systems needing to be checked and fixed than there were in the years leading up to Y2K. In order to address the Y2K38 bug we are going to have to pull a lot of fielded equipment out of the ground, test it in a lab, and put remediations in place, all across the globe, and during the next 13 years. Let that sink in for a bit.

Using controlled experiments across multiple environments (including IoT devices, ICS/OT, and embedded systems) we document unexpected vulnerabilities and behaviors.

These findings reveal critical risks that our society cannot afford to ignore, especially given that for a resourceful attacker, 2038 can be any old day they like.

This presentation is intended for developers, security professionals, and incident responders seeking to understand more about this issue. We will present technical realities in plain, hopefully so that any high school kid could understand it, therefore policymakers are encouraged to join, because this issue will impact us all soon! In the early days of the computing age, RAM was expensive and programmers represented timestamps using a two digit year.

As the year 2000 approached, retired developers were brought back into the workforce to fix legacy systems so that they would not crash on 01 January 2000. Remediation efforts were aided by the fact that there was a widespread fear of apocalyptic scenarios manifesting to coincide with the change of millenia and this cultural hype, combined with the novelty of dawning public awareness of the existence of the global internet (which we take for granted today), served to amplify the public and governmental attention on the so-called Y2K bug as the trigger date approached.

As we all know, the world did not end on 01 January 2000. So hyped was the Y2K bug, and so high the expectation of disaster, that when “nothing” happened the entire thing came off as a dud in the public sphere.
Those of us working in IT know all too well how our work is invisible when things are working properly, and how our work is usually only noticed when things go wrong. There were incidents related to the Y2K bug, and there is a body of academic literature on this topic, however that is tertiary to this talk.

Consider at a high level the types of systems which would logically fail when confronted with an error of the calendar date in some calculation: shipment, hospitality, travel, billing, logistics, etc. Now consider the types of systems which would logically be impacted if they confronted an error with the system clock representation of ticks: basically this can screw with any naively implemented state machine.

19 January 2038 at 03:14:07 UTC implementations relying on 32-bit signed integer representations of Unix epoch time will overflow, resulting in a system time of 20:45:52 UTC on 13 December 1901. (Unix epoch time is a concept more ubiquitous than Unix itself, this bug impacts a wide array of platforms.)

For most impacted systems, the result will be some chaotic breakdown of running state machine logic in which the flow of time logically reverses itself.

Y2K38, the Year 2038 Problem, or simply the Epochalypse is approaching fast

Recall the 2008 financial crisis? That was 16 years ago, and you can see how well we did at making our financial sector safe in the intervening years. Now consider that 2038 is only 13 years from now. We have been furiously digitizing our whole societies for the past 25 years.

There are today orders of magnitude more systems needing to be checked and fixed than there were in the years leading up to Y2K. In order to address the Y2K38 bug we are going to have to pull a lot of fielded equipment out of the ground, test it in a lab, and put remediations in place, all across the globe, and during the next 13 years. Let that sink in for a bit. 

The Y2K38 bug presents a real challenge for any system reliant on 32-bit timestamps. In this session we will move beyond conjecture and demonstrate some of the Y2K38 bug’s real-world consequences in real devices. Our research documents how various systems and devices react as they approach and cross the 2038 threshold. We are documenting classes of failure modes triggered by these programming flaws, with the security researcher mindset.

Using controlled experiments across multiple environments (including IoT devices, ICS/OT, and embedded systems) we document unexpected vulnerabilities and behaviors.

These findings reveal some critical risks that our society cannot afford to ignore, especially given that for a resourceful attacker, 2038 can be any old day they like.

This presentation is intended for developers, security professionals, and incident responders seeking to understand more about this issue. We will present technical realities in plain, hopefully so that any high school kid could understand it, therefore policymakers are encouraged to join, because this issue will impact us all soon!

# Outline
* Introduction (5 minutes)
    * How it began for both of us.
    * Overview of Y2K38 and its relevance.
* Context and Methodology (5 minutes)
    * The technical basis of Y2K38 (epoch time and 32-bit limitation).
    * How this session addresses the gap between speculation and evidence.
    * The idea of exhaustive search and classification.
* Case Studies: Real-World Findings (15 minutes)
    * Case study 1 .. N  Failure modes observed and mitigation experiments.
    * Unexpected software behaviors.
    * Challenges for critical infrastructure.
* Mitigation Strategies (5 minutes)
    * Steps to identify and address Y2K38 risks.
    * Long-term approaches for future-proofing systems.
* Implications & Q&A (remaining time if any)
    * Interactive discussion on challenges and solutions.

### Wyse Management Subversion : Taking over Dell's Wyse Management Suite
Speakers: Alain Mowat
page: https://pretalx.com/hack-lu-2025/talk/EB7SPU/ | slides: /media/hack-lu-2025/submissions/EB7SPU/resources/2025.10.23-ha_LZLYCQx.pdf
By it's own definition, Dell's Wyse Management Suite is "a secure hybrid cloud management solution for Dell thin clients". While attempting to determine how secrets are encrypted in the policies pushed to thin clients, we stumbled down a rabbit hole which led to the discovery of multiple vulnerabilities. 

These vulnerabilities allow not only to decrypt the secrets from policies issued to arbitrary devices, but also to fully compromise the Wyse Management Suite server, which in turn allows to take over all the devices in the thin client fleet. 

While these issues are already important in the case of on-premise deployments, the risk is even higher in Dell's own cloud environment, where tenant isolation is not sufficient to prevent exploitation from one tenant to another. This talk will walk through our process of examining Dell's Wyse Management Suite in search of weaknesses or vulnerabilities that would initially allow us to decrypt secrets found in policies pushed out to thin clients.

WMS can be seen as a sort of Configuration Manager or even Device Management solution, where thin clients can register and retrieve configuration files and applications to be deployed. This makes it an ideal target for an attacker, as compromising the server would allow to take control of any clients in the fleet.

During this research, multiple vulnerabilities were discovered. The first ones allow an attacker to impersonate legitimate devices within the system in order to recover policies and decrypt secrets found within. Additional efforts uncovered vulnerabilities that can be exploited to fully compromise the WMS server or any remote repository configured by the system. This can in turn lead to the compromise of any of the devices in the fleet.

The device impersonation issues can also be exploited within Dell's own cloud environment, where it is possible to leak information across tenants to access and compromise sensitive data and assets.

### What's New in Suricata 8: Enhanced Detection and Performance
Speakers: Eric Leblond, Peter Manev
page: https://pretalx.com/hack-lu-2025/talk/7NJXCF/
Suricata is a widely-used high performance, open source network analysis and threat detection software.This talk will provide an overview of the key new features introduced in Suricata 8, the latest release of the open-source network threat detection engine. We will cover the addition of several new protocols, including LDAP, DNS over HTTPS, SIP, SDP, POP3, and websocket, expanding Suricata's monitoring capabilities. We will also discuss the new "transactional rules" functionality, which allows single signatures to match traffic in both directions. The presentation will highlight some of the more than 100 new keywords available, such as those for entropy matching, domain transform, dataset with JSON context, ENIP matching, full DNS field matching, and enhanced support for SMTP, EMAIL, and FTP. Finally, we will touch on the improvements to performance and security, including the default availability of vendoring and sandboxing Lua, and the implementation of HTTP parsing in Rust.

This talk will be relevant for security analysts and network administrators seeking to leverage the latest advances in Suricata for advanced threat detection and network security monitoring.

### How to better identify (weaponized) file formats with ftguess
Speakers: Philippe Lagadec
page: https://pretalx.com/hack-lu-2025/talk/UAJRA9/ | slides: /media/hack-lu-2025/submissions/UAJRA9/resources/2025-10-23_Ha_QhT4jkT.pdf
Ftguess is an open-source tool designed to identify file formats in a more precise and robust way than traditional tools such as file/libmagic  and TrID or even the recent Magika, especially in the context of malware detection and analysis. Indeed in some cases, those tools may be fooled by specially crafted files or polyglots. 

Such tools are often used by malware detection and analysis platforms to decide how to process files. Malware may go undetected if the file format is wrongly identified, for example if a malicious PDF is processed as an innocuous HTML file.
Ftguess implements a new algorithm designed to overcome this issue.

This presentation will show several real cases of malware wrongly identified by malware analysis platforms, and how ftguess can be used to improve detection. Most of the malware analysis and detection platforms like VirusTotal, MalwareBazaar or AssemblyLine rely on tools such as file/libmagic, TrID and Magika to identify the format of a file, in order to decide which tools and algorithms should be used to process the file. This approach works great in most cases, but once in a while we can observe wrong results.

When a file format is wrongly identified, automated analysis tools may not see the true nature of the file and fail to extract relevant information. In the worst case, a malicious file might bypass detection and reach its target without being blocked.

This happens mostly in two situations:
- When the file is a polyglot, which means it combines the structures of two or more different file formats in one;
- or when the file is malformed in a way to fool file/libmagic/TrID, while still being acceptable for its target application.

Several real-life cases will be demonstrated during the presentation.

In fact the main issue with file format identification tools including file/libmagic, TrID and Magika is that they rely solely on the content of the file to be analysed. Whereas, current operating systems such as Windows and GNU/Linux check the file extension to decide which application should open a file. Unlike other tools, ftguess takes into account both the file content and its extension to better identify the intended file format.

### Hacking for hoodies: MISP edition
Speakers: Jeroen Pinoy
page: https://pretalx.com/hack-lu-2025/talk/BWBCZV/ | slides: /media/hack-lu-2025/submissions/BWBCZV/resources/Hacking_for_h_RsY8UpI.pdf
Cyber threat information sharing continues to be important. The tools we use for this should be regularly scrutinized to ensure their security. The most common way of testing seems to be pentesting using automated tools. In this research I decided to use a different approach, focusing on manual code reviews and exploratory testing of MISP and associated tools, with help from LLM in some cases. This research led to a significant list of vulnerability findings. In this talk, I go over my approach to code review, and some of the security findings in MISP and associated tools.

## 2025-10-23 — Schengen 1 & 2

### So you're interested in social engineering? The very first steps
Speakers: Kirils Solovjovs
page: https://pretalx.com/hack-lu-2025/talk/CTVFW8/
It is well known that humans are the weakest link in information security.
Social engineering has emerged as a means to influence and manipulate individuals to achieve desired outcomes. In this presentation, we delve into the realm of social engineering, exploring the art of behavior alteration, manipulation and persuasive communication. We will provide a general introduction to social engineering and guide the audience in the very first steps to actually start training this skill in a safe and responsible manner that will allow you to get a taste of social engineering by slightly altering your behaviour and still staying legal.

We will cover the following topics:
- Introduction to social engineering
- Using OSINT to collect initial information
- Creating pretext
- Fundamental principles of human behavior and decision-making
- Leveraging social normativity in persuasive interactions
- Building rapport and trust
- Exploiting trust
- Practical exercises in everyday life

### iOS analysis using the Sysdiagnose analysis framework workshop - advanced session
Speakers: David Durvaux, Christophe Vandeplas
page: https://pretalx.com/hack-lu-2025/talk/RHLSNB/
This is the second part, or deep dive, of the Sysdiagnose Analysis Framework Workshop.

We will continue on the topics discussed in the first workshop, but here the focus is on diving DEEP in lots of the data that is present in the sysdiagnose archive. 
Please ONLY attend this workshop if you either attended previous year's session or attended the beginners session, or already used the sysdiagnose analysis framework before. We will get our hands dirty and dive deeper into advanced Splunk queries digging into data and better understanding what is in the Sysdiagnose archive.

We will also develop a parser and/or analyser for the sysdiagnose analysis framework

Prerequisites for attending the workshop are: 
- Having downloaded the [workshop material]() beforehand, prepared the Splunk docker, and have a python development environment ready.
- Solid experience with Splunk Query Language 
- Solid experience with `grep`, `sed`, `awk` and `jq`  (or their alternatives)
- Experience with development in python
- Familiarity with the [sysdiagnose analysis framework](https://github.com/EC-DIGIT-CSIRC/sysdiagnose)

### Lockpicking Workshop
Speakers: Walter Belgers
page: https://pretalx.com/hack-lu-2025/talk/N3XMWE/
Former world lockpicking champion, multiple times winner of Dutch lockpicking championships and author of a lockpicking book, Walter Belgers, gives a hands-on workshop about lockpicking. Former world lockpicking champion, multiple times winner of Dutch lockpicking championships and author of a lockpicking book, Walter Belgers, gives a hands-on workshop about lockpicking.

## 2025-10-23 — Hollenfels

### Digital Forensics 1.0.1 - From Zero to Hero
Speakers: Michael Hamm
page: https://pretalx.com/hack-lu-2025/talk/BMLVNX/ | slides: /media/hack-lu-2025/submissions/BMLVNX/resources/DfIr-101_rXxWEVk.pdf
Tools, Tools, Tools, analysts love it to have a large collection of forensics tools available, to perform the analysis and present the results. Unfortunately often the analysts do not exactly know how the tools come to the results. And so, if the tools fail and present wrong results the analyst do not know what is going wrong. This training will start with a little demo. Different tools produce different output. Than we will:
1. Read a stream of Bit
2. Apply addressing to it
3. Learn to interpret values like integer, signed integer or ASCII
4. Be able to convert a little endian value into a big endian
5. Apply a data structure on the data
6. Recover data manually

At the end of the training the attendee will be able to read a MBR/BootSector and read the partition table manually.

## 2025-10-23 — Vianden & Wiltz

### Vulnerability Lookup and GCVE: A Decentralized Approach to Vulnerability Publishing and Management
Speakers: Alexandre Dulaunoy, Cédric Bonhomme
page: https://pretalx.com/hack-lu-2025/talk/QS8PZK/
This hands-on workshop introduces the open-source Vulnerability Lookup project and the Global Common Vulnerabilities and Exposures (GCVE) initiative, two complementary efforts designed to modernize and decentralize the way vulnerabilities are published, shared, and consumed. This hands-on workshop introduces the open-source Vulnerability Lookup project and the Global Common Vulnerabilities and Exposures (GCVE) initiative, two complementary efforts designed to modernize and decentralize the way vulnerabilities are published, shared, and consumed.

Participants will discover how Vulnerability Lookup acts as a collaborative platform for collecting, enriching, and analyzing vulnerability data, supporting every stage of the vulnerability management lifecycle, from discovery and prioritization to tracking remediation and assessing exposure. The session will also introduce GCVE, a next-generation, decentralized framework for vulnerability identification that empowers organizations to act as GCVE Numbering Authorities (GNAs) with greater autonomy and flexibility.

- How to publish and synchronize vulnerabilities using the GCVE and vulnerability-lookup ReST API.
- How decentralized allocation empowers vendors, researchers, and CSIRTs to disclose vulnerabilities more efficiently.
- How to leverage Vulnerability Lookup to support vulnerability triage, enrichment (EPSS, CVSS, Multi KEV), and exposure tracking.
- How Vulnerability Lookup integrates with GCVE to provide real-time insights, cross-references, and analytics.
- Best practices for integrating GCVE and Vulnerability Lookup into your existing vulnerability management workflows.

By the end of the workshop, attendees will understand how these open-source initiatives can strengthen their own vulnerability management processes and contribute to a more resilient, transparent, and collaborative security community.

### Hands-On Hardware Hacking: Extracting Keys and Owning Encrypted Laptops
Speakers: Edouard D'hoedt, Hayk Gevorgyan
page: https://pretalx.com/hack-lu-2025/talk/DE9ZSA/
This hands-on workshop complements the talk *“Field Guide to Physical Attacks Against Full-Disk Encryption”* by guiding participants through a full-chain compromise of a BitLocker-protected Windows system. This isn’t just about sniffing keys, it’s about turning physical access into full control.

Participants will:
- Learn to use a logic analyzer to intercept TPM traffic to extract encryption keys,
- Use those keys to unlock the disk and access system data,
- And escalate privileges to achieve full interactive access on the target machine.

Attendees will walk away having executed every stage of the attack chain, from signal capture to full compromise, on real hardware! Ever wonder what happens when someone steals a laptop that’s “secure because it’s encrypted”? In this workshop, you’ll find out...by doing it yourself!

You will be handed a powered-off, BitLocker-encrypted laptop and guided through the full attack chain. First, you will capture TPM traffic using provided hardware. Then, you will extract the encryption key, decrypt the drive, and finally gain full system access, without ever knowing the user's password!

No theory. No staged environments. You will work directly with real hardware and proven red team tooling. We will walk you through every step: hardware reconnaissance, signal capture, key recovery, drive decryption, and post-exploitation. You’ll even finish with a local admin shell.

Everything you need is provided: gear, guides, tools, and targets. Just bring a laptop and a healthy dose of curiosity.

You’ll walk away having broken into a locked encrypted laptop without a password... and knowing exactly how and why that’s possible.

**Heads-up:** *To make the most of our limited number of hardware kits, attendance will be limited, and participants will collaborate in small groups (4–5 people) during the hands-on portion. This ensures everyone gets time on the tools without sacrificing depth.*

### Practical intro to deeplearning: chihuahuas vs muffins
Speakers: Pauline Bourmeau (Cookie), William Robinet
page: https://pretalx.com/hack-lu-2025/talk/SHRCZE/
Once upon a time, an algorithm's goal was to make a distinction between a chiwawa and a cookie... true story. Human, curiosity is a great thing, and this workshop is built around it.

Here total beginners in AI learn the fundamentals of deep learning, set up their environment, and apply it to image classification. By the end of the workshop, they are able to build a simple web application using Gradio that classifies images. Agenda:

• Short introduction to deep learning

• Setting up the environment

• Hands-on session: we’ll experiment with image classification

• Hands-on session: we build a web app with Gradio

We’ll also be discussing applications to cybersecurity you can prototype, deep learning and training methods, cool the hype and discuss realistic LLM capacities.

## 2025-10-23 — Echternach & Diekirch

## 2025-10-23 — Fitness room

## 2025-10-24 — Europe

### Palo Alto GlobalProtect : Remote Full Compromise Exploit Chain
Speakers: Maxime Escourbiac
page: https://pretalx.com/hack-lu-2025/talk/XDHVWE/ | slides: /media/hack-lu-2025/submissions/XDHVWE/resources/RemoteFullCo_bOdlp55.pptx
This session provides an in-depth analysis of multiple critical vulnerabilities discovered by Michelin CERT in the Palo Alto Networks GlobalProtect VPN client, referenced as CVE-2024-5921, CVE-2025-0117, CVE-2025-0118, CVE-2025-0120, CVE-2025-0131 and CVE-2025-2183

The research highlights how attackers on the same network can exploit weaknesses in certificate verification, root CA management, embedded browser authentication, and client-server communications to achieve remote code execution and privilege escalation on Windows workstations. Elements highlighted during the session : 
1. Certificate Verification Bypass: The VPN client can be tricked into bypassing certificate verification, allowing attackers to impersonate the VPN portal and deliver malicious payloads.

2. Arbitrary Root CA Insertion: Attackers can insert a malicious root CA into the system, enabling them to issue fraudulent certificates and potentially install malware.

3. Embedded Browser Exploits: The use of an embedded browser for authentication can be exploited to deliver malicious content, such as [HTA](https://en.wikipedia.org/wiki/HTML_Application) files, leading to remote code execution.

4. Privilege Escalation: Abusing the Impersonation Mechanism or the Weak System Update to get system privileges.

We will go through all the steps, try to understand GlobalProtect thoroughly, and pave the way towards a full chain exploit.

### Audit and retrospective of an automotive application: Carplay
Speakers: Etienne CHARRON, Khadim
page: https://pretalx.com/hack-lu-2025/talk/LPVDSH/
In this presentation, we share the methodology used during a security audit of the Carplay application. This application exposes services to external car interfaces through Bluetooth and Wi-Fi. **Our work focused on identifying vulnerabilities that could lead to compromise the multimedia equipment, by an attacker already connected to the car's Wi-Fi hotspot.** 

During this analysis, we present how we identified the function responsible for parsing external data sent to the car, how we fuzzed it and discovered a bug already known by Apple (CVE 2023-23494). Vehicle security is essential due to their longevity and the potential impacts on the physical integrity of their users. 

The In-Vehicle Infotainment (IVI) System is an interesting target for an attacker looking for initial access through remote interfaces such as Bluetooth or Wi-Fi. The Carplay application uses Wi-Fi, to allow a user to access iPhone’s services from the IVI (navigation, phone calls, third-party applications such as Spotify...) 

Developed by Apple, the application’s source code is not publicly available, and few security analyses have been conducted on it. 

In this presentation, we share the methodology used during a security audit of the Carplay application.  Our work focused on identifying vulnerabilities that could lead to the compromise of the multimedia equipment, by an attacker already connected to the car's Wi-Fi hotspot. 

During this analysis, we present how we identified the function responsible for parsing external data sent to the car, how we fuzzed it and discovered a bug already known by Apple (CVE 2023-23494).

### From YAML to Root: CI/CD Pipeline Attacks and Countermeasures
Speakers: Hugo
page: https://pretalx.com/hack-lu-2025/talk/CGRNFY/
As CI/CD pipelines become integral to modern software development through systems like Azure DevOps or GitHub Actions, and tools such as Terraform and Ansible, their compromise can have devastating effects, from infrastructure breaches to mass malware distribution.

Originally, CI/CD pipelines were managed and accessed only by a limited group of administrators or integration engineers. However, with the widespread adoption of Infrastructure as Code, it has become increasingly common for companies to open controlled access to their pipelines—sometimes even to external clients. This shift supports use cases such as self-service sandbox environments, client-controlled infrastructure provisioning, or dynamic testbed deployments in multi-tenant platforms. While these scenarios offer flexibility and scalability, they also introduce new risks and potential attack vectors, making it critical to rethink pipeline security under this broader exposure model.

In this talk, we will demonstrate how an attacker can exploit seemingly limited permissions—such as those of a standard contributor account—to fully compromise a CI/CD pipeline and the underlying infrastructure. By chaining misconfigurations, abusing legitimate features, and bypassing common restrictions, we’ll show how limited access can quickly escalate into full control. 
In the second phase of the talk, we’ll look at the defensive side: how a company can effectively secure its pipelines in a context where access is no longer limited to internal teams. Talk Description and Structure
  The talk is divided into two main parts: an offensive demonstration and a defensive strategy session.

  Part 1 – Offensive: From Contributor to Full Compromise
  We will begin with a realistic demonstration of attack scenarios showing how a basic contributor-level account can be used to hijack a CI/CD pipeline, escape the provided use cases and fully compromise the infrastructure through Terraform integration. To reflect real-world conditions, common pipeline protections will be enabled—and bypassed. Key topics include:
  
    
      Remote Code Execution via pipeline files:
      We’ll explore how attackers can achieve RCE through configuration file manipulation or config file poisoning, Terraform constructs (e.g., external data sources, malicious custom providers or modules, abuse of provisioners), and other legitimate pipeline features.
    
    
      Bypassing restrictions:
      Techniques to bypass provider restrictions, function or module blacklists, and CI/CD step filters will be demonstrated, showing how misconfigurations or insufficient validation open the door to exploitation.
    
    
      Post-exploitation steps:
      Once initial execution is achieved, we’ll show how attackers can perform lateral movement in the underlying infrastructure, such as:
      
        Extracting sensitive secrets (cloud credentials, environment variables, connection strings).
        Establishing persistence within the CI/CD pipeline (e.g., malicious jobs, trigger abuse, backdoor artifacts).
      
    
  

  Part 2 – Defensive: How to Secure Your Pipelines in This New Model
  With the offensive risks clearly laid out, we’ll move on to the defensive strategies. This section is divided into two phases:
  
    
      Reinforcement and Protection:
      This proactive phase aims to secure the pipeline by design. We’ll cover:
      
        Secure handling of secrets and credentials.
        Hardening of CI/CD agents and build runners.
        Implementation of integrity checks (e.g., checksum validation, signed commits, restricted runners).
        Tightening access control and repository hygiene.
      
    
    
      Detection and Monitoring:
      Even well-protected pipelines require active monitoring to catch suspicious activity. We’ll discuss:
      
        CI/CD log analysis techniques.
        Indicators of compromise in pipeline behavior.
        Anomaly detection approaches tailored to build systems.

### Persōna Theory: Infiltration & Deception of Emerging Threat Groups
Speakers: Tammy Harper
page: https://pretalx.com/hack-lu-2025/talk/SGWZ8Y/
This talk explores various techniques, tactics, and psychological models used to infiltrate emerging threat actor groups. We will examine the process of target identification and discuss when it is appropriate to attempt infiltration. Additionally, we take a closer look at the concept of probing the enemy and the idea of weaponizing new relationship energy (NRE), which can be effective at destabilize individuals and placing them outside of their comfort zones. An important aspect of Persona Theory is not only what we write but also how we present it. Stylometric analysis can be particularly useful in this area. We will compare transliteration and translation (both human and machine) to understand how to pass as a native speaker. Persona Theory goes beyond the sock puppet and examines the essence, the persona, and what it takes to make a believable persona and how to build relationships online where no one trusts each other by design.

We begin by examining the philosophical foundation of Persona Theory, the idea that everyone wears masks, especially online, and connecting it to the fundamentals of threat intelligence gathering.

Persona Theory outlines the stages of infiltration: identifying targets, probing their weaknesses, gathering intelligence, verifying authenticity, and conducting deep analysis. These stages are demonstrated through practical examples, particularly focused on illicit forums like RAMP, Telegram and other private channels, where recruitment and initial contact occur.

Next, we explore persona sculpting, from stylometry (writing style and language usage) to time zone alignment and geopolitical masking. Techniques include leveraging adjacent Slavic and regional languages, transliteration, and carefully crafted writing habits to convincingly inhabit an identity.

Then we look at case studies that bring the theory to life, walking the audience through actual infiltration scenarios.

### Russian-speaking underground  - changes in the risks, attack surface and modus operandi
Speakers: Vladimir Kropotov
page: https://pretalx.com/hack-lu-2025/talk/EXYE9H/
Criminal business processes are significantly reshaped in recent years due to appearance and accessibility of new technologies and significant changes in the geo-political landscape. The presentation will focus on the changes of behaviour of russian-speaking criminal groups, significant developments and changes on the cyber underground. Those changes are affecting the lists of priority targets, geographical location of the targets of attacks, criminal business processes, modus operandi and priorities of criminal groups.
The presentation will also include case studies on the criminal business processes related to money mule services, attacks, leveraging e-commerce platforms, reshipment services, offers of commit violent actions in the particular regions of EU, appearance of the business models in EU, which was previously leveraged in the Russian-speaking countries. We dive into one of the most sophisticated and impactful ecosystems within the global cybercrime landscape. Our research looks at tools and techniques, specialized forums, popular services, plus a deeply ingrained culture of secrecy and collaboration.

### Lethal Language Models: From Bit Flip to RCE in Ollama
Speakers: Paul Gerste
page: https://pretalx.com/hack-lu-2025/talk/7MHDPF/ | slides: /media/hack-lu-2025/submissions/7MHDPF/resources/Lethal_Langua_uliyCuZ.pdf
AI and LLMs are everywhere, but how are they actually implemented? In this session, we will take a detailed look at Ollama, a popular tool to run LLMs locally. In the context of Pwn2Own, we will learn about Ollama's architecture and the GGUF file format for storing large language models. We will then explore a few memory corruption bugs in the handling of these files and dive deep into the exploitation of one of them. The presentation ends with a live exploit demo, notes on disclosure, and lessons learned. With the rise of AI, a new target category was introduced at Pwn2Own Berlin 2025 covering software that powers AI and machine learning applications. One of the targets was Ollama, a widely used tool for running LLMs like Llama and DeepSeek-R1 on your local machine.

This talk tells the story of my attempt to exploit Ollama for Pwn2Own, how I failed, and how I still eventually succeeded. If you ever wondered about LLM implementations and their attack surface, this talk is for you! We will discover how models are serialized to files and how the handling of the GGUF file format can lead to several types of vulnerabilities. We will then turn one of these bugs with an interesting bit-flipping primitive into a full exploit that executes arbitrary code on a vulnerable Ollama instance.

### Exploiting Legit APIs for Covert C2: A New Perspective on Cloud-based Malware Operations
Speakers: cocomelonc
page: https://pretalx.com/hack-lu-2025/talk/XDPLNP/
As modern security defenses evolve, attackers continue to leverage legitimate cloud services for command-and-control (C2) communication, effectively bypassing traditional network detection systems. This talk presents original research into the abuse of lesser-known free cloud APIs such as GitHub Gists, Telegram Bot API, Discord Webhooks, and Google Apps Script for stealthy malware communication. Unlike well-documented abuses of Google Drive or Dropbox, our study explores new, unmonitored attack surfaces that can be exploited by adversaries while remaining under the radar of enterprise security monitoring tools.

Key topics of my talk:
Techniques for establishing C2 channels using free cloud services.
Encryption and obfuscation strategies to evade EDR/ML-based detection.
Case studies demonstrating real-world proof-of-concepts (PoC) of API abuse.
Recommendations for mitigating risks and detecting malicious API-based C2 activity.

Traditional C2 detection methods focus on recognizing known malware signatures or anomalous network traffic. However, API-based C2 channels blend seamlessly into normal cloud service usage, making them exceptionally difficult to detect. This talk will provide defenders with insight into how attackers exploit these mechanisms and offer practical countermeasures to strengthen security postures against emerging threats.

Target Audience:

Red Teamers, Ethical Hackers, and Penetration Testers
SOC Analysts and Threat Hunters
Incident Responders and Security Engineers As defenders improve security mechanisms, adversaries are increasingly turning to overlooked cloud APIs to maintain covert command-and-control (C2) channels. This talk introduces original research into the misuse of lesser-monitored services like GitHub Gists, Telegram Bot API, Discord Webhooks, and Google Apps Script—highlighting how these platforms can be repurposed for stealthy malware communications. In contrast to widely studied vectors like Google Drive or Dropbox, our work focuses on emerging, underexplored APIs that evade most enterprise detection strategies.

This talk will cover:

    Techniques to establish resilient C2 channels using free cloud APIs.

    Methods of encryption and obfuscation to bypass EDR and ML-based detection.

    Real-world PoCs showcasing API misuse for malware communications.

    Defensive recommendations for detecting and disrupting API-based C2 activity.

Conventional C2 detection relies on pattern matching or anomaly spotting in network traffic. However, API-driven communications often blend with legitimate usage patterns, allowing attackers to remain undetected. This presentation aims to equip defenders with the knowledge and tools to recognize and respond to this evolving threat landscape.

Intended audience:
    Red Teamers, Penetration Testers, and Malware Researchers
    Threat Hunters and SOC Analysts
    Security Engineers and Incident Responders

### Fake Likes, Real Risks: Mapping Fake Social Activity Shops in Europe
Speakers: Sviatlana Höhn, Anastasia “Asya”  Sergeeva
page: https://pretalx.com/hack-lu-2025/talk/TZKXVG/ | slides: /media/hack-lu-2025/submissions/TZKXVG/resources/hack.lu_xVYLKGa.pdf
Fake Likes, Real Risks: Mapping Fake Social Activity Shops in Europe
 
We looked into the world of fake social activity shops - those websites selling likes, followers, and other engagement metrics - specifically targeting the EU market. By analyzing 881 webshops and speaking with social media experts, we uncovered how these services operate, the gaps between what they promise and deliver, and the risks they pose for disinformation, fraud, and financial crime. We explore the hidden world of fake social activity shops - the websites that sell likes, followers, and other engagement metrics. These services are widely available online and often operate in legal grey zones, despite efforts by social media platforms to curb inauthentic engagement. We analyzed 881 such webshops targeting the EU market and conducted interviews with 15 social media marketing experts. Our findings reveal major gaps between what these shops promise and what they deliver, along with recurring business patterns. We also highlight how these services can be exploited for disinformation, cyberfraud, and financial crime.

### Bugs in the Human Code - Help Timo
Speakers: Paul Hirtz
page: https://pretalx.com/hack-lu-2025/talk/EE3B3L/
Bugs and vulnerabilities aren’t limited to software, they exist in our biology too. This talk offers a high-level, hacker-friendly view of what happens when the human code breaks. 

It shares the story of my son Timo, who lives with WOREE syndrome. With no existing treatment, we’re racing to build our own patch to rewriting his code of life to give him a future. When DNA breaks, the consequences can be life-altering. This hacker friendly talk explores how genetic mutations act like bugs in the human code and how rare diseases are like critical vulnerabilities. 

Through my son Timo’s story, we explore what happens when the body’s code breaks, and why we’ve had to become builders ourselves, racing to create a gene therapy that doesn’t yet exist.

### Reverse Engineering, for real
Speakers: Henri Ahola
page: https://pretalx.com/hack-lu-2025/talk/SXNG9K/
Processors execute code sequentially, in a natural order - typically presented as top to bottom. Of course, this makes reverse engineering programs easy. Can we do better? Presented is a silly code obfuscation technique that demonstrates how expectations can be broken with x64 debug register abuse and a bit of magic. We also get (partial) anti-debugging and (partial) anti-VM measures as a bonus on top.

### 4-Byte Hell: When Unicode Enters the Stage
Speakers: Jonas Hess
page: https://pretalx.com/hack-lu-2025/talk/K3JGNF/ | slides: /media/hack-lu-2025/submissions/K3JGNF/resources/4-byte_hell_mLgRBpd.pdf
How complex is your password really? Still using ASCII characters? Password managers aren't your friends - they trick you into weak passwords by limiting character sets in their generators. Consider giving emojis a try instead. I'll briefly talk about how passwords get encoded and how to perform byte-wise password cracking with Hashcat. From there, we'll explore characters beyond ASCII and how they increase password complexity at the byte level.

### Pwn2Own: Hacking IoT devices
Speakers: Adam Hustava
page: https://pretalx.com/hack-lu-2025/talk/PWGECR/
With my university CTF team we participated in pwn2own, a hardware bug bounty competition, and attempted to hack a smart home hub and synology IoT camera. We sucesfully developped an exploit for the camera, but 12h before the competition synology published an update. Talk is about how we hacked and what happened with the update Includes specialised precise soldering equipment to extract data from bga153 format chips, U-boot hacking, format strings, etc.

### Threat Actor Tripping on the Finish Line
Speakers: Rasmus
page: https://pretalx.com/hack-lu-2025/talk/KAPH77/ | slides: /media/hack-lu-2025/submissions/KAPH77/resources/ThreatActorTr_XdKO0pl.pdf
A short presentation of a threat actor that used several layers of obfuscation, native windows functionality, component object model, registry manipulations and domain fronting to execute a stealthy persistence, only to fumble at the finishline with sloppy powershell code. Highly effective and stealthy persistence technique with a unfortunate/fortunate twist.

### Revisiting RAND’s Lost Monte Carlo Simulations: Sharla Perrine, Paul Baran, and the True Business Case for the Internet
Speakers: Trey Darley
page: https://pretalx.com/hack-lu-2025/talk/8NMQUJ/
Before the Internet existed, Sharla Perrine proved—using punched cards—that it could survive a nuclear strike. Sixty years later, we trust the cloud with everything. This talk revisits her forgotten Monte Carlo experiments and proposes a modern rerun: same logic, new topology, fresh risks. If Perrine’s math built the Internet, it’s time to ask ourselves whether that math still holds—or whether resilience has quietly rotted. In the early 1960s, RAND researchers Paul Baran and Sharla Perrine (later Boehm) quietly ran a set of Monte Carlo experiments that changed history. Using punched cards and octal assembly, Sharla’s simulations proved that a distributed packet-switched network could survive attack or failure—work that Vint Cerf later used to persuade DARPA to fund what became the ARPANET.

Yet her name faded into the footnotes. After her death in 2023, she was described as the “grandmother of the Internet” only in the fine print of a real-estate listing—not yet on her Wikipedia page.

This lightning talk reintroduces Sharla Perrine and Paul Baran not just as pioneers, but as data-driven systems thinkers. It also proposes a new research effort: re-running their Monte Carlo simulations under modern assumptions and using contemporary toolchains—to revisit network survivability, traffic models, and failure modes, including time-synchronization shear effects in packet-switched networks.

By comparing 1960s-era modeling assumptions with the centralized “cloud” architectures of today, we may uncover how far the Internet has drifted from its resilient origins—and perhaps even find bugs in the original Monte Carlo code.

Audience Takeaway: The Internet’s founding math was sound, but our faith in its resilience may rest on outmoded—or even false—assumptions.

### Automotive Security Analyzer for Exploitability Risks: An Automated and Attack Graph-Based Evaluation of On-Board Networks
Speakers: Martin Salfer
page: https://pretalx.com/hack-lu-2025/talk/QV9GZF/ | slides: /media/hack-lu-2025/submissions/QV9GZF/resources/AutoSAlfER-Sl_qDNRabq.pdf
Our lives depend on automotive cybersecurity, protecting us inside and near vehicles. If vehicles go rogue, they can operate against the driver’s will and potentially drive off a cliff or into a crowd. The “Automotive Security Analyzer for Exploitability Risks” (AutoSAlfER) evaluates the exploitability risks of automotive on-board networks by attack graphs. AutoSAlfER’s Multi-Path Attack Graph algorithm is 40 to 200 times smaller in RAM and 200 to 5 000 times faster than a comparable implementation using Bayesian networks, and the Single-Path Attack Graph algorithm constructs the most reasonable attack path per asset with a computational, asymptotic complexity of only O(n * log(n)), instead of O(n²). AutoSAlfER runs on a self-written graph database, heuristics, pruning, and homogenized Gaussian distributions and boosts people’s productivity for a more sustainable and secure automotive on-board network. Ultimately, we enjoy more safety and security in and around autonomous, connected, electrified, and shared vehicles. ### The Problem

Computers control steering and brakes usually nowadays, and "smart" features increase a vehicle's attack surface and occasionally introduce vulnerabilities.
Even a combination of seemingly minor vulnerabilities can undermine a vehicle's cybersecurity.
Securing automotive Information Technology (IT) is expensive and challenging, even for leading tech companies.
Compared to corporate IT, this challenge arises from a) the safety-criticality, b) homologation obligations, and c) the IT diversity within each vehicle.
- a) Safety criticality: ECUs (Electronic Control Units) cannot stay indoors with air-conditioning but must work safely and reliably outdoors in the scorching sun and on freezing winter nights, from deserts to the Arctic.
	Such extreme conditions demand special software requirements, which can interfere with security patching.
- b) Homologation obligations: Securing ECUs with swift patches can be hindered by governmental homologation obligations, as patches must not interfere with certifications, e.g., for exhaust purification or crash safety.
- c) IT diversity: ECUs are challenging to secure due to their diversity, as they usually do not communicate homogeneously via TCP/IP (Transmission Control Protocol / Internet Protocol) but rather via a combination of CAN (Controller Area Network), MOST (Media Oriented Systems Transport), LIN (Local Interconnect Network), BroadR-Reach, and FlexRay. ECUs usually do not incorporate x86 CPUs but rather a combination of TriCore, Super-H, PowerPC, ARM, V850, and even less-widely known chips, as this obtains maximum dependability, energy efficiency, and sustainability.


### How does this help? Who will benefit?

AutoSAlfER's automatic evaluation boosts people's productivity for a more sustainable automotive cyber security:
- Architects can automatically evaluate their designs, recheck changes for surprising attack combinations, and shape network topologies toward more security.
- Penetration testers ("red teams") get a head-start on the riskiest and most significant targets and network connections.
- Risk managers can extend their calculations onto a sound model for more precisely and reliably calculated risk reserves.
- Incident handlers ("blue teams") can enrich their situation report regarding what targets and assets could be compromised next and how acutely they are at stake.
- All stakeholders get orientation on anticipated neuralgic points and their impact on adequately prioritizing cybersecurity investments.
- Ultimately, we all gain more security and, thus, safety in and around autonomous, connected, electrified, and shared vehicles.


### Why are you a good person to tell us this?

I initiated, planned, designed, implemented, documented, tested, and evaluated the Automotive Security Analyzer for Exploitability Risks (AutoSAlfER).


#### Agenda
1)	Motivation and Survey
2)	Data and Models
	a.	System Model, Attacker Profile, and Exploit Model
	b.	Attack Surface Exploitability Quantification
	c.	Implementation / Tech Stack
3)	Practical Demo
4)	Algorithms for Attack Graphs
	a.	Single-Path Attack Graph Algorithm (PI + PII)
	b.	Implementation and Evaluation of PI + PII
5)	Algorithms for Total Risk
	a.	Probabilistic Model
	b.	Multi-Path Attack Graph Algorithm (P3Salfer)
	c.	Bayes Network Unsuitability Finding
	d.	Design and Implementation of an Alternative Algorithm with Bayesian Networks (P3Bayes)
	e.	Implementation and Evaluation of the Multi-Path Attack Graph Algorithm (P3Salfer)
6)	Future Work
7)	Further Material
	a)	Patents, Papers, and Posters
	b)	Open-Source Software
	c)	Book

### DCOM Turns 30: Revisiting a Legacy Interface in the Modern Threatscape
Speakers: Julien Bedel
page: https://pretalx.com/hack-lu-2025/talk/AEHE9V/
Part of Windows operating system for over 20 years, DCOM (Distributed Component Object Model) has received a lot of attention from the security research community.

Ranging from lateral movement and privilege escalation to persistence techniques, DCOM is an extremely versatile attack vector. Yet, its inner workings remains unknown to many security experts.

To close this knowledge gap, we will take a deep dive into DCOM latest research works — including this year's many new contributions— through practical use cases and tooling. A comprehensive testing framework will eventually be presented, enabling security researchers to build upon these previous works more effectively.

At last, we will discuss practical defensive strategies, along with key insights to help security analysts effectively detect and respond to DCOM-based abuse. After introducing Windows Component Object Model, we will see how it fits into almost every step of the cyber kill chain. Security profesionnals from any background (academic, offensive and defensive security experts, network administrators..) should find practical use cases and tooling, as well as a deep understanding of how these various attacks work under the hood.

### Beyond post-quantum stereotypes
Speakers: Antoine Gicquel, Benjamin SEPE
page: https://pretalx.com/hack-lu-2025/talk/TP8Y9Y/ | slides: /media/hack-lu-2025/submissions/TP8Y9Y/resources/slides_cgfuSrD.pdf
"Post-quantum", what a scary word... While this field may seem a bit austere at first glance, we will show that it is in fact easier than one may imagine, and that getting a feel for it is within everyone's reach. This talk serves as a soft introduction to the topic aimed at non-cryptographers cybersecurity enthusiasts, emphasizing on the many parallels with traditional cryptography. As an offensive security company, Synacktiv needs to constantly follow the evolutions in security to stay on top of the game and perform high quality audits. Recently, we got interested in post-quantum cryptography, bound to become the next standard in data protection. While we were familiar with "traditional" cryptography, we had never studied the "post-quantum" side of the field, and were a bit intimidated at first. Through our learning, we realized two things: first, it is not as inaccessible as it seems and second, although there have been many advances in the academic field, the industry is far behind in this area as quantum computers are already threatening information security.

We will cover basic security principles in cryptography, why they are threatened by quantum computing, how post-quantum cryptography tackle these threats, and how to incorporate post-quantum security to your products.

The talk will unfold in five parts:
- What does "being secure" mean in the context of cryptography? A quick refresher on the basic principles and definitions.
- How do quantum computers affect the security of current cryptographic algorithms? An overview of how quantum computing undermines classical cryptography.
- What are these "post-quantum" cryptographic algorithms? Key features that make these algorithms resistant to quantum attacks.
- How to migrate to post-quantum algorithms? A look at the challenges of transitioning to post-quantum cryptography, including hybridization and trust concerns with new algorithms.
- What are the associated challenges with transitioning ? A case study of TLS at Cloudflare.

### CLI ambush
Speakers: William Robinet
page: https://pretalx.com/hack-lu-2025/talk/73RXZR/ | slides: /media/hack-lu-2025/submissions/73RXZR/resources/hacklu-2025-C_h8IkaqC.pdf
In this talk, I'll present how I discovered a vulnerability common to various TLS/SSL cryptographic toolkits while considering giving a lightning talk at hack.lu last year ... We'll see how to craft ASN.1 messages and how it helps highlight issues in some CLI apps (OpenSSL as an example).

I'll then show how this problem extends to other cryptographic toolkits and how one can exploit such  issues in order to trap unsuspecting administrators.
We'll walk through the different attack vectors I found.

### THAT PICTURE IS A LIE: SMUGGLING BINARIES WITH STYLE
Speakers: Harpreet Singh
page: https://pretalx.com/hack-lu-2025/talk/WJDWMF/
In this session, I will explore innovative techniques that transform the way executable binaries are delivered. By leveraging HTML smuggling and image polyglot methodologies, the presentation reveals how payloads can be compressed, XOR-encrypted, and artfully embedded within benign image files. This approach not only bypasses conventional security mechanisms such as IDS/IPS, XDR, and DLP systems but also challenges traditional notions of digital content integrity. The talk offers a deep dive into advanced red team tactics designed to operate beneath the radar of modern cybersecurity defenses. "THAT PICTURE IS A LIE: SMUGGLING BINARIES WITH STYLE" provides a comprehensive overview of a sophisticated payload delivery process that repurposes everyday image files into covert carriers of executable binaries. Attendees will be guided through the multi-stage transformation process—starting with the compression of binaries into 7z/zip archives, followed by XOR encryption, and culminating in the embedding within PNG and GIF files using HTML smuggling techniques. This session is crafted for experienced cybersecurity professionals, particularly those involved in red team operations and offensive security. Through live demonstrations and real-world case studies, I will illustrate how these methods can be deployed to evade detection, offering insights into both the offensive potential and the defensive challenges posed by such innovative tactics.

### French stealer ecosystem: the resurgence skid gangs in cybercrime space
Speakers: 0xSeeker
page: https://pretalx.com/hack-lu-2025/talk/AKYVKP/ | slides: /media/hack-lu-2025/submissions/AKYVKP/resources/French_steale_boyCw08.pdf
For years, cybersecurity reports have centered around well-known stealers like Vidar and Raccoon.  there’s an often overlooked and underestimated threat that exists : low-profile cybercriminals
. These are typically young actors, flying under the radar and posing a unique and evolving risk. 

In this talk, we will dive into the French stealer ecosystem, offering insights into the lesser-known groups operating within it. After an overview of the ecosystem—mapping out the groups and their interconnections—we will provide a technical deep-dive into the simplicity and effectiveness of their stealers. We’ll also reveal how we identified similar stealers lurking in open-source repositories. 

The final part of the presentation will expose the poor operational security practices of these actors, culminating in a compelling case study of the group 'Epsilon.' Starting from a simple forum complaint, we’ll demonstrate how we uncovered a surprising link between one of the group’s administrators and a potential drug trafficking operation. This presentation will explore the ecosystem of French-speaking infostealers, focusing on the groups that sell and distribute them and the connections between key actors. We’ll start with an overview of recent developments, identifying recurring pseudonyms and linking various groups.

Next, we’ll dive into the technical side, analyzing how stealers operate, examining their code, and exploring how open-source tools like Bytestealer seems to be customized by threat actors to create advanced malware.

We’ll then profile the administrators behind theses campaigns, analyzing their interactions and operational security (OpSec) missteps that expose them to identification. We will wrap up with a case study on the Epsilon group, revealing the connection between one of its administrators and a possible drug trafficking network, showing how these cybercriminals often diversify into other illegal activities.

Key Takeaways:

   - French Stealer Ecosystem Overview: Understand the structure and connections of various French-speaking stealer groups.

  -  Technical Insights on Stealers: Learn how these stealers operate and how open-source tools are use to enhance their capabilities.

   - Profiling Threat Actors: Discover how analyzing cybercriminal interactions and OpSec errors can lead to identification and disruption.

   - Epsilon Group Case Study: See how one group’s activities extend into illicit fields like drug trafficking, underscoring the broader impact of these operations.

## 2025-10-24 — Schengen 1 & 2

### Practical Maldoc Analysis Workshop
Speakers: Didier Stevens
page: https://pretalx.com/hack-lu-2025/talk/X83SQU/
Maybe you already attended a maldoc analysis workshop from Didier at the Hack.lu conference. Didier has delivered workshops on PDF, Office and RTF document analysis. These workshops were bottom-up: we first learn about the fundamentals, and gradually we make our way through ever more complex exercises.

This workshop is the other way around: we go top-down (and we cover PDF, Office and RTF in the same workshop). We don’t start with the fundamentals (they will come later during the exercises when necessary), but we start directly with exercise files that we first have to identify, and then decide how to proceed with the analysis.

We immediately start with real maldoc samples, and you learn how to triage the file and start the analysis. You will learn what tools to use depending on the type of maldoc, and what analysis strategy to follow. You will also be guided with custom decision trees designed for this workshop, that you can use later on in your professional practice.

And we will also cover some automation to perform batch analysis. Attendees will have to bring a laptop with Python.
They must be prepared to handle real malware, thus a virtual machine to perform the analysis in is recommended.
Windows, Linux and macOS are suitable.
Didier will perform the workshop inside a Windows VM.

### Hacking Kubernetes
Speakers: Benjamin Koltermann
page: https://pretalx.com/hack-lu-2025/talk/TJGLQE/
Kubernetes security is critical to protect containerized applications and infrastructure from vulnerabilities and threats in complex, distributed environments. Because Kubernetes automates and orchestrates workloads, its large attack surface, multi-tenancy and integration with CI/CD pipelines requires strong security measures to prevent attacks and ensure compliance. Effective security practices help to minimize risks such as privilege escalation, data leakage and supply chain attacks in dynamic cloud-native environments.

This training will provide you with comprehensive practical knowledge on securing your Kubernetes environments. You will learn tools and techniques to increase the security of your Kubernetes environments and minimize risks such as privilege escalation, data leakage and supply chain attacks. You will be able to put what you have learned into practice in a lab environment. In this training, you will learn how to secure your Kubernetes clusters. You will dive into core security concepts including admission control and best practices for Kubernetes clusters. The training provides hands-on practice in a lab environment enforcing policies, managing access controls, and securing containerized workloads. You will learn to recognize misconfigurations and take effective countermeasures. You will also learn what the most important aspects of Kubernetes security are and where you can start.

## 2025-10-24 — Hollenfels

### MISP API sorcery workshop
Speakers: Sami Mokaddem, Andras Iklody
page: https://pretalx.com/hack-lu-2025/talk/TQFERQ/
MISP is heavily used by a long list of communities to ingest, share and collaborate on threat intelligence, but its most powerful aspect, it's flexible API, goes under utilised by many of its users. 

This workshop aims to walk you through the various ways in which automation can make your life easier, both in producing and ingesting threat intelligence.

Bring your laptop along and if possible, have a MISP installation available locally, as we'll also be tackling modifications to the system! The workshop aims to walk participants through the various different API techniques that can be used in MISP both to create and to extract information from the system.

Participants will learn to create and enhance information in MISP as well as follow a deep dive into techniques for extracting accurately filtered sub-sets of the information. 

We will also take a small detour on how to develop your own integration to cover whatever format MISP doesn't handle by default - either by building a new export modules or, if time permits it, by relying on the workflow system of MISP.

### Malware Development for Ethical Hackers (Windows, Linux, Android)
Speakers: cocomelonc
page: https://pretalx.com/hack-lu-2025/talk/FEUP9R/
Whether you are a Red Team or Blue Team specialist, learning the techniques
and tricks of malware development gives you the most complete picture of
advanced attacks. Also, due to the fact that most (classic) malwares are written
under Windows, as a rule, this gives you tangible knowledge of developing under Windows.
The course will teach you how to develop malware, including classic tricks and tricks of modern ransomware found in the wild. Everything is supported by real examples.
The course is intended for Red Team specialists to learn in more detail the tricks of malware development (also persistence and AV bypass) and will also be useful to Blue Team specialists when conducting investigations and analyzing malware.

The course is divided into four logical sections:
- Malware development tricks and techniques (classic injection tricks, DLL injection tricks, shellcode running)
- AV evasion tricks (Anti-VM, Anti-Sandbox, Anti-disassembling)
- Persistence techniques
- Cryptographic functions in malware development (exclusive)
- Malware Development for Android and Linux (bonus)

Most of the example in this course require a deep understanding of the Python, Kotlin
and C/C++ programming languages.

Knowledge of assembly language basics is not required but will be an advantage Malware Development and Persistence Tricks for Ethical Hackers

MALWARE INJECTION TECHNIQUES:
1. Traditional Injection Approaches: Code and DLL (2 practical examples, LAB + 1 homework)
2. Exploring Hijacking Techniques (1 practrical example, LAB + 1 homework)
3. Understanding Asynchronous Procedure Call (APC) Injections (1 practical example, LAB + 1 homework)
4. Mastering API Hooking Techniques (1 practical example, LAB)

PERSISTENCE MECHANISMS:
5. Classic Path: Registry Run Keys ( 1 practical example, LAB)
6. Persistence via Winlogon Process ( 1 practical example, LAB)
7. Exploiting Windows Services for Persistence ( 1 practical example, LAB + 1 homework)
8. Exploring Non-Trivial Loopholes ( 2 practical examples, LAB + 1 homework)

MALWARE FOR PRIVILEGE ESCALATION:
9. Manipulating Access Tokens like APT (1 practical example, LAB + 1 homework)
10. Password stealing (1 practical example, LAB + 1 homework)
11. Malware for bypass User Access Control (1 practical example LAB + 1 homework)

ANTI-VM AND AV BYPASSING
12. Anti-Virtual Machine Strategies (4 practical example, LAB + 1 homework)
13. Practical use of hash algorithms in malware ( 1 practical example, LAB + 1 homework)
14. Evasion Static Detection ( 1 practical example, LAB + 1 homework)
15. Evasion Dynamic Detection (1 practical example, LAB + 1 homework)
16. Advanced Evasion Techniques (1 practical example, LAB + 1 homework)
17. Cryptography for bypassing security solutions ( 4 practical examples, LAB + 2 homework)

Linux and Android Malware
18. Linux Kernel Hacking (1 practical example, LAB)
19. Linux process injection (1 practical example, LAB)
20. Introduction to Android Malware (3 practical examples, LAB)
21. Leveraging legit APIs for Android Malware (2 practical examples, LAB)

RESEARCH AND PRACTICE:
22. Simple ciphers for malware development (3 practical examples, LAB + 1 homework)
23. The Power of Base64 Algorithm (2 practical examples, LAB + 1 homework)
24. Elliptic Curve Cryptography (ECC) and Malware ( 1 practical example, LAB + 1 homework)

## 2025-10-24 — Vianden & Wiltz

### Hack your brain
Speakers: Pauline Bourmeau (Cookie)
page: https://pretalx.com/hack-lu-2025/talk/ZKNFYV/ | slides: /media/hack-lu-2025/submissions/ZKNFYV/resources/hack-your-bra_Qq4k2eO.pdf
If you are done hearing about focus on one side and productivity on the other, you are not an alien. This workshop is about breaking misconceptions, focus and work (especially in cybersecurity demanding tasks). You'll learn the ropes to reprogram your brain (using the language of your choice). The outline: 

- Super duper intro to focus and flow
- Understand your system
- Hack your system with computer programming
- Take advantage of your multi-core processing
- Personal use of AI 
- Build systems to help others
- Practice brain-f***
- Colors and music - make some noise - even if you don't know how to sing. 

I’ll teach you what I’ve learned along the way and how I’ve hacked my brain after some adventures and misadventures in the curious world of brain injury recovery.

Requirements:
Bring your brain.

## 2025-10-24 — Echternach & Diekirch

