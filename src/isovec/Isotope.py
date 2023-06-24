# Python class for isotope

class Isotope:

    def __init__(self, name: str, atomicNumber: int, massNumber: int, atomicWeight: float) -> 'Isotope':
        
        self._name: str = name                    # name
        self._atomicNumber: int = atomicNumber    # atomic number (protons)
        self._massNumber: int = massNumber        # (atomic) mass number (protons + neutrons)
        self._atomicWeight: float = atomicWeight  # atomic weight

    # ########
    # Getter
    # ########

    @property
    def name(self):
        """ Name of the isotope """
        return self._name

    @property
    def atomicNumber(self):
        """ Atomic number (number of protons) """
        return self._atomicNumber

    @property
    def massNumber(self):
        """ (Atomic) Mass number (number of protons + neutrons) """
        return self._massNumber

    @property
    def atomicWeight(self):
        """ Atomic weight of the isotope """
        return self._atomicWeight


    # ########
    # Functions
    # ########

    def NeutronNumber(self) -> int:
        """ Neutron number (number of neutrons) """
        return self._massNumber - self._atomicNumber


    # ########
    # Print
    # ########

    def String(self) -> str:
        """ Return Isotope as string """
        return self._name


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.String()

    def __repr__(self):
        return self.String()

    def __hash__(self):
        return hash((self._atomicNumber, self._massNumber))

    def __eq__(self, other: 'Isotope'):
        try:
            if (self._atomicNumber == other._atomicNumber) and (self._massNumber == other._massNumber):
                return True
            else:
                return False
        except:
            raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")

    def __ne__(self, other: 'Isotope'):
        return not self.__eq__(other)

    def __lt__(self, other: 'Isotope'):
        try:
            if self._atomicNumber < other._atomicNumber:
                return True
            elif self._atomicNumber == other._atomicNumber:
                if self._massNumber < other._massNumber:
                    return True
                else:
                    return False
            else:
                return False
        except:
            raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")

    def __le__(self, other: 'Isotope'):
        return self.__lt__(other) or self.__eq__(other)


    def __gt__(self, other: 'Isotope'):
        try:
            if self._atomicNumber > other._atomicNumber:
                return True
            elif self._atomicNumber == other._atomicNumber:
                if self._massNumber > other._massNumber:
                    return True
                else:
                    return False
            else:
                return False
        except:
            raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")

    def __ge__(self, other: 'Isotope'):
        return self.__gt__(other) or self.__eq__(other)

