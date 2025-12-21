
import math
import forallpeople as fp
from utils.units.structural_units_forallpeople import SI, US, to_unit, safe_sqrt

# ============================================================
# BASED ON DESIGN GUIDE 39 
# EXAMPLE B.3-2 PAGE 314 
# ============================================================

print(f"\n=====================================")
print("STEEL CONNECTION CHECK")
print("FOUR BOLT EXTENDED STIFFENED THIN END-PLATE")
print(f"=====================================\n")

# Load LRFD
M_u  = 7620 * US.kip * US.inch
T_u  = 20.4 * US.kip
V_u  = 45.8 * US.kip
V_uc = 19.6 * US.kip

print(f"Load Design:")
print(f"Moment                  : {M_u}")
print(f"Axial tension           : {T_u}")
print(f"Shear force             : {V_u}")
print(f"Column shear            : {V_uc}")

print(f"\n-------------------------------------\n")

# Materail properties
# Steel
E = 29000 * US.ksi
# Beam and column
F_y_beam_column = 50 * US.ksi
F_u_beam_column = 65 * US.ksi
# Plate
F_y_plate = 50 * US.ksi
F_u_plate = 65 * US.ksi
# Stiffener
F_y_stiffener = 50 * US.ksi
F_u_stiffener = 65 * US.ksi
# Bolt
F_nt_bolt = 113 * US.ksi
F_nv_bolt = 68 * US.ksi

# Bolt pretension force
T_b = 102 * US.kip # For grade A490 bolt according to AISC Specification Table J3.1

print(f"Material properteis:")

print(f"\nSteel:")
print(f"E                       : {E}")

print(f"\nBeam:")
print(f"Fy beam and column      : {F_y_beam_column}")
print(f"Fu beam and column      : {F_u_beam_column}")

print(f"\nPlate:")
print(f"Fy plate                : {F_y_plate}")
print(f"Fu plate                : {F_u_plate}")

print(f"\nBolt:")
print(f"Fnt bolt                : {F_nt_bolt}")
print(f"Fnv bolt                : {F_nv_bolt}")

print(f"\n-------------------------------------\n")

# Geometry properties
# Beam
d_b = 24.1 * US.inch # web height
b_bf = 9.02 * US.inch # flange width
t_bw = 0.470 * US.inch # web thick
t_bf = 0.770 * US.inch # flange thick

# Column
d_c = 14.2 * US.inch # web height
b_cf = 14.6 * US.inch # flange width
t_cw = 0.485 * US.inch # web thick
t_cf = 0.780 * US.inch # flange thick
k_des = 1.38 * US.inch # distance from outer face of flange to web toe of fillet used for design

# End plate geometric properties
b_p = 9 * US.inch # width plate
t_p = 7/8  * US.inch # thick plate

# Bolt geometric properties
d_bolt = (1+1/4) * US.inch # bolt diameter
clearance = 1/8 * US.inch # bolt clearance
d_hole = (d_bolt + clearance) # hole diameter

# Bolt configuration geometric properties
g = (5+3/4) * US.inch # width bolt hole 
p_ext = (4+1/2) * US.inch # distance from top side of plate to top of beam 
d_e = (1+3/4) * US.inch # distance from top side of plate to bolt hole
p_fo = (2+3/4) * US.inch # distance from top side of beam to bolt hole
p_fi = 2 * US.inch # distance from inner top side of beam (bottom of flange) to inner bolt hole
d_p = (33+1/8) * US.inch # height bolt hole

# Stiffener geometric properties
t_s = 1/2 * US.inch # thick stiffener
L_st = 8 * US.inch # stiffener length
h_st = (4+1/2) * US.inch # thick stiffener heigth

print(f"Geometry properteis:")

print(f"\nBeam:")
print(f"db beam                 : {d_b}")
print(f"b_bf beam               : {b_bf}")
print(f"t_bw beam               : {t_bw}")
print(f"t_bf beam               : {t_bf}")

print(f"\nColumn:")
print(f"dc column               : {d_c}")
print(f"b_cf column             : {b_cf}")
print(f"t_cw column             : {t_cw}")
print(f"t_cf column             : {t_cf}")
print(f"k_des column            : {k_des}")

print(f"\nEnd plate:")
print(f"b_p plate               : {b_p}")
print(f"t_p plate               : {t_p}")

print(f"\nBolt:")
print(f"d_bol bolt              : {d_bolt}")
print(f"clearance               : {clearance}")
print(f"d_hole bolt             : {d_hole}")

print(f"\nBolt configuration:")
print(f"g bolt                  : {g}")
print(f"p_ext bolt              : {p_ext}")
print(f"d_e bolt                : {d_e}")
print(f"p_fo bolt               : {p_fo}")
print(f"p_fi bolt               : {p_fi}")
print(f"d_p bolt                : {d_p}")

print(f"\nStiffenen:")
print(f"t_s stiffenen           : {t_s}")
print(f"L_st stiffenen          : {L_st}")
print(f"h_st stiffenen          : {h_st}")


print(f"\n=====================================")
print("CALCULATION START")
print(f"=====================================\n")

# =====================================================
# 1) Distance from compression flange CL to bolt line
# =====================================================

print("1) Distance from compression flange CL to bolt line")

# Formula / Requirement
print("Distance from h_1:")
print("  h_1 = d_b - (t_bf / 2) + p_fo")
print("Distance from h_2:")
print("  h_2 = d_b - (3 * t_bf / 2) - p_fi")

# Substitution
print("Substitution:")
print(f"  h_1 = {d_b} - ({t_bf} / 2) + {p_fo}")
print(f"  h_2 = {d_b} - (3 * {t_bf} / 2) - {p_fi}")

# Result
print("Result:")
h_1 = d_b - (t_bf / 2) + p_fo
h_2 = d_b - (3 * t_bf / 2) - p_fi

print(f"h1 = {h_1}")
print(f"h2 = {h_2}")

# -----------------------------------------------------
# 1.1) Plate width check
# -----------------------------------------------------

print("\n1.1) Plate width check")

# Formula / Requirement
print("Requirement:")
print("  b_p ≤ b_bf + max(t_p, 1 in)")

# Substitution
print("Substitution:")
print(f"  {b_p} ≤ {b_bf} + max({t_p}, {1 * US.inch})")

# Result
print("Result:")
b_p_limit = b_bf + max(t_p, 1 * US.inch)

if b_p <= b_p_limit:
    print(f"Result: {b_p} ≤ {b_p_limit}  → OK")
else:
    raise ValueError(f"Result: {b_p} > {b_p_limit}  → NOT OK")


# -----------------------------------------------------
# 1.2) Beam flange width check
# -----------------------------------------------------

print("\n1.2) Beam flange width check")

# Formula / Requirement
print("Requirement:")
print("  b_bf ≥ g")

# Substitution
print("Substitution:")
print(f"  b_bf ≥ {g}")

# Result
print("Result:")
b_bf_limit = g

if b_bf >= b_bf_limit:
    print(f"Result: {b_bf} ≥ {b_bf_limit}  → OK")
else:
    raise ValueError(f"Result: {b_bf} < {b_bf_limit}  → NOT OK")

# =====================================================
# 2) Beam flange to end-plate stiffener geometric properties
# =====================================================

print("\n2) Beam flange to end-plate stiffener geometric properties")

# -----------------------------------------------------
# 2.1) Stiffener length check
# -----------------------------------------------------

print("\n2.1) Stiffener length check")

# Formula / Requirement
print("Requirement:")
print(f"  h_st = p_ext = {h_st}")
print(f"  L_st_min ≤ L_st")
print(f"  h_st / tan(30°) ≤ L_st")

# Substitution
print("Substitution:")
print(f"  {h_st} / tan(30°) ≤ {L_st}")

# Result
L_st_min = h_st / math.tan(math.radians(30))

if L_st_min <= L_st:
    print(f"Result: {L_st_min} ≤ {L_st}  → OK")
else:
    raise ValueError(f"Result: {L_st_min} > {L_st}  → NOT OK")

# -----------------------------------------------------
# 2.2) Stiffener thickness check
# -----------------------------------------------------

print("\n2.2) Stiffener thickness check")

# Formula / Requirement
print("Requirement:")
print("  t_s ≥ t_s_min")
print("  t_s ≥ t_bw(F_yb / F_ys)")

print("Substitution:")
print(f"  t_s ≥ {t_bw}({F_y_beam_column} / {F_y_stiffener})")

# Result
t_s_min = t_bw*(F_y_beam_column / F_y_stiffener)

if t_s >= t_s_min:
    print(f"Result: {t_s} ≥ {t_s_min}  → OK")
else:
    raise ValueError(f"Result: {t_s} < {t_s_min}  → NOT OK")

# -----------------------------------------------------
# 2.3) Stiffener slender check
# -----------------------------------------------------

print("\n2.3) Stiffener slender check")

# Formula / Requirement
print("Requirement:")
print("  h_st / t_s ≤ 0.56 √(E / F_y_stiffener)")

print("Substitution:")
print(f"  {h_st} / {t_s} ≤ 0.56 √({E} / {F_y_stiffener})")

# Result
slenderness_actual = h_st / t_s
slenderness_limit = 0.56 * safe_sqrt(E / F_y_stiffener)

if slenderness_actual <= slenderness_limit:
    print(f"Result: {slenderness_actual} ≤ {slenderness_limit}  → OK")
else:
    raise ValueError(
        f"Result: {slenderness_actual} > {slenderness_limit}  → NOT OK"
    )

# =====================================================
# A) End-Plate and Bolt Design Verification
# =====================================================

print("\nA) End-Plate and Bolt Design Verification")

# -----------------------------------------------------
# A.1) Calculate equivalent required moment
# -----------------------------------------------------

print("\nA.1) Calculate equivalent required moment consider the effect of the required tensile force using Eq.3-30")

# Formula / Requirement
print("Equivalent required moment:")
print("  M_u_eq = M_u + (T_u / 2) * (d_b - t_bf)")

# Substitution
print("Substitution:")
print(f"  M_u_eq = {M_u} + ({T_u} / 2) * ({d_b} - {t_bf})")

# Result
print(f"Result:")
M_u_eq = M_u + (T_u / 2) * (d_b - t_bf)
print(f"  M_u_eq = {M_u_eq}")

# -----------------------------------------------------
# A.2) Determine if the specified end-plate and bolt are 
#      sufficient using the thin end/plate bolt diameter 
#      procedure
# -----------------------------------------------------

print("\nA.2) Determine if the specified end-plate and bolt are sufficient using the thin end/plate bolt diameter procedure")

# Formula / Requirement
print("Distance between inner bolt hole to bottom yiel line parameter:")
print("  s = √(b_p * g) / 2")
print("  s > d_e")
print("  s ≥ p_fo")
print("  s ≥ p_fi")


# Substitution
print("Substitution:")
print(f"  s = √({b_p} * {g}) / 2")

# Result
print(f"Result:")
s = safe_sqrt(b_p * g) / 2

print(f"  s = {s}")

if s > d_e:
    
    print(f"  s > d_e")
    print(f"  {s} > {d_e}")
    print(f"  s ≥ p_fo")
    print(f"  {s} ≥ {p_fo}")
    print(f"  s ≥ p_fi")
    print(f"  {s} ≥ {p_fi}")
    print(f"  → OK")
elif s <= d_e:
    print(f"  s ≤ d_e")
    print(f"  {s} ≤ {d_e}")
    print(f"  s < p_fo")
    print(f"  {s} < {p_fo}")
    print(f"  s < p_fi")
    print(f"  {s} < {p_fi}")
    raise ValueError(f"  → NOT OK")

# -----------------------------------------------------
# A.3) Calculate yield line parameter
# -----------------------------------------------------

print("\nA.3) Calculate yield line parameter")

# Formula / Requirement
print("Formula from Table 5-11 pg.114:")
print("  Y_p = b_p / 2 * Y_p_part1 + Y_p_part2")
print("  Y_p_part1 = h_1*(1/p_fo + 1/(2 * d_e)) + h_2*(1/p_fi + 1/s)")
print("  Y_p_part2 = 2 / g * (h_1*(p_fo + d_e) + h_2*(p_fi + s))")

# Substitution
print("Substitution:")
print(f"  Y_p = {b_p} / 2 * Y_p_part1 + Y_p_part2")
print(f"  Y_p_part1 = {h_1}*(1/{p_fo} 1/(2 * {d_e})) + {h_2}*(1/{p_fi} + 1/{s})")
print(f"  Y_p_part2 = 2 / {g} * ({h_1}*({p_fo} + {d_e}) + {h_2}*({p_fi} + {s}))")

# Result
Y_p_part1 = h_1*(1/p_fo + 1/(2 * d_e)) + h_2*(1/p_fi + 1/s)
Y_p_part2 = 2 / g * (h_1*(p_fo + d_e) + h_2*(p_fi + s))
Y_p = b_p / 2 * Y_p_part1 + Y_p_part2

print(f"Result:")
print(f"  Y_p = {b_p} / 2 * {Y_p_part1} + {Y_p_part2}")
print(f"  Y_p = {Y_p}")


# -----------------------------------------------------
# A.4) Determine the required end-plate thickness
# -----------------------------------------------------

print("\nA.4) Determine the required end-plate thickness")

# Load factor to limit connection rotation at ultimate moment to 10% of simple span rotation
# 0.80 for flush end-plate configuration
# 1.00 for extended end-plate configuration
gamma_r = 1.00 

# Resistance factor for flexure = 0.90
theta_b = 0.90 

# Formula / Requirement
print("Requirement from Table 5-5 pg.56:")
print("  t_p_req = √(M_u_eq / (gamma_r * theta_b * F_y_plate * Y_p))")
print("  t_p ≥ t_p_req")

# Substitution
print("Substitution:")
print(f"  t_p_req = √({M_u_eq} / ({gamma_r} * {theta_b} * {F_y_plate} * {Y_p}))")
print(f"  {t_p} ≥ t_p_req")

# Result
t_p_req = safe_sqrt(M_u_eq / (gamma_r * theta_b * F_y_plate * Y_p))

if t_p >= t_p_req:
    print(f"Result:")
    print(f"  t_p ≥ t_p_req")
    print(f"  {t_p} ≥ {t_p_req}  → OK")

elif t_p < t_p_req:
    print(f"Result:")
    print(f"  t_p < t_p_req")
    # raise ValueError(f"  {t_p} < {t_p_req}  → NOT OK")

# -----------------------------------------------------
# A.5) Determine if the specified bolt are sufficient 
# -----------------------------------------------------

print("\nA.5) Determine if the specified bolt are sufficient")

# Formula
print("Bolt's nominal area:")
print("  A_b = 1/4 * pi * d_bolt**2")
print("Bolt's tensile strength:")
print("  P_t = F_nt_bolt * A_b")

# Substitution
print("Substitution:")
print(f"  A_b = 1/4 * pi * {d_bolt}**2")
print(f"  P_t = {F_nt_bolt} * A_b")

# Result
A_b = 1/4*math.pi*d_bolt**2
P_t = F_nt_bolt * A_b

print(f"Result:")
print(f"  A_b = {A_b}")
print(f"  P_t = {P_t}")

# -----------------------------------------------------
# A.6) Calculate the bolt distance from  bolt to edge of effective tee stub 
# ----------------------------------------------------- 

print("\nA.6) Calculate the bolt distance from  bolt to edge of effective tee stub")

# Formula / Requirement
print("The bolt distance from  bolt to edge of effective tee stub :")
print("  a = 3.62 * (t_p / d_b)**3 - 0.085")

# Substitution
print("Substitution:")
print(f"  a = 3.62 * ({t_p} / {d_bolt})**3 - 0.085")

# Result
a_part1 = (3.62 * (t_p / d_bolt)**3) * US.inch
a_part2 = 0.085 * US.inch 
a = a_part1 - a_part2

print(f"Result:")
print(f"  a_part1 = {a_part1}")
print(f"  a_part2 = {a_part2}")
print(f"  a = {a}")

# -----------------------------------------------------
# A.7) Calculate the geometry of the effective tee stub
# ----------------------------------------------------- 

print("\nA.7) Calculate the geometry of the effective tee stub")

# -----------------------------------------------------
# A.7.a) Bolt position I - outside bolt
# ----------------------------------------------------- 

print("\nA.7.a) Bolt position I - outside bolt")

# Formula / Requirement
print("Width of the effective tee stub, w1 :")
print("  w1 = b_p / 2")

print("Net effective width, w1' :")
print("  w1' = w1 - d_hole")

print("Distance from effective tee stem to the bolt, b1 :")
print("  a1 = min(a, d_e)")
print("  b1 = p_fo")

# Substitution
print("Substitution:")
print(f"  w1 = {b_p} / 2")
print(f"  w1' = w1 - ({d_hole})")
print(f"  a1 = min({a}, {d_e})")
print(f"  b1 = {p_fo}")

# Result
w1 = b_p / 2
w1_prime = w1 - (d_hole)
a1 = min(a, d_e)
b1 = p_fo

print(f"Result:")
print(f"  w1 = {w1}")
print(f"  w1' = {w1_prime}")
print(f"  a1 = {a1}")
print(f"  b1 = {b1}")

# Formula / Requirement
print("Calculate force related to prying")
print("The force, F1' :")
print(f"  F_1_prime_part1 = (t_p**2 * F_y_plate) / 4 * (0.85*w1 + 0.8*w1_prime)")
print(f"  F_1_prime_part2 = (pi * d_bolt**3 * F_nt_bolt) / 32")
print(f"  F_1_prime = 1/b1 * (F_1_prime_part1 + F_1_prime_part2)")

# Substitution
print("Substitution:")
print(f"  F_1_prime_part1 = ({t_p}**2 * {F_y_plate}) / 4 * (0.85*{w1} + 0.8*{w1_prime})")
print(f"  F_1_prime_part2 = (pi * {d_bolt}**3 * {F_nt_bolt}) / 32")

# Result
F_1_prime_part1 = (t_p**2 * F_y_plate) / 4 * (0.85*w1 + 0.8*w1_prime)
F_1_prime_part2 = (math.pi * d_bolt**3 * F_nt_bolt) / 32 
F_1_prime = 1/b1 * (F_1_prime_part1 + F_1_prime_part2)

print("Result:")
print(f"  F_1_prime_part1 = {F_1_prime_part1}")
print(f"  F_1_prime_part2 = {F_1_prime_part2}")
print(f"  F_1_prime = {F_1_prime}")

# Formula / Requirement
print("The prying force, Q_max,1' :")
print("  Q_max1_part1 = (w1_prime*t_p**2) / (4*a1)")
print("  Q_max1_part2 =  √((F_y_plate**2) - (3*(F_1_prime/(w1_prime*t_p))**2))")
print("  Q_max1 = Q_max1_part1 * Q_max1_part2")

# Substitution
print("Substitution:")
print(f"  Q_max1_part1 = ({w1_prime}*{t_p}**2) / (4*{a1})")
print(f"  Q_max1_part2 =  √(({F_y_plate}**2) - (3*({F_1_prime}/({w1_prime}*{t_p}))**2))")

# Result
Q_max1_part1 = (w1_prime*t_p**2) / (4*a1)
Q_max1_part2 = safe_sqrt(F_y_plate**2 - 3*(F_1_prime/(w1_prime*t_p))**2)
Q_max1 = Q_max1_part1 * Q_max1_part2

print("Result:")
print(f"  Q_max1_part1 = {Q_max1_part1}")
print(f"  Q_max1_part2 =  {Q_max1_part2}")
print(f"  Q_max1 = {Q_max1}")

# Formula / Requirement
print("Bolt rension contributing to flexural strength, P_q1:")
print(f"  P_q1 = max(P_t - Q_max1, T_b)")

# Substitution
print("Substitution:")
print(f"  P_q1 = max({P_t} - {Q_max1}, {T_b})")

# Result
P_q1 = max(P_t - Q_max1, T_b)

print("Result:")
print(f"  P_q1 = {P_q1}")

# Reduqction in bolt contribution
alpha_1 = 1.0

# -----------------------------------------------------
# A.7.b) Bolt position II - interior bolt
# ----------------------------------------------------- 

print("\nA.7.b) Bolt position II - interior bolt")

# Formula / Requirement
print("Distance from effective tee stem to the bolt, b1 :")
print("  a2 = a")
print("  b2 = p_fi")

# Substitution
print("Substitution:")
print(f"  a2 = {a}")
print(f"  b2 = {p_fi}")

# Result
a2 = a
b2 = p_fi

print(f"Result:")
print(f"  a2 = {a2}")
print(f"  b2 = {b2}")

# Formula / Requirement
print("Calculate force related to prying")
print("The force, F1' :")
print(f"  F_2_prime_part1 = (t_p**2 * F_y_plate) / 4 * (0.85*w1 + 0.8*w1_prime)")
print(f"  F_2_prime_part2 = (pi * d_bolt**3 * F_nt_bolt) / 32")
print(f"  F_2_prime = 1/b2 * (F_2_prime_part1 + F_2_prime_part2)")

# Substitution
print("Substitution:")
print(f"  F_2_prime_part1 = ({t_p}**2 * {F_y_plate}) / 4 * (0.85*{w1} + 0.8*{w1_prime})")
print(f"  F_2_prime_part2 = (pi * {d_bolt}**3 * {F_nt_bolt}) / 32")

# Result
F_2_prime_part1 = (t_p**2 * F_y_plate) / 4 * (0.85*w1 + 0.8*w1_prime)
F_2_prime_part2 = (math.pi * d_bolt**3 * F_nt_bolt) / 32 
F_2_prime = 1/b2 * (F_2_prime_part1 + F_2_prime_part2)

print("Result:")
print(f"  F_2_prime_part1 = {F_2_prime_part1}")
print(f"  F_2_prime_part2 = {F_2_prime_part2}")
print(f"  F_2_prime = {F_2_prime}")

# Formula / Requirement
print("The prying force, Q_max,1' :")
print("  Q_max2_part1 = (w1_prime*t_p**2) / (4*a2)")
print("  Q_max2_part2 =  √((F_y_plate**2) - (3*(F_2_prime/(w1_prime*t_p))**2))")
print("  Q_max2 = Q_max2_part1 * Q_max2_part2")

# Substitution
print("Substitution:")
print(f"  Q_max2_part1 = ({w1_prime}*{t_p}**2) / (4*{a2})")
print(f"  Q_max2_part2 =  √(({F_y_plate}**2) - (3*({F_2_prime}/({w1_prime}*{t_p}))**2))")

# Result
Q_max2_part1 = (w1_prime*t_p**2) / (4*a2)
Q_max2_part2 = safe_sqrt(F_y_plate**2 - 3*(F_2_prime/(w1_prime*t_p))**2)
Q_max2 = Q_max2_part1 * Q_max2_part2

print("Result:")
print(f"  Q_max2_part1 = {Q_max2_part1}")
print(f"  Q_max2_part2 =  {Q_max2_part2}")
print(f"  Q_max2 = {Q_max2}")

# Formula / Requirement
print("Bolt rension contributing to flexural strength, P_q2:")
print(f"  P_q2 = max(P_t - Q_max2, T_b)")

# Substitution
print("Substitution:")
print(f"  P_q2 = max({P_t} - {Q_max2}, {T_b})")

# Result
P_q2 = max(P_t - Q_max2, T_b)

print("Result:")
print(f"  P_q2 = {P_q2}")

# Reduqction in bolt contribution
alpha_2 = 1.0
# -----------------------------------------------------
# A.8) Calculate the flexural strength for bolt rupture with pyring action
# ----------------------------------------------------- 

print("\nA.8) Calculate the flexural strength for bolt rupture with pyring action")

# Resistance factor for bolt rupture
theta_r = 0.75

# Formula / Requirement
print("The design flexural strength, theta_r * M_q:")
print("  M_q = alpha_1 * P_q1 * 2 * h_1 + alpha_2 * P_q2 * 2 * h_2")
print("  theta_M_q = theta_r * M_q")
print("Compared to the required flexural stringth, Rn_bt:")
print("  theta_M_q ≥ M_u_eq")

# Substitution
print("Substitution:")
print(f"  M_q = {alpha_1} * {P_q1} * 2 * {h_1} + {alpha_2} * {P_q2} * 2 * {h_2}")

# Result
print("Result:")
M_q = alpha_1 * P_q1 * 2 * h_1 + alpha_2 * P_q2 * 2 * h_2
theta_M_q = theta_r * M_q

print(f"  M_q = {M_q}")
print(f"  theta_M_q = {theta_M_q}")

if theta_M_q  >= M_u_eq:
    print(f"Result: {theta_M_q} ≥ {M_u_eq}  → OK")
else:
    raise ValueError(f"Result: {theta_M_q} < {M_u_eq}  → NOT OK")

# -----------------------------------------------------
# A.9) Check shear shear transfer at the top bolt holes
# ----------------------------------------------------- 

print("\nA.9) Check shear shear transfer at the top bolt holes")

# Resistance factor for shear
theta_v = 0.75

# Formula / Requirement
print("Nominal shear strength of bolt, Rn_bt:")
print("  Rn_bt = F_nv_bolt * A_b")
print("Nominal bearing strength at a bolt hole, Rn_bt:")
print("  Rn_brg = 2.4*d_bolt*t_cf*F_u_beam_column")
print("Nominal shear transfer strength at the four bolt hole is, V_n:")
print("  V_n = theta_v * 4 * min(Rn_bt, Rn_brg)")
print("  V_n ≥ V_u")

# Substitution
print("Substitution:")
print(f"  Rn_bt = {F_nv_bolt} * {A_b}")
print(f"  Rn_brg = 2.4*{d_bolt}*{t_cf}*{F_u_beam_column}")

# Result
Rn_bt = F_nv_bolt * A_b
Rn_brg = 2.4*d_bolt*t_cf*F_u_beam_column
V_n = theta_v*4*min(Rn_bt, Rn_brg)

print("Result:")
print(f"  Rn_bt = {Rn_bt}")
print(f"  Rn_brg = {Rn_brg}")
print(f"  V_n =  {V_n}")

if V_n >= V_u:
    print(f"Result: {V_n} ≥ {V_u}  → OK")
else:
    raise ValueError(f"Result: {V_n} < {V_u}  → NOT OK")

print(f"\n=====================================")
print("CALCULATION END")
print(f"=====================================\n")