#!/usr/bin/env python3
"""Optional essay A3 (gravity as geometry): checked numbers and the generated figure.

    python3 scripts/a3_gravity.py            # print the numbers used in the essay
    python3 scripts/a3_gravity.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:clockrates markers in
chapters/a3-general-relativity.html.

Model: weak field, non-rotating spherical Earth, circular orbits; ground clock at the equator
radius with Earth's rotation ignored. Rates are fractional offsets relative to a ground clock.
  gravitational : + (GM/c^2)(1/R_E - 1/r)
  motion        : - v^2/(2c^2) = - GM/(2 r c^2)
FIGURE RECORD
  Plotted quantity : daily clock offset in microseconds per day against orbital altitude
                     (0 to 25,000 km): gravitational (dashed, positive), motion (dotted, negative),
                     net (solid). GPS (20,200 km) and ISS (~420 km) marked.
Constants: GM = 3.986004e14 m^3 s^-2; R_E = 6.371e6 m; GPS orbit radius 26,560 km.
"""
import math
import re
import sys
from pathlib import Path

c = 299792458.0
GM = 3.986004418e14
RE = 6.371e6
DAY = 86400


def rates(r):
    grav = GM / c**2 * (1 / RE - 1 / r)
    mot = -GM / (2 * r * c * c)
    return grav, mot, grav + mot


def report():
    g, h = 9.81, 22.5
    print(f"Pound-Rebka: g h / c^2 = {g*h/c**2:.3e}")
    print(f"one metre higher: {g/c**2:.2e} per metre; per day {g/c**2*DAY*1e9:.3f} ns")
    for name, r in (("GPS", 26.56e6), ("ISS", RE + 420e3)):
        gr, mo, net = rates(r)
        v = math.sqrt(GM / r)
        print(f"{name}: r = {r/1e3:.0f} km, v = {v:.0f} m/s; gravity {gr*DAY*1e6:+.2f} us/day, motion {mo*DAY*1e6:+.2f} us/day,"
              f" net {net*DAY*1e6:+.2f} us/day; light travel in net offset: {net*DAY*c/1e3:.1f} km/day")
    r0 = 1.5 * RE
    print(f"net offset zero at r = 1.5 R_E, altitude {(r0-RE)/1e3:.0f} km")
    print(f"Earth surface GM/(R c^2) = {GM/(RE*c*c):.2e}; Sun surface = {1.32712e20/(6.957e8*c*c):.2e}")
    # tidal: two balls 1 m apart horizontally at the surface, falling 1 s
    acc_conv = 9.81 * 1.0 / RE
    print(f"tidal convergence of balls 1 m apart: relative acceleration {acc_conv:.2e} m/s^2; after 10 s they close by {0.5*acc_conv*100*1e6:.1f} micrometres")


W, H = 680, 330
L_, R_, T_, B_ = 70, 20, 20, 50
XM = 25000.0
YLO, YHI = -35.0, 55.0


def sx(alt_km):
    return L_ + (W - L_ - R_) * alt_km / XM


def sy(us):
    return T_ + (H - T_ - B_) * (YHI - us) / (YHI - YLO)


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-cr-title fig-cr-desc">')
    a('<title id="fig-cr-title">How fast an orbiting clock runs compared with one on the ground</title>')
    a('<desc id="fig-cr-desc">Daily clock gain or loss against orbital altitude. The gravitational effect makes higher clocks gain, rising towards about 60 microseconds a day. The orbital speed makes them lose, most strongly in low orbit. The net is a loss in low orbit, zero at about 3,200 kilometres, and a gain of about 38 microseconds a day at the altitude of GPS.</desc>')
    a(f'<path class="fig-axis" d="M{L_},{T_} V{H-B_} H{W-R_}"/>')
    a(f'<path class="fig-axis" style="stroke-width:1.2" d="M{L_},{sy(0):.1f} H{W-R_}"/>')
    for x in range(0, 25001, 5000):
        a(f'<path class="fig-axis" d="M{sx(x):.1f},{H-B_} v5"/>')
        a(f'<text class="fig-tick" x="{sx(x):.1f}" y="{H-B_+19}" text-anchor="middle">{x:,}</text>')
    for y in (-30, -15, 0, 15, 30, 45):
        a(f'<path class="fig-axis" d="M{L_},{sy(y):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{L_-9}" y="{sy(y)+4:.1f}" text-anchor="end">{y:+d}</text>'.replace("+0", "0"))
    a(f'<text class="fig-label" x="{(L_+W-R_)/2:.1f}" y="{H-12}" text-anchor="middle">orbital altitude (km)</text>')
    a(f'<text class="fig-label" transform="translate(18,{(T_+H-B_)/2:.1f}) rotate(-90)" text-anchor="middle">clock gain per day (μs)</text>')
    alts = [XM * i / 400 for i in range(1, 401)]
    for idx, cls, extra in ((0, "fig-mid", ' style="stroke-dasharray:6 4"'), (1, "fig-cool", ' style="stroke-dasharray:2 3"'), (2, "fig-hot", ' style="stroke-width:2.6"')):
        pts = " L".join(f"{sx(al):.1f},{sy(rates(RE+al*1e3)[idx]*DAY*1e6):.1f}" for al in alts)
        a(f'<path class="fig-curve {cls}"{extra} d="M{pts}"/>')
    a(f'<text class="fig-note" x="{sx(15500):.1f}" y="{sy(51):.1f}">gravity: higher clocks gain</text>')
    a(f'<text class="fig-note" x="{sx(14500):.1f}" y="{sy(-19):.1f}">orbital speed: moving clocks lose</text>')
    for name, alt in (("GPS", 20190), ("ISS", 420)):
        net = rates(RE + alt * 1e3)[2] * DAY * 1e6
        a(f'<circle cx="{sx(alt):.1f}" cy="{sy(net):.1f}" r="4.5" class="fig-dot"/>')
        a(f'<text class="fig-note" x="{sx(alt)+8:.1f}" y="{sy(net)+(16 if name=="ISS" else -8):.1f}">{name}, net {net:+.1f}</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "a3-general-relativity.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:clockrates generated by scripts/a3_gravity.py -->\n" + figure_svg() + "\n<!-- /FIGURE:clockrates -->"
    new, n = re.subn(r"<!-- FIGURE:clockrates.*?<!-- /FIGURE:clockrates -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:clockrates markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
