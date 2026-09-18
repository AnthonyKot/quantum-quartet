#!/usr/bin/env python3
"""Chapter 09b (harmonic oscillator): checked numbers and the generated figure.

    python3 scripts/ch09b_oscillator.py            # print the numbers used in the essay
    python3 scripts/ch09b_oscillator.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:oscillator
markers in chapters/09b-oscillator.html.

FIGURE RECORD
  Left panel  : potential V = x^2/2 (units hbar = m = omega = 1), levels E_n = n + 1/2 for
                n = 0..4, each carrying phi_n(x) (Hermite functions, from the recurrence below),
                drawn with its zero line at the level (arbitrary amplitude).
  Right panel : n = 10: quantum density |phi_10|^2 (solid) against the classical density
                1 / (pi sqrt(A^2 - x^2)) for the same energy, A = sqrt(2E) = sqrt(21) (dashed).
Molecular data: CO fundamental vibrational band at 2143 cm^-1; HCl at 2886 cm^-1.
"""
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34
hbar = h / (2 * math.pi)
c = 299792458.0
eV = 1.602176634e-19
kB = 1.380649e-23
u = 1.66053906660e-27


def hermite_fn(n, x):
    """Normalised oscillator eigenfunction phi_n(x), units hbar = m = omega = 1."""
    p0 = math.pi ** -0.25 * math.exp(-x * x / 2)
    if n == 0:
        return p0
    p1 = math.sqrt(2) * x * p0
    for k in range(2, n + 1):
        p0, p1 = p1, math.sqrt(2 / k) * x * p1 - math.sqrt((k - 1) / k) * p0
    return p1


def report():
    for name, wn, m1, m2, bond in (("CO", 2143.0, 12.000, 15.995, 112.8e-12), ("HCl", 2886.0, 1.008, 34.969, 127.5e-12)):
        omega = 2 * math.pi * c * wn * 100
        E = hbar * omega / eV
        mu = m1 * m2 / (m1 + m2) * u
        k = mu * omega**2
        a = math.sqrt(hbar / (mu * omega))
        print(f"{name}: hbar omega = {E:.4f} eV, lambda = {1e4/wn:.2f} um, nu = {c*wn*100:.3e} Hz; zero-point = {E/2:.4f} eV;"
              f" mu = {mu/u:.3f} u; spring k = {k:.0f} N/m; ground-state dx = a/sqrt2 = {a/math.sqrt(2)*1e12:.2f} pm"
              f" ({a/math.sqrt(2)/bond*100:.1f}% of bond {bond*1e12:.0f} pm)")
        for T in (300, 1000):
            print(f"    population ratio n=1 / n=0 at {T} K: e^(-hbar w / kT) = {math.exp(-E*eV/(kB*T)):.2e}")
    # check normalisation and energies numerically
    dx = 0.01
    xs = [-10 + i * dx for i in range(2001)]
    for n in (0, 1, 2, 10):
        norm = sum(hermite_fn(n, x) ** 2 for x in xs) * dx
        # energy: <-1/2 phi'' + x^2/2 phi>
        e = 0.0
        for i in range(1, len(xs) - 1):
            x = xs[i]
            d2 = (hermite_fn(n, x + dx) - 2 * hermite_fn(n, x) + hermite_fn(n, x - dx)) / dx**2
            e += hermite_fn(n, x) * (-0.5 * d2 + 0.5 * x * x * hermite_fn(n, x)) * dx
        print(f"phi_{n}: norm = {norm:.5f}, energy = {e:.4f} (expected {n+0.5})")
    print(f"n = 10 turning point A = sqrt(21) = {math.sqrt(21):.3f}")


# ---------------------------------------------------------------- figure
W, H = 680, 340


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-osc-title fig-osc-desc">')
    a('<title id="fig-osc-title">Oscillator levels, and a high level compared with a classical spring</title>')
    a('<desc id="fig-osc-desc">Left: a parabola with five evenly spaced energy levels; on each sits a wavefunction with 0, 1, 2, 3 and 4 nodes, extending slightly beyond the parabola walls. Right: for the tenth excited level, the quantum probability density oscillates but follows the classical density, which is lowest at the centre and highest near the turning points.</desc>')
    # left panel
    X0, X1, YB, YT = 30, 330, 300, 30
    XM, EM = 4.0, 5.2
    sx = lambda x: X0 + (X1 - X0) * (x + XM) / (2 * XM)
    sy = lambda e: YB - (YB - YT) * e / EM
    pts = " L".join(f"{sx(x):.1f},{sy(min(EM, x*x/2)):.1f}" for x in [(-XM + 2 * XM * i / 200) for i in range(201)] if x * x / 2 <= EM)
    a(f'<path class="fig-axis" style="stroke-width:2" d="M{pts}"/>')
    for n in range(5):
        E = n + 0.5
        A = math.sqrt(2 * E)
        a(f'<path class="fig-axis" style="stroke-dasharray:4 4" d="M{sx(-A):.1f},{sy(E):.1f} H{sx(A):.1f}"/>')
        pts = " L".join(f"{sx(x):.1f},{sy(E)-26*hermite_fn(n, x):.1f}" for x in [(-XM + 2 * XM * i / 300) for i in range(301)])
        a(f'<path class="fig-curve fig-hot" style="stroke-width:1.6" d="M{pts}"/>')
        a(f'<text class="fig-tick" x="{X1+4}" y="{sy(E)+4:.1f}">n = {n}</text>')
    a(f'<path class="fig-axis" d="M{sx(0):.1f},{sy(0):.1f} v6"/>')
    a(f'<text class="fig-note" x="{(X0+X1)/2}" y="{YB+24}" text-anchor="middle">levels (n + ½)ħω, evenly spaced</text>')
    # right panel
    R0, R1 = 390, 660
    XR = 5.2
    rx = lambda x: R0 + (R1 - R0) * (x + XR) / (2 * XR)
    ry = lambda d: YB - (YB - 80) * d / 0.36
    A = math.sqrt(21)
    a(f'<path class="fig-axis" d="M{R0},{YB} H{R1}"/>')
    q = " L".join(f"{rx(x):.1f},{ry(hermite_fn(10, x)**2):.1f}" for x in [(-XR + 2 * XR * i / 500) for i in range(501)])
    a(f'<path class="fig-curve fig-hot" style="stroke-width:1.6" d="M{q}"/>')
    cl = []
    for i in range(1, 400):
        x = -A + 2 * A * i / 400
        d = 1 / (math.pi * math.sqrt(A * A - x * x))
        if d <= 0.36:
            cl.append(f"{rx(x):.1f},{ry(d):.1f}")
    a(f'<path class="fig-curve fig-classical" d="M{" L".join(cl)}"/>')
    for s in (-1, 1):
        a(f'<path class="fig-axis" style="stroke-dasharray:2 3" d="M{rx(s*A):.1f},{YB} V{ry(0.36):.1f}"/>')
    a(f'<text class="fig-note" x="{(R0+R1)/2}" y="{YB+24}" text-anchor="middle">n = 10: quantum (solid), classical (dashed)</text>')
    a(f'<text class="fig-tick" x="{rx(A)-6:.1f}" y="{ry(0.37):.1f}" text-anchor="end">classical turning point</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "09b-oscillator.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:oscillator generated by scripts/ch09b_oscillator.py -->\n" + figure_svg() + "\n<!-- /FIGURE:oscillator -->"
    new, n = re.subn(r"<!-- FIGURE:oscillator.*?<!-- /FIGURE:oscillator -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:oscillator markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
