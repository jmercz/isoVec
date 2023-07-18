# Python class for isotope

from __future__ import annotations

from .constants import ATOM_NUMB_TO_SYMBOL, M_u


class Isotope:

    def __init__(self, Z: int, A: int, A_r: float, name: str = "") -> None:
        
        self._Z: int = Z        # atomic number (protons)
        self._A: int = A        # mass number (protons + neutrons)
        self._A_r: float = A_r  # relative atomic mass (atomic weight) [-]
        self._name: str         # name

        if name == "":
            self._name = ATOM_NUMB_TO_SYMBOL[self._Z] + "-" + str(self._A)
        else:
            self._name = name


    # ########
    # Getter
    # ########

    @property
    def name(self):
        """Name of the isotope."""
        return self._name

    @property
    def Z(self):
        """Atomic number (number of protons)."""
        return self._Z

    @property
    def A(self):
        """Mass number (number of protons + neutrons)."""
        return self._A

    @property
    def A_r(self):
        """Relative atomic mass (atomic weight) [-] of the isotope."""
        return self._A_r

    @property
    def M(self):
        """Molar mass [g mol^-1] of the isotope."""
        return self.calc_M()

    @property
    def N(self):
        """Neutron number (number of neutrons)."""
        return self.calc_N()


    # ########
    # Functions
    # ########

    def calc_M(self) -> float:
        """Calculates molar mass [g mol^-1] of the isotope."""
        return self._A_r * M_u * 1e+03
    
    def calc_N(self) -> int:
        """Calculates neutron number (number of neutrons)."""
        return self._A - self._Z


    # ########
    # Print
    # ########


    # ########
    # Operators
    # ########

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self.__class__.__name__} \"{self._name}\""

    def __hash__(self):
        return hash((self._Z, self._A))

    def __eq__(self, other):
        try:
            if (self._Z == other._Z) and (self._A == other._A):
                return True
            else:
                return False
        except:
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        try:
            if self._Z < other._Z:
                return True
            elif self._Z == other._Z:
                if self._A < other._A:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


    def __gt__(self, other):
        try:
            if self._Z > other._Z:
                return True
            elif self._Z == other._Z:
                if self._A > other._A:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

