import forallpeople as fp
import math
fp.environment("structural")  # gives SI + US structural units

class SI:
    m   = fp.m
    mm  = fp.mm
    m2  = fp.m**2
    mm2 = fp.mm**2
    m3  = fp.m**3

    N   = fp.N
    kN  = fp.kN
    MN  = fp.MN

    Pa  = fp.Pa
    kPa = fp.kPa
    MPa = fp.MPa
    GPa = fp.GPa

    Nm  = fp.N * fp.m
    kNm = fp.kN * fp.m

    kg = fp.kg
    kg_m3 = fp.kg / fp.m**3
    kN_m3 = fp.kN / fp.m**3

class US:
    inch = fp.inch
    ft   = fp.ft

    in2 = fp.inch**2
    ft2 = fp.ft**2
    in3 = fp.inch**3
    ft3 = fp.ft**3

    # lbf = fp.lbf
    kip = fp.kip

    psi = fp.psi
    ksi = fp.ksi

    # lbft  = fp.lbf * fp.ft
    kipft = fp.kip * fp.ft
    kipin = fp.kip * fp.inch

    # pcf = fp.lbf / fp.ft**3

class Materials:
    E_STEEL_SI = 200 * fp.GPa
    E_STEEL_US = 29000 * fp.ksi

    GAMMA_CONC_SI = 24 * fp.kN / fp.m**3
    GAMMA_CONC_US = 150 * fp.pcf

def to_unit(value, unit):
    return 0 * unit + value

def safe_sqrt(value):
    """
    Calculate square root while preserving forallpeople units using string parsing.
    Automatically tries US units first, then SI units.
    
    Args:
        value: A number or forallpeople Physical quantity
        
    Returns:
        Square root with properly handled units
        
    Examples:
        >>> # SI units
        >>> area = 25 * SI.m2
        >>> length = safe_sqrt(area)
        >>> print(length)  # 5.0 m
        
        >>> # US units
        >>> area = 25 * US.ft2
        >>> length = safe_sqrt(area)
        >>> print(length)  # 5.0 ft
    """
    # Handle plain numbers
    if isinstance(value, (int, float)):
        return math.sqrt(value)
    
    # Convert to string and parse
    value_str = str(value).strip()
    
    # Split into numeric and unit parts
    parts = value_str.split(maxsplit=1)
    
    if len(parts) == 1:
        # No unit found, treat as plain number
        return math.sqrt(float(parts[0]))
    
    numeric_str, unit_str = parts
    
    # Extract numeric value
    try:
        numeric_value = float(numeric_str)
    except ValueError:
        raise ValueError(f"Could not parse numeric value from '{numeric_str}'")
    
    # Calculate square root of numeric value
    sqrt_value = math.sqrt(numeric_value)
    
    # Handle the unit for square root
    # Remove ² from unit (e.g., "ft²" -> "ft", "m²" -> "m")
    if "²" in unit_str:
        unit_sqrt_str = unit_str.replace("²", "")
    elif "**2" in unit_str:
        unit_sqrt_str = unit_str.replace("**2", "")
    elif unit_str.endswith("2"):
        # Handle cases like "ft2", "in2", "m2", "mm2"
        unit_sqrt_str = unit_str[:-1]
    else:
        # If no squared symbol found, assume we're taking sqrt of a non-squared unit
        print(f"Warning: Unit '{unit_str}' doesn't appear to be squared. Result may not be standard.")
        unit_sqrt_str = unit_str
    
    # Try to get the unit - first try US, then SI
    unit_sqrt = None
    try:
        unit_sqrt = getattr(US, unit_sqrt_str)
    except AttributeError:
        try:
            unit_sqrt = getattr(SI, unit_sqrt_str)
        except AttributeError:
            # Couldn't find the unit in any system
            available_us = [attr for attr in dir(US) if not attr.startswith('_')]
            available_si = [attr for attr in dir(SI) if not attr.startswith('_')]
            raise AttributeError(
                f"Unit '{unit_sqrt_str}' not found in US or SI class.\n"
                f"Available US units: {available_us}\n"
                f"Available SI units: {available_si}"
            )
    
    # Combine numeric sqrt with unit
    result = sqrt_value * unit_sqrt
    
    return result
