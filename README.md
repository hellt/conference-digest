# conference-digest

Curated **digests** of conferences relevant to datacenter and cloud-native
networking, network security, and identity, published as a blog at
**https://hellt.github.io/conference-digest/**.

A GitHub Actions workflow fetches each conference's published program, wraps it
in a universal triage prompt, commits the prompt, and opens a GitHub Issue.
[ToFaRev](https://github.com/hellt/tofarev) then reads the program with
`zai-org/GLM-5.3` on Nebius Token Factory, drafts the digest and opens a
pull request. You review and merge it; the digest lands in `digests/`, the issue
closes and the site rebuilds. You can still paste a prompt into Claude yourself.

The scan needs no API keys: it uses the workflow's built-in `GITHUB_TOKEN`. The
bot needs the `TOFAREV_API_KEY` secret, which reaches ToFaRev's isolated
container and nothing else. An optional `TAVILY_API_KEY` secret lets ToFaRev read
linked PDFs that block GitHub's runners.

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

The links come from the program (fetchers record each item's `page:`, `pdf:`,
`slides:`, `video:` and IETF `materials:`), from the talk's own page read again
(USENIX, Sched and netdev pages add slides and the recording after the event),
and, for a pick still without a recording, from a YouTube search. A found
recording is linked only if its title or description carries the talk's title,
the conference or its channel is named, and it was uploaded within eight months
after the event. On the site the row becomes chips, and a talk recording gets a
thumbnail that plays in place.

**Recordings come later.** CNCF uploads KubeCon talks about two weeks after
the event, USENIX and SIGCOMM within a few months. `links-refresh.yml` reruns
the links step every Wednesday for each digest whose conference ended in the
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
- Optional: add the repository secret `TAVILY_API_KEY`. Linked PDFs that
  ToFaRev cannot fetch from a runner (ACM DL, USENIX) are then read through
  Tavily Extract. Without it, those picks are written from the abstract. The
  links step also uses it to read talk pages that block runners and as the
  fallback recording search.
- Settings → General → Features → enable **Issues** (forks start with Issues
  off). The scan opens one issue per conference.
- Settings → Actions → General → enable **Allow GitHub Actions to create and
  approve pull requests**.

## Site

The blog is built with [Zensical](https://zensical.org/) exactly like
containerlab.dev: `uv` runs the pinned Zensical from the `docs` dependency group
(`pyproject.toml`, `uv.lock`), `mkdocs.yml` carries the theme settings, and
`overrides/` + `docs/stylesheets/extra.css` are adapted from containerlab's.
`scripts/build_site.py` turns every `digests/<key>.md` into a post (the digest
text is unchanged; tiers and picks get markup for styling) and writes the
Conferences tracker. `site.yml` builds it on PRs and publishes it to the
`gh-pages` branch with `peaceiris/actions-gh-pages` on `main`.

```bash
make serve-site   # live preview on http://localhost:8001
make site         # strict build into site/
```

**One-time setup:** after the first `site.yml` run creates `gh-pages`, set
Settings → Pages → Source to **Deploy from a branch**, `gh-pages` / root.

## Layout

```
conferences/
  registry.yaml      # the conferences (one entry per edition/year)
  prompt/            # the universal digest prompt, composed at build time
    base.md          #   persona, tiers, item format, rules, output (slots:
                     #   {CONFERENCE} {TYPE} {TYPE_GUIDANCE} {PROGRAM_TEXT} ...)
    types/*.md       #   per-type reading guidance, one injected per conference
  state.json         # auto-managed bookkeeping (created on first run)
  links.py           # links rows: program links, talk pages, verified search
  fetchers/
    base.py          # shared fetch + result types + bot-block heuristic
    usenix.py        # NSDI / USENIX Security / SREcon (static HTML)
    ietf.py          # datatracker meeting API: agenda drafts, slides, recordings
    sched.py         # KubeCon / CNCF public Sched schedule (HTML)
    sigcomm.py       # SIGCOMM papers-info table (HTML)
    netdev.py        # netdevconf.info sessions index + per-session pages (HTML)
scripts/
  generate_digest_prompt.py   # orchestrator (state machine)
  build_issue.py              # renders run_summary.json -> issue body
  bot_queue.py                # which prompts the Digest Bot writes this run
  propose_digest.py           # validates a ToFaRev artifact, writes PR text
  enrich_links.py             # adds/refreshes each pick's links row
  links_queue.py              # which digests Links Refresh revisits
  build_site.py               # digests/ -> docs/posts/ + Conferences page
prompts/             # generated, committed by the workflow
digests/             # merged digests; presence = done
docs/  overrides/    # Zensical site sources (docs/posts/ is generated)
mkdocs.yml pyproject.toml uv.lock Makefile
.github/workflows/
  conference-digest.yml   # weekly scan
  digest-bot.yml          # ToFaRev drafts digests as PRs
  close-digest-issue.yml  # closes the issue when a digest lands
  site.yml                # builds + publishes the site
  links-refresh.yml       # weekly: new recordings/slides -> links PRs
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

**If it recurs, add the series, not the edition.** `conferences/series.yaml`
describes the conference itself — URL templates, how its editions are numbered
(`kubecon-eu-{year}`, `ietf-{n}`, `netdev-0x{HEX}`) and where to fall back for
an end date. Every scheduled run probes each series for editions the registry
doesn't have yet and appends the ones the source confirms, so next year's
KubeCon files itself. Check a new series without writing anything:

```bash
python3 scripts/discover_editions.py --dry-run --series kubecon-eu
```

Sources that bot-block CI (`run_location: local`) are only discovered on a
local run — in CI they're reported as needing one.

**For a one-off event**, or to correct a discovered entry, copy a block in
`registry.yaml` and set:

- `key` — unique slug, also the prompt/digest filename
- `type` — `academic | standards | vendor | operator | security` (drives how
  the prompt tells Claude to read the program)
- `end_date` — `YYYY-MM-DD` (selection is based on this)
- `fetcher` — `usenix | ietf | sched | sigcomm | netdev`
- `program_url` — the machine/human-readable program endpoint
- `manual_fallback_url` — page for you to open if auto-fetch is blocked

## Fetcher notes & known fragilities

- **USENIX** and **Sched** are HTML scrapers using browser-like headers. Both
  sites can bot-block (USENIX confirmed to do so). On a block they return
  `manual` and the issue gives you the URL to copy from by hand. The HTML class
  selectors are best-effort; if a site restyles, the fetcher returns zero items
  (`not_published`) and eventually trips the stall flag rather than producing
  wrong output. **The first live run is the real test of these selectors.**
- **IETF** uses the open datatracker API (no key, no bot-block) for one
  meeting: for each WG in the curated `RELEVANT_WGS` list (edit in `ietf.py` as
  interests shift) that met, the drafts named on its agenda, the slide decks
  presented (decks with no draft become their own items), and the session's
  YouTube recording. Each item links its draft page, slides, session recording
  and the session's materials page. A meeting whose WGs have posted no agenda
  or slides yet is `not_published` and retried.
- **SIGCOMM** and **Netdev** are static HTML with no observed bot-block. Netdev
  does a second pass: the sessions index has only titles/speakers, so it follows
  each session page for the description, track label, slides and video. A
  session page that fails to fetch degrades to title+speakers rather than
  failing the run.
- The `*.sched.com` subdomains and exact `end_date`s in the registry should be
  verified close to each event; they're flagged in registry `notes`.

## Dependencies

`requests`, `beautifulsoup4`, `PyYAML`. Installed fresh in the workflow runner.
