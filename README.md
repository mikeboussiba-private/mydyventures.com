# mydyventures.com

Corporate website of **MYDY VENTURES LTD** (mydy Ventures), the publisher of ToothPal and BabyBloomy. It is the organization website used for Apple Developer and Google Play verification.

Live at **https://mydyventures.com**, served by GitHub Pages from the root of `main`.

## Pages

| Path | What it is |
|---|---|
| `/` | Home: hero, apps, about, contact |
| `/privacy.html` | Privacy Policy (DRAFT, pending legal review) |
| `/terms.html` | Terms of Use (DRAFT, pending legal review) |
| `/404.html` | Not-found page (served by GitHub Pages, `noindex`) |

Plain static HTML with inline CSS and a little inline JS. No build step, no frameworks, no external scripts, no web fonts, no cookies, no analytics.

## Run locally

```bash
python3 -m http.server 8150
```

Open http://localhost:8150. Use HTTP, not `file://`: links are root-absolute.

## Rules

- The design, copy and legal drafts are Dean's v1 handoff (10 Oct 2026). Change them with Dean.
- These strings must match official records and must not be edited without both founders agreeing: legal name `MYDY VENTURES LTD`, email `support@mydyventures.com`, the one-line description, and the footer.
- House style: single hyphen `-`, no em or en dashes.
- Keep the DRAFT banners on the legal pages until counsel signs off.

## SEO and icons

- `<link rel="canonical">`, Open Graph, Twitter card and JSON-LD `Organization` on the indexable pages.
- `robots.txt` and `sitemap.xml`. Update `<lastmod>` when a page's content changes.
- Icons: `favicon.ico` (16/32/48), `favicon-96.png` and `icon-192.png` (Google Search uses sizes that are multiples of 48), `apple-touch-icon.png` (180), and `icon-512.png` via `site.webmanifest`. `favicon.png` (64) is kept for old links.

## Deploy

Pushing to `main` deploys. `CNAME` holds the custom domain; `.nojekyll` turns off Jekyll processing.

## After deploying

`python3 tools/indexnow.py .` pings Bing/Yandex (IndexNow) with every sitemap URL, once GitHub Pages has published. Google reads `sitemap.xml` via Search Console instead.
