# ---------------------------------------------
# Fillet Weld Shear Strength Calculation
# Perpendicular to Weld Length (Transverse Shear)
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
Fexx_mpa = 490.0

# Load direction angle to weld axis (degrees)
# 90° = perpendicular to weld length
theta_deg = 90.0

# ---------------------------------------------
# CALCULATION
# ---------------------------------------------

# Effective throat thickness (mm)
a_mm = 0.707 * z_mm

# Effective shear area (mm²)
Aw_mm2 = a_mm * L_mm

# AISC baseline weld shear stress (MPa)
fvw_base_mpa = 0.60 * Fexx_mpa

# Directional strength increase factor
theta_rad = math.radians(theta_deg)
direction_factor = 1.0 + 0.50 * (math.sin(theta_rad) ** 1.5)

# Increased shear stress (MPa)
fvw_mpa = fvw_base_mpa * direction_factor

# Weld shear capacity
V_n = Aw_mm2 * fvw_mpa      # Newton
V_kn = V_n / 1_000          # kiloNewton

# ---------------------------------------------
# OUTPUT
# ---------------------------------------------

print("FILLET WELD SHEAR STRENGTH (TRANSVERSE)")
print("--------------------------------------")
print(f"Weld size z              = {z_mm:.2f} mm")
print(f"Weld length L            = {L_mm:.2f} mm")
print(f"Ultimate strength Fexx   = {Fexx_mpa:.1f} MPa")
print(f"Load angle theta         = {theta_deg:.1f} deg")
print()
print(f"Throat thickness a       = {a_mm:.3f} mm")
print(f"Effective area Aw        = {Aw_mm2:.1f} mm²")
print(f"Base shear stress        = {fvw_base_mpa:.1f} MPa")
print(f"Direction factor         = {direction_factor:.2f}")
print(f"Increased shear stress   = {fvw_mpa:.1f} MPa")
print()
print(f"Weld shear capacity      = {V_n:,.0f} N")
print(f"Weld shear capacity      = {V_kn:.2f} kN")
