from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable, Dict

from utils.sections.loaders import load_steel_csv

# -------------------------------------------------
# Section identity
# -------------------------------------------------

from enum import Enum

class SectionKey(Enum):
    WF_150x75x5x7 = ("WF.150x75x5x7")
    WF_200x100x5_5x8 = ("WF.200x100x5.5x8")
    WF_250x125x6x9 = ("WF.250x125x6x9")
    H_100x100x8x6 = ("H.100x100x8x6")

    def __init__(self, key: str):
        self._key = key

    @property
    def key(self) -> str:
        return self._key
    
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable

@dataclass(frozen=True)
class SourceInfo:
    path: Path
    standard: str
    loader: Callable
    
class SourceKey(Enum):
    WF_GRP = SourceInfo(
        path=Path(r"D:\COMPUTATIONAL\Python\HANDCALCS\utils\sections\docs\WF GRP.csv"),
        standard="JIS 3192",
        loader=load_steel_csv,
    )
    H_GRP = SourceInfo(
        path=Path(r"D:\COMPUTATIONAL\Python\HANDCALCS\utils\sections\docs\H GRP.csv"),
        standard="JIS 3192",
        loader=load_steel_csv,
    )