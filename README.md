# conference-digest

Curated **digests** of conferences relevant to networking, cloud, Kubernetes,
and AI, published as a blog at
**https://tldr.netdevops.me/**.

A GitHub Actions workflow fetches each conference's published program, wraps it
in a universal triage prompt, commits the prompt, and opens a GitHub Issue.
[ToFaRev](https://github.com/hellt/tofarev) then reads the program with
`zai-org/GLM-5.3` on Nebius Token Factory, drafts the digest and opens a
pull request. You review and merge it; the digest lands in `digests/`, the issue
closes and the site rebuilds. You can still paste a prompt into Claude yourself.

The scan uses the workflow's built-in `GITHUB_TOKEN`, plus `TAVILY_API_KEY` for
the one source it reads through Tavily (nanog.org). The bot needs the
`TOFAREV_API_KEY` secret, which reaches ToFaRev's isolated container and nothing
else. `TAVILY_API_KEY` also lets ToFaRev read linked PDFs that block GitHub's
runners.

## How it works

```
trigger (fortnightly cron, or manual workflow_dispatch)
  -> discovery reads series.yaml: probes for editions the registry is missing
       confirmed     -> append the edition to registry.yaml
       not up yet    -> re-probe next run
  -> orchestrator reads registry + state
  -> for each past, not-yet-digested conference: run its fetcher
       OK            -> write prompts/<key>.md, mark published
       not_published -> retry next run (event past but artifacts not up yet)
       manual         -> auto-fetch blocked; you paste the program in yourself
  -> commit prompts/ + state.json + registry.yaml
  -> open ONE GitHub Issue summarising what's ready / needs you / stalled
Digest Bot (after the scan, or on a pushed prompt)
  -> ToFaRev reads prompts/<key>.md and drafts the digest
  -> PR "digest: <key>" -> [you] review + merge -> digests/<key>.md
  -> issue closes, site rebuilds and publishes to GitHub Pages
```

A conference is considered **done** when `digests/<key>.md` exists — that's the
only "done" signal; the script never writes it, you do (by committing the
digest). State (`conferences/state.json`) only tracks pending/published and
retry bookkeeping.

### Selection rule

On each run, the orchestrator selects every conference whose `end_date` is in
the past and which has no digest yet, then (re)attempts the fetch. Artifacts
(papers, videos) are usually published *after* the event, so a past conference
that isn't fetchable yet stays `pending` and is retried until it succeeds — or,
after `STALL_THRESHOLD` (4) failed attempts, is flagged **stalled** so you know
a site changed and a fetcher needs adjusting.

## ToFaRev digest bot

`.github/workflows/digest-bot.yml` calls ToFaRev's reusable
[`digest.yml`](https://github.com/hellt/tofarev/blob/main/docs/digest.md),
pinned to a full commit SHA, the same way containerlab runs `/tofarev review`.
It runs after every scan, when someone pushes a prompt to `main`, or by hand
(**Actions → Digest Bot → Run workflow**, optionally with one `conference` key to
rewrite).

1. `queue` lists prompts with program text, no digest and no open bot PR,
   newest first, at most three per run (`scripts/bot_queue.py`).
2. `write` runs ToFaRev once per key. Programs too large for one context window
   (IETF, KubeCon, USENIX Security reach ~800 kB) are shortlisted in batches,
   narrowed to ≤25 picks, then written. ToFaRev reads the picks' linked PDFs
   (papers, slides) and gives their text to the writer, which may also fetch
   each pick's `page:` link. Code, not the model, then checks the result: links not
   in the program text are reduced to plain text, headings that match no
   program item are flagged, and the canonical metadata block is applied (with
   `written_by`).
3. `propose` validates each artifact (`scripts/propose_digest.py`), adds each
   pick's links row (below), builds the site with it, and opens a PR on
   `tofarev/digest-<key>` whose body lists the check notes and link counts.
   Merging it is the human review step.

### Links: abstract, paper, slides, recording

Every pick gets one row under its heading, built by code
(`conferences/links.py`), never by the model:

```
**Links:** [Abstract](…) · [Paper](…) · [Slides](…) · [Recording](…)
```

A deck published in two formats gets both links (`Slides (PDF) · Slides
(PPTX)`). The links come from the program (fetchers record each item's `page:`, `pdf:`,
`slides:`, `video:` and IETF `materials:`), from the talk's own page read again
(USENIX, Sched and netdev pages add slides and the recording after the event),
from reviewed transcript offsets into whole-day streams (`RECORDING_STREAMS`),
and, for a pick still without a recording, from a YouTube search. A found
recording is linked only if its title or description carries the talk's title,
the conference or its channel is named, and it was uploaded within eight months
after the event. On the site the row becomes muted source links separated by
centered dots, and a talk recording gets a thumbnail that plays in place.

**Recordings come later.** CNCF uploads KubeCon talks about two weeks after
the event, USENIX and SIGCOMM within a few months. `links-refresh.yml` reruns
the links step every day for each digest whose conference ended in the
last 120 days, and opens a `links: <key>` PR listing the picks that gained
links; the digest text is not touched and earlier links are kept. Run it from
the Actions tab with `conference: <key>` for an older digest, or locally:

```bash
python3 scripts/enrich_links.py <key>     # rewrites digests/<key>.md in place
```

The model is `zai-org/GLM-5.3`, set as `"model"` in the workflow's
`trusted_config`. It won a trial of nine Token Factory models on digest
quality. Any Kimi, GLM or DeepSeek model ID or selector works there; see
[ToFaRev model selection](https://github.com/hellt/tofarev/blob/main/docs/models.md).
To move to a newer ToFaRev, run `make pin-tofarev SHA=<full commit sha>`.

**One-time setup:**

- Add the repository secret `TOFAREV_API_KEY`: a Nebius Token Factory API key
  (the one containerlab uses works).
- Add the repository secret `TAVILY_API_KEY`. NANOG needs it: nanog.org blocks
  automated clients, so its agenda is read through Tavily Extract. For the
  rest it is optional: linked PDFs that ToFaRev cannot fetch from a runner
  (ACM DL, USENIX) are read through Tavily Extract, and the links step uses it
  for talk pages that block runners and as the fallback recording search.
  Without it, NANOG editions wait as `manual`, and those picks are written from
  the abstract.
- Settings → General → Features → enable **Issues** (forks start with Issues
  off). The scan opens one issue per conference.
- Settings → Actions → General → enable **Allow GitHub Actions to create and
  approve pull requests**.

## Site

The blog is built with [Zensical](https://zensical.org/) exactly like
containerlab.dev: `uv` runs the pinned Zensical from the `docs` dependency group
(`pyproject.toml`, `uv.lock`), and `mkdocs.yml` carries the theme settings.
`overrides/` + `docs/stylesheets/extra.css` implement Quiet Signal in light and
dark, with a locally served Inter font. Search results, heading permalinks,
right-hand scroll tracking, theme persistence and instant navigation use
Zensical’s native components.
`scripts/build_site.py` turns every `digests/<key>.md` into a post (the digest
text is unchanged; tiers and picks get markup for styling) and writes the
Conferences tracker — a table of every tracked edition, newest first, with a
client-side name filter (`docs/javascripts/conf-filter.js`). `site.yml` builds
it on PRs and publishes it to the
`gh-pages` branch with `peaceiris/actions-gh-pages` on `main`.

```bash
make serve-site   # live preview on http://localhost:8001
make site         # strict build into site/
```

**One-time setup:** after the first `site.yml` run creates `gh-pages`, set
Settings → Pages → Source to **Deploy from a branch**, `gh-pages` / root.

**Domain:** the site is served at **https://tldr.netdevops.me/**. `site.yml`
writes a `CNAME` file to `gh-pages` (the `cname:` input), which sets the Pages
custom domain; the DNS record is `tldr` CNAME `hellt.github.io` in the
netdevops.me zone (Cloudflare, DNS only, so GitHub can issue the HTTPS
certificate). `site_url` in `mkdocs.yml` must match it: it builds every
absolute link, the canonical URLs and the RSS feed. Old
`hellt.github.io/conference-digest/` links redirect to the domain.

## Layout

```
conferences/
  registry.yaml      # the conferences (one entry per edition/year)
  prompt/            # the universal digest prompt, composed at build time
    base.md          #   persona, tiers, item format, rules, output (slots:
                     #   {CONFERENCE} {SOURCE_URL} {KEY} {DATE} {PROGRAM_TEXT})
  state.json         # auto-managed bookkeeping (created on first run)
  links.py           # links rows: program links, talk pages, verified search
  fetchers/
    base.py          # shared fetch + result types + bot-block heuristic
    usenix.py        # NSDI / USENIX Security / SREcon (static HTML)
    ietf.py          # datatracker meeting API: agenda drafts, slides, recordings
    sched.py         # KubeCon / CNCF public Sched schedule (HTML)
    sigcomm.py       # SIGCOMM papers-info table (HTML)
    netdev.py        # netdevconf.info sessions index + per-session pages (HTML)
    nanog.py         # nanog.org agenda + talk pages, read via Tavily Extract
    autocon.py       # AutoCon program + NAF guide, slides repo, YouTube uploads
    ovscon.py        # OVS+OVNcon schedule + anchored abstracts, slides and recordings
    ciscolive.py     # Cisco Live public on-demand abstracts and speakers (US/Europe)
    ripe.py          # RIPE 91+: meeting plan -> sessions -> full talk pages
    nlnog.py         # NLNOG Day program tables, slides and recordings (no abstracts)
    denog.py         # official DENOG agenda -> Pretalx JSON export
    ccs.py           # ACM CCS schedule: sessions, paper titles, authors
    imc.py           # ACM IMC program: papers, abstracts, doi.org links
    conext.py        # ACM CoNEXT program partial: papers, abstracts, ACM DL links
    apricot.py       # APRICOT via the open APNIC conference API
    fosdem.py        # FOSDEM Pentabarf XML, curated track filter
    pretalx.py       # any Pretalx schedule export (hack.lu, CfgMgmtCamp)
    tnc.py           # TNC dates via Tavily; programme pasted by hand
    arin.py          # ARIN meetings: agenda tables, PDFs, timestamped webcasts
    lacnic.py        # LACNIC via the WP REST API behind the event sites
    pets.py          # PETS accepted papers: titles, authors, issues
    ausnog.py        # AusNOG day tables: titles, speakers, PDFs, YouTube
    nznog.py         # NZNOG accepted-talks pages (titles, speakers, abstracts)
    zanog.py         # ZANOG programs, wherever the annual ran (2026: iWeek)
    peeringdays.py   # Peering Days per-year sites: talks, speakers, decks
    moreip.py         # MORE-IP (AMS-IX): agenda articles with speakers, blurbs
    swinog.py         # SwiNOG meeting pages: talks, abstracts, slides, videos
    capacity.py       # Capacity Europe: server-rendered session library
    indico.py         # generic Indico export API (nog.fi, NetUK, GRNOG, DKNOG)
    itnog.py          # ITNOG program tables with PDF slides (Italian)
    netnod.py        # Netnod Tech Meeting agenda paragraphs
                    #   (cfgmgmtcamp reuses pretalx.py)
scripts/
  generate_digest_prompt.py   # orchestrator (state machine)
  build_issue.py              # renders run_summary.json -> issue body
  bot_queue.py                # which prompts the Digest Bot writes this run
  propose_digest.py           # validates a ToFaRev artifact, writes PR text
  enrich_links.py             # adds/refreshes each pick's links row
  links_queue.py              # which digests Links Refresh revisits
  build_site.py               # digests/ -> docs/posts/, docs/<key>/ talk pages, Companies, Conferences
prompts/             # generated, committed by the workflow
digests/             # merged digests; presence = done
docs/  overrides/    # Zensical site sources (docs/posts/ and docs/<key>/ are generated)
layouts/             # the share-card layout (Zensical social plugin)
mkdocs.yml pyproject.toml uv.lock Makefile
.github/workflows/
  ci.yml                  # unit tests + actionlint on PRs and main
  conference-digest.yml   # weekly scan
  digest-bot.yml          # ToFaRev drafts digests as PRs
  close-digest-issue.yml  # closes the issue when a digest lands
  site.yml                # builds + publishes the site
  links-refresh.yml       # daily: new recordings/slides -> links PRs
docs/javascripts/video.js # click-to-play recordings on the site
```

## Running it

- **Manual, one conference:** Actions tab -> Conference Digest -> Run workflow,
  set `conference` to a registry key (e.g. `nsdi-2025`). Ignores the date and
  digested gates — forces that one.
- **Scheduled:** runs weekly; the state machine no-ops when nothing is new, so
  you only get an issue when there's something to digest.
- **Locally:** `pip install -r requirements.txt && python scripts/generate_digest_prompt.py`

## Adding a conference

See **[ADDING-A-CONFERENCE.md](ADDING-A-CONFERENCE.md)**: checking the source,
reusing or writing a fetcher, the program-text format and its link keys
(`page:`, `pdf:`, `slides:`, `video:`), recordings, the series or registry
entry, a local trial, and shipping it.

In short: **if it recurs, add the series, not the edition.**
`conferences/series.yaml` describes the conference itself, and every scheduled
run appends the editions its source confirms. Check a new series without
writing anything:

```bash
python3 scripts/discover_editions.py --dry-run --series kubecon-eu
```

Sources that block CI (`run_location: local`) are only discovered on a local
run.

## Fetcher notes & known fragilities

- **USENIX** and **Sched** are HTML scrapers using browser-like headers. Both
  sites can bot-block (USENIX confirmed to do so). Sched makes three direct
  attempts, then tries Tavily Extract when `TAVILY_API_KEY` is set; only if
  both routes fail does it return `manual` with the URL to copy by hand.
  USENIX still returns `manual` on its first block. The HTML class selectors
  are best-effort; if a site restyles, the fetcher returns zero items
  (`not_published`) and eventually trips the stall flag rather than producing
  wrong output. **The first live run is the real test of these selectors.**
- **IETF** uses the open datatracker API (no key, no bot-block) for one
  meeting: for each WG in the curated `RELEVANT_WGS` list (edit in `ietf.py` as
  interests shift) that met, the drafts named on its agenda, the slide decks
  presented (decks with no draft become their own items), and the session's
  YouTube recording. Each item links its draft page, slides, session recording
  and the session's materials page. A meeting whose WGs have posted no agenda
  or slides yet is `not_published` and retried.
- **NANOG**: nanog.org blocks automated clients with Cloudflare, including
  GitHub's runners, so the fetcher reads the public agenda through Tavily
  Extract. The repository owner approved this on 2026-11-01. The agenda gives
  each talk's page, presenters and abstract. Up to NANOG 96 it also gives the
  recording and slides; from NANOG 97 those are on each talk page, read 20 per
  request. The agenda's day headers give exact dates, so discovery adds each
  meeting once its agenda is up. It needs `TAVILY_API_KEY`, and costs about 2
  Tavily credits per agenda plus 2 per 5 talk pages.
- **AutoCon** (Network Automation Forum): the open edition page
  (`networkautomation.forum/autocon<n>`) lists each session as "time — speaker
  - title", without abstracts. Abstracts come from NAF's program guide repo
  when the edition has one (`Network-Automation-Forum/ac<n>-guide`, AutoCon 5
  on), and otherwise from NAF's YouTube upload of the talk, whose description is
  the abstract. Uploads are found through NAF's per-edition playlist
  ("AutoCon 4"), which costs one request; each video is given to one talk only.
  Without a playlist the fetcher searches per talk. The upload also gives the recording. Slides (PDF, or PPTX for
  AutoCon 3) come from NAF's `handyinfo` repository
  (`docs/autocon_coverage/slides/AutoCon<n>/`, in Git LFS, so links use
  `media.githubusercontent.com`). They are paired with talks by the speaker
  names and title words in their file names.
  The page's form CAPTCHA trips `looks_blocked()`, so this fetcher trusts the
  status code. Recordings arrive weeks after the event: an edition fetched
  early has fewer abstracts, and Links Refresh adds the recordings later.
- **OVS+OVNcon**: `openvswitch.org/support/ovscon<year>/` is open static HTML.
  The fetcher joins schedule rows to abstracts by their `#tN` anchors, keeping
  speakers, slide decks (PDF/PPTX/ODP) and official YouTube recordings. Links
  Refresh reads only the matching row, never another talk's materials. The
  registry includes 2024 and 2025; annual discovery reads event dates from the
  introduction and adds future editions once their abstracts are published.
- **Cisco Live**: the public RainFocus on-demand catalog lists regional events,
  exact session titles (including session codes), speakers and HTML abstracts.
  The fetcher resolves each `ciscolive-us-<year>` / `ciscolive-eu-<year>` key to
  one event and reads the entire program, refusing mixed or partial results.
  Searches are capped at 500 results, so larger editions are split using public
  session-type, level, track and technology filters; the deduplicated union must
  account for every session in the edition's advertised total.
  The widget/profile IDs in the fetcher are public catalog identifiers, not
  credentials. No bot blocking observed. Slides and recordings require login;
  the fetcher never guesses PDF paths or bypasses authentication. Picks link to
  the public `#/session/<id>` page; verified YouTube search can add recordings.
  Links Refresh skips the shared catalog HTML to avoid unrelated materials.
  Discovery uses conservative date estimates (June 30 / March 31); confirm
  discovered dates against the event site. A move to an unknown city requires
  updating `CITIES` in `ciscolive.py`; unknown locations fail closed.
- **RIPE Meetings**: from RIPE 91 onward, the meeting plan links sessions and
  individual talk pages. Session cards truncate abstracts, so the fetcher reads
  the full talk pages for abstracts, decks and native MP4 recordings. Failed
  talk fetches retain a clearly labelled session excerpt. Discovery reads only
  the meeting's date banner, not CFP deadlines. The registry starts with
  RIPE 91–93; ordinal discovery handles the twice-yearly meetings.
- **NLNOG Day**: the annual program table provides exact titles, speakers,
  slides and YouTube recordings, but no abstracts. Prompts state that limitation.
  The fetcher follows the site's explicit HTML canonical redirects; it never
  treats the shared program as a talk page. Ambiguous recordings reused for
  multiple talks (a source error in 2026) are omitted for verified search later.
- **DENOG**: the official agenda links its Pretalx schedule, whose JSON export
  gives full abstracts, speakers, attachments and exact event dates. Following
  that link handles the move from `pretalx.com` (DENOG17) to `cfp.denog.de`
  (DENOG18). Missing recordings use the normal verified links search. The
  registry includes DENOG17–18 and NLNOG Day 2025–2026. All three new sources
  are open; blocks fall back to manual input, never an extraction service.
- **SIGCOMM** and **Netdev** are static HTML with no observed bot-block. Netdev
  does a second pass: the sessions index has only titles/speakers, so it follows
  each session page for the description, track label, slides and video. A
  session page that fails to fetch degrades to title+speakers rather than
  failing the run.
- **GTC**: `www.nvidia.com/gtc/session-catalog/` is a client-rendered app, but
  its JSON catalog API (`api-prod.nvidia.com/services/sessioncatalog`) is open
  and unauthenticated. The event id is opaque and changes yearly; the fetcher
  resolves it from the per-year JS bundle the catalog page embeds
  (`.../gtc/rf/gtc26.js`), which also carries the day→date map discovery reads.
  Only the current edition's bundle exists: a year's bundle 404s until its site
  is built (discovery's "not yet" signal) and 404s again once the site moves on
  (re-run past editions from the committed prompt; the fetcher returns `manual`
  then, pointing at the on-demand library). The API lists ~950 sessions of every
  type; the fetcher keeps presentation-like ones with an abstract (~550 for
  GTC26) and drops posters, hands-on labs, office hours, watch parties and the
  Chinese-language post-event days. Recordings are not in the catalog API —
  sessions go to NVIDIA on-demand (login-gated) and many later to NVIDIA's
  YouTube channel, which the links step finds and verifies.
- **CCS**: `sigsac.org` serves the full schedule as plain HTML: every paper
  with its exact title and authors, grouped by session with room, dates and
  times. Abstracts and papers are ACM DL-only, so prompts say picks are written
  from title, authors and session. The schedule appears about two weeks before
  the event; `start: 2026` because older editions keep no schedule page.
- **IMC**: the program page is server-rendered with every paper's title,
  authors, full abstract and doi.org Paper link, grouped by session. The
  page anchors double as each item's `page:` link. Same static site family as
  SIGCOMM; no bot blocking observed.
- **CoNEXT**: the site is an Angular app, but every page is a server-rendered
  partial — the fetcher reads `partials/program.html` directly: sessions,
  papers, authors, full abstracts and ACM DL page+PDF links. The day headers
  ("Monday, 1st, Dec 2025") carry a comma plain date scanning misses, so the
  probe has its own day-header parser. A preliminary program parses zero
  papers and stays `not_published` until the real one is up.
- **APRICOT**: every `{year}.apricot.net` schedule is served by one open API
  (`api.apnic.net`). The events listing gives the edition id, dates and city —
  the probe reads it directly — and the event document lists each agenda item
  with speaker, affiliation, abstract and slides. A session's YouTube live
  link is attached only when it holds a single talk. Week-long workshops,
  breaks and sponsor invites are dropped.
- **FOSDEM**: one schedule XML per edition gives every event's page, abstract,
  speakers, slide attachments and video.fosdem.org recording. With ~1000
  events over 71 tracks the fetcher keeps a curated track set (network, eBPF,
  DNS, AI, HPC/data science, containers, virtualization/cloud infrastructure,
  kernel, main) and drops workshops and lightning talks; `RELEVANT_TRACKS` in
  `fosdem.py` is the lever. The XML states the conference dates exactly.
- **Pretalx (generic)**: conferences whose CfP runs on Pretalx expose the
  schedule as JSON; the fetcher reads it directly (hack.lu, CfgMgmtCamp).
  Every talk comes with speakers, abstract, attachments and its public page.
  `looks_blocked()` is skipped on this path on purpose — a security-conference
  abstract that mentions "captcha" is not a bot challenge.
- **TNC**: tnc<yy>.geant.org blocks datacenter IPs, so the probe reads the
  site through Tavily Extract for the dates (owner-approved 2026-11-01, same
  as NANOG). The programme page's embedded Pretty Event app exposes public
  JSON endpoints for the complete schedule and configuration. The fetcher
  reads those directly to get every presentation, abstract, speaker and slide
  attachment, without going through bot-walled Indico; recordings for the
  links step land on the GÉANT YouTube channel.
- **ARIN**: one plain-HTML agenda page per meeting, one table per day. Every
  row carries the agenda item, speaker, slide PDF and a timestamped YouTube
  webcast link; policy rows link their draft pages. Same URL shape since
  ARIN 56 (earlier meetings used different paths).
- **LACNIC**: the event sites are React apps over one open WP REST API
  (`apievt.lacnic.net`). The `our_events` taxonomy maps an edition number to
  its term id; the `agenda` posts give titles (English preferred), speakers,
  session groups, per-language YouTube recordings and slide media ids, which
  the media endpoint resolves to URLs. The agenda timestamps give the exact
  dates for discovery.
- **PETS**: the accepted-papers page lists every paper with exact title and
  authors per PoPETs issue. Abstracts are in the journal (not fetched), so
  prompts say picks are written from title and authors. The page carries no
  dates, so the series uses an `end_date_hint`.
- **AusNOG**: the program page has one table per conference day; each talk row
  links its PDF deck and YouTube recording through icon links, with the
  speaker and affiliation in the title cell. No abstracts are published, and
  the day captions carry no year — hence the `end_date_hint`.
- **Peering Days**: one static site per edition. The programme page gives each
  slot's title, an "(Speaker: IXP - Name)" line and Download deck links; only
  workshops publish abstracts, which prompts state. The 2027 site was
  announced with broken TLS at add time; discovery retries until it serves.
- **MORE-IP**: AMS-IX's agenda is plain WordPress HTML: title, "Name - Company"
  speaker lines, short blurbs and YouTube recordings on some items. The
  theme's CSS mentions captcha classes, so `looks_blocked()` markers are
  skipped there — status codes alone decide.
- **SwiNOG**: one page per meeting with the program plugin: title, "Name ·
  Company", full abstract and Slides/Video link spans per talk; the Quick
  facts box has the dates. Form-validation strings mentioning recaptcha make
  this a status-only source too. Decks can land days after the meeting, so
  recent editions may want a prompt regeneration.
- **Capacity Europe**: the agenda looks like a JS app, but every session is
  server-rendered — title, description, "Name, Role - COMPANY" speakers, stream
  tags and a session page link, grouped by day wrapper ids. A commercial
  event, so no recordings or slides; social-agenda items are dropped.
- **JANOG**: the timetable links every session to its own page, which carries
  the overview, slide PDFs and the YouTube live link that doubles as the
  archived recording. The program is Japanese and presented as-is; the
  probe has its own 年月日 date parser because plain scanning misses Japanese
  dates. One page per session makes the fetch chatty (~60 requests).
- **Indico (generic)**: one open export endpoint (`/export/event/<id>.json?
  detail=contributions`) serves every contribution with title, description,
  speakers and material. Used by nog.fi, NetUK, GRNOG and DKNOG. The series
  or registry entry points `program_url` at an event page, a category page or
  a site root; a root that redirects straight to the event page resolves
  itself (and the redirect's host serves the export — DKNOG's subdomains
  point at the shared events.dknog.dk), and a plain listing resolves by the
  edition's name (upcoming events only — past ones are hand-added with their
  event URL).
- **NetUK** uses the generic Indico fetcher: its event ids match the edition
  numbers (event 3 = NetUK3), so the series template points straight at the
  event page and the export gives titles, abstracts, speakers and material.
- **GRNOG** also uses the Indico fetcher, through the NOG Alliance instance.
  Its category listing shows only upcoming events, so discovery resolves
  future editions by name and past ones (GRNOG 20) are hand-added with their
  event URL.
- **DKNOG** also uses the Indico fetcher. Each edition's subdomain root
  redirects to the event on the shared events.dknog.dk backend, and that
  redirect both resolves the event and names the export host.
- **ITNOG**: a static page per meeting with program tables linking PDF
  decks. Italian titles are presented as-is; no abstracts are published.
- **Netnod**: the Tech Meeting page renders its agenda as Drupal paragraphs
  — time, title, speaker with company, presentation links. Titles and
  speakers only; the URL carries the year and the page scan finds the date.
- **CfgMgmtCamp**: the Ghent automation camp next to FOSDEM runs on Pretalx,
  so the generic Pretalx fetcher reads its schedule export (hosted at
  cfp.cfgmgmtcamp.be, also cfp.cfgmgmtcamp.org).
- **OCP Global Summit**: every edition is its own host on the FN TECH event
  platform (`{year}ocpglobal.fnvirtual.app`) and its schedule page is a
  Gatsby app with no public API — but the whole program (titles, speakers,
  full abstracts, tracks, YouTube recordings, material links, exact dates) is
  baked into the `app-*.js` bundle the page embeds, which the fetcher parses
  the JSON out of. Posters, staff-internal events and items without abstracts
  are dropped (~550 talks stay). A future year's host does not resolve until
  its site is built ("not up yet"), and past hosts stay up, so past editions
  re-fetch fine. Recordings are on OCP's YouTube channel, many already
  linked in the program; specs/white papers/repos are filed as materials.
  The series covers the San Jose Global Summit only — EMEA and APAC editions
  sit on their own fnVirtual hosts and can be hand-added if wanted.
- **MLSys** runs a NeurIPS-style virtual site per edition
  (`mlsys.org/virtual/<year>/`): the papers index lists every accepted paper
  (orals included) and each paper page carries authors, the full abstract,
  an OpenReview link (page+pdf; the virtual-site page is the fallback) and a
  SlidesLive embed that maps straight to a recording URL. The invited talks
  are read from their own list first, before the ~170 paper pages, with a
  polite delay between requests. The conference page's "May 18th - 22nd,
  2026" dates need the probe's own regex; earlier editions state dates in
  other formats, so the series carries an `end_date_hint` and a discovered
  date may need the expected confirming glance.
- **Sessionize** (PyTorch Conference): the Linux Foundation's event page
  links its Sessionize schedule, which publishes a clean per-event markdown
  view that needs no key. The sessionize event id is new each edition and the
  LF URL stays the same, so the fetcher finds the id on the page and checks
  the schedule's event year against the registry key before trusting it — a
  page still showing the previous edition is `not_published` for the next
  one, which is also what keeps discovery from adding an edition from a
  stale page. Talks are sessions with a named speaker and a description;
  registration, meals and breaks are dropped by title and shape. Recordings
  are not in the schedule — the links step finds them on the PyTorch
  YouTube channel.
- **MCP Dev Summit North America** uses the generic Sched fetcher: one
  `mcpdevsummitna<yy>.sched.com` programme per edition with titles, speakers
  and abstracts. Speaker-provided slide decks are attached to the Sched
  session pages; recordings are on the official `@AgenticAI-Foundation`
  YouTube channel. The series starts with the April 2026 New York edition.
- **ONE Summit / Open Networking & Edge Summit** uses the generic Sched
  fetcher: one `onesummit<year>.sched.com` programme per edition with titles,
  speakers and abstracts. Speaker-provided decks are attached to the Sched
  session pages; recordings are on the official `@lfnetworking` YouTube
  channel. The series covers the 2024 San Jose, 2025 London and 2026 Tokyo
  editions.
- **OPI Summit on DPUs/IPUs** uses the generic Sched fetcher: one
  `opisummit<year>.sched.com` programme per edition with titles, speakers and
  abstracts. Slide decks are attached to the Sched session pages; recordings
  are found on the official `@OPI_project` YouTube channel. The series starts
  with the 2026 edition, held alongside OCP Global Summit in San Jose.
- **@Scale** (Meta): one WordPress agenda layout serves the four current
  series — Networking, Product, AI & Data, and Systems & Reliability. Accordion
  items carry exact titles, speakers with companies and abstracts; Product and
  AI & Data also include video-on-demand or poster tabs. Unique item ids become
  per-talk anchors (duplicated source ids are deliberately not linked). Watch
  buttons resolve through their @Scale video page to the embedded YouTube
  upload; missing and future recordings use the official `@scaleconference`
  channel. Discovery reads only the event hero because article-card dates below
  the agenda can outvote the real event date. Form CSS mentions captcha, so this
  is a status-only source like MORE-IP and SwiNOG.
- The `*.sched.com` subdomains and exact `end_date`s in the registry should be
  verified close to each event; they're flagged in registry `notes`.

## Dependencies

`requirements.in` declares the direct runtime dependencies (`requests`,
`beautifulsoup4`, `PyYAML`). `requirements.txt` is the locked, hash-checked
installation file used by the workflows. After changing the direct dependencies,
regenerate it with:

```bash
uv pip compile requirements.in --output-file requirements.txt --generate-hashes --python-version 3.14
```

The site toolchain is separately locked in `uv.lock`; `make site` uses it with
`uv run --locked`. CI runs the unit tests and `actionlint` on pull requests and
pushes to `main`.
