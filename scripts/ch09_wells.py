#!/usr/bin/env python3
"""Chapter 09 (confinement and tunnelling): checked numbers and the generated figure.

    python3 scripts/ch09_wells.py            # print the numbers used in the essay
    python3 scripts/ch09_wells.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:wells
markers in chapters/09-wells-tunneling.html.

FIGURE RECORD
  Left panel  : infinite square well of width L. Levels E_n = n^2 E_1 for n = 1, 2, 3, drawn to
                scale; on each level the stationary state phi_n(x) = sin(n pi x / L) is drawn
                (arbitrary amplitude, zero line at the level).
  Right panel : rectangular barrier, height U0, width a, with E = 0.5 U0 and kappa a = 2.0
                (units hbar = 2m = 1). Re psi is the EXACT stationary solution for a wave
                arriving from the left, from the transfer-matrix matching below; the
                transmitted wave's amplitude is sqrt(T), with T printed by this script.
"""
import cmath
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34
hbar = h / (2 * math.pi)
m_e = 9.1093837015e-31
eV = 1.602176634e-19
HBARC = 197.3269804  # MeV fm
MA = 3727.379        # alpha particle rest energy, MeV
COUL = 1.43996       # e^2/(4 pi eps0) in MeV fm


def box_E1(L, m=m_e):
    return (math.pi * hbar) ** 2 / (2 * m * L * L) / eV


def barrier(E, U0, a):
    """Exact transmission for a rectangular barrier, units hbar = 2m = 1 (so E = k^2).
    Returns T and a function giving Re psi(x) for an incident wave e^{ikx} from the left."""
    k = math.sqrt(E)
    q = cmath.sqrt(E - U0)            # imaginary inside when E < U0
    # region I: e^{ikx} + r e^{-ikx}; II: A e^{iqx} + B e^{-iqx}; III: t e^{ikx}
    # solve by matching at x = 0 and x = a
    e1, e2 = cmath.exp(1j * q * a), cmath.exp(-1j * q * a)
    eka = cmath.exp(1j * k * a)
    # from x=a: A e1 + B e2 = t eka ; iq(A e1 - B e2) = ik t eka
    # => A = t eka (1 + k/q) / (2 e1), B = t eka (1 - k/q) / (2 e2)
    Acoef = eka * (1 + k / q) / (2 * e1)
    Bcoef = eka * (1 - k / q) / (2 * e2)
    # at x=0: 1 + r = A + B ; ik(1 - r) = iq(A - B)  (with A, B per unit t)
    # => 2 = (A+B) + (q/k)(A-B) per unit t
    t = 2 / ((Acoef + Bcoef) + (q / k) * (Acoef - Bcoef))
    A, B = Acoef * t, Bcoef * t
    r = A + B - 1
    T = abs(t) ** 2

    def re_psi(x):
        if x < 0:
            return (cmath.exp(1j * k * x) + r * cmath.exp(-1j * k * x)).real
        if x <= a:
            return (A * cmath.exp(1j * q * x) + B * cmath.exp(-1j * q * x)).real
        return (t * cmath.exp(1j * k * x)).real

    def abs_psi(x):
        if x < 0:
            return abs(cmath.exp(1j * k * x) + r * cmath.exp(-1j * k * x))
        if x <= a:
            return abs(A * cmath.exp(1j * q * x) + B * cmath.exp(-1j * q * x))
        return abs(t)

    return T, abs(r) ** 2, re_psi, abs_psi


def gamow(Q, Zd, Ad):
    """Tunnelling exponent 2*gamma for an alpha of energy Q leaving a daughter (Zd, Ad)."""
    mu = MA * (931.494 * Ad) / (MA + 931.494 * Ad)
    R = 1.2 * Ad ** (1 / 3) + 1.2 * 4 ** (1 / 3)   # touching radius, fm
    rc = 2 * Zd * COUL / Q
    n = 20000
    integral = 0.0
    for i in range(n):
        r = R + (rc - R) * (i + 0.5) / n
        V = 2 * Zd * COUL / r
        integral += math.sqrt(max(0.0, 2 * mu * (V - Q))) / HBARC * (rc - R) / n
    return 2 * integral, R, rc, 2 * Zd * COUL / R, mu


def report():
    for L in (1e-9, 0.5e-9, 2e-9):
        E1 = box_E1(L)
        print(f"electron in box L = {L*1e9:.1f} nm: E1 = {E1:.3f} eV, E2 = {4*E1:.3f}, E3 = {9*E1:.3f};"
              f" 2->1 photon {3*E1:.3f} eV = {1239.84/(3*E1):.0f} nm")
    print()
    for kap_a in (0.5, 1.0, 2.0, 3.0, 5.0):
        U0, E = 2.0, 1.0
        kap = math.sqrt(U0 - E)
        a = kap_a / kap
        T, R, _, _ = barrier(E, U0, a)
        print(f"E = U0/2, kappa a = {kap_a}: exact T = {T:.4e}, R = {R:.4f}, T+R = {T+R:.6f}; e^(-2 kappa a) = {math.exp(-2*kap_a):.4e}; ratio = {T/math.exp(-2*kap_a):.3f}")
    T, R, _, _ = barrier(3.0, 2.0, 1.0)
    print(f"E = 1.5 U0 (above the barrier), k a ~ 1: T = {T:.3f}, R = {R:.3f}")
    print()
    kap = math.sqrt(2 * m_e * 4 * eV) / hbar
    print(f"electron under a 4 eV barrier: kappa = {kap*1e-9:.2f} per nm; factor per extra 0.1 nm of gap = e^(2 kappa 0.1nm) = {math.exp(2*kap*0.1e-9):.1f}")
    print()
    data = (("U-238", 4.27, 90, 234, 1.41e17), ("Po-212", 8.95, 82, 208, 2.99e-7))
    res = []
    for name, Q, Zd, Ad, thalf in data:
        g, R, rc, VB, mu = gamow(Q, Zd, Ad)
        v = math.sqrt(2 * Q / mu) * 2.998e23      # fm/s
        f = v / (2 * R)
        lam = f * math.exp(-g)
        print(f"{name}: Q = {Q} MeV, barrier top ~ {VB:.1f} MeV at R = {R:.2f} fm, exit point {rc:.1f} fm; 2*gamma = {g:.1f};"
              f" T = e^-{g:.1f} = {math.exp(-g):.2e}; knocks/s ~ {f:.1e}; predicted half-life {math.log(2)/lam:.2e} s vs measured {thalf:.2e} s")
        res.append((name, g, thalf, math.log(2) / lam))
    print(f"measured half-life ratio U/Po = {res[0][2]/res[1][2]:.1e}; predicted = {res[0][3]/res[1][3]:.1e}; energy ratio = {8.95/4.27:.2f}")
    # what the agreement rests on
    g0, R0, *_ = gamow(4.27, 90, 234)
    gE, *_ = gamow(8.95, 90, 234)
    print(f"energy alone (U-238's daughter, Q raised to 8.95 MeV): tunnelling factor changes by e^{g0-gE:.1f} = {math.exp(g0-gE):.1e}")
    gZ, *_ = gamow(8.95, 82, 234)
    print(f"then lowering the daughter charge 90 -> 82: a further e^{gE-gZ:.1f} = {math.exp(gE-gZ):.1e}")

    def gamow_R(Q, Zd, R):
        mu = MA * (931.494 * 234) / (MA + 931.494 * 234)
        rc = 2 * Zd * COUL / Q
        n = 20000
        return 2 * sum(math.sqrt(max(0.0, 2 * mu * (2 * Zd * COUL / (R + (rc - R) * (i + 0.5) / n) - Q))) / HBARC * (rc - R) / n for i in range(n))
    for dR in (-0.10, +0.10):
        g = gamow_R(4.27, 90, R0 * (1 + dR))
        print(f"U-238 with radius {100*dR:+.0f}% ({R0*(1+dR):.2f} fm): half-life changes by a factor {math.exp(g-g0):.2f}")


# ---------------------------------------------------------------- figure
W, H = 680, 330


def figure_svg():
    o = []
    a_ = o.append
    a_(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-wells-title fig-wells-desc">')
    a_('<title id="fig-wells-title">A particle in a box, and a wave meeting a barrier</title>')
    a_('<desc id="fig-wells-desc">Left: a box with vertical walls. Three energy levels at heights in the ratio 1 to 4 to 9, each carrying a standing wave with one, two and three half-wavelengths across the box. Right: a wave arriving from the left meets a raised flat barrier. Inside the barrier the wave dies away exponentially, and a much smaller wave emerges on the far side.</desc>')
    # left: box
    x0, x1, yb, yt = 40, 290, 290, 40
    a_(f'<path class="fig-axis" style="stroke-width:3" d="M{x0},{yt} V{yb} H{x1} V{yt}"/>')
    scale = (yb - yt - 20) / 9.5
    for n in (1, 2, 3):
        y = yb - n * n * scale
        a_(f'<path class="fig-axis" style="stroke-dasharray:4 4" d="M{x0},{y:.1f} H{x1}"/>')
        pts = " L".join(f"{x0+(x1-x0)*i/100:.1f},{y-16*math.sin(n*math.pi*i/100):.1f}" for i in range(101))
        a_(f'<path class="fig-curve fig-hot" d="M{pts}"/>')
        a_(f'<text class="fig-note" x="{x1+8}" y="{y+4:.1f}">n = {n}</text>')
    a_(f'<text class="fig-note" x="{(x0+x1)/2}" y="{yb+22}" text-anchor="middle">box of width L: energies 1 : 4 : 9</text>')
    # right: barrier (exact solution)
    U0, E = 2.0, 1.0
    kap = math.sqrt(U0 - E)
    a = 2.0 / kap
    T, _, re_psi, _ = barrier(E, U0, a)
    X0, X1 = 360, 660
    xs_lo, xs_hi = -9.0, a + 9.0
    sxb = lambda x: X0 + (X1 - X0) * (x - xs_lo) / (xs_hi - xs_lo)
    ybase, yU = 230, 150
    a_(f'<path class="fig-axis" style="stroke-width:2" d="M{X0},{ybase} H{sxb(0):.1f} V{yU} H{sxb(a):.1f} V{ybase} H{X1}"/>')
    a_(f'<text class="fig-note" x="{(sxb(0)+sxb(a))/2:.1f}" y="{yU-8}" text-anchor="middle">barrier</text>')
    yE = ybase - (ybase - yU) * E / U0
    a_(f'<path class="fig-axis" style="stroke-dasharray:4 4" d="M{X0},{yE:.1f} H{X1}"/>')
    a_(f'<text class="fig-tick" x="{X1}" y="{yE-14:.1f}" text-anchor="end">energy E</text>')
    n = 600
    pts = " L".join(f"{sxb(xs_lo+(xs_hi-xs_lo)*i/n):.1f},{yE-22*re_psi(xs_lo+(xs_hi-xs_lo)*i/n):.1f}" for i in range(n + 1))
    a_(f'<path class="fig-curve fig-hot" d="M{pts}"/>')
    a_(f'<text class="fig-note" x="{X0}" y="{ybase+22}">incoming and reflected</text>')
    a_(f'<text class="fig-note" x="{X1}" y="{ybase+22}" text-anchor="end">transmitted, T = {T:.3f}</text>')
    a_('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "09-wells-tunneling.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:wells generated by scripts/ch09_wells.py -->\n" + figure_svg() + "\n<!-- /FIGURE:wells -->"
    new, n = re.subn(r"<!-- FIGURE:wells.*?<!-- /FIGURE:wells -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:wells markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
