from math import pi

from pint import UnitRegistry
ureg = UnitRegistry()

## Input

## Hook spesification
'''hook_length = 3.5 * ureg.inch
d_a = 7/8 * ureg.inch
f_prime_c = 4000 * ureg.psi'''

anchorDiameter = 25
hookLength = 5 * anchorDiameter
hookDepth = 35 * anchorDiameter

print(f'hookLength: {hookLength}')
print(f'hookDepth: {hookDepth}')

d_a = (anchorDiameter * ureg.millimeter).to(ureg.inch)
hook_length = (hookLength * ureg.millimeter).to(ureg.inch)
f_prime_c = (30 * ureg.megapascal).to(ureg.psi)

e_h = hook_length - d_a

print(f'd_a: {d_a}')
print(f'e_h: {e_h}')
print(f'e_h / d_a: {e_h / d_a}')

print(f'3 * d_a: {3 * d_a}')
print(f'4.5 * d_a: {4.5 * d_a}')

if 3 * d_a <= e_h <= 4.5 * d_a :
    print('the hook geometry is acceptable')
else: 
    print('\n!!! WARNING !!!')
    print('consider using different anchor size')

N_p = (0.9 * f_prime_c * e_h * d_a).to(ureg.kips)

print(f'N_p: {N_p}')

psi = 1
N_pn = psi * N_p

print(f'N_pn: {N_pn}')

theta = 0.7
thetaN_pn = theta * N_pn

print(f'thetaN_pn: {thetaN_pn}')
print(f'thetaN_pn: {thetaN_pn.to(ureg.kilonewton)}')