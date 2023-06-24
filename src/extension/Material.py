# python module for Serpent2 material

from collections import defaultdict

from ..isovec.Isotope import Isotope


class Material:

    _xsT = "03c" # TODO: implement all temperatures

    def __init__(self, name: str, density: float, constituent: any, **kwargs) -> 'Material':

        self._name: str = name
        self._density: float = density
        self._constituent = constituent
        
        self._rgb: tuple = (-1,-1,-1)

        if "rgb" in kwargs:
            self._rgb = kwargs["rgb"]

        
        return

    # ########
    # Getter
    # ########

    @property
    def name(self):
        """ Name of the material """
        return self._name

    @property
    def density(self):
        """ Density of the material """
        return self._density

    @property
    def constituent(self):
        """ Dictionary of constituents """
        return self._constituent

    @property
    def rgb(self):
        """ RGB triple of the material """
        return self._rgb


    # ########
    # Functions
    # ########

    def AppendIsotopes(self) -> defaultdict[Isotope, list[float]]:
        """ Get all isotopes and their atmoc fraction """
        return self._constituent.AppendIsotopes()

    def PrintMatCard(self) -> None:
        """ Print material card for Serpent2 """

        # card header
        cardHeader = "mat {0} {1}".format(self._name, self._density)
        if self._rgb != (-1,-1,-1):
            cardHeader += " rgb {0} {1} {2}".format(*self._rgb)
        print(cardHeader)

        # isotopes
        isotopes = self.AppendIsotopes()
        for isotope, fractions in sorted(isotopes.items()):
            xsFile = "{0}{1:03}.{2}".format(isotope.atomicNumber, isotope.massNumber, self._xsT)
            print("        {0:>10}  {1:11E}     % {2}".format(xsFile, sum(fractions), isotope.name))

        return
