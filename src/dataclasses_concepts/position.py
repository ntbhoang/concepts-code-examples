from dataclasses import dataclass, field
from math import radians, sin, cos, asin, sqrt

"""
    - Immutable data class:
        One of the defining features of the namedtuple you saw earlier is that it is immutable. 
        That is, the value of its fields may never change.
        For many types of data classes, this is a great idea! To make a data class immutable, 
        set frozen=True when you create it.
    
"""


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


@dataclass
class Capital(Position):
    country: str = field(default="Norway")

