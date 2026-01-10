from __future__ import annotations

from importlib import resources
import csv
from pathlib import Path

from dataclasses import dataclass
from enum import Enum
from typing import Union

from handcalcs_adapter.units import *


# =========================================================
# ENUM (OPTIONAL, USER-FACING)
# =========================================================

from enum import Enum


class Section(Enum):
    # C 100 x 50 x 20
    C100x50x20x2   = "C100x50x20x2"
    C100x50x20x2_3 = "C100x50x20x2.3"
    C100x50x20x2_5 = "C100x50x20x2.5"
    C100x50x20x2_8 = "C100x50x20x2.8"
    C100x50x20x3   = "C100x50x20x3"
    C100x50x20x3_2 = "C100x50x20x3.2"

    # C 125 x 50 x 20
    C125x50x20x2   = "C125x50x20x2"
    C125x50x20x2_3 = "C125x50x20x2.3"
    C125x50x20x2_5 = "C125x50x20x2.5"
    C125x50x20x2_8 = "C125x50x20x2.8"
    C125x50x20x3   = "C125x50x20x3"
    C125x50x20x3_2 = "C125x50x20x3.2"

    # C 150 x 50 x 20
    C150x50x20x2   = "C150x50x20x2"
    C150x50x20x2_3 = "C150x50x20x2.3"
    C150x50x20x2_5 = "C150x50x20x2.5"
    C150x50x20x2_8 = "C150x50x20x2.8"
    C150x50x20x3   = "C150x50x20x3"
    C150x50x20x3_2 = "C150x50x20x3.2"

    # C 150 x 65 x 20
    C150x65x20x2   = "C150x65x20x2"
    C150x65x20x2_3 = "C150x65x20x2.3"
    C150x65x20x2_5 = "C150x65x20x2.5"
    C150x65x20x2_8 = "C150x65x20x2.8"
    C150x65x20x3   = "C150x65x20x3"
    C150x65x20x3_2 = "C150x65x20x3.2"

    # C 200 x 75 x 20
    C200x75x20x2   = "C200x75x20x2"
    C200x75x20x2_3 = "C200x75x20x2.3"
    C200x75x20x2_5 = "C200x75x20x2.5"
    C200x75x20x2_8 = "C200x75x20x2.8"
    C200x75x20x3   = "C200x75x20x3"
    C200x75x20x3_2 = "C200x75x20x3.2"


# =========================================================
# DATA MODELS
# =========================================================

@dataclass(frozen=True)
class SteelSection:
    name: str
    standard: str
    source: str


@dataclass(frozen=True)
class CnpSection(SteelSection):
    t: float
    A: float
    w: float
    Ix: float
    Iy: float
    Zx: float
    Zy: float
    rx: float
    ry: float
    Cy: float
    Xo: float
    J: float
    Cw: float


# =========================================================
# LOADERS
# =========================================================

def _load_cnp(*, standard: str) -> dict[str, CnpSection]:
    table = {}

    # Access CSV as a package resource
    with resources.files("handcalcs_adapter.data").joinpath(
        "CNP GRP.csv"
    ).open("r", encoding="utf-8-sig", newline="") as f:

        reader = csv.DictReader(f)

        for r in reader:
            name = r["name"].strip()

            table[name] = CnpSection(
                name=name,
                standard=standard,
                source="CNP GRP.csv",
                t=float(r["t_mm"]) * mm,
                A=float(r["A_cm2"]) * cm**2,
                w=float(r["w_kg/m"]) * kg / m,
                Ix=float(r["Ix_cm4"]) * cm**4,
                Iy=float(r["Iy_cm4"]) * cm**4,
                Zx=float(r["Zx_cm3"]) * cm**3,
                Zy=float(r["Zy_cm3"]) * cm**3,
                rx=float(r["rx_cm"]) * cm,
                ry=float(r["ry_cm"]) * cm,
                Cy=float(r["Cy_cm"]) * cm,
                Xo=float(r["Xo_cm"]) * cm,
                J=float(r["J_cm4"]) * cm**4,
                Cw=float(r["Cw_cm6"]) * cm**6,
            )

    return table


# =========================================================
# SOURCE CATALOG
# =========================================================

_SOURCES = [
    {
        "name": "CNP_GRP",
        "standard": "JIS 3192",
        "loader": _load_cnp,
    }
]


_SECTION_CACHE: dict[str, dict[str, SteelSection]] = {}

# =========================================================
# CACHE + PUBLIC API
# =========================================================

_cache: dict[str, dict[str, SteelSection]] = {}


def _normalize_name(name: Union[str, Section]) -> str:
    if isinstance(name, Section):
        return name.value
    return name


def _load_source(src: dict) -> dict[str, SteelSection]:
    """
    Load section table from a source (cached).
    """
    key = src["name"]

    if key not in _SECTION_CACHE:
        _SECTION_CACHE[key] = src["loader"](
            standard=src["standard"]
        )

    return _SECTION_CACHE[key]


def section(name: Union[str, Section]) -> SteelSection:
    """
    Get steel section by name or Section enum.

    Examples:
        section("C150x50x20x3.2")
        section(Section.C150x50x20x3_2)
    """
    key = _normalize_name(name)

    for src in _SOURCES:
        table = _load_source(src)
        if key in table:
            return table[key]

    raise KeyError(f"Section not found: {key}")

__all__ = [
    "section",
    "Section",
    "SteelSection",
    "CnpSection",
]

