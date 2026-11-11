#!/usr/bin/env python3
"""Smoke-check the built Briefing site with a real browser.

make site
python3 -m http.server 8766 --directory site
uv run --with playwright python scripts/check_site_ui.py http://127.0.0.1:8766

Playwright is a development-only tool; screenshots stay in design-review/.
"""
from pathlib import Path
import re
import sys
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = (sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8001').rstrip('/')
SHOTS = ROOT / 'design-review' / 'screenshots'
SHOTS.mkdir(parents=True, exist_ok=True)

# Every generated digest section and pick has a real permalink and TOC target.
for source in (ROOT/'digests').glob('*.md'):
    html=(ROOT/'site'/source.stem/'index.html').read_text()
    headings=re.findall(r'<h([23])\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>',html,re.S)
    assert headings, source.name
    for _,anchor,content in headings:
        assert f'href="#{anchor}"' in content and 'class="headerlink"' in content, (source.name,anchor)
        assert f'href="#{anchor}" class="md-nav__link"' in html, (source.name,anchor)

# Firefox reserves a gutter for the sidebars' vertical scrollbar
# (scrollbar-gutter: stable; Chromium opts out). A sidebar whose content is
# sized to the full sidebar width then grows an empty horizontal scrollbar, so
# replay that gutter here and require the content to fit beside it.
SIDEBAR_OVERFLOW = """(()=>{const s=document.createElement('style');
  s.textContent='.md-sidebar__scrollwrap{scrollbar-gutter:stable!important}';document.head.append(s);
  const bad=[...document.querySelectorAll('.md-sidebar__scrollwrap')].filter(w=>w.offsetParent&&w.scrollWidth>w.clientWidth)
    .map(w=>[w.closest('.md-sidebar').className,w.scrollWidth,w.clientWidth]);
  s.remove();return bad})()"""

with sync_playwright() as p:
    binary=Path(p.chromium.executable_path)
    if not binary.exists():
        cached=sorted(Path.home().glob('.cache/ms-playwright/chromium-*/chrome-linux*/chrome'))
        if cached: binary=cached[-1]
    browser=p.chromium.launch(executable_path=str(binary))
    for theme,scheme in [('light','default'),('dark','slate')]:
        context=browser.new_context(viewport={'width':1440,'height':1080},color_scheme=theme)
        page=context.new_page()
        errors=[]
        search_requests=[]
        page.on('pageerror',lambda error:errors.append(str(error)))
        context.on('request',lambda request:search_requests.append(request.url) if 'search' in request.url else None)
        for path,name in [('/','home'),('/nsdi-2025/','digest')]:
            page.goto(BASE+path,wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            assert page.locator('body').get_attribute('data-md-color-scheme') == scheme
            assert page.locator('.md-tabs .md-powered-logo:visible').get_attribute('src').endswith(f'-{theme}.svg')
            assert page.locator('.md-tabs .md-powered-logo:visible').evaluate('img=>img.complete && img.naturalWidth>0')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            assert not page.evaluate(SIDEBAR_OVERFLOW), page.evaluate(SIDEBAR_OVERFLOW)
            assert page.locator('.ambient,.line-field,.featured').count()==0
            assert 'From the reading list' not in page.locator('body').inner_text()
            if name=='home':
                cards=page.locator('.md-post--excerpt')
                assert cards.count()==12
                assert page.locator('.cd-hero h1').inner_text()=='All the talks in one place'
                assert page.locator('header.md-typeset h2').count()==0
                assert cards.first.locator('time').count()==1
                assert cards.first.locator('.md-meta__item').count()>=2
                assert 'min read' not in cards.first.inner_text()
                assert cards.first.locator('.md-post__content > p').inner_text().strip()
                # Pick counts carry the tiers' signal bars; tags keep their own
                # links above the row-wide title link.
                assert cards.evaluate_all("cs=>cs.every(c=>/^\\d+ picks?$/.test(c.querySelector('.cd-picks__total')?.textContent.trim()||''))")
                assert page.locator('.md-post--excerpt .cd-bars--core').count()==12
                tag=cards.first.locator('.cd-post-tag').first
                assert re.search(r'/tags/[a-z0-9-]+/$',tag.get_attribute('href')), tag.get_attribute('href')
                assert tag.evaluate("t=>document.elementFromPoint(t.getBoundingClientRect().x+4,t.getBoundingClientRect().y+4).closest('a')===t")
                assert page.locator('.cd-hero').bounding_box()['height'] < 280
            else:
                assert page.locator('.pick').count()==17
                toc=page.locator('.md-sidebar--secondary')
                assert toc.is_visible()
                assert toc.bounding_box()['x'] > page.locator('.md-content--post').bounding_box()['x']
                assert page.locator('.pick-link').evaluate_all("links=>links.every(e=>parseFloat(getComputedStyle(e).borderRadius)>0 && getComputedStyle(e).fontFamily.startsWith('\"IBM Plex Mono\"'))")
                assert page.evaluate("document.fonts.check('16px \"IBM Plex Sans\"') && document.fonts.check('500 12px \"IBM Plex Mono\"')")
                # Picks are numbered across the digest, and tiers carry 3/2/1 bars.
                assert page.locator('.digest-body').evaluate("b=>getComputedStyle(b).counterReset")=='pick 0'
                numbers=page.locator('.digest-body .pick').evaluate_all("ps=>ps.map(p=>[getComputedStyle(p).counterIncrement,getComputedStyle(p.querySelector('h3'),'::before').content])")
                assert numbers==[['pick 1','counter(pick, decimal-leading-zero)']]*17, numbers
                bars=page.locator('h2.tier').evaluate_all("hs=>Object.fromEntries(hs.map(h=>[h.id,getComputedStyle(h,'::before').backgroundImage.split('linear-gradient').slice(1).map(g=>g.match(/rgba?[(][^)]*[)]/)[0])]))")
                lit={tier:[colour==bars['core'][0] for colour in bars[tier]] for tier in ('core','adjacent','wildcard')}
                assert lit=={'core':[True]*3,'adjacent':[True,True,False],'wildcard':[True,False,False]}, bars
                assert page.locator('.pick-link').evaluate_all("links=>links.every(e=>e.textContent===e.textContent.trim() && !e.querySelector('.twemoji'))"), 'Source links must not underline leftover icon spacing'
                assert page.locator('.digest-facts + .digest-body > h2.tier:first-child').evaluate("e=>getComputedStyle(e).borderTopWidth==='0px'"), 'The first section must not duplicate the metadata divider'
                assert page.locator('.digest-fact').all_text_contents() == ['April 28, 2025 – April 30, 2025', 'Program']
            page.mouse.move(0,0)
            page.screenshot(path=str(SHOTS/f'briefing-{name}-{theme}.png'),animations='disabled')
            for width in [360,390,768,1024]:
                page.set_viewport_size({'width':width,'height':844})
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (theme,name,width)
                assert not page.evaluate(SIDEBAR_OVERFLOW), (theme,name,width,page.evaluate(SIDEBAR_OVERFLOW))
                assert page.locator('.md-nav__item--powered .md-powered-logo').count()==2
                if width==390:
                    page.wait_for_timeout(250)
                    page.screenshot(path=str(SHOTS/f'briefing-{name}-{theme}-mobile.png'),animations='disabled')
            page.set_viewport_size({'width':1440,'height':1080})

        # Search a paper not listed on the first archive page. This must use
        # Zensical's complete index, native snippets and keyboard navigation.
        page.goto(BASE+'/',wait_until='networkidle')
        page.locator('.md-search__button').click()
        query=page.get_by_role('combobox',name='Search')
        query.fill('ONCache')
        result=page.get_by_role('option').filter(has_text='ONCache').first
        result.wait_for()
        assert '/nsdi-2025/oncache-' in result.get_attribute('href')
        assert result.locator('mark').count() >= 1
        assert 'NSDI' in result.inner_text() and 'Why:' in result.inner_text()
        page.screenshot(path=str(SHOTS/f'briefing-search-{theme}.png'),animations='disabled')
        query.press('Enter')
        page.wait_for_url('**/nsdi-2025/oncache-*/?h=ONCache')
        page.goto(BASE+'/nsdi-2025/',wait_until='networkidle')
        assert search_requests, 'No native search assets were requested'

        # Scroll tracking must also initialize after search/instant navigation.
        page.wait_for_function("document.querySelector('#adjacent') !== null")
        page.wait_for_function("document.querySelector('.pick h3').getBoundingClientRect().top < innerHeight")
        page.evaluate('getSelection()?.removeAllRanges()')
        page.locator('#adjacent').evaluate("e=>e.scrollIntoView({block:'start'})")
        page.wait_for_function("!!document.querySelector('.md-nav--secondary a.md-nav__link--active[href$=\"#adjacent\"]')")
        page.wait_for_function("document.querySelector('#adjacent').getBoundingClientRect().top < 200")
        page.mouse.move(0,0)
        page.screenshot(path=str(SHOTS/f'briefing-scrollspy-{theme}.png'),animations='disabled')
        page.locator('#adjacent > .headerlink').click()
        assert page.url.endswith('#adjacent')
        page.reload(wait_until='networkidle')
        assert page.locator('#adjacent').bounding_box()['y'] >= page.locator('.md-header').bounding_box()['height'] - 5

        # The native palette persists across a page load.
        page.locator('.md-switch__target:not([hidden])').click()
        opposite='slate' if scheme=='default' else 'default'
        page.wait_for_function('(scheme)=>document.body.dataset.mdColorScheme===scheme',arg=opposite)
        page.goto(BASE+'/',wait_until='networkidle')
        assert page.locator('body').get_attribute('data-md-color-scheme') == opposite

        # Existing recordings still sit after the author and before Why; the
        # first click swaps in the privacy-enhanced player, with no eager iframe.
        page.goto(BASE+'/nsdi-2025/',wait_until='networkidle')
        pick=page.locator('.pick').first
        assert pick.locator('iframe').count()==0
        assert pick.evaluate('''el=>{const video=el.querySelector('.pick-video');const author=[...el.querySelectorAll('strong')].find(e=>e.textContent.startsWith('Authors'));const why=[...el.querySelectorAll('strong')].find(e=>e.textContent.startsWith('Why'));return Boolean(author.compareDocumentPosition(video)&Node.DOCUMENT_POSITION_FOLLOWING)&&Boolean(video.compareDocumentPosition(why)&Node.DOCUMENT_POSITION_FOLLOWING)}''')
        pick.locator('.pick-video__thumb').click()
        assert pick.locator('iframe').get_attribute('src').startswith('https://www.youtube-nocookie.com/embed/')
        assert not errors, errors
        context.close()
        print(f'PASS {theme}: responsive pages, logos, native search, permalinks, scrollspy, palette persistence and recordings',flush=True)
    browser.close()
print('All digest heading links and browser checks passed. Screenshots saved in design-review/screenshots/.')
