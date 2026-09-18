#!/usr/bin/env python3
"""Chapter 01 (blackbody): checked numbers and the generated figure.

Run from the repository root:

    python3 scripts/ch01_blackbody.py            # print the numbers used in the essay
    python3 scripts/ch01_blackbody.py --write    # also regenerate the figure in the chapter

Pure standard library. The figure is inline SVG so that it follows the page's
light/dark theme; --write replaces whatever sits between the FIGURE markers in
chapters/01-blackbody-planck.html.

FIGURE RECORD
  Plotted quantity : spectral energy density per unit WAVELENGTH, u_lambda(lambda, T)
                     u_lambda = (8 pi h c / lambda^5) / (exp(h c / (lambda k T)) - 1)
  Units            : J m^-3 per metre of wavelength; drawn in J m^-3 per micrometre
                     (1 J m^-4 = 1e-6 J m^-3 um^-1)
  Horizontal axis  : wavelength, 0 to 3000 nm (NOT frequency; the frequency form
                     u_nu peaks elsewhere, see X_NU below)
  Curves           : Planck at T = 5800 K, 4500 K, 3500 K (solid)
                     Rayleigh-Jeans at 5800 K, u_lambda = 8 pi k T / lambda^4 (dashed)
  Shaded band      : visible light, 400 to 700 nm
"""
import math
import re
import sys
from pathlib import Path

# CODATA / SI exact values
h = 6.62607015e-34      # J s
c = 299792458.0         # m / s
kB = 1.380649e-23       # J / K
eV = 1.602176634e-19    # J
TO_PLOT = 1e-6          # J m^-4  ->  J m^-3 per micrometre


def u_lambda(lam, T):
    """Planck spectral energy density per unit wavelength, J m^-4."""
    x = h * c / (lam * kB * T)
    if x > 700:
        return 0.0
    return 8 * math.pi * h * c / lam**5 / math.expm1(x)


def u_lambda_rj(lam, T):
    """Rayleigh-Jeans (classical) form, J m^-4."""
    return 8 * math.pi * kB * T / lam**4


def solve(f, lo, hi):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


# Peak conditions. Wavelength form: x = 5 (1 - e^-x). Frequency form: x = 3 (1 - e^-x).
X_LAM = solve(lambda x: x - 5 * (1 - math.exp(-x)), 1, 10)
X_NU = solve(lambda x: x - 3 * (1 - math.exp(-x)), 1, 10)
WIEN_B = h * c / (X_LAM * kB)  # m K


def photon_eV(lam):
    return h * c / lam / eV


def mean_energy_ratio(x):
    """<E> / kT for a quantised oscillator, x = h nu / k T."""
    return x / math.expm1(x)


def report():
    print(f"x at wavelength-form peak  h nu / kT = {X_LAM:.4f}   (1/x = {1/X_LAM:.4f}; Born quotes 0.2014)")
    print(f"x at frequency-form peak   h nu / kT = {X_NU:.4f}")
    print(f"Wien constant b = hc/(x k) = {WIEN_B*1e3:.4f} mm K   (Born quotes 0.290 cm K)")
    print()
    for T in (5800, 4500, 3500, 1000, 310):
        lam = WIEN_B / T
        print(f"T = {T:5d} K : kT = {kB*T/eV:.4f} eV, wavelength peak = {lam*1e9:9.1f} nm, "
              f"quantum there = {photon_eV(lam):.4f} eV, u_lambda peak = {u_lambda(lam, T)*TO_PLOT:.4g} J m^-3 um^-1")
    T = 5800
    nu_pk = X_NU * kB * T / h
    print(f"\nFrequency-form peak at 5800 K: nu = {nu_pk:.3e} Hz, i.e. lambda = {c/nu_pk*1e9:.0f} nm")
    print()
    for name, lam in (("red 700 nm", 700e-9), ("green 550 nm", 550e-9), ("violet 400 nm", 400e-9)):
        nu = c / lam
        print(f"{name:14s}: nu = {nu:.3e} Hz, h nu = {h*nu:.3e} J = {photon_eV(lam):.3f} eV, "
              f"h nu/kT at 1000 K = {h*nu/(kB*1000):.1f}, at 5800 K = {h*nu/(kB*5800):.2f}")
    for T in (1000, 1500, 3000, 5800, 8000, 20000):
        r = u_lambda(400e-9, T) / u_lambda(700e-9, T)
        print(f"u_lambda(400 nm)/u_lambda(700 nm) at {T} K = {r:.3e}")
    print(f"same ratio as T -> infinity (Rayleigh-Jeans) = (700/400)^4 = {(700/400)**4:.2f}")
    print()
    for x in (0.1, 1, 3, 10):
        print(f"<E>/kT at h nu/kT = {x:4}: {mean_energy_ratio(x):.4e}")
    print()
    T = 5800
    for lam_nm in (2000, 1000, 500, 250):
        lam = lam_nm * 1e-9
        print(f"5800 K, {lam_nm:4d} nm: Planck/Rayleigh-Jeans = {u_lambda(lam, T)/u_lambda_rj(lam, T):.4f}")


# ---------------------------------------------------------------- figure
W, H = 680, 400
L, R, TOP, BOT = 70, 20, 20, 56
X_MAX_NM = 3000.0
Y_MAX = 1.4  # J m^-3 um^-1


def sx(lam_nm):
    return L + (W - L - R) * lam_nm / X_MAX_NM


def sy(y):
    return H - BOT - (H - TOP - BOT) * y / Y_MAX


def path(fn, lam_lo, lam_hi, step=10.0, clip=True):
    pts = []
    lam = lam_lo
    while lam <= lam_hi + 1e-9:
        y = fn(lam * 1e-9) * TO_PLOT
        if not clip or y <= Y_MAX * 1.02:
            pts.append(f"{sx(lam):.1f},{sy(min(y, Y_MAX * 1.02)):.1f}")
        lam += step
    return "M" + " L".join(pts)


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-planck-title fig-planck-desc">')
    a('<title id="fig-planck-title">Blackbody spectra at three temperatures, with the classical prediction</title>')
    a('<desc id="fig-planck-desc">Energy density per unit wavelength against wavelength. Each Planck curve rises to a single peak and falls; hotter curves are taller and peak at shorter wavelength. The dashed classical curve for 5800 K matches at long wavelengths but climbs without limit at short ones.</desc>')
    # visible band
    a(f'<rect class="fig-band" x="{sx(400):.1f}" y="{TOP}" width="{sx(700)-sx(400):.1f}" height="{H-TOP-BOT}"/>')
    a(f'<text class="fig-note" x="{(sx(400)+sx(700))/2:.1f}" y="{TOP+14}" text-anchor="middle">visible</text>')
    # axes
    a(f'<path class="fig-axis" d="M{L},{TOP} V{H-BOT} H{W-R}"/>')
    for lam in range(0, 3001, 500):
        a(f'<path class="fig-axis" d="M{sx(lam):.1f},{H-BOT} v5"/>')
        a(f'<text class="fig-tick" x="{sx(lam):.1f}" y="{H-BOT+19}" text-anchor="middle">{lam}</text>')
    for i in range(0, 8):
        y = i * 0.2
        a(f'<path class="fig-axis" d="M{L},{sy(y):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{L-9}" y="{sy(y)+4:.1f}" text-anchor="end">{y:.1f}</text>')
    a(f'<text class="fig-label" x="{(L+W-R)/2:.1f}" y="{H-12}" text-anchor="middle">wavelength λ (nm)</text>')
    a(f'<text class="fig-label" transform="translate(18,{(TOP+H-BOT)/2:.1f}) rotate(-90)" text-anchor="middle">energy density per unit wavelength (J m⁻³ per μm)</text>')
    # curves
    a(f'<path class="fig-curve fig-classical" d="{path(lambda l: u_lambda_rj(l, 5800), 600, 3000)}"/>')
    for T, cls in ((5800, "fig-hot"), (4500, "fig-mid"), (3500, "fig-cool")):
        a(f'<path class="fig-curve {cls}" d="{path(lambda l, T=T: u_lambda(l, T), 40, 3000, clip=False)}"/>')
        lam_pk = WIEN_B / T * 1e9
        a(f'<text class="fig-note" x="{sx(lam_pk)+8:.1f}" y="{sy(u_lambda(lam_pk*1e-9, T)*TO_PLOT)-6:.1f}">{T} K</text>')
    a(f'<text class="fig-note" x="{sx(1150):.1f}" y="{sy(1.25):.1f}">classical prediction, 5800 K</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "01-blackbody-planck.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:planck generated by scripts/ch01_blackbody.py -->\n" + figure_svg() + "\n<!-- /FIGURE:planck -->"
    new, n = re.subn(r"<!-- FIGURE:planck.*?<!-- /FIGURE:planck -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:planck markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
