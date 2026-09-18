# Rework plan — from "The Quantum Quartet" to a readable guide to quantum mechanics

Status: **merged plan, 2026-09-18. The single authority for the rework.** It combines two
earlier drafts (an editorial plan and an evidence-based plan); the editorial draft has been
deleted so nothing stale can be followed. Supporting evidence, per chapter:
`notes/rework-survey.md`. Yardstick for the essay shape: `~/book2`
(e.g. `chapters/07-entanglement-schmidt.html`). Progress: pilot 1 (Blackbody) drafted and **approved by the user as the template**
(2026-09-18: "very readable", proceed the same way); pilot 2 (Double slit) approved; Part I (Photons, Bohr) drafted; Part II (05 Representations, 06 Wavefunction, 08 Formalism, 07 Uncertainty) drafted 2026-09-18; structure approved by the user, scientific wording pass done. Part III (09, new 09b oscillator, new 09c angular momentum, 10–14) drafted 2026-09-18; precision pass after user review done; continuous read of all 16 done (17 issues fixed: fold-out dependencies, undefined terms, symbol clashes, essay nicknames). Essential step 8 done (index, about, README, CONTEXT). Source levels: notes/source-ledger.md. Optional essays a1–a4 rewritten 2026-09-18 (scripts/aN_*.py); their claims under fact-check. Numbers and figures: `scripts/chNN_*.py`; page checks: `scripts/check_page.py`.

## 1. The decision

Remove the four-way comparison of Born, Feynman, Landau & Lifshitz and Dirac as the
organising principle. Each chapter becomes a self-contained educational essay on its
physics. The books survive in two places only: an occasional attributed aside where one
treatment is genuinely the clearest way in, and a short verified "Further reading" note at
the end (no obligation to mention every book).

**Governing principle: one central question per essay, enough mathematics to answer it,
optional depth beyond that.** When a chapter brief below conflicts with this, the principle
wins and the excess moves to an optional branch. Several briefs hold more than one essay's
worth of material; density is the main risk of this rework.

Why. About half to two thirds of each current chapter is about the books, not the physics.
Across all eighteen chapters there is no worked instance with a number and a unit, and the
formulas a reader would expect (Planck's law, the photoelectric equation, the Compton shift,
Bohr's energies, the infinite-well levels, the Pauli matrices, first-order perturbation
theory, the Lorentz transformation, the Dirac equation) are absent. Removing the comparison
tables leaves holes; this is a rewrite of each chapter's core, keeping hooks and good
sentences, not a trim.

## 2. The reader

An adult with university mathematics and a physics course about twenty years ago. Recognises
derivatives, integrals, vectors, waves, energy and probability but may not remember how to
use them. Complex numbers, differential equations, matrix operations, Hamiltonians, Fourier
transforms and most notation need a gentle reintroduction. No prior quantum mechanics. Not
sitting an exam; wants to understand, and to follow a calculation when one is shown.

The reader's job: "When I return to physics after a long absence, I want to rebuild the
ideas and mathematics together, so I can understand what quantum mechanics predicts and
follow why those predictions make sense."

Progress means being able to explain a physical distinction, interpret a diagram or
equation, and make a small prediction. These are working assumptions, to be tested on the
two pilot chapters.

## 3. Editorial agreement

- One patient adult voice. Assume intelligence and rusty recall. Never "obviously",
  "simply", or any suggestion the reader should already know something.
- Start with something to explain: an observation, a prediction that fails, a useful
  question. History enters when it clarifies that question.
- The essay carries the argument in connected prose with descriptive headings. Do not turn
  every paragraph into a box, quiz or list.
- Keep equations that do explanatory work. Every symbol is named at first use; assumptions
  are stated; an important equation is followed by what it lets us predict. Formulas that
  are cited rather than derived are labelled as such.
- **Reminders are short and skippable** (3–6 lines near the top, only the tools this essay
  uses). More substantial refreshers sit beside the step that needs them.
- **Numerical constants are introduced where they are first calculated with**, with units,
  not listed at the top. Shared values live in one constants table (§9) so no chapter
  invents its own rounding.
- **Longer derivations are optional branches** (`<details>`), placed after the necessary
  explanation. Skipping one must never break the next chapter.
- Original diagrams and independently written worked reasoning. No reproduced textbook prose
  or figures. The content policy is clarified to permit original educational derivations.
- Length: usually 1,400–2,200 words of main essay, shorter for historical chapters.
  Readability beats the quota.
- Banned in new prose: "the four authors", "our four books", "the course", "entry points",
  any sentence about which treatment is more elegant, author-personality generalisations,
  grand closing paragraphs.

## 4. The essay template

Reading flow: physical question → enough recalled physics/maths → new idea → worked
consequence → what it explains and where it stops → bridge. An editorial guide, not a rigid
set of identical visible headings.

1. **Opening question** — one paragraph; concrete and answerable. "Why does a hot poker
   glow red, then white, never violet?" Not "In this chapter we consider…".
2. **Reminders** — short, skippable block.
3. **Set-up** — the system, the assumptions, the notation. Define before calculating.
4. **The physics** — why each equation follows; what each term predicts.
5. **A worked example** — reproducible line by line, units throughout where quantities are
   physical. An explicit two-state calculation counts; a physical number is not mandatory
   in every chapter.
6. **A check** — a classical limiting case where natural; otherwise a consistency check or
   a counterexample to a tempting overclaim.
7. **One original figure** (usually) — makes a specific relationship easier to see; has a
   usable text explanation; works in light, dark and print.
8. **Optional branch(es)** — longer derivation(s) in `<details>`.
9. **Two worked questions** in `<details>` — one varies the example or an assumption; one is
   conceptual, exposes a distinction, and its answer includes help for a plausible wrong
   turn. Two, not four.
10. **Further reading** — short, verified, chosen for usefulness.
11. **Bridge** — the final paragraph explains why the next essay follows.

**Lessons from the pilot review (2026-09-18). The Double slit essay is the model for the rest.**
- *Concrete progression and an observable number.* Build from familiar cases to the new
  one (bullets → water waves → electrons), and tie the new idea to something
  measurable (a 0.61 mm fringe spacing). A memorable one-line statement of the puzzle helps
  ("opening a second door reduces the traffic").
- *Reminders only for what the reader has genuinely met before.* Ideas that are likely new
  to this reader (the Boltzmann factor, equipartition, the work function) are introduced
  in the text at the step that needs them, not in the reminders box.
- *Show the thing to be explained early* (the spectrum figure now opens the blackbody
  essay; the classical calculation is then read against it).
- *Selective depth.* State and use a result in the main path; put its derivation in a
  fold-out (Wien's 4.965). A noticeable jump in difficulty (the partial which-path record
  with γ, δ) is explained in words in the main path, with the algebra as an extension.
  Both questions must be answerable without opening any fold-out.
- *Say exactly what a plotted or computed quantity is* (a probability per fixed-width
  detector window; same incident beam for every comparison), so normalisation never
  becomes a later confusion.
- *Do not let an answer reinstate a picture the essay has argued against* (loss of
  interference is set by the distinguishability of the records, not by a mechanical kick).
- *State the scope of every general claim* (Part II review): rules are for ideal
  measurements with distinct results; non-commuting operators cannot share a complete set of
  eigenstates, but may share some, so "no state is sharp in both" is said only where true
  (x and p, the photon's H/V and D/A); stationary states are permanent only in the isolated
  fixed-potential model, and excited atoms decay by spontaneous emission; order-of-magnitude
  estimates are labelled as estimates of scale and mechanism, not derivations.
- *Opening and ending must match exactly* (the poker question now asks what the ending
  answers).
- *Presentation:* figures sit in a `.fig-scroll` wrapper so labels keep their designed size
  on phones; fold-outs open when printing (a `beforeprint` handler plus print CSS).
  `scripts/check_page.py` checks label size at phone width and that every fold-out reaches
  the printed PDF.

Each brief below names a **Reader can** outcome: the thing the reader should be able to do
afterwards. Math in KaTeX as now.

## 5. Sequence

File names and URLs are **kept**; only prev/next links, the index map and displayed order
change. **Numbers are dropped from titles**; order is carried by the index map and prev/next.
Part II is reordered so ψ, operators and expectation values are defined before they are
used: a reader should never need a forward link to a chapter they have not reached.

| Order | File | Working title | Action |
|---|---|---|---|
| 1 | `01-blackbody-planck.html` | Why hot objects forced physics to change | rewrite · **pilot** |
| 2 | `02-photons.html` | Light arrives in individual events | rewrite, + de Broglie as closing move |
| 3 | `03-bohr-atom.html` | The atom that almost worked | rewrite, compact |
| 4 | `04-quantum-behavior.html` | How alternatives interfere | rewrite · **pilot** |
| 5 | `05-two-mechanics.html` | One state, different ways to describe it | rewrite as intuitive on-ramp |
| 6 | `06-wavefunction.html` | What a wavefunction tells us | rewrite |
| 7 | `08-dirac-formalism.html` | A practical language for quantum states | rewrite, **moved before uncertainty** |
| 8 | `07-uncertainty.html` | Why localization has a cost | rewrite, **moved after formalism** |
| 9 | `09-wells-tunneling.html` | Confinement and tunnelling | rewrite, + bound wells |
| 10 | `09b-oscillator.html` | The harmonic oscillator (short) | **new** |
| 11 | `09c-angular-momentum.html` | Angular momentum (short) | **new** |
| 12 | `10-hydrogen.html` | Hydrogen without little planetary orbits | rewrite |
| 13 | `11-spin.html` | Spin: a two-state quantum system | rewrite |
| 14 | `12-identical-particles.html` | Why identical particles change matter | rewrite |
| 15 | `13-approximations.html` | How to calculate when exact solutions run out | rewrite |
| 16 | `14-measurement.html` | What measurement predicts — and what it leaves open | rewrite; **core book ends here** |
| opt | `a1-special-relativity.html` | Events, clocks, and spacetime | rewrite, optional |
| opt | `a2-mass-energy.html` | Energy, momentum, and mass | rewrite, optional |
| opt | `a3-general-relativity.html` | Gravity as geometry: a short excursion | rewrite, optional excursion |
| opt | `a4-dirac-equation.html` | Toward relativistic quantum mechanics | rewrite, optional finale |

Relativity is labelled optional and sits outside the core sequence. A1 → A2 → A4 is the
path toward relativistic quantum mechanics; A3 is a separate excursion and not a
prerequisite for A4. A3's place does not depend on it containing a numerical calculation,
though a meaningful one would help.

## 6. Known problems to fix

Verified by direct check of the HTML, not only by the survey. Classified.

**Confirmed errors / obsolete conventions**
- Relativity appendix uses the relativistic-mass convention. Drop it: mass is invariant,
  E = γmc², p = γmv.
- README and CONTEXT.md describe most chapters as unwritten; all eighteen contain prose.

**Ambiguous notation (correct but dangerous)**
- Hydrogen: `E_n = −mα²/2ħ²n²` is printed before `V = −α/r` is introduced, and α is never
  distinguished from the fine-structure constant. **Avoid the letter altogether**: write
  the constants out (e²/4πε₀) or use an explicitly defined Coulomb coefficient with a
  non-colliding symbol. α is reserved for the fine-structure constant if it appears at all.
- Two Mechanics: `v̇ = [v, H]` is right for Dirac's quantum Poisson bracket (iħ absorbed)
  but reads as a missing 1/iħ. Write the commutator explicitly: `dv/dt = (1/iħ)[v, H]`.
  This equation and its explanation live in the Formalism essay (optional section) only.
  Essay 5 stays genuinely intuitive and contains no commutators; nothing is kept there
  merely because it appeared in the old chapter.
- Uncertainty: h, ħ/2 and "≳" are mixed without saying which relation is meant.

**Missing explanations**
- No number with a physical unit in the body text of any chapter.
- Planck's law is never written in the blackbody chapter. "Wells" contains no bound well.
- Δx and Δp are never defined (uncertainty).
- Relied on but introduced nowhere: see the gaps table, §7.

**Passages flagged for targeted review, not to be carried into new prose unchecked**
- 01: historical chronology. 02: claims about the development of quantum field theory.
  07: descriptions of uncertainty versus disturbance. 14: necessity claims about a
  measurement jump. A3: the local-versus-global equivalence argument. A4: claims about what
  relativity alone forces. Avoid broad claims about what an entire book does not cover
  unless needed and verified.

## 7. Whole-book gaps and where each now lives

| Gap | Introduced in |
|---|---|
| de Broglie λ = h/p | Photons (closing), used from the double slit on |
| state versus its coordinates; amplitudes as components | One state, different descriptions |
| probability density, normalisation, stationary states, separation of variables | Wavefunction |
| kets, inner product, eigenbasis, Born probabilities, expectation value | Formalism |
| Δ as standard deviation; Fourier pair; commutator form | Uncertainty |
| bound wells | Confinement and tunnelling |
| harmonic oscillator, (n+½)ħω | Oscillator (new) |
| angular momentum operators, l(l+1)ħ², m | Angular momentum (new) |
| tensor product, two-system states | Identical particles (product functions), Measurement (system + detector) |
| relativistic E–p relation | stated in Photons, derived in A2 |

## 8. Chapter briefs

Format: question · reminders · main path · optional branch · worked example · figure ·
reader can · bridge · keep. **All proposed numbers are targets to be computed and checked
before publication, not verified facts.**

**Blackbody** (`01`, pilot, most work). *Why does a hot poker glow red, then white, never
violet?* · Reminders: frequency, wavelength and energy of a wave; equipartition; Boltzmann
factor. · Main: what a spectrum plots (labelled axes, units), what temperature changes, the
cavity, why the classical prediction fails, energy quanta as the new ingredient, Planck's
law written and read term by term, Rayleigh–Jeans and Wien as its two limits. · Optional:
mode counting; the oscillator average. · Worked: Sun at 5800 K → peak near 500 nm; energies
of two quanta of different frequency, in eV. · Figure: spectra at two temperatures with the
classical curve diverging. · Reader can: explain what a spectrum measures and what problem
quantisation solves. · Bridge: is the discreteness only in matter exchanging energy, or in
light itself? · Keep: cavity set-up, equipartition paragraph.

**Photons** (`02`, most work). *Why does blue light eject electrons from sodium when red
cannot, however bright?* · Reminders: E = hν; electronvolt; p = E/c for light; relativistic
E–p relation stated (derived in A2). · Main: intensity versus frequency separated;
K_max = hν − W; Compton as second evidence; de Broglie λ = h/p as the closing move. ·
Optional: the full Compton collision calculation, Δλ = (h/m_e c)(1 − cos θ), checked at
θ = 0 and 180°. · Worked: energy budget with sodium's work function, all units shown. ·
Figure: threshold graph (K_max against ν). · Reader can: predict the effect of changing
frequency or intensity. · Bridge: atoms also absorb and emit selected energies. · Keep: the
photoelectric narrative.

**Bohr** (`03`, compact). *Why does hydrogen emit only certain colours?* · Reminders:
Coulomb force, circular orbit, L = mvr, negative binding energy. · Main: spectral lines, the
classical atom's failure, two postulates → r_n, E_n = −13.6 eV/n², Rydberg formula; what the
model explains and where it stops. · Optional: large-n orbital frequency matches the
classical one (correspondence). · Worked: Hα at 656 nm from E₃ − E₂. · Figure: energy-level
diagram. · Reader can: connect an energy difference with a photon, and say why a correct
spectrum does not establish literal orbits. · Bridge: what can replace a trajectory? ·
Keep: "scaffold, not building" as one sentence.

**Double slit** (`04`, pilot, least work). *If an electron is a particle, why fringes?* ·
Reminders: complex numbers as arrows, phase, |z|²; λ = h/p in one line. · Main: individual
detections, the accumulated distribution, amplitude introduced through the example before
the general rule, expand |a₁+a₂|² to the cosine term, what path information does. ·
Optional: bracket factorisation in general. · Worked: two alternatives adding and
cancelling at a chosen point; fringe spacing λL/d for a 100 eV electron. · Check: a
which-path factor kills the cross term and restores the sum of probabilities. · Figure:
detection distributions with and without path information. · Reader can: explain why adding
probabilities and adding amplitudes predict different things. · Bridge: how do we describe
all the possibilities in a state? · Keep: the three rules, bracket factorisation, which-path
criterion — the best physics in the book now.

**Representations** (`05`). *Is a state the same thing as the numbers we use to describe
it?* · Reminders: a two-component vector. · Main: an ordinary vector along different axes;
a simple quantum state as a short list of amplitudes; the wavefunction previewed as the
continuous version; historical convergence of matrices and waves as a short closing note. ·
Deferred to Formalism, none of it appears here: bra-ket notation, proof of equivalence,
commutators and the equation of motion. · Worked: one state,
two bases, same probabilities for the same question. · Figure: change-of-axes drawing. ·
Reader can: distinguish a state from its coordinates. · Bridge: what does a position-based
description look like?

**Wavefunction** (`06`). *What does the wave tell us, and what equation does it obey?* ·
Reminders: area under a curve, derivatives and curvature, complex exponentials. · Main:
probability density, normalisation and phase first; then the Schrödinger equation read term
by term (plane wave → p = −iħ∇), as a motivated equation, not a derivation; stationary
states gently. · Optional: separation of variables; Gaussian packet spreading with numbers
and the large-mass limit. · Worked: normalise a simple ψ and find the probability in an
interval. · Figure: ψ and |ψ|² with distinct labels. · Reader can: use a density to reason
about probability in an interval and say what the evolution equation is for. · Bridge: we
need a compact language for states and measurements. · Keep: Born-rule paragraph.

**Formalism** (`08`, now before uncertainty). *What does "in a state" mean, and what does a
measurement give?* · Reminders: eigenvectors and eigenvalues, Hermitian means real
eigenvalues, inner product. · Main: reuse the Representations two-state example to introduce
kets, bras, inner products, operators, eigenstates, expectation values, in that order;
average versus individual outcome; translate back to ψ(x). · Optional: "matrices and waves
are one theory", with `dv/dt = (1/iħ)[v, H]`. · Worked: an explicit 2×2 Hermitian matrix —
eigenvectors, probabilities |⟨i|ψ⟩|², ⟨A⟩, including the matrix multiplication. · Check:
the eigenstate case gives a certain outcome. · Support: notation translation sheet. ·
Reader can: read a simple state, get normalised probabilities, compute an expectation value.
· Bridge: can one state have sharp position and sharp momentum? · Keep: ket/bra/projector
definitions.

**Uncertainty** (`07`, now after formalism). *Why doesn't the electron fall into the
nucleus?* · Reminders: standard deviation; Fourier transform in one line. · Main: a packet
built from many wavelengths; Δx, Δp defined as standard deviations before the relation is
shown; diffraction; preparation, statistical spread and measurement disturbance separated;
one relation stated clearly (ΔxΔp ≥ ħ/2). · Optional: Gaussian pair gives exactly ħ/2; the
general operator proof (now legitimately available). · Worked: minimise ⟨p²⟩/2m − e²/4πε₀r →
a₀ and roughly −10 eV. · Check: a dust grain. · Figure: wave packet and its spectrum. ·
Reader can: say what both spreads mean and why a better instrument does not remove the
relation. · Bridge: apply all this to a confined particle. · Keep: single-slit picture.

**Confinement and tunnelling** (`09`). *How does an alpha particle leave a nucleus it lacks
the energy to leave?* · Reminders: standing waves, exponentials, constant-coefficient ODEs.
· Main: particle in a box, boundary conditions → discrete energies; finite barrier, what
transmission means, T ~ e^{−2κa}; **one** application (alpha decay), not a catalogue. ·
Optional: barrier matching algebra; finite-well shift; STM or ammonia as a second case. ·
Worked: how the box energy scale changes with width (electron in 1 nm). · Check: κa → ∞ and
E > U₀. · Figure: potential, state and energy, unambiguously labelled. · Reader can: predict
the direction of change when confinement tightens or a barrier widens. · Bridge: the most
useful well of all. · Keep: alpha-decay / Geiger–Nuttall narrative.

**Oscillator** (`09b`, new, short). *Why does a vibrating molecule never quite stop?* ·
Reminders: spring potential ½mω²x². · Main: energies (n+½)ħω, zero-point energy, evenly
spaced levels; link to Planck's quanta in essay 1. · Optional: ladder operators. · Worked:
level spacing for a diatomic molecule in eV. · Check: large n recovers classical turning
points. · Reader can: state the spectrum and why the ground energy is not zero. · Bridge:
rotation is quantised too.

**Angular momentum** (`09c`, new, short). *Why do orbits come in the sizes they do?* ·
Reminders: polar coordinates; rotation as a phase. · Main: a physical motivation first;
L_z = −iħ∂_φ with eigenvalues mħ; L² eigenvalues l(l+1)ħ² stated; the (l, m) table. ·
Optional: ladder sketch. · Worked: list the states for l = 1 and their L_z values. ·
Reader can: read l and m and say what each fixes. · Bridge: put this into the Coulomb
potential.

**Hydrogen** (`10`). *Why is hydrogen's spectrum exactly the Balmer series?* · Reminders:
reduced mass; Laplacian in spherical coordinates (stated). · Main: return to Bohr's spectrum
with states in a Coulomb potential; energy levels and spatial distributions answer different
questions; ranges of n, l, m; Coulomb constants written out as e²/4πε₀ (no bare α). · Optional: separation
of variables, special functions. · Worked: solve the l = 0 ground state by trying e^{−r/a} →
a₀, −13.6 eV; revisit Hα. · Check: ⟨r⟩ ~ n²a₀, large n. · Figure: energy diagram plus a
radial distribution. · Reader can: distinguish an orbital, an energy level and a trajectory.
· Bridge: atomic observations need another degree of freedom. · Keep: Balmer-as-difference,
degeneracy n².

**Spin** (`11`). *Why does a silver beam split into exactly two?* · Reminders: magnetic
moment in a field gradient; 2×2 eigenproblems. · Main: idealised sequential analysers make
the formalism physical; limits of the rotating-ball picture; Pauli matrices; changing axes.
· Optional: Stern–Gerlach deflection numbers; the 2π sign flip. · Worked: probability
cos²(θ/2) for a tilted magnet, checked at θ = 0 and π/2. · Figure: sequential analyser
diagrams. · Reader can: predict outcomes for a sequence of ideal filters. · Bridge: several
identical particles. · Keep: "no classical picture" argument.

**Identical particles** (`12`, least work). *Why don't all electrons sit in the lowest
orbit?* · Reminders: product wavefunctions; exchange as a label swap. · Main: ψ_S and ψ_A
explicitly; ψ_A = 0 for equal orbitals; exclusion → shells, 2n² through Li, Ne, Na; limits
of the independent-electron picture. · Optional: helium ortho/para; general many-particle
formalism. · Worked: small orbital-filling example including spin. · Check: non-overlapping
particles behave as distinguishable. · Reader can: say what exclusion forbids and use it. ·
Bridge: interacting particles make exact calculation hard. · Keep: phase² = 1 argument,
determinant → exclusion, honest "spin–statistics not proved here".

**Approximations** (`13`, most work). *Helium has no exact solution; how close can we get?*
· Reminders: expanding in a small parameter; ⟨n|V|n⟩ as an integral. · Main: a weakly
perturbed two-state model, approximate versus exact; what "small" is relative to;
near-degeneracy breaking the series; variational idea as a shorter companion. · Optional:
derive E⁽¹⁾ = ⟨n|V|n⟩ by projection; WKB linked to tunnelling. · Worked: the 2×2 comparison;
helium −74.8 eV (first order) against −79.0 eV measured. · Check: V → 0. · Reader can:
identify an approximation's regime and know when to check it. · Bridge: probabilities still
leave a question about individual outcomes.

**Measurement** (`14`). *What does the equation say when a detector clicks?* · Reminders:
tensor product of two states; inner product of detector states. · Main: return to the double
slit and spin filters; operational rules separated from interpretive claims; a small
entangled system first; spin-½ plus two-state detector, cross term multiplied by ⟨A_↑|A_↓⟩,
the macroscopic limit; decoherence with its scope stated; one honest paragraph on what
remains open. · Optional: brief, even-handed interpretation summaries. · Reader can:
distinguish a predicted probability, an observed outcome, and an interpretation. · Ends the
core book with questions the reader can now approach and specific optional next steps. ·
Keep: two-kinds-of-evolution framing, which-path link back to the double slit.

**A1 Events, clocks, spacetime** (optional). *How does a 2.2 μs muon reach the ground from
15 km up?* · Light-clock γ, simultaneity, Lorentz transformation, spacetime diagram. ·
Worked: the muon. · Keep: the simultaneity argument.

**A2 Energy, momentum, mass** (optional). E = γmc², p = γmv, low-speed expansion,
E² = p²c² + m²c⁴; invariant mass only. · Worked: helium mass defect; 1 g ↔ 9×10¹³ J. ·
Keep: sticky-collision argument.

**A3 Gravity as geometry** (optional excursion). Local free fall, then tidal effects, to
show the scope and limits of the equivalence argument; no tensor calculus. · Worked, if it
earns its place: gravitational redshift gh/c², Pound–Rebka or the GPS clock offset.

**A4 Toward relativistic quantum mechanics** (optional finale). *What happens when
Schrödinger's equation must respect relativity?* · Main: the electron problem, linearising
the square root, why matrices appear, spin "for free", g = 2, negative-energy solutions,
positron, 1.022 MeV threshold; hole theory separated from the later field description. ·
Optional extension: the full 4×4 construction and the Pauli limit. · Needs Pauli matrices
(Spin) and the E² relation (A2).

## 9. Process

1. **Pilots first:** Blackbody (restoring forgotten physics gently; most work) and Double
   slit (explaining a distinctly quantum idea; least work). The user reads both. The first
   review asks: was it interesting, where did you have to stop, could you explain the worked
   result afterwards? The template is adjusted here before anything else is written.
2. **Then in reading order**, because later essays depend on earlier definitions: rest of
   Part I → Part II → Part III → optional relativity → site reconciliation.
   **Checkpoints with the user:** after this merge, after each pilot, after each Part. After
   each Part, a continuous read for repeated introductions, missing prerequisites and
   notation drift.
3. **Who writes.** Judgment-heavy drafting is done by the main session, one chapter at a
   time. Mechanical passes (nav rewiring, phrase sweeps, constants consistency) may be
   delegated.
4. **Never false.** Born (full text), Dirac (PDF) and Landau & Lifshitz (PDF) are verified
   copies (paths in CONTEXT.md). Every formula and number in a new essay is computed
   independently and checked against one of them or a standard reference before the chapter
   is marked done. Feynman stays link-only, never mirrored. **Existing source notes are
   evidence to review, not text to freeze:** rewritten content needs references that match
   what it now teaches, and no pointer ships unverified.
5. **Quantitative figures are generated from the checked calculations**, not drawn by eye.
   Each records the plotted quantity, its units, the parameters, and the axis choice (for
   blackbody curves: frequency or wavelength, with the matching form of Planck's law — the
   two peak at different places). The small generation and checking scripts are kept in
   the repository (`scripts/`) so every number and illustration is reproducible.
   Schematic figures (apparatus, change of axes) may be hand-written SVG.
6. **Shared constants table** (ħ, h, e, m_e, ε₀, k_B, c, a₀) in this folder, one rounding.
7. **Do not:** restore the entry-points table or per-author sections; add sources that are
   not on disk or link-verified; mirror Feynman.

## 10. A chapter is ready when

1. Its opening poses a physical question that its ending actually answers.
2. The main argument can be followed without knowing the source books and with every
   optional branch closed.
3. New terms and symbols are defined before use; reminders are where they are needed.
4. Its worked example is reproducible, independently checked (script in `scripts/`), and
   says what the result means.
5. Its figure makes a specific relationship easier to understand and has a text explanation;
   a quantitative figure is script-generated with quantity, units and parameters recorded.
6. Its two questions have reasoning-based answers, including help for a plausible wrong turn.
7. **Its final paragraph explains why the next essay follows**; the core ending and the
   optional branch are explicit.
8. References and historical claims are checked or omitted; nothing survives merely because
   it was in the old version. None of the banned phrases appear.
9. `python3 scripts/check_page.py <chapter>` passes (banned phrases, KaTeX errors, no display
   equation wider than the column at desktop or phone width: break long ones with `aligned`).
10. The page is checked for narrow-screen reading, KaTeX rendering, keyboard access to
   disclosures, light/dark figure, print, and working prev/next links.

## 11. Site changes (after the chapters)

- `index.html`: reader promise, a short starting note, a chapter map described by physical
  questions in the new order, core versus optional.
- `about.html`: assumed background, main versus optional material, source use, scope;
  bibliography and editions stay here; content policy clarified.
- A small shared notation/refresher page holding only what rewritten chapters actually
  introduced (units and eV; frequency and wavelength; complex numbers and phase; density and
  normalisation; derivatives and curvature; standard deviation; vectors, matrices,
  eigenvectors, inner products). Nobody needs a preliminary maths course to start essay 1.
- `static/style.css`: only what the essays need (reminders, worked example, optional branch,
  figures). Keep the restrained reading layout. No framework, no interactive simulations.
- `README.md`, `CONTEXT.md`: new premise and true completion status; keep the source records.

## 12. Still open

- **Title.** "The Quantum Quartet" names the comparison being removed. Decide after the
  pilots. Candidate: "Quantum Mechanics, Revisited".
