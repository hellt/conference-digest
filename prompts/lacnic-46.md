>>> HOW TO RUN THIS <<<
This is the digest prompt for lacnic-46. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/lacnic-46.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/lacnic-46.md
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

Below is the program for LACNIC 46 (operator). Read it and produce a digest
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
conference: LACNIC 46
type: operator
source_url: https://lacnic46.lacnic.net/
generated: 2026-11-01
registry_key: lacnic-46
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Reunión de LAC CSIRTs ()
### LAC CSIRTs (By invitation)
The goal of this activity is to create spaces where participants can share and collaborate on security incident management issues affecting the region. In line with this, we propose that those CSIRTs that are in operation provide a brief update on their teams. In addition, a space will be reserved to identify possible topics of interest or common projects that can be addressed during the week. The meeting is aimed at all CSIRT members attending the event, as well as at anyone who is interested in creating their own teams or who is in the process of creating a CSIRT. Esta actividad pretende generar espacios de intercambio y de colaboración en temas de gestión de incidentes de seguridad en la región. Para ellos proponemos que los CSIRTs constituídos brinden un breve update de sus equipos. Además, se destinará un espacio para identificar posibles temas de interés o proyectos en común que se puedan abordar durante la semana. IMPORTANTE: Dirigido a todos los integrantes de los CSIRTs que asistan al evento, así como a staff de CSIRTs en proceso de ingreso al FIRST iniciado formalmente.

## FIRST ()
### Capture The Flag (FIRST)
This Capture the Flag (CTF), organized by CERT.br/NIC.br, is a Replay of the competition originally held at the 38th Annual FIRST Conference. This is a defensive CTF organized since 2012 by the FIRST Seclounge SIG. The CTF is a competitive exercise comprised of individual challenges that require analytic cybersecurity skills to be solved. The challenges were created by incident handlers and are based on incident handling and blue team skills, with topics covering different knowledge areas such as networking, forensics, web and cryptography. Players form teams of up to four people to combine their expertise, share experiences, and develop their skills. Teams earn points for each solved challenge, and the team with the highest score at the deadline wins the CTF. * Date and Time The FIRST CTF Replay will take place on TUESDAY, from 09:00h to 18:00h. Only in-person attendees can participate. * Registration The registration will be open on Monday. You can meet the organizers at [LAC-CSIRT ROOM] from 16:30h to 18h00 to validate your registration. * Winners Presentation The winners will give a five-minute presentation on Wednesday, followed by a wrap-up session among all participants, starting at 11:00h at [De Los Cerros II-III]. ⁠How to register: https://lacnic.firstseclounge.org/ Registration Code: !_2026LACNIC46_! Este Capture the Flag (CTF) es organizado por CERT.br/NIC.br y es un replay de la competencia que se llevó a cabo originalmente en la 38.ª Conferencia Anual de FIRST. Se trata de un CTF defensivo que el FIRST Seclounge SIG organiza desde 2012. El CTF es un ejercicio competitivo compuesto por desafíos individuales que requieren habilidades analíticas de ciberseguridad para ser resueltos. Los desafíos fueron creados por manejadores de incidentes y se basan en la gestión de incidentes y habilidades de equipos de defensa ( blue team ). Los temas abarcan diferentes áreas de conocimiento como redes, ciencia forense, web y cifrado. Los jugadores forman equipos de hasta cuatro personas para combinar sus conocimientos, compartir experiencias y desarrollar sus habilidades. Cada equipo suma puntos por cada desafío resuelto y el equipo con la puntuación más alta al finalizar el tiempo asignado es el ganador del CTF. *Fecha y hora El FIRST CTF Replay se llevará a cabo el MARTES, de 09:00 a 18:00. Solo podrán participar los asistentes presenciales. ⁠Cómo registrarse: https://lacnic.firstseclounge.org/ Código de registro: !_2026LACNIC46_! *Registro El registro abrirá el lunes. Puede reunirse con los organizadores en la [SALA LAC-CSIRT] de 16:30 a 18:00 para validar su registro. * Presentación de los ganadores El miércoles, los ganadores darán una presentación de cinco minutos. A continuación habrá una sesión de cierre entre todos los participantes a partir de las 11:00 en [De Los Cerros II-III].

## Registro (18/10/2026)
### Accreditation
No description published; title, speakers and materials only.

## Orientación para nuevos participantes (19/10/2026)
### Orientation Session for Newcomers
Speakers: Laura Kaplan, Ernesto Majó, Jorge Villa, Erika Vega Valenzuela
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/orientacion-para-nuevos-participantes-v1-laura-kaplan.pdf | video: https://youtu.be/i2JmaxyK1aM
Welcome session for first-time attendees at a LACNIC meeting. It will offer a practical guide to help you make the most of the event, including sessions, tutorials, panel discussions, networking opportunities, and social activities. Sesión de bienvenida para quienes asisten por primera vez a LACNIC 46 LACNOG2026. Ofrecerá una guía práctica para aprovechar mejor la agenda del evento, incluyendo sesiones, tutoriales, paneles, espacios de networking y encuentros sociales.

## Tutoriales (19/10/2026)
### Mission Accomplished? The 2026 KSK Rollover Story
slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/mision-cumplida-la-historia-del-rollover-de-la-ksk-de-2026-v1-nicolas-antoniello-carlos-martinez.pdf
The key was rolled — but that’s not the end of the story. This session revisits the 2026 Root KSK Rollover, what worked, what we learned along the way, and how those lessons can help prepare the DNS community for the future. La clave se renovó, pero la historia no termina ahí. En esta sesión repasaremos el rollover de la KSK de la zona raíz de 2026, qué funcionó, qué aprendimos durante el proceso y cómo estas lecciones pueden ayudar a la comunidad del DNS a prepararse para el futuro.

### Resource Management - MiLACNIC/Security Module
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/adm-de-recursos-mi-lacnic-modulo-de-seguridad-v1-lorenzo-abelenda-guillermo-pereyra-graciela-martinez-giordano-julio-buiza.pdf
The main goal of this tutorial is to provide detailed information on the features and functions of MiLACNIC and how to use them. It is geared towards representatives of organizations that are already members and have been assigned IPv4 and/or IPv6 resources directly by LACNIC and who wish to learn more about the advantages of using the functions offered by MiLACNIC, such as how to mitigate operational risks by maintaining updated records for assigned resources. The two new tools available in MiLACNIC to strengthen RPKI management and Internet routing security will be presented: ASPA: Allows Autonomous Systems (AS) to declare their authorized transit providers, helping detect BGP route leaks. Delegated RPKI: Allows organizations to independently manage their own RPKI Certificate Authority (CA), maintaining control over the issuance and management of their RPKI objects. LACNIC CSIRT will present the MiLACNIC Security Module, where users can submit information about resources involved in security events. They will also explain the importance of correcting these problems, using strong passwords, and the need for a second authentication factor for data protection. Finally, they will touch upon the concepts of what a CSIRT is and the role of LACNIC CSIRT in managing computer security incidents. Important: Because NIRs in the LACNIC region use a different platform, the material shown during the presentation will not be available to members of organizations in Brazil. In the case of Mexico, the reports and RPKI module are compatible with what will be shown in this presentation. Este tutorial tiene como principal finalidad conocer en profundidad el uso y las funcionalidades de MiLACNIC. Está orientado a representantes de organizaciones que ya son miembros asociados y poseen recursos IPv4 y/o IPv6 asignados directamente por LACNIC y quieren conocer más acerca de las ventajas de utilizar las funcionalidades de MiLACNIC, como por ejemplo cómo mitigar riesgos de operación manteniendo registros actualizados para los recursos asignados. Se presentarán las dos nuevas herramientas disponibles en MiLACNIC para fortalecer la gestión de RPKI y la seguridad del enrutamiento de Internet: ASPA: Permite declarar los proveedores de tránsito autorizados de un Sistema Autónomo (AS), contribuyendo a la detección de fugas de rutas ( route leaks ) en BGP. RPKI Delegado: Permite a las organizaciones gestionar de forma autónoma su propia Autoridad Certificadora (CA) de RPKI, manteniendo el control sobre la emisión y administración de sus objetos RPKI. El CSIRT de LACNIC presentará el Módulo de Seguridad de MiLACNIC, donde se envía la información de recursos involucrados en eventos de seguridad informática. Se explicará la importancia de corregir esos problemas, de utilizar contraseñas seguras y la necesidad de un segundo factor de autenticación para la protección de los datos. También se abordarán de forma breve los conceptos de qué es un CSIRT y el rol del CSIRT de LACNIC en la gestión de incidentes de seguridad informática. Aclaración importante: debido a que los NIRs de LACNIC utilizan una plataforma distinta, el material mostrado en la presentación no está disponible para miembros de organizaciones en Brasil. En el caso de México, el módulo de RPKI y reportes son compatibles con lo que se expondrá en esta presentación.

### Hacia la transición definitiva de redes IPv6 Only
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/ipv6-and-ipv6-mostly-troubleshooting-tips-and-war-stories-jen-linkova-v1-jen-linkova.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/ipv6-mostly-using-ipv4-to-turn-ipv4-off-v1-jen-linkova.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/hacia-la-transicion-definitiva-de-redes-ipv6-only-v1-alejandro-acosta.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/464xlat-en-la-practica-plat-con-jool-clat-en-openwrt-y-cabecera-mikrotik-v1-uesley-correa.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/enrutamiento-ipv4-con-next-hop-ipv6-only-rfc8950-fundamentos-tecnicos-y-pruebas-con-mikrotik-routeros-v7-v1-jose-cotua.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/hacia-la-transicion-definitiva-de-redes-ipv6-only-v1-jose-cotua.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/delegacion-de-prefijos-dhcpv6-pd-v1-jose-cotua.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/delegacion-de-prefijos-dhcpv6-pd-v1-jose-cotua.pdf
Adoptar IPv6 va mucho más allá de asegurar la estabilidad y el futuro de nuestras plataformas en línea; representa la llave para desbloquear tecnologías de vanguardia y optimizaciones estructurales clave. Este taller ofrece un enfoque práctico enfocado en el despliegue de infraestructuras basadas únicamente en IPv6 (IPv6 Only). Analizaremos configuraciones críticas como NAT64 para garantizar la comunicación con el entorno IPv4 tradicional y exploraremos la transición progresiva hacia topologías IPv6 Mostly. Asimismo, implementaremos el enrutamiento nativo de tráfico IPv4 sobre redes IPv6 y demostraremos cómo operar un resolvedor DNS exclusivo para IPv6 sin comprometer la compatibilidad del sistema. Entre las novedades para este taller traeremos la opción DHCP 108 vía DHCP-Relay y enrutamiento nativo de tráfico IPv4en redes IPv6 con Mikrotik En el escenario actual, posponer la migración a IPv6 no es una opción: significa aceptar el aislamiento tecnológico y quedar al margen de la infraestructura global de internet. Adoptar IPv6 va mucho más allá de asegurar la estabilidad y el futuro de nuestras plataformas en línea; representa la llave para desbloquear tecnologías de vanguardia y optimizaciones estructurales clave. Este taller ofrece un enfoque práctico enfocado en el despliegue de infraestructuras basadas únicamente en IPv6 (IPv6 Only). Analizaremos configuraciones críticas como NAT64 para garantizar la comunicación con el entorno IPv4 tradicional y exploraremos la transición progresiva hacia topologías IPv6 Mostly. Asimismo, implementaremos el enrutamiento nativo de tráfico IPv4 sobre redes IPv6 y demostraremos cómo operar un resolvedor DNS exclusivo para IPv6 sin comprometer la compatibilidad del sistema. Entre las novedades para este taller traeremos la opción DHCP 108 vía DHCP-Relay y enrutamiento nativo de tráfico IPv4en redes IPv6 con Mikrotik En el escenario actual, posponer la migración a IPv6 no es una opción: significa aceptar el aislamiento tecnológico y quedar al margen de la infraestructura global de internet.

### Interactive Workshop: How LACNIC Manages Your Internet Resources and How You Can Influence the PDP
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/taller-interactivo-como-administra-lacnic-tus-recursos-en-internet-y-como-puedes-influir-en-ello-v1-mariela-rocha-franco-cabrera.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/taller-interactivo-como-administra-lacnic-tus-recursos-en-internet-y-como-puedes-influir-en-ello-v1-mariela-rocha-franco-cabrera.pdf
This workshop is an opportunity to practically understand how the community defines the rules for the administration of IP addresses and Autonomous Systems in our region, through LACNIC’s Policy Development Process (PDP). Throughout the workshop, we will detail each phase of the PDP, share experiences, and hold interactive discussions with collaborators involved in the process. Additionally, we will organize a group activity so that participants can simulate the process, exchange ideas, and experience what it’s like to actively engage in discussions and contribute to LACNIC’s work. Este taller es una oportunidad para conocer de forma práctica cómo la comunidad define las reglas sobre la administración de direcciones IP y Sistemas Autónomos en nuestra región, a través del Proceso de Desarrollo de Políticas (PDP) de LACNIC. A lo largo del taller, detallaremos cada fase del PDP, compartiremos experiencias y charlas interactivas con colaboradores involucrados en el proceso. Además, organizaremos una actividad grupal para que los participantes puedan simular el proceso, intercambiar ideas, y experimentar cómo es involucrarse activamente en las discusiones y así contribuir a la labor de LACNIC.

### BGP in 2026: Threats, Incidents, and Solutions
slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/bgp-en-2026-amenazas-incidentes-y-soluciones-v1-erika-vega-valenzuela-alvaro-retana-guillermo-cicileo.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/bgp-en-2026-amenazas-incidentes-y-soluciones-v1-erika-vega-valenzuela-alvaro-retana-guillermo-cicileo.pdf | video: https://youtu.be/-rJxv367cE8
Routing system security is essential to Internet stability and resilience. In this tutorial, we will analyze the main threats and incidents affecting BGP, including route hijacking and route leaks. We will also discuss the practices and technologies available to prevent, detect, and mitigate their impact. Using real-world examples, we’ll see how tools and standards such as IRR, RPKI, and origin validation (ROV), BGP Roles, and ASPA can help operators protect their networks. We will also cover mechanisms for responding to attacks, such as RTBH, the BLACKHOLE community, and BGP Flowspec. By the end of this tutorial, participants will be able to identify the main risks associated with BGP routing, identify which mechanisms can be used to mitigate each type of incident, and assess which measures they can implement in their own networks. They will also take away a practical roadmap to gradually advance in the adoption of best practices in routing security, from properly publishing and validating information to incident readiness and new path protection technologies. La seguridad del sistema de ruteo es fundamental para la estabilidad y resiliencia de Internet. En este tutorial analizaremos las principales amenazas e incidentes que afectan a BGP, como secuestros de rutas y route leaks, y las prácticas y tecnologías disponibles para prevenirlos, detectarlos y mitigar su impacto. A partir de casos reales, veremos cómo herramientas y estándares como IRR, RPKI y la validación de origen (ROV), BGP Roles y ASPA pueden ayudar a los operadores a proteger sus redes. También abordaremos mecanismos de respuesta ante ataques, como RTBH, la comunidad BLACKHOLE y BGP Flowspec. Al finalizar el tutorial, los participantes podrán identificar los principales riesgos asociados al ruteo BGP, reconocer qué mecanismos permiten mitigar cada tipo de incidente y evaluar qué medidas pueden aplicar en sus propias redes. Además, se llevarán una hoja de ruta práctica para avanzar progresivamente en la adopción de buenas prácticas de seguridad de ruteo, desde la correcta publicación y validación de información hasta la preparación frente a incidentes y nuevas tecnologías de protección del path.

### Secure Routing and Origin Validation Lab
slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/laboratorio-de-ruteo-seguro-y-validacion-de-origen-v1-santiago-aggio.pdf | video: https://youtu.be/C1e0hJ4zHWA
This lab focuses on exploring the latest tools and best practices for enhancing Internet routing security. It will cover the monitoring of BGP advertisements, beginning with a manual review followed by an introduction to automation engines for RPKI configuration, along with the application of filters to help mitigate attacks. Participants will have access to a virtual lab where they will configure devices using automation tools presented in the tutorial. Requirements: Participants are recommended to have prior knowledge of BGP, RPKI, and IRR. Topics to be covered: Introduction to the current challenges in Internet routing and strategies for enhancing BGP security. BGP peering configuration in an IXP environment. Use of the FORT validator to verify prefixes announced by the participants. Monitoring BGP and RPKI announcements. Generating filters based on AS-SET records in the LACNIC IRR. Route hijacks and mitigation techniques Automation with Ansible: Configuring validators, ACLs, and filters. Este laboratorio se centra en explorar las herramientas más recientes y las mejores prácticas para mejorar la seguridad en el ruteo de Internet. Se abordará el monitoreo del estado de los anuncios BGP, comenzando con una revisión manual y continuando con una introducción a motores de automatización para la configuración de RPKI y la aplicación de filtros que ayudan a mitigar ataques. Los participantes tendrán acceso a un laboratorio virtual en el que configurarán equipos utilizando herramientas de automatización presentadas en el tutorial. Requisitos previos: Se recomienda que los participantes tengan conocimientos previos sobre el funcionamiento de BGP, RPKI e IRR. Temas a abordar: Introducción a los desafíos actuales del ruteo en Internet y estrategias para mejorar la seguridad en BGP. Configuración de peering BGP en un entorno de IXP. Uso del validador FORT para verificar prefijos anunciados por los participantes. Monitoreo de anuncios BGP y validación de RPKI. Generación de filtros a partir de registros AS-SET en el IRR de LACNIC. Secuestro de rutas y técnicas de mitigación. Automatización con Ansible: configuración de validadores, ACLs y filtros.

## Cóctel de Bienvenida (19/10/2026)
### Welcome Cocktail
Hilton Hotel, Ground Floor Lobby Hotel Hilton, Lobby planta baja

## LACNIC (20/10/2026)
### Opening Ceremony
Speakers: Esteban Lescano, Erika Vega Valenzuela
video: https://youtu.be/d2panh8u2ZY
Official opening ceremony of the event, where participants will be welcomed and activities will formally begin. Espacio de apertura oficial del evento, en el que se dará la bienvenida a los participantes y se inaugurará formalmente la agenda de actividades.

### The BGP Analyst's Notebook: 17 Years In
Speakers: Doug Madory
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/el-cuaderno-de-un-analista-de-bgp-17-anos-despues-v1-doug-madory.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/el-cuaderno-de-un-analista-de-bgp-17-anos-despues-v1-doug-madory.pdf | video: https://youtu.be/EH-9DQ0_nTE
For the past 17 years, Doug Madory has made a career of watching BGP break and publishing his analysis of it. In this keynote, he reflects on the journey routing security has taken over that time and where it&#8217;s headed next. While routing hygiene has improved substantially, there remain unsolved problems yet to be addressed. Using examples from his work, Doug will look at what&#8217;s changed, what hasn&#8217;t, and what the road ahead looks like for the internet&#8217;s routing system. Durante los últimos 17 años, Doug Madory se ha dedicado a observar las vulnerabilidades del BGP y a publicar sus análisis. En esta ponencia, reflexiona sobre el camino que ha recorrido la seguridad del enrutamiento a lo largo de ese tiempo y hacia dónde se dirige en el futuro. Si bien la higiene del enrutamiento ha mejorado significativamente, aún quedan problemas por resolver. A partir de ejemplos de su trabajo, Doug analizará qué ha cambiado, qué sigue igual y qué podemos esperar del futuro del sistema de enrutamiento de Internet.

### Autonomous Networks: Automation for Greater Agility
Speakers: Eduardo Panciera, Guido Priano, Rodrigo Plaza
video: https://youtu.be/VSXuQ_SclMw
Operators must adapt quickly to customer demands, optimize their resources, and deploy new services with greater agility. Moving toward autonomous networks involves incorporating software and automation to configure, monitor, and adjust the network with less manual intervention. This panel will share experiences and case studies of network automation, its benefits, and implementation challenges. It will also analyze how to begin this process gradually to improve operator efficiency, scalability, and responsiveness. Los operadores necesitan adaptarse rápidamente a las demandas de sus clientes, optimizar sus recursos y desplegar nuevos servicios con mayor agilidad. Avanzar hacia redes autónomas implica incorporar software y automatización para configurar, monitorear y ajustar la red con menor intervención manual. Este panel presentará experiencias y casos de uso sobre automatización de redes, sus beneficios y los desafíos de implementación. También analizará cómo iniciar este proceso de forma gradual para mejorar la eficiencia, la escalabilidad y la capacidad de respuesta de los operadores.

### Going IPv6-Only: From Myths to Modern Network Realities
Speakers: Jen Linkova
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/transicion-a-ipv6-only-de-los-mitos-a-las-realidades-de-las-redes-modernas-v1-jen-linkova.pdf | video: https://youtu.be/tXvvk5DnYaY
While many still believe that IPv6 is simply IPv4 with longer addresses or a distant upgrade we can indefinitely delay, the reality of transitioning away from IPv4 is already here. This presentation unpacks the common myths surrounding IPv6 and dives into the practical, hands-on realities of deploying it within complex enterprise networks. We will explore how modern transition technologies bridge the gap between the old and new worlds and examine how today&#8217;s operating systems actually perform when IPv4 is completely turned off. Ultimately, you&#8217;ll see that going IPv6-only is not only possible but is quickly becoming the standard for high-performing modern networks. Aunque muchos todavía creen que IPv6 es simplemente IPv4 con direcciones más largas o una actualización que se puede posponer indefinidamente, la transición a IPv6 ya es una realidad. Esta presentación desmiente los mitos más comunes en torno a IPv6 y profundiza en aspectos prácticos y reales de su despliegue en redes empresariales complejas. Exploraremos cómo las tecnologías de transición modernas tienden un puente entre el mundo antiguo y el nuevo y analizaremos cómo funcionan los sistemas operativos actuales cuando IPv4 se desactiva por completo. En definitiva, verá que adoptar IPv6-only no solo es posible, sino que se está convirtiendo rápidamente en el estándar para redes modernas de alto rendimiento.

### Legacy Resources: Call for Updated Information
Speakers: Alfredo Verderosa, Julio Buiza
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/recursos-legados-convocatoria-para-actualizar-su-informacion-v1-alfredo-verderosa-julio-buiza.pdf | video: https://youtu.be/I6TT7CQUPGU
In June, LACNIC launched a call for organizations that hold or use legacy IPv4 resources, i.e., resources assigned before the creation of the current Regional Internet Registry system. The process seeks to update registration information, verify the right to use the resources, and formalize the relationship with LACNIC, helping ensure a more legitimate and secure management. In this session, we will explain the scope of the call, which organizations may be included, the steps they must follow, and the main implications of the process. LACNIC inició en junio una convocatoria dirigida a las organizaciones titulares o usuarias de recursos IPv4 legados, asignados antes de la creación del sistema actual de Registros Regionales de Internet. El proceso busca actualizar la información de registro, verificar el derecho de uso de los recursos y formalizar el vínculo con LACNIC, contribuyendo a una gestión más legítima y segura. En este update explicaremos el alcance de la convocatoria, qué organizaciones pueden estar comprendidas, los pasos que deben seguir y las principales implicancias del proceso.

### RIR Governance Document: Progress and Next Steps
Speakers: Esteban Lescano, Ricardo Patara, Jorge Villa
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/documento-de-gobernanza-de-los-rir-avances-y-proximos-pasos-v1-esteban-lescano-ricardo-patara-jorge-villa.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/documento-de-gobernanza-de-los-rir-avances-y-proximos-pasos-v1-esteban-lescano-ricardo-patara-jorge-villa.pdf | video: https://youtu.be/4fboPeq8d7M
In this session, we will provide an update on the ICP-2 review process and the development of the new RIR Governance Document. We will review the progress achieved so far, the current status of the process, and the next steps thar are anticipated. En esta sesión compartiremos una actualización sobre el proceso de revisión de ICP-2 y el desarrollo del nuevo Documento de Gobernanza de los RIR. Repasaremos los principales avances alcanzados hasta el momento, el estado actual del proceso y los próximos pasos previstos.

## LACNOG (20/10/2026)
### LACNOG 2026 Opening Ceremony
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/apertura-lacnog-2026-v1-ariel-weher.pdf | video: https://youtu.be/Ozb1v0GY3Y4
No description published; title, speakers and materials only.

### Keynote Presentation: Lessons in Digital Resilience: Multistakeholder Response and Connectivity Recovery in Venezuela Following the 2026 Earthquakes
Speakers: Alejandra Stolk Ganteaume
slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/presentacion-keynote-lecciones-de-resiliencia-digital-respuesta-multisectorial-y-recuperacion-de-la-conectividad-en-venezuela-tras-los-sismos-de-2026-v1-alejandra-stolk-ganteaume.pdf | video: https://youtu.be/RX5FInLGVPo
No description published; title, speakers and materials only.

### Beyond the Radio Link: Routing Dynamics in LEO Satellite Networks
Speakers: Katarina Stefanović
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/mas-alla-del-enlace-de-radio-dinamica-del-enrutamiento-en-redes-de-satelites-leo-v1-katarina-stefanovic-1.pdf | video: https://youtu.be/btqpBfW38wk
No description published; title, speakers and materials only.

### The mystery of the routes that refused to die
Speakers: Andrés Pugawko
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/el-misterio-de-las-rutas-que-no-querian-morir-v2-andres-pugawko.pdf | video: https://youtu.be/_LmqccuTYAs
No description published; title, speakers and materials only.

### Beyond RPKI Origin Validation: How to Close the Route Leak Gap with ASPA, Today.
Speakers: Sthefany Conceição Duquini
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/mas-alla-de-la-validacion-de-origen-en-rpki-como-cerrar-la-brecha-de-las-route-leaks-con-aspa-hoy-mismo-v2-sthefany-conceicao-duquini.pdf | video: https://youtu.be/VIcW7bJUmSw
No description published; title, speakers and materials only.

### Latency-Based BGP Route Selection – An Intelligent Failover Engine Optimized with Supervised Learning
Speakers: Ernesto Sánchez, Henri Alves de Godoy
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/seleccion-de-rutas-bgp-basada-en-latencia-un-motor-de-failover-inteligente-optimizado-con-aprendizaje-supervisado-1.pdf | video: https://youtu.be/a1eB6ZnUDwQ
No description published; title, speakers and materials only.

### From Classic L3VPN to EVPN: Mastering Type 5 Routes on the Backbone
Speakers: Samuel Emanuel Urbano Tomassoni, Fernando Neiverth
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/de-l3vpn-clasico-a-evpn-dominando-las-rutas-tipo-5-en-el-backbone-v1-samuel-emanuel-urbano-tomassoni.pdf | video: https://youtu.be/-CAbGJIpnfs
No description published; title, speakers and materials only.

### Between the Law and the Protocol: An Overview of Blocking Orders on the Brazilian Internet
Speakers: Pedro de Botelho Marcos
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/entre-el-derecho-y-el-protocolo-un-panorama-general-de-las-ordenes-de-bloqueo-en-internet-en-brasil-v1-pedro-de-botelho-marcos.pdf | video: https://youtu.be/Cyl1GHusKKY
No description published; title, speakers and materials only.

### Lightning Talks
Speakers: Roberto Oya Luengo, Jorge Cano, Jen Linkova, Gilberto Zorello, Hernan Uriel Kleinman, Christian O’Flaherty, Sergio Kleiman, Celsa Sánchez, Yerlin Otárola Delgado, Anahí Rebatta, Santiago Manduca, Antonio Marcos Moreiras
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/the-enemy-within-el-enemigo-en-casa-v1-roberto-oya-luengo.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/the-enemy-within-el-enemigo-en-casa-v1-roberto-oya-luengo.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/esteganografia-v1-jorge-cano.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/why-should-you-care-about-ietf-v1-jen-linkova.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/proxies-residenciales-v1-hernan-uriel-kleinman.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/como-solucao-de-conectividade-em-areas-remotas-e-rur-v1-gilberto-zorello.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/proxies-residenciales-v1-hernan-uriel-kleinman.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/dns-anycast-quien-responde-detras-de-la-nube-v1-celsa-sanchez.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/open-fibre-data-standard-v1-christian-o-flaherty.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/updating-the-manrs-network-operators-baseline-v1-sergio-kleiman.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/updating-the-manrs-network-operators-baseline-v1-sergio-kleiman.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/vlaas-v1-yerlin-otarola-delgado.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/vlaas-v1-yerlin-otarola-delgado.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/netflix-open-connect-geofeeds-v1-anahi-rebatta.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/netflix-open-connect-geofeeds-v1-anahi-rebatta.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/mediciones-de-internet-isoc-v1-santiago-manduca.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/rpki-selflab-roa-rov-and-aspa-in-a-lab-that-runs-on-your-laptop-v1-antonio-marcos-moreiras.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/rpki-selflab-roa-rov-and-aspa-in-a-lab-that-runs-on-your-laptop-v1-antonio-marcos-moreiras.pdf
On-site lightning talks provide an opportunity for attendees at LACNIC 46 &#8211; LACNOG 2026 to share knowledge and experiences through brief, dynamic 10-minute technical presentations, followed by an additional 5 minutes for Q&amp;A and comments. Presentations will be selected by the LACNOG Program Committee through a special call for submissions which will take place in the days leading up to or during the first days of the event. Las charlas relámpago (Lightning Talks) in situ, fomentan la compartición de conocimientos y experiencias entre asistentes presenciales a LACNIC 46 &#8211; LACNOG 2026 mediante la realización de presentaciones técnicas breves y dinámicas de 10 minutos de duración, con un espacio de otros 5 minutos adicionales para la sección de preguntas, respuestas y comentarios. Los trabajos serán seleccionados por el Comité de Programa de LACNOG, a partir de una convocatoria especial a tal efecto; que tendrá lugar los días previos al inicio del evento o durante las primeras jornadas del mismo.

## LACNIC Runners (21/10/2026)
### LACNIC Runners
We invite you to join the LACNIC runners group in Mendoza, Argentina. , we will be visiting Parque General San Martín. We will meet on Wednesday, October 21, at 7:00 AM at the entrance of the Hilton Mendoza hotel (Lateral Nte. Acceso Este 3292). Transportation to the park will be provided via vans, arriving at 7:40 AM. At the park participants will be free to roam or jog around. We will meet back at the starting point at 8:10 AM. We will be back at the hotel by 8:30 AM. To stay updated on the runners&#8217; group activities, you can subscribe to the mailing list at: https://mail.lacnic.net/mailman/listinfo/runners Los invitamos a unirse al grupo de runners de LACNIC en Mendoza, Argentina. En esta oportunidad visitaremos el Parque General San Martín. Nos encontraremos el día miércoles 21 de octubre a las 7:00 am en la entrada del hotel Hilton Mendoza (Lateral Nte. Acceso Este 3292). El traslado hacia parque se realizará en vans contratadas, llegando a las 7:40. Una vez allí se podrá recorrer libremente el parque, caminando o corriendo. A las 8:10 nos encontraremos en el punto de partida. La llegada al hotel será a las 8:30. Para mantenerse informados sobre las actividades del grupo de runners, pueden inscribirse a la lista en: https://mail.lacnic.net/mailman/listinfo/runners

## FIRST (21/10/2026)
### FIRST Symposium
2026 FIRST Regional Symposium Latin America &amp; Caribbean Agenda here 2026 FIRST Regional Symposium Latin America &amp; Caribbean Agenda aquí

### FIRST Conf.
2026 FIRST Regional Symposium Latin America &amp; Caribbean Agenda here 2026 FIRST Regional Symposium Latin America &amp; Caribbean Agenda aquí

## Foro Público de Políticas (21/10/2026)
### Opening and Chairs Presentation
Speakers: Tomás Lynch, Sergio Rojas
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/apertura-y-presentacion-moderadores-v4-tomas-lynch-sergio-rojas.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/apertura-y-presentacion-moderadores-v4-tomas-lynch-sergio-rojas-1.pdf | video: https://youtu.be/n4AYFVj8234
No description published; title, speakers and materials only.

### LAC-2026-5 v1: Recovery of Unjustified Legacy Resources
Speakers: Jordi Palet Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/lac-2026-5-v1-recuperacion-de-recursos-legados-no-justificados-v1-jordi-palet-martinez.pdf | video: https://youtu.be/rCrTlCRTQLA
No description published; title, speakers and materials only.

### LAC-2026-4 v1: Justification of Need for Inter-RIR Transfers
Speakers: Ricardo Patara
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/lac-2026-4-v1-justificativa-de-necesidad-transferencia-inter-rir-v1-ricardo-patara.pdf | video: https://youtu.be/KnZnoPt-Zkc
No description published; title, speakers and materials only.

### LAC-2026-6 v1: Clarifications to the PDP
Speakers: Jordi Palet Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/lac-2026-6-v1-aclaraciones-del-pdp-v1-jordi-palet-martinez.pdf | video: https://youtu.be/LUkf80MysPo
No description published; title, speakers and materials only.

### LAC-2026-3 v1: Require Valid ROA Coverage for Requesting Additional Resources
Speakers: Sergio Kleiman
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/lac-2026-3-v1-cobertura-de-roas-validas-para-la-solicitud-de-recursos-adicionales-v1-sergio-kleiman.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/lac-2026-3-v1-cobertura-de-roas-validas-para-la-solicitud-de-recursos-adicionales-v1-sergio-kleiman.pdf | video: https://youtu.be/VMMECbIoC9w
No description published; title, speakers and materials only.

### Implementation of Policy LAC-2025-5: Sub-Assignment of IPv4 Resources to Third Parties
Speakers: Alfredo Verderosa
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/implementacion-de-la-politica-lac-2025-5-sub-asignacion-de-recursos-ipv4-a-terceros-v1-alfredo-verderosa.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/implementacion-de-la-politica-lac-2025-5-sub-asignacion-de-recursos-ipv4-a-terceros-v1-alfredo-verderosa.pdf | video: https://youtu.be/y4CjDde-3-I
No description published; title, speakers and materials only.

### ASO/NRO report
Speakers: Esteban Lescano, Ricardo Patara, Jorge Villa
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/reporte-aso-nro-v1-esteban-lescano-ricardo-patara-jorge-villa.pdf | video: https://youtu.be/UXsUw4cWzKs
No description published; title, speakers and materials only.

### Open Mic
video: https://youtu.be/HiJ-sRGtxgA
No description published; title, speakers and materials only.

## Grupo de trabajo de Mediciones de Internet (IMWG) (21/10/2026)
### Internet Measurement Working Group - Introduction
Speakers: Elisa Peirano, Massimo Candela
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/grupo-de-trabajo-de-mediciones-de-internet-introduccion-v1-elisa-peirano-massimo-candela-1.pdf | video: https://youtu.be/PAy5Wwg3zBM
A space for the community to share studies, experiences, and tools related to internet measurements. This session will address the collection and analysis of network data to better understand how the Internet functions in the region and provide valuable information to support decision-making. Espacio de la comunidad para compartir estudios, experiencias y herramientas vinculadas con la medición de Internet. La sesión abordará la recolección y el análisis de datos sobre las redes, con el objetivo de comprender mejor el funcionamiento de Internet en la región y aportar información útil para la toma de decisiones.

### Monitoring to Mitigate Micro-Outages in MikroTik-Based ISP Topologies Using Natural Language
Speakers: Joaquin Tadeo Riedmaier, Santiago Agustín Zualet
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/monitoreo-para-mitigar-microcortes-en-topologias-isp-basadas-en-mikrotik-mediante-lenguaje-natural-v1-joaquin-tadeo-riedmaier-santiago-agustin-zualet.pdf | video: https://youtu.be/7342HApR9F8
No description published; title, speakers and materials only.

### When Does It End? Detecting Routing Loops in the Dominican Republic
Speakers: Wilson Ramírez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/cuando-se-termina-deteccion-de-bucles-de-enrutamiento-en-la-republica-dominicana-v3-wilson-ramirez.pdf | video: https://youtu.be/TW6TUTLFWOM
No description published; title, speakers and materials only.

### A Network Tomography Approach to Imputing OD Traffic in an IP/MPLS Network
Speakers: Claudio Risso, Carlos Martínez, Pablo Cuello
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/un-enfoque-de-tomografia-en-redes-para-imputar-trafico-od-en-una-red-ip-mpls-v1-claudio-risso-carlos-martinez-pablo-cuello.pdf | video: https://youtu.be/GuxZLeRFLH0
No description published; title, speakers and materials only.

### TurboTest: Learning When Less Is Enough Through Early Termination of Internet Speedtests
Speakers: Haarika Manda
video: https://youtu.be/PbIT0UnVbYU
No description published; title, speakers and materials only.

## Taller de Gobernanza de Internet (21/10/2026)
### Internet Governance Workshop
No description published; title, speakers and materials only.

### Why Should Engineers Participate in Internet Governance?
Speakers: Carolina Aguerre
No description published; title, speakers and materials only.

### Internet Governance Spaces: How Can These Spaces Be Created?
Speakers: Paula Oteguy, Alan Ramírez
No description published; title, speakers and materials only.

### The Role of the Technical Community and Academia in Internet Governance
Speakers: Marcela Alejandra Orbiscay
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/el-rol-tecnico-y-academico-en-la-gobernanza-de-internet-v1-marcela-alejandra-orbiscay.pdf
No description published; title, speakers and materials only.

### NGOs and Internet Governance in LAC
Speakers: Lía Solís Montaño
No description published; title, speakers and materials only.

## LACNIC (21/10/2026)
### RPKI in Action: Updates and Routing Security
Speakers: Gerardo Rada, Jorge Cano, Carlos Martínez
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/rpki-en-accion-novedades-y-seguridad-de-enrutamiento-v1-gerardo-rada-jorge-cano-carlos-martinez.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/rpki-en-accion-novedades-y-seguridad-de-enrutamiento-v1-jorge-cano.pdf | slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/rpki-en-accion-novedades-y-seguridad-de-enrutamiento-v1-gerardo-rada.pdf | video: https://youtu.be/YTTa9F-YIRo
The session will begin with a presentation of the main technical updates on RPKI, including the latest FORT developments, the implementation of ASPA in MiLACNIC, the enablement of the delegated model through its interface, and an overview of LACNIC’s RPKI architecture. We will then revisit the interactive activity held at LACNIC 45, based on a route hijacking scenario, and continue with new guided demonstrations and hands-on ASPA configuration exercises. The session will be dynamic and interactive, with audience participation and incentives throughout the activity. La sesión comenzará con una presentación de las principales novedades técnicas de RPKI, entre ellas la actualización de FORT, la implementación de ASPA en MiLACNIC, la habilitación del modelo delegado desde su interfaz y una mirada general a la arquitectura de RPKI en LACNIC. Luego retomaremos la actividad interactiva realizada en LACNIC 45 a partir de un caso de secuestro de rutas y avanzaremos con nuevas demostraciones guiadas y ejercicios prácticos de configuración de ASPA. Será una sesión dinámica e interactiva, con participación de la audiencia e incentivos durante la actividad.

### Site Blocking in Latin America and the Caribbean
Speakers: César Díaz, Silvana Rivero
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/bloqueo-de-sitios-en-latinoamerica-y-el-caribe-motivaciones-procedimientos-y-desafios-para-la-operacion-de-redes-v1-cesar-diaz-silvana-rivero.pdf | video: https://youtu.be/TyRdXFmmZ1E
During 2025, LACNIC, in collaboration with MARYVA, conducted a study on regional trends in Internet resource blocking which included an analysis of 18 countries/territories. The presentation will show how, in contrast to the previously observed pattern of active blocking, the dominant trend in the region is now reactive online blocking. We will also examine how blocks are typically applied to websites, URLs, IP addresses, and/or platforms in response to specific activities or events. Durante 2025, LACNIC junto a MARYVA trabajaron en un estudio sobre las tendencias a nivel regional de bloqueos de recursos de Internet, a través del análisis de 18 países/territorios. En la presentación visualizaremos cómo la región muestra un patrón dominante de bloqueo online reactivo, contrario a un esquema de monitoreo activo previo, y analizaremos cómo la lógica predominante es intervenir sobre sitios, URLs, Direcciones IP y/o plataformas, usualmente ante una actividad concreta.

## Encuentro de operadores locales - CABASE (21/10/2026)
### Panel: The Botnet Is at Home: Compromised TV Boxes—Risks, Impact, and Challenges for ISPs
Speakers: Mario Clep, Gaston Pechieu Caiña, Santiago Trucco, Fanny Lospennato
slides: https://apievt.lacnic.net/wp-content/uploads/2026/10/panel-la-botnet-esta-en-casa-tv-box-comprometidas-riesgos-impacto-y-desafios-para-los-isps-v2-fanny-lospennato.pdf
A space for exchange aimed at Internet operators in Argentina, featuring a brief institutional presentation by CABASE and a technical panel on current challenges faced by ISPs. The session will cover experiences related to compromised devices, malicious traffic, and network protection, based on cases and lessons shared by operators from Argentina. Espacio de intercambio dirigido a operadores de Internet de Argentina, con una breve presentación institucional de CABASE y un panel técnico sobre desafíos actuales para los ISPs. La sesión abordará experiencias vinculadas con dispositivos comprometidos, tráfico malicioso y protección de redes, a partir de casos y aprendizajes compartidos por operadores de Argentina.

## Evento social (21/10/2026)
### Social Event
Buses depart from the Hilton Hotel at 7:00 p.m. Salida de buses del Hotel Hilton, 19.00 hs

## FIRST (22/10/2026)
### FIRST Training
2026 FIRST Regional Symposium Latin America &#038; Caribbean Agenda here 2026 FIRST Regional Symposium Latin America &#038; Caribbean Agenda aquí

## LACNOG (22/10/2026)
### MANRS and Best Practices for Protecting Routing and Experiences
Speakers: Jose Manuel Blanco Pino
slides: https://apievt.lacnic.net/wp-content/uploads/2026/07/manrs-y-buenas-practicas-para-proteger-el-enrutamiento-y-las-experiencias.pdf | video: https://youtu.be/G5uQio1EsSE
No description published; title, speakers and materials only.

### From Planning to Operation: IPv6 Deployment at a Regional ISP – The ETAPA EP Case Study
Speakers: Wilmer Miguel Sarango Torres
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/de-la-planificacion-a-la-operacion-implementacion-de-ipv6-en-un-isp-regional-caso-etapa-ep-v1-wilmer-miguel-sarango-torres.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/de-la-planificacion-a-la-operacion-implementacion-de-ipv6-en-un-isp-regional-caso-etapa-ep-v1-wilmer-miguel-sarango-torres.pdf | video: https://youtu.be/K0382vvtabc
No description published; title, speakers and materials only.

### IPv6-Mostly on Campus
Speakers: Henri Alves de Godoy
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/ipv6-mostly-en-campus-1.pdf | video: https://youtu.be/DNDdFoDC014
No description published; title, speakers and materials only.

### Bypassing CGNAT. You Don’t Need PBR, and I Can Prove It!
Speakers: Douglas Fernando Fischer
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/bypass-de-cgnat-no-necesitas-pbr-y-puedo-demostrarlo-v1-douglas-fernando-fischer-1.pdf | video: https://youtu.be/Z1Fqa-zOXK0
No description published; title, speakers and materials only.

### NTPv5 and Updated Time Security: What Changes for Network Operators
Speakers: Antonio Marcos Moreiras
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/ntpv5-y-la-renovacion-de-la-seguridad-horaria-que-cambia-para-los-operadores-de-redes-v1-antonio-marcos-moreiras-1.pdf | video: https://youtu.be/O2yRiTr73oE
No description published; title, speakers and materials only.

### Panel: A Look at the Impact of the 2026 FIFA World Cup on Network Traffic in the Region
Speakers: Nicolás Graizer, Hernán Moguilevsky, Julimar Lunguinho Mendes, Guilherme Ganascim
video: https://youtu.be/YQ1JXE1QdPE
No description published; title, speakers and materials only.

### From CLI to Autonomous Networks: How the Evolution of Protocols Made Operational AI Possible
Speakers: Luiz Cosme Puppin Magalhaes
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/de-cli-a-redes-autonomas-como-la-evolucion-de-los-protocolos-ha-posibilitado-la-ia-operativa-v1-luiz-cosme-puppin-magalhaes.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/de-cli-a-redes-autonomas-como-la-evolucion-de-los-protocolos-ha-posibilitado-la-ia-operativa-v2-luiz-cosme-puppin-magalhaes.pdf | video: https://youtu.be/TtdnnsSlssQ
No description published; title, speakers and materials only.

### New DNS Limits: Let's Avoid Excessive Dependencies
Speakers: Hugo Salgado
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/nuevos-limites-en-el-dns-cuidemos-el-exceso-de-dependencias-v2-hugo-salgado.pdf | video: https://youtu.be/W9JOJVDp2gM
No description published; title, speakers and materials only.

### Recursive DNS: Performance, Monitoring, and Security for ISPs
Speakers: Pedro Orlando Filho
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/dns-recursivo-performance-monitoreo-y-seguridad-para-los-isp-v1-pedro-orlando-filho.pdf | video: https://youtu.be/pJ-fn1A9o3s
No description published; title, speakers and materials only.

### Anycast DNS and KINDNS at a Public University
Speakers: Valdinei Rodrigues dos Reis
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/dns-anycast-y-kindns-en-una-universidad-publica-v1-valdinei-rodrigues-dos-reis.pdf | video: https://youtu.be/jwLamSktNb0
No description published; title, speakers and materials only.

### Panel: Neutral and Hybrid Networks
Speakers: Facundo Javier Caselles Costa, José Luis Vanella, Javier Balmaceda
video: https://youtu.be/6OfnfNUfMl0
No description published; title, speakers and materials only.

### Strengthening University Cybersecurity in Resource-Constrained Environments Using Fail2Ban‑UI and OTX
Speakers: Manuel José Linares Alvaro
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/fortalecimiento-de-la-ciberseguridad-universitaria-en-entornos-de-recursos-limitados-mediante-fail2ban-ui-y-otx-4.pdf | video: https://youtu.be/q7mRzveSWbE
No description published; title, speakers and materials only.

### Open and Reproducible Container-Based Lab for Vulnerability Assessment
Speakers: Daniel Felipe Palomo Luna
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/laboratorio-abierto-y-reproducible-para-la-evaluacion-de-vulnerabilidades-basado-en-contenedores-v1-daniel-felipe-palomo-luna.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/laboratorio-abierto-y-reproducible-para-la-evaluacion-de-vulnerabilidades-basado-en-contenedores-v1-daniel-felipe-palomo-luna.pdf | video: https://youtu.be/rZKigaqlE5U
No description published; title, speakers and materials only.

### LACNOG Institutional Session
Speakers: Carlos Martínez, Jorge Villa
slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/lacnog-sesion-institucional-v1-carlos-martinez-jorge-villa.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/09/lacnog-sesion-institucional-v1-carlos-martinez-jorge-villa.pdf
No description published; title, speakers and materials only.

### LACNOG Closing Ceremony
Speakers: Carlos Martínez, Jorge Villa
slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/cierre-lacnog-v1-carlos-martinez-jorge-villa.pptx | slides: https://apievt.lacnic.net/wp-content/uploads/2026/08/cierre-lacnog-v1-carlos-martinez-jorge-villa.pdf | video: https://youtu.be/pDo_PKp-Gfk
No description published; title, speakers and materials only.

## LACNIC (22/10/2026)
### LACNIC 46 Wrap-Up
No description published; title, speakers and materials only.

