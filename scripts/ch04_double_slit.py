#!/usr/bin/env python3
"""Chapter 04 (double slit): checked numbers and the generated figure.

    python3 scripts/ch04_double_slit.py            # print the numbers used in the essay
    python3 scripts/ch04_double_slit.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:fringes
markers in chapters/04-quantum-behavior.html.

FIGURE RECORD
  Plotted quantity : probability of arrival per unit length along the screen, P(x),
                     in units where the no-interference value at the centre is 1.
                       both slits, no record : P = E(x) * (1 + cos(2 pi x / dx))
                       which-slit record     : P = E(x)
                     E(x) = sinc^2(pi w x / (lambda L)) is the single-slit envelope.
  Horizontal axis  : position on the screen x, -2.4 mm to 2.4 mm
  Parameters       : electron kinetic energy 100 eV (lambda = 0.1226 nm),
                     slit separation d = 200 nm, slit width w = 50 nm,
                     slit-to-screen distance L = 1 m  ->  fringe spacing dx = 0.613 mm
  Note             : the essay's main text takes E(x) = 1 (very narrow slits); the
                     figure keeps the envelope so that it looks like a real pattern.
"""
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34       # J s
c = 299792458.0          # m / s
eV = 1.602176634e-19     # J
m_e = 9.1093837015e-31   # kg

E_KIN = 100 * eV
D = 200e-9
W_SLIT = 50e-9
L_SCREEN = 1.0


def de_broglie(m, E):
    """Non-relativistic: p = sqrt(2 m E), lambda = h / p."""
    return h / math.sqrt(2 * m * E)


LAM = de_broglie(m_e, E_KIN)
DX = LAM * L_SCREEN / D


def envelope(x):
    a = math.pi * W_SLIT * x / (LAM * L_SCREEN)
    return 1.0 if abs(a) < 1e-12 else (math.sin(a) / a) ** 2


def p_both(x, gamma=1.0):
    return envelope(x) * (1 + gamma * math.cos(2 * math.pi * x / DX))


def p_marked(x):
    return envelope(x)


def report():
    p = math.sqrt(2 * m_e * E_KIN)
    print(f"100 eV electron: E = {E_KIN:.4e} J, p = {p:.4e} kg m/s, v = {p/m_e:.4e} m/s = {p/m_e/c:.4f} c")
    print(f"  kinetic energy / rest energy = {E_KIN/(m_e*c*c):.2e}  (non-relativistic formula is fine)")
    print(f"  lambda = h/p = {LAM*1e9:.4f} nm")
    print(f"  d = {D*1e9:.0f} nm, L = {L_SCREEN} m: angle between fringes lambda/d = {LAM/D:.3e} rad, spacing = {DX*1e3:.4f} mm")
    print(f"  first envelope zero (w = {W_SLIT*1e9:.0f} nm) at x = {LAM*L_SCREEN/W_SLIT*1e3:.3f} mm")
    lam4 = de_broglie(m_e, 400 * eV)
    print(f"400 eV electron: lambda = {lam4*1e9:.4f} nm, spacing = {lam4*L_SCREEN/D*1e3:.4f} mm")
    lam_b = h / (0.010 * 300)
    print(f"10 g bullet at 300 m/s: lambda = {lam_b:.3e} m; with d = 1 cm, L = 100 m: spacing = {lam_b*100/0.01:.3e} m")
    print()
    print("Arrow arithmetic, equal lengths A = 1:")
    for deg in (0, 90, 120, 180):
        ph = math.radians(deg)
        z = complex(1, 0) + complex(math.cos(ph), math.sin(ph))
        print(f"  phase difference {deg:3d} deg: |a1+a2|^2 = {abs(z)**2:.3f}   (2 + 2 cos = {2+2*math.cos(ph):.3f}; sum of probabilities = 2)")
    print()
    print("Partial which-slit record, overlap gamma: visibility (Pmax-Pmin)/(Pmax+Pmin)")
    for g in (1.0, 0.5, 0.0):
        pmax, pmin = 1 + g, 1 - g
        print(f"  gamma = {g}: Pmax = {pmax}, Pmin = {pmin}, visibility = {(pmax-pmin)/(pmax+pmin):.2f}")
    # consistency: interference redistributes, average over one fringe = sum of probabilities
    n = 1000
    avg = sum(1 + math.cos(2 * math.pi * i / n) for i in range(n)) / n
    print(f"\naverage of (1 + cos) over one fringe = {avg:.6f}  (equals the no-interference value 1)")


# ---------------------------------------------------------------- figure
W, H = 680, 360
LM, RM, TOP, BOT = 62, 20, 18, 56
X_MAX = 2.4e-3
Y_MAX = 2.1


def sx(x):
    return LM + (W - LM - RM) * (x + X_MAX) / (2 * X_MAX)


def sy(y):
    return H - BOT - (H - TOP - BOT) * y / Y_MAX


def path(fn, n=960):
    pts = []
    for i in range(n + 1):
        x = -X_MAX + 2 * X_MAX * i / n
        pts.append(f"{sx(x):.1f},{sy(fn(x)):.1f}")
    return "M" + " L".join(pts)


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-fringes-title fig-fringes-desc">')
    a('<title id="fig-fringes-title">Arrival pattern with and without a which-slit record</title>')
    a('<desc id="fig-fringes-desc">Probability of arrival against position on the screen. Without a record the curve oscillates between zero and twice the smooth curve, with fringes 0.61 millimetres apart. With a which-slit record the curve is smooth, with no fringes, and runs through the middle of the oscillating one.</desc>')
    a(f'<path class="fig-axis" d="M{LM},{TOP} V{H-BOT} H{W-RM}"/>')
    for i in range(-2, 3):
        x = i * 1e-3
        a(f'<path class="fig-axis" d="M{sx(x):.1f},{H-BOT} v5"/>')
        a(f'<text class="fig-tick" x="{sx(x):.1f}" y="{H-BOT+19}" text-anchor="middle">{i}</text>')
    for y in (0, 0.5, 1.0, 1.5, 2.0):
        a(f'<path class="fig-axis" d="M{LM},{sy(y):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{LM-9}" y="{sy(y)+4:.1f}" text-anchor="end">{y:.1f}</text>')
    a(f'<text class="fig-label" x="{(LM+W-RM)/2:.1f}" y="{H-12}" text-anchor="middle">position on the screen x (mm)</text>')
    a(f'<text class="fig-label" transform="translate(18,{(TOP+H-BOT)/2:.1f}) rotate(-90)" text-anchor="middle">probability of arrival (relative)</text>')
    a(f'<path class="fig-curve fig-hot" d="{path(p_both)}"/>')
    a(f'<path class="fig-curve fig-classical" d="{path(p_marked)}"/>')
    # fringe spacing marker between the central maximum and the next one
    ym = sy(2.04)
    a(f'<path class="fig-axis" d="M{sx(0):.1f},{ym:.1f} H{sx(DX):.1f} M{sx(0):.1f},{ym-4:.1f} v8 M{sx(DX):.1f},{ym-4:.1f} v8"/>')
    a(f'<text class="fig-note" x="{sx(DX)+8:.1f}" y="{ym+4:.1f}">λL/d = 0.61 mm</text>')
    a(f'<text class="fig-note" x="{sx(-2.35e-3):.1f}" y="{sy(1.75):.1f}">both slits open,</text>')
    a(f'<text class="fig-note" x="{sx(-2.35e-3):.1f}" y="{sy(1.75)+16:.1f}">no record: fringes</text>')
    a(f'<text class="fig-note" x="{sx(1.32e-3):.1f}" y="{sy(1.05):.1f}">which-slit record:</text>')
    a(f'<text class="fig-note" x="{sx(1.32e-3):.1f}" y="{sy(1.05)+16:.1f}">no fringes (dashed)</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "04-quantum-behavior.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:fringes generated by scripts/ch04_double_slit.py -->\n" + figure_svg() + "\n<!-- /FIGURE:fringes -->"
    new, n = re.subn(r"<!-- FIGURE:fringes.*?<!-- /FIGURE:fringes -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:fringes markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
