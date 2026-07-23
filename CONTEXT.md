# The Quantum Quartet — Project Context

## Premise

Comparative reading of early 20th-century theoretical physics through four books:

1. **Born** — *Atomic Physics* (Dover reprint 1969, 8th English ed.)
2. **Feynman** — *The Feynman Lectures on Physics*, Vols. I (1963) & III (1964), Caltech
3. **Landau & Lifshitz** — *Quantum Mechanics: Non-Relativistic Theory* (2nd ed. 1965, Pergamon)
4. **Dirac** — *The Principles of Quantum Mechanics* (4th ed., revised, 1958, Clarendon)

Each chapter pairs the four authors on a single topic and asks how each one enters the material. No rankings — read the differences productively.

## Style

- Typography-forward, restrained
- Serif body (Georgia/Times), sans-serif headings
- Light/dark theme toggle (respects `prefers-color-scheme`)
- Print-friendly
- Semantic HTML, mobile-readable

## Tech Stack

- Plain HTML + one shared CSS (`static/style.css`) + minimal vanilla JS (theme toggle only)
- No framework, no build step
- KaTeX from CDN: inline `$...$` and display `$$...$$`
- Relative links only (works under project subpath)
- Deploys to GitHub Pages from repo root

## Files Created

```
README.md                  — build instructions, GH Pages setup
index.html                 — landing page, full 18-chapter map
about.html                 — method, editions, content policy, verification rule
static/style.css           — typography, dark mode, print styles
chapters/01-blackbody-planck.html  — Part I, Chapter I
chapters/02-photons.html               — Part I, Chapter II
chapters/03-bohr-atom.html             — Part I, Chapter III
chapters/07-uncertainty.html           — sample chapter (Part II, VII)
books/                         — local PDFs
  Dirac-Principles of Quantum Mechanics.pdf
  Shankar - Principles of quantum mechanics.pdf
  born.pdf
```

## Chapter Map (14 core + 4 appendix)

### PART I — THE CRISIS (1900–1913)
- **01** / blackbody-planck — Blackbody Radiation and Planck's Quantum
  - Lead: Born. Feynman/Dirac/L&L near-absent.
- **02** / photons — Photons: Photoelectric Effect and Compton Scattering
  - Lead: Born; Feynman counterpoint.
- **03** / bohr-atom — The Bohr Atom and the Old Quantum Theory
  - Lead: Born. Feynman/L&L/Dirac skip it — "scaffold, not building."

### PART II — THE NEW MECHANICS (1925–1930)
- **04** / quantum-behavior — Quantum Behavior: The Double Slit and Amplitudes
  - Lead: Feynman.
- **05** / two-mechanics — Two Mechanics: Matrices vs. Waves
  - Lead: Born (participant) + Dirac (transformation theory proof).
- **06** / wavefunction — The Wavefunction and Schrödinger's Equation
  - Lead: Landau; Born = statistical interpretation.
- **07** / uncertainty — The Uncertainty Principle ← WRITTEN
  - L&L: electron diffraction + classical apparatus; Feynman: double slit; Born: wave packets; Dirac: non-commuting observables.
- **08** / dirac-formalism — States, Observables, Bras and Kets
  - Lead: Dirac. Other three = translation layer.

### PART III — THE PHYSICS
- **09** / wells-tunneling — Wells, Barriers, and Tunneling (Lead: Landau)
- **10** / hydrogen — The Hydrogen Atom (Lead: Landau; Born: historical)
- **11** / spin — Spin (Co-lead: Feynman vs. Dirac — sharpest style contrast)
- **12** / identical-particles — Identical Particles and the Periodic Table
- **13** / approximations — Approximation Methods (Lead: Landau)
- **14** / measurement — Measurement and What It All Means (Lead: Feynman; L&L silence is the 4th data point)

### APPENDIX — RELATIVITY
- **A1** / special-relativity — Spacetime and Lorentz Transformations (Lead: Einstein 1916)
- **A2** / mass-energy — Mass, Energy, Relativistic Dynamics (Lead: Einstein 1916)
- **A3** / general-relativity — General Relativity, Sketched (Lead: Einstein 1916)
- **A4** / dirac-equation — Where the Threads Meet: The Dirac Equation (Lead: Dirac)

## Content Policy

All prose is original synthesis. Direct quotes rare, short (<15 words), attributed. No reproducing passages, derivations, or figures. Feynman linked to feynmanlectures.caltech.edu (never mirrored — read-online license).

## Verification Rule

No "read the originals" pointer ships unverified. Unverified references get flagged or cut — never guessed.

## Source inventory (actual)

- **Born, *Atomic Physics*** — genuine EPUB, Dover 1969 reprint of 8th English ed.
  (ISBN 9780486318585). Full text extracted to
  `books/born-atomic-physics-dover1969/full-text.txt`. VERIFIED.
- **Born, *The Mechanics of the Atom*** (1927, G. Bell & Sons) — a DIFFERENT,
  earlier Born book (old quantum theory). Pasted at `born.txt`. Usable only as a
  labeled supplementary source for ch.03; NOT *Atomic Physics*.
- **Dirac** — `books/Dirac-Principles of Quantum Mechanics.pdf` is the **4th ed.
  (1958)**, readable via the Read tool (renders PDF pages as images). VERIFIED.
- **Landau & Lifshitz** — `/mnt/c/Users/CoderA/Downloads/LandauLifshitz-QuantumMechanics.pdf`,
  2nd ed. 1965 Pergamon (Sykes & Bell). Read via Read tool. VERIFIED.
- **Feynman** — link-only (read-online license, never mirrored). Vol. III pointers
  verified from the official Caltech ToC by the user. Vol. I pointers (ch.01/02)
  still pending.
- Deleted: fake `books/born.pdf` (SEO spam), irrelevant `books/Shankar-*.pdf` (1994).

### Tooling note
The Read tool renders PDF pages as images and reads them directly — the earlier
"encoding prevents extraction" claim was a *wrong-file* problem, not a real
limitation. No poppler/tesseract pipeline is required.

## Verification ledger (single source of truth for mark-or-cut)

| Source | Status | Notes |
|---|---|---|
| Born *Atomic Physics* (Dover 1969) | ✓ verified | ToC + uncertainty treatment read directly |
| Dirac (4th ed. 1958) | ✓ verified | full ToC read; uncertainty = Ch. IV §24 |
| L&L (2nd ed. 1965) | ✓ verified | Ch. I §1–§5 read directly |
| Feynman Vol. III | ✓ verified | user-supplied from Caltech ToC |
| Feynman Vol. I | ✗ pending | ch.01 blackbody, ch.02 photons — marked `.unverified` |

Key verified facts:
- Born does NOT open with blackbody (Ch. VII) or wave packets. Uncertainty =
  **Ch. IV §7** (single-slit diffraction primary, γ-ray microscope second, wave
  packets third; rigorous proof in Appendix XII).
- L&L §1 "uncertainty principle" opens with electron diffraction + classical
  apparatus and contains NO inequality; the inequality follows later from §§3–4.
- Dirac uncertainty = **Ch. IV §24 "Heisenberg's Principle of Uncertainty"** (his
  book opens with photon polarization/interference, not non-commuting observables).
- Feynman uncertainty = Vol. III §1-8 and §2-2; Schrödinger eq. not until Ch. 16.

### Verified Feynman Vol. III pointers (authoritative — use verbatim when writing)
Link pattern: `https://www.feynmanlectures.caltech.edu/III_NN.html`. Link-only,
never mirrored. Applied already to ch.07. The rest are for UNWRITTEN chapters —
use these exact pointers, do not re-derive:
- **ch.04** double-slit/amplitudes: Vol. III **Ch. 1 "Quantum Behavior" (§1-1..1-8)**,
  into **Ch. 2** and **Ch. 3 "Probability Amplitudes"**.
- **ch.06** Schrödinger: Vol. III **Ch. 16 "The Dependence of Amplitudes on Position"**.
  → COMPARISON CELL: Feynman derives Schrödinger's eq. 16 chapters in, vs. Landau
  who opens with it. Put this contrast in the table, not just the pointer.
- **ch.07** uncertainty [WRITTEN]: Vol. III **§1-8** + **§2-2**. ✓ applied.
- **ch.08** formalism: Vol. III **Ch. 3**, **Ch. 8 "The Hamiltonian Matrix"**,
  **Ch. 20 "Operators"**.
- **ch.10** hydrogen: Vol. III **Ch. 19 "The Hydrogen Atom and the Periodic Table"**.
- **ch.11** spin: Vol. III **Ch. 5 "Spin One"**, **Ch. 6 "Spin One-Half"** (§5-1
  confirms the Stern-Gerlach-first premise).
- **ch.12** identical particles: Vol. III **Ch. 4 "Identical Particles"** (+ Ch. 19
  for the periodic-table payoff).
- **ch.14** measurement: Vol. III **§1-6 "Watching the electrons"** + **§2-6
  "Philosophical implications"**.
- **ch.01** blackbody & **ch.02** photons: CONFIRMED ABSENT from Vol. III →
  Vol. I (section numbers still pending; marked `.unverified` in-page).

### Edition pinning (final)
- Born: **Dover 1969, 8th ed.** (expanded — mesons, Mössbauer, neutron scattering)
- Feynman: 1963 (Vol. I) / 1964 (Vol. III) Caltech — link-only, caltech.edu
- L&L: 2nd ed. 1965 Pergamon, tr. Sykes & Bell
- Dirac: 4th ed. revised 1958, Clarendon
- Einstein, *The Meaning of Relativity*, 4th ed. 1950 Princeton — Appendix A–C

### Remaining TODO
- Feynman Vol. I ToC → verify ch.01 blackbody & ch.02 photons section numbers,
  then drop the two `.unverified` marks.
- Write chapters 04–06, 08–14 and appendix A1–A4.

## Writing Notes

### L&L distinctive features
- Opens with electron diffraction, not commutators
- Measurement by classical apparatus as entry point
- "Contains classical mechanics as limiting case yet needs it for its own formulation"
- Mathematical rigor over historical narrative
- No discussion of interpretation — establish formalism, derive consequences

### Born distinctive features
- Participant historian — witnessed Planck/Einstein debate, helped Heisenberg
- Generous, patient, historically grounded
- Emphasizes correspondence principle
- More cautious about radical ideas than later authors

### Feynman distinctive features
- Informal, vivid, pedagogical
- Double-slit as the one irreducible mystery
- Does not treat old quantum theory seriously
- Prefers correct theory over historical detours

### Dirac distinctive features
- Austere, logical, terse
- Mathematics IS the physics
- Derives from first principles
- Non-commuting observables as primitive

## Chapter Template

1. Short framing intro (what problem this chapter answers)
2. "Entry points" comparison table (4 rows × 4 cols: experiment/axiom/calculation/thought experiment)
3. Synthesis essay (~1200-2000 words)
4. "Read the originals" box (verified section pointers)
5. Prev/next nav

## Next Steps

1. Wire full map into index.html ✓
2. Update about.html with pinned editions ✓
3. Write Part I (01–03) ✓
4. Write Part II (04–08) — need Feynman OCR + Born OCR
5. Write Part III (09–14) — need targeted Born OCR
6. Write Appendix (A–D) — need Einstein 1916 text
7. Final verification pass on all "read the originals" pointers
