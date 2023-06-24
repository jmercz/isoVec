# Python class for element, made of isotopes

from collections import defaultdict

from .exceptions import *

from .Isotope import Isotope

from .conversion import WtToAt, AtToWt

class Element:

    def __init__(self, name: str, isotopes: dict[Isotope, float], **kwargs) -> 'Element':
        """
        Element object

        Optional parameters:
          "atomicWeight": float - overwrite atomic weight of element
        """
        
        self._name: str = name                     # name
        self._atomicNumber: int                    # atomic number (protons)
        self._isotopes: dict[Isotope, float] = {}  # {isotope: atomic fraction}
        self._atomicWeight: float                  # atomic weight, weighted by (atomic) abundance of isootopes

        if not all(fraction > 0 for fraction in isotopes.values()):
            # either all negative or mixed
            if all(fraction < 0 for fraction in isotopes.values()):
                # given in terms of weight fraction
                
                # remove negative sign from input
                for isotope, wtFraction in isotopes.items():
                    isotopes[isotope] = abs(wtFraction)

                # convert to atomic fraction
                isotopes = WtToAt(isotopes)

            else:
                raise FractionError(f"Element \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")

        # set atomic number from first isotope
        self._atomicNumber = list(isotopes.keys())[0].atomicNumber

        fractionSum = sum(isotopes.values())
        for isotope, fraction in isotopes.items():
            
            # check if atomic number matches
            if isotope.atomicNumber != self._atomicNumber:
                raise ValueError(f"Atomic number of all isotopes of Element \"{self._name}\" must match!")

            if fraction == 0:
                # not present in element
                pass
            else:
                # given as atomic fraction or already converted to atomic fraction
                self._isotopes[isotope] = fraction / fractionSum # normalised

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
        """ Name of the element """
        return self._name

    @property
    def atomicNumber(self):
        """ Atomic number (number of protons) """
        return self._atomicNumber

    @property
    def isotopes(self):
        """ Dictionary of isotopes and their abundance (atomic fractions) """
        return self._isotopes
    
    @property
    def atomicWeight(self):
        """ Atomic weight of element, weighted by (atomic) abundance of isotopes """
        return self._atomicWeight


    # ########
    # Functions
    # ########

    def CalcAtomicWeight(self) -> float:
        """
        Calculate atomic weight of element, weighted by (atomic) abundance of isotopes
        """

        atomicWeight = sum([atFrac * isotope.atomicWeight for isotope, atFrac in self._isotopes.items()])

        return atomicWeight

    def AppendIsotopes(self, dictList: defaultdict[Isotope, list[float]] = defaultdict(list), topFraction: float = 1.0) -> list[dict[Isotope, float]]:
        """
        Takes input dictionary and appends all isotopes with their atomic fraction
        """

        for isotope, fraction in self._isotopes.items():
            dictList[isotope].append(topFraction*fraction)

        return dictList

    def GetIsotopes(self) -> dict[Isotope, float]:
        """ Gets all isotopes with their atomic fraction from the constituents """
        return {isotope: sum(atFractions) for isotope, atFractions in sorted(self.AppendIsotopes().items())}


    # ########
    # Print
    # ########

    def String(self) -> str:
        """ Return Element as string """
        return self._name

    def PrintOverview(self, scale: bool = False, numberStr: str = "", atFrac: float = 1.0, wtFrac: float = 1.0) -> None:
        """
        Prints an overview of the element.
          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Element \"{1}\": {2:.4f} g/mol".format(numberStr, self._name, self._atomicWeight))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numberStr), atFrac*1e2, wtFrac*1e2))
        print()

        dictWtFrac = AtToWt(self._isotopes)

        for i, (isotope, atFraction) in enumerate(self._isotopes.items(), start = 1):
            iStr = numberStr + str(i) + "."
            wtFraction = dictWtFrac[isotope]

            if scale:
                atFraction = atFrac * atFraction
                wtFraction = wtFrac * wtFraction
            
            print("{0:<9} {1:<7} {2:8.4f} at.%  |  {3:8.4f} wt.%".format(iStr, isotope._name + ":", atFraction*1e2, wtFraction*1e2))

        return



    # ########
    # Operators
    # ########

    def __str__(self):
        return self.String()

    def __repr__(self):
        return self.String()

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other: 'Element'):
        try:
            return self._name == other._name
        except:
            raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")

    def __ne__(self, other: 'Element'):
        return not self.__eq__(other)

    def __lt__(self, other: 'Element'):
        try:
            return self._atomicNumber < other._atomicNumber
        except:
            raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")

    def __le__(self, other: 'Element'):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: 'Element'):
        try:
            return self._atomicNumber > other._atomicNumber
        except:
            raise TypeError(f"Cannot compare Element with type \"{type(other)}\".")

    def __ge__(self, other: 'Element'):
        return self.__gt__(other) or self.__eq__(other)