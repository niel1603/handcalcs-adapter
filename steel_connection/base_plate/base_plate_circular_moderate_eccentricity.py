import sys
import math
from utils.units.structural_units import *

## Input parameters
'''
## Input parameters
method = 'ASD'

# Load
P_U = 889.6 * kN
M_U = 67.8 * kN*m

# Column
D = 406.4 * mm

# Baseplate
N = 559 * mm
Fy_plate = 345 * MPa

# Stiffener
stiffener = False

# Concrete
Fc = 35 * MPa

# Assumption
A = 360 * mm
A2A1_ratio = 1
'''

method = 'LRFD'
# Load
# Major P
# P_U = 471.49 * kN
# M_U = 79.78 * kN*m
#Major M
P_U = 469.72 * kN
M_U = 211.58 * kN*m
# Column
column_dia = 406.4
D = column_dia * mm
# Baseplate
baseplate_offset = 250
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 240 * MPa
# Bolt
bolt_offset = 125
bolt_layer = 1
bolt1_radius = (column_dia + bolt_offset*2)/2 * mm
bolt1_num = 8
bolt2_radius = 0 * mm
bolt2_num = 0
Fy_bolt = 245 * MPa
Fu_bolt = 450 * MPa
# Stiffener
stiffener = True
# Concrete
Fc = 30 * MPa
# Assumption
A = 137 * mm # 151
A2A1_ratio = 1.5  

# if A < N / 2:
#     print("Invalid geometry: segment rise A cannot less than plate radius (N/2)")
#     sys.exit()

# 1. Calculate e and determine loading condition
e = M_U/P_U

if e <= N / 8:
    print('base plate is subjected to small, ' \
    'use different equation')
    sys.exit()

elif N / 8 < e < N / 2:
    print('base plate subjected to moderate eccentricities')

elif N / 2 <= e:
    print('base plate is subjected to large eccentricities, ' \
    'use different equation')
    sys.exit()

# 2. Calculate Fp
phi_c = 0.6

if method == 'LRFD':
    Fp = 0.85 * phi_c * Fc * (A2A1_ratio)**0.5
    Fp_limit = 2 * 0.85 * Fc

elif method == 'ASD':
    Fp = 0.35 * Fc * (A2A1_ratio)**0.5
    Fp_limit = 0.7 * Fc

# Fp = min(Fp, Fp_limit)

if Fp <= Fp_limit :
    print('stress is bellow allowable stress')
if Fp > Fp_limit :
    print('stress exceed allowable stress')
    sys.exit()

print(f'Fp:{Fp.to(MPa):.2f}' )

# 4. Calculate C1 and C2

A_circ = 1/4*math.pi*N**2

alpha2_rad = math.acos((A - N/2) / (N/2))
B2 = 2 * (N/2) * math.sin(alpha2_rad)
A2_crit = A_circ/2 - (N / 2)**2 * (2 * alpha2_rad - math.sin(2 * alpha2_rad)) / 2
C2 = 1 / A2_crit * 2/3 * ((N/2)**3 - ((N/2)**2 - (A-(N/2))**2)**(3/2))

C1 = 2 * N / (3 * math.pi)

print(f'C1:{C1:.2f}' )
print(f'C2:{C2:.2f}' )

# 5. Calculate R1 and R2

f1 = Fp
R1 = f1 * (A - N/2 + C1) / A * (math.pi * N**2) / 8
R2 = f1 * (A - N/2 - C2) / A * A2_crit

R_total = R1 + R2

print(f'R1:{R1.to(kN):.2f}' )
print(f'R2:{R2.to(kN):.2f}' )

difference_percentage = (abs(P_U - R_total) / ((P_U + R_total)/2)) * 100

if difference_percentage < 1 :
    print(f'the percentage difference is: {float(difference_percentage):.2f}%')
elif difference_percentage >= 1 :
    print(f'the percentage difference is exceed 1% : {float(difference_percentage):.2f}%')
    sys.exit()

# 6. Calculate C_crit

if stiffener == True:
    A_chord = 1 * 0.5*D
elif stiffener == False:
    A_chord = 0.8 * 0.5*D

alpha_rad = math.acos((A_chord) / (N/2))

B_crit = 2 * (N/2) * math.sin(alpha_rad)

A_crit = (N / 2)**2 * (2 * alpha_rad - math.sin(2 * alpha_rad)) / 2

def calculate_C(diameter: float, alpha_rad: float) -> float:
    """
    Compute the distance (C) between circle minor segment centers of gravity to the segment chord.

    Args:
        diameter (float): Diameter of the geometry (N).
        alpha_radians (float): Angle in radians.

    Returns:
        float: Distance C.
    """
    
    sin_alpha = math.sin(alpha_rad)
    cos_alpha = math.cos(alpha_rad)

    # Term 1: (2 sin³α) / [3(α - sinα cosα)]
    numerator = 2 * sin_alpha ** 3
    denominator = 3 * (alpha_rad - sin_alpha * cos_alpha)
    term1 = numerator / denominator

    # Term 2: -cosα
    term2 = -cos_alpha

    # Final formula: C = (diameter/2) * [term1 + term2]
    C = (diameter / 2) * (term1 + term2)

    return C

# term_1 = (2 * math.sin(alpha_rad)**3)
# term_2 = 3 * (alpha_rad - math.sin(alpha_rad) * math.cos(alpha_rad))
# term_3 = math.cos(alpha_rad)
# C_crit = (N / 2) * (term_1 / term_2 - term_3)

C_crit = calculate_C(N, alpha_rad)

print(f'C:{C_crit:.2f}')

# 7. Calculate Mp1

bracket_term = ((A - N/2 + A_chord + C_crit)/A)
M = bracket_term * f1 * A_crit * C_crit

Mp1 = M/B_crit

print(f'Mp1:{Mp1.to(inch*kips / inch):.2f}')

# 8. Calculate tp

if method == 'LRFD':
    tp = ((4 * Mp1) / (0.9 * Fy_plate)) ** 0.5
elif method == 'ASD':
    tp = ((6 * Mp1) / (0.75 * Fy_plate)) ** 0.5 

print(f'tp: {tp.to(mm):.2f}')