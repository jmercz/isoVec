# Python class for element, made of isotopes

from collections import defaultdict

from .substance import Substance
from .isotope import Isotope


class Element(Substance):

    # override
    #_ALLOWED_CLASSES = (Isotope,)
    @classmethod
    def _GET_ALLOWED_CLASSES(cls):
        """Returns a tuple of allowed classes for constituents."""
        return (Isotope,)

    def __init__(self, name: str, isotopes: dict[Isotope, float], mode: str = "_legacy", **kwargs) -> None:

        super().__init__(name=name, constituents=isotopes, mode=mode, kwargs=kwargs)

        # take atomic number of first isotope (and make sure all isotopes are of the same element)
        self._Z: int = next(iter(isotopes)).Z  # atomic number of element
        if not all(self._Z == isotope.Z for isotope in isotopes.keys()):
            raise ValueError(f"Atomic number of all isotopes of {self.__class__.__name__} \"{self._name}\" must match!")

    # override
    @classmethod
    def _inp_constituents_volume(cls, inp_constituents: dict[Isotope, float]) -> dict[Isotope, float]:
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
        """Calculates relative atomic mass (atomic weight) [-] of the element.
        
        The relative atomic masses of all isotopes are weighted by their atomic fraction and summed up:
            $$\overline{M} = \sum_i \left( x_i \cdot A_\mathrm{r},i \right)$$
        """
        return sum(x_i*constituent.M for constituent, x_i in self._constituents.items())


    # ########
    # Isotope Collection
    # ########

    # override
    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]], x_p: float = 1.0) -> defaultdict[Isotope, list[float]]:
        for isotope, x_i in self._constituents.items():
            dict_list[isotope].append(x_p*x_i)
        return dict_list
    

    # ########
    # Print
    # ########

    def print_overview(self, scale: bool = False, numbering_str: str = "", x_p: float = 1.0, w_p: float = 1.0) -> None:
        """Prints an overview of the element.

          scale = True - adapts the fractions of sub-components according to the fraction of the parent-component
        """

        print("{0} Element \"{1}\": {2:.4f} g/mol".format(numbering_str, self._name, self._M))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), x_p*1e2, w_p*1e2))
        print()

        # calculate weight fractions of isotopes
        wt_constituents = self.get_constituents_in_wt()

        for i, (isotope, x_i) in enumerate(self._constituents.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            w_i = wt_constituents[isotope]

            if scale:
                # scale with parent fraction
                x_i = x_p * x_i
                w_i = w_p * w_i
            
            print("{0:<9} {1:<7} {2:8.4f} at.%  |  {3:8.4f} wt.%".format(cur_num_str, isotope._name + ":", x_i*1e2, w_i*1e2))

        return