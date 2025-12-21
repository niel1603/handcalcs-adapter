import math
from math import pi
import sys

from utils.section_modulus import plastic_section_modulus_pipe

from pint import UnitRegistry
ureg = UnitRegistry()

# HSS_diameter = (6.625 * ureg.inch)
# HSS_thickness = 0.349 * ureg.inch
# Z = 13.8 * ureg.inch**3
# Fy_tube = 50 * ureg.ksi

# t_p = 0.625 * ureg.inch

# bolt_number = 6
# bolt_diameter = 7/8 * ureg.inch
# a = b = 1.5  * ureg.inch
# F_yb = 92 * ureg.ksi

# F_up = 65 * ureg.ksi
# F_nt = 90 * ureg.ksi

HSS_diameter = (508.8 * ureg.millimeter).to(ureg.inch)
HSS_thickness = (15 * ureg.millimeter).to(ureg.inch)
Fy_tube = (250 * ureg.megapascal).to(ureg.ksi)
Z = plastic_section_modulus_pipe(HSS_diameter, HSS_thickness)

t_p = (25 * ureg.millimeter).to(ureg.inch)
F_up = (240 * ureg.megapascal).to(ureg.ksi)

bolt_number = 16
bolt_diameter = (25 * ureg.millimeter).to(ureg.inch)
a = b = (50  * ureg.millimeter).to(ureg.inch)
F_yb = (585 * ureg.megapascal).to(ureg.ksi)
F_nt = (825 * ureg.megapascal).to(ureg.ksi)

nb_prime = bolt_number/3
B_t = F_nt * 1/4 * pi * bolt_diameter ** 2
a_prime = a + bolt_diameter / 2
b_prime = b - bolt_diameter / 2
L_e = HSS_diameter + 2 * b_prime

print(B_t)
print(a_prime)
print(b_prime)
print(L_e)

# end plate thickness
t_preq = ((4 * nb_prime * B_t * b_prime) / (F_up * L_e)) **  0.5
print(t_preq)

if t_p > t_preq:
    print("bolt spacing or edge distance does NOT meet end plate thicknes requirements.")
    sys.exit()

# bolt spacing
end_plate_circumference = pi * (HSS_diameter + b * 2)
bolt_arc_spacing = end_plate_circumference / bolt_number

min_spacing = 3 * bolt_diameter
edge_to_hole = 1.25 * ureg.inch

if bolt_arc_spacing < min_spacing:
    print("bolt spacing or edge distance does NOT meet minimum spacing requirements AISC Spec. Section J3.3.")
    sys.exit()

elif a < edge_to_hole:
    print("bolt spacing or edge distance does NOT meet minimum edge to hole distance requirements AISC Spec. Section J3.4.")
    sys.exit()

print('bolt spacing meets minimum spacing requirements AISC Spec. Section J3.3')
print('bolt spacing meets minimum edge to hole distance requirements AISC Spec. Section J3.4')

# available moment capacitt for bolt failure limit state

# Bolt term
bolt_term = nb_prime * HSS_diameter * (3 * B_t * a_prime + (3 * pi * bolt_diameter**3 * F_yb) / 32)

# Plate term
plate_term = 0.75 * F_up * t_p**2 * L_e * (HSS_diameter + 2 * a + 2 * b)

# Total available moment
M_available_bolt_limitstate = (bolt_term + plate_term) / (4 * (a + b))

print(f"M_available_bolt_limitstate = {M_available_bolt_limitstate}")
print(f"M_available_bolt_limitstate = {M_available_bolt_limitstate.to('kilonewton * meter')}")

# available moment capacitt for end-plate plastification limit state

# First term: bolt contribution
bolt_term = nb_prime * HSS_diameter * ((3 * pi * bolt_diameter**3 * F_yb) / 32)

# Second term: plate contribution
plate_term = 1.5 * F_up * t_p**2 * L_e * (HSS_diameter + b_prime)

# Total available moment
M_available_end_plate_limitstate = (bolt_term + plate_term) / (4 * b_prime)

print(f"M_available_end_plate_limitstate = {M_available_end_plate_limitstate}")
print(f"M_available_end_plate_limitstate = {M_available_end_plate_limitstate.to('kilonewton * meter')}")

M_available = min(M_available_bolt_limitstate, M_available_end_plate_limitstate)

print(f"M_available = {M_available}")
print(f"M_available = {M_available.to('kilonewton * meter')}")

# proportion of connection available moment capacity to tube available design strength

E = 29000 * ureg.ksi
theta = 0.9

if HSS_diameter / HSS_thickness <= 0.07 * (E / Fy_tube):
    print('HSS is compact')
    thetaMn = 0.9 * Fy_tube * Z
else:
    print('\n!!! WARNING !!!\n')
    print('HSS is not compact')

print(thetaMn.to('kip * inch'))
print(thetaMn.to('kilonewton * meter'))
print(f'ratio: {float(M_available / thetaMn) * 100:.2f}%')