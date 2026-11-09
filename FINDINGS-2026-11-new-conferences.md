# Findings: ingesting the RIPE-calendar conference shortlist (2026-11)

On 2026-11-01 the repository owner asked for the events on
`ripe.net/meetings/calendar/` to be analyzed, sized and ingested, with a
findings document for anything that did not work. This is that document.
Twenty-three of the 24 chosen events are ingested through stacked PRs
(`feat/ccs` … `feat/cfgmgmtcamp`); one (CHNUG) is deliberately not ingested.

Size and reputability figures were verified against the sources themselves
(Tavily search/extract, 2026-11-01): APRICOT 1,000+ delegates (largest AP
Internet event), FOSDEM 8,000+ attendees, TNC 800+ participants / 70+
countries, Capacity Europe ~4,000 attendees, ACM CCS / IMC / CoNEXT / PETS
top-tier research venues, M3AAWG 300–500 (dropped from the final list by
owner), hack.lu 500+, SwiNOG 150–300, AusNOG ~250 (capped, sold out),
Peering Days ~300 (largest CEE peering conference), MORE-IP ~300, LACNIC
sold-out (maximum capacity), ARIN biannual public meetings, JANOG ~1,000,
Netnod Tech Meeting 200+, NetUK/GRNOG/DKNOG/nog.fi/ITNOG national NOGs.

## Per-event summary

| Event | Fetcher | Source | Verified (2026-11-01) |
| --- | --- | --- | --- |
| ACM CCS | `ccs` | `sigsac.org` schedule HTML | ccs-2026: 483 papers (titles+authors; ACM DL carries the rest) |
| ACM IMC | `imc` | `conferences.sigcomm.org` program HTML | imc-2026: 77 papers with abstracts + doi.org links |
| ACM CoNEXT | `conext` | `co-next/{year}/partials/program.html` | conext-2025: 50 papers with abstracts + ACM DL links |
| APRICOT | `apricot` | open APNIC conference API | apricot-2026: 133 talks; 2027 dates already in the API |
| FOSDEM | `fosdem` | Pentabarf schedule XML | fosdem-2026: 158 events across 10 relevant tracks, 157 with recordings |
| hack.lu | `pretalx` | pretalx.com schedule export | hacklu-2025: 124, hacklu-2026: 116 talks |
| TNC | `tnc` | Tavily probe + Pretty Event JSON | tnc-2026: 181 programme items from 111 sessions |
| ARIN | `arin` | agenda tables | arin-56/57/58: 24/35/28 items with PDFs + timestamped YouTube |
| LACNIC | `lacnic` | WP REST API behind the event sites | lacnic-45/46: 69/68 items with per-language recordings |
| PETS | `pets` | accepted-papers page | pets-2026: 160 papers (titles+authors) |
| AusNOG | `ausnog` | program tables | ausnog-2025/2026: 22/23 talks with PDFs + YouTube |
| Peering Days | `peeringdays` | per-year site programme | peeringdays-2026: 19 items with decks |
| MORE-IP | `moreip` | agenda page | moreip-2025/2026(/2027): 22/24/28 items |
| SwiNOG | `swinog` | meeting pages | swinog-41/42: 13/17 talks with abstracts |
| Capacity Europe | `capacity` | agenda page session library | capacity-2026: 118 sessions with speakers, streams, pages |
| JANOG | `janog` | timetable + session pages | janog-58: 56 sessions (Japanese) |
| nog.fi | `indico` | nog.fi Indico export | nogfi-2026-06: 20 talks, nogfi-2026-11 (upcoming): 12 so far |
| NetUK | `indico` | indico.netuk.org export | netuk-2/3: 25/24 contributions |
| GRNOG | `indico` | NOG Alliance Indico export | grnog-20 (hand-added): 15 talks; 21 resolves when its program is up |
| DKNOG | `indico` | events.dknog.dk export | dknog-16: 19 contributions with abstracts |
| ITNOG | `itnog` | static program tables | itnog-9/10: 20/30 talks with PDF decks |
| Netnod | `netnod` | agenda paragraphs | netnod-2025/2026: 16/16 items |
| CfgMgmtCamp | `pretalx` | Pretalx schedule export | cfgmgmtcamp-2026: 135 talks |

## Not ingested

- **CHNUG** (Swiss Network User Group): a Meetup community (32 members, one
  past event at 2026-11-01) with no published programs, slides or recordings
  anywhere a fetcher could read. Nothing to digest yet; revisit if they start
  publishing event agendas. Deliberately left out of the registry rather than
  added as a permanently-manual edition.

- **M3AAWG** was on the analysis list but removed by the owner before
  ingestion (meetings are members + vetted guests).

## Things that did not work, and how they were handled

- **TNC's programme is in its app API, not Indico.** `tnc{yy}.geant.org`
  serves a plain 403 to datacenter clients; Tavily Extract reads the WordPress
  pages (owner approval covers blocked public pages, 2026-11-01). Tavily's
  rendered programme only exposes the default day, and GÉANT's Indico blocks
  both direct requests and Tavily. The WordPress REST source, however, names
  the embedded Pretty Event loader, whose public programme and config JSON
  endpoints are directly readable. The fetcher uses those for all sessions,
  presentations, abstracts, speakers and attachments; Tavily remains only the
  discovery probe for dates.

- **APNIC's API keeps only recent editions.** APRICOT 2025 resolves in the
  events listing but its event document has no sessions, so discovery reports
  `not_published` for it. The series effectively starts at 2026; older
  APRICOTs are gone from the source.

- **CoNEXT's accepted-papers partial 404s for 2025** (`partials/
  accepted-papers.html` exists only for 2026+); the program partial is the
  stable path, so the fetcher reads that. CoNEXT 2026's program is still the
  preliminary one — zero papers, `not_published`, re-probed until December.

- **GRNOG's Indico category listing shows only upcoming events.** Future
  editions resolve by name; past ones are hand-added. GRNOG 20 = event 13
  (added). GRNOG 19's event id could not be found through any public listing —
  skipped; add by hand if it matters.

- **JANOG 57 predates the `program-timetable` layout** (its site uses
  `?p=`-style WordPress pages), so the series starts at 58. JANOG 59's site is
  not up yet; discovery will pick it up. Archive video links expire (JANOG58's
  are public until 2027-01-31) — prompt regeneration after expiry loses
  nothing the committed prompt hasn't kept.

- **Peering Days 2027** was announced but `2027.peeringdays.eu` served TLS
  errors at add time; discovery retries each run until it serves.

- **DKNOG's per-edition subdomains redirect `/export/`** to the shared
  `events.dknog.dk` backend. The generic Indico fetcher takes the export host
  from the subdomain-root redirect target, so no per-series override is needed
  (an earlier design used a custom `indico_export_url` field, which discovery
  does not copy onto candidates and was dropped).

- **`looks_blocked()` false positives on WordPress sites.** MORE-IP's theme
  CSS mentions captcha form classes and SwiNOG's page embeds
  form-validation strings mentioning recaptcha; the heuristic would call both
  pages bot challenges. Both fetchers are status-only for that check
  (documented in their docstrings). hack.lu's JSON export once failed the
  marker check because a talk was *about* captchas — the Pretalx fetcher skips
  body markers on its JSON path entirely.

- **Capacity Europe's agenda serves the current edition only.** A year check
  in fetch() keeps `capacity-2027` at `not_published` while the page still
  shows 2026 (otherwise it would ingest 2026's sessions under 2027 — the
  wrong-items invariant).

- **SwiNOG decks can land days after the meeting**; a digest written the week
  after may miss slides that appear later. Regenerate the prompt (run
  Conference Digest with the key) if that matters; Links Refresh cannot add
  program-internal materials.

- **CCS/PETS digests are titles-and-authors only** — abstracts and papers
  live behind the ACM DL / PoPETs journal. Prompts say so; the writer marks
  picks accordingly.

- **nog.fi numbers editions by year.month** (two meetings a year), which
  series discovery cannot enumerate; both 2026 editions are hand-added. The
  same applies to future nog.fi meetings.

- **Netnod has two meeting series** (spring "Netnod Meeting" and autumn "Tech
  Meeting") on different URL patterns; only the Tech Meeting is a series. The
  spring meetings can be hand-added (`/netnod-meeting-<year>`) if wanted.
