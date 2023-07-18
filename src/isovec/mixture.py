# Python class for mixture, made of elements or compounds

from typing import Union, TypeAlias
from collections import defaultdict

from .exceptions import *
from .printer import *
from .conversion import wt_to_at, at_to_wt, percent

from .substance import Substance
from .isotope import Isotope
from .element import Element
from .molecule import Molecule


Constituent: TypeAlias = Union["Mixture", Molecule, Element]

class Mixture(Substance):

    # override
    #_ALLOWED_CLASSES = (Constituent,)
    @classmethod
    def _GET_ALLOWED_CLASSES(cls):
        """Returns a tuple of allowed classes for constituents."""
        return (Mixture, Molecule, Element)
    
    def __init__(self, name: str, constituents: dict[Isotope, float], mode: str = "_legacy", **kwargs) -> None:

        super().__init__(name=name, constituents=constituents, mode=mode, kwargs=kwargs)


    def print_overview(self, scale: bool = False, numbering_str: str = "", x_p: float = 1.0, w_p: float = 1.0) -> None:
        """Prints an overview of the mixture.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """
        
        print()
        print(big_sep)
        print()
        #print("{0} Mixture \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._atomic_wt))
        print("{0} Mixture \"{1}\"".format(numbering_str, self._name))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), x_p*1e2, w_p*1e2))
        print()

        wt_constituents = self.get_constituents_in_wt()

        for i, (constituent, x_i) in enumerate(self._constituents.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            w_i = wt_constituents[constituent]

            if scale:
                x_i = x_p * x_i
                w_i = w_p * w_i
            
            print(med_sep)
            constituent.print_overview(scale, cur_num_str, x_i, w_i)

        print(med_sep)
        print()
        print(big_sep)
        
        return