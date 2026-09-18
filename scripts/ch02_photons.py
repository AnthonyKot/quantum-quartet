#!/usr/bin/env python3
"""Chapter 02 (photons): checked numbers and the generated figure.

    python3 scripts/ch02_photons.py            # print the numbers used in the essay
    python3 scripts/ch02_photons.py --write    # also regenerate the figure in the chapter

Pure standard library. --write replaces what sits between the FIGURE:threshold
markers in chapters/02-photons.html.

Work functions are typical handbook values for clean surfaces; measured values vary
by a few tenths of an eV with surface preparation, so the essay says "about".

FIGURE RECORD
  Plotted quantity : maximum kinetic energy of photoelectrons, K_max = h nu - W, in eV
                     (drawn only where positive; below threshold no electrons emerge)
  Horizontal axis  : light frequency nu, 0 to 15 x 10^14 Hz
  Parameters       : sodium W = 2.3 eV, zinc W = 4.3 eV
  Shaded band      : visible light, 400 to 700 nm (4.28 to 7.49 x 10^14 Hz)
  Slope            : h / e = 4.136 x 10^-15 eV s, identical for both metals
"""
import math
import re
import sys
from pathlib import Path

h = 6.62607015e-34       # J s
c = 299792458.0          # m / s
eV = 1.602176634e-19     # J
m_e = 9.1093837015e-31   # kg

W_NA = 2.3   # eV
W_ZN = 4.3   # eV


def photon_eV(lam):
    return h * c / lam / eV


def report():
    print(f"hc = {h*c/eV*1e9:.2f} eV nm")
    for name, lam in (("red 700 nm", 700e-9), ("red laser 650 nm", 650e-9), ("blue 450 nm", 450e-9),
                      ("violet 400 nm", 400e-9), ("UV 300 nm", 300e-9), ("UV 250 nm", 250e-9)):
        E = photon_eV(lam)
        print(f"{name:17s}: nu = {c/lam:.3e} Hz, E = {E:.3f} eV, "
              f"K_max Na = {E-W_NA:+.2f} eV, K_max Zn = {E-W_ZN:+.2f} eV")
    for name, W in (("sodium", W_NA), ("zinc", W_ZN)):
        lam0 = h * c / (W * eV)
        print(f"{name}: threshold nu0 = {W*eV/h:.3e} Hz, lambda0 = {lam0*1e9:.0f} nm")
    K = photon_eV(450e-9) - W_NA
    v = math.sqrt(2 * K * eV / m_e)
    print(f"blue on sodium: K_max = {K:.2f} eV, stopping potential = {K:.2f} V, speed = {v:.3e} m/s")
    P = 1e-3
    print(f"1 mW red laser (650 nm): {P/(photon_eV(650e-9)*eV):.2e} photons per second")
    print(f"slope h/e = {h/eV:.4e} eV s = {h/eV*1e14:.4f} eV per 10^14 Hz")
    print()
    lam_c = h / (m_e * c)
    print(f"Compton wavelength h/(m_e c) = {lam_c*1e12:.4f} pm")
    for deg in (0, 90, 180):
        print(f"  shift at {deg:3d} deg = {lam_c*(1-math.cos(math.radians(deg)))*1e12:.3f} pm")
    lam_x = 71.0e-12
    print(f"X-ray 71 pm: photon energy = {photon_eV(lam_x)/1e3:.1f} keV; 90 deg shift is {lam_c/lam_x*100:.2f} % of lambda")
    lam_x2 = lam_x + lam_c
    print(f"  scattered at 90 deg: {lam_x2*1e12:.2f} pm; electron recoil energy = {(photon_eV(lam_x)-photon_eV(lam_x2)):.0f} eV")
    lam_v = 500e-9
    print(f"visible 500 nm: 90 deg shift is {lam_c/lam_v*100:.2e} % of lambda")
    print()
    p_red = h / 700e-9
    print(f"photon momentum at 700 nm: p = h/lambda = {p_red:.3e} kg m/s")


# ---------------------------------------------------------------- figure
W, H = 680, 360
LM, RM, TOP, BOT = 62, 20, 18, 56
NU_MAX = 15.0   # units of 1e14 Hz
K_MAX = 4.0     # eV


def sx(nu14):
    return LM + (W - LM - RM) * nu14 / NU_MAX


def sy(k):
    return H - BOT - (H - TOP - BOT) * k / K_MAX


def line(Wf):
    slope = h / eV * 1e14          # eV per 1e14 Hz
    nu0 = Wf / slope
    nu1 = min(NU_MAX, (K_MAX + Wf) / slope)
    return nu0, f"M{sx(nu0):.1f},{sy(0):.1f} L{sx(nu1):.1f},{sy(slope*nu1-Wf):.1f}"


def figure_svg():
    o = []
    a = o.append
    a(f'<svg class="fig-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig-thr-title fig-thr-desc">')
    a('<title id="fig-thr-title">Maximum electron energy against light frequency for sodium and zinc</title>')
    a('<desc id="fig-thr-desc">Two parallel straight lines. Each is zero up to a threshold frequency, which is in the green for sodium and in the ultraviolet for zinc, and rises steadily beyond it with the same slope, Planck\'s constant.</desc>')
    v_lo, v_hi = c / 700e-9 / 1e14, c / 400e-9 / 1e14
    a(f'<rect class="fig-band" x="{sx(v_lo):.1f}" y="{TOP}" width="{sx(v_hi)-sx(v_lo):.1f}" height="{H-TOP-BOT}"/>')
    a(f'<text class="fig-note" x="{(sx(v_lo)+sx(v_hi))/2:.1f}" y="{TOP+14}" text-anchor="middle">visible</text>')
    a(f'<path class="fig-axis" d="M{LM},{TOP} V{H-BOT} H{W-RM}"/>')
    for n in range(0, 16, 3):
        a(f'<path class="fig-axis" d="M{sx(n):.1f},{H-BOT} v5"/>')
        a(f'<text class="fig-tick" x="{sx(n):.1f}" y="{H-BOT+19}" text-anchor="middle">{n}</text>')
    for k in range(0, 5):
        a(f'<path class="fig-axis" d="M{LM},{sy(k):.1f} h-5"/>')
        a(f'<text class="fig-tick" x="{LM-9}" y="{sy(k)+4:.1f}" text-anchor="end">{k}</text>')
    a(f'<text class="fig-label" x="{(LM+W-RM)/2:.1f}" y="{H-12}" text-anchor="middle">frequency of the light ν (10¹⁴ Hz)</text>')
    a(f'<text class="fig-label" transform="translate(18,{(TOP+H-BOT)/2:.1f}) rotate(-90)" text-anchor="middle">maximum electron energy (eV)</text>')
    for Wf, cls, name in ((W_NA, "fig-hot", "sodium"), (W_ZN, "fig-mid", "zinc")):
        nu0, d = line(Wf)
        a(f'<path class="fig-curve {cls}" d="{d}"/>')
        a(f'<circle cx="{sx(nu0):.1f}" cy="{sy(0):.1f}" r="3.5" class="fig-dot"/>')
        k_lab = 3.4 if name == "sodium" else 1.4
        nu_lab = (k_lab + Wf) / (h / eV * 1e14)
        a(f'<text class="fig-note" x="{sx(nu_lab)+10:.1f}" y="{sy(k_lab)+4:.1f}">{name}</text>')
    # blue-on-sodium worked point
    nu_b = c / 450e-9 / 1e14
    kb = h / eV * nu_b * 1e14 - W_NA
    a(f'<path class="fig-axis" style="stroke-dasharray:3 4" d="M{sx(nu_b):.1f},{sy(0):.1f} V{sy(kb):.1f} H{LM}"/>')
    a(f'<circle cx="{sx(nu_b):.1f}" cy="{sy(kb):.1f}" r="3.5" class="fig-dot"/>')
    a(f'<text class="fig-note" x="{sx(nu_b)-8:.1f}" y="{sy(kb)-10:.1f}" text-anchor="end">blue, 450 nm</text>')
    a(f'<text class="fig-note" x="{sx(7.9):.1f}" y="{sy(3.3):.1f}">parallel lines: same slope, h</text>')
    a('</svg>')
    return "\n".join(o)


def write_figure():
    page = Path(__file__).resolve().parent.parent / "chapters" / "02-photons.html"
    html = page.read_text(encoding="utf-8")
    block = "<!-- FIGURE:threshold generated by scripts/ch02_photons.py -->\n" + figure_svg() + "\n<!-- /FIGURE:threshold -->"
    new, n = re.subn(r"<!-- FIGURE:threshold.*?<!-- /FIGURE:threshold -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("FIGURE:threshold markers not found exactly once in the chapter")
    page.write_text(new, encoding="utf-8")
    print(f"figure written into {page}")


if __name__ == "__main__":
    report()
    if "--write" in sys.argv:
        write_figure()
