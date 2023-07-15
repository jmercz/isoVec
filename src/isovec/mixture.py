# Python class for mixture, made of elements or compounds

from typing import Union
from collections import defaultdict

from .exceptions import *
from .printer import *
from .conversion import wt_to_at, at_to_wt, percent

from .isotope import Isotope
from .element import Element
from .molecule import Molecule

Constituent = Union[Element, Molecule]

class Mixture:

    def __init__(self, name: str, constituents: dict[Constituent, float]) -> None:

        self._name: str = name                             # name
        self._constituents: dict[Constituent, float] = {}  # {constituent: atomic fraction}
        self._atomic_wt: float = 0.0

        if not all(frac > 0 for frac in constituents.values()):
            # either all negative or mixed
            if all(frac < 0 for frac in constituents.values()):
                # given in terms of weight fraction

                # remove negative sign from input
                for constituent, wt_frac in constituents.items():
                    constituents[constituent] = abs(wt_frac)

                # convert to atomic fraction
                constituents = wt_to_at(constituents)

            else:
                # mixed
                raise FractionError(f"Mixture \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")
        else:
            # given in terms of atomic fraction, no action needed
            pass

        frac_sum = sum(constituents.values())
        for constituent, frac in constituents.items():
            
            if frac == 0:
                # not present in mixture
                pass
            else:
                # given as atomic fraction or already converted to atomic fraction
                self._constituents[constituent] = frac / frac_sum  # normalised

        return


    # ########
    # Getter
    # ########

    @property
    def name(self):
        """Name of the mixture."""
        return self._name

    @property
    def constituents(self):
        """Dictionary of constituents their abundance (atomic fractions)."""
        return self._constituents


    # ########
    # Functions
    # ########

    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]] = None, par_at_frac: float = 1.0) -> defaultdict[Isotope, list[float]]:
        """Appends all isotopes with their atomic fraction to given dictionary."""

        if dict_list is None:
            dict_list = defaultdict(list)  # new defaultdict should be the default value for dict_list, but those are mutable and stay the same object over multiple function calls (clutter up)
                                           # thanks to Don Cross' article: https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422

        for constituent, at_frac in self._constituents.items():
            dict_list = constituent._append_isotopes(dict_list, par_at_frac*at_frac)

        return dict_list

    def get_isotopes(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes().items())}


    # ########
    # Print
    # ########

    def string(self) -> str:
        """Returns mixture name."""
        return self._name

    def print_overview(self, scale: bool = False, numbering_str: str = "", par_at_frac: float = 1.0, par_wt_frac: float = 1.0) -> None:
        """Prints an overview of the mixture.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """
        
        print()
        print(big_sep)
        print()
        #print("{0} Mixture \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._atomic_wt))
        print("{0} Mixture \"{1}\"".format(numbering_str, self._name))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), par_at_frac*1e2, par_wt_frac*1e2))
        print()

        wt_fracs = at_to_wt(self._constituents)

        for i, (constituent, con_at_frac) in enumerate(self._constituents.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            con_wt_frac = wt_fracs[constituent]

            if scale:
                con_at_frac = par_at_frac * con_at_frac
                con_wt_frac = par_wt_frac * con_wt_frac
            
            print(med_sep)
            constituent.print_overview(scale, cur_num_str, con_at_frac, con_wt_frac)

        print(med_sep)
        print()
        print(big_sep)
        
        return


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.string()

    def __repr__(self):
        return self.string()
