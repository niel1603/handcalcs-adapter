import sys
import math
from utils.units.structural_units import *

## Input parameters
'''method = 'ASD'

# Load
P_U = 889.6 * kN
M_U = 56.5 * kN*m

# Column
D = 406.4 * mm

# Baseplate
N = 559 * mm
Fy_plate = 345 * MPa

# Stiffener
stiffener = False

# Concrete
Fc = 20.7 * MPa

# Assumption
A2A1_ratio = 1'''

method = 'LRFD'
# Load
# Major P
P_U = 70.88 * kN
M_U = 2.6 * kN*m
# Column
column_dia = 76.3
D = column_dia* mm
# Baseplate
baseplate_offset = 100
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 240 * MPa
# Stiffener
stiffener = True
# Concrete
Fc = 30 * MPa
# Assumption
A = 175 * mm
A2A1_ratio = 1

# 1. Calculate e and determine loading condition
e = M_U/P_U

if e <= N / 8:
    print('base plate is subjected to small')

elif N / 8 < e < N / 2:
    print('base plate subjected to moderate eccentricities, ' \
    'use different equation')
    sys.exit()

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

# 3. Calculate f1 and f2
numerator1 = P_U
denominator1 = (math.pi * (N ** 2)) / 4
term1 = numerator1 / denominator1

numerator2 = M_U * (N / 2)
denominator2 = (math.pi * (N ** 4)) / 64
term2 = numerator2 / denominator2

f1 = term1 + term2

f2 = term1 - term2

print(f'f1:{f1.to(MPa):.2f}')
print(f'f2:{f2.to(MPa):.2f}')

# 4. Calculate C

if stiffener == True:
    A_chord = 1 * 0.5*D
elif stiffener == False:
    A_chord = 0.8 * 0.5*D

alpha_rad = math.acos((A_chord) / (N/2))

B = 2 * (N/2) * math.sin(alpha_rad)

A_crit = (N / 2)**2 * (2 * alpha_rad - math.sin(2 * alpha_rad)) / 2

term_1 = (2 * math.sin(alpha_rad)**3)
term_2 = 3 * (alpha_rad - math.sin(alpha_rad) * math.cos(alpha_rad))
term_3 = math.cos(alpha_rad)
C = (N / 2) * (term_1 / term_2 - term_3)

print(f'C:{C:.2f}')

# 5. Calculate Mp1

f1 = Fp

bracket_term = f2 + ((N/2 + A_chord + C)/N) * (f1 - f2)
M = bracket_term * A_crit * C

Mp1 = M/B

print(f'Mp1:{Mp1.to(inch*kips / inch):.2f}')

# 6. Calculate tp

if method == 'LRFD':
    tp = ((4 * Mp1) / (0.9 * Fy_plate)) ** 0.5
elif method == 'ASD':
    tp = ((6 * Mp1) / (0.75 * Fy_plate)) ** 0.5 

print(f'tp: {tp.to(mm):.2f}')