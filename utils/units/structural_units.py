from pint import UnitRegistry
from dataclasses import dataclass

ureg = UnitRegistry()
Q_ = ureg.Quantity

@dataclass(frozen=True)
class SI:
    # Length
    m  = ureg.meter
    mm = ureg.millimeter

    # Area / Volume
    m2  = ureg.meter**2
    mm2 = ureg.millimeter**2
    m3  = ureg.meter**3

    # Force
    N  = ureg.newton
    kN = ureg.kilonewton
    MN = ureg.meganewton

    # Stress
    Pa  = ureg.pascal
    kPa = ureg.kilopascal
    MPa = ureg.megapascal
    GPa = ureg.gigapascal

    # Moment
    Nm  = N * m
    kNm = kN * m

    # Density / unit weight
    kg = ureg.kilogram
    kg_m3 = kg / m3
    kN_m3 = kN / m3

    # Acceleration
    g = ureg.gravity

@dataclass(frozen=True)
class US:
    # Length
    inch = ureg.inch
    ft   = ureg.foot

    # Area / Volume
    in2 = inch**2
    ft2 = ft**2
    in3 = inch**3
    ft3 = ft**3

    # Force
    lbf  = ureg.pound_force
    kip  = ureg.kip

    # Stress
    psi = ureg.psi
    ksi = ureg.ksi

    # Moment
    lbft  = lbf * ft
    kipft = kip * ft
    kipin = kip * inch

    # Density / unit weight
    pcf = lbf / ft3

class Materials:
    # Elastic modulus
    E_STEEL_SI = 200 * SI.GPa
    E_STEEL_US = 29000 * US.ksi

    # Unit weight
    GAMMA_CONC_SI = 24 * SI.kN_m3
    GAMMA_CONC_US = 150 * US.pcf

def to_SI(q):
    """
    Convert quantity to SI base units.
    Use ONLY at I/O boundaries.
    """
    return q.to_base_units()


def to_US(q):
    """
    Convert quantity to US customary base units.
    """
    return q.to(ureg.foot, ureg.kip, ureg.second)
