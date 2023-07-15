# Python class for molecule, made of elements

from collections import defaultdict

from .exceptions import *
from .printer import *
from .conversion import wt_to_at, at_to_wt, percent

from .isotope import Isotope
from .element import Element

class Molecule:
    
    def __init__(self, name: str, elements: dict[Element, int], **kwargs) -> None:

        self._name: str = name                              # name
        self._elements: dict[Element, int] = {}             # {element: atoms}
        self._elementsFractions: dict[Element, float] = {}  # {element: atomic fraction}
        self._atoms: int                                    # number of atoms
        self._atomic_wt: float                              # atomic weight, weighted by (atomic) abundance of isotopes

        if not all(atoms > 0 for atoms in elements.values()):
            # either all negative or mixed
            if all(atoms < 0 for atoms in elements.values()):
                # given in terms of weight
                raise FractionError(f"Molecule \"{self._name}\": Giving weight fractions is not allowed for molecules.")

            else:
                # mixed
                raise FractionError(f"Molecule \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")
        else:
            # given in terms of atoms, no action needed
            pass

        self._atoms = int(sum(elements.values()))
        for element, element_atoms in elements.items():
            
            if element_atoms == 0:
                # not present in molecule
                pass
            else:
                # given as atoms
                self._elements[element] = element_atoms  # not normalised
                self._elementsFractions[element] = element_atoms / self._atoms  # normalised

        if "atomic_wt" in kwargs:
            self._atomic_wt = kwargs["atomic_wt"]
        else:
            self._atomic_wt = self.calc_atomic_wt()

        return


    # ########
    # Getter
    # ########

    @property
    def name(self):
        """Name of the molecule."""
        return self._name

    @property
    def elements(self):
        """Dictionary of elements."""
        return self._elements

    @property
    def elementsFractions(self):
        """Dictionary of fractions of elements."""
        return self._elementsFractions

    @property
    def atoms(self):
        """Number of atoms in the molecule."""
        return self._atoms

    @property
    def atomic_wt(self):
        """Atomic weight of element, weighted by (atomic) abundance of isotopes."""
        return self._atomic_wt


    # ########
    # Functions
    # ########

    def calc_atomic_wt(self) -> float:
        """Calculates atomic weight of molecule, weighted by number of atoms per element."""
        
        atomic_wt = sum([element_atoms * element.atomic_wt for element, element_atoms in self._elements.items()])

        return atomic_wt

    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]] = None, par_at_frac: float = 1.0) -> list[dict[Isotope, float]]:
        """Appends all isotopes with their atomic fraction to given dictionary."""

        if dict_list is None:
            dict_list = defaultdict(list)  # new defaultdict should be the default value for dict_list, but those are mutable and stay the same object over multiple function calls (clutter up)
                                           # thanks to Don Cross' article: https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422
        for element, at_frac in self._elementsFractions.items():
            dict_list = element._append_isotopes(dict_list, par_at_frac*at_frac)

        return dict_list

    def get_isotopes(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes().items())}


    # ########
    # Print
    # ########

    def string(self) -> str:
        """Returns molecule name."""
        return self._name

    def print_overview(self, scale: bool = False, numbering_str: str = "", par_at_frac: float = 1.0, par_wt_frac: float = 1.0) -> None:
        """Prints an overview of the molecule.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Molecule \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._atomic_wt))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), par_at_frac*1e2, par_wt_frac*1e2))

        wt_fracs = at_to_wt(self._elementsFractions)
        
        for i, (element, ele_at_frac) in enumerate(self._elementsFractions.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            ele_wt_frac = wt_fracs[element]

            if scale:
                ele_at_frac = par_at_frac * ele_at_frac
                ele_wt_frac = par_wt_frac * ele_wt_frac
            
            print(sma_sep)
            element.print_overview(scale, cur_num_str, ele_at_frac, ele_wt_frac)

        return


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.string()

    def __repr__(self):
        return self.string()
