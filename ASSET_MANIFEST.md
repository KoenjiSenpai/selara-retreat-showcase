# Selara photography asset manifest · v1.2

The site is an original **fictional** resort concept, not a real property, and all imagery represents imagined accommodations and experiences. No images were scraped from hotel listings. Seven new **individually generated ChatGPT images** replace the former vector illustrations. Each was separately generated as 1448 × 1086 PNG, converted to WebP and given a responsive 760px derivative.

| Section | Production asset | Original GPT-generated PNG |
|---|---|---|
| Shore Villa | `public/assets/shore-villa.webp` + `shore-villa-sm.webp` | `tropical_villa_at_golden_hour_sunset.png` |
| Grove Suite | `public/assets/grove-suite.webp` + `grove-suite-sm.webp` | `golden_hour_tropical_villa_retreat.png` |
| Horizon Residence | `public/assets/horizon-residence.webp` + `horizon-residence-sm.webp` | `golden_sunset_island_retreat.png` |
| Sunset Sail | `public/assets/sunset-sail.webp` + `sunset-sail-sm.webp` | `golden_hour_catamaran_escape.png` |
| Forest Walk | `public/assets/forest-walk.webp` + `forest-walk-sm.webp` | `golden_jungle_boardwalk_vista.png` |
| Starlit Dining | `public/assets/starlit-dining.webp` + `starlit-dining-sm.webp` | `candlelit_tropical_seaside_dinner.png` |
| Slow Mornings | `public/assets/slow-mornings.webp` + `slow-mornings-sm.webp` | `golden_hour_tropical_breakfast_by_the_sea.png` |

The original cinematic `coast-hero.webp` from the first Selara build remains in the full-bleed homepage hero. The final call-to-action intentionally reuses the existing Sunset Sail image as a background; this is an intentional decorative reuse, not a separate generated original. `mark.svg` is retained only as the brand favicon. No room or experience uses an SVG illustration.

## Implementation and quality rules

- Each card, editorial interlude, dynamic experience panel and details dialog references a genuine WebP image in the repository.
- Images display with `object-fit: cover`; card and editorial illustrations use responsive `srcset`, below-fold loading is lazy, the homepage hero loads eagerly.
- Visitors are explicitly told all property images, prices and experiences are fictional concept content.
- GitHub tree and production build must contain actual binary WebP files. Do not claim visual QA until a browser test has shown every image with a nonzero natural width.
- Copy, logos and icons are HTML/CSS or the tiny SVG brand mark; these are not presented as generated photographic artwork.
