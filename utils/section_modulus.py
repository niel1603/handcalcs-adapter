from math import pi

import math

def plastic_section_modulus_pipe(D, t):
    """
    Calculate the plastic section modulus (Z) of a steel pipe.
    
    Parameters:
        D (float): Outer diameter of the pipe [mm or in]
        t (float): Wall thickness of the pipe [mm or in]
    
    Returns:
        float: Plastic section modulus (Z) [mm³ or in³]
    """
    Z = (D**3 - (D - 2 * t)**3) / 6
    return Z