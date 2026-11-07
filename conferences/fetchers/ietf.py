"""IETF fetcher: the program of ONE meeting, from the datatracker JSON API.

What a meeting's program is: for each relevant working group that met, the
drafts on its agenda and the slide decks presented, with the session recording.
All of it comes from datatracker, which needs no key and does not bot-block:

    /api/v1/group/group/?acronym__in=<wgs>                 group id -> acronym
    /api/v1/meeting/session/?meeting__number=<n>&group__acronym__in=<wgs>
    /api/v1/meeting/sessionpresentation/?session__meeting__number=<n>&...
        -> per session, its materials in agenda order: agenda, slides decks,
           recording (type "recording", external_url = YouTube), minutes...
    /api/v1/doc/document/?name__in=<names>                 titles, URLs, abstracts
    /meeting/<n>/materials/<agenda-name>-<rev>             agenda text

Items:
  - every draft named on a WG agenda (regex over the agenda text), with its
    title and abstract, the deck presented for it, and its session recording;
  - every remaining deck (an operator talk, a problem statement) that is not a
    chairs' deck, with its slides and the recording.

Each item carries these link lines (one line, " | "-separated), which the
digest's links row and ToFaRev's source reading use:

    page: https://datatracker.ietf.org/doc/<draft>/        the draft
    slides: https://datatracker.ietf.org/meeting/<n>/materials/<deck>-<rev>
    video: https://youtu.be/<id>                           session recording
    materials: https://datatracker.ietf.org/meeting/<n>/session/<wg>

Before this fetcher was rewritten (2026-11), it listed the WGs' *current*
drafts and only labelled them with the meeting number, so editions fetched on
the same day got identical programs.

Outcomes:
  OK              -> at least one relevant WG posted an agenda or slides
  NOT_PUBLISHED   -> the meeting has no materials for these WGs yet
  MANUAL_FALLBACK -> transport error (the API doesn't bot-block, so this is rare)
"""

from __future__ import annotations

import html
import re
from datetime import date, timedelta
from typing import Iterable, Optional
from urllib.parse import urlencode

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

# WGs whose work touches networking, cloud, Kubernetes, and AI infrastructure.
RELEVANT_WGS = {
    # cloud / compute / AI traffic steering
    "cats", "teas",
    # transport / datapath / proxying
    "masque", "quic", "tls", "tsvwg", "httpbis", "tcpm", "ccwg", "scone",
    # routing / addressing / ops
    "idr", "grow", "savnet", "rtgwg", "6man", "v6ops", "dnsop", "add",
    "spring", "lsr", "srv6ops",
    # network virtualization / service
    "nvo3", "rift", "bess",
    # network management / automation
    "netconf", "netmod", "opsawg",
}

SITE = "https://datatracker.ietf.org"
API = f"{SITE}/api/v1"

DRAFT_RE = re.compile(r"\bdraft-[a-z0-9]+(?:-[a-z0-9]+)+", re.I)
REV_RE = re.compile(r"-\d{2}$")
# Decks that report on the WG rather than present work.
CHAIR_DECK_RE = re.compile(
    r"chair|wg[- ]?status|status[- ]update|agenda|welcome|note[- ]?well|"
    r"intro(?:duction)?[- ]slides|administrivia|wg[- ]update|working group update|"
    r"charter|milestones|combined slides|all slides|hackathon|open mic|wrap[- ]?up",
    re.I,
)
# Agenda numbering decks often carry: "01 ", "04-", "3.1 ".
NUMBERING_RE = re.compile(r"^\s*\d{1,2}(?:\.\d{1,2})*\s*[-_.)]?\s+|^\s*\d{1,2}[-_]")
STOP = {"the", "and", "for", "with", "from", "into", "over", "using", "draft", "ietf", "of", "to", "in", "on", "a", "an"}


class IetfFetcher(Fetcher):
    name = "ietf"

    # probe() asks datatracker's meeting API outright, so discovery needs no
    # second opinion; fetch() would only add that the meeting has materials.
    probe_is_sufficient = True

    def fetch(self, entry: dict) -> FetchResult:
        meeting_url = entry["program_url"]  # e.g. .../meeting/126/agenda.json
        number = self._meeting_number(meeting_url)
        if not number:
            return self.manual(entry, f"no meeting number in program_url {meeting_url}")

        wgs = ",".join(sorted(RELEVANT_WGS))
        try:
            groups = {g["resource_uri"]: g["acronym"] for g in self._all("group/group/", acronym__in=wgs)}
            sessions = self._all("meeting/session/", meeting__number=number, group__acronym__in=wgs)
            presentations = self._all(
                "meeting/sessionpresentation/",
                session__meeting__number=number,
                session__group__acronym__in=wgs,
            )
        except Exception as e:
            return self.manual(entry, f"datatracker API error: {e}")

        session_wg = {s["resource_uri"]: groups.get(s["group"], "") for s in sessions}
        # Materials per session, in agenda order.
        by_session: dict[str, list[tuple[int, str]]] = {}
        for p in presentations:
            name = p["document"].rstrip("/").rsplit("/", 1)[-1]
            by_session.setdefault(p["session"], []).append((int(p.get("order") or 0), name))
        if not by_session:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail=f"meeting {number}: no materials posted for the relevant WGs yet",
                source_url=meeting_url,
            )

        try:
            docs = self._docs(sorted({n for mats in by_session.values() for _, n in mats}))
        except Exception as e:
            return self.manual(entry, f"datatracker document API error: {e}")

        # Per WG: its sessions' decks and recordings, and its agenda(s).
        wg_sessions: dict[str, list[dict]] = {}
        for uri, mats in sorted(by_session.items(), key=lambda kv: kv[0]):
            wg = session_wg.get(uri, "")
            if not wg:
                continue
            decks, recordings, agendas = [], [], []
            for _, name in sorted(mats):
                d = docs.get(name)
                if not d:
                    continue
                kind = d["type"].rstrip("/").rsplit("/", 1)[-1]
                if kind == "slides":
                    decks.append(d)
                elif kind == "recording" and d.get("external_url"):
                    recordings.append(d["external_url"])
                elif kind == "agenda":
                    agendas.append(d)
            wg_sessions.setdefault(wg, []).append({"decks": decks, "recordings": recordings, "agendas": agendas})

        # Drafts named on each WG's agenda, in agenda order, with the agenda line.
        agenda_drafts: dict[str, list[tuple[str, str]]] = {}
        for wg, sess in wg_sessions.items():
            seen: set[str] = set()
            for agenda in {a["name"]: a for s in sess for a in s["agendas"]}.values():
                for draft, line in self._agenda_drafts(number, agenda):
                    if draft not in seen:
                        seen.add(draft)
                        agenda_drafts.setdefault(wg, []).append((draft, line))
        try:
            drafts = self._docs(sorted({d for v in agenda_drafts.values() for d, _ in v}))
        except Exception as e:
            return self.manual(entry, f"datatracker document API error: {e}")

        lines: list[str] = []
        count = deck_only = with_video = 0
        listed: set[str] = set()
        for wg in sorted(wg_sessions):
            sess = wg_sessions[wg]
            decks = [(d, i) for i, s in enumerate(sess) for d in s["decks"]]
            only_recording = next((r for s in sess for r in s["recordings"]), "") if len(sess) == 1 else ""
            materials = f"{SITE}/meeting/{number}/session/{wg}"
            items: list[str] = []
            used_decks: set[str] = set()

            for name, agenda_line in agenda_drafts.get(wg, []):
                d = drafts.get(name)
                if not d or name in listed or not d["type"].rstrip("/").endswith("/draft"):
                    continue
                listed.add(name)
                title = (d.get("title") or name).strip()
                deck = self._deck_for(name, title, decks, used_decks)
                video = (sess[deck[1]]["recordings"][:1] or [""])[0] if deck else only_recording
                links = [f"page: {SITE}/doc/{name}/"]
                if deck:
                    links.append(f"slides: {self._material_url(number, deck[0])}")
                if video:
                    links.append(f"video: {video}")
                    with_video += 1
                links.append(f"materials: {materials}")
                items.append(f"### {title}")
                items.append(f"Draft: {name} · Working group: {wg}")
                if agenda_line:
                    items.append(f"Agenda: {agenda_line}")
                items.append(" | ".join(links))
                if d.get("abstract"):
                    items.append(re.sub(r"\s+", " ", d["abstract"]).strip())
                items.append("")
                count += 1

            for deck, i in decks:
                title = NUMBERING_RE.sub("", (deck.get("title") or "").strip()).replace("_", " ").strip()
                if deck["name"] in used_decks or not title or CHAIR_DECK_RE.search(title) or CHAIR_DECK_RE.search(deck["name"]):
                    continue
                if DRAFT_RE.fullmatch(REV_RE.sub("", title.lower())):
                    continue  # a deck titled with a draft name that resolved to nothing
                used_decks.add(deck["name"])
                video = (sess[i]["recordings"][:1] or [""])[0]
                links = [f"slides: {self._material_url(number, deck)}"]
                if video:
                    links.append(f"video: {video}")
                    with_video += 1
                links.append(f"materials: {materials}")
                items.append(f"### {title}")
                items.append(f"Presentation · Working group: {wg}")
                items.append(" | ".join(links))
                items.append(f"Slides presented at the {wg} session; no Internet-Draft is linked to them.")
                items.append("")
                count += 1
                deck_only += 1

            if items:
                lines.append(f"## Working Group: {wg}")
                lines.append("")
                lines.extend(items)

        if count == 0:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail=f"meeting {number}: sessions found but no agenda drafts or slides yet",
                source_url=meeting_url,
            )
        return FetchResult(
            status=OK,
            program_text="\n".join(lines),
            source_url=meeting_url,
            item_count=count,
            detail=(f"{len(wg_sessions)} WGs met; {count - deck_only} agenda drafts, "
                    f"{deck_only} other presentations; {with_video} with a session recording"),
        )

    # ------------------------------------------------------------------ API --

    def _get_json(self, path: str, **params) -> dict:
        url = f"{API}/{path}?{urlencode({'format': 'json', **params})}"
        resp = http_get(url, timeout=60)
        resp.raise_for_status()
        return resp.json()

    def _all(self, path: str, **params) -> list[dict]:
        out: list[dict] = []
        offset = 0
        while True:
            page = self._get_json(path, limit=500, offset=offset, **params)
            objs = page.get("objects") or []
            out.extend(objs)
            offset += len(objs)
            if not objs or offset >= int(page.get("meta", {}).get("total_count") or 0):
                return out

    def _docs(self, names: list[str]) -> dict[str, dict]:
        out: dict[str, dict] = {}
        for i in range(0, len(names), 40):
            for d in self._all("doc/document/", name__in=",".join(names[i:i + 40])):
                out[d["name"]] = d
        return out

    @staticmethod
    def _material_url(number: str, doc: dict) -> str:
        return f"{SITE}/meeting/{number}/materials/{doc['name']}-{doc['rev']}"

    def _agenda_drafts(self, number: str, agenda: dict) -> list[tuple[str, str]]:
        """Drafts named in an agenda, in order, each with its (trimmed) agenda line."""
        filename = agenda.get("uploaded_filename") or ""
        if filename.lower().endswith(".pdf"):
            return []
        try:
            resp = http_get(self._material_url(number, agenda))
            if resp.status_code != 200:
                return []
            text = resp.text
        except Exception:
            return []
        if "<" in text and ">" in text:
            text = html.unescape(re.sub(r"<[^>]+>", " ", text))
        out: list[tuple[str, str]] = []
        for raw in text.splitlines():
            for m in DRAFT_RE.finditer(raw):
                name = REV_RE.sub("", m.group(0).lower().rstrip("-."))
                line = re.sub(r"\s+", " ", raw).strip()
                out.append((name, line[:200]))
        return out

    @staticmethod
    def _words(s: str) -> set[str]:
        return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1}

    def _deck_for(self, draft: str, title: str, decks: list[tuple[dict, int]], used: set[str]):
        """The deck presented for a draft: named after it, else the closest title."""
        stem = draft.removeprefix("draft-")
        for deck, i in decks:
            if deck["name"] not in used and (stem in deck["name"] or draft in (deck.get("title") or "").lower()):
                used.add(deck["name"])
                return deck, i
        # A deck named after the draft with words dropped or reordered
        # ("ietf126-bess-draft-jot-evpn-mcast-router-sync" for draft-jot-bess-...).
        stem_words = self._words(stem)
        for deck, i in decks:
            have = self._words(deck["name"]) | self._words(deck.get("title") or "")
            if deck["name"] not in used and len(stem_words) >= 3 and len(stem_words & have) / len(stem_words) >= 0.75:
                used.add(deck["name"])
                return deck, i
        want = self._words(title)
        best, score = None, 0.0
        for deck, i in decks:
            if deck["name"] in used:
                continue
            have = self._words(deck.get("title") or "") | self._words(deck["name"])
            s = len(want & have) / max(len(want), 1)
            if s > score:
                best, score = (deck, i), s
        if best and score >= 0.6:
            used.add(best[0]["name"])
            return best
        return None

    # --------------------------------------------------------------- probe --

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """Discovery probe via the datatracker meeting API.

        Unlike the HTML sources, IETF states its schedule outright:

            /api/v1/meeting/meeting/?number=<n>&format=json
            -> {"objects": [{"number", "date", "days", "city", ...}]}

        `date` is day one and `days` the length, so end_date is exact and the
        city gives the edition its "(Montreal)" suffix. Meetings are published
        years ahead, so a hit here is NOT "the meeting happened" — it is "this
        meeting number is real", which is precisely what discovery needs. The
        end_date then keeps the selection gate honest.
        """
        url = entry["program_url"]
        number = self._meeting_number(url)
        if not number:
            return super().probe(entry, years)

        api = f"{API}/meeting/meeting/?number={number}&format=json"
        try:
            resp = http_get(api)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code != 200:
            return ProbeResult(False, f"meeting API status {resp.status_code}", source_url=url)

        try:
            objects = resp.json().get("objects") or []
        except Exception as e:
            return ProbeResult(False, f"meeting API not JSON: {e}", source_url=url)
        if not objects:
            return ProbeResult(False, f"no meeting {number} scheduled yet", source_url=url)

        m = objects[0]
        # Only real IETF meetings; the same table also holds interims.
        if "meetingtypename/ietf" not in (m.get("type") or ""):
            return ProbeResult(False, f"meeting {number} is not a plenary IETF meeting",
                               source_url=url)

        end = None
        try:
            start = date.fromisoformat(m["date"])
            end = start + timedelta(days=max(int(m.get("days") or 1) - 1, 0))
        except Exception:
            pass

        return ProbeResult(
            True,
            f"meeting {number} scheduled" + (f", ends {end}" if end else ""),
            end_date=end,
            location=(m.get("city") or "").strip(),
            source_url=url,
        )

    @staticmethod
    def _meeting_number(url: str) -> str:
        m = re.search(r"/meeting/(\d+)/", url)
        return m.group(1) if m else ""
