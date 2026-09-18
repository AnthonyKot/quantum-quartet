#!/usr/bin/env python3
"""Chapter 05 (one state, different descriptions): checked numbers and the generated figure.

    python3 scripts/ch05_representations.py            # print the numbers used in the essay
    python3 scripts/ch05_representations.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:axes markers
in chapters/05-two-mechanics.html.

Conventions: a linear polarisation at angle theta (from horizontal) is the unit
arrow (cos theta, sin theta) in the H/V description. The D/A axes are at 45 and
135 degrees. The amplitude to pass a polariser at angle phi is the component of the
state along that polariser's direction, cos(theta - phi).

FIGURE RECORD
  Drawn            : one state arrow at 30 degrees, unit length
  Axes             : H/V (0, 90 degrees), solid; D/A (45, 135 degrees), dashed
  Projections      : onto H and V (0.866, 0.500) and onto D and A (0.966, -0.259),
                     computed below; drawn as dotted perpendiculars
"""
import math
import re
import sys
from pathlib import Path

THETA = 30.0


def comps(theta_deg, axes_deg):
    return [math.cos(math.radians(theta_deg - a)) for a in axes_deg]


def report():
    hv = comps(THETA, (0, 90))
    da = comps(THETA, (45, 135))
    print(f"state at {THETA} deg, H/V amplitudes: {hv[0]:.4f}, {hv[1]:.4f}  probs {hv[0]**2:.4f}, {hv[1]**2:.4f}")
    print(f"                  D/A amplitudes: {da[0]:.4f}, {da[1]:.4f}  probs {da[0]**2:.4f}, {da[1]**2:.4f}")
    # the question "horizontal?" asked of the D/A description
    h_in_da = comps(0, (45, 135))
    amp = da[0] * h_in_da[0] + da[1] * h_in_da[1]
    print(f"H described in D/A: {h_in_da[0]:.4f}, {h_in_da[1]:.4f}; amplitude from D/A lists = {amp:.4f}, prob {amp**2:.4f}")
    # mixture comparison
    mix_pD = hv[0]**2 * 0.5 + hv[1]**2 * 0.5
    print(f"mixture 75% H / 25% V: P(D) = {mix_pD:.3f}   vs superposition P(D) = {da[0]**2:.3f}")
    # three polarisers
    print(f"H photon at V polariser: {math.cos(math.radians(90))**2:.3f}")
    p = math.cos(math.radians(45))**2 * math.cos(math.radians(45))**2
    print(f"H photon via 45 deg then V: {p:.3f}")
    print(f"photon at 60 deg: P(pass 0) = {math.cos(math.radians(60))**2:.3f}, P(pass 45) = {math.cos(math.radians(15))**2:.3f}")
    # circular
    c = (1 / math.sqrt(2), 1j / math.sqrt(2))
    for name, ax in (("H", (1, 0)), ("V", (0, 1)), ("D", (1 / math.sqrt(2), 1 / math.sqrt(2))), ("A", (-1 / math.sqrt(2), 1 / math.sqrt(2)))):
        a = ax[0] * c[0] + ax[1] * c[1]
        print(f"circular (1, i)/sqrt2: P({name}) = {abs(a)**2:.3f}")
    R = (1 / math.sqrt(2), 1j / math.sqrt(2))
    L = (1 / math.sqrt(2), -1j / math.sqrt(2))
    for name, ax in (("R", R), ("L", L)):
        a = ax[0].conjugate() * c[0] + ax[1].conjugate() * c[1]
        print(f"circular: P({name}) = {abs(a)**2:.3f}")
    d = (1 / math.sqrt(2), 1 / math.sqrt(2))
    for name, ax in (("R", R), ("L", L)):
        a = ax[0].conjugate() * d[0] + ax[1].conjugate() * d[1]
        print(f"diagonal D: P({name}) = {abs(a)**2:.3f}")


# ---------------------------------------------------------------- figure
W, H = 680, 400
CX, CY, S = 250, 330, 250   # origin and unit length in px


def pt(x, y):
    return CX + S * x, CY - S * y


def figure_svg():
    o = []
    a = o.append
    th = math.radians(THETA)
    sx_, sy_ = math.cos(th), math.sin(th)
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-axes-title fig-axes-desc">')
    a('<title id="fig-axes-title">One arrow, two pairs of axes</title>')
    a('<desc id="fig-axes-desc">A single arrow at 30 degrees from horizontal. Solid axes H and V give it components 0.87 and 0.50. Dashed axes D and A, rotated by 45 degrees, give the same arrow components 0.97 and minus 0.26. The arrow itself is the same in both.</desc>')
    # H/V axes
    x0, y0 = pt(-0.55, 0); x1, y1 = pt(1.25, 0)
    a(f'<path class="fig-axis" style="stroke-width:1.4" d="M{x0:.1f},{y0:.1f} H{x1:.1f}"/>')
    x0, y0 = pt(0, -0.25); x1, y1 = pt(0, 1.2)
    a(f'<path class="fig-axis" style="stroke-width:1.4" d="M{x0:.1f},{y0:.1f} V{y1:.1f}"/>')
    a(f'<text class="fig-label" x="{pt(1.27,0)[0]:.1f}" y="{pt(0,0)[1]+5:.1f}">H</text>')
    a(f'<text class="fig-label" x="{pt(0,1.22)[0]-5:.1f}" y="{pt(0,1.22)[1]:.1f}">V</text>')
    # D/A axes
    for ang, name, lo, hi in ((45, "D", -0.3, 1.25), (135, "A", -0.3, 0.75)):
        ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        xa, ya = pt(lo * ux, lo * uy); xb, yb = pt(hi * ux, hi * uy)
        a(f'<path class="fig-axis" style="stroke-dasharray:6 5" d="M{xa:.1f},{ya:.1f} L{xb:.1f},{yb:.1f}"/>')
        xl, yl = pt((hi + 0.06) * ux, (hi + 0.06) * uy)
        a(f'<text class="fig-label" x="{xl-6:.1f}" y="{yl+4:.1f}">{name}</text>')
    # projections onto H and V
    xs, ys = pt(sx_, sy_)
    a(f'<path class="fig-axis" style="stroke-dasharray:2 4" d="M{xs:.1f},{ys:.1f} V{pt(0,0)[1]:.1f} M{xs:.1f},{ys:.1f} H{pt(0,0)[0]:.1f}"/>')
    a(f'<text class="fig-note" x="{xs:.1f}" y="{pt(0,0)[1]+20:.1f}" text-anchor="middle">0.87</text>')
    a(f'<text class="fig-note" x="{pt(0,0)[0]-10:.1f}" y="{ys+5:.1f}" text-anchor="end">0.50</text>')
    # projections onto D and A
    d, al = comps(THETA, (45, 135))
    ux, uy = math.cos(math.radians(45)), math.sin(math.radians(45))
    xd, yd = pt(d * ux, d * uy)
    a(f'<path class="fig-axis" style="stroke-dasharray:2 4" d="M{xs:.1f},{ys:.1f} L{xd:.1f},{yd:.1f}"/>')
    a(f'<text class="fig-note" x="{xd-12:.1f}" y="{yd-8:.1f}" text-anchor="end">0.97</text>')
    vx, vy = math.cos(math.radians(135)), math.sin(math.radians(135))
    xA, yA = pt(al * vx, al * vy)
    a(f'<path class="fig-axis" style="stroke-dasharray:2 4" d="M{xs:.1f},{ys:.1f} L{xA:.1f},{yA:.1f}"/>')
    a(f'<text class="fig-note" x="{xA+6:.1f}" y="{yA+18:.1f}">−0.26</text>')
    # the state arrow
    xo, yo = pt(0, 0)
    a(f'<path class="fig-curve fig-hot" style="stroke-width:3" d="M{xo:.1f},{yo:.1f} L{xs:.1f},{ys:.1f}"/>')
    hx, hy = math.cos(th), -math.sin(th)
    px_, py_ = -hy, hx
    tip = (xs, ys)
    b1 = (xs - 14 * hx + 6 * px_, ys - 14 * hy + 6 * py_)
    b2 = (xs - 14 * hx - 6 * px_, ys - 14 * hy - 6 * py_)
    a(f'<path class="fig-arrowhead" d="M{tip[0]:.1f},{tip[1]:.1f} L{b1[0]:.1f},{b1[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f} Z"/>')
    a(f'<text class="fig-note" x="{xs+12:.1f}" y="{ys-2:.1f}">the state:</text>')
    a(f'<text class="fig-note" x="{xs+12:.1f}" y="{ys+14:.1f}">polarised at 30°</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "05-two-mechanics.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:axes generated by scripts/ch05_representations.py -->\n" + figure_svg() + "\n<!-- /FIGURE:axes -->"
    new, n = re.subn(r"<!-- FIGURE:axes.*?<!-- /FIGURE:axes -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:axes markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
