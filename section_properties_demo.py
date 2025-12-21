from utils.sections.enum import SectionKey, SourceKey
from utils.sections.registry import SectionRegistry
from utils.sections.loaders import load_steel_csv
from utils.materials.steel import ASTM_A992
from utils.units.structural_units import SI, US

# registry = SectionRegistry()
# registry.register_table(
#     "AISC",
#     load_steel_csv(
#         r"D:\COMPUTATIONAL\Python\HANDCALCS\utils\sections\docs\database WF.csv", 
#         standard="AISC"
#         )
# )

# sec = registry.get("WF.250x125x6x9", "AISC")
# steel = ASTM_A992
# phi_b = 0.90

# Mn = steel.Fy * sec.props.Zx
# phi_Mn = phi_b * Mn

# print(phi_Mn.to(SI.kN*SI.m))

registry = SectionRegistry()

sec = registry.get(SectionKey.H_100x100x8x6, SourceKey.H_GRP)

print(sec.props.Zx)

# print(sec)



