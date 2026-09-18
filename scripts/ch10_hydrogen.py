#!/usr/bin/env python3
"""Chapter 10 (hydrogen): checked numbers and the generated figure.

    python3 scripts/ch10_hydrogen.py            # print the numbers used in the essay
    python3 scripts/ch10_hydrogen.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:radial markers
in chapters/10-hydrogen.html. Coulomb constants are written e^2/(4 pi eps0); no bare alpha.

FIGURE RECORD
  Plotted quantity : radial probability density P(r) = r^2 R_nl(r)^2, probability per unit
                     radius, in units of 1/a0, for 1s, 2s, 2p, 3s (normalised hydrogen radial
                     functions, infinite nuclear mass)
  Horizontal axis  : r / a0 from 0 to 20
  Markers          : Bohr's orbit radii n^2 a0 for n = 1, 2, 3 (dotted)
"""
import math
import re
import sys
from pathlib import Path


def R(n, l, x):
    """Radial function in units a0 = 1."""
    if (n, l) == (1, 0):
        return 2 * math.exp(-x)
    if (n, l) == (2, 0):
        return (1 / (2 * math.sqrt(2))) * (2 - x) * math.exp(-x / 2)
    if (n, l) == (2, 1):
        return (1 / (2 * math.sqrt(6))) * x * math.exp(-x / 2)
    if (n, l) == (3, 0):
        return (2 / (81 * math.sqrt(3))) * (27 - 18 * x + 2 * x * x) * math.exp(-x / 3)
    raise ValueError


def P(n, l, x):
    return x * x * R(n, l, x) ** 2


def report():
    dx = 0.001
    xs = [i * dx for i in range(1, 80000)]
    for n, l, name in ((1, 0, "1s"), (2, 0, "2s"), (2, 1, "2p"), (3, 0, "3s")):
        norm = sum(P(n, l, x) for x in xs) * dx
        mean = sum(x * P(n, l, x) for x in xs) * dx
        peak = max(xs[:30000], key=lambda x: P(n, l, x))
        print(f"{name}: norm = {norm:.4f}, <r> = {mean:.3f} a0 (formula {(3*n*n - l*(l+1))/2:.1f}), most probable r = {peak:.3f} a0")
    print(f"1s: P(r < a0) = 1 - 5 e^-2 = {1-5*math.exp(-2):.4f};  P(r > 2 a0) = 13 e^-4 = {13*math.exp(-4):.4f}")
    E1 = 13.6057
    print(f"E_n: " + ", ".join(f"n={n}: {-E1/n/n:.3f} eV" for n in range(1, 5)))
    print("states per n (no spin): " + ", ".join(f"n={n}: {sum(2*l+1 for l in range(n))}" for n in range(1, 5)))
    # check the trial function e^{-r/a}: coefficients of 1/r cancel iff a = a0; energy -hbar^2/(2 m a0^2)
    hbar2_2m = 0.0380998  # eV nm^2
    K = 1.439965          # eV nm
    a0 = 2 * hbar2_2m / K
    print(f"a0 = hbar^2/(m K) = 2 (hbar^2/2m) / K = {a0:.5f} nm; E = -(hbar^2/2m)/a0^2 = {-hbar2_2m/a0**2:.4f} eV")


W, H = 680, 330
L, Rm, T, B = 60, 20, 20, 50
XM, YM = 20.0, 0.56


def sx(x):
    return L + (W - L - Rm) * x / XM


def sy(y):
    return H - B - (H - T - B) * y / YM


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-rad-title fig-rad-desc">')
    a('<title id="fig-rad-title">Radial probability distributions for hydrogen</title>')
    a('<desc id="fig-rad-desc">Probability per unit distance from the nucleus for the 1s, 2s, 2p and 3s states. The 1s curve peaks at one Bohr radius; the 2p curve peaks at four; 2s and 3s have one and two nodes, with outer peaks further out. Dotted lines mark Bohr orbit radii 1, 4 and 9.</desc>')
    a(f'<path class="fig-axis" d="M{L},{T} V{H-B} H{W-Rm}"/>')
    for x in range(0, 21, 4):
        a(f'<path class="fig-axis" d="M{sx(x):.1f},{H-B} v5"/>')
        a(f'<text class="fig-tick" x="{sx(x):.1f}" y="{H-B+19}" text-anchor="middle">{x}</text>')
    for y in (0, 0.2, 0.4):
        a(f'<path class="fig-axis" d="M{L},{sy(y):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{L-9}" y="{sy(y)+4:.1f}" text-anchor="end">{y:.1f}</text>')
    a(f'<text class="fig-label" x="{(L+W-Rm)/2:.1f}" y="{H-12}" text-anchor="middle">distance from the nucleus, r / a₀</text>')
    a(f'<text class="fig-label" transform="translate(18,{(T+H-B)/2:.1f}) rotate(-90)" text-anchor="middle">probability per unit r</text>')
    for r in (1, 4, 9):
        a(f'<path class="fig-axis" style="stroke-dasharray:2 4" d="M{sx(r):.1f},{H-B} V{T+10}"/>')
    a(f'<text class="fig-tick" x="{sx(9)+4:.1f}" y="{T+20}">Bohr orbits n²a₀</text>')
    styles = {"1s": ("fig-hot", 2.6), "2s": ("fig-mid", 1.4), "2p": ("fig-hot", 1.4), "3s": ("fig-cool", 1.4)}
    labels = {"1s": (1.3, 0.54), "2s": (5.6, 0.2), "2p": (4.6, 0.215), "3s": (13.5, 0.115)}
    for n, l, name in ((1, 0, "1s"), (2, 0, "2s"), (2, 1, "2p"), (3, 0, "3s")):
        cls, wdt = styles[name]
        extra = ' style="stroke-dasharray:6 4;stroke-width:1.6"' if name == "2p" else f' style="stroke-width:{wdt}"'
        pts = " L".join(f"{sx(x):.1f},{sy(P(n, l, x)):.1f}" for x in [XM * i / 600 for i in range(601)])
        a(f'<path class="fig-curve {cls}"{extra} d="M{pts}"/>')
        lx, ly = labels[name]
        a(f'<text class="fig-note" x="{sx(lx):.1f}" y="{sy(ly):.1f}">{name}</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "10-hydrogen.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:radial generated by scripts/ch10_hydrogen.py -->\n" + figure_svg() + "\n<!-- /FIGURE:radial -->"
    new, n = re.subn(r"<!-- FIGURE:radial.*?<!-- /FIGURE:radial -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:radial markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
