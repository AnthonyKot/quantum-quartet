# Source ledger for the rewritten core (16 essays)

Status 2026-09-18. Every "Further reading" pointer in the rewritten chapters, with what
was actually checked. Two levels, which establish different things:

- **Location** — the section number and title were confirmed against a table of contents
  or the section headings of the source (so the pointer leads to the right place), but the
  passage itself was not read against the claim the essay attaches to it.
- **Passage** — the supporting text itself was read and matches what the essay says about it.

Sources on disk: Born, *Atomic Physics* (Dover 1969), full text at
`books/born-atomic-physics-dover1969/full-text.txt`. Dirac, *Principles* (4th ed.) PDF in
`books/` (contents = PDF pages 9–10). Landau & Lifshitz (2nd ed. 1965) PDF at
`~/book2/sources/LandauLifshitz-QuantumMechanics.pdf` (contents = PDF pages 7–8). Feynman
chapters saved as text in `sources/feyman*.txt` (file numbers do not match chapter numbers;
first line of each file gives the chapter). Feynman is linked, never mirrored.

| Essay | Pointer | Level | Checked against |
|---|---|---|---|
| Blackbody | Born VII §1 "Heat Radiation and Planck's Law" | Passage | full text: displacement law, Rayleigh–Jeans, Planck, 0.2014 hc/k, 0.290 cm K |
| Blackbody | Feynman I Ch. 41 §41-2, §41-3 | Passage | `feyman26.txt` headings and §41-3 text on Planck's oscillator |
| Photons | Born IV §2 "Light Quanta", §4 "Compton Effect", App. X | Passage | full text: photoelectric laws, "hail of shot", Meyer–Gerlach, Compton recoil, Bothe–Geiger |
| Photons | Feynman I Ch. 34 §34-9 "The momentum of light" | Location | `feyman23.txt` heading |
| Bohr | Born IV §2–§3, V §1 | Passage | full text: classical atom's failure, Bohr's hypothesis, Balmer 1885, correspondence principle |
| Double slit | Feynman III Ch. 1 §1-2…§1-6, Ch. 3 §3-1, §3-2 | Location (+ one passage) | `feyman1.txt`, `feyman3.txt` headings; §3-2 "never add amplitudes for distinct final states" read |
| Double slit | Dirac Ch. I §4–§5 | Location | Dirac contents page |
| Double slit | L&L §2 | Location | L&L contents page |
| Representations | Dirac Ch. I §2, §4; Ch. III | Location | Dirac contents page |
| Representations | Feynman III Ch. 8 §8-1…§8-3 | Location | `feyman5.txt` headings |
| Representations | Born V §3, §4, §8 ("two forms of the same content") | Passage | full text, §8 |
| Wavefunction | Feynman III Ch. 16 §16-2, §16-5 | Location | `feyman16.txt` headings |
| Wavefunction | L&L §10, §17 | Location | L&L contents page |
| Wavefunction | Born V §4, §7 | Location | Born contents |
| Formalism | Dirac Ch. I §6, Ch. II §7–§10 | Location | Dirac contents page |
| Formalism | Feynman III Ch. 8 §8-5, §8-6 | Location | `feyman5.txt` headings |
| Formalism | L&L §3, §11 | Location | L&L contents page |
| Uncertainty | Feynman III §1-8, Ch. 2 §2-2, §2-4 | Location | `feyman1.txt`, `feyman2.txt` headings |
| Uncertainty | Born IV §7 + App. XII | Passage (earlier session) | CONTEXT.md verification ledger |
| Uncertainty | L&L §16; Dirac IV §24 | Location | contents pages |
| Confinement | Born X §1 "The Size of the Nucleus and α-Decay" | Passage | full text: Gamow, Condon–Gurney 1928, Geiger–Nuttall 1911, glass air-gap analogy |
| Confinement | L&L §22, §25, §50 | Location | L&L contents page |
| Confinement | Feynman III §16-6 | Location | `feyman16.txt` heading |
| Oscillator | L&L §23; Dirac VI §34 | Location | contents pages |
| Oscillator | Born V §4 + App. XVI | Passage | full text: oscillator solution referred to App. XVI |
| Angular momentum | L&L §26, §27; Dirac VI §35; Born V §5 | Location | contents pages |
| Hydrogen | Feynman III Ch. 19 §19-1…§19-5 | Location | `feyman7.txt` headings |
| Hydrogen | L&L §36 | Location | L&L contents page |
| Hydrogen | Born V §4 + App. XVIII | Passage | full text: 3-D solution referred to App. XVIII |
| Spin | Feynman III Ch. 5 §5-1, §5-3; Ch. 6 §6-2…§6-6 | Location | `feyman6.txt`, `feyman8.txt` headings |
| Spin | Born VI §1; §7 "Magnetism" | Location (§1), Passage (§7) | contents; full text of §7 on the Stern–Gerlach method |
| Spin | L&L §54, §55 | Location | L&L contents page |
| Identical particles | Feynman III Ch. 4 §4-1, §4-7; §19-6 | Location | `feyman9.txt`, `feyman7.txt` headings |
| Identical particles | Born VI §4–§6; L&L §61 | Location | contents pages |
| Approximations | L&L §20, §38; Born VI §4 | Location | contents pages |
| Measurement | Feynman III §1-6, §2-6 | Location | `feyman1.txt`, `feyman2.txt` headings |
| Measurement | L&L §7; Born IV §7 | Location | contents pages |

Removed rather than shipped unverified: Feynman III Ch. 9 "The Ammonia Maser" (formalism
essay; not among the saved texts); the Stern–Gerlach cigar-smoke anecdote (spin essay; no
source on disk).

## Prose claims: verified 2026-09-18 (after the Parts I–III milestone commit)

Checked against external references by a research pass; four needed changes, made in the same commit.

| Claim | Result | Reference |
|---|---|---|
| Sodium work function "about 2.3 eV" | **Changed.** Modern handbook value is 2.75 eV (2.3 is an older, often-quoted value). Essay now states the range, uses 2.3 eV explicitly, and notes the 450 nm threshold at 2.75 eV. | Michaelson, J. Appl. Phys. 48, 4729 (1977) |
| Zinc work function about 4.3 eV | Correct (4.33 eV) | Michaelson 1977 |
| Millikan 1916, expected to refute Einstein, slope = h | Correct; nuance added that he stayed unconvinced about light quanta | Phys. Rev. 7, 355 (1916); Millikan's 1923 Nobel lecture |
| H-alpha 656.28 nm air / 656.46 nm vacuum; reduced-mass Bohr 656.47 nm | Correct (difference ~1.5×10⁻⁵) | NIST Atomic Spectra Database |
| Kennard 1927; Heisenberg microscope 1927 | Correct | Z. Phys. 44, 326 (1927); Z. Phys. 43, 172 (1927) |
| Ammonia maser line 23.87 GHz; first maser 1954 | Correct (NH₃ (3,3) inversion line) | Gordon, Zeiger & Townes, Phys. Rev. 95, 282 (1954) |
| Malus's law early nineteenth century | Correct (1809) | — |
| U-238, Po-212 half-lives | Correct (4.468 Gyr; 0.299 µs) | NNDC NuDat 3 |
| "Po-212 alpha particles carry 9.0 MeV" | **Changed** to "alpha decay releases 9.0 MeV" (Q-value; E_α = 8.78 MeV); note added on Q-value vs alpha energy | NNDC NuDat 3 |
| Geiger–Nuttall 1911; Gamow, Gurney–Condon 1928 | Correct | Phil. Mag. 22, 613 (1911); Z. Phys. 51, 204; Nature 122, 439 (1928) |
| CO band 2143 cm⁻¹, bond 112.8 pm; HCl 2886 cm⁻¹ | Correct | NIST Chemistry WebBook |
| CO lines 115.2712, 230.5380, 345.7960 GHz; ¹³CO 110.2014 GHz | Correct | CDMS catalogue c028503, c029501 |
| Stern–Gerlach 1922, first read as confirming Bohr's theory; apparatus numbers | Correct; numbers plausible (10 T/cm, 3.5 cm, ~1273 K, 0.2 mm total splitting) | Friedrich & Herschbach, Physics Today 56(12), 53 (2003) |
| "Only in 1925 ... did it become clear" | **Changed** to "only after 1925 ... gradually ... spelled out by 1927" | Friedrich & Herschbach 2003 |
| Uhlenbeck–Goudsmit 1925; Pauli matrices 1927; neutron 4π 1975 | Correct | Naturwiss. 13, 953 (1925); Z. Phys. 43, 601 (1927); Phys. Lett. A 54, 425 and PRL 35, 1053 (1975) |
| Pauli exclusion 1925; Slater 1929; helium once thought two gases | Correct | Z. Phys. 31, 765 (1925); Phys. Rev. 34, 1293 (1929); Nature 52, 327 (1895) |
| Ionisation energies H, He, He⁺, Li, Be, Ne, Na | Correct (79.005 eV total for He) | NIST ASD ionisation energies |
| "interference with molecules of thousands of atoms ... fades when gas is let in" | **Changed** to "up to about two thousand atoms" and the gas experiment attributed to fullerenes | Fein et al., Nat. Phys. 15, 1242 (2019); Hornberger et al., PRL 90, 160401 (2003) |
| Objective-collapse theories tested, none seen | Correct (bounds only) | e.g. Donadi et al., Nat. Phys. 17, 74 (2021) |
| Rutherford 1911, Balmer 1885, de Broglie 1924, electron diffraction 1927, Compton 1923, Planck 1900, Ehrenfest "ultraviolet catastrophe" 1911, Einstein 1905, Born 1926, Schrödinger 1926 and equivalence within months, Heisenberg–Born–Jordan 1925 | Correct; checked from standard citations, not re-fetched | Phil. Mag. 21, 669 (1911); Phys. Rev. 21, 483 (1923); Phys. Rev. 30, 705 (1927); Ann. Phys. 36, 91 (1911) |

Nothing is outstanding for the core essays. The relativity essays (a1–a4) have not been through this process.
