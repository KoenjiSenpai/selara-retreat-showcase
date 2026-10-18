# Selara Retreat v1.1 — build and interaction QA

## What changed

- Seven original vector illustrations composed individually with dedicated layouts, plus existing cinematic original AI-generated hero art.
- Each stay now has its own illustrated image and a native details dialog with specific amenities; removed generic placeholder imagery and a cropped hero derivative.
- Saved stays now have a real filter, empty state and clear counters rather than only a toast.
- Experience controls change the visible image, descriptive copy, chosen-experience summary and exported JSON itinerary.
- New illustrated brand-story interlude, adjusted card hierarchy, mobile layout, section captioning and native dialog styles.

## Testing evidence

- `npm run qa`: structural checks, unit tests, and full static build — passing in this environment.
- `tests/offline_browser_qa.py`: Chromium running in a restricted environment with `page.set_content`, the actual HTML/CSS/client JS embedded locally and true image bytes, testing **1440×900, 900×900, 390×844**. Checks no horizontal scrolling or uncaught JS errors; all referenced images load. Verified saved filter, modal, illustrated experience switching, room selection, local price calculation, JSON download with experience, and mobile menu.
- Visual screenshot review: `qa-screenshots/selara-1440.png`, `selara-900.png`, `selara-390.png` generated locally. They are screenshots of the offline embedded application, **not** captures of the remotely deployed Workers URL.
- Web references: official Cloudflare Workers static-asset documentation confirms `wrangler.jsonc` asset directory approach. Reference hospitality brand is The Datai Langkawi; no images, copy, assets or trademarks were copied.

## Residual risks

- **Production not yet independently validated** after pushing; check actual Workers deployment status and asset 200 responses (SVG/WebP), test production flows and browser console.
- No automated Lighthouse, axe/WCAG conformance audit, Safari/iOS or Firefox/Android native testing in this environment; do not call the website visually flawless or 100% accessible.
- For a real hotel, additional work would be required for legally approved photographs, authenticated availability, customer data handling, backend reservations, terms, payments, email, accessibility and SEO.
- This demo intentionally has no server, no actual inventory, and no external submission system. Fictional concept disclaimers remain visible.
