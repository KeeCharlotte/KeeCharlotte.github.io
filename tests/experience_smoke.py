"""Offline browser regression tests for the static portfolio.

Install: python -m pip install playwright
         python -m playwright install chromium
Run: python tests/experience_smoke.py --browser /usr/bin/chromium
Use --browser only when using a system Chromium. No network is needed by tests.
The fixture inlines local CSS/JS without modifying their contents. This tests
DOM, rendering, history and focus, not HTTP delivery or Google Fonts loading.
"""
import argparse
import hashlib
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ['Fiction', 'Achievements', 'Survival Skills', 'Games', 'Discipline',
              'Software', 'Cognition', 'Music', 'Civilizational Mastery', 'Art']
COGNITION = ['personality-destiny', 'worldview', 'emotion-reason', 'meaning-freedom',
             'self-integration', 'human-ethics']
SURVIVAL = ['threats', 'body', 'environment', 'location', 'resources', 'priority']
SURVIVAL_ROOT = '#ability/Survival%20Skills/situation-assessment'
ROUTES = ['#home', '#ability', '#about'] + ['#ability/' + c.replace(' ', '%20') for c in CATEGORIES]
ROUTES += ['#ability/Fiction/' + s for s in ['unreachable-sincerity', 'interference-of-fate-and-time', 'universe-no-99']]
ROUTES += ['#ability/Discipline/2022-08-2022-11']
ROUTES += ['#ability/Cognition/' + s for s in COGNITION]
ROUTES += [SURVIVAL_ROOT] + [SURVIVAL_ROOT + '/' + s for s in SURVIVAL]
ROUTES += ['#ability/Games/0', '#ability/Software/0']


def fixture():
    html = (ROOT / 'index.html').read_text()
    for asset, tag in [('experience.css', 'style'), ('experience.js', 'script')]:
        marker = f'<link rel="stylesheet" href="assets/{asset}">' if tag == 'style' else f'<script src="assets/{asset}"></script>'
        assert html.count(marker) == 1, f'Missing/duplicate asset: {asset}'
        html = html.replace(marker, f'<{tag}>' + (ROOT / 'assets' / asset).read_text() + f'</{tag}>')
    return html


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser')
    parser.add_argument('--output', default='test-results/experience.json')
    parser.add_argument('--screenshots', default='test-results/screenshots')
    args = parser.parse_args()
    output = Path(args.output); output.parent.mkdir(parents=True, exist_ok=True)
    shots = Path(args.screenshots); shots.mkdir(parents=True, exist_ok=True)
    result = {'environment': 'offline Chromium; original remote fonts/cover not loaded',
              'checks': [], 'failures': [], 'page_errors': [], 'screenshots': []}
    html = fixture()

    def check(name, condition, detail=None):
        result['checks'].append(name)
        if not name.startswith('layout '): print(name, condition, flush=True)
        if not condition: result['failures'].append({'check': name, 'detail': detail})

    with sync_playwright() as p:
        options = {'headless': True, 'args': ['--no-sandbox']}
        if args.browser: options['executable_path'] = args.browser
        browser = p.chromium.launch(**options)
        result['browser'] = browser.version

        def mount(width=1440, height=900, route='#home', state=None, reduced=False):
            page = browser.new_page(viewport={'width': width, 'height': height},
                                    has_touch=width <= 760,
                                    reduced_motion='reduce' if reduced else 'no-preference')
            page.set_default_timeout(6000)
            page.set_default_navigation_timeout(6000)
            page.route('**/*', lambda request: request.abort())
            page.on('pageerror', lambda error: result['page_errors'].append(str(error)))
            page.evaluate('([hash,state]) => history.replaceState(state,"",hash)', [route, state])
            page.set_content(html, wait_until='domcontentloaded')
            page.wait_for_timeout(80)
            return page

        def go(page, route):
            page.evaluate('(hash) => { location.hash = hash; }', route)
            page.wait_for_timeout(65)

        def shot(page, name):
            path = shots / (name + '.png')
            page.screenshot(path=str(path), full_page=True)
            result['screenshots'].append(str(path))

        # Every content route is rendered at each viewport, not just the homepage.
        widths = [320, 390, 540, 760, 768, 960, 1024, 1080, 1100, 1440, 1920]
        for width in widths:
            print('Viewport', width, flush=True)
            page = mount(width, 800)
            for route in ROUTES:
                if route != '#home': go(page, route)
                measures = page.evaluate('''() => {
                  const view = document.querySelector('.view.active');
                  const visible = e => e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden';
                  const bad = [...view.querySelectorAll('*')].filter(e => visible(e) && !e.closest('.skip-link'))
                    .filter(e => { const r = e.getBoundingClientRect(); return r.left < -1 || r.right > innerWidth + 1; })
                    .slice(0, 5).map(e => ({tag:e.tagName, class:e.className, text:e.textContent.slice(0,60)}));
                  return {active:document.querySelectorAll('.view.active').length, h1:view.querySelectorAll('h1').length,
                          width:document.documentElement.scrollWidth, viewport:innerWidth, bad};
                }''')
                check(f'layout {width} {route}', measures['active'] == 1 and measures['h1'] == 1
                      and measures['width'] <= width + 1 and not measures['bad'], measures)
            go(page, '#ability')
            names = page.locator('.view.active .category-title').all_text_contents()
            check(f'directory order {width}', names == CATEGORIES, names)
            check(f'no button navigation {width}', page.locator('.view.active button').count() == 0)
            if width in [320, 390, 1440]:
                shot(page, f'ability-{width}')
                go(page, '#home'); shot(page, f'home-{width}')
            if width == 960:
                go(page, '#ability/Software'); shot(page, 'software-960')
            page.close()

        # Actual entry -> detail -> parent, including focus and browser forward.
        print('Functional tests', flush=True)
        page = mount(390, 760)
        page.locator('.view.active .portal-card').first.tap(); page.wait_for_timeout(80)
        card = page.locator('.view.active .category').filter(has_text='Cognition')
        card.scroll_into_view_if_needed(); card.focus(); page.wait_for_timeout(40)
        expected_y = page.evaluate('scrollY'); expected_id = card.get_attribute('id')
        card.press('Enter'); page.wait_for_timeout(80)
        check('new page starts at top', page.evaluate('scrollY') == 0)
        check('new page focuses title', page.evaluate('document.activeElement.tagName') == 'H1')
        page.locator('.view.active .topbar .back-link').click(); page.wait_for_timeout(100)
        check('parent route', page.url.endswith('#ability'))
        check('parent restores scroll', abs(page.evaluate('scrollY') - expected_y) <= 2,
              {'expected': expected_y, 'actual': page.evaluate('scrollY')})
        check('parent restores focus', page.evaluate('document.activeElement.id') == expected_id)
        page.go_forward(wait_until='commit'); page.wait_for_timeout(100)
        check('browser forward', page.url.endswith('#ability/Cognition'))
        page.locator('.view.active .cognition-theme-card').filter(has_text='自我整合與幸福').click(); page.wait_for_timeout(100)
        check('deep breadcrumbs', page.locator('.view.active .breadcrumbs a').count() == 3)
        summary = page.locator('.view.active .toc-mobile summary')
        check('long-page mobile toc visible', summary.is_visible())
        summary.click()
        chapter = page.locator('.view.active .toc-mobile [data-chapter-link]').nth(1)
        target_id = chapter.get_attribute('data-chapter-link')
        chapter.click(); page.wait_for_timeout(700)
        check('toc collapses', not page.locator('.view.active .toc-mobile').get_attribute('open'))
        check('toc focuses heading', page.evaluate('document.activeElement.id') == target_id)
        check('toc bookmark', '?section=' + target_id in page.url)
        rect = page.locator('#' + target_id).bounding_box()
        bar = page.locator('.view.active .topbar').bounding_box()
        check('heading clears sticky bar', rect['y'] >= bar['height'] - 1, {'heading':rect,'bar':bar})
        check('sticky topbar', abs(bar['y']) <= 1, bar)
        shot(page, 'reading-mobile')
        page.evaluate('scrollTo(0,900)'); page.wait_for_timeout(240)
        state = page.evaluate('history.state'); reload_hash = page.evaluate('location.hash'); saved_y = page.evaluate('scrollY')
        reloaded = mount(390, 760, reload_hash, state)
        check('reload restores saved entry', abs(reloaded.evaluate('scrollY') - saved_y) <= 2)
        reloaded.close()
        page.locator('.view.active .page-return a').click(); page.wait_for_timeout(100)
        check('bottom return after chapter', page.url.endswith('#ability/Cognition'))
        page.close()

        # Fresh deep links, chapter links, invalid encodings, and narrow reflow.
        page = mount(1440, 800, '#ability/Cognition/self-integration')
        check('desktop toc visible', page.locator('.view.active .toc-rail').is_visible())
        check('desktop mobile toc hidden', not page.locator('.view.active .toc-mobile').is_visible())
        shot(page, 'reading-desktop')
        deep_link = page.locator('.view.active .toc-rail [data-chapter-link]').last.get_attribute('href')
        page.locator('.view.active .topbar .back-link').click(); page.wait_for_timeout(80)
        check('fresh deep-link parent fallback', page.url.endswith('#ability/Cognition') and page.evaluate('scrollY') == 0)
        page.close()
        page = mount(1440, 800, deep_link)
        check('fresh chapter deep-link focus', page.evaluate('document.activeElement.id') == deep_link.split('?section=')[1])
        page.set_viewport_size({'width': 720, 'height': 800}); page.wait_for_timeout(180)
        check('200 percent equivalent reflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
        check('resized toc collapsible', page.locator('.view.active .toc-mobile summary').is_visible())
        page.close()
        for route in ['#ability/%ZZ', '#ability/__proto__', '#ability/Fiction/not-a-work', '#ability/Software/-1']:
            page = mount(390, 760, route)
            check('invalid route handled ' + route, page.locator('.view.active h1').count() == 1)
            page.close()

        page = mount(1440, 800, '#ability/Software/0', reduced=True)
        check('short project no toc', page.locator('.view.active .toc-rail').count() == 0)
        check('external link retained', page.locator('#githubLink').get_attribute('target') == '_blank')
        go(page, '#home')
        link = page.locator('.view.active .portal-card').first
        link.focus(); page.keyboard.press('Tab')
        computed = page.evaluate('''() => {const s=getComputedStyle(document.activeElement); return {
          outline:s.outlineWidth, style:s.outlineStyle, transition:s.transitionDuration};}''')
        check('keyboard focus visible', computed['outline'] == '2px' and computed['style'] == 'solid', computed)
        check('reduced motion', computed['transition'] == '0s', computed)
        page.close()
        browser.close()

    check('no JavaScript page errors', not result['page_errors'], result['page_errors'])
    result['passed'] = len(result['checks']) - len(result['failures'])
    result['total'] = len(result['checks'])
    result['assets_sha256'] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in [ROOT/'index.html', ROOT/'assets/experience.css', ROOT/'assets/experience.js']}
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'passed': result['passed'], 'total':result['total'], 'failures':result['failures'],
                      'page_errors':result['page_errors'], 'report':str(output)}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['failures']))

if __name__ == '__main__': main()
