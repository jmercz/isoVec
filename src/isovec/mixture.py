"""Class for Mixture.

Mixture class is the top class, but may serve as a constituent for itself.
"""

from typing import Union, TypeAlias

from .substance import Substance
from .element import Element
from .molecule import Molecule
from .node import med_sep, big_sep


Constituent: TypeAlias = Union["Mixture", Molecule, Element]

class Mixture(Substance):
    """A substance made of elements, molecules or other mixtures.

    A molecule shares its properties with its parent class `Substance`.
    Furthermore, it is possible to calculate the density of a mixture, as long
    as all its constituents have a specified density.
    """

    # override
    @classmethod
    def _get_allowed_classes(cls):
        return (Mixture, Molecule, Element)
    
    def __init__(self, name: str, constituents: dict[Constituent, float], mode: str = "_legacy", **kwargs) -> None:
        """Constructor of mixture.
        
        Args:
            name:
                Descriptive name.
            constituents:
                Dictionary that maps a constituent of the mixture to its
                fraction. The fractions are physically interpreted according
                to the given mode. Values are normalsied and don't need to add
                up to unity.
            mode:
                Fractions in constituents can be interpreted as atomic, weight
                or volumetric fractions. Volumetric is only valid, if all 
                constituents have a density. The default value allows inputs
                as before 1.1.0, where positive fractions refer to atomic and 
                negative fractions to weight.
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
            not a substance.
        """

        super().__init__(name=name, constituents=constituents, mode=mode, **kwargs)

        if self._rho == 0.0:
            self._rho = self._calc_rho()


    # ########
    # Quantity Calculation
    # ########

    def _calc_rho(self) -> float:
        r"""Calculates average density of the mixture.
        
        The densities of all constituents are weighted by their weight fraction, summed up and inversed:
            $$\overline{\rho} = \left( \sum_i \frac{w_i}{\rho_i} \right)^{-1}$$
        Will return zero if calculation is not possible.
        """
        if all(constituent.M > 0 for constituent in self._constituents.keys()):
            wt_constituents = self.get_constituents_in_wt()
        else:
            return 0.0

        if all(constituent.rho > 0 for constituent in wt_constituents.keys()):
            summed = sum(w_i / constituent.rho for constituent, w_i in wt_constituents.items())
            return summed**-1
        else:
            return 0.0


    # ########
    # Print
    # ########

    def print_overview(self, scale: bool = False, **kwargs) -> None:
        """Prints an overview of the mixture.

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
            constituent.print_overview(scale, numbering_str=cur_num_str, x_p=x_i, w_p=w_i)

        print(med_sep)
        print()
        print(big_sep)
        