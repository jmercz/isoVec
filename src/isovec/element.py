# Python class for element, made of isotopes

from collections import defaultdict

from .substance import Substance
from .isotope import Isotope
from .isotopes import _natural_compositions

from .constants import ATOM_NUMB_TO_SYMBOL


class Element(Substance):

    # override
    #_ALLOWED_CLASSES = (Isotope,)
    @classmethod
    def _GET_ALLOWED_CLASSES(cls):
        """Returns a tuple of allowed classes for constituents."""
        return (Isotope,)

    def __init__(self, name: str, isotopes: dict[Isotope, float], mode: str = "_legacy", natural: bool = False, **kwargs) -> None:

        super().__init__(name=name, constituents=isotopes, mode=mode, **kwargs)

        self._is_natural = natural

        # take atomic number of first isotope (and make sure all isotopes are of the same element)
        self._Z: int = next(iter(isotopes)).Z  # atomic number of element
        if not all(self._Z == isotope.Z for isotope in isotopes.keys()):
            raise ValueError(f"Atomic number of all isotopes of {self.__class__.__name__} \"{self._name}\" must match!")
        
        # search for symbol
        if self._symbol == "":
            self._symbol = ATOM_NUMB_TO_SYMBOL[self._Z]

    # override
    @classmethod
    def _inp_constituents_volume(cls, inp_constituents: dict[Isotope, float]) -> dict[Isotope, float]:
        raise ValueError(f"Input mode 'volume' is disabled for {cls.__name__} creation.")


    # ########
    # Properties
    # ########

    @property
    def Z(self):
        """Atomic number of the element."""
        return self._Z
    
    @property
    def A_r(self):
        """Relative atomic mass (atomic weight) [-] of the element."""
        return self._calc_A_r()


    # ########
    # Quantity Calculation
    # ########

    def _calc_A_r(self) -> float:
        r"""Calculates relative atomic mass (atomic weight) [-] of the element.
        
        The relative atomic masses of all isotopes are weighted by their atomic fraction and summed up:
            $$\overline{M} = \sum_i \left( x_i \cdot A_\mathrm{r},i \right)$$
        """
        return sum(x_i*constituent.M for constituent, x_i in self._constituents.items())


    # ########
    # Isotope Collection
    # ########

    # override
    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]], by_weight: bool = False, f_p: float = 1.0, use_natural: bool = False) -> defaultdict[Isotope, list[float]]:
        if not by_weight:
            constituents = self._constituents
        else:
            constituents = self.get_constituents_in_wt() 
        if use_natural and self._is_natural:
            natural_isotope = _natural_compositions[self._Z]
            f_i = sum(constituents.values())
            dict_list[natural_isotope].append(f_p*f_i)
        else:
            for isotope, f_i in constituents.items():
                dict_list[isotope].append(f_p*f_i)
        return dict_list
    

    # ########
    # Print
    # ########

    def print_overview(self, scale: bool = False, numbering_str: str = "", x_p: float = 1.0, w_p: float = 1.0) -> None:
        """Prints an overview of the element.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Element \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._M))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), x_p*1e2, w_p*1e2))
        print()

        # calculate weight fractions of isotopes
        wt_constituents = self.get_constituents_in_wt()

        for i, (isotope, x_i) in enumerate(self._constituents.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            w_i = wt_constituents[isotope]

            if scale:
                # scale with parent fraction
                x_i = x_p * x_i
                w_i = w_p * w_i
            
            print("{0:<9} {1:<7} {2:8.4f} at.%  |  {3:8.4f} wt.%".format(cur_num_str, isotope._name + ":", x_i*1e2, w_i*1e2))

        return