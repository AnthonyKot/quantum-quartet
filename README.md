# The Quantum Quartet

A readable guide to the basics of quantum mechanics, written as a connected sequence of essays for
an adult returning to physics: university mathematics some years ago, no previous quantum mechanics.
Each essay answers one concrete question with enough mathematics to answer it, restores the tools it
uses in short reminders, works one example with real numbers, puts longer derivations in optional
fold-outs, and ends with two worked questions.

The site began as a comparison of four textbooks (Born, Feynman, Landau & Lifshitz, Dirac). That
comparison is no longer the organising principle; the books appear only as checked "Further reading"
notes. Editions are listed on the About page.

## Status

- **Core sequence, 16 essays: rewritten** (September 2026), in the reading order shown on the landing
  page. Reading order differs from file numbering in a few places, deliberately:
  01 → 02 → 03 → 04 → 05 → 06 → 08 → 07 → 09 → 09b → 09c → 10 → 11 → 12 → 13 → 14.
- **Optional relativity essays, a1–a4: awaiting revision.** Still in the earlier comparative format.
- Plan, reader model and acceptance criteria: `notes/REWORK-PLAN.md`.
  Source verification levels: `notes/source-ledger.md`.

## Structure

- `index.html` — landing page: who it is for, how the essays work, map by question
- `about.html` — what the project is, editions, content policy, verification
- `chapters/*.html` — one essay per page; file names are stable URLs
- `scripts/chNN_*.py` — the numbers and generated figures for each essay (standard library only).
  `python3 scripts/ch01_blackbody.py` prints the checked numbers; `--write` regenerates the figure
  between the `FIGURE:` markers in the chapter.
- `scripts/check_page.py <chapter>` — banned phrases, KaTeX errors, equation and page overflow at
  desktop and phone width, figure label size, and that every fold-out reaches a printed PDF
  (needs a headless Chromium and `pdftotext`).

## Content policy

All prose, worked examples and figures are original. Quotations from the books are rare, short and
attributed; their derivations and figures are not reproduced. The Feynman Lectures are linked at
feynmanlectures.caltech.edu, never mirrored. The source books are copyrighted and are not in this repo.

## Local preview

No build step. From the repository root:

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000`.

## Deploy to GitHub Pages

Settings → Pages → Deploy from a branch → `main`, `/ (root)`.

## Tech stack

Plain HTML, one shared CSS file (`static/style.css`), minimal vanilla JS (theme toggle; fold-outs
open when printing), KaTeX from CDN. Light/dark theme, mobile-readable, print-friendly.
