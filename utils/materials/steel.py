from dataclasses import dataclass
from .base import Material
from ..units.structural_units import SI

@dataclass(frozen=True)
class Steel(Material):
    Fy: float        # yield strength
    Fu: float        # ultimate strength
    E: float         # Young's modulus
    nu: float        # Poisson's ratio
    density: float

ASTM_A992 = Steel(
    name="ASTM A992/A992M",
    source="ASTM A992/A992M",
    Fy=345 * SI.MPa,
    Fu=450 * SI.MPa,
    E=200_000 * SI.MPa,
    nu=0.29,
    density=7850 * SI.kg / SI.m**3,
)
