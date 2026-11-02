>>> HOW TO RUN THIS <<<
This is the digest prompt for lacnic-45. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/lacnic-45.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/lacnic-45.md
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

Below is the program for LACNIC 45 (operator). Read it and produce a digest
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
conference: LACNIC 45
type: operator
source_url: https://lacnic45.lacnic.net/
generated: 2026-11-02
registry_key: lacnic-45
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## LACNIC Runners ()
### LACNIC Runners
We invite you to join the LACNIC Runners group in Panama City. This time, we will be getting together for a walk or run along Bulevar Panamá Pacífico. The group will meet on Wednesday, 27 May at 07:00 am at the entrance to the Westin Playa Bonita Panama (Km 6 Camino a Veracruz). From there, we will walk or run to Bulevar Panamá Pacifico and Av. Bertsch, approximately 2.4 km from the hotel. We will start our way back along the same route at 7:40 am and expect to arrive at the hotel at around 8:10 am. For those who prefer a longer route, Bulevar Panamá Pacífico extends for 5 km. For the latest information about the group&#8217;s activities, subscribe to the runners list at: https://mail.lacnic.net/mailman/listinfo/runners Los invitamos a unirse al grupo de runners de LACNIC en ciudad de Panamá. En esta oportunidad, realizaremos una actividad libre de caminata o corrida por Bulevar Panamá Pacífico. Nos encontraremos el día miércoles 27 de mayo a las 7:00 am en la entrada del Westin Playa Bonita Panama (Km 6 Camino A Veracruz). El trayecto propuesto consiste en caminar o correr hasta el Bulevar Panamá Pacífico a la altura de Av. Bertsch (ubicado a 2,4 km del hotel). A las 7:40 iniciaremos el retorno volviendo por el mismo recorrido y llegaremos al hotel alrededor de las 8:10 am. El Bulevar Panamá Pacífico tiene 5 km de extensión para quienes prefieran hacer un recorrido más largo. Para mantenerse informados sobre las actividades del grupo de runners, pueden inscribirse a la lista en: https://mail.lacnic.net/mailman/listinfo/runners

## Foro Técnico de LACNIC ()
### The Internet ASN graph
Speakers: Claudio Risso, Carlos Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/el-grafo-de-los-asns-de-internet-lacnic45.pdf | video: https://youtu.be/EBa1wEFbnKs
No description published; title, speakers and materials only.

### Behind the Routes: Measuring BGP Instability on the Internet
Speakers: Milena Bueno Rocha
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic-45-behind-the-routes-measuring-bgp-instability-on-the-internet.pdf | video: https://youtu.be/c51phXoslpM
No description published; title, speakers and materials only.

## Receso ()
### NIC.br Commercial presentation
No description published; title, speakers and materials only.

## Reunión de LAC CSIRTs ()
### Closing of the conference and presentation of the “Hands-on CSIRT Incident Management Workshop: From an Incident to Containment”
Speakers: Graciela Martínez Giordano
No description published; title, speakers and materials only.

### TBC
No description published; title, speakers and materials only.

### Do You Really Know Your Attack Surface? Real Exposure and Continuous Visibility Using IVRE
Speakers: André Ricardo Landim
No description published; title, speakers and materials only.

### From Fragmentation to Observability: Operational Lessons in the Evolution of a SOC Towards Analytics- and AI-Based Detection and Response Capabilities
Speakers: Gonzalo Romero
No description published; title, speakers and materials only.

### CERT.br Threat Feeds for AS Holders and National CSIRTs
Speakers: Ueslei Prado
No description published; title, speakers and materials only.

### SEO Poisoning in the Brazilian National Education and Research Network
Speakers: Antonio Silverio Montagner
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/Apresentacao-SEO-Poison-LACNIC45.pdf
No description published; title, speakers and materials only.

### LAC CSIRTs (Training)
Taller de Gestión de incidentes Hands-on CSIRT: del Incidente a la Contención LACNIC &#8211; TILSOR El objetivo principal de este taller es dotar a los asistentes del conocimiento necesario, tanto técnico como metodológico, para comprender los procesos involucrados en la gestión de un incidente. El taller tiene un perfil práctico (hands-on), donde utilizando LAVA, el Cyber range de Tilsor, se hará disponible para cada equipo una infraestructura tecnológica virtualizada (emulando la realidad de una organización). Los equipos operan como un CSIRT corporativo respondiendo a un incidente activo simulado dentro del cyber range. El ejercicio sigue el ciclo estándar de gestión de incidentes de seguridad, poniendo a prueba tanto las capacidades técnicas como las de coordinación y comunicación. Resultados A través de este taller Usted podrá adquirir un entendimiento inicial acerca de: La ejecución de un proceso de gestión de incidentes Ejercitar técnicas utilizadas en cada una de las cinco etapas de la gestión de un incidente Este Taller está dirigido a: Responsables de Seguridad Informática/ Seguridad de la Información Técnicos en el área de Seguridad Informática/ Seguridad de la Información Gerentes de Tecnología IMPORTANTE: La inscripción a este evento presencial no implica la confirmación automática de asistencia. Su cupo será confirmado la semana anterior al inicio de LACNIC 45. Entrenamiento dictado únicamente en idioma español. Inscripción: https://eventos.lacnic.net/ev4/detail?id=training_csirt_2026 Instructores: Ing. Marcelo Rodríguez, Ing. Guillermo Guerrero, MsC Taller de Gestión de incidentes Hands-on CSIRT: del Incidente a la Contención LACNIC &#8211; TILSOR El objetivo principal de este taller es dotar a los asistentes del conocimiento necesario, tanto técnico como metodológico, para comprender los procesos involucrados en la gestión de un incidente. El taller tiene un perfil práctico (hands-on), donde utilizando LAVA, el Cyber range de Tilsor, se hará disponible para cada equipo una infraestructura tecnológica virtualizada (emulando la realidad de una organización). Los equipos operan como un CSIRT corporativo respondiendo a un incidente activo simulado dentro del cyber range. El ejercicio sigue el ciclo estándar de gestión de incidentes de seguridad, poniendo a prueba tanto las capacidades técnicas como las de coordinación y comunicación. Resultados A través de este taller Usted podrá adquirir un entendimiento inicial acerca de: La ejecución de un proceso de gestión de incidentes Ejercitar técnicas utilizadas en cada una de las cinco etapas de la gestión de un incidente Este Taller está dirigido a: Responsables de Seguridad Informática/ Seguridad de la Información Técnicos en el área de Seguridad Informática/ Seguridad de la Información Gerentes de Tecnología IMPORTANTE: La inscripción a este evento presencial no implica la confirmación automática de asistencia. Su cupo será confirmado la semana anterior al inicio de LACNIC 45. Entrenamiento dictado únicamente en idioma español. Inscripción: https://eventos.lacnic.net/ev4/detail?id=training_csirt_2026 Instructores: Ing. Marcelo Rodríguez, Ing. Guillermo Guerrero, MsC

### LAC-CSIRTs (Conf.) Opening Remarks
Speakers: Graciela Martínez Giordano
The goal of this activity is to create spaces where participants can share and collaborate on security incident management issues affecting the region. In line with this, we propose that those CSIRTs that are in operation provide a brief update on their teams. In addition, a space will be reserved to identify possible topics of interest or common projects that can be addressed during the week. The meeting is aimed at all CSIRT members attending the event, as well as at anyone who is interested in creating their own teams or who is in the process of creating a CSIRT. Esta actividad pretende generar espacios de intercambio y de colaboración en temas de gestión de incidentes de seguridad en la región. Para ellos proponemos que los CSIRTs constituídos brinden un breve update de sus equipos. Además, se destinará un espacio para identificar posibles temas de interés o proyectos en común que se puedan abordar durante la semana. IMPORTANTE: Dirigido a todos los integrantes de los CSIRTs que asistan al evento, así como a staff de CSIRTs en proceso de ingreso al FIRST iniciado formalmente.

### LAC CSIRTs (By invitation)
The goal of this activity is to create spaces where participants can share and collaborate on security incident management issues affecting the region. In line with this, we propose that those CSIRTs that are in operation provide a brief update on their teams. In addition, a space will be reserved to identify possible topics of interest or common projects that can be addressed during the week. The meeting is aimed at all CSIRT members attending the event, as well as at anyone who is interested in creating their own teams or who is in the process of creating a CSIRT. Esta actividad pretende generar espacios de intercambio y de colaboración en temas de gestión de incidentes de seguridad en la región. Para ellos proponemos que los CSIRTs constituídos brinden un breve update de sus equipos. Además, se destinará un espacio para identificar posibles temas de interés o proyectos en común que se puedan abordar durante la semana. IMPORTANTE: Dirigido a todos los integrantes de los CSIRTs que asistan al evento, así como a staff de CSIRTs en proceso de ingreso al FIRST iniciado formalmente.

## Foro Público de Políticas ()
### Round Table: Experience of the Co-authors of the LAC-2025-5 Proposal
Speakers: Edmundo Cázarez-López, Hernán José Arcidiácono, Douglas Fernando Fischer, Tomás Lynch, Sergio Rojas
video: https://youtu.be/xvBlgpCCbsE
No description published; title, speakers and materials only.

## LAC Peering Forum ()
### LAC Peering Forum
Agenda Agenda

## Orientación para nuevos participantes (25/05/2026)
### Orientation Session for Newcomers
Speakers: Ernesto Majó, Laura Kaplan
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/orientacion-nuevos-participantes-lacnic45.pdf | video: https://youtu.be/ztkHEr7M0GU
Welcome session for first-time attendees at a LACNIC meeting. It will offer a practical guide to help you make the most of the event, including sessions, tutorials, panel discussions, networking opportunities, and social activities. Sesión de bienvenida para quienes asisten por primera vez a LACNIC 45. Ofrecerá una guía práctica para aprovechar mejor la agenda del evento, incluyendo sesiones, tutoriales, paneles, espacios de networking y encuentros sociales.

## Tutoriales (25/05/2026)
### What You Need to Know About LACNIC 45 Tutorials
Speakers: Mariela Rocha
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/orientacion-inicio-de-tutoriales-lacnic-45.pdf | video: https://youtu.be/a6kR3fe3cec
A brief session to kick off the day, introduce the content of the tutorials, and offer participants a quick guide to help them choose their learning path. It will serve as a space to welcome attendees and provide orientation on the tutorials included in the event program, which will cover topics ranging from routing security and RPKI to IPv6, DNS, and resource management. The goal is to help participants make the most of their time at the event. Una sesión breve para abrir la jornada, presentar el contenido de los tutoriales del día y ofrecer a los participantes una guía rápida para elegir mejor su recorrido. Será un espacio de bienvenida y orientación sobre los principales tutoriales de la agenda, desde seguridad de ruteo y RPKI hasta IPv6, DNS y administración de recursos, con el objetivo de facilitar una participación más provechosa.

### Resource Management - MiLACNIC/Security Module
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/adm-de-recursos-mi-lacnic-modulo-de-seguridad-lacnic45.pdf
The main goal of this tutorial is to provide detailed information on the features and functions of MiLACNIC and how to use them. It is geared towards representatives of organizations that are already members and have been assigned IPv4 and/or IPv6 resources directly by LACNIC and who wish to learn more about the advantages of using the functions offered by MiLACNIC, such as how to mitigate operational risks by maintaining updated records for assigned resources. The presentation on delegated RPKI is geared towards experienced RPKI users who prefer to generate their organization’s RPKI objects within their own infrastructure. LACNIC CSIRT will present the MiLACNIC Security Module, where users can submit information about resources involved in security events. They will also explain the importance of correcting these problems, using strong passwords, and the need for a second authentication factor for data protection. Finally, they will touch upon the concepts of what a CSIRT is and the role of LACNIC CSIRT in managing computer security incidents. Important: Because NIRs in the LACNIC region use a different platform, the material shown during the presentation will not be available to members of organizations in Brazil. In the case of Mexico, the reports and RPKI module are compatible with what will be shown in this presentation. Este tutorial tiene como principal finalidad conocer en profundidad el uso y las funcionalidades de MiLACNIC. Está orientado a representantes de organizaciones que ya son miembros asociados y poseen recursos IPv4 y/o IPv6 asignados directamente por LACNIC y quieren conocer más acerca de las ventajas de utilizar las funcionalidades de MiLACNIC, como por ejemplo cómo mitigar riesgos de operación manteniendo registros actualizados para los recursos asignados. La presentación sobre RPKI delegado está enfocada a usuarios experimentados en RPKI que prefieran que la generación de los objetos RPKI de su organización se realice dentro su propia infraestructura. El CSIRT de LACNIC presentará el Módulo de Seguridad de MiLACNIC, donde se envía la información de recursos involucrados en eventos de seguridad informática. Se explicará la importancia de corregir esos problemas, de utilizar contraseñas seguras y la necesidad de un segundo factor de autenticación para la protección de los datos. También se abordarán de forma breve los conceptos de qué es un CSIRT y el rol del CSIRT de LACNIC en la gestión de incidentes de seguridad informática. Aclaración importante: debido a que los NIRs de LACNIC utilizan una plataforma distinta, el material mostrado en la presentación no está disponible para miembros de organizaciones en Brasil. En el caso de México, el módulo de RPKI y reportes son compatibles con lo que se expondrá en esta presentación.

### Is My Recursive DNS Server Ready for the Root KSK Rollover?
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/ksk-rollover-presentation-technical-audiencees-lacnic45.pdf | video: https://youtu.be/8VlLWR7pBJQ
The DNSSEC Root KSK Rollover is around the corner. In this session, we will walk through the steps needed to verify that our recursive DNS servers are prepared to avoid potential issues. We will cover what the KSK rotation involves and configurations for some of the most commonly used recursive servers. Participants will have the opportunity to complete a hands-on exercise to check whether their own recursive servers are ready. Estamos próximos a la rotación de la clave KSK de DNSSEC para la raíz del DNS. En este espacio veremos algunos pasos para verificar que nuestros servidores DNS recursivos están preparados de forma de evitar posibles problemas. Repasaremos de qué se trata esta rotación de la KSK, algunas configuraciones para algunos de los servidores recursivos más comúnmente utilizados y cada participante podrá realizar una breve práctica donde efectivamente chequee que sus servidores recursivos están preparados.

### Routing Security: From RPKI to ASPA
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/seguridad-en-ruteo-de-rpki-a-aspa-lacnic45.pdf
This tutorial provides a detailed, practical overview of routing security. It begins with the fundamentals of RPKI, ROA creation, and origin validation. Building on this foundation, it addresses other key aspects for strengthening routing security, such as bogon filtering, route leak classification, and best practices for mitigation, including the use of BGP roles. Finally, it offers an overview of the latest developments, including ASPA and new initiatives within the IETF. Este tutorial ofrece una visión detallada y práctica de la seguridad en ruteo, comenzando por los fundamentos de RPKI, la creación de ROAs y la validación de origen. A partir de esa base, aborda otros aspectos clave para mejorar la seguridad del enrutamiento, como el filtrado de bogons, la clasificación de route leaks y las buenas prácticas para su mitigación, incluyendo Roles en BGP. Finalmente, presenta un panorama general de desarrollos más recientes, como ASPA y nuevas iniciativas en el ámbito de la IETF.

### Towards the Age of IPv6-Only
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/redes-mayoritariamente-ipv6v4.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-dnsrecursivodetrasdenat64.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-alejandroacosta-nat64-dns64.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/jgc-lacnic45-rfc8950.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/jgc-lacnic45-dhcpv6pd.pdf | video: https://youtu.be/zHTjt1dLqYI
Implementing IPv6 is not only about ensuring the continuity of our networks and Internet services. It also opens the door to new technologies and multiple improvements. This tutorial will focus on hands-on demonstrations for configuring IPv6-only networks. We will cover essential configurations such as NAT64 which enable connectivity with IPv4 networks and then explore how to move to IPv6-mostly. In addition, we will look at IPv4 packet routing in IPv6 networks and show how it is possible to have an IPv6-only DNS resolver without any disruptions. Today, ignoring IPv6 adoption means falling behind in the evolution of the Internet and becoming increasingly isolated within the network ecosystem. Implementar IPv6 no se trata únicamente de garantizar la continuidad de nuestras redes y servicios en Internet; también abre la puerta a nuevas tecnologías y mejoras desde varias perspectivas. En este tutorial llevaremos a cabo demostraciones prácticas para configurar redes que funcionen exclusivamente con IPv6 (IPv6 Only). Abordaremos configuraciones esenciales como NAT64, que permite la alcanzabilidad a redes IPv4 y veremos desde aquí cómo ir a redes IPv6 Mostly. Adicionalmente trabajaremos con enrutamiento nativo de paquetes IPv4 en redes IPv6 y realizaremos una demostración de cómo se puede tener un DNS resolver IPv6 Only sin romper nada. Ignorar la adopción de IPv6 hoy equivale a quedarse rezagado en la evolución de Internet y quedarnos aislados en el ecosistema de redes.

### Interactive Workshop: How LACNIC Manages Your Internet Resources and How You Can Influence the PDP
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/taller-interactivo-como-administra-lacnic-tus-recursos-en-internet-y-como-puedes-influir-en-ello-lacnic45.pdf
This workshop is an opportunity to practically understand how the community defines the rules for the administration of IP addresses and Autonomous Systems in our region, through LACNIC’s Policy Development Process (PDP). Throughout the workshop, we will detail each phase of the PDP, share experiences, and hold interactive discussions with collaborators involved in the process. Additionally, we will organize a group activity so that participants can simulate the process, exchange ideas, and experience what it’s like to actively engage in discussions and contribute to LACNIC’s work. Este taller es una oportunidad para conocer de forma práctica cómo la comunidad define las reglas sobre la administración de direcciones IP y Sistemas Autónomos en nuestra región, a través del Proceso de Desarrollo de Políticas (PDP) de LACNIC. A lo largo del taller, detallaremos cada fase del PDP, compartiremos experiencias y charlas interactivas con colaboradores involucrados en el proceso. Además, organizaremos una actividad grupal para que los participantes puedan simular el proceso, intercambiar ideas, y experimentar cómo es involucrarse activamente en las discusiones y así contribuir a la labor de LACNIC.

### Secure Routing and Origin Validation Lab
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45_laboratorio-de-ruteo-seguro-y-validacion-de-origen.pdf
This lab focuses on exploring the latest tools and best practices for enhancing Internet routing security. It will cover the monitoring of BGP advertisements, beginning with a manual review followed by an introduction to automation engines for RPKI configuration, along with the application of filters to help mitigate attacks. Participants will have access to a virtual lab where they will configure devices using automation tools presented in the tutorial. Requirements: Participants are recommended to have prior knowledge of BGP, RPKI, and IRR. Topics to be covered: Introduction to the current challenges in Internet routing and strategies for enhancing BGP security. BGP peering configuration in an IXP environment. Use of the FORT validator to verify prefixes announced by the participants. Monitoring BGP and RPKI announcements. Generating filters based on AS-SET records in the LACNIC IRR. Route hijacks and mitigation techniques Automation with Ansible: Configuring validators, ACLs, and filters. Este laboratorio se centra en explorar las herramientas más recientes y las mejores prácticas para mejorar la seguridad en el ruteo de Internet. Se abordará el monitoreo del estado de los anuncios BGP, comenzando con una revisión manual y continuando con una introducción a motores de automatización para la configuración de RPKI y la aplicación de filtros que ayudan a mitigar ataques. Los participantes tendrán acceso a un laboratorio virtual en el que configurarán equipos utilizando herramientas de automatización presentadas en el tutorial. Requisitos previos: Se recomienda que los participantes tengan conocimientos previos sobre el funcionamiento de BGP, RPKI e IRR. Temas a abordar: Introducción a los desafíos actuales del ruteo en Internet y estrategias para mejorar la seguridad en BGP. Configuración de peering BGP en un entorno de IXP. Uso del validador FORT para verificar prefijos anunciados por los participantes. Monitoreo de anuncios BGP y validación de RPKI. Generación de filtros a partir de registros AS-SET en el IRR de LACNIC. Secuestro de rutas y técnicas de mitigación. Automatización con Ansible: configuración de validadores, ACLs y filtros.

## Cóctel de Bienvenida (25/05/2026)
### Welcome Cocktail
Oceánica (El Bohío) Oceánica (El Bohío)

## LACNIC (26/05/2026)
### Opening Ceremony
Speakers: Esteban Lescano
video: https://youtu.be/DivTPYaWok0
Official opening ceremony of the event, where participants will be welcomed and activities will formally begin. Espacio de apertura oficial del evento, en el que se dará la bienvenida a los participantes y se inaugurará formalmente la agenda de actividades.

### Introduction to Current Cybersecurity Challenges
Speakers: Carlos Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/panorama-y-desafios-de-la-ciberseguridad-en-2026-lacnic45.pdf | video: https://youtu.be/gwKIqGK3CWU
Today, the cybersecurity landscape is marked by new forms of abuse, increasingly sophisticated attacks, and growing challenges for Internet infrastructure. La ciberseguridad enfrenta hoy un escenario marcado por nuevas formas de abuso, una mayor sofisticación de los ataques y desafíos crecientes para la infraestructura de Internet.

### Current Cybersecurity Challenges
Speakers: Severin Walker, Kyle Krejci, Silvia  Batista, Marcelo Rodríguez Da Silva
video: https://youtu.be/SKwpxWwmvWg
Today, the cybersecurity landscape is marked by new forms of abuse, increasingly sophisticated attacks, and growing challenges for Internet infrastructure. In this session, we will explore how various stakeholders understand these challenges and what can be done to mitigate and address them. The panel will bring together various perspectives to discuss threats amplified by AI, risks associated with routing, DNS, and IPv6, and concrete measures to strengthen prevention, coordination, and response. The focus will be on sharing experiences, lessons learned, and best practices relevant to the technical community, operators, CSIRTs, and security professionals. La ciberseguridad enfrenta hoy un escenario marcado por nuevas formas de abuso, una mayor sofisticación de los ataques y desafíos crecientes para la infraestructura de Internet. En este espacio veremos la visión de diferentes actores sobre estos desafíos y sobre posibles formas de mitigar estos ataques y solventar estos desafíos. A partir de este marco, el panel reunirá distintas miradas para conversar sobre amenazas potenciadas por IA, riesgos de ataques vinculados a routing, DNS e IPv6, y medidas concretas para fortalecer la prevención, la coordinación y la respuesta. El foco estará puesto en compartir experiencias, lecciones y buenas prácticas que resulten útiles para la comunidad técnica, operadores, CSIRTs y responsables de seguridad.

### ICP-2 Update or RIR Governance Document
Speakers: Esteban Lescano, Jorge Villa, Ricardo Patara
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/actualizacion-sobre-el-documento-de-gobernanza-de-los-rir-version-2-lacnic45.pdf | video: https://youtu.be/Irq2SM-iBDw
A session for sharing the status of the process for updating ICP-2 , the document that outlines the principles and criteria for the governance of Regional Internet Registries. Presenters will review the progress made so far, the main comments received during community consultations, and the next steps ahead. The session will provide an opportunity to understand how this discussion is evolving and why it is important for the future of the regional Internet registry system. Un espacio para compartir en qué etapa está hoy el proceso de actualización de ICP-2 , el documento que reúne los principios y criterios vinculados a la gobernanza de los RIRs. Durante la sesión se repasará el camino recorrido hasta ahora, los principales comentarios surgidos en las consultas con la comunidad y los próximos pasos previstos. Será una oportunidad para entender de manera simple cómo avanza esta discusión y por qué es importante para el futuro del sistema de registros regionales de Internet.

### The Value of Open Standards
Speakers: Alvaro Retana
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-open-standards-keynote-alvaro-retana.pdf | video: https://youtu.be/ZUbmo9UvJik
In an era of rapid digital transformation, the infrastructure that supports global connectivity depends on the robustness and interoperability of open standards. This session will explore the strategic value proposition for organizations to move beyond passive implementation and participate directly in standards development. We will examine how active participation in standardization bodies and other industry councils allows organizations to future-proof their infrastructure, drive interoperability, and promote innovation. By contributing to the collaborative development of open standards, organizations do more than simply build better networks. They help safeguard the growth and stability of the global Internet ecosystem. En una era de rápida transformación digital, la infraestructura que sustenta la conectividad global depende de la solidez e interoperabilidad de los estándares abiertos. Esta charla explora la propuesta de valor estratégica para que las organizaciones vayan más allá de la implementación pasiva y participen directamente en el desarrollo de estándares. Examinaremos cómo la participación activa en organismos de estandarización y otros consejos industriales permite a las organizaciones: preparar su infraestructura para el futuro, impulsar la interoperabilidad y promover la innovación. Al contribuir al desarrollo colaborativo de estándares abiertos, las organizaciones hacen más que simplemente construir mejores redes; ayudan a salvaguardar el crecimiento y la estabilidad del ecosistema global de Internet.

### IPv6 from an Operational Perspective: Experiences and Challenges for Internet Evolution
Speakers: Lee Howard, Tomás Lynch, Henri Alves de Godoy, Orlando Flores Avila
video: https://youtu.be/UdvoEC9V6N4
IPv6 remains key for the Internet&#8217;s evolution, and many organizations are deploying the protocol on a significant scale. Recently, it was announced that IPv6 access to applications hosted by Google exceeded 50% for the first time. However, IPv6 deployment continues to present technical, operational, and coordination challenges across various environments. This panel will bring together the perspectives of data centers, ISPs, academia, and the technical Internet ecosystem to discuss barriers, lessons learned, and opportunities for advancing IPv6 adoption. Based on their experiences, the session will seek to identify persistent obstacles, highlight effective strategies, and discuss how different stakeholders can help accelerate a more sustainable and scalable transition aligned with regional needs. IPv6 sigue siendo una pieza clave para la evolución de Internet y diferentes organizaciones vienen desplegándolo de formas significativas. Recientemente se hizo público que la cantidad de accesos por IPv6 a las aplicaciones alojadas en Google superaron el 50% por primera vez Sin embargo, el despliegue de IPv6 aún presenta desafíos técnicos, operativos y de coordinación en distintos entornos. Este panel reunirá miradas complementarias desde datacenters, ISPs, academia y el ecosistema técnico de Internet para conversar sobre barreras, aprendizajes y oportunidades en la adopción de IPv6. A partir de experiencias, la sesión buscará poner en común qué obstáculos persisten, qué estrategias están dando resultado y cómo distintos actores pueden contribuir a acelerar una transición más sostenible, escalable y alineada con las necesidades de la región.

## LACTLD (26/05/2026)
### LACTLD
LACTLD is a nonprofit association that brings together Latin American and Caribbean ccTLD administrators to foster cooperation, promote development, and represent the interests of its members. Among other activities, LACTLD holds several annual workshops on business, technical, legal, and policy issues. During the workshops, members of the community come together to share and exchange experiences, solutions, best practices, and common projects. LACTLD es una asociación sin fines de lucro que agrupa a los administradores de ccTLD de América Latina y el Caribe con los objetivos de fomentar la cooperación, promover el desarrollo y representar los intereses de sus miembros. Entre sus actividades, LACTLD realiza una serie de talleres anuales sobre asuntos comerciales, técnicos, legales y de políticas. Durante los talleres, los ccTLD miembros tienen la oportunidad de intercambiar experiencias, soluciones, mejores prácticas y proyectos comunes.

## Foro Técnico de LACNIC (26/05/2026)
### Introduction to the LACNIC Technical Forum
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/introduccion-foro-tecnico-de-lacnic-lacnic-45-az-v2.pdf | video: https://youtu.be/br9KtesF9LI
The LACNIC Technical Forum (LTF) is a space for the LACNIC community to share and discuss Internet technology related topics. It will include technical presentations on cybersecurity, IPv6, DNS, the Internet of Things, interconnection, network operation, regulations, and other relevant topics. El Foro Técnico de LACNIC (FTL) es un espacio de intercambio y discusión de la comunidad de LAC sobre tecnologías de Internet. Se presentan trabajos técnicos que incluyen temáticas como ciberseguridad, IPv6, DNS, Internet de las Cosas, interconexión, operación de redes, regulación, entre otros.

### IP Geolocation Update
Speakers: Lee Howard
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic4-ipgeo-v2.pdf | video: https://youtu.be/VaxG99ELJB0
No description published; title, speakers and materials only.

### Detecting BGP Route Hijacking on the Internet Using a Hybrid AI Model
Speakers: Carlos Mariano Ramírez Amaya
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/secuestrorutasbgp-lacnic45.pdf | video: https://youtu.be/UIDNCaAzVRU
No description published; title, speakers and materials only.

### Exploring the State of the Art of CGNAT
Speakers: Fernando Frediani
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic2026-ftl-en-busca-del-estado-del-arte-del-cgnat-fernando-frediani-es.pdf | video: https://youtu.be/WUY-fz84fEk
No description published; title, speakers and materials only.

### The annoying Noisy BGP Speakers
Speakers: Alejandro Acosta, Elisa Peirano
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/BGP-Noisy-speakers-ElisaP-AleA-v2.pdf | video: https://youtu.be/9j1Nb7MN5ew
No description published; title, speakers and materials only.

### What Is My RPKI Validator Doing Right Now?
Speakers: Santiago Aggio
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/que-estara-haciendo-mi-validador-rpki-en-este-momento-lacnic45.pdf | video: https://youtu.be/k263dzMIiI4
No description published; title, speakers and materials only.

### EVPN & VXLAN: The New Language of Modern Peering
Speakers: Ariel Weher
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/weher-202605261225-peering_moderno-vxlan_evpn.pdf | video: https://youtu.be/mrgn6HbzmmY
No description published; title, speakers and materials only.

## La academia y la comunidad técnica en la región: sinergias, desafíos y oportunidades (26/05/2026)
### Academia, the technical community and the industry: challenges, synergies and collaboration opportunities
The activity will consist of a dynamic work and exchange session between participants guided by moderators. The objective of the activity is to promote joint work between participants from academia, the technical community and industry, and to identify concrete challenges and problems for Internet operations, collaboration ideas and specific actions. Participants will select their preferred topics between the 4 priority lines of research and work of the collaboration project in applied research, along with a fifth open axis on emerging topics. The themes and challenges that each group identifies will guide the new collaborations that LACNIC develops with research groups in academic institutions in the region. Registration &nbsp; La actividad consistirá en una sesión dinámica de trabajo e intercambio entre los participantes guiada por moderadores. El objetivo de la actividad es promover el trabajo conjunto entre participantes de la academia, la comunidad técnica y la industria, e identificar desafíos y problemas concretos para las operaciones de Internet, ideas de colaboración y acciones específicas. Los participantes seleccionarán sus temáticas de preferencia entre las 4 líneas de investigación y trabajo prioritarias para el proyecto de colaboración en investigación aplicada, junto a un quinto eje abierto sobre temáticas emergentes. Las temáticas y desafíos que cada grupo identifique permitirán orientar las nuevas colaboraciones que LACNIC desarrolle con grupos de investigación en instituciones académicas de la región. Registro

## Redes de acceso en Panamá: el paso pendiente hacia IPv6 (26/05/2026)
### Access Networks in Panama: The Pending Step Towards IPv6
Speakers: Carlos Martínez, Alejandro Acosta, Guillermo Cicileo, Erika Vega Valenzuela
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/redes-de-acceso-en-panama-el-paso-pendiente-hacia-ipv6-lacnic45.pdf
Panama still has a way to go in the adoption of IPv6 by Internet service providers. This activity will attempt to review the present situation, understand why the country lags behind Central America and neighboring countries, and create a space for discussing the challenges and opportunities to promote a more extensive deployment that is both stable and sustainable. Panamá todavía tiene un camino pendiente en la adopción de IPv6 por parte de los proveedores de Internet. Esta actividad propone revisar el escenario actual, entender por qué el país permanece por detrás de Centroamérica y de los países vecinos y generar un espacio de intercambio sobre los desafíos y oportunidades para impulsar un despliegue más amplio, que a la vez sea estable y sostenido

## LACNIC (27/05/2026)
### Spaces within LACNIC for Strengthening the Role of the Technical Community
Speakers: Laura Kaplan
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/espacios-de-lacnic-para-fortalecer-roles-de-la-comunidad-tecnica-lacnic45.pdf | video: https://youtu.be/rmS6iJGQtUQ
An overview of the community spaces that help define policies, strengthen transparency and support LACNIC&#8217;s governance. Un recorrido por los espacios comunitarios que ayudan a definir políticas, fortalecer la transparencia y sostener la gobernanza de LACNIC.

### Case Study: Route Hijacking, RPKI, and Social Engineering
Speakers: Carlos Martínez, Guillermo Cicileo
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/secuestros-de-rutas-en-bgp-el-extrano-caso-del-pdf-falso-lacnic45.pdf | video: https://youtu.be/jDwbvmqJZpY
An interactive presentation of a real-world case study, featuring audience participation and key lessons learned for routing operation and security. Presentación interactiva de un caso real, con participación de la audiencia y principales aprendizajes para la operación y la seguridad de ruteo.

### Hands-on ASPA: Configuration and Lessons Learned
Speakers: Carlos Martínez, Guillermo Cicileo
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-aspa-fundamentos.pdf | video: https://youtu.be/jDwbvmqJZpY?si=AINliImhXzawKGQU&t=1347
A guided demonstration and hands-on exercise on ASPA configuration, connecting the previous case study to its operational application. Demostración guiada y ejercicio práctico de configuración de ASPA, conectando el caso anterior con su aplicación operativa.

### B-Root Server in the LACNIC Region
Speakers: John Heidemann
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/b_root_in_latam_2026-04-28-lacnic45.pdf | video: https://youtu.be/oSM8bHdCnTM
In this session, we will explore the increasingly important role of the B-Root server in the LACNIC region, beginning with our deployment in Chile in 2019, through the renumbering using LACNIC address space in 2023, to our plans for 2026 and 2027. While reliable operation remains our primary objective, we will also discuss the B-Root server&#8217;s role in DNS research, including the deployment of DNS-over-TLS in 2023 and our commitment to supporting zone transfers for organizations interested in maintaining a local copy in the cache of the root server, in accordance with REF-8806. Exploraremos el papel cada vez más importante de B-Root en la región de LACNIC, desde nuestro despliegue en Chile en 2019, pasando por la renumeración en 2023 dentro del espacio de direcciones de LACNIC, hasta nuestros planes para 2026 y 2027. Si bien la operación confiable es nuestro principal objetivo, también hablaremos sobre el rol de B-Root en la investigación sobre DNS, con el despliegue de DNS-over-TLS en la raíz en 2023 y nuestro compromiso de apoyar transferencias de zona para organizaciones interesadas en contar con una copia local en caché de la raíz, de acuerdo con REF-8806.

## Foro Público de Políticas (27/05/2026)
### Introduction by the Chairs
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/presentacion-fpp-lacnic-45-v2.pdf | video: https://youtu.be/eBbwsIxk3OY
LACNIC’s Public Policy Forum is a space for presenting and discussing the policies to be applied in our region for managing Internet number resources. It is an open forum where anyone interested in doing so may participate. El Foro Público de Políticas de LACNIC es el lugar donde se presentan y discuten propuestas sobre las políticas a aplicar en nuestra región, en relación a la administración de los recursos numéricos. El foro es abierto a todos los interesados.

### ASO AC Update
Speakers: Esteban Lescano, Jorge Villa, Ricardo Patara
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic-45-aso-update.pdf | video: https://youtu.be/ckJdtI0l-4s
No description published; title, speakers and materials only.

### NRO EC Update
Speakers: Ernesto Majó
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/nro-update-lacnic45-v2.pdf | video: https://youtu.be/vCYD3PPLBvA
No description published; title, speakers and materials only.

### Open Mic
video: https://youtu.be/lCPwp17MQ6I
No description published; title, speakers and materials only.

## Grupo de trabajo de Mediciones de Internet (IMWG) (27/05/2026)
### Introduction: Internet Measurements Working Group
Speakers: Massimo Candela
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/imwg_panama_2026.pdf | video: https://youtu.be/-J4TPS0_suI
No description published; title, speakers and materials only.

### Sources of Information on Internet Number Resources
Speakers: Carlos Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/fuentes-de-datos-recursos-de-numeracion-internet-lacnic45.pdf | video: https://youtu.be/R5sPFenTlko
No description published; title, speakers and materials only.

### LightScope: Turning Unused Production Ports into Global Network Telescopes and Honeypots
Speakers: Eric Kapitanski
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic-45-lightscope-v2.pdf | video: https://youtu.be/zr7wZqv1MwY
No description published; title, speakers and materials only.

### New Community Dataset: From Internet Outages to DDoS Attacks.
Speakers: Jelena Mirkovic
video: https://youtu.be/OZSdKBrmv38
No description published; title, speakers and materials only.

### Routing under siege: how traffic engineering decisions facilitate prefix hijackings
Speakers: Renan Paredes Barreto
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/enrutamiento-bajo-presion-como-las-decisiones-de-ingenieria-de-trafico-facilitan-el-secuestro-de-prefijos-lacnic45.pdf | video: https://youtu.be/pRq5GjlLnUI
No description published; title, speakers and materials only.

### Monitoring Internet Connectivity in Healthcare Facilities: A Large-Scale Measurement Experience in Brazil
Speakers: Cristiane Honora Millan
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/Cristiane-Millan-Lacnic45.pdf | video: https://youtu.be/Npfh4CT98kU
No description published; title, speakers and materials only.

### Closing Ceremony: Internet Measurements Working Group
video: https://youtu.be/Xti-0OAxq6U
No description published; title, speakers and materials only.

## Asamblea General Asociados de LACNIC (27/05/2026)
### Ordinary Member Assembly
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/asamblea-Informe-anual-final-lacnic45.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/informe-anual-de-actividades-del-directorio-2025.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/reporte-financiero-2025.pdf | video: https://youtu.be/SL2v7PDf9aA
Documents published by LACNIC are originally written in Spanish. In case of discrepancy, the Spanish version will prevail. This document and/or information was originally written in Spanish, the official language of Uruguay, the country where LACNIC is legally incorporated and whose laws and regulations govern the organization. Likewise, unofficial information and/or documents are also written in Spanish, as this is the language in which most of LACNIC&#8217;s advisors and officers work and communicate. We do our best to ensure that our translations are reliable and serve as a guide for our non-Spanish-speaking members. However, discrepancies may exist between the translations and the original document and/or information written in Spanish. In such cases, the original text written in Spanish will always prevail. REFERENCE DOCUMENTATION: Invitation to attend the Ordinary Member Assembly Power of Attorney for the Ordinary Member Assembly* Voters’ registry ** Annual report 2025 * The power of attorney can be sent by mail to membresia@lacnic.net or presented during the event before receiving the voting material. ** Adhering members rights: to participate in the General Assembly with speaking privileges but without the right to vote. The person responsible for voting in the assembly or sign the power of attorney on behalf of the organization is the membership contact listed in our database (LACNIC – Nic Brasil – Nic México). Do you know who your representative is? We kindly request you to contact LACNIC through membresia@lacnic.net , inform the name of your organization together with the ORGID or ASN/CNPJ number. In cases where the membership contact is not a real person or is no longer more in the company, it is requested to update the information before the Assembly or the responsible to sign the power of attorney will be a legal representative of the organization (and it will be necessary to send a document that proves that he/she is legally entitled to sign on behalf of the organization). Los documentos que LACNIC publica son originariamente en español, por tanto este será el idioma que prevalezca. El presente documento y/o información ha sido redactado en idioma español, en virtud de que el mismo es el idioma oficial en Uruguay, país en donde LACNIC se encuentra establecida y cuyas regulaciones debe cumplir. Asimismo, los documentos y/o informaciones no oficiales también son escritos en español, en virtud de que es el idioma en que se comunican y trabajan la mayoría de los asesores y funcionarios de LACNIC. No obstante lo cual, realizamos nuestros mejores esfuerzos para que la traducción del mismo sea fehaciente y constituya una guía para nuestros asociados no hispanoparlantes, sin embargo puede que existan discrepancias entre la misma y el documento y/o información original redactado en español. En cualquier caso prevalecerá siempre el texto original redactado en español. DOCUMENTACIÓN DE REFERENCIA: Convocatoria Asamblea Carta poder Asamblea ordinaria* Padrón Electoral ** Reporte anual 2025 * La carta poder puede ser enviada por correo electrónico a membresia@lacnic.net o presentarla durante el evento antes de retirar el material de votación. ** Derechos de los asociados adherentes: podrán integrar la Asamblea General con voz y sin voto. El responsable de ejercer el voto en la Asamblea o de firmar la carta poder en representación de la organización será el contacto de membresía registrado en nuestra base de datos (LACNIC -Nic Brasil- Nic México). ¿No sabe quién es su representante? Le sugerimos comunicarse con LACNIC a través de membresia@lacnic.net indicando el nombre de su organización junto con el ORGID o el número de ASN/CNPJ. En casos donde el contacto de membresía no sea una persona física o ya no esté más en la organización, se solicita actualizar la información antes de la Asamblea o que un representante legal firme la carta poder y que la organización presente un documento que acredite que esa persona tiene derecho legal de firmar a nombre de la organización.

## Evento social (27/05/2026)
### Social Event
Oceánica (El Bohío) Oceánica (El Bohío)

## Foro Técnico de LACNIC (28/05/2026)
### BGP Optimization for Medium-Sized ISPs: Technical and Financial Decisions Using Open-Source Tools
Speakers: Fernando Tipiani
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/fernando-tipiani-lacnic45-ftl-optimizacion-bgp-para-isps.pdf | video: https://youtu.be/cuiku_FkTPI
No description published; title, speakers and materials only.

### BGP ORIGIN in Practice: Inconsistencies Observed in LACNIC Prefixes
Speakers: Celsa Sánchez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/bgp-origin-v3-lacnic45.pdf | video: https://youtu.be/t4qf4JM5GGQ
No description published; title, speakers and materials only.

### Automating Technical Support at ISPs Using AI Agents and TR-369 (USP)
Speakers: Jaris Aizprúa Barrios
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/LACNIC_FTL_2026_Jaris_Aizprua.pdf | video: https://youtu.be/vwqoQCrLgFk
No description published; title, speakers and materials only.

### Automation and Telemetry applied to BGP Routing Policies
Speakers: Henri Alves de Godoy, Ernesto Sánchez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/automatizacion-y-telemetria-aplicada-a-politicas-de-enrutamiento-bgp.pdf | video: https://youtu.be/FA_p-IipxqM
No description published; title, speakers and materials only.

### Towards detecting DoS attacks in the server's NIC
Speakers: Adrián Lara, Juan Felipe Botero
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lara-botero-lacnic45-v3.pdf | video: https://youtu.be/hQe2kLWE_Ew
No description published; title, speakers and materials only.

### R&D Ambassadors Program: Presentation of Results
Speakers: Guillermo Cicileo, Fernando Tipiani, David Macmahon, José Augusto Canul
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/programa-embajadores-id-2026-guillermo-cicileo.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/desde-la-comunidad-para-la-region-mi-impacto-como-embajador-lacnic-id-2025-lacnic45-david-macmahon.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-embajadores-fernando-tipiani.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/emb-2025-2026.pdf | video: https://youtu.be/9aCSMhXPe6A
No description published; title, speakers and materials only.

## LACNOG (28/05/2026)
### LACNOG Institutional Session
Speakers: Carlos Martínez, Jorge Villa, Erika Vega Valenzuela
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/llamado-a-trabajos-lacnog-2026.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnog2026-plan-de-trabajo-lacnic45-v2.pdf | video: https://youtu.be/hTMDHL-skiY
No description published; title, speakers and materials only.

### Channelmania! Secure the Future of your DWDM Network Topology Remaining Flexible to 1.6T Technology
Speakers: Gerhard Stein
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/flexoptix-brainfuck-lacnic45.pdf | video: https://youtu.be/Ioy-GKR0NpE
No description published; title, speakers and materials only.

### Impacts of LLM Traffic on Peering Strategies
Speakers: Tomás Lynch
slides: https://apievt.lacnic.net/wp-content/uploads/2026/05/llm-traffic-implications-for-peering-strategy.pdf | video: https://youtu.be/kSSug2XqAxc
No description published; title, speakers and materials only.

### VxLAN Configuration Lab
Speakers: Ariel Weher
video: https://youtu.be/eibmRu2GvEk
No description published; title, speakers and materials only.

## LACNIC (28/05/2026)
### Panel. A Turning Point for Digital Infrastructure: Data Centers, Submarine Cables, IXPs, and ISPs
Speakers: Evandro Varonil, Pablo Ruidiaz, Giovanni King, Carlos Pazmiño
video: https://youtu.be/le0GMOKWo80
As Latin America and the Caribbean experience an unprecedented digital transformation, this panel will bring together regional leaders and specialists from key sectors of Internet infrastructure —data centers, submarine cables, internet exchange points (IXPs), and Internet service providers (ISPs)— to explore the region&#8217;s current challenges, share trends and concrete actions that are redefining connectivity, and analyze how emerging technologies such as artificial intelligence, edge computing, gaming, and high-demand streaming are increasing the pressure on digital infrastructure. The goal will be to discuss how to strengthen Internet capacity, resilience, and competitiveness throughout Latin America and the Caribbean. En un momento en que América Latina y el Caribe atraviesan una transformación digital sin precedentes, este panel regional reunirá a líderes y especialistas de sectores clave de la infraestructura de Internet —centros de datos, cables submarinos, puntos de intercambio de tráfico (IXP) y proveedores de acceso a Internet (ISP)— para conversar sobre los desafíos actuales de la región, compartir tendencias y acciones concretas que están redefiniendo la conectividad, y analizar cómo tecnologías emergentes como la inteligencia artificial, el edge computing, el gaming y el streaming de alta demanda están elevando las exigencias sobre la infraestructura digital. El objetivo común será debatir cómo fortalecer la capacidad, la resiliencia y la competitividad de Internet en América Latina y el Caribe.

### LACNIC 45 Wrap-Up
Speakers: Fanny Lospennato, Esteban Lescano
video: https://youtu.be/dLzOn0AYm7c
No description published; title, speakers and materials only.

