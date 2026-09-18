# Rework survey — The Quantum Quartet → self-contained essays

Survey date 2026-09-18. Read-only pass over CONTEXT.md and chapters/01–14, a1–a4.
Target reader: adult with university mathematics, physics course ~20 years ago.
Yardstick: sister-book house style (concrete opening question; system/assumptions/notation
first; why the equation follows and what its terms predict; one worked instance with numbers
or explicit vectors; a limiting-case check; two short problems with worked answers).

Top-level findings are at the end of this file (section "Top-level"), written after all
chapters were read. Per-chapter notes follow in book order.

Conventions in the per-chapter notes:
- "stated" = equation/concept written down with a sentence of gloss
- "explained" = the reason it holds is given in words
- "worked" = an actual instance is carried through (numbers, explicit vectors, or a
  derivation with steps)
- Scaffolding % = rough share of the body (excluding nav/pointers) that is about the four
  books rather than the physics.

---

## 01 — Blackbody Radiation and Planck's Quantum

**Physics present**
- Blackbody = cavity with a hole, spectrum depends only on T (stated).
- Equipartition: each field mode carries k_B T; mode count grows as ν² → UV catastrophe
  (stated, half-explained; the ν² is asserted, not shown).
- Planck's hypothesis E = nhν for wall oscillators (stated). The Planck formula itself is
  NEVER written down. Wien and Rayleigh–Jeans limits are named but neither formula appears.
- No worked example, no numbers, no derivation. h is not given a value.
**Scaffolding share**: ~55%. Half the body is "why the other three are absent" plus the
  Synthesis on Born as witness.
**Missing for the target reader**
- The Planck formula u(ν,T) = (8πν²/c³)·hν/(e^{hν/kT}−1) and where each factor comes from
  (mode density × mean energy of a quantised oscillator).
- The one-line Boltzmann average ⟨E⟩ = hν/(e^{hν/kT}−1) that replaces kT — this IS the
  chapter and it is absent.
- The two limits actually taken (hν ≪ kT → kT; hν ≫ kT → Wien exponential).
- A number: Wien peak at 2.9 mm·K → the Sun at 5800 K peaks at 500 nm; or "how many
  modes/photons in a cubic metre at room temperature".
- What "a mode" is (standing wave in a box; counting k-vectors in a shell) — a rusty
  reader has forgotten this.
**Proposed spine**: "Why does a hot poker glow red, then white, and never ultraviolet?"
  Work the mean energy of one oscillator classically (kT) and quantised (Planck average),
  multiply by the mode density, get the Planck law; check hν ≪ kT recovers Rayleigh–Jeans
  and hν ≫ kT gives Wien; put the Sun's temperature in and get the visible peak.
**Keep**: the cavity-with-a-hole definition; the honest "Planck did not believe it" framing.
**Cut**: the whole "absence of Feynman, L&L, Dirac" section; Born-as-witness synthesis.
**Add**: Planck formula, its derivation sketch, mode counting reminder, Wien number, two
  problems (e.g. energy per quantum at 500 nm in eV; ratio of Planck to R–J at hν = 3kT).
**Dependencies**: none (first chapter). Needs a Boltzmann-factor reminder in-chapter.

---

## 02 — Photons: Photoelectric Effect and Compton Scattering

**Physics present**
- E = hν, p = hν/c for photons (stated).
- Photoelectric effect: threshold frequency, intensity ↔ number, frequency ↔ energy
  (explained in words). Einstein's equation K_max = hν − W is NOT written.
- Compton effect: described as a photon–electron billiard collision with energy and momentum
  conservation (stated). The Compton shift formula Δλ = (h/mc)(1 − cos θ) is NOT written;
  the Compton wavelength is not mentioned.
- Creation/annihilation operators, quantised field: name-dropped only.
**Scaffolding share**: ~70%. After the intro, everything is "Born's treatment / Feynman's
  counterpoint / L&L's deferral / Dirac's field" plus synthesis.
**Missing for the target reader**
- The photoelectric equation, and a plot-in-words: stopping potential vs frequency is a
  straight line of slope h/e (this is how h was measured — Millikan).
- The Compton derivation: two conservation equations, eliminate the electron, get the
  shift. Needs relativistic E² = p²c² + m²c⁴ — which appears only in A2 at the END of the
  book. Either import a one-paragraph reminder or use it as the forward pointer.
- Numbers: photon energy at 500 nm ≈ 2.5 eV; work function of sodium ≈ 2.3 eV; Compton
  wavelength 2.43 pm and why only X-rays show the shift.
- Why intensity does not change electron energy (the counting argument), stated as a
  prediction the wave picture makes and gets wrong.
**Proposed spine**: "Why does blue light eject electrons from sodium when a floodlight of
  red cannot?" Work Einstein's photoelectric equation with sodium numbers (threshold
  wavelength, stopping potential at 400 nm); then Compton as the second confirmation, with
  the shift derived from conservation laws and checked at θ = 0 (no shift) and θ = 180°
  (maximum 2λ_C).
**Keep**: the two-experiment structure; "hail of shot" image; the intensity/frequency
  separation argument.
**Cut**: all four author sections and synthesis; the QED/field-quantisation gestures.
**Add**: both equations, worked numbers, a short relativistic-momentum reminder, problems
  (e.g. stopping potential for Zn at 300 nm; Compton shift at 90°).
**Dependencies**: 01 (E = hν). Silently relies on A2 (relativistic kinematics) for Compton.

---

## 03 — The Bohr Atom and the Old Quantum Theory

**Physics present**
- Bohr postulates: hν = E_i − E_f and mvr = nℏ (stated).
- "Explains the hydrogen spectrum", "fails for helium" (asserted). The Bohr radius, the
  energy formula E_n = −13.6 eV/n², and the Balmer/Rydberg formula are NOT written.
- Correspondence principle: named and praised, never illustrated.
- Anomalous Zeeman, helium failure: named only.
**Scaffolding share**: ~65%.
**Missing for the target reader**
- The actual two-line derivation: Coulomb force = centripetal force + mvr = nℏ → r_n =
  n² a₀, E_n = −(me⁴/2ℏ²)/n² (or −13.6 eV/n²). Nothing in the chapter lets the reader
  compute anything.
- The Rydberg formula 1/λ = R(1/n_f² − 1/n_i²) and one line of Balmer (n=3→2, 656 nm).
- A correspondence-principle check: for large n, orbital frequency ≈ transition frequency
  n→n−1 — this is the one place the principle can be shown in three lines.
- Where mvr = nℏ comes from (de Broglie standing wave 2πr = nλ) — the chapter does not
  even mention de Broglie, which is the natural bridge to 04–06.
**Proposed spine**: "Why does hydrogen emit only certain colours?" Work the Bohr model from
  the two postulates to E_n and the Balmer line at 656 nm; check the large-n limit against
  the classical orbital frequency; state plainly what it gets wrong (helium, intensities,
  angular momentum of the ground state) as the reason chapters 04–10 exist.
**Keep**: "right kind of wrong"; list of what it cannot explain.
**Cut**: absence sections, Synthesis ("scaffolds are meant to be removed").
**Add**: full Bohr derivation, Rydberg formula, numbers, de Broglie standing-wave picture,
  problems (ionisation energy of He⁺; wavelength of Lyman-α).
**Dependencies**: 01–02 (E = hν). Nothing else.

---

## 04 — Quantum Behavior: The Double Slit and Amplitudes

**Physics present**
- The central rule: add complex amplitudes for indistinguishable routes, square the sum;
  cross-term = interference (stated and explained in words).
- Feynman's three rules (probability = |amplitude|²; add for alternatives; multiply for
  stages) (stated). Bracket notation ⟨x|s⟩ = ⟨x|1⟩⟨1|s⟩ (stated).
- "Distinguishable in principle ⇒ add probabilities" (explained well — best paragraph in
  Part II).
- Dirac: superposition on photon polarisation; c₁|A⟩ + c₂|B⟩; state = ray, not vector
  (stated, explained).
- L&L: |ψ|² dq probability; linearity of all equations as corollary (stated).
- Born rule from scattering analogy (stated). Wave packet dispersing (mentioned).
- NO worked example: the two-slit pattern is never computed. No |a₁ + a₂|² =
  |a₁|² + |a₂|² + 2Re(a₁*a₂) written out; no phase difference = 2π d sinθ/λ; no
  de Broglie wavelength.
**Scaffolding share**: ~45%. The physics content is actually decent but is chopped into
  four author-voices that each restate the same principle.
**Missing for the target reader**
- Explicit complex arithmetic: write a₁ = A e^{iφ₁}, a₂ = A e^{iφ₂}, expand the modulus
  squared, show the cos(φ₁−φ₂) term. The reader has complex numbers; use them.
- The phase from path length (φ = 2π L/λ) and de Broglie λ = h/p, with an electron number
  (e.g. 100 eV electron → λ ≈ 0.12 nm) — otherwise the slit experiment is a metaphor.
- Why "watching" destroys the pattern, made quantitative: a which-path record makes the
  two final states orthogonal so the cross-term vanishes. Three lines of inner products.
- What "state", "ket", "amplitude" mean operationally before 08 abstracts them.
**Proposed spine**: "If an electron is a particle, why does it make a fringe pattern?"
  Work the two-slit amplitude sum with explicit complex numbers, get the cos term and
  fringe spacing λL/d for a 100 eV electron; then add a which-path marker as an extra
  factor and show the cross-term cancels; check the limit d ≫ coherence (fringes wash out).
**Keep**: the three rules; the "record exists anywhere" criterion; ray-not-vector remark;
  the six-dimensional configuration-space warning.
**Cut**: "the four treatments" structure; the Feynman-vs-Dirac direction-of-travel
  synthesis; the historical Born-in-1926 material (move a sentence to 06).
**Add**: the explicit |a₁+a₂|² expansion, de Broglie number, fringe-spacing formula,
  which-path calculation, problems (fringe spacing for neutrons; phase for one extra
  wavelength of path).
**Dependencies**: 02 (photon momentum → de Broglie), 03 not really. Introduces the
  bracket notation that 08 formalises — ordering is fine.

---

## 05 — Two Mechanics: Matrices vs. Waves

**Physics present**
- Matrix mechanics from observables-only (explained historically; the Ritz combination
  rule is named, the multiplication rule not written).
- Non-commutativity as ordinary matrix non-commutativity (stated). [x,p] = iℏ NOT written.
- Dirac: Schrödinger vs Heisenberg picture via unitary T; equation of motion
  dv/dt = [v,H] "in his bracket notation" (stated — and the notation is ambiguous:
  Dirac's bracket here is the quantum Poisson bracket, which is (1/iℏ)[ , ]; as printed
  it reads like the commutator with the iℏ dropped. A reader who checks will be confused.)
- L&L: matrix element f_nm = ∫ψ_n* f̂ ψ_m dq; energy representation diagonal (stated).
- Equivalence of the two mechanics: asserted, never shown.
**Scaffolding share**: ~65%. This chapter is by design historical/comparative.
**Missing for the target reader**
- What a "picture" is and what the transformation does, in explicit form:
  |ψ(t)⟩ = U(t)|ψ(0)⟩, A_H(t) = U†AU, so ⟨A⟩ is picture-independent. Three lines, all
  linear algebra the reader owns.
- A concrete 2×2 or harmonic-oscillator instance in which a matrix element is computed
  from wavefunctions, so "matrix = operator in a basis" is seen, not told.
- The commutator [x,p] = iℏ and the statement that it is the same thing as the
  Heisenberg multiplication rule.
- What a Hamiltonian is (never defined anywhere in the book before this point).
**Proposed spine**: "Are Heisenberg's matrices and Schrödinger's waves the same theory?"
  Work the harmonic oscillator (or a two-level system) both ways: build the matrix of x
  from the first few ψ_n, show it is tridiagonal with the same non-zero elements Heisenberg
  had, and show the two time pictures give the same ⟨x(t)⟩; check the classical limit
  (Ehrenfest: d⟨p⟩/dt = −⟨V'⟩).
  ALTERNATIVE: merge into 08 (formalism) — see top-level.
**Keep**: the historical hook (one paragraph); "matrix is an operator in a basis";
  Heisenberg/Schrödinger picture distinction.
**Cut**: Born-as-participant, Feynman-silence sections, "four distances" synthesis.
**Add**: the unitary-picture algebra, one explicit matrix element calculation, [x,p] = iℏ,
  Hamiltonian reminder; problems (verify [x,p] on a test function; show the 2×2 rotation
  preserves eigenvalues).
**Dependencies**: 04 (states as vectors), and silently on 06 (needs ψ_n and Ĥ that are
  only introduced in the next chapter) and 08 (bras/kets). Order is backwards for the
  target reader.

---

## 06 — The Wavefunction and Schrödinger's Equation

**Physics present**
- The Schrödinger equation iℏ∂_tΨ = −(ℏ²/2m)ΔΨ + UΨ (stated).
- L&L's symmetry argument (homogeneity → no x-dependence; isotropy → |p|; Galilean
  invariance → p²/2m) (explained in words, not shown).
- Classical limit via Ψ = a e^{iS/ℏ} → Hamilton–Jacobi and a continuity equation
  (stated; not worked; the reader has forgotten Hamilton–Jacobi and the chapter does not
  remind them).
- Feynman's lattice-hopping derivation, imaginary diffusion coefficient (described).
- Born rule |ψ|² as probability density; six-dimensional configuration space; dispersing
  wave packet (stated).
- Dirac: iℏ d/dt|Pt⟩ = H|Pt⟩ and its position-basis reading (stated).
- NO worked solution: not the free particle, not the plane wave, not separation of
  variables, not the time-independent equation Hψ = Eψ. "Stationary state" is not defined.
**Scaffolding share**: ~50%.
**Missing for the target reader**
- Operator correspondence p → −iℏ∇, E → iℏ∂_t and why (act on a plane wave
  e^{i(kx−ωt)}, use de Broglie p = ℏk and E = ℏω). This is the honest "motivation" that
  a rusty reader can follow in five lines and the chapter skips.
- Separation of variables → time-independent equation → stationary states with
  e^{−iEt/ℏ}; that is what every later chapter uses.
- Normalisation ∫|ψ|² = 1 and the probability current.
- The free-particle Gaussian packet spreading, with a number (an electron packet 1 nm wide
  doubles in ~10⁻¹⁶ s) — this makes Born's "packet disperses" remark real and feeds 07.
- Hamilton–Jacobi reminder if the classical-limit argument is kept (or drop it).
**Proposed spine**: "What equation does the de Broglie wave obey, and what does its
  solution mean?" Motivate via the plane wave and operator substitutions; define ψ, the
  Born rule and normalisation; separate variables to get Hψ = Eψ; work the free particle
  and a Gaussian packet's spreading with numbers; check the limit ℏ → 0 or large mass
  (packet stops spreading — the classical particle).
**Keep**: the honesty that the equation is postulated; the symmetry argument condensed to
  one paragraph; the configuration-space warning.
**Cut**: the four-way "how do you present a postulated equation" framing; Feynman's
  Chapter-16 placement as a topic; Hamilton–Jacobi (unless reminded).
**Add**: operator substitutions, stationary states, normalisation, worked free particle
  and packet, problems (normalise a Gaussian; show e^{i(kx−ωt)} satisfies the free
  equation with E = ℏ²k²/2m).
**Dependencies**: 04 (amplitudes), 02 (de Broglie — which the book never actually
  introduces; must be added in 02 or 04). Chapter 05 uses this chapter's ψ_n before it
  exists.

---

## 07 — The Uncertainty Principle

**Physics present**
- Single-slit argument: slit width Δx, diffraction spread → transverse Δp, with λ = h/p
  gives Δx Δp ~ h (explained in words; the angle θ ≈ λ/Δx and p_⊥ ≈ p θ step is not
  written).
- γ-ray microscope (explained qualitatively; Compton recoil named).
- Wave packet needs a spread of momenta (stated; Fourier not shown).
- Feynman's movable-slit argument (explained qualitatively, best paragraph).
- L&L: [x̂,p̂] = iℏ → Δx·Δp ≥ ℏ/2 "as a theorem" (stated; Cauchy–Schwarz named in the
  table, not used). Feynman's version quoted as Δx Δp ≳ ℏ/2 — three different constants
  (h, ℏ/2, "~") appear with no remark on why they differ.
- Dirac: non-commuting observables (stated only).
- "Not about measurement disturbance but about states" (explained — good).
- No worked example, no numbers, no Fourier pair, no Gaussian.
**Scaffolding share**: ~50%. The physics paragraphs are decent but each is a précis of
  a book rather than an explanation.
**Missing for the target reader**
- What Δx and Δp actually are (standard deviations of |ψ|² and |φ(p)|²) — never defined.
- The Fourier reminder: ψ(x) and φ(p) are a transform pair with kernel e^{ipx/ℏ}; a
  Gaussian of width σ transforms to width ℏ/(2σ) — the minimum-uncertainty case worked in
  four lines. This is what a maths-literate reader can actually verify.
- Reconciling h vs ℏ/2 vs "≳": order-of-magnitude arguments give ~h, the sharp bound is
  ℏ/2, and it is attained only by a Gaussian.
- A number: electron confined to an atom (0.1 nm) → Δp → kinetic energy ~ eV, which
  explains why atoms do not collapse and previews 10. Or a proton in a nucleus (MeV).
- The general form ΔA ΔB ≥ ½|⟨[A,B]⟩| — needs 08's expectation value, which is defined
  after this chapter (ordering issue).
- Energy–time relation, at least mentioned (needed in 13/14 for lifetimes and linewidth).
**Proposed spine**: "Why doesn't the electron fall into the nucleus?" Define Δx, Δp as
  standard deviations; do the single-slit estimate; then work the Gaussian packet's Fourier
  transform explicitly to get Δx Δp = ℏ/2; use it to estimate the ground-state size and
  energy of hydrogen (~0.1 nm, ~−10 eV) by minimising ⟨p²⟩/2m − e²/4πε₀⟨r⟩; check the
  limit of a macroscopic object (dust grain: Δv negligible).
**Keep**: single slit; movable-slit refutation of "clumsiness"; the "about states, not
  instruments" paragraph.
**Cut**: the four-author sections and three-lesson synthesis; the Born-ordering aside
  ("slit first, microscope second" is source-criticism, not physics).
**Add**: definitions of Δ; Fourier pair; Gaussian worked; hydrogen size estimate;
  problems (Δv for a 1 g grain located to 1 μm; minimum KE of a proton in 5 fm).
**Dependencies**: 04 (amplitudes), 06 (ψ, packets, Fourier — which 06 does not actually
  supply). Uses expectation values and commutators from 08 before 08.

---

## 08 — States, Observables, Bras and Kets

**Physics present**
- Kets |A⟩, bras ⟨B|, scalar product ⟨B|A⟩ complex (stated).
- Hermitian operators have real eigenvalues (stated, not shown).
- Observable = Hermitian operator with complete eigenstates; measurement yields an
  eigenvalue and the state "jumps" to the eigenstate; repeat measurement gives same
  result (stated, explained).
- Projector |A⟩⟨A| with eigenvalues 0,1 (stated).
- Completeness ⟨χ|φ⟩ = Σ⟨χ|i⟩⟨i|φ⟩; orthonormal base ⟨i|j⟩ = δ_ij; expansion
  |φ⟩ = Σ|i⟩⟨i|φ⟩ (stated, motivated by Stern–Gerlach filters in words).
- Matrix element ⟨n|f|m⟩ = ∫ψ_n* f̂ ψ_m dq (stated).
- p̂ = −iℏ∂_x; Pauli matrices (named).
- NOTHING is worked: no 2×2 example, no eigenvalue computed, no expectation value, no
  probability |⟨i|φ⟩|² formula written (it is implied only).
**Scaffolding share**: ~55%. The Dirac section is close to physics; the L&L/Feynman/Born
  sections are about whose notation means what.
**Missing for the target reader**
- Expectation value ⟨A⟩ = ⟨ψ|A|ψ⟩ = Σ a_i |c_i|² — never defined, though later chapters
  (and 07) use the idea.
- The Born-rule bridge: probability of outcome a_i is |⟨i|ψ⟩|²; ties back to 04's "square
  the amplitude".
- Why Hermitian ⇒ real eigenvalues and orthogonal eigenvectors (a 3-line proof the reader's
  linear algebra allows).
- A finite-dimensional worked case: spin-½ or a two-level system with an explicit 2×2
  Hermitian matrix, its eigenvectors, and the probabilities from a given state. Everything
  in the chapter is abstract; the reader has linear algebra and needs to see it bite.
- Commutator and compatibility: [A,B] = 0 ⇔ simultaneous eigenstates — the reason 07 and
  11 work.
- Continuous case: ⟨x|ψ⟩ = ψ(x) explicitly, with the caveat about delta-normalisation.
**Proposed spine**: "What does 'the electron is in a state' mean, and what does a
  measurement do to it?" Set up a 2-dimensional Hilbert space (polarisation or spin);
  write an explicit Hermitian matrix, find its eigenvalues/vectors, compute the outcome
  probabilities and expectation value for an explicit state vector; then say how this
  generalises to ψ(x) and p̂ = −iℏ∂_x; check the limit of an eigenstate (probability 1,
  repeat measurement identical).
**Keep**: observable = complete set of eigenstates; jump postulate; completeness relation
  motivated by filters; projector.
**Cut**: "translation layer" framing; L&L-vs-Dirac ontology of ψ vs ket; Born's absence.
**Add**: expectation value, Born rule in bracket form, Hermitian proof, worked 2×2,
  commutator/compatibility; problems (eigenvectors of σ_x; probability of +ℏ/2 along x
  for a spin-up-along-z state).
**Dependencies**: 04 (amplitudes and brackets), 06 (ψ). Should precede 05 and 07 — see
  top-level.

---

## 09 — Wells, Barriers, and Tunneling

**Physics present**
- Transmission D = transmitted/incident current, R = 1 − D (stated).
- Reflection above a step (stated, no formula).
- Rectangular barrier: D ∝ e^{−2κa}, ℏκ = √(2m(U₀−E)) (stated; not derived).
- Exact solvable barriers (cosh⁻², smooth step) and transmission resonances (named).
- WKB penetration formula (named; not written).
- Alpha decay as tunnelling through a Coulomb "crater"; Geiger–Nuttall law qualitative;
  cold field emission (explained in words).
- Ammonia inversion as two-state tunnelling, level splitting → maser (described).
- No bound-state well at all: the infinite square well and its E_n = n²π²ℏ²/2mL² never
  appear anywhere in the book, though the chapter title says "Wells".
**Scaffolding share**: ~45%. Physics is more present than in Part II but still
  précis-level.
**Missing for the target reader**
- Boundary conditions: ψ and ψ' continuous — the mechanism of every result here — never
  stated.
- The bound-state well worked (infinite well → discrete E_n; finite well → fewer, lower
  levels, ψ leaks into the walls) as the preparation for tunnelling. This is the
  "confined ⇒ discrete" fact the rest of the book assumes.
- The barrier calculation actually carried out: three regions, match at x=0 and x=a,
  extract D ≈ 16(E/U₀)(1−E/U₀) e^{−2κa}. Even a sketch with the key step shown.
- Numbers: electron, U₀−E = 1 eV, a = 1 nm → κ ≈ 5 nm⁻¹, e^{−2κa} ≈ 5×10⁻⁵; how this
  gives the STM its atomic sensitivity (factor ~10 per 0.1 nm).
- Probability current j = (ℏ/m) Im(ψ*ψ') — used to define D but never given.
- Ammonia: the 2×2 Hamiltonian [[E₀,−A],[−A,E₀]] and its splitting 2A — it is described
  but the matrix is not shown, though 08 supposedly prepared the reader for exactly this.
**Proposed spine**: "How does an alpha particle get out of a nucleus it does not have the
  energy to leave?" First the infinite/finite well to establish discrete levels and leakage
  into forbidden regions; then the rectangular barrier matched explicitly to get
  e^{−2κa}; put in numbers for an electron (STM) and for an alpha particle (why
  half-lives span 10²⁰ in a factor 2 of energy); check the classical limit κa → ∞
  (D → 0) and E > U₀ (oscillatory, D → 1 with resonances).
**Keep**: alpha-decay crater picture; Geiger–Nuttall; STM/cold emission; resonance-over-a-
  well surprise; ammonia as tunnelling (short).
**Cut**: Dirac-absence section; Feynman-vs-Landau genre discussion; hypergeometric
  catalogue (one sentence at most).
**Add**: boundary conditions, wells worked, barrier matched, current, numbers, problems
  (levels of an electron in a 1 nm infinite well; D for a 2 nm barrier).
**Dependencies**: 06 (time-independent Schrödinger equation, stationary states — which 06
  did not define), 08 (two-state Hamiltonian for ammonia).

---

## 10 — The Hydrogen Atom

**Physics present**
- E_n = −mα²/(2ℏ²n²) (stated). NOTE: here α means the Coulomb coupling e²/4πε₀ (Dirac's
  V = −α/r), not the fine-structure constant; the chapter never says so, and a reader who
  knows α ≈ 1/137 will get a wrong formula. Must be fixed in the rewrite.
- Classical atom collapses by radiation (explained in words; the ~10⁻¹¹ s number is not
  given).
- Balmer formula as difference of two terms → energy levels (explained in words; formula
  not written; Rydberg constant not related to m, e, ℏ explicitly).
- Coulomb/atomic units; radial equation → confluent hypergeometric; termination of the
  series ⇒ n integer, n ≥ l+1; E = −1/2n² (stated; not worked).
- Accidental degeneracy n² (stated, explained as special to 1/r).
- Dirac's radial Hamiltonian H = (1/2m)(r⁻¹p_r²r + k(k+ℏ)/r²) + V (stated; opaque to the
  reader; also uses Dirac's k rather than l).
- Angular part eigenvalues l(l+1)ℏ² (stated).
- Feynman's series solution "fiddle around" (described).
- ∇²(1/r) hides a delta function (mentioned).
- No wavefunction is written (not even ψ₁₀₀ ∝ e^{−r/a₀}); no a₀; no 13.6 eV; no
  quantum-number table (n, l, m ranges); no spectrum line computed.
**Scaffolding share**: ~55%.
**Missing for the target reader**
- Separation in spherical coordinates: ψ = R(r)Y_lm(θ,φ), the effective potential
  V + ℏ²l(l+1)/2mr², and the reminder of what l and m are.
- The ground state actually worked: try ψ = e^{−r/a} in the l = 0 radial equation, find
  a = a₀ = 4πε₀ℏ²/me² = 0.053 nm and E₁ = −13.6 eV. Four lines, fully checkable by the
  reader — far better than describing hypergeometric functions.
- Quantum-number bookkeeping (n ≥ 1, 0 ≤ l ≤ n−1, |m| ≤ l, count n²) and what degeneracy
  means.
- Balmer numbers: Hα at 656 nm from 3 → 2; Rydberg constant R = 1.097×10⁷ m⁻¹ from the
  formula.
- Link to 07's uncertainty estimate (same a₀ and energy scale) and to 03's Bohr result
  (identical E_n, different meaning of n and l).
- Reduced mass mention (why deuterium lines shift) — optional but a nice check.
**Proposed spine**: "Why is hydrogen's spectrum exactly the Balmer series?" Separate
  variables, reduce to the radial equation with the centrifugal term; solve l = 0 ground
  state by substitution e^{−r/a₀}; state the general E_n and the quantum-number ranges;
  compute Hα; check the large-n correspondence limit and the size of the n-th orbit
  (n²a₀ — Rydberg atoms).
**Keep**: classical-collapse hook; Balmer-difference insight; accidental-degeneracy
  remark; ∇²(1/r) footnote (one line).
**Cut**: all four author sections; "Feynman pays the bill" synthesis; continuous spectrum;
  Dirac's radial-momentum algebra.
**Add**: separation of variables, worked ground state, a₀ and 13.6 eV, quantum-number
  table, Hα number, fix the α symbol; problems (energy of Lyman-α; He⁺ ground-state
  energy and radius; most probable radius from |ψ₁₀₀|² r²).
**Dependencies**: 03 (Bohr — recovered result), 06 (time-independent SE), 09 (bound
  states), 07 (size estimate). Needs angular momentum eigenvalues l(l+1)ℏ², which no
  chapter derives or explains (a gap in the whole book — see top-level).

---

## 11 — Spin

**Physics present**
- Spin: intrinsic angular momentum, half-integer, no classical rotating-ball picture
  (explained in words, well).
- Stern–Gerlach: inhomogeneous field splits beam into 2s+1 beams; filtering, no re-split
  after a second identical apparatus (explained).
- Dirac: σ_i² = 1, anticommuting; σ_z diagonal ⇒ Pauli matrices forced (explained in words;
  the matrices themselves are NOT written).
- L&L: spin operators obey the angular-momentum commutation relations; s² = s(s+1);
  half-integers allowed because the coordinate-representation argument fails; 2π rotation
  flips sign of half-integer spinor (stated).
- Born: alkali doublets, anomalous Zeeman, Uhlenbeck–Goudsmit 1925; spin magnetic moment
  (named).
- Feynman: rotation amplitudes "by pure reasoning" (mentioned; none shown).
- No matrix written; no spinor written; no magnetic moment formula (μ = −g(e/2m)S, g ≈ 2);
  no Zeeman energy ±μ_B B; no Stern–Gerlach force F = μ_z ∂B/∂z; no Larmor precession.
**Scaffolding share**: ~55%. The framing paragraph explicitly says the chapter is "built
  to let the contrast do the work".
**Missing for the target reader**
- The Pauli matrices written down, with eigenvectors of σ_x and σ_z shown explicitly —
  this is the single most natural 2×2 worked example in the book and it is absent.
- The Stern–Gerlach calculation: force on a dipole in a gradient, the deflection, the
  number two, and hence s = ½ and μ ≈ μ_B (9.27×10⁻²⁴ J/T).
- The probability that a spin-up-along-z is found up along x (½) or along a direction at
  angle θ (cos²(θ/2)) — the "rotation amplitudes" made concrete.
- Why the commutation relations [S_x,S_y] = iℏS_z fix the spectrum (a sketch, or a pointer
  back to an angular-momentum section that the book lacks).
- Precession in a field: H = −μ·B, the two-level time evolution — bridges to 09's ammonia
  two-state system and to 14.
**Proposed spine**: "Why does a beam of silver atoms split into exactly two?" Do the
  Stern–Gerlach force and deflection with numbers; infer two states; write the Pauli
  matrices and verify σ_x² = 1 and the anticommutation; find the eigenvectors of σ_x; work
  the probability cos²(θ/2) for a tilted second magnet; check θ = 0 (certainty) and
  θ = π/2 (½); mention the 2π sign flip as a consequence of the half-angle.
**Keep**: "no classical picture" opening; Stern–Gerlach as filter; Dirac's algebraic
  forcing of the matrices; Born's doublets as one motivating paragraph.
**Cut**: Feynman-vs-Dirac contrast as the chapter's thesis; "four doors into one room";
  L&L rotation-group derivation (state the result only).
**Add**: matrices, eigenvectors, S–G numbers, magnetic moment and Zeeman energy, tilted
  magnet probability, problems (probability of spin-down along a direction 60° from z;
  Zeeman splitting of an electron in 1 T in eV).
**Dependencies**: 08 (2-dim state space, Hermitian matrices, measurement postulate), 10
  (angular momentum labels l, m). Feeds 12 (spin part of the two-electron wavefunction)
  and A4.

---

## 12 — Identical Particles and the Periodic Table

**Physics present**
- Indistinguishability ⇒ exchange changes ψ by a phase; exchanging twice ⇒ phase² = 1 ⇒
  ψ symmetric or antisymmetric (explained — the one real derivation in the chapter, in
  words).
- Antisymmetric ⇒ determinant ⇒ vanishes if two states coincide ⇒ Pauli exclusion
  (explained; the 2×2 Slater determinant is not written).
- Boson/fermion scattering: amplitudes combined with ± ; doubling at 90° for bosons
  (stated).
- Spin–statistics theorem: stated as a fact from relativistic QFT, honestly not derived.
- Symmetry preserved by dynamics because H is symmetric (stated).
- Exchange interaction: spin-dependent energy from symmetry of the spatial part
  (explained in words; no formula, no singlet/triplet).
- Periodic table from shell filling (described; no shell-capacity count 2n², no
  configuration, no example element).
**Scaffolding share**: ~50%.
**Missing for the target reader**
- Explicit two-particle wavefunctions: ψ_S = [φ_a(1)φ_b(2) + φ_b(1)φ_a(2)]/√2,
  ψ_A with the minus; show ψ_A = 0 when a = b. Two lines; the reader can see the
  exclusion principle happen.
- Spin ⊗ space: total antisymmetry ⇒ symmetric space with singlet spin, antisymmetric
  space with triplet; why the triplet has lower Coulomb energy (electrons kept apart) —
  helium's ortho/para, Hund's rule. This is where the "exchange interaction" becomes
  meaningful.
- The counting: 2(2l+1) electrons per subshell, 2n² per shell; walk through Li, Ne, Na
  to show why sodium is an alkali.
- Scattering example needs |f(θ) ± f(π−θ)|² written out and evaluated at θ = π/2.
- What happens in the classical limit (wave packets non-overlapping ⇒ symmetrisation
  irrelevant) — the limiting-case check.
**Proposed spine**: "Why don't all of an atom's electrons sit in the lowest orbit?"
  Derive ± from double exchange; write the two-particle symmetric/antisymmetric
  functions and show the antisymmetric one vanishes for identical orbitals; combine with
  spin (singlet/triplet) for helium and explain the ortho/para energy order; count shell
  capacities and build Li → Ne → Na; check the limit of non-overlapping particles.
**Keep**: phase-squared argument; determinant; Feynman's honest "we cannot explain
  spin–statistics"; exchange interaction; periodic-table payoff.
**Cut**: the "three assertions and one confession" synthesis; Dirac's permutation-
  operator framing; who-said-what.
**Add**: explicit two-particle functions, singlet/triplet, helium, shell counting,
  scattering formula; problems (why is ψ = φ_a(1)φ_a(2) allowed for bosons but not
  fermions; ground-state configuration of oxygen).
**Dependencies**: 06 (multi-particle ψ on configuration space), 10 (orbitals n,l,m), 11
  (spin states, singlet/triplet needs 2-spin algebra not given anywhere).

---

## 13 — Approximation Methods

**Physics present**
- Split H = H₀ + V, small V, compute corrections as a series (stated).
- First-order energy = diagonal matrix element; second-order = sum over intermediate
  states with energy denominators; degenerate case = secular determinant (stated in
  words; NO formula written — not even E⁽¹⁾ = ⟨n|V|n⟩).
- Time-dependent perturbations → transition probabilities; periodic perturbation →
  resonance (named).
- Dirac's two-method taxonomy: shifting stationary states vs causing transitions
  (explained — the only genuinely explanatory paragraph).
- Two-state exact diagonalisation, ammonia (described; matrix not written).
- Helium via Hylleraas; screening; Lamb shift (named).
- No variational method, no WKB (the "approximation methods" of the title are only
  perturbation theory), no worked example, no numbers.
**Scaffolding share**: ~70%. The chapter says of itself "the interest is in stance rather
  than result".
**Missing for the target reader**
- The formulas: E_n⁽¹⁾ = ⟨n|V|n⟩, ψ⁽¹⁾ = Σ_{k≠n} |k⟩⟨k|V|n⟩/(E_n−E_k),
  E⁽²⁾ = Σ |⟨k|V|n⟩|²/(E_n−E_k), and a two-line reason for the first (project the
  equation onto ⟨n|). The reader can follow this; it is linear algebra.
- Why the second-order correction to the ground state is always negative (denominators)
  — a useful sanity check.
- A worked instance: the 2×2 case, where exact and perturbative answers can both be
  written and compared (E± = E₀ ± √(Δ² + V²) vs E₀ ± Δ ± V²/2Δ); this ties Feynman's
  "exact two-state" and Landau's "series" into one example rather than opposing them.
- Or: Stark/Zeeman first-order shift of hydrogen ground state, or the helium ground state
  by first-order perturbation (−108.8 eV → −74.8 eV vs −79.0 eV measured) — a number
  that shows what "works to excellent agreement" means.
- The variational principle in one paragraph (E[ψ_trial] ≥ E₀), because helium is the
  classic case and it is far easier to explain than second-order PT.
- Fermi's golden rule stated (transitions), since 14 and A4 gesture at emission.
**Proposed spine**: "Helium has two electrons and no exact solution — how close can we
  get?" Derive first-order PT by projecting onto the unperturbed state; apply to helium
  (Z = 2, e–e repulsion as V) to get −74.8 eV vs −79.0 eV measured; then the 2×2 example
  to show what second order does and when the series fails (V ~ Δ); check the limit
  V → 0 (series collapses to the unperturbed level) and the variational bound as the
  cross-check (−77.5 eV with an effective Z).
**Keep**: "hard problem as easy one slightly disturbed"; the two-method distinction;
  Born's "beyond hydrogen everything is approximate".
**Cut**: all four temperament sections; "method is never separable from temperament".
**Add**: the formulas, the projection derivation, helium number, 2×2 comparison,
  variational bound, golden rule statement; problems (first-order shift of a
  particle-in-a-box under a linear potential; when does |V|/Δ = 0.3 make second order
  necessary).
**Dependencies**: 08 (matrix elements, expectation values), 09 (two-state system), 10
  (hydrogen-like states for helium), 12 (two-electron ground state is symmetric-space
  singlet).

---

## 14 — Measurement and What It All Means

**Physics present**
- Two kinds of evolution: smooth deterministic Schrödinger vs measurement "jump"
  (stated, explained).
- Watching the slit destroys interference; minimum disturbance (explained in words).
- Born: ψ evolves deterministically but only |ψ|² is observable, so initial ψ is not
  fixed by data; "causality empty" (explained — a genuinely interesting argument, though
  its logic is shaky: a state IS fixed up to global phase by a complete set of
  measurements on an ensemble; the real point is that outcomes are only statistical).
- L&L: classical apparatus + quantum object; correlation of reading with object-state;
  two-faced character; irreversibility and arrow of time (stated in words; no formula
  for the entangled apparatus–object state Σ c_n |n⟩|A_n⟩).
- Dirac: projection postulate, repeatability (stated).
- No calculation at all. No density matrix, no decoherence, no Bell/EPR, no example with
  numbers.
**Scaffolding share**: ~65%. By design a "what will each author say" chapter.
**Missing for the target reader**
- The measurement postulate written as an equation: state Σ c_n|n⟩ → |k⟩ with probability
  |c_k|², and the contrast with unitary evolution. The reader has read 08; this is the
  place to use it.
- Von Neumann's chain made concrete: apparatus states |A_n⟩, unitary interaction gives
  Σ c_n |n⟩|A_n⟩; the pointer is in a superposition; why this does not itself produce a
  definite outcome — that is the measurement problem in one line, and no chapter says
  it.
- Why interference disappears when a record exists (reduced probabilities; cross-terms
  ⟨A_1|A_2⟩ ≈ 0): a three-line calculation that unifies 04, 07 and this chapter and gives
  the "irreversibility" claim its mechanism (decoherence, if named).
- A limiting case: a macroscopic pointer with 10²³ degrees of freedom — overlap
  ⟨A_1|A_2⟩ essentially zero — so classical apparatus is a limit, not an axiom.
- Honest statement of what remains open (interpretations) in one paragraph, not four.
**Proposed spine**: "What does the equation say happens when a detector clicks?" Set up a
  spin-½ particle and a two-state detector; evolve unitarily to the entangled state;
  show the cross-term in the particle's probabilities is multiplied by ⟨A_↑|A_↓⟩ and
  vanishes when the detector states are distinguishable; contrast with the projection
  postulate; check the limit of a "detector" that does not record (⟨A_↑|A_↓⟩ = 1,
  interference intact — 04's which-path result recovered); end with the one-paragraph
  statement of the open problem.
**Keep**: two-kinds-of-evolution opening; Feynman's "only ask what you can measure"
  tempered; L&L's classical-apparatus picture and irreversibility; Born's outcomes-are-
  statistical point (reworded).
**Cut**: "four disciplined responses"; tree-in-the-forest; the L&L-is-not-silent surprise.
**Add**: measurement postulate as equation; entangled apparatus state; cross-term
  suppression; macroscopic limit; problems (probability of a sequence of two spin
  measurements along z then x; show a repeated measurement gives the same result).
**Dependencies**: 04 (which-path), 08 (postulate, projectors), 11 (spin-½ as the
  example), 12 (tensor product of two systems — never introduced anywhere in the book;
  needs a reminder here).

---

## A1 — Spacetime and Lorentz Transformations

**Physics present**
- Two postulates (stated). Relativity of simultaneity via the train/lightning argument
  (explained, well — the best physics prose in the book).
- Lorentz transformation: named, NEVER written. No γ, no x' = γ(x − vt), no time
  dilation, no length contraction, no velocity addition, no invariant interval formula.
- Michelson–Morley: described.
- m = m₀/√(1−v²/c²) (stated, and in the outdated "relativistic mass" convention).
- Minkowski spacetime as "rotation" (named).
**Scaffolding share**: ~45% (two-author comparison instead of four).
**Missing for the target reader**
- The transformation itself and the two-line derivation of γ from the light-clock (or
  from requiring x² − c²t² invariant, which a linear-algebra reader can verify).
- Time dilation and length contraction as consequences, with the muon number (2.2 μs
  lifetime, γ ≈ 10 at cosmic-ray energies → reaches the ground).
- Velocity addition and the check that c + anything = c.
- Invariant interval s² = c²t² − x² and the "rotation" made honest (hyperbolic angle).
- Low-velocity check γ → 1 + v²/2c², Galilean limit.
**Proposed spine**: "How can a muon that lives 2 μs reach the ground from 15 km up?"
  Postulates; simultaneity argument (keep); derive γ from the light clock; write the
  Lorentz transformation and read off dilation, contraction, velocity addition; work
  the muon numbers; check v ≪ c recovers Galileo.
**Keep**: the train/lightning simultaneity argument; Maxwell-as-motivation paragraph.
**Cut**: Einstein-vs-Feynman "inside and after" synthesis; the relativistic-mass
  formula (move to A2 in modern form).
**Add**: the transformation, γ, the three consequences, the interval, muon example,
  problems (γ at 0.6c; length of a 1 m rod at 0.8c).
**Dependencies**: none physically; relies on Maxwell's-equations invariance as a fact
  the reader accepts on trust.

---

## A2 — Mass, Energy, Relativistic Dynamics

**Physics present**
- E = mc² as a consequence of Lorentz invariance (stated). Absorbing energy E₀ raises
  inertial mass by E₀/c² (stated).
- ΔT = (m − m₀)c², total energy = mc² in the relativistic-mass convention (stated).
- Inelastic collision: composite heavier by the kinetic energy brought in (explained in
  words, no equations).
- "Effect invisible because c² is enormous" (stated; no number).
- No four-momentum, no E² = p²c² + m²c⁴, no p = γmv, no kinetic energy expansion
  T ≈ ½mv² + ⅜mv⁴/c², no binding-energy example.
**Scaffolding share**: ~55%.
**Missing for the target reader**
- Modern conventions: m is invariant; E = γmc², p = γmv; E² = (pc)² + (mc²)². The
  chapter's velocity-dependent-mass language will confuse anyone who later reads a
  current text (and 02's Compton derivation needs the modern form).
- The low-speed check: expand γ to get ½mv² + rest energy — the single most satisfying
  limiting case in the appendix and it is missing.
- A number: 1 g of mass ↔ 9×10¹³ J; helium binding energy 28 MeV ↔ 0.03 u mass defect
  (0.7%); the Sun's 4×10⁹ kg/s.
- The collision worked: two masses m at ±v stick; M = 2γm > 2m, with a numerical case
  (v = 0.6c → γ = 1.25, M = 2.5m).
- Massless particles: E = pc and the photon (closes the loop with 02).
**Proposed spine**: "Where does the Sun's energy come from, and why does a helium
  nucleus weigh less than its parts?" Define γ, p = γmv, E = γmc²; check the low-speed
  expansion; derive E² = p²c² + m²c⁴; work the mass defect of helium and the
  1-g-of-matter number; the sticky collision as the second instance.
**Keep**: "conservation of mass and energy are one law"; "a hotter gas is heavier";
  Einstein's honesty about the un-measurable effect in 1920.
**Cut**: Einstein-vs-Feynman synthesis; relativistic-mass language.
**Add**: the four formulas, the expansion, the numbers, problems (energy of a proton at
  γ = 7 in GeV; speed at which T = mc²).
**Dependencies**: A1 (γ, Lorentz transformation — which A1 does not actually write).
  Chapter 02 (Compton) silently needs this.

---

## A3 — General Relativity, Sketched

**Physics present**
- Equivalence principle via the accelerating chest (explained well).
- Equality of inertial and gravitational mass (stated).
- Light bends and clocks slow in a gravitational field (asserted as consequences; no
  formula).
- Rotating disc: circumference/diameter ≠ π ⇒ non-Euclidean geometry (explained).
- "Matter tells spacetime how to curve" (quoted-in-spirit). Field equations deferred.
- No number, no calculation, no gravitational redshift formula, no deflection angle.
**Scaffolding share**: ~40% (single-voice already; the scaffolding is the "why the
  comparison collapses" paragraphs).
**Missing for the target reader**
- Two things the reader can actually compute from the equivalence principle alone:
  gravitational redshift Δν/ν = gh/c² (Pound–Rebka: 2.5×10⁻¹⁵ over 22 m) and the
  Newtonian-order light deflection 2GM/(c²R) (0.87″; GR doubles it to 1.75″). These are
  "sketch-level" but quantitative and honest.
- GPS clock correction (+45 μs/day gravitational, −7 μs/day velocity) as the everyday
  instance.
- The Schwarzschild radius 2GM/c² as the scale at which curvature matters, with numbers
  for the Sun (3 km) and Earth (9 mm), so the reader sees why GR is negligible in atoms.
- A one-paragraph honest statement of what the field equations say (G_μν = 8πG T_μν/c⁴)
  without deriving.
**Proposed spine**: "Why does a clock on a mountain run fast, and by how much?" Equivalence
  principle (keep the chest); derive gravitational redshift from an accelerating lab and a
  light pulse; convert to clock rate; put in Pound–Rebka and GPS numbers; sketch light
  deflection; check the limit of weak fields (Newton recovered) via the Schwarzschild
  radius scale.
**Keep**: the chest; the rotating disc; the honesty about stopping short.
**Cut**: "why the comparison collapses to one voice"; "unfinished business" coda
  (duplicated in A4).
**Add**: redshift derivation and numbers, deflection number, Schwarzschild scale, GPS;
  problems (fractional clock difference over 1 km; Earth's Schwarzschild radius).
**Dependencies**: A1 (time dilation for GPS), A2 (E = mc² for the photon-energy version
  of redshift).

---

## A4 — Where the Threads Meet: The Dirac Equation

**Physics present**
- Motivation: theory must be Lorentz invariant; equation first order in all four
  coordinates (explained in words).
- Dirac equation itself NEVER written (no iℏγ^μ∂_μψ = mcψ, no α, β matrices, no
  4-component spinor).
- Magnetic moment −eℏ/2mc emerges automatically (stated). Spin ½ℏσ needed for angular
  momentum conservation (stated).
- Negative-energy solutions; Dirac sea; hole = positron; Anderson 1932 (explained in
  words).
- "Spin ½ for any particle whose position is an observable" (stated).
- No calculation of any kind; no plane-wave solution; no non-relativistic limit
  (Pauli equation); no g = 2.
**Scaffolding share**: ~50% (single voice, but "the arc of the site" framing is
  heavy).
**Missing for the target reader**
- The equation, and the derivation route a linear-algebra reader can follow: demand
  (E − cα·p − βmc²)ψ = 0 square to E² = p²c² + m²c⁴ ⇒ α_i, β anticommute and square
  to 1 ⇒ smallest matrices are 4×4 ⇒ four components. This is exactly the 11-chapter
  Pauli-matrix argument scaled up; it is the payoff of the whole book and is missing.
- The non-relativistic limit worked (or sketched) giving the Pauli term
  −(eℏ/2m)σ·B and hence g = 2: the "spin for free" claim shown, not told.
- Plane-wave solutions at rest: two with E = +mc², two with E = −mc² — where the
  four components go.
- Modern reading of the sea (antiparticles in QFT) in one sentence, so the reader is
  not left with the 1930 picture as final.
- Numbers: positron mass, pair-production threshold 1.022 MeV; fine-structure scale
  α² ~ 5×10⁻⁵ of hydrogen levels (why relativity matters in atoms).
**Proposed spine**: "What happens when you insist Schrödinger's equation respects
  relativity?" Try the square-root Hamiltonian, reject it; demand linearity and squaring
  to E² = p²c² + m²c⁴; derive the anticommutation algebra and the 4×4 size; write the
  equation; solve at p = 0 (four solutions, two negative-energy); take the low-speed
  limit in a magnetic field to exhibit the spin term and g = 2; check the non-
  relativistic limit recovers Schrödinger; end with the positron and 1.022 MeV.
**Keep**: "spin was grafted on; here it is forced"; the hole argument; Anderson.
**Cut**: "arc of the whole site" synthesis; the GR-not-united coda (already in A3).
**Add**: the equation, the anticommutation derivation, rest solutions, Pauli limit,
  numbers; problems (verify (α·p)² = p² given the algebra; threshold energy for pair
  production).
**Dependencies**: 11 (Pauli matrices — which 11 never writes), A2 (E² = p²c² + m²c⁴ —
  which A2 never writes), 12 (exclusion principle for the sea), 06 (Schrödinger).

---

# Top-level

## Overall state

All 18 chapters are book-comparison essays, not physics essays. Averaged across the
book, roughly 50–60% of the body text is about the four (or two, or one) sources;
the remainder is précis-level physics — concepts named and glossed, almost nothing
derived, and NOT ONE worked instance with numbers or explicit vectors anywhere in the
18 chapters. Key formulas the reader would expect are absent from the whole book:
Planck's law, Einstein's photoelectric equation, the Compton shift, the Bohr energy,
the Rydberg formula, the infinite-well levels, the Pauli matrices, first-order
perturbation formula, the Lorentz transformation, the Dirac equation. The rewrite is
therefore not a trim; every chapter needs its physics core written fresh, and the
existing text supplies at most the hook and a few well-put sentences.

Content errors/traps to fix in the rewrite:
- 10: E_n = −mα²/2ℏ²n² with α = Coulomb coupling, unlabelled; reads as fine-structure α.
- 05: Dirac's dv/dt = [v,H] printed as if a commutator; missing the 1/iℏ.
- 07: h, ℏ/2 and "≳" used interchangeably without comment.
- A1/A2: relativistic-mass convention m = m₀/√(1−v²/c²), obsolete and confusing.
- 14: Born's "causality empty" argument as glossed is logically loose.
- 09: title says "Wells" but no bound-state well appears.

Gaps in the book as a whole (no chapter covers them, several rely on them):
- Angular momentum operators, l(l+1)ℏ², m — needed by 10, 11, 12; never introduced.
- Expectation values and the general uncertainty relation — used in 07, defined nowhere.
- Tensor product / two-system states — needed by 12, 14; never introduced.
- Stationary states and separation of variables — needed by everything from 09 on;
  06 does not do it.
- de Broglie relation — assumed from 04 onward; never actually introduced.
- The harmonic oscillator — the standard worked system, absent entirely (could live in
  05 or 09).

## Does the order still work?

Mostly yes for Part I and Part III; Part II is out of order for a rusty reader once
the comparison is gone. Proposed sequence:

1. 01 Blackbody — keep first.
2. 02 Photons — keep; add de Broglie at the end (bridge to 04).
3. 03 Bohr — keep; it becomes the first real worked calculation. Short.
4. 04 Amplitudes/double slit — keep.
5. 06 Wavefunction & Schrödinger — MOVE BEFORE 05 and 07; it defines ψ, stationary
   states, packets, which 05 and 07 need.
6. 08 Formalism (states, operators, expectation values) — MOVE BEFORE 07; 07's sharp
   inequality needs it.
7. 07 Uncertainty — after 06 and 08.
8. 05 Two mechanics — MERGE INTO 08 or DROP as a standalone chapter. Its physics
   (matrix = operator in a basis; Heisenberg vs Schrödinger picture) is one section of a
   formalism essay; its history is one paragraph. Reason: as a standalone it has no
   spine once "who lived through 1925" is gone.
9. 09 Wells/barriers — keep; add the bound-state wells at the front. Consider adding the
   harmonic oscillator here.
10. NEW short section or chapter: angular momentum (or fold into 10 as its first
   section). Reason: 10, 11, 12 all use l, m, s without definition.
11. 10 Hydrogen — keep.
12. 11 Spin — keep.
13. 12 Identical particles — keep.
14. 13 Approximations — keep; rename "Perturbation theory and helium" (it does not cover
   WKB/variational unless added).
15. 14 Measurement — keep last of the QM part; becomes a short calculational essay on
   entanglement with a detector, not a philosophy survey.
16. A1, A2 — keep; A2 could be merged into A1 as one "Special relativity" essay (both
   are thin; together they make one normal-length essay with γ, the transformation,
   E = γmc², and the muon + helium mass-defect examples). Reason: neither has enough
   physics for a chapter alone.
17. A3 — keep short; it is honestly a sketch. Could be dropped without loss to the QM
   thread; keep only if the redshift/GPS numbers are added.
18. A4 Dirac equation — keep as the finale; it is the only place the appendix earns its
   place in a quantum book. Consider moving A1+A2 to sit directly before it (i.e. after
   14) and dropping A3, so the tail reads: measurement → special relativity → Dirac
   equation.

Alternative if the relativity appendix is unwanted: move a one-page relativistic-
kinematics reminder into 02 (Compton needs it) and into A4, drop A1–A3.

## Closest to / furthest from a proper essay

Least work (already have a physical argument the reader can follow; need formulas and
one worked instance added, framing stripped):
- 04 Amplitudes (the three rules and the which-path criterion are there; add the
  explicit |a₁+a₂|² and a number).
- 09 Tunnelling (structure of D, e^{−2κa}, alpha decay all present; add the matching and
  numbers).
- 12 Identical particles (the ± derivation and the determinant argument are there).
- A1 Special relativity (simultaneity argument is good; add γ and the transformation).
- A3 GR (already single-voice; add two numbers).

Middle: 06, 07, 08, 10, 11, 14, A4 — decent hooks and some correct statements, but the
core calculation must be written from nothing.

Most work (almost no physics, mostly meta-commentary on the sources; essentially
rewrite from a blank page keeping only the title and hook):
- 01 Blackbody (Planck's law absent).
- 02 Photons (no equations).
- 03 Bohr (no derivation).
- 05 Two mechanics (no spine without the history; merge into 08).
- 13 Approximations (no formula at all; "interest is in stance rather than result").
- A2 Mass–energy (thin, obsolete convention).
