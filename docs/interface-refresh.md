# Portfolio interface refresh — 2026-09-09

## Scope

Implements the approved navigation, reading-density, and visual-refinement work.
The deep-purple background, warm text, serif headings, existing editorial text,
artwork reference, external destinations, and original route names are retained.
There is no framework, new build step, analytics, or content-fetch dependency.

`index.html` keeps the original data and renderers. Its changes are limited to
loading `assets/experience.css` and `assets/experience.js`, allowing a section
query inside the existing hash, and delegating navigation initialization to the
new layer. Removing those four integration changes reproduces the original
Git blob `e5292c55fa8e3e9ed48ea1e9099539667ea3968b` byte for byte.

## Implemented behavior

- Slim sticky brand/parent navigation, deep-page breadcrumbs, keyboard skip link,
  and return-to-collection links at the end of detail pages. New destinations
  start at their heading; returning restores the previous scroll and focus.
  Browser back/forward and saved-entry reloads retain their history semantics.
  A directly opened detail page has an explicit parent fallback.
- Long articles with at least two published sections get a desktop chapter rail
  or a collapsible mobile/tablet table of contents. Chapter links focus the actual
  heading, clear the sticky header, and are bookmarkable without adding a
  history entry for every section click. Short project pages have no chapter UI.
- Navigation cards are real anchors, preserving copy-link/open-in-new-tab
  behavior. Arrows indicate entry; empty categories have a textual state rather
  than appearing disabled. Unpublished fiction regions are explicitly labeled.
- Ability is a single row-major directory. The previous desktop row order is
  retained on desktop, mobile, and keyboard traversal. Project dates/statuses
  wrap in a metadata row rather than forcing four minimum-width columns.
- Restrained one-pixel borders, unboxed information rows, shared spacing,
  bounded reading width, readable bilingual paragraphs, explicit keyboard
  focus, touch feedback, and reduced-motion/forced-color adaptations.

## Regression validation

Run from the repository root:

```sh
python -m pip install playwright
python -m playwright install chromium
python tests/experience_smoke.py
```

A system Chromium may be selected with `--browser /usr/bin/chromium`. Reports
and screenshots default to `test-results/`, which is ignored by Git. The test
fixture inlines the exact local CSS/JavaScript in a blank document and aborts
network requests. It does not require a web server or change browser policies.

Validated with Chromium **144.0.7559.96**: **404 / 404 checks passed**, including
**352 route/viewport combinations** (32 routes at 11 widths: 320, 390, 540, 760,
768, 960, 1024, 1080, 1100, 1440, and 1920 CSS pixels). No JavaScript page errors
were recorded. Other checks cover consistent directory order, real anchors,
new-page focus, parent scroll/focus restoration, browser forward, breadcrumbs,
mobile chapter collapse/focus/bookmarks, sticky-header clearance, saved-entry
reloads, direct deep links, malformed routes, external link semantics, and
reduced motion. A 720px reflow check approximates the layout width of a 1440px
window at 200% zoom; it is not a claim of native browser-zoom testing.

### Validation boundary

This is an offline Chromium rendering/interaction run, not a live deployment
or cross-browser certification. The remote Google Fonts and existing cover
image were not loaded in this environment. Fallback fonts and reserved image
geometry were tested instead. Live HTTP asset delivery, production font
rendering, Safari/Firefox, physical-device touch, and screen-reader output
remain separate acceptance checks. Passing these tests does not claim full
WCAG conformance or successful GitHub Pages publication.
