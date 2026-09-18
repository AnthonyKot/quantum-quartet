#!/usr/bin/env python3
"""Optional essay A1 (special relativity): checked numbers and the generated figure.

    python3 scripts/a1_special_relativity.py            # print the numbers used in the essay
    python3 scripts/a1_special_relativity.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:spacetime markers
in chapters/a1-special-relativity.html.

FIGURE RECORD
  Drawn            : a spacetime diagram in the ground frame (x horizontal, ct vertical, equal
                     scales), with the axes of a frame moving at v = 0.6c: its time axis
                     (x = vt) and its line of simultaneity through the origin (ct = (v/c) x).
                     Light rays at 45 degrees. Two events A and B, simultaneous in the moving
                     frame, drawn at ct = (v/c) x for x = +-2 units (so the ground frame sees
                     them 1.2 units apart in ct).
Muon data: rest lifetime 2.197 microseconds (PDG); production altitude ~15 km is typical.
"""
import math
import re
import sys
from pathlib import Path

c = 299792458.0
TAU = 2.197e-6


def gamma(beta):
    return 1 / math.sqrt(1 - beta * beta)


def report():
    L = 15e3
    for beta in (0.99, 0.998, 0.999):
        g = gamma(beta)
        t_lab = L / (beta * c)
        t_mu = t_lab / g
        print(f"v = {beta}c: gamma = {g:.2f}; ground time {t_lab*1e6:.2f} us = {t_lab/TAU:.1f} lifetimes;"
              f" muon's own time {t_mu*1e6:.2f} us = {t_mu/TAU:.2f} lifetimes; survive {math.exp(-t_mu/TAU):.3f}"
              f" (without dilation {math.exp(-t_lab/TAU):.1e}); atmosphere in muon frame {L/g:.0f} m")
    beta = 0.6
    g = gamma(beta)
    print(f"v = 0.6c: gamma = {g}")
    # interval check for an event t = 5 s, x = 3 light-seconds
    t, x = 5.0, 3.0
    tp = g * (t - beta * x)
    xp = g * (x - beta * t)
    print(f"event (ct, x) = ({t}, {x}) -> ({tp:.3f}, {xp:.3f}); interval ground {t*t-x*x:.3f}, moving {tp*tp-xp*xp:.3f}")
    # simultaneity: events at x = -2, +2 with ct = 0.6 x
    for X in (-2, 2):
        T = beta * X
        print(f"event at x = {X}, ct = {T:+.2f}: in moving frame ct' = {g*(T-beta*X):+.3f}")
    print(f"everyday: airliner 250 m/s: gamma - 1 = {0.5*(250/c)**2:.2e}")


W, H = 680, 400
CX, CY, S = 300, 330, 70


def P(x, t):
    return CX + S * x, CY - S * t


def figure_svg():
    beta = 0.6
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-st-title fig-st-desc">')
    a('<title id="fig-st-title">A spacetime diagram with a moving frame</title>')
    a('<desc id="fig-st-desc">Horizontal axis x, vertical axis ct. Dashed light rays run at 45 degrees. The moving frame\'s time axis leans towards the light ray, and its line of simultaneity leans up from the x axis by the same angle. Two events that lie on that tilted line are simultaneous for the moving observer but occur at different times on the ground.</desc>')
    x0, y0 = P(-3.5, 0); x1, _ = P(4.3, 0)
    a(f'<path class="fig-axis" style="stroke-width:1.4" d="M{x0:.1f},{y0:.1f} H{x1:.1f}"/>')
    _, yt = P(0, 4.4)
    a(f'<path class="fig-axis" style="stroke-width:1.4" d="M{CX},{CY+10} V{yt:.1f}"/>')
    a(f'<text class="fig-label" x="{x1+6:.1f}" y="{y0+5:.1f}">x</text>')
    a(f'<text class="fig-label" x="{CX-8}" y="{yt-6:.1f}" text-anchor="end">ct (ground)</text>')
    for s_ in (-1, 1):
        xa, ya = P(0, 0); xb, yb = P(s_ * 4.2, 4.2)
        a(f'<path class="fig-axis" style="stroke-dasharray:5 5" d="M{xa:.1f},{ya:.1f} L{xb:.1f},{yb:.1f}"/>')
    xl, yl = P(-4.1, 4.1)
    a(f'<text class="fig-tick" x="{xl+4:.1f}" y="{yl+14:.1f}">light</text>')
    # moving frame axes
    xb, yb = P(beta * 4.3, 4.3)
    a(f'<path class="fig-curve fig-hot" d="M{CX},{CY} L{xb:.1f},{yb:.1f}"/>')
    a(f'<text class="fig-note" x="{xb+6:.1f}" y="{yb+4:.1f}">ct′ (moving at 0.6c)</text>')
    xa, ya = P(-3.4, -beta * 3.4 * 0 - beta * 3.4); xb, yb = P(4.2, beta * 4.2)
    xa, ya = P(-0.4, -0.24)
    a(f'<path class="fig-curve fig-hot" style="stroke-dasharray:1 0" d="M{xa:.1f},{ya:.1f} L{xb:.1f},{yb:.1f}"/>')
    a(f'<text class="fig-note" x="{xb:.1f}" y="{yb+20:.1f}" text-anchor="end">x′: her "now" at time zero</text>')
    # a later line of simultaneity through events A and B
    off = 1.5
    xa, ya = P(-3.4, off + beta * -3.4); xb2, yb2 = P(3.2, off + beta * 3.2)
    a(f'<path class="fig-axis" style="stroke-dasharray:2 4" d="M{xa:.1f},{ya:.1f} L{xb2:.1f},{yb2:.1f}"/>')
    for X, name in ((-2, "A"), (2, "B")):
        xe, ye = P(X, off + beta * X)
        a(f'<circle cx="{xe:.1f}" cy="{ye:.1f}" r="5" class="fig-dot"/>')
        a(f'<text class="fig-label" x="{xe-9:.1f}" y="{ye-9:.1f}" text-anchor="end">{name}</text>')
        a(f'<path class="fig-axis" style="stroke-dasharray:1 3" d="M{xe:.1f},{ye:.1f} H{CX:.1f}"/>')
        a(f'<path class="fig-axis" d="M{CX-5},{ye:.1f} h10"/>')
        a(f'<text class="fig-tick" x="{CX+10}" y="{ye+4:.1f}">ground time of {name}</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "a1-special-relativity.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:spacetime generated by scripts/a1_special_relativity.py -->\n" + figure_svg() + "\n<!-- /FIGURE:spacetime -->"
    new, n = re.subn(r"<!-- FIGURE:spacetime.*?<!-- /FIGURE:spacetime -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:spacetime markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
