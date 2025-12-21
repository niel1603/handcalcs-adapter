import sys
import math
from utils.units.structural_units import *



## Bridge column
method = 'LRFD'
# Load
# Major P
P_U = 471.49 * kN
M_U = 79.78 * kN*m
#Major M
# P_U = 469.72 * kN
# M_U = 211.58 * kN*m
# Column
column_dia = 558.8
D = column_dia* mm
# Baseplate
baseplate_offset = 150
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 240 * MPa
# Stiffener
stiffener = True
# Concrete
Fc = 30 * MPa
# Assumption
A = 162 * mm
A2A1_ratio = 1

## Globe ribbon support
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
