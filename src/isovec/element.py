"""Class for Element

Element class serves as constituents for `Molecule`.
"""

from collections import defaultdict
from typing import Iterable

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
    def _get_allowed_constituents(cls):
        return (Isotope,)
    
    _RIGHT_ALIGN_PREF = -2  # override

    def __init__(self, name: str, composition: dict[Isotope, float], mode: str = "_legacy", natural: bool = False, **kwargs) -> None:
        """Constructor of element.
        
        Args:
            name:
                Descriptive name.
            composition:
                Dictionary that maps an isotope of the element to its
                fraction. The fractions are physically interpreted according
                to the given mode. Values are normalsied and don't need to add
                up to unity.
            mode:
                Fractions in the composition can be interpreted as atomic or
                weight fractions. The default value allows inputs as before
                v1.1.0, where positive fractions refer to atomic and negative
                fractions to weight.
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

        super().__init__(name=name, composition=composition, mode=mode, **kwargs)

        self._is_natural = natural

        # take atomic number of first isotope (and make sure all isotopes are of the same element)
        self._Z: int = next(iter(composition)).Z  # atomic number of element
        if not all(self._Z == isotope.Z for isotope in composition.keys()):
            raise ValueError(f"Atomic number of all isotopes of {self.__class__.__name__} \"{self._name}\" must match!")
        
        # construct symbol
        if not self._symbol:
            self._symbol = self.element_symbol()
        

    # override
    @classmethod
    def _inp_composition_volume(cls, inp_composition: dict[Isotope, float]) -> dict[Isotope, float]:
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
        return sum(x_i*isotope.A_r for isotope, x_i in self._composition.items())


    # ########
    # Collection
    # ########

    def surrogate_isotope(self) -> Isotope:
        """Returns the surrogate isotope for a natural element."""
        return _natural_compositions[self._Z]

    # override
    def _append_elements(self, element_list: dict, by_weight: bool = False, f_p: float = 1.0):

        element_list[-1] = element_list[-1] + 1  # increase counter
        element_list[element_list[-1]] = (self, f_p)  # append element
        element_list[-1] = element_list[-1] + len(self._composition)  # skip numbers of isotopes in element

        return element_list


    # ########
    # Functions
    # ########

    def element_symbol(self) -> str:
        """Returns the element symbol as a string."""
        return ATOM_NUMB_TO_SYMBOL[self._Z]


    # ########
    # Operators
    # ########
    
    def __hash__(self):
        #return hash((self.__class__, self._name))
        return hash((self.__class__, self._Z, self._M))

    def __eq__(self, other):
        try:
            if (self._Z == other._Z) and (self._M == other._M):
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
                if self._M < other._M:
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
                if self._M > other._M:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)