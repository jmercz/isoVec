"""Class for Isotope

Isotope class serves as constituent for Element class.
"""

from __future__ import annotations

from .constants import ATOM_NUMB_TO_SYMBOL, M_u


class Isotope:
    """Isotope are nuclides of the same element.

    Each isotope is characterised by their atomic number (Z), mass number (M)
    and isomeric state (I). Furthermore, each isotope has a chracteristic 
    relative atomic mass (A_R). They are used to compose elements.
    """

    def __init__(self, Z: int, A: int, A_r: float, I: int = 0, name: str = "") -> None:
        """Constructor of isotope.
        
        Args:
            Z:
                Atomic number (number of protons).
            A:
                Mass number (number of protons + neutrons).
            A_r:
                Relative atomic mass ("atomic weight") [-].
            I:
                Isomeric state.
            name:
                Override name of isotope.
        """
        
        self._Z: int = Z        # atomic number (protons)
        self._A: int = A        # mass number (protons + neutrons)
        self._A_r: float = A_r  # relative atomic mass (atomic weight) [-]
        self._I: int = I        # isomeric state (0 = ground state, 1 = metastable, ...)
        self._name: str         # name

        if name == "":
            self._name = self.short_name()
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
    def I(self):
        """Isomeric state."""
        return self._I

    @property
    def M(self):
        """Molar mass [g mol^-1] of the isotope."""
        return self.calc_M()

    @property
    def N(self):
        """Neutron number (number of neutrons)."""
        return self.calc_N()
    
    @property
    def ZA(self):
        """ZA notation of the isotope."""
        return self.ZA_notation()
    
    @property
    def ZAI(self):
        """ZAI notation of the isotope."""
        return self.ZAI_notation()


    # ########
    # Functions
    # ########

    def calc_M(self) -> float:
        """Calculates molar mass [g mol^-1] of the isotope."""
        return self._A_r * M_u * 1e+03
    
    def calc_N(self) -> int:
        """Calculates neutron number (number of neutrons)."""
        return self._A - self._Z
    
    def get_symbol(self) -> str:
        """Returns symbol of element that isotope represents."""
        return ATOM_NUMB_TO_SYMBOL[self._Z]
    
    def ZA_notation(self) -> int:
        """Returns the ZA notation of the isotope.
        
        ZA = Z*1000 + A
        """
        return self._Z*1000 + self._A
    
    def ZAI_notation(self) -> int:
        """Returns the ZAI notation of the isotope.

        ZAI = Z*10000 + A*10 + I
        """
        return self._Z*10000 + self._A*10 + self._I

    def short_name(self, verbose: bool = False) -> str:
        """Returns short name of isotope as string.
        
        Similar to pronunciation of AZE notation.

        Args:
            verbose:
                Flag to explicitly show isomeric state of isotope.
        """
        
        name = f"{self.get_symbol()}-{self._A}"
        
        if verbose:
            if self._I == 0:
                name += "g"
            else:
                name += f"m{self._I}"
        else:
            if self._I == 1:
                name += "m"
            if self._I > 1:
                name += f"m{self._I}"
            
        return name
    

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
        return hash((self._Z, self._A, self._I))

    def __eq__(self, other):
        try:
            if (self._Z == other._Z) and (self._A == other._A) and (self._I == other._I):
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
                elif self._A == other._A:
                    if self._I < other._I:
                        return True
                    else:
                        return False
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
                elif self._A == other._A:
                    if self._I > other._I:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

