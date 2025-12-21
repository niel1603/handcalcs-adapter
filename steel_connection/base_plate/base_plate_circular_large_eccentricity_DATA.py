import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.units.structural_units import *

## Globe main column baseplate
method = 'LRFD'
# Load
# Major P
# P_U = 251.66 * kN
# M_U = 910.1 * kN*m
#Major M
P_U = 176.11 * kN
M_U = 1124.847 * kN*m
# Column
column_dia = 558.8
D = column_dia* mm
# Baseplate
baseplate_offset = 400
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 245 * MPa
# Bolt
bolt_offset = 125
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
A = 242 * mm
A2A1_ratio = 1.5

## Bridge end support
method = 'LRFD'
# Load
# Major P
# P_U = 47.2686 * kN
# M_U = 13.30359 * kN*m
#Major M
P_U = 18.9509 * kN
M_U = 321.3191 * kN*m
# Column
column_dia = 558.8
D = column_dia * mm
# Baseplate
baseplate_offset = 150
N = (column_dia + baseplate_offset*2) * mm # 1558.8
Fy_plate = 240 * MPa
# Bolt
bolt_offset = 75
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
A = 148 * mm # 151
A2A1_ratio = 1.5    

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
# Bolt
bolt_offset = 75
bolt_layer = 1
bolt1_radius = (column_dia + bolt_offset*2)/2 * mm
bolt1_num = 10
bolt2_radius = 0 * mm
bolt2_num = 0
Fy_bolt = 585 * MPa
# Stiffener
stiffener = True
# Concrete
Fc = 30 * MPa
# Assumption
A = 151 * mm # 151
A2A1_ratio = 1.5