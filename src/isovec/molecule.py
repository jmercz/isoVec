# Python class for molecule, made of elements

from .printer import *

from .substance import Substance
from .element import Element


class Molecule(Substance):

    # override
    #_ALLOWED_CLASSES = (Element,)
    @classmethod
    def _GET_ALLOWED_CLASSES(cls):
        """Returns a tuple of allowed classes for constituents."""
        return (Element,)

    def __init__(self, name: str, elements: dict[Element, float], mode: str = "_legacy", **kwargs) -> None:

        self._atoms: int = int(sum(elements.values()))  # number of atoms in molecule

        super().__init__(name=name, constituents=elements, mode=mode, kwargs=kwargs)
        
    # override
    @classmethod
    def _inp_constituents_weight(cls, inp_constituents: dict[Element, float]) -> dict[Element, float]:
        raise ValueError(f"Input mode 'weight' is disabled for {cls.__name__} creation.")
    
    # override
    @classmethod
    def _inp_constituents_volume(cls, inp_constituents: dict[Element, float]) -> dict[Element, float]:
        raise ValueError(f"Input mode 'volume' is disabled for {cls.__name__} creation.")

    # override
    @classmethod
    def _inp_constituents_legacy(cls, inp_constituents: dict[Element, float]) -> dict[Element, float]:
        
        if not all(frac > 0 for frac in inp_constituents.values()):  # either all negative or mixed
            if all(frac < 0 for frac in inp_constituents.values()):  # all negative -> weight fractions given, need to be converted
                raise ValueError(f"Could not create {cls.__name__}: Giving weight fractions is not allowed for molecules..")
            else:  # mixed, not allowed
                raise ValueError(f"Could not create {cls.__name__}: Mixing of atomic and weight fractions is not allowed.")
        else:  # all positive -> atomic fractions given, no action needed
            return inp_constituents

    @property
    def atoms(self):
        """Number of atoms in the molecule."""
        return self._atoms
    
    @property
    def constituent_atoms(self):
        """Dictionary with constituents and their number of atoms in the molecule."""
        return {constituent: int(x_i*self._atoms) for constituent, x_i in self._constituents.items()}
    
    # override
    def _calc_M(self) -> float:
        """Calculates molar mass of the molecule.
        
        The molar masses of all constituents are multiplied by their number of atoms in the molecule and summed up:
            $$\overline{M} = \sum_i \left( N_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """
        if all(constituent.M > 0 for constituent in self._constituents.keys()):
            return sum(N_i*constituent.M for constituent, N_i in self.constituent_atoms.items())
        else:
            return 0.0


    def print_overview(self, scale: bool = False, numbering_str: str = "", x_p: float = 1.0, w_p: float = 1.0) -> None:
        """Prints an overview of the molecule.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Molecule \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._M))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), x_p*1e2, w_p*1e2))

        wt_constituents = self.get_constituents_in_wt()
        
        for i, (element, x_i) in enumerate(self._constituents.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            w_i = wt_constituents[element]

            if scale:
                x_i = x_p * x_i
                w_i = w_p * w_i
            
            print(sma_sep)
            element.print_overview(scale, cur_num_str, x_i, w_i)

        return