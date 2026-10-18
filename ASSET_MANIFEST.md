# Selara original visual asset manifest · v1.1

All assets in `public/assets/` are part of the fictional, **non-operating** Selara hospitality showcase. No scraped guest or hotel photography, copied branding, fake testimonials or hidden image hotlinks.

## Individually authored production visuals

| Asset | Position / function | Origin | Descriptive alternative text |
|---|---|---|---|
| `coast-hero.webp` | Main full-bleed hero image | Original AI-generated cinematic concept art from initial site production, optimized to WebP; not a photograph of a real resort | AI-generated sunset island villa, palms and plunge pool |
| `slow-mornings.svg` | Editorial brand-story interlude | Independently authored vector illustration of island breakfast still-life; generated from `scripts/create_original_scenes.py` | Coffee, fruit and journal on wood table |
| `shore-villa.svg` | Shore room card and details dialog | Independently authored vector scene: beachfront villa and infinity pool | Shore Villa beside the water with plunge pool |
| `grove-suite.svg` | Grove room card and details dialog | Independently authored vector scene: palm-grove pavilion | Grove Suite nestled into tropical greenery |
| `horizon-residence.svg` | Horizon room card and details dialog | Independently authored vector scene: larger panoramic residence | Horizon Residence with sea-facing pool |
| `sunset-sail.svg` | Experience panel when Sunset selected | Independently authored vector scene: sunset yacht | Sailboat crossing the water at sunset |
| `forest-walk.svg` | Experience panel when Nature selected | Independently authored vector scene: rainforest walkway | Path under palms and rainforest canopy |
| `starlit-dining.svg` | Experience panel when Dinner selected | Independently authored vector scene: lantern-lit beach dining | Open-air dinner by the shore at night |
| `mark.svg` | Favicon | Original SVG logomark in existing v1.0 repository | Decorative |

## Visual direction

- **Art direction:** coastal editorial; mineral green, warm cream, sun-faded rose, gold, sea glass and pale teak.
- **Hero:** cinematic photographic AI concept, no text baked into image. **Supporting collection:** intentionally illustrated editorial/postcard scenes with shared palette and distinct geometry.
- **Sizes:** SVG scenery `1200 × 800` responsive/viewBox; photographic hero WebP `1672 × 941` optimized for visible first screen.
- **Loading:** Hero uses `fetchpriority=high`; below-fold scenes lazy load. SVGs remain crisp and text-free. No collage cut into assets; each scene is separately composed in the source generator.
- **Provenance honesty:** Vector scenes are code-authored SVGs, **not** text-to-image AI photographs. When the image-generation tool is not available, do not mislabel the generated illustrations as photorealistic AI images.

The old derivative `coast-card.webp` and generic placeholder vectors from v1.0 were retired in v1.1. Every new scene is intentionally linked to a visible UI section or working dialog. The resort, rates, inventory, experiences, and reservations are fictional.
