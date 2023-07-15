# Python class for isotope

class Isotope:

    def __init__(self, name: str, atomic_num: int, mass_num: int, atomic_wt: float) -> None:
        
        self._name: str = name          # name
        self._atomic_num: int = atomic_num  # atomic number (protons)
        self._mass_num: int = mass_num  # (atomic) mass number (protons + neutrons)
        self._atomic_wt: float = atomic_wt  # atomic weight

    # ########
    # Getter
    # ########

    @property
    def name(self):
        """Name of the isotope."""
        return self._name

    @property
    def atomic_num(self):
        """Atomic number (number of protons)."""
        return self._atomic_num

    @property
    def mass_num(self):
        """(Atomic) Mass number (number of protons + neutrons)."""
        return self._mass_num

    @property
    def atomic_wt(self):
        """Atomic weight of the isotope."""
        return self._atomic_wt


    # ########
    # Functions
    # ########

    def neutron_number(self) -> int:
        """Calculates neutron number (number of neutrons)."""
        return self._mass_num - self._atomic_num

    def hash(self) -> int:
        """Hashes isotope via atomic and mass number."""
        return hash((self._atomic_num, self._mass_num))


    # ########
    # Print
    # ########

    def string(self) -> str:
        """Returns isotope name."""
        return self._name


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.string()

    def __repr__(self):
        return self.string()

    def __hash__(self):
        return self.hash()

    def __eq__(self, other):
        try:
            if (self._atomic_num == other._atomic_num) and (self._mass_num == other._mass_num):
                return True
            else:
                return False
        except:
            #raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        try:
            if self._atomic_num < other._atomic_num:
                return True
            elif self._atomic_num == other._atomic_num:
                if self._mass_num < other._mass_num:
                    return True
                else:
                    return False
            else:
                return False
        except:
            #raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")
            return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


    def __gt__(self, other):
        try:
            if self._atomic_num > other._atomic_num:
                return True
            elif self._atomic_num == other._atomic_num:
                if self._mass_num > other._mass_num:
                    return True
                else:
                    return False
            else:
                return False
        except:
            #raise TypeError(f"Cannot compare Isotope with type \"{type(other)}\".")
            return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

