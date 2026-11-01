# Adding a conference

This guide covers everything a new conference needs, from checking its website to its first published digest. Each digest pick then carries links to its material: the abstract page, the paper, the slides (PDF or PPTX), and the recording, which the site embeds.

Most of the work is the **fetcher**: code that turns the conference's published program into the program text that the prompt is built from. Everything after the fetcher already works for any conference: the prompt, ToFaRev, the links step, the site and Links Refresh.

## 1. Check the source first

Before you write code, open the conference's program and answer these questions. The answers decide the rest.

| Question | Why it matters |
| --- | --- |
| Is there one page, an API or a feed that lists every talk with its title, speakers and abstract? | That is the fetcher's input. A single list page is easiest. Per-talk pages are fine, as netdev shows: the fetcher follows each one. |
| Does each talk have its own page? | It becomes the item's `page:` link, shown as **Abstract**. The links step reads it again later, when slides and recordings appear. |
| Where are the slides (PDF or PPTX), the papers and the recordings? | Each becomes a link key. Recordings on YouTube also get the embedded player. |
| Can GitHub Actions read the site? | Some sites block datacenter IPs (USENIX), or block automated clients outright (nanog.org blocks with Cloudflare). |
| When are the program and the recordings published? | Sets `end_date` and tells you whether Links Refresh will find more later. |

**Respect the site's bot protection.** If a site blocks automated access, the pipeline does not route around it by default: no headless browsers, no proxies, and no extraction services aimed at the blocked site. Instead, use the repo's local paths:

- `run_location: local` means CI skips the fetch, and you run it from your own machine, where the site serves you normally.
- The manual-paste path covers a source that blocks even that: you paste the program into the prompt by hand (see CLAUDE.md).

The one exception is **NANOG**. nanog.org blocks every automated client, so the repository owner explicitly approved reading its public agenda through Tavily Extract (2026-11-01). Record any such approval in the fetcher's docstring and in CLAUDE.md, as NANOG's are.

Recordings are a separate case. The links step looks them up on YouTube and checks each match, so a talk page that blocks the runner does not cost a pick its recording.

## 2. Pick or write a fetcher

Reuse a fetcher when the conference is hosted on a platform one already reads:

| Fetcher | Reads |
| --- | --- |
| `sched` | Any `*.sched.com` event (KubeCon, many vendor events) |
| `usenix` | USENIX technical-sessions pages (NSDI, USENIX Security, SREcon, OSDI…) |
| `ietf` | One IETF meeting, from the datatracker API |
| `sigcomm` | The SIGCOMM papers-info table |
| `netdev` | netdevconf.info sessions index and session pages |
| `nanog` | One NANOG meeting's agenda and talk pages, via Tavily Extract |
| `autocon` | One AutoCon edition: the program, NAF's program guide, its slides repository and NAF's YouTube uploads |
| `ovscon` | One OVS+OVNcon annual program: schedule rows, anchored abstracts, slides and YouTube recordings |
| `ciscolive` | One Cisco Live US/Europe edition from the public RainFocus on-demand catalog; abstracts and speakers, without login-only materials |
| `ripe` | RIPE 91+ meeting plan, sessions and full talk pages, including decks and native MP4 recordings |
| `nlnog` | Annual NLNOG Day table: titles, speakers, slides and videos (no abstracts) |
| `denog` | Official DENOG agenda's linked Pretalx JSON schedule export and attachments |
| `gtc` | One NVIDIA GTC (San Jose) edition: the JSON session-catalog API behind the catalog app |

Otherwise add `conferences/fetchers/<name>.py`:

```python
from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

class ExampleFetcher(Fetcher):
    name = "example"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")
        if looks_blocked(resp):
            return self.manual(entry, f"blocked ({resp.status_code}); paste the program by hand")
        text, count = self._parse(resp.text)   # program text, see below
        if count == 0:
            return FetchResult(status=NOT_PUBLISHED, detail="no talks parsed yet", source_url=url)
        return FetchResult(status=OK, program_text=text, source_url=url,
                           item_count=count, detail=f"parsed {count} talks")
```

Then register it in `conferences/fetchers/__init__.py` (`FETCHERS["example"] = ExampleFetcher()`).

Rules every fetcher follows:

- **Never raise.** Return `MANUAL_FALLBACK` (via `self.manual(...)`) on a transport error or a block. Return `NOT_PUBLISHED` while the program is not up.
- **Zero items beats wrong items.** If the page layout changed and you parse nothing, return `NOT_PUBLISHED`. After four failed runs the edition is marked `stalled`, which tells you the selectors need fixing.
- **Use the exact titles.** The links step finds each digest pick by matching its heading to an item title.
- Override `probe()` only when the source states its dates through an API, as IETF does. The default probe reads the dates off `program_url`.

### The program text a fetcher returns

```
## Track or session group

### Exact talk title
Speakers: Jane Doe (Example Corp), John Roe (Other Inc)
page: https://conf.example/talks/123 | slides: https://conf.example/talks/123.pptx | video: https://youtu.be/abc123defgh
The abstract, as published.
```

- `##` lines group items. Each `###` line is one item, titled exactly as the program does.
- A `Speakers:` or `Authors:` line comes under the title, with affiliations when the source has them.
- One links line holds `key: URL` parts separated by ` | `. Leave out a key you do not have; never guess a URL.

| Key | Shown as | Meaning |
| --- | --- | --- |
| `page:` | Abstract | The talk or paper page. It usually lists every material, and it is read again for slides and recordings. |
| `pdf:` | Paper | The paper. ToFaRev reads it before writing. |
| `slides:` | Slides | The deck: PDF, PPTX, PPT, KEY or ODP. Give it twice when the deck is published in two formats; both are shown, as `Slides (PDF)` and `Slides (PPTX)`. Put the PDF first: ToFaRev reads the first `slides:` link when there is no `pdf:`, and it can read only PDFs. |
| `video:` | Recording | The recording. YouTube links are embedded on the site, and a `?t=` timestamp sets where playback starts. |
| `materials:` | Materials | A page that collects a session's materials (IETF). |

The abstract follows on the next lines. With no abstract, the writer marks the pick "from abstract only", or works from the title and speakers alone.

**Slides kept outside the program** can be paired by file name, as AutoCon's are: NAF keeps each edition's decks in a GitHub repository, named after the speakers and a short title (`AC4-AndyLapteff-CLILifer.pdf`). `match_slides()` in `autocon.py` scores every talk–file pair: a speaker's name in the file name is required, and title words break ties. The best pairs are assigned first, so a speaker with two decks gets each one right. Files in Git LFS must be linked through `media.githubusercontent.com`; `raw.githubusercontent.com` serves only the LFS pointer.

**A program without abstracts** can borrow them from the official recordings, as AutoCon does. NAF uploads each talk with its abstract as the description, so the fetcher calls `conferences.links.find_video()`. That returns the checked upload with its description, and the description becomes the abstract. Import it inside `fetch()`: `conferences.links` imports the fetchers package.

**Prefer the conference's own playlist to per-talk search.** One playlist page lists every upload of an edition (`youtube_playlists()` finds it by title and channel, and `youtube_playlist()` lists it). Per-talk search costs a search and up to twelve video pages per talk. Under that load YouTube starts answering "sign in to confirm you're not a bot", and its results change from run to run. When the player data is withheld, `youtube_video()` reads the title, channel, date and description from the page's own data. Never try to get around the sign-in check itself.

## 3. Let the links step find recordings

`conferences/links.py` adds every pick's links row and searches YouTube for a missing recording. A search result is linked only when all three checks pass:

1. The talk title appears in the video's title or description.
2. The conference is named in the title or description, or the video is on the conference's channel.
3. The upload date is within eight months after the event.

For check 1, an upload that was renamed ("Opening Keynote: Jane Doe - A shorter title") still passes if one of the talk's speakers is named in the video title and half the title's words match. Speakers come from the item's `Speakers:` line.

For check 2, add the conference to `CHANNELS` and `DISPLAY` in `conferences/links.py`, keyed by the first segment of its registry key:

```python
CHANNELS = { ..., "nanog": ("nanog",) }      # words naming it, incl. the YouTube channel name
DISPLAY  = { ..., "nanog": "NANOG" }         # the word added to the search query
```

Without an entry, a search result must name the key's first segment (for example `srecon`) itself.

If a conference keeps its decks under a URL that holds nothing else, such as NANOG's `storage.googleapis.com/site-media-prod/meetings/`, add it to `DECK_URLS` in the same file. A PDF there is then filed as Slides, whatever its link text says.

## 4. Choose its type

`type` picks the reading guidance that goes into the prompt:

| Type | For |
| --- | --- |
| `academic` | Peer-reviewed papers (SIGCOMM, NSDI) |
| `standards` | Standards work (IETF) |
| `vendor` | Vendor and community conferences (KubeCon, Netdev) |
| `operator` | Network operators (NANOG, RIPE, SREcon) |
| `security` | Security research (USENIX Security) |

A new type needs `conferences/prompt/types/<type>.md`. The prompt build fails without it.

## 5. Add the series, or one edition

**A recurring conference gets a series** in `conferences/series.yaml`. Discovery then adds each new edition by itself:

```yaml
  - series: example
    enumerate: ordinal            # or: year
    key_template: "example-{n}"   # must match keys already in registry.yaml
    name_template: "Example {n}"
    type: operator
    fetcher: example
    lookahead: 2
    start: 41                     # first edition, for a brand-new series
    end_date_hint: "06-15"        # only if the source does not state dates
    program_url_template: "https://conf.example/{n}/agenda/"
    manual_fallback_url_template: "https://conf.example/{n}/agenda/"
    run_location: local           # only if the site blocks GitHub Actions
```

Check it without writing anything:

```bash
python3 scripts/discover_editions.py --dry-run --series example
```

**A one-off event, or a past edition you want now**, gets a block in `conferences/registry.yaml`. Use the same fields, but with a concrete `key`, `name`, `end_date`, `program_url` and `manual_fallback_url`. Never rename a key once it has a prompt, an issue or a digest.

## 6. Try it locally

```bash
pip install -r requirements.txt
python3 scripts/generate_digest_prompt.py --conference example-41   # writes prompts/example-41.md
grep -c '^### ' prompts/example-41.md                               # items parsed
grep -m5 -E '(^| \| )(page|pdf|slides|video):' prompts/example-41.md
```

Check that titles, speakers and abstracts look right, and that the links resolve. To try the links step without a model, put two or three item titles under `## Core` as `###` headings in a scratch digest, then run:

```bash
python3 scripts/enrich_links.py example-41 --digest /tmp/scratch-digest.md
```

## 7. Ship it

1. Commit the fetcher, its `FETCHERS` entry, the series or registry block, any `CHANNELS`/`DISPLAY` entry, and a line in the README's fetcher notes. Open a PR.
2. After merging, run **Conference Digest** from the Actions tab with `conference: <key>`. For `run_location: local`, run `generate_digest_prompt.py --conference <key>` on your machine and push `prompts/<key>.md` instead.
3. The scan commits the prompt, and **Digest Bot** drafts the digest. The draft arrives as a `digest: <key>` PR with the links rows and link counts.
4. Merge it. The site publishes the digest, and for 120 days **Links Refresh** adds recordings and slides as they appear, as `links: <key>` PRs.

## Worked example: NANOG

Adding NANOG took these steps:

1. **Source check.** The agenda (`nanog.org/events/nanog-<n>/agenda/`) has every session, with a talk page, presenters and the full abstract. Up to NANOG 96 it also lists the YouTube recording and the slide files; from NANOG 97 those are only on each talk page. nanog.org blocks all automated clients, so the owner approved reading it through Tavily Extract.
2. **Fetcher.** `conferences/fetchers/nanog.py` reads the agenda in one Tavily request and keeps sessions with an abstract, recording or slides, dropping meals, registration and socials. It then reads the talk pages that still lack slides or a recording, 20 per request. The day headers give the dates, so `probe()` is enough for discovery (`probe_is_sufficient = True`).
3. **Links.** NANOG got entries in `CHANNELS`/`DISPLAY` (its YouTube channel is "NANOG"). Its slide bucket went into `DECK_URLS`.
4. **Type.** `operator`, which already exists.
5. **Series and editions.** The series `nanog` uses `enumerate: ordinal` and `key_template: "nanog-{n}"`. NANOG 96, 97 and 98 went into the registry by hand. Discovery adds NANOG 99 once its agenda is published.
6. **Secrets and workflow.** `TAVILY_API_KEY` was added to the scan's discovery and prompt-generation steps.
7. **Local trial.** `generate_digest_prompt.py --conference nanog-98` read 53 talks, 44 with recordings and 45 with slides. `enrich_links.py` on a scratch digest added Abstract, Slides and Recording links. For a talk with no recording in the program, it found and verified the upload on NANOG's YouTube channel.

## Redoing a digest when better material arrives

Links Refresh adds recordings and slides to a published digest, but it never rewrites the text. If a program first had little to read (AutoCon's abstracts arrive with the recordings, weeks after the event), redo the digest once the material is out:

1. Regenerate the prompt: run **Conference Digest** with `conference: <key>`, or run `generate_digest_prompt.py --conference <key>` locally and push the prompt.
2. Run **Digest Bot** with `conference: <key>`. It drafts the digest again and opens a PR that replaces the published one.
