# Python class for molecule, made of elements

from .exceptions import *

from collections import defaultdict

from .Isotope import Isotope
from .Element import Element

from .printer import *
from .conversion import WtToAt, AtToWt

class Molecule:
    
    def __init__(self, name: str, elements: dict[Element, int], **kwargs) -> 'Molecule':

        self._name: str = name                             # name
        self._elements: dict[Element, int] = {}            # {element: atoms}
        self._elementsFractions: dict[Element, float] = {} # {element: atomic fraction}
        self._atoms: int                                   # number of atoms
        self._atomicWeight: float                          # atomic weight, weighted by (atomic) abundance of isotopes

        if not all(atoms > 0 for atoms in elements.values()):
            # either all negative or mixed
            if all(atoms < 0 for atoms in elements.values()):
                # given in terms of weight
                raise FractionError(f"Molecule \"{self._name}\": Giving weight fractions is not allowed for molecules.")

            else:
                # mixed
                raise FractionError(f"Molecule \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")
        else:
            # given in terms of atoms, no action needed
            pass

        self._atoms = int(sum(elements.values()))
        for element, elementAtoms in elements.items():
            
            if elementAtoms == 0:
                # not present in molecule
                pass
            else:
                # given as atoms
                self._elements[element] = elementAtoms # not normalised
                self._elementsFractions[element] = elementAtoms / self._atoms # normalised

        if "atomicWeight" in kwargs:
            self._atomicWeight = kwargs["atomicWeight"]
        else:
            self._atomicWeight = self.CalcAtomicWeight()

        return


    # ########
    # Getter
    # ########

    @property
    def name(self):
        """ Name of the molecule """
        return self._name

    @property
    def elements(self):
        """ Dictionary of elements """
        return self._elements

    @property
    def elementsFractions(self):
        """ Dictionary of fractions of elements """
        return self._elementsFractions

    @property
    def atomicWeight(self):
        """ Atomic weight of element, weighted by (atomic) abundance of isotopes """
        return self._atomicWeight

    @property
    def atoms(self):
        """ Number of atoms in the molecule """
        return self._atoms


    # ########
    # Functions
    # ########

    def CalcAtomicWeight(self) -> float:
        """
        Calculate atomic weight of molecule, weighted by (atomic) fraction of elements
        """

        atomicWeight = sum([elementAtoms * element._atomicWeight for element, elementAtoms in self._elements.items()])

        return atomicWeight

    def AppendIsotopes(self, dictList: defaultdict[Isotope, list[float]] = None, topFraction: float = 1.0) -> list[dict[Isotope, float]]:
        """
        Takes input dictionary and appends all isotopes with their atomic fraction
        """

        if dictList is None:
            dictList = defaultdict(list)  # new defaultdict should be the default value for dictList, but those are mutable and stay the same object over multiple function calls (clutter up)
                                          # thanks to Don Cross' article: https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422
        for element, fraction in self._elementsFractions.items():
            dictList = element.AppendIsotopes(dictList, topFraction*fraction)

        return dictList

    def GetIsotopes(self) -> dict[Isotope, float]:
        """ Gets all isotopes with their atomic fraction from the constituents """
        return {isotope: sum(atFractions) for isotope, atFractions in sorted(self.AppendIsotopes().items())}


    # ########
    # Print
    # ########

    def String(self) -> str:
        """ Return Molecule as string """
        return self._name

    def PrintOverview(self, scale: bool = False, numberStr: str = "", atFrac: float = 1.0, wtFrac: float = 1.0) -> None:
        """
        Prints an overview of the molecule.
          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Molecule \"{1}\": {2:.4f} g/mol".format(numberStr, self._name, self._atomicWeight))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numberStr), atFrac*1e2, wtFrac*1e2))

        dictWtFrac = AtToWt(self._elementsFractions)

        for i, (element, atFraction) in enumerate(self._elementsFractions.items(), start = 1):
            iStr = numberStr + str(i) + "."
            wtFraction = dictWtFrac[element]

            if scale:
                atFraction = atFrac * atFraction
                wtFraction = wtFrac * wtFraction
            
            print(smaSep)
            element.PrintOverview(scale, iStr, atFraction, wtFraction)

        return


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.String()

    def __repr__(self):
        return self.String()