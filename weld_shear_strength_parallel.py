# ---------------------------------------------
# Fillet Weld Shear Strength Calculation
# Metric Units (mm, MPa, N, kN)
# ---------------------------------------------

import math

# ---------------------------------------------
# INPUT DATA
# ---------------------------------------------

# Fillet weld leg size (mm)
z_mm = 6.0

# Effective weld length (mm)
L_mm = 60 * 2 # two side fillet weld

# Ultimate tensile strength of weld metal (MPa = N/mm²)
# Example:
# E60 -> 410 MPa
# E70 -> 490 MPa
fu_mpa = 490.0

# ---------------------------------------------
# CALCULATION
# ---------------------------------------------

# Effective throat thickness (mm)
a_mm = 0.707 * z_mm

# Effective shear area (mm²)
Aw_mm2 = a_mm * L_mm

# Design shear stress of weld metal (MPa)
fvw_mpa = fu_mpa / math.sqrt(3)

# Weld shear capacity
V_n = Aw_mm2 * fvw_mpa      # Newton
V_kn = V_n / 1_000          # kiloNewton

# ---------------------------------------------
# OUTPUT
# ---------------------------------------------

print("FILLET WELD SHEAR STRENGTH (METRIC)")
print("----------------------------------")
print(f"Weld size z           = {z_mm:.2f} mm")
print(f"Weld length L         = {L_mm:.2f} mm")
print(f"Ultimate strength fu  = {fu_mpa:.1f} MPa")
print()
print(f"Throat thickness a   = {a_mm:.3f} mm")
print(f"Effective area Aw    = {Aw_mm2:.1f} mm²")
print(f"Shear stress fvw     = {fvw_mpa:.1f} MPa")
print()
print(f"Weld shear capacity  = {V_n:,.0f} N")
print(f"Weld shear capacity  = {V_kn:.2f} kN")
