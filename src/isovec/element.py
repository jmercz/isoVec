# Python class for element, made of isotopes

from collections import defaultdict

from .exceptions import *
from .conversion import wt_to_at, at_to_wt, percent

from .isotope import Isotope

class Element:

    def __init__(self, name: str, isotopes: dict[Isotope, float], **kwargs) -> None:
        """Element object

        Optional parameters:
          "atomic_wt": float - overwrite atomic weight of element
        """
        
        self._name: str = name                     # name
        self._atomic_num: int                        # atomic number (protons)
        self._isotopes: dict[Isotope, float] = {}  # {isotope: atomic fraction}
        self._atomic_wt: float                       # atomic weight, weighted by (atomic) abundance of isootopes

        if not all(frac > 0 for frac in isotopes.values()):
            # either all negative or mixed
            if all(frac < 0 for frac in isotopes.values()):
                # given in terms of weight fraction
                
                # remove negative sign from input
                for isotope, wt_frac in isotopes.items():
                    isotopes[isotope] = abs(wt_frac)

                # convert to atomic fraction
                isotopes = wt_to_at(isotopes)

            else:
                raise FractionError(f"Element \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")

        # set atomic number from first isotope
        self._atomic_num = list(isotopes.keys())[0].Z

        frac_sum = sum(isotopes.values())
        for isotope, frac in isotopes.items():
            
            # check if atomic number matches
            if isotope.Z != self._atomic_num:
                raise ValueError(f"Atomic number of all isotopes of Element \"{self._name}\" must match!")

            if frac == 0:
                # not present in element
                pass
            else:
                # given as atomic fraction or already converted to atomic fraction
                self._isotopes[isotope] = frac / frac_sum  # normalised

        # process kwargs
        self._atomic_wt = kwargs.get("atomic_wt", self.calc_atomic_wt())  # use given atomic weight or calculate
            

        return
                
    

    # ########
    # Getter
    # ########

    @property
    def name(self):
        """Name of the element."""
        return self._name

    @property
    def atomic_num(self):
        """Atomic number (number of protons)."""
        return self._atomic_num

    @property
    def isotopes(self):
        """Dictionary of isotopes and their abundance (atomic fractions)."""
        return self._isotopes
    
    @property
    def atomic_wt(self):
        """Atomic weight of element, weighted by (atomic) abundance of isotopes."""
        return self._atomic_wt


    # ########
    # Functions
    # ########

    def calc_atomic_wt(self) -> float:
        """Calculates atomic weight of element, weighted by (atomic) abundance of isotopes."""

        atomic_wt = sum([at_frac * isotope.M for isotope, at_frac in self._isotopes.items()])

        return atomic_wt

    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]] = None, par_at_frac: float = 1.0) -> defaultdict[Isotope, list[float]]:
        """Appends all isotopes with their atomic fraction to given dictionary."""

        if dict_list is None:
            dict_list = defaultdict(list)  # new defaultdict should be the default value for dict_list, but those are mutable and stay the same object over multiple function calls (clutter up)
                                           # thanks to Don Cross' article: https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422

        for isotope, at_frac in self._isotopes.items():
            dict_list[isotope].append(par_at_frac*at_frac)

        return dict_list

    def get_isotopes(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes().items())}

    def hash(self) -> int:
        """Hashes element via name."""
        return hash(self._name)


    # ########
    # Print
    # ########

    def string(self) -> str:
        """Returns element name."""
        return self._name

    def print_overview(self, scale: bool = False, numbering_str: str = "", par_at_frac: float = 1.0, par_wt_frac: float = 1.0) -> None:
        """Prints an overview of the element.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Element \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._atomic_wt))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), par_at_frac*1e2, par_wt_frac*1e2))
        print()

        # calculate weight fractions of isotopes
        wt_fracs = at_to_wt(self._isotopes)

        for i, (isotope, iso_at_frac) in enumerate(self._isotopes.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            iso_wt_frac = wt_fracs[isotope]

            if scale:
                # scale with parent fraction
                iso_at_frac = par_at_frac * iso_at_frac
                iso_wt_frac = par_wt_frac * iso_wt_frac
            
            print("{0:<9} {1:<7} {2:8.4f} at.%  |  {3:8.4f} wt.%".format(cur_num_str, isotope._name + ":", iso_at_frac*1e2, iso_wt_frac*1e2))

        return



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
            return self._name == other._name
        except:
            #raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")
            return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        try:
            return self._atomic_num < other._atomic_num
        except:
            #raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")
            return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        try:
            return self._atomic_num > other._atomic_num
        except:
            #raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")
            return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
