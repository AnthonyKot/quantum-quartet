#!/usr/bin/env python3
"""Chapter 07 (uncertainty): checked numbers and the generated figure.

    python3 scripts/ch07_uncertainty.py            # print the numbers used in the essay
    python3 scripts/ch07_uncertainty.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:tradeoff
markers in chapters/07-uncertainty.html.

FIGURE RECORD
  Plotted quantity : left panels, position density |psi(x)|^2; right panels, momentum
                     density |phi(p)|^2, for two Gaussian states
  Units            : hbar = 1; x in units of a length s, p in units of hbar/s
  Parameters       : narrow state sigma_x = 0.5 s (so sigma_p = 1.0 hbar/s)
                     wide state   sigma_x = 1.5 s (so sigma_p = 0.333 hbar/s)
                     each curve normalised to unit area and drawn on a shared scale per panel
  Check            : the momentum densities are computed by numerical Fourier transform of
                     psi(x), not from the formula, and their spreads printed below
"""
import cmath
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34
hbar = h / (2 * math.pi)
m_e = 9.1093837015e-31
m_p = 1.67262192369e-27
e = 1.602176634e-19
eps0 = 8.8541878128e-12
K = e**2 / (4 * math.pi * eps0)
HBARC_MEVFM = hbar * 299792458.0 / e / 1e6 * 1e15


def gaussian_psi(sx):
    return lambda x: (2 * math.pi * sx**2) ** -0.25 * math.exp(-x * x / (4 * sx**2))


def spreads(psi, L=12.0, N=1200, P=8.0, M=400):
    dx = 2 * L / N
    xs = [-L + i * dx for i in range(N + 1)]
    vals = [psi(x) for x in xs]
    norm = sum(abs(v) ** 2 for v in vals) * dx
    mx = sum(x * abs(v) ** 2 for x, v in zip(xs, vals)) * dx / norm
    sx = math.sqrt(sum((x - mx) ** 2 * abs(v) ** 2 for x, v in zip(xs, vals)) * dx / norm)
    dp = 2 * P / M
    ps = [-P + j * dp for j in range(M + 1)]
    phis = [sum(v * cmath.exp(-1j * p * x) for x, v in zip(xs, vals)) * dx / math.sqrt(2 * math.pi) for p in ps]
    pn = sum(abs(f) ** 2 for f in phis) * dp
    mp = sum(p * abs(f) ** 2 for p, f in zip(ps, phis)) * dp / pn
    sp = math.sqrt(sum((p - mp) ** 2 * abs(f) ** 2 for p, f in zip(ps, phis)) * dp / pn)
    return sx, sp, ps, [abs(f) ** 2 / pn for f in phis]


def report():
    for s in (0.5, 1.5):
        sx, sp, _, _ = spreads(gaussian_psi(s))
        print(f"Gaussian sigma_x = {s}: numerical sigma_x = {sx:.4f}, sigma_p = {sp:.4f}, product = {sx*sp:.4f} (hbar = 1)")
    b = 1.0
    sx, sp, _, _ = spreads(lambda x: math.exp(-abs(x) / b) / math.sqrt(b), L=20, N=4000, P=40, M=1600)
    print(f"exp(-|x|/b): sigma_x = {sx:.4f} (b/sqrt2 = {1/math.sqrt(2):.4f}), sigma_p = {sp:.4f} (1/b; slow tails), product = {sx*sp:.4f}")
    print()
    # hydrogen estimate: E(r) = hbar^2/(2 m r^2) - K/r ; min at r = hbar^2/(m K)
    r = hbar**2 / (m_e * K)
    E = hbar**2 / (2 * m_e * r**2) - K / r
    print(f"estimate with p ~ hbar/r: r_min = {r*1e9:.4f} nm, E_min = {E/e:.2f} eV")
    r2 = hbar**2 / (4 * m_e * K)
    E2 = hbar**2 / (8 * m_e * r2**2) - K / r2
    print(f"estimate with p ~ hbar/(2r): r_min = {r2*1e9:.4f} nm, E_min = {E2/e:.2f} eV")
    for rr in (0.01e-9, 0.02e-9, 0.0529e-9, 0.1e-9, 0.2e-9):
        print(f"   r = {rr*1e9:.4f} nm: KE = {hbar**2/(2*m_e*rr**2)/e:7.2f} eV, PE = {-K/rr/e:7.2f} eV, total = {(hbar**2/(2*m_e*rr**2)-K/rr)/e:7.2f} eV")
    print()
    dx = 0.1e-9
    dp = hbar / (2 * dx)
    print(f"electron, dx = 0.1 nm: dp >= {dp:.3e} kg m/s, dv >= {dp/m_e:.3e} m/s")
    m, dx = 1e-9, 1e-6
    print(f"dust grain 1 ug, dx = 1 um: dv >= {hbar/(2*m*dx):.3e} m/s")
    print(f"hbar c = {HBARC_MEVFM:.2f} MeV fm")
    dxn = 2.0
    pc = HBARC_MEVFM / (2 * dxn)
    mpc2 = m_p * 299792458.0**2 / e / 1e6
    print(f"proton, dx = {dxn} fm: dp c >= {pc:.1f} MeV; KE ~ (dp c)^2 / (2 m c^2) = {pc**2/(2*mpc2):.2f} MeV  (m_p c^2 = {mpc2:.1f} MeV)")
    # slit example: 100 eV electron, slit width 1 um? use w = 100 nm
    p = math.sqrt(2 * m_e * 100 * e)
    lam = h / p
    w = 100e-9
    print(f"100 eV electron through a {w*1e9:.0f} nm slit: lambda = {lam*1e9:.4f} nm, angle to first zero = lambda/w = {lam/w:.3e} rad,"
          f" p_x spread ~ p lambda/w = h/w = {h/w:.3e}; times w = h")


# ---------------------------------------------------------------- figure
W, H = 680, 360
PANEL_W, PANEL_H = 290, 120
X0L, X0R = 30, 370
ROW_Y = (30, 200)


def panel(o, x0, y0, xs, ys, xmax, ymax, cls, label):
    sxp = lambda x: x0 + PANEL_W * (x + xmax) / (2 * xmax)
    syp = lambda y: y0 + PANEL_H - PANEL_H * y / ymax
    o.append(f'<path class="fig-axis" d="M{x0},{y0+PANEL_H} H{x0+PANEL_W}"/>')
    o.append(f'<path class="fig-axis" d="M{x0+PANEL_W/2:.1f},{y0+PANEL_H} v5"/>')
    pts = " L".join(f"{sxp(x):.1f},{syp(y):.1f}" for x, y in zip(xs, ys) if -xmax <= x <= xmax)
    o.append(f'<path class="fig-curve {cls}" d="M{pts}"/>')
    o.append(f'<text class="fig-note" x="{x0+PANEL_W:.1f}" y="{y0+14}" text-anchor="end">{label}</text>')


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-tr-title fig-tr-desc">')
    a('<title id="fig-tr-title">Narrow in position means wide in momentum</title>')
    a('<desc id="fig-tr-desc">Two rows. Top row: a narrow bell curve in position beside a wide bell curve in momentum. Bottom row: a wide bell curve in position beside a narrow one in momentum. Squeezing one spreads the other.</desc>')
    a(f'<text class="fig-label" x="{X0L+PANEL_W/2}" y="18" text-anchor="middle">position density</text>')
    a(f'<text class="fig-label" x="{X0R+PANEL_W/2}" y="18" text-anchor="middle">momentum density</text>')
    XM, PM = 5.0, 3.5
    for row, (s, cls) in enumerate(((0.5, "fig-hot"), (1.5, "fig-mid"))):
        y0 = ROW_Y[row] + 10
        psi = gaussian_psi(s)
        xs = [-XM + i * 2 * XM / 400 for i in range(401)]
        panel(o, X0L, y0, xs, [psi(x) ** 2 for x in xs], XM, 0.85, cls, f"Δx = {s} s")
        _, sp, ps, dens = spreads(psi, P=PM + 0.5, M=300)
        panel(o, X0R, y0, ps, dens, PM, 1.25, cls, f"Δp = {sp:.2f} ħ/s")
    a(f'<text class="fig-tick" x="{X0L+PANEL_W/2}" y="{ROW_Y[1]+10+PANEL_H+20}" text-anchor="middle">x (from −5s to 5s)</text>')
    a(f'<text class="fig-tick" x="{X0R+PANEL_W/2}" y="{ROW_Y[1]+10+PANEL_H+20}" text-anchor="middle">p (from −3.5 to 3.5 ħ/s)</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "07-uncertainty.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:tradeoff generated by scripts/ch07_uncertainty.py -->\n" + figure_svg() + "\n<!-- /FIGURE:tradeoff -->"
    new, n = re.subn(r"<!-- FIGURE:tradeoff.*?<!-- /FIGURE:tradeoff -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:tradeoff markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
