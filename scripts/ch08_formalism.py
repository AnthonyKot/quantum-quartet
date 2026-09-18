#!/usr/bin/env python3
"""Chapter 08 (formalism): checked numbers for the two-state ammonia example.

    python3 scripts/ch08_formalism.py

Pure standard library. No generated figure: the ammonia diagram in the chapter is a
hand-drawn schematic (not to scale), so there is nothing quantitative to regenerate.

Model (the chapter writes the coupling A as C): basis states |up>, |down> (nitrogen above / below the plane of the hydrogens).
Energy matrix H = [[E0, -A], [-A, E0]], A > 0. Eigenstates
|I>  = (|up> + |down>)/sqrt2, energy E0 - A
|II> = (|up> - |down>)/sqrt2, energy E0 + A
The splitting 2A is fixed from the ammonia maser line, 23.87 GHz (the (3,3) inversion line).
"""
import math

h = 6.62607015e-34
eV = 1.602176634e-19
NU = 23.87e9

split = h * NU / eV
A = split / 2
print(f"2A = h nu = {split:.4e} eV = {split*1e6:.2f} micro-eV;  A = {A*1e6:.2f} micro-eV")
print(f"wavelength of the maser line = {299792458/NU*100:.3f} cm")

I = (1 / math.sqrt(2), 1 / math.sqrt(2))
II = (1 / math.sqrt(2), -1 / math.sqrt(2))


def matvec(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


# work in units: E0 = 0, A = 1 (so energies are E0 + (number) * A)
Hm = ((0.0, -1.0), (-1.0, 0.0))
print("check eigenvectors: H|I> =", matvec(Hm, I), " = -1 x |I>;  H|II> =", matvec(Hm, II), " = +1 x |II>")
for name, psi in (("up", (1.0, 0.0)), ("30 deg", (math.cos(math.radians(30)), math.sin(math.radians(30)))),
                  ("(0.6, 0.8)", (0.6, 0.8))):
    aI, aII = dot(I, psi), dot(II, psi)
    Hpsi = matvec(Hm, psi)
    print(f"state {name}: <I|psi> = {aI:.4f}, <II|psi> = {aII:.4f}; P(E0-A) = {aI**2:.4f}, P(E0+A) = {aII**2:.4f}")
    print(f"    <E> from probabilities = E0 + ({-aI**2 + aII**2:+.4f}) A ;  H psi = ({Hpsi[0]:.4f}, {Hpsi[1]:.4f}) A;"
          f"  <psi|H psi> = E0 + ({dot(psi, Hpsi):+.4f}) A")
    sd = math.sqrt(1 - (aII**2 - aI**2) ** 2)
    print(f"    spread (standard deviation) of E = {sd:.4f} A")

sz = ((1, 0), (0, -1))
sx = ((0, 1), (1, 0))
mm = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
print("HV-observable times DA-observable:", mm(sz, sx), " reversed:", mm(sx, sz))

# Heisenberg-picture oscillation: starting |up>, P(up) = cos^2(A t / hbar), period of <up-down> = h / (2A) = 1/nu
print(f"starting in |up>, the nitrogen returns every 1/nu = {1/NU*1e12:.1f} ps")
