"""Class for Molecule

Molecule class serves as constituents for `Mixture`.
"""

from .substance import Substance
from .element import Element
from .node import sma_sep


class Molecule(Substance):
    """A substance containing at least two atoms, potentially from different elements.

    A molecule shares its properties with its parent class `Substance`, with
    the exception that constituents can only be elements. The distribution of
    elements can be expressed as fractions or in integers, which sum up to the
    total amount of atoms in the molecule.
    """

    # override
    @classmethod
    def _get_allowed_constituents(cls):
        return (Element,)

    def __init__(self, name: str, composition: dict[Element, float], mode: str = "_legacy", **kwargs) -> None:
        """Constructor of molecule.
        
        Args:
            name:
                Descriptive name.
            composition:
                Dictionary that maps an element of the molecule to its atomic
                fraction or number of atoms. Values are normalsied and don't
                need to add up to unity.
            mode:
                Fractions in elements can be interpreted only as atomic
                fractions or number of atoms. The default value allows inputs
                as before 1.1.0.
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
            not an element.
        """

        self._atoms: int = int(sum(composition.values()))  # number of atoms in molecule

        super().__init__(name=name, composition=composition, mode=mode, **kwargs)

        # construct symbol
        if not self._symbol:
            sym = ""
            for element, atoms in self.get_composition_in_atoms().items():
                sym += f"{element.element_symbol()}"
                if atoms > 1:
                    sym += f"{atoms:.2g}"
            self._symbol = sym
        
    # override
    @classmethod
    def _inp_composition_weight(cls, inp_composition: dict[Element, float]) -> dict[Element, float]:
        raise ValueError(f"Input mode 'weight' is disabled for {cls.__name__} creation.")
    
    # override
    @classmethod
    def _inp_composition_volume(cls, inp_composition: dict[Element, float]) -> dict[Element, float]:
        raise ValueError(f"Input mode 'volume' is disabled for {cls.__name__} creation.")


    # ########
    # Properties
    # ########

    @property
    def atoms(self):
        """Number of atoms in the molecule."""
        return self._atoms
    

    # ########
    # Quantity Calculation
    # ########

    # override
    def _calc_M(self) -> float:
        r"""Calculates molar mass.
        
        The molar masses of all constituents are multiplied by their number of
        atoms in the molecule and summed up:
            $$\overline{M} = \sum_i \left( N_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """
        if all(constituent.M > 0 for constituent in self._composition.keys()):
            return sum(N_i*constituent.M for constituent, N_i in self.get_composition_in_atoms().items())
        else:
            return 0.0


    # ########
    # Conversion
    # ########

    def get_composition_in_atoms(self) -> dict[Element, float]:
        """Returns constituents with their number of atoms."""
        return {element: int(x_i*self._atoms) for element, x_i in self._composition.items()}


    # ########
    # Collection
    # ########

    # override
    def _append_elements(self, element_list: dict[int, tuple[Substance, float]], by_weight: bool = False, f_p: float = 1.0):

        element_list[-1] = element_list[-1] + 1  # increase counter

        if not by_weight:
            composition = self.get_composition_in_atoms()
        else:
            composition = self.get_composition_in_wt()  
        
        for constituent, f_i in composition.items():
            constituent._append_elements(element_list, by_weight, f_p*f_i)

        return element_list
