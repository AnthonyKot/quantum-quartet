#!/usr/bin/env python3
"""Optional essay A4 (the Dirac equation): checked numbers, matrix checks and the figure.

    python3 scripts/a4_dirac.py            # print the checks and numbers used in the essay
    python3 scripts/a4_dirac.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:branches markers in
chapters/a4-dirac-equation.html.

FIGURE RECORD
  Plotted quantity : the two solutions E = +-sqrt(p^2c^2 + m^2c^4) for an electron, in MeV,
                     against pc in MeV from -2.5 to 2.5; the gap of 2mc^2 = 1.022 MeV between the
                     branches is marked, and the Newtonian curve mc^2 + p^2/2m (dashed) for comparison.
Constants: m_e c^2 = 0.51099895 MeV; fine-structure constant 1/137.035999; electron anomaly
a_e = (g-2)/2 = 0.00115965218 (CODATA).
"""
import math
import re
import sys
from pathlib import Path

ME = 0.51099895


def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def is_scalar(A, val):
    return all(abs(A[i][j] - (val if i == j else 0)) < 1e-12 for i in range(len(A)) for j in range(len(A)))


def report():
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]
    P = {"x": sx, "y": sy, "z": sz}
    for a in P:
        print(f"sigma_{a}^2 = 1: {is_scalar(mm(P[a], P[a]), 1)}")
    for a, b in (("x", "y"), ("y", "z"), ("z", "x")):
        print(f"sigma_{a} sigma_{b} + sigma_{b} sigma_{a} = 0: {is_scalar(add(mm(P[a], P[b]), mm(P[b], P[a])), 0)}")
    # a fourth 2x2 matrix anticommuting with all three? try the general form M = a I + b.sigma
    print("any 2x2 matrix is a I + b.sigma; anticommuting with all three sigmas forces a = 0 and b = 0 (checked by hand in the essay)")
    # Dirac representation
    Z = [[0, 0], [0, 0]]
    I2 = [[1, 0], [0, 1]]
    def block(A, B, C, D):
        return [A[0] + B[0], A[1] + B[1], C[0] + D[0], C[1] + D[1]]
    beta = block(I2, Z, Z, [[-1, 0], [0, -1]])
    alphas = {a: block(Z, P[a], P[a], Z) for a in P}
    mats = dict(alphas, beta=beta)
    ok = True
    names = list(mats)
    for i, a in enumerate(names):
        ok &= is_scalar(mm(mats[a], mats[a]), 1)
        for b in names[i + 1:]:
            ok &= is_scalar(add(mm(mats[a], mats[b]), mm(mats[b], mats[a])), 0)
    print(f"4x4 Dirac alphas and beta: each squares to 1 and all pairs anticommute: {ok}")
    print(f"pair-creation threshold 2 m c^2 = {2*ME:.4f} MeV")
    alpha = 1 / 137.035999
    print(f"fine-structure constant alpha = e^2/(4 pi eps0 hbar c) = {alpha:.6f}; alpha^2 = {alpha**2:.2e}")
    print(f"1s electron speed in Bohr model v/c = alpha = {alpha:.5f}")
    ae = 0.00115965218
    print(f"g = 2(1 + a_e) = {2*(1+ae):.8f}; Schwinger alpha/(2 pi) = {alpha/(2*math.pi):.8f}")
    # H fine structure 2p splitting ~ alpha^2 * 13.6 eV / 16  (2p3/2 - 2p1/2 = alpha^2 Ry / 16 * ... )
    split = alpha**2 * 13.6057 / 16
    print(f"hydrogen n=2 fine-structure splitting alpha^2 * 13.6 eV/16 = {split*1e6:.1f} micro-eV = {split/4.135667e-15/1e9:.2f} GHz")


W, H = 680, 360
L_, R_, T_, B_ = 60, 20, 20, 50
XM, YM = 2.5, 2.9


def sx(p):
    return L_ + (W - L_ - R_) * (p + XM) / (2 * XM)


def sy(e):
    return T_ + (H - T_ - B_) * (YM - e) / (2 * YM)


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-br-title fig-br-desc">')
    a('<title id="fig-br-title">The two energy branches of a relativistic electron</title>')
    a('<desc id="fig-br-desc">Energy against momentum. An upper curve starts at plus 0.511 MeV at zero momentum and rises, becoming straight at large momentum. A mirror-image lower curve starts at minus 0.511 MeV and falls. Between them is an empty gap of 1.022 MeV. A dashed Newtonian parabola hugs the upper curve near zero momentum.</desc>')
    a(f'<path class="fig-axis" d="M{sx(-XM):.1f},{sy(0):.1f} H{sx(XM):.1f} M{sx(0):.1f},{T_} V{H-B_}"/>')
    for p in (-2, -1, 2):
        a(f'<path class="fig-axis" d="M{sx(p):.1f},{sy(0):.1f} v5"/>')
        a(f'<text class="fig-tick" x="{sx(p):.1f}" y="{sy(0)+18:.1f}" text-anchor="middle">{p}</text>')
    for e in (-2, -1, 1, 2):
        a(f'<path class="fig-axis" d="M{sx(0):.1f},{sy(e):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{sx(0)-9:.1f}" y="{sy(e)+4:.1f}" text-anchor="end">{e}</text>')
    a(f'<text class="fig-label" x="{sx(-XM):.1f}" y="{sy(0)+36:.1f}">momentum, pc (MeV) →</text>')
    a(f'<text class="fig-label" x="{sx(0)+8:.1f}" y="{T_+10}">energy E (MeV)</text>')
    ps = [-XM + 2 * XM * i / 400 for i in range(401)]
    up = " L".join(f"{sx(p):.1f},{sy(math.sqrt(p*p+ME*ME)):.1f}" for p in ps)
    dn = " L".join(f"{sx(p):.1f},{sy(-math.sqrt(p*p+ME*ME)):.1f}" for p in ps)
    nw = " L".join(f"{sx(p):.1f},{sy(ME+p*p/(2*ME)):.1f}" for p in ps if ME + p * p / (2 * ME) <= YM)
    a(f'<path class="fig-curve fig-hot" style="stroke-width:2.6" d="M{up}"/>')
    a(f'<path class="fig-curve fig-mid" style="stroke-width:2.2" d="M{dn}"/>')
    a(f'<path class="fig-curve fig-classical" d="M{nw}"/>')
    xg = sx(0.3)
    a(f'<path class="fig-axis" d="M{xg:.1f},{sy(ME):.1f} V{sy(-ME):.1f} M{xg-5:.1f},{sy(ME):.1f} h10 M{xg-5:.1f},{sy(-ME):.1f} h10"/>')
    a(f'<text class="fig-note" x="{xg+10:.1f}" y="{sy(0.18):.1f}">gap 2mc²</text>')
    a(f'<text class="fig-note" x="{xg+10:.1f}" y="{sy(-0.32):.1f}">= 1.022 MeV</text>')
    a(f'<text class="fig-note" x="{sx(1.35):.1f}" y="{sy(1.05):.1f}">positive energy</text>')
    a(f'<text class="fig-note" x="{sx(1.05):.1f}" y="{sy(-2.2):.1f}">negative energy</text>')
    a(f'<text class="fig-note" x="{sx(-2.45):.1f}" y="{sy(1.35):.1f}">dashed: Newton,</text>')
    a(f'<text class="fig-note" x="{sx(-2.45):.1f}" y="{sy(1.05):.1f}">mc² + p²/2m</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "a4-dirac-equation.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:branches generated by scripts/a4_dirac.py -->\n" + figure_svg() + "\n<!-- /FIGURE:branches -->"
    new, n = re.subn(r"<!-- FIGURE:branches.*?<!-- /FIGURE:branches -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:branches markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
