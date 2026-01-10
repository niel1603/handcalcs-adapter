from handcalcs_adapter.section import section, Section
sec = section(Section.C200x75x20x2_8)

## 2. Selec purlin
section_name = (sec.name)
w_self = (sec.w) # self weight
I_x = (sec.Ix) # strong-axis moment of inertia
I_y = (sec.Iy) # weak-axis moment of inertia
Z_x = (sec.Zx) # strong-axis modulus of section
Z_y = (sec.Zy) # weak-axis modulus of section