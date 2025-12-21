# sections/models.py
from dataclasses import dataclass

@dataclass(frozen=True)
class SteelSectionProps:
    A: float
    Ix: float
    Iy: float
    Zx: float   # governing elastic section modulus
    Zy: float
    rx: float
    ry: float

@dataclass(frozen=True)
class SteelSection:
    name: str
    props: SteelSectionProps
    standard: str       # AISC, JIS, EN, SNI
    source: str         # e.g., "AISC 15th"
