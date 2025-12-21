import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import math
from typing import List, Tuple
from utils.units.structural_units import *

## Input parameters
'''method = 'ASD'
# Load
P_U = 889.6 * kN
M_U = 2260 * kN*m
# Column
D = 1067 * mm
# Baseplate
N = 1524 * mm
Fy_plate = 345 * MPa
# Bolt
bolt_layer = 1
bolt1_radius = 647.7 * mm
bolt1_num = 13
bolt2_radius = 0 * mm
bolt2_num = 0
# Stiffener
stiffener = True
# Concrete
Fc = 35 * MPa
# Assumption
A = 460 * mm
A2A1_ratio = 1.5
'''

method = 'LRFD'
# Load
# Major P
# P_U = 251.66 * kN
# M_U = 910.1 * kN*m
#Major M
P_U = 180.11 * kN
M_U = 1124.847 * kN*m
# Column
column_dia = 558.8
D = column_dia* mm
# Baseplate
baseplate_offset = 400
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 245 * MPa
# Bolt
bolt_offset = 100
bolt_layer = 2
bolt1_radius = (column_dia + bolt_offset*2)/2 * mm
bolt1_num = 5
bolt2_radius = (column_dia + baseplate_offset*2 - bolt_offset*2)/2 * mm
bolt2_num = 8
Fy_bolt = 245 * MPa
Fu_bolt = 450 * MPa
# Stiffener
stiffener = True
# Concrete
Fc = 30 * MPa
# Assumption
A = 260 * mm
A2A1_ratio = 1.25
 
if A > N / 2:
    print("Invalid geometry: segment rise A cannot exceed plate radius (N/2)")
    sys.exit()

# 1. Calculate e and determine loading condition
e = M_U/P_U

if e <= N / 8:
    print('base plate is subjected to small, ' \
    'use different equation')
    sys.exit()

elif N / 8 < e < N / 2:
    print('base plate subjected to moderate eccentricities, ' \
    'use different equation')
    sys.exit()

elif N / 2 <= e:
    print('base plate is subjected to large eccentricities')


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

# 3. Calculate A'

def sum_tension_bolt_distances(radius: float, num_bolts: int, verbose: bool = False) -> Tuple[float, float]:
    """
    """
    if num_bolts % 2 == 0 :
        offset = 180 / (num_bolts)
    else:
        offset = 0

    angle = 180 - offset
    angle_increment = angle / (num_bolts - 1)

    distances: List[float] = []

    for i in range(num_bolts):
        angle_deg = i * angle_increment + offset / 2
        angle_rad = math.radians(angle_deg)
        distance = radius * math.sin(angle_rad)
        distances.append(distance)

        if verbose:
            print(f'Bolt {i+1}: Angle = {angle_deg:.2f}°, Distance = {distance:.2f}')

    sum_distance = sum(distances)

    max_distance = max(distances)

    return sum_distance, max_distance 

A_prime2 = 0 
total_bolts2 = 0

sum_distance1, max_distance1 = sum_tension_bolt_distances(bolt1_radius, bolt1_num, verbose=True)
total_bolts1 = bolt1_num - 2
A_prime1 = (sum_distance1) / (total_bolts1)
max_distance = max_distance1
sum_distance = sum_distance1
print(f'A_prime1: {A_prime1:.2f}\n')

if bolt_layer == 2:
    sum_distance2, max_distance2 = sum_tension_bolt_distances(bolt2_radius, bolt2_num, verbose=True)
    total_bolts2 = bolt2_num
    A_prime2 = (sum_distance2) / (total_bolts2)
    sum_distance = (sum_distance1 + sum_distance2)
    max_distance = max(max_distance1, max_distance2)
    print(f'A_prime2: {A_prime2:.2f}\n')

A_prime_total = (A_prime1 * total_bolts1 + A_prime2 * total_bolts2) / (total_bolts1 + total_bolts2)
print(f'A_prime_total: {A_prime_total:.2f}')

# 4. Calculate C

A_circ = 1/4*math.pi*N**2

alpha_rad = math.acos((N/2 - A) / (N/2))
B = 2 * (N/2) * math.sin(alpha_rad)

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
# C = (N / 2) * (term_1 / term_2 - term_3)

C = calculate_C(N, alpha_rad)

print(f'C:{C:.2f}')


# 5. Check the state of equilibrium

A_crit = (N / 2)**2 * (2 * alpha_rad - math.sin(2 * alpha_rad)) / 2

left_side = P_U * (e + A_prime_total)
right_side = Fp * (C / A) * A_crit * (N / 2 - (A - C) + A_prime_total)

difference_percentage = (abs(left_side - right_side) / 
                         ((left_side + right_side)/2)) * 100

if difference_percentage < 1 :
    print(f'the percentage difference is: {float(difference_percentage):.2f}%')
elif difference_percentage >= 1 :
    print(f'the percentage difference is exceed 1% : {float(difference_percentage):.2f}%')
    sys.exit()

# 6. Calculate Tmax

T = Fp * C / A * A_crit - P_U
T_max = T * max_distance / (sum_distance)

# Calculate anchor diameter and hook length according to AISC Design Guide 2003
phi_t = 0.75
Dbolt = (T_max / (0.75 * phi_t * 1/4*math.pi * Fu_bolt))**0.5
# Dbolt = 42 * mm
Lh = (T_max / 2) / (0.7 * Fc * Dbolt)
Hh = 35 * Dbolt # According to office standard detail

print(f'T_max: {T_max.to(kN):.3f}')
print(f'Dbolt: {Dbolt:.3f}')
print(f'Lh: {Lh:.3f}')
print(f'Hh: {Hh:.3f}')

# 7. Calculate C_crit

if stiffener == True:
    A_chord = 1 * 0.5*D
elif stiffener == False:
    A_chord = 0.8 * 0.5*D

alpha_rad = math.acos((A_chord) / (N/2))

B_crit = 2 * (N/2) * math.sin(alpha_rad)

A_crit = (N / 2)**2 * (2 * alpha_rad - math.sin(2 * alpha_rad)) / 2

# term_1 = (2 * math.sin(alpha_rad)**3)
# term_2 = 3 * (alpha_rad - math.sin(alpha_rad) * math.cos(alpha_rad))
# term_3 = math.cos(alpha_rad)
# C_crit = (N / 2) * (term_1 / term_2 - term_3)

C_crit = calculate_C(N, alpha_rad)

print(f'C_crit:{C_crit:.2f}')

# 7. Calculate Mp1

f1 = Fp
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
print(f'tp: {tp.to(inch):.2f}')