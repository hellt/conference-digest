#!/usr/bin/env python3
"""Render run_summary.json into per-conference GitHub issue specs.

Writes issues.json: a list of {key, title, body, labels} objects, one per open
work item (every conference past its end_date and not yet digested). The
workflow's github-script step UPSERTS these: if an open issue with the matching
"conf:<key>" label exists, it updates the body; otherwise it creates one.

The issue exists for the whole window between "event is past" and "digest
merged", independent of whether automated fetch succeeded. Its body states the
current status and the exact next action (run locally / run the prompt / fix
the fetcher / wait). The close-workflow closes it when digests/<key>.md lands.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
summary = json.loads((ROOT / "run_summary.json").read_text(encoding="utf-8"))
today = date.today().isoformat()


def conf_label(key: str) -> str:
    return f"conf:{key}"


def run_prompt_instructions(key: str) -> str:
    return (
        "**ToFaRev drafts this digest automatically.** The Digest Bot workflow "
        "runs after this scan and opens a pull request titled "
        f"`digest: {key}`. Review it and merge it: that publishes the digest to "
        "the site and closes this issue. To redo a draft, close its PR and run "
        f"Digest Bot from the Actions tab with `conference: {key}`.\n\n"
        "To write it yourself instead:\n\n"
        "- In a Claude session with filesystem access to this repo, tell it:\n"
        f"  \"Read `prompts/{key}.md` and follow its instructions.\"\n"
        f"- Or open `prompts/{key}.md`, paste it into Claude, and run it.\n\n"
        f"The result must be committed as `digests/{key}.md` (that auto-closes "
        "this issue)."
    )


def local_fetch_instructions(key: str, program_url: str) -> str:
    return (
        "This source blocks automated fetches from CI (datacenter IPs get a "
        "403), so generate the prompt **from your own machine**:\n\n"
        "1. Fetch the program and build the prompt:\n"
        "   ```bash\n"
        "   cd conference-digest\n"
        f"   python3 scripts/generate_digest_prompt.py --conference {key}\n"
        "   ```\n"
        f"   This writes `prompts/{key}.md`.\n"
        f"2. Commit and push `prompts/{key}.md` to `main`. ToFaRev then drafts "
        "the digest and opens a pull request; merging it closes this issue.\n"
        "   _Or_ run the digest yourself: in a Claude session with filesystem "
        f"access to this repo, tell it: \"Read `prompts/{key}.md` and follow its "
        f"instructions.\", then commit the result as `digests/{key}.md`.\n\n"
        f"_Fallback, only if your machine is also blocked: open {program_url}, copy "
        f"the program, and paste it into `prompts/{key}.md` where it says "
        "`{PROGRAM_TEXT}` before running step 2._"
    )


def manual_paste_instructions(key: str, manual_url: str) -> str:
    return (
        "Automated fetch reached the site but returned nothing parseable. Try a "
        "local run first — it usually works from a non-datacenter IP:\n\n"
        "1. Fetch and build the prompt locally:\n"
        "   ```bash\n"
        "   cd conference-digest\n"
        f"   python3 scripts/generate_digest_prompt.py --conference {key}\n"
        "   ```\n"
        f"   If that writes `prompts/{key}.md` with real content, continue.\n"
        f"2. Commit and push `prompts/{key}.md` to `main`. ToFaRev then drafts "
        "the digest and opens a pull request; merging it closes this issue.\n"
        "   _Or_ tell a repo-connected Claude session: "
        f"\"Read `prompts/{key}.md` and follow its instructions.\", then commit "
        f"the result as `digests/{key}.md`.\n\n"
        f"_Fallback, if the local run also comes back empty: open {manual_url}, "
        f"copy the program, paste it into `prompts/{key}.md` where it says "
        "`{PROGRAM_TEXT}`, then do step 2._"
    )


def discovered_note(item: dict) -> str:
    """Banner for editions nobody typed in by hand.

    discover_editions.py adds these from conferences/series.yaml once the source
    confirms the edition exists. The end_date may be an estimate from the series
    hint rather than something the source stated, and that date is what decides
    when the digest is due — so ask for one look before trusting it.
    """
    when = item.get("discovered")
    if not when:
        return ""
    return (
        f"> Auto-discovered on {when} from `conferences/series.yaml` — this "
        "edition was not added by hand.\n"
        "> Worth a glance at the registry entry: the `end_date` may be an "
        "estimate from the series hint, and the name/URL follow the series "
        "template.\n\n"
    )


def body_for(item: dict) -> str:
    key = item["key"]
    status = item["status"]
    header = f"**{item['name']}**  \n`status: {status}`\n\n"
    header += discovered_note(item)

    if status == "ready":
        n = item.get("items", "?")
        action = (
            f"The program was fetched ({n} items) and the prompt is ready at "
            f"[`prompts/{key}.md`](../blob/main/prompts/{key}.md).\n\n"
            + run_prompt_instructions(key)
        )
    elif status == "local_required":
        action = local_fetch_instructions(key, item.get("program_url", ""))
    elif status == "manual":
        action = manual_paste_instructions(key, item.get("manual_url", "") or item.get("program_url", ""))
    elif status == "stalled":
        action = (
            f"Automated fetch has failed {item.get('attempts', '?')} times "
            f"(`{item.get('detail', '')}`). The site structure or URL has "
            "probably changed and the fetcher needs adjusting. Until then you "
            "can fetch locally / by hand:\n\n"
            + local_fetch_instructions(key, item.get("program_url", ""))
        )
    elif status == "waiting":
        action = (
            "The event is over but the program/artifacts aren't published yet "
            f"(`{item.get('detail', '')}`). Nothing to do — this will retry "
            "automatically. You can also force a local run once the program is "
            f"up: `python3 scripts/generate_digest_prompt.py --conference {key}`."
        )
    else:
        action = f"Status `{status}`: {item.get('detail', '')}"

    footer = (
        "\n\n---\n"
        f"_Updated {today}. This issue auto-closes when `digests/{key}.md` is "
        "committed to `main`._"
    )
    return header + action + footer


def title_for(item: dict) -> str:
    return f"Digest: {item['name']}"


issues = []
for item in summary.get("items", []):
    key = item["key"]
    issues.append(
        {
            "key": key,
            "title": title_for(item),
            "body": body_for(item),
            "labels": ["digest", f"status:{item['status']}", conf_label(key)],
        }
    )

(ROOT / "issues.json").write_text(json.dumps(issues, indent=2) + "\n", encoding="utf-8")
print(f"prepared {len(issues)} issue spec(s): {[(i['key']) for i in issues]}")
