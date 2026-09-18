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

## OUTSTANDING: historical and numerical claims in the prose not checked against a source on disk

Status at the Parts I–III milestone commit: **none of the items below has been verified yet.**
They are the next task, before the optional essays are drafted.

These are standard history or standard data, stated from general knowledge. They should be
checked against a reference before release, or softened.

- Photons: Millikan's 1916 photoelectric test, and that he set out expecting to refute Einstein;
  sodium and zinc work functions (typical handbook values, stated as "about").
- Bohr: H-alpha measured wavelength 656.28 nm (air) / 656.47 nm (vacuum).
- Uncertainty: Kennard 1927 for the Δx Δp ≥ ħ/2 form; Heisenberg's 1927 microscope.
- Formalism: ammonia maser line 23.87 GHz; first maser 1954.
- Representations: Malus's law "early nineteenth century".
- Confinement: U-238 / Po-212 half-lives and alpha energies.
- Oscillator / angular momentum: CO band at 2143 cm⁻¹, bond length 113 pm; CO rotational lines
  115.271, 230.538, 345.796 GHz and ¹³CO 110.201 GHz; HCl band 2886 cm⁻¹.
- Spin: Stern–Gerlach 1922; Uhlenbeck–Goudsmit 1925; Pauli matrices 1927; neutron 4π
  interferometry 1975; deflection numbers are illustrative.
- Identical particles: Pauli 1925, Slater 1929; ionisation energies (NIST values quoted in the script).
- Approximations: helium measured total binding 79.0 eV (24.59 + 54.42 eV).
- Measurement: collisional decoherence experiments with large molecules; air-collision rate
  (computed in the script from standard gas values).
