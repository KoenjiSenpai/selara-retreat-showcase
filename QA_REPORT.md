# Selara QA — build 1.0.0

Automated checks: `npm run qa`: PASS (structural, 4 model tests, build). JavaScript syntax checks: PASS. Local HTML internal link integrity: PASS.

## Known limitations (do not conceal)

- Chromium page navigation was blocked with `net::ERR_BLOCKED_BY_ADMINISTRATOR` in this environment. **Real visual, responsive and end-to-end browser verification did not complete**. `tests/browser_qa.py` is provided for an unrestricted local/browser environment.
- Cloudflare deployment is not executed; GitHub repo not created/modified as part of this build.
- No inventory, backend, real booking, payments, contact collection or external APIs. The trip estimator is an explicitly fictional client-side simulation.
- The original hero photo has one AI generation; its room derivative is resized from the same source; three additional scenes are original SVG illustrations, not independent generated photos. Do not misrepresent these as independent AI-photo shoots.
- No live Lighthouse/axe score was recorded. Manual keyboard, screen reader, cross-browser and mobile testing remains necessary.
- The aesthetic/design direction is a first implementation, not a certified "flawless" release.

## Release verification checklist

- [ ] Desktop screenshots at 1280 and 1440 px, mobile at 390 px and tablet at 768 px
- [ ] No horizontal overflow; no clipped room copy or controls
- [ ] Filters show expected room categories; favorites persist on refresh
- [ ] Date boundary validation, checkout-after-checkin, 30-night limit, room guest capacities
- [ ] JSON export downloads actual current selections; print layout works
- [ ] Mobile navigation opens and closes, Escape works, accessible keyboard focus
- [ ] Images load, no broken routes or console errors
- [ ] Reduced motion works and contrast checked against WCAG 2.2 AA
- [ ] `build-version.json` reflects released source; verify actual Workers deployment SHA
- [ ] Live asset URLs return status 200 and correct MIME types
- [ ] Noindexed fictional property and clear demo disclaimer persist on production
