from dataclasses import dataclass

@dataclass(frozen=True)
class Material:
    """
    Base material class.
    No design logic. No solvers. No assumptions.
    """
    name: str
    source: str
