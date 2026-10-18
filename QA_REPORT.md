# Selara v1.2 quality-assurance report

## Scope

- Replaced seven illustrated scenes with seven **separately generated ChatGPT images**, converted to 14 original-resolution and mobile-sized WebP files.
- Removed the obsolete scene SVGs from the source; preserved the small brand SVG favicon.
- Updated stay cards, details dialog, editorial story, dynamic experience display, page metadata/asset ledger, and the photograph-backed closing section.
- Preserved fake-booking disclaimers, real favorites/filters/date-price estimation/export interactions.

## Locally verified

- `npm run check`: passed.
- `npm test`: all four calculation tests passed.
- `npm run build`: passed.
- `python tests/offline_browser_qa.py`: run after build to check Chromium at 1440px, 900px and 390px for image loading, no horizontal overflow, JavaScript runtime errors, filters, favorites, room modal, experience switch, price calculator, downloadable JSON summary, and mobile menu.

## Deployment and limitations

- Offline QA uses Chromium and the *real* local HTML/CSS/JS/assets embedded into an about:blank document because this environment's browser navigation is restricted. Screenshot scrolling is required to avoid offscreen image rasterization blanks.
- This does **not** verify HTTP caching, response security headers, or the live Cloudflare Worker. Verify the published commit and image responses after GitHub push.
- The site is a **fictional demo**: no live reservations, inventory, payments or real property. All room/rate representations are illustrative.
