#!/usr/bin/env python3
"""Chapter 03 (Bohr atom): checked numbers and the generated figure.

    python3 scripts/ch03_bohr.py            # print the numbers used in the essay
    python3 scripts/ch03_bohr.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:levels
markers in chapters/03-bohr-atom.html.

Notation: the Coulomb constants are written out as e^2 / (4 pi eps0); the essay
never uses a bare alpha for them (alpha is the fine-structure constant).
Main text uses an infinitely heavy nucleus; the reduced-mass correction is
printed here and mentioned in one sentence.

FIGURE RECORD
  Plotted quantity : Bohr energy levels of hydrogen, E_n = -13.6 eV / n^2, n = 1..6 and n -> infinity
  Vertical axis    : energy in eV, linear, -14.5 to +0.8
  Arrows           : Lyman alpha (2 -> 1) and the first four Balmer lines (3,4,5,6 -> 2),
                     labelled with wavelengths computed from the level differences
"""
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34        # J s
hbar = h / (2 * math.pi)
c = 299792458.0           # m / s
e = 1.602176634e-19       # C
eps0 = 8.8541878128e-12   # F / m
m_e = 9.1093837015e-31    # kg
m_p = 1.67262192369e-27   # kg
eV = e

K = e**2 / (4 * math.pi * eps0)          # J m, the Coulomb coefficient
A0 = hbar**2 / (m_e * K)                 # Bohr radius, m
RY = K / (2 * A0)                        # J, 13.6 eV
HC_EVNM = h * c / eV * 1e9


def E(n):
    return -RY / eV / n**2


def lam_nm(ni, nf):
    return HC_EVNM / (E(ni) - E(nf))


def report():
    print(f"e^2/(4 pi eps0) = {K:.4e} J m = {K/eV*1e9:.4f} eV nm")
    print(f"hbar = {hbar:.4e} J s")
    print(f"a0 = {A0*1e9:.5f} nm")
    print(f"E1 = {E(1):.4f} eV")
    for n in (1, 2, 3):
        v = n * hbar / (m_e * n * n * A0)
        print(f"n={n}: r = {n*n*A0*1e9:.4f} nm, v = {v:.4e} m/s = c/{c/v:.1f}, E = {E(n):.3f} eV")
    print(f"R_inf = {RY/(h*c):.6e} 1/m")
    for ni, name in ((3, "H-alpha"), (4, "H-beta"), (5, "H-gamma"), (6, "H-delta")):
        print(f"{name}: {ni}->2  dE = {E(ni)-E(2):.4f} eV  lambda = {lam_nm(ni, 2):.1f} nm")
    print(f"Balmer series limit: {HC_EVNM/(-E(2)):.1f} nm")
    print(f"Lyman alpha 2->1: {lam_nm(2, 1):.1f} nm, dE = {E(2)-E(1):.3f} eV")
    mu = m_e * m_p / (m_e + m_p)
    print(f"reduced-mass factor mu/m_e = {mu/m_e:.6f}; H-alpha with it = {lam_nm(3,2)*m_e/mu:.2f} nm (vacuum); "
          f"measured in air 656.28 nm, vacuum 656.47 nm")
    # classical collapse time: t = a0^3 / (4 r_e^2 c), r_e classical electron radius
    r_e = K / (m_e * c**2)
    t = A0**3 / (4 * r_e**2 * c)
    print(f"classical radiative collapse from a0: t = {t:.3e} s")
    print("Correspondence: orbital frequency vs emitted frequency n -> n-1")
    for n in (2, 10, 100, 1000):
        f_orb = 2 * RY / (h * n**3)
        f_em = (RY / h) * (1 / (n - 1)**2 - 1 / n**2)
        print(f"  n = {n:4d}: orbital {f_orb:.4e} Hz, emitted {f_em:.4e} Hz, ratio {f_em/f_orb:.4f}")


# ---------------------------------------------------------------- figure
W, H = 680, 420
LM, RM, TOP, BOT = 62, 150, 18, 22
Y_LO, Y_HI = -14.5, 0.8


def sy(E_):
    return TOP + (H - TOP - BOT) * (Y_HI - E_) / (Y_HI - Y_LO)


def figure_svg():
    o = []
    a = o.append
    x0, x1 = LM + 10, W - RM
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-lev-title fig-lev-desc">')
    a('<title id="fig-lev-title">Energy levels of hydrogen in the Bohr model</title>')
    a('<desc id="fig-lev-desc">Horizontal lines at minus 13.6, minus 3.4, minus 1.5, minus 0.85 electronvolts and so on, crowding together towards zero. Downward arrows from higher levels to the second level are the visible Balmer lines at 656, 486, 434 and 410 nanometres. A long arrow from the second level to the first is the ultraviolet Lyman alpha line at 122 nanometres.</desc>')
    a(f'<path class="fig-axis" d="M{LM},{sy(Y_LO):.1f} V{sy(Y_HI):.1f}"/>')
    for v in (0, -2, -4, -6, -8, -10, -12, -14):
        a(f'<path class="fig-axis" d="M{LM},{sy(v):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{LM-9}" y="{sy(v)+4:.1f}" text-anchor="end">{v}</text>')
    a(f'<text class="fig-label" transform="translate(16,{(TOP+H-BOT)/2:.1f}) rotate(-90)" text-anchor="middle">energy (eV)</text>')
    for n in range(1, 7):
        a(f'<path class="fig-axis" style="stroke-width:1.6" d="M{x0},{sy(E(n)):.1f} H{x1}"/>')
        if n <= 3:
            a(f'<text class="fig-note" x="{x1+8}" y="{sy(E(n))+4:.1f}">n = {n}, {E(n):.2f} eV</text>')
    a(f'<path class="fig-axis" style="stroke-dasharray:5 4" d="M{x0},{sy(0):.1f} H{x1}"/>')
    a(f'<text class="fig-note" x="{x1+8}" y="{sy(0)+4:.1f}">n → ∞, 0 eV (free)</text>')
    a(f'<text class="fig-note" x="{x1+8}" y="{(sy(0)+sy(E(3)))/2+4:.1f}">n = 4, 5, 6, …</text>')
    # arrows
    xa = x0 + 40
    a(f'<path class="fig-curve fig-mid" d="M{xa},{sy(E(2)):.1f} V{sy(E(1))-7:.1f}"/>')
    a(f'<path class="fig-arrowhead-mid" d="M{xa-5},{sy(E(1))-9:.1f} L{xa},{sy(E(1)):.1f} L{xa+5},{sy(E(1))-9:.1f} Z"/>')
    a(f'<text class="fig-note" x="{xa+8}" y="{(sy(E(2))+sy(E(1)))/2:.1f}">Lyman α, {lam_nm(2,1):.0f} nm (ultraviolet)</text>')
    for i, ni in enumerate((3, 4, 5, 6)):
        xb = x0 + 250 + 50 * i
        a(f'<path class="fig-curve fig-hot" d="M{xb},{sy(E(ni)):.1f} V{sy(E(2))-7:.1f}"/>')
        a(f'<path class="fig-arrowhead" d="M{xb-5},{sy(E(2))-9:.1f} L{xb},{sy(E(2)):.1f} L{xb+5},{sy(E(2))-9:.1f} Z"/>')
        a(f'<text class="fig-tick" x="{xb}" y="{sy(E(2))+16:.1f}" text-anchor="middle">{lam_nm(ni,2):.0f}</text>')
    a(f'<text class="fig-note" x="{x0+325}" y="{sy(E(2))+34:.1f}" text-anchor="middle">Balmer lines (nm), visible</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "03-bohr-atom.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:levels generated by scripts/ch03_bohr.py -->\n" + figure_svg() + "\n<!-- /FIGURE:levels -->"
    new, n = re.subn(r"<!-- FIGURE:levels.*?<!-- /FIGURE:levels -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:levels markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
