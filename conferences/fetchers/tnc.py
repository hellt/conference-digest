"""TNC (GÉANT): dates via Tavily; the programme itself is a manual paste.

tnc{yy}.geant.org serves a plain-403 to datacenter clients, so both probe and
fetch go through Tavily Extract (repository owner approved reading blocked
public pages through Tavily, 2026-11-01; the scan steps carry TAVILY_API_KEY).
The site's WordPress pages state the dates, which the probe reads; but the
programme itself is a client-side app whose data has no public endpoint — and
GÉANT's Indico (events.geant.org, which backs it) sits behind a JS verification
interstitial that blocks automated clients too. So fetch() can never produce
the program text: it returns manual_fallback pointing at the programme page,
and the digest is written from the manual-paste path (see CLAUDE.md).
"""

from __future__ import annotations

import os
import re

from .nanog import tavily_extract

from .base import Fetcher, FetchResult, ProbeResult, scan_end_date


class TncFetcher(Fetcher):
    name = "tnc"

    def _page(self, entry: dict) -> str:
        key = os.environ.get("TAVILY_API_KEY", "").strip()
        if not key:
            raise RuntimeError("TAVILY_API_KEY not set; tnc.geant.org blocks datacenter clients")
        return tavily_extract(entry["program_url"], key)

    def fetch(self, entry: dict) -> FetchResult:
        try:
            page = self._page(entry)
            end = scan_end_date(page)
            note = "programme page reachable"
            if end:
                note += f"; event ended {end.isoformat()}"
            return self.manual(
                entry,
                f"programme is a client-side app with no public data endpoint "
                f"({note}); open manual_fallback_url and paste the programme into the prompt",
            )
        except Exception as e:
            return self.manual(entry, f"could not read the site through Tavily: {e}")

    def probe(self, entry: dict, years=None) -> ProbeResult:
        url = entry["program_url"]
        try:
            page = self._page(entry)
        except Exception as e:
            return ProbeResult(False, f"probe error: {e}", source_url=url)
        end = scan_end_date(page, years)
        return ProbeResult(True, "site readable through Tavily; dates scanned" if end
                           else "site readable; dates not found", end_date=end, source_url=url)
