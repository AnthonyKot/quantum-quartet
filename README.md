# The Quantum Quartet

A comparative reading of early 20th-century theoretical physics through four books:

1. **Born** — *Atomic Physics* (Dover reprint 1969, 8th English ed.)
2. **Feynman** — *The Feynman Lectures on Physics*, Vols. I (1963) & III (1964)
3. **Landau & Lifshitz** — *Quantum Mechanics: Non-Relativistic Theory* (2nd ed. 1965)
4. **Dirac** — *The Principles of Quantum Mechanics* (4th ed. revised, 1958)

Exact editions and section pointers are listed on the site's About page.

## Structure

- `index.html` — Landing page with premise and chapter map
- `about.html` — Method page: editions, how chapters compare authors
- `chapters/NN-slug.html` — One page per chapter

Each chapter has:
1. A short framing intro
2. An "entry points" comparison table (how each author enters the topic)
3. A synthesis essay weaving the four treatments together
4. A "read the originals" box with chapter/section pointers

## Content policy

All prose is original synthesis. Direct quotes from the books are rare, short
(under ~15 words), and attributed. No passages, derivations, or figures are
reproduced verbatim.

## Local preview

No build step required. Open `index.html` in a browser:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve .

# PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`.

## Deploy to GitHub Pages

1. Push to the default branch (`main`)
2. Go to **Settings → Pages** in the repository
3. Under **Source**, select **Deploy from a branch**
4. Choose the `main` branch and the `/ (root)` folder
5. Save

Your site will be live at `https://<username>.github.io/<repo>/`.

## Tech stack

- Plain HTML + one shared CSS file + minimal vanilla JS
- KaTeX from CDN for math rendering (inline `$...$` and display `$$...$$`)
- Semantic HTML, mobile-readable
- Light/dark theme toggle (respects `prefers-color-scheme`, overridden via button)
- Print-friendly (hides navigation, resets colors)

## Status

Scaffold, shared CSS, landing page, and About page complete. Full 18-chapter
map wired in. Written so far: Part I (blackbody, photons, Bohr atom) and the
sample chapter "The Uncertainty Principle." Remaining chapters are listed on
the landing page and are being written against verified source editions.

Every "read the originals" pointer is verified against the actual text; any
not-yet-checked reference is visibly marked *unverified* on the page rather
than guessed.

Note: the source books are copyrighted and are **not** included in this repo.
The site links to freely available originals (e.g. the Feynman Lectures at
feynmanlectures.caltech.edu) but never hosts their text.
