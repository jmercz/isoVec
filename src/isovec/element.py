"""Class for Element

Element class serves as constituents for `Molecule`.
"""

from collections import defaultdict

from .substance import Substance
from .isotope import Isotope
from .isotopes import _natural_compositions
from .constants import ATOM_NUMB_TO_SYMBOL


class Element(Substance):
    """A substance containing only isotopes with the same atomic number.

    An element shares its properties with its parent class `Substance`, with
    the exception that constituents can only be isotopes and therefore has a
    well-defined atomic number Z and relative atomic mass A_r itself. An 
    element can be flagged as a natural element, indicating the natural 
    abundance of its isotopes. 
    """

    # override
    @classmethod
    def _get_allowed_classes(cls):
        return (Isotope,)

    def __init__(self, name: str, isotopes: dict[Isotope, float], mode: str = "_legacy", natural: bool = False, **kwargs) -> None:
        """Constructor of element.
        
        Args:
            name:
                Descriptive name.
            isotopes:
                Dictionary that maps an isotope of the element to its
                fraction. The fractions are physically interpreted according
                to the given mode. Values are normalsied and don't need to add
                up to unity.
            mode:
                Fractions in isotopes can be interpreted as atomic or weight
                fractions. The default value allows inputs as before 1.1.0, 
                where positive fractions refer to atomic and negative fractions
                to weight.
            **kwargs:
                Keyword arguments to override values.
        
        Keyword Args:
            M (float):
                Set molar mass.
            rho (float):
                Set density.
            symbol (str):
                Short symbol.

        Raises:
            ValueError: If non-valid constructor mode or given constituent is
            not an isotope.
        """

        super().__init__(name=name, constituents=isotopes, mode=mode, **kwargs)

        self._is_natural = natural

        # take atomic number of first isotope (and make sure all isotopes are of the same element)
        self._Z: int = next(iter(isotopes)).Z  # atomic number of element
        if not all(self._Z == isotope.Z for isotope in isotopes.keys()):
            raise ValueError(f"Atomic number of all isotopes of {self.__class__.__name__} \"{self._name}\" must match!")
        
        # construct symbol
        if not self._symbol:
            self._symbol = self.element_symbol()
        

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
        
        The relative atomic masses of all isotopes are weighted by their atomic
         fraction and summed up:
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
    # Functions
    # ########

    def element_symbol(self) -> str:
        """Returns the element symbol as a string."""
        return ATOM_NUMB_TO_SYMBOL[self._Z]


    # ########
    # Print
    # ########

    def print_overview(self, scale: bool = False, **kwargs) -> None:
        """Prints an overview of the element.

        Args:
            scale:
                Adapts the fractions of sub-components according to the fraction
                of the parent-component.
            **kwargs:
                Internal dictionary to pass information down recursive calls.
        """

        # get data from kwargs
        numbering_str = kwargs.get("numbering_str", "")
        x_p = kwargs.get("x_p", 1.0)
        w_p = kwargs.get("w_p", 1.0)

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
