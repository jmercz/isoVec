# Python class for mixture, made of elements or compounds

from typing import Union
from collections import defaultdict

from .exceptions import *

from .Isotope import Isotope
from .Element import Element
from .Molecule import Molecule

from .printer import *
from .conversion import AtToWt, WtToAt

Constituent = Union[Element, Molecule]

class Mixture:

    def __init__(self, name: str, constituents: dict[Constituent, float]) -> 'Mixture':

        self._name: str = name                            # name
        self._constituents: dict[Constituent, float] = {} # {constituent: atomic fraction}

        if not all(fraction > 0 for fraction in constituents.values()):
            # either all negative or mixed
            if all(fraction < 0 for fraction in constituents.values()):
                # given in terms of weight fraction

                # remove negative sign from input
                for constituent, wtFraction in constituents.items():
                    constituents[constituent] = abs(wtFraction)

                # convert to atomic fraction
                constituents = WtToAt(constituents)

            else:
                # mixed
                raise FractionError(f"Mixture \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")
        else:
            # given in terms of atomic fraction, no action needed
            pass

        fractionSum = sum(constituents.values())
        for constituent, fraction in constituents.items():
            
            if fraction == 0:
                # not present in mixture
                pass
            else:
                # given as atomic fraction or already converted to atomic fraction
                self._constituents[constituent] = fraction / fractionSum # normalised

        return


    # ########
    # Getter
    # ########

    @property
    def name(self):
        """ Name of the mixture """
        return self._name

    @property
    def constituents(self):
        """ Dictionary of constituents """
        return self._constituents


    # ########
    # Functions
    # ########

    def AppendIsotopes(self, dictList: defaultdict[Isotope, list[float]] = defaultdict(list)) -> defaultdict[Isotope, list[float]]:
        """
        Takes input dictionary and appends all isotopes with their atomic fraction from the constituents 
        """

        for constituent, fraction in self._constituents.items():
            dictList = constituent.AppendIsotopes(dictList, fraction)

        return dictList

    def GetIsotopes(self) -> dict[Isotope, float]:
        """ Gets all isotopes with their atomic fraction from the constituents """
        return {isotope: sum(atFractions) for isotope, atFractions in sorted(self.AppendIsotopes().items())}


    # ########
    # Print
    # ########

    def String(self) -> str:
        """ Return Mixture as string """
        return self._name

    def PrintOverview(self, scale: bool = False):
        """
        Prints an overview of the mixture.
          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """
        
        print()
        print(bigSep)
        print()
        print("Mixture \"{0}\"".format(self._name))
        print()

        dictWtFrac = AtToWt(self._constituents)

        for i, (constituent, atFraction) in enumerate(self._constituents.items(), start = 1):
            iStr = str(i) + "."
            wtFraction = dictWtFrac[constituent]
            
            print(medSep)
            constituent.PrintOverview(scale, iStr, atFraction, wtFraction)

        print(medSep)
        print()
        print(bigSep)
        
        return


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.String()

    def __repr__(self):
        return self.String()