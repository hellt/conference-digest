# Site targets mirror containerlab's: uv runs the pinned Zensical from the
# `docs` dependency group. build_site.py renders digests/ into docs/ first.
UV ?= uv

.PHONY: site
site:
	$(UV) run --group docs python scripts/build_site.py
	$(UV) run --group docs zensical build --clean --strict 2>&1 | tee zensical-build.log
	@# Zensical can exit 0 on hard build errors (zensical/zensical#491).
	@test -f site/index.html
	@! sed 's/\x1b\[[0-9;]*m//g' zensical-build.log | grep -qE '^Error:' || (echo "Zensical reported build errors" && exit 1)
	@rm -f zensical-build.log
	@# Talk results would repeat their title as the breadcrumb; say the conference instead.
	$(UV) run --group docs python scripts/search_paths.py site

.PHONY: serve-site
serve-site:
	$(UV) run --group docs python scripts/build_site.py
	$(UV) run --group docs zensical serve -a 0.0.0.0:8001

# Point the Digest Bot at a ToFaRev commit, as containerlab pins /tofarev review.
# The pin is the only 40-hex string in digest-bot.yml (`uses:` ref and bot_ref).
.PHONY: pin-tofarev
pin-tofarev:
	@echo "$(SHA)" | grep -Eqx '[0-9a-f]{40}' || { echo "usage: make pin-tofarev SHA=<full ToFaRev commit SHA>"; exit 1; }
	sed -i -E 's/[0-9a-f]{40}/$(SHA)/g' .github/workflows/digest-bot.yml
	@test "$$(grep -c '$(SHA)' .github/workflows/digest-bot.yml)" -eq 2 && echo "pinned ToFaRev to $(SHA)"
