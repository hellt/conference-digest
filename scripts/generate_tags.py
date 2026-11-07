#!/usr/bin/env python3
"""Tag every digest with searchable keywords, by running a local LLM.

Zensical's search index has a `tags` field per page, filled from the page's
front matter and weighted like `title`; the search UI also offers matching
tags as suggestions. This script produces those tags:

  1. For each digest missing from conferences/tags.yaml, it composes a prompt
     (the digest text plus the controlled vocabulary in
     conferences/tag-vocabulary.yaml) and sends it to a local LLM through an
     OpenAI-compatible chat endpoint - Ollama (`ollama serve`, default), a
     llama.cpp/LM Studio/vLLM server, anything speaking /v1/chat/completions.
  2. The reply must be strict JSON: post-level tags and tags per pick, keyed
     by the pick's exact `###` heading. Anything else is dropped or repaired,
     and a tag that is not in the vocabulary is printed so a good newcomer can
     be added to the vocabulary and a bad spelling kept out.
  3. The result is merged into conferences/tags.yaml, committed like any
     other hand-curated metadata. scripts/build_site.py reads that file and
     writes the tags into the front matter of the digest post and of each
     talk page; a hand edit of tags.yaml is kept until the digest is redone
     with `--force`.

No model call ever happens in CI - only when a person runs this locally,
exactly like `generate_digest_prompt.py --conference <key>`.

Usage:
  scripts/generate_tags.py                     # every digest not yet tagged
  scripts/generate_tags.py --digest <key>      # one digest
  scripts/generate_tags.py --force             # redo digests that are tagged
  scripts/generate_tags.py --print-prompt <key>   # the manual path: paste the
  scripts/generate_tags.py --apply <key> <file>   # prompt into any chat, save
                                                  # the JSON reply, apply it
  scripts/generate_tags.py --from-digest <key>    # convert the keywords block
                                                  # a hand-written digest
                                                  # carries (prompt output)
                                                  # into tags.yaml and strip it

New digests do not need this: their prompt (conferences/prompt/base.md) has
the writer emit the same block, and propose_digest.py converts it in the
Digest Bot's PR, before the digest is committed. This script is the backfill
and hand-run tool."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import (  # noqa: E402
    DIGESTS,
    extract_tags_block,
    nest_lists,
    pick_sections,
    read_digest,
    split_body,
)

ROOT = Path(__file__).resolve().parent.parent
VOCABULARY = ROOT / "conferences" / "tag-vocabulary.yaml"
TAGS = ROOT / "conferences" / "tags.yaml"
BASE_URL = os.environ.get("TAGS_BASE_URL", "http://localhost:11434/v1")
API_KEY = os.environ.get("TAGS_API_KEY")
MODEL = os.environ.get("TAGS_MODEL")
MAX_POST_TAGS = 8
MAX_TALK_TAGS = 4

HEADER = """\
# Search keywords per digest: tags for the digest post and for each pick,
# keyed by the pick's exact `###` heading in digests/<key>.md.
# Written by scripts/generate_tags.py (a local LLM run; see it for the
# vocabulary in conferences/tag-vocabulary.yaml) and read by
# scripts/build_site.py. Hand edits are welcome and survive until the digest
# is regenerated with --force.
"""


def normalize(tag: str) -> str:
    """lowercase, hyphens, no surrounding punctuation - a search token set."""
    return re.sub(r"[^a-z0-9]+", "-", tag.strip().lower()).strip("-")


def load_vocabulary() -> dict[str, str]:
    data = yaml.safe_load(VOCABULARY.read_text(encoding="utf-8")) or {}
    vocab = data.get("vocabulary") or {}
    if not isinstance(vocab, dict) or not vocab:
        raise SystemExit(f"{VOCABULARY} has no `vocabulary:` mapping")
    return {normalize(k): str(v) for k, v in vocab.items()}


def load_tags() -> dict:
    if TAGS.is_file():
        data = yaml.safe_load(TAGS.read_text(encoding="utf-8")) or {}
        return {k: v for k, v in data.items() if isinstance(v, dict)}
    return {}


def save_tags(data: dict) -> None:
    TAGS.write_text(
        HEADER + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )


def headings_of(body: str) -> list[str]:
    """A digest body's pick headings, in order, as build_site.py keys them."""
    h1, intro, rest = split_body(nest_lists(body))
    return [p["heading"] for p in pick_sections(rest)]


def headings(key: str) -> list[str]:
    """The digest's pick headings, read from digests/<key>.md."""
    meta, body = read_digest(DIGESTS / f"{key}.md")
    return headings_of(body)


def compose_prompt(key: str, vocab: dict[str, str]) -> str:
    meta, body = read_digest(DIGESTS / f"{key}.md")
    heading_list = headings_of(body)
    vocab_text = "\n".join(f"- {t}: {d}" for t, d in sorted(vocab.items()))
    return f"""\
You are tagging one conference digest for a site search index. The reader is a \
product manager working on networking, cloud platforms, Kubernetes, and AI.

Digest {key} - "{meta.get('conference', key)}":

---8<--- DIGEST START
{body.strip()}
---8<--- DIGEST END

Tag vocabulary (prefer these; a tag is a lowercase hyphenated topic):

{vocab_text}

Return strict JSON, nothing else - no markdown fences, no prose - of the form:

{{"post": ["tag", ...], "talks": {{"<pick heading>": ["tag", ...], ...}}}}

Rules:
- "post": {MAX_POST_TAGS} at most, the topics this digest as a whole is about.
- "talks": exactly one entry per pick heading below, keyed by that exact \
string (copy it character for character, including any presenter part), each \
with {MAX_TALK_TAGS} at most tags naming what the talk is about - the \
technology or practice, not the tier it was picked in and not the conference.
- Use the vocabulary above when it fits. Invent a new tag only when nothing \
in the vocabulary does, and then reuse exactly one new spelling if the \
concept repeats.
- Tags name the reader's domains (networking, cloud, Kubernetes, AI, and the \
automation that runs them), not generic words ("talk", "overview", \
"interesting").

Pick headings, in order:
{chr(10).join("- " + h for h in heading_list)}
"""


def parse_reply(reply: str) -> dict:
    """The JSON object from an LLM reply; tolerates fences and stray prose."""
    text = re.sub(r"^```(?:json)?|```$", "", reply.strip(), flags=re.MULTILINE).strip()
    start = text.find("{")
    depth, in_string, escaped = 0, False, False
    for i, ch in enumerate(text[start:], start):
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
        elif ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise ValueError("no JSON object in the reply")


def clean_tags(raw, limit: int, vocab: dict[str, str], known: set[str]) -> list[str]:
    """Normalized, deduped tags in the LLM's order; vocabulary misses reported."""
    tags: list[str] = []
    for t in raw or []:
        tag = normalize(str(t))
        if not tag or tag in tags or len(tags) >= limit:
            continue
        if tag not in vocab and tag not in known:
            known.add(tag)
            print(f"    new tag outside the vocabulary: {tag}")
        tags.append(tag)
    return tags


# The keywords block (fenced `post`/`talks` json) is parsed by
# extract_tags_block() in build_site.py, imported above.


def validate(key: str, reply: dict, vocab: dict[str, str], known: set[str],
             body: str | None = None) -> tuple[list[str], dict[str, list[str]]]:
    """The reply, reduced to what this digest actually contains. `body` is
    the digest text to read headings from when it is not on disk yet (the
    propose job validates the artifact before writing digests/<key>.md)."""
    expected = headings_of(body) if body is not None else headings(key)
    by_heading = {}
    talks = reply.get("talks") or {}
    if not isinstance(talks, dict):
        raise ValueError("`talks` is not an object")
    for heading in expected:
        raw = talks.get(heading)
        if raw is None:   # the LLM may have trimmed the heading - try a prefix match
            raw = next((v for k, v in talks.items() if str(k).strip().startswith(heading[:40])), None)
        by_heading[heading] = clean_tags(raw, MAX_TALK_TAGS, vocab, known)
    for k in talks:
        if k not in by_heading:
            print(f"    dropped a key matching no pick: {str(k)[:60]}")
    post = clean_tags(reply.get("post"), MAX_POST_TAGS, vocab, known)
    return post, by_heading


def call_llm(prompt: str, model: str, base_url: str) -> str:
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    response = requests.post(
        f"{base_url.rstrip('/')}/chat/completions",
        headers=headers,
        json={"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0},
        timeout=600,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def apply_reply(key: str, reply: dict, vocab: dict[str, str], tags: dict, known: set[str]) -> bool:
    try:
        post, talks = validate(key, reply, vocab, known)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"  {key}: unusable reply ({e}); left for a rerun")
        return False
    tags[key] = {"post": post, "talks": talks}
    print(f"  {key}: {len(post)} post tag(s), {len(talks)} pick(s) tagged")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--digest", help="tag only this digest key")
    parser.add_argument("--force", action="store_true", help="redo digests that already have tags")
    parser.add_argument("--print-prompt", metavar="KEY", help="print the prompt for a digest, for the manual path")
    parser.add_argument("--apply", nargs=2, metavar=("KEY", "FILE"), help="apply a saved JSON reply to a digest")
    parser.add_argument("--from-digest", metavar="KEY", dest="from_digest",
                        help="read the keywords block out of a hand-written digests/<key>.md, merge it into tags.yaml, strip it from the digest")
    parser.add_argument("--model", default=MODEL, help=f"model name (default: $TAGS_MODEL or {MODEL})")
    parser.add_argument("--base-url", default=BASE_URL, help=f"OpenAI-compatible endpoint (default: {BASE_URL})")
    args = parser.parse_args()

    vocab = load_vocabulary()
    known: set[str] = set()

    if args.print_prompt:
        print(compose_prompt(args.print_prompt, vocab), end="")
        return 0

    if args.from_digest:
        key = args.from_digest
        path = DIGESTS / f"{key}.md"
        body, block = extract_tags_block(path.read_text(encoding="utf-8"))
        if not block:
            raise SystemExit(f"digests/{key}.md has no keywords block")
        try:
            reply = parse_reply(block)
            post, talks = validate(key, reply, vocab, known, body=body)
        except (ValueError, json.JSONDecodeError) as e:
            raise SystemExit(f"the keywords block of digests/{key}.md is unusable: {e}")
        merged = load_tags()
        merged[key] = {"post": post, "talks": talks}
        path.write_text(body, encoding="utf-8")
        save_tags(merged)
        print(f"{key}: {len(post)} post tag(s), {len(talks)} pick(s) tagged; block stripped from the digest")
        return 0

    tags = load_tags()
    if args.apply:
        key, path = args.apply
        raw = Path(path).read_text(encoding="utf-8")
        try:   # a saved LLM reply (with or without fences), or a hand-edited one
            reply = parse_reply(raw)
            if not isinstance(reply, dict):
                raise ValueError("not an object")
        except (ValueError, json.JSONDecodeError):
            reply = yaml.safe_load(raw)
            if not isinstance(reply, dict):
                raise SystemExit(f"{path} holds neither a JSON object nor a YAML mapping")
        if apply_reply(key, reply, vocab, tags, known):
            save_tags(tags)
            print(f"wrote {TAGS}")
            return 0
        return 1

    if not args.model:
        parser.error("a --model is needed (or set $TAGS_MODEL); e.g. --model qwen3:14b for Ollama")

    keys = [args.digest] if args.digest else sorted(p.stem for p in DIGESTS.glob("*.md"))
    todo = [k for k in keys if args.force or not tags.get(k)]
    if not todo:
        print("every digest is already tagged (use --force to redo)")
        return 0

    print(f"tagging {len(todo)} digest(s) via {args.base_url} ({args.model})")
    done = failed = 0
    for key in todo:
        try:
            reply = parse_reply(call_llm(compose_prompt(key, vocab), args.model, args.base_url))
        except Exception as e:   # a model or endpoint problem on one digest never kills the run
            print(f"  {key}: LLM call failed ({e})")
            failed += 1
            continue
        done += 1 if apply_reply(key, reply, vocab, tags, known) else 0
        time.sleep(0.2)   # be polite to a small local server
    if done:
        save_tags(tags)
        print(f"wrote {TAGS}: {done} tagged, {failed} failed")
    else:
        print(f"nothing tagged ({failed} failed)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
