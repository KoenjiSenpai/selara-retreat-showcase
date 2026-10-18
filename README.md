# Selara · An island to come back to yourself

**An original fictional boutique-retreat website prototype for the Gerbang Studio portfolio.** The coastal hero is independently AI-generated artwork. The room and experience illustrations are original SVG designs authored for this project. This is not an operating resort, and no transactions, real inventory, or reservations exist.

## Features

- Responsive editorial hospitality landing page with original art and mobile navigation
- Three imaginary room categories with accessible filters and saved favorites
- Experience switcher and explanatory visitor guide
- Date/guest selection and genuine client-side sample-cost calculation, with room-capacity checks
- Downloadable JSON sample itinerary and print-friendly itinerary
- Local-storage persistence and explicit reset
- Semantic structure, keyboard focus states, reduced-motion CSS, no outside analytics or fonts
- Robots headers intentionally block indexing of a nonreal accommodation property

## Run locally

Node.js 20+ for build/tests. No production dependency installation required for local static build.

```powershell
cd "$HOME\Downloads\selara-retreat"
npm run qa
python -m http.server 4173 -d dist
```

Visit http://localhost:4173/ . All paths work at the site root. No fake booking forms or transactional APIs are implied. For tests of browser behavior, install Playwright in an unrestricted machine and run `python tests/browser_qa.py` after changing its URL to the local server. This environment's Chromium could not open local files due to an administrator policy; browser screenshots are therefore *not* certified.

## Publish via Cloudflare Workers

Cloudflare Workers static assets: `wrangler.jsonc` includes `assets.directory: ./dist` and `name: selara-retreat-demo`. When GitHub is connected to a **new** Cloudflare Worker with the same name:

- Build: `npm run build`
- Deploy: `npx wrangler deploy`
- Production branch: `main`

Cloudflare Worker Git builds are distinct from Cloudflare Pages. Select the correct product and verify the Worker name exactly matches the Wrangler name. Keep this demo separate from existing Gerbang and Hushday deployments. Do not attach the real Gerbang domain.

Do **not** push this to an existing production repository. Request a separate private repo, e.g. `KoenjiSenpai/selara-retreat-showcase`, and connect it intentionally. Actual Cloudflare deployment needs the owner's account integration; no claim is made that remote deployment occurred.

## Data and privacy

The browser saves chosen favorites and sample trip fields locally with key `selara-showcase-v1`. The reset button clears those. Download exports only fictional itinerary fields. There is no checkout, server, lead collection or consent UI needed for this prototype. Do not submit actual sensitive data.

## QA status

`npm run qa` includes structural checks, four model tests and a build. It does **not** certify browser visual appearance, WCAG conformance, security penetration testing or performance budgets. Validate at 390, 768, 1280, 1440 px and on real Chrome, Firefox, Safari/Edge before showcasing as production-grade.
