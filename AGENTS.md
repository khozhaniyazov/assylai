# Assyl AI Landing Page - Project Context

## What is this?
A static HTML landing page for **Assyl AI** — a children's speech therapy and development center in Aktau, Kazakhstan. Content is in Kazakh language.

**Live URL:** https://khozhaniyazov.github.io/assylai/
**Repo:** https://github.com/khozhaniyazov/assylai
**Stack:** Single `index.html`, Tailwind CSS (CDN v3.4.1), Lucide Icons (CDN v0.263.0), Google Fonts (Montserrat + Inter), vanilla JS.

## Hosting
- **Migrated from Netlify to GitHub Pages** (Netlify hit bandwidth limits after 3 days).
- Deployed via GitHub Actions workflow at `.github/workflows/deploy.yml`.
- GitHub Pages enabled with `build_type: workflow`.
- `.nojekyll` file present for proper static serving.

## What was done

### Hosting Migration
- Removed Netlify config (`.netlify/`, `.github/workflows/netlify.yml`).
- Created GitHub Pages deploy workflow (`.github/workflows/deploy.yml`).
- Renamed repo from `assyl-ai-landing` to `assylai`.
- Enabled GitHub Pages via `gh api`.

### Bug Fixes
- **Form submission** — was permanently disabling the submit button after first use. Now resets after 4s.
- **FAQ section placement** — was after the footer. Moved before the CTA form section (correct flow: FAQ → Form).
- **Facebook Pixel** — placeholder `YOUR_PIXEL_ID` was making failed requests. Commented out until real ID is provided.
- **Lucide icons version** — pinned to `0.263.0` (typo `0.263.1` caused 404, all icons disappeared).
- **animation-delay-2000** — CSS class was used in HTML but never defined. Added to `<style>` block.
- **Combo discount logic** — was applying first matching combo, not the best one. Fixed to find lowest price across all matching combos.

### SEO Improvements
- Fixed `<html lang="ru">` to `lang="kk"` (Kazakh).
- Added Open Graph meta tags (og:title, og:description, og:image, og:locale).
- Added Twitter Card meta tags.
- Added `<link rel="canonical">`.
- Added `<meta name="theme-color">`.
- Added JSON-LD structured data (`MedicalBusiness` schema with address, phone, hours, Instagram).

### Performance
- Pinned Tailwind CSS CDN to v3.4.1 (was unpinned `@latest`).
- Pinned Lucide Icons to v0.263.0 (was unpinned `@latest`).
- Added `<link rel="preload">` for Google Fonts.

### Accessibility
- Fixed image alt text from Russian to Kazakh.
- Added `inputmode="tel"` and `pattern` to phone input.

### UX
- Added phone number validation (strips non-digits, checks 10-13 length).
- Added popup blocker fallback for WhatsApp redirect.
- Updated testimonial names to proper Kazakh names (Әсем Қ., Гүлнар Б., Мәдина С.).

### Cleanup
- Removed unused files from git: `specialist.png`, `reorder.py`, `frontend-brief.md`.
- Added `.nojekyll` for GitHub Pages.

## MCP Servers Configured (opencode.json)
- **context7** — search documentation (Tailwind, etc.)
- **gh_grep** — search code examples from GitHub

## Known Issues / TODO
- Facebook Pixel is commented out — needs real Pixel ID when ready.
- No backend for form data — leads only go through WhatsApp redirect.
- Using Tailwind CDN runtime compiler (not ideal for production, but acceptable for a single-page static site without a build step).
- No 404 page configured.
- Images (hero.png, specialist.jpg) are not optimized/compressed — could benefit from WebP conversion.

## Key Files
| File | Purpose |
|---|---|
| `index.html` | Entire landing page (~750 lines) |
| `hero.png` | Hero section image |
| `specialist.jpg` | Specialist portrait |
| `.github/workflows/deploy.yml` | GitHub Pages CI/CD |
| `opencode.json` | MCP server config |
| `.nojekyll` | GitHub Pages config |
