from math import pi

from pint import UnitRegistry
ureg = UnitRegistry()

# diameter = (0.75 * ureg.inch)
# F_u = 58 * ureg.ksi
# f_prime_c = 3 * ureg.ksi

diameter = (30 * ureg.mm).to(ureg.inch)
F_u = (825 * ureg.megapascal).to(ureg.ksi)
f_prime_c = (30 * ureg.megapascal).to(ureg.ksi)

phi_t = 0.75
A_g = 1/4 * pi * diameter ** 2
T_u = 0.75 * phi_t * F_u * A_g
L_h = (T_u / 2) / (0.7 * f_prime_c * diameter)

print(T_u)
print(T_u.to(ureg.kilonewton))
print(L_h)
print(L_h.to(ureg.millimeter))