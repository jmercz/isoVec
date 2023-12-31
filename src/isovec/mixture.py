"""Class for Mixture.

Mixture class is the top class, but may serve as a constituent for itself.
"""

from typing import Union, TypeAlias

from .substance import Substance
from .element import Element
from .molecule import Molecule


Constituent: TypeAlias = Union["Mixture", Molecule, Element]

class Mixture(Substance):
    """A substance made of elements, molecules or other mixtures.

    A molecule shares its properties with its parent class `Substance`.
    Furthermore, it is possible to calculate the density of a mixture, as long
    as all its constituents have a specified density.
    """

    # override
    @classmethod
    def _get_allowed_constituents(cls):
        return (Mixture, Molecule, Element)
    
    def __init__(self, name: str, composition: dict[Constituent, float], mode: str = "_legacy", **kwargs) -> None:
        """Constructor of mixture.
        
        Args:
            name:
                Descriptive name.
            composition:
                Dictionary that maps a constituent of the mixture to its
                fraction. The fractions are physically interpreted according
                to the given mode. Values are normalsied and don't need to add
                up to unity.
            mode:
                Fractions in the composition can be interpreted as atomic,
                weight or volumetric fractions. Volumetric is only valid, if
                all constituents have a density. The default value allows
                inputs as before v1.1.0, where positive fractions refer to
                atomic and negative fractions to weight.
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

        super().__init__(name=name, composition=composition, mode=mode, **kwargs)

        if self._rho == 0.0:
            self._rho = self._calc_rho()


    # ########
    # Quantity Calculation
    # ########

    def _calc_rho(self) -> float:
        r"""Calculates average density.
        
        The densities of all constituents are weighted by their weight fraction,
        summed up and inverted:
            $$\overline{\rho} = \left( \sum_i \frac{w_i}{\rho_i} \right)^{-1}$$
        Will return zero if calculation is not possible.
        """
        if all(constituent.M > 0 for constituent in self._composition.keys()):
            wt_composition = self.get_composition_in_wt()
        else:
            return 0.0

        if all(constituent.rho > 0 for constituent in wt_composition.keys()):
            summed = sum(w_i / constituent.rho for constituent, w_i in wt_composition.items())
            return summed**-1
        else:
            return 0.0
