# Selara Retreat — Somewhere Between Tide & Time

**Gerbang Studio fictional hospitality concept**, version **1.1.0**. A richly illustrated, editorial coastal-retreat website for showcasing design, front-end engineering and real in-browser interactions. No real hotel, rooms, testimonials, payments, bookings or availability are represented.

## What's in the experience

- **Cinematic hero and visual storytelling** — one original AI-generated hero scene and seven separate original, code-authored SVG scenes (not cropped duplicates) across story, room cards, room details and experiences.
- **Three stays** — select All / For two / For family / Saved, tap ♡ to save locally, or explore a detailed accessible modal with amenities and an action that populates the trip planner.
- **Three illustrated experiences** — changing an experience also changes the visual and stores the selected experience for the trip summary.
- **Sample trip planner** — choose dates, room, guests and pace; get a *fictional* nightly-cost estimate; capacity checks reject 3–4 guests in two-person rooms; download a JSON summary or print it. Selected experience is included in downloads.
- **Visitor guide** — explains demo features and limitations. Favorites, trip choices, and selected experience persist only in local browser storage. Clear button resets preferences.
- **Accessibility and resilience** — semantic landmarks, skip link, proper image descriptions, native dialog, focus indicators, reduced-motion support, and responsive 1440/900/390 layouts. No trackers or third-party fonts, CDNs or API keys.

## How to use the site

1. Browse the hero and editorial story. The retreat is entirely fictional.
2. In **Find your sanctuary**, use the category chips, tap ♡ to save, and select **Saved stays** to see only favorites. **Explore stay** opens amenities; the arrow selects that room for the sample trip.
3. In **Experiences**, switch between a sunset sail, nature walk, or beach dining. The scene and description change immediately, and your choice becomes part of the sample itinerary.
4. In **Dream up your little escape**, choose an arrival and departure, guests and pace. The total reflects the nightly room price times the number of nights (fictional). Export the JSON or use Print. No reservation or charge occurs.
5. Use **Clear my saved demo preferences** near the visitor guide to reset locally stored choices.

## Run and verify

Requires Node.js 20+. No production runtime dependencies; all static assets are committed.

```powershell
cd "$HOME\Downloads\selara-retreat"
npm run qa
python -m http.server 4173 -d dist
```

On an unrestricted machine browse `http://localhost:4173/`. Browser testing is in `tests/browser_qa.py`. When local navigation is blocked by an administrator policy, `tests/offline_browser_qa.py` uses Playwright `page.set_content` with the actual HTML/CSS/scripts and embedded assets, and checks three screen widths and interactions (requires `playwright`, `beautifulsoup4` Python modules and Chromium).

## Cloudflare Worker Git integration

Existing deployment configuration is retained in `wrangler.jsonc`:

- Worker: `selara-retreat-demo`
- Static assets directory: `./dist`
- Build command: `npm run build`
- Deploy command: `npx wrangler deploy`
- Production branch: `main` when connected to the repository

**Important:** pushing to GitHub triggers Cloudflare only if this Worker is configured with the right repository and auto-deploy for `main`. Verify the new commit in Cloudflare Deployments, check assets and interactive functionality at the actual Workers URL and hard-refresh if needed. GitHub Actions QA is not evidence that Workers deployed the update.

## Files and provenance

- `public/` — complete website; page, CSS, client-side model, UI and original art assets.
- `scripts/create_original_scenes.py` — reproducible independent SVG scenes. Does not require image API or third-party art.
- `scripts/build.mjs` — copy static files to `dist`, write build metadata.
- `scripts/check.mjs` — asset and structure checks.
- `tests/` — domain math tests, offline Chromium interaction & viewport tests.
- `ASSET_MANIFEST.md` — exact visual inventory and production methods.
- `QA_REPORT.md` — evidence, passes, and limits.

## Privacy and limitations

Browser storage uses the `selara-showcase-v1` key (compatible with v1.0 data). No real guests are contacted, no server stores preferences, and no payment is processed. JSON downloads are itinerary demonstrations, **not** booking confirmations. This is a portfolio demo with fictional descriptions and illustrative RM prices. The intentionally non-indexed site should not be presented as an operating property.
