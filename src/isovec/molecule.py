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

        self._M_mol = self._calc_M_mol()  # molar mass of molecule

        # construct symbol
        if not self._symbol:
            sym = ""
            for element, atoms in self.get_constituent_in_atoms().items():
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

    # override
    @classmethod
    def _inp_composition_legacy(cls, inp_composition: dict[Element, float]) -> dict[Element, float]:
        
        if not all(frac > 0 for frac in inp_composition.values()):  # either all negative or mixed
            if all(frac < 0 for frac in inp_composition.values()):  # all negative -> weight fractions given, need to be converted
                raise ValueError(f"Could not create {cls.__name__}: Giving weight fractions is not allowed for molecules..")
            else:  # mixed, not allowed
                raise ValueError(f"Could not create {cls.__name__}: Mixing of atomic and weight fractions is not allowed.")
        else:  # all positive -> atomic fractions given, no action needed
            return inp_composition


    # ########
    # Properties
    # ########

    @property
    def atoms(self):
        """Number of atoms in the molecule."""
        return self._atoms
    
    @property
    def M_mol(self):
        """Molar mass of molecule [g mol^-1]."""
        return self._M_mol
    

    # ########
    # Quantity Calculation
    # ########

    # override
    def _calc_M_mol(self) -> float:
        r"""Calculates molar mass of molecule.
        
        The molar masses of all constituents are multiplied by their number of
        atoms in the molecule and summed up:
            $$\overline{M} = \sum_i \left( N_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """
        if all(constituent.M > 0 for constituent in self._composition.keys()):
            return sum(N_i*constituent.M for constituent, N_i in self.get_constituent_in_atoms().items())
        else:
            return 0.0


    # ########
    # Conversion
    # ########

    def get_constituent_in_atoms(self) -> dict[Element, float]:
        """Returns constituents with their number of atoms."""
        return {element: int(x_i*self._atoms) for element, x_i in self._composition.items()}


    # ########
    # Tree
    # ########

    def _get_data_dict(self) -> dict:
        """Dictionary with data of molecule."""

        data = super()._get_data_dict()
        if self._M_mol:
            data["M_mol"] = self._M_mol

        return data


    # ########
    # Print
    # ########

    def print_overview(self, scale: bool = False, **kwargs) -> None:
        """Prints an overview of the molecule.

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

        print("{0} Molecule \"{1}\": {2:.4f} g/mol ({3:.4f} g/mol)".format(numbering_str, self._name, self._M, self._M_mol))
        print("{0}  {1:8.4f} at.%  |  {2:8.4f} wt.%".format(" "*len(numbering_str), x_p*1e2, w_p*1e2))

        wt_composition = self.get_composition_in_wt()
        
        for i, (element, x_i) in enumerate(self._composition.items(), start = 1):
            cur_num_str = numbering_str + str(i) + "."  # list indention string
            w_i = wt_composition[element]

            if scale:
                x_i = x_p * x_i
                w_i = w_p * w_i
            
            print(sma_sep)
            element.print_overview(scale, numbering_str=cur_num_str, x_p=x_i, w_p=w_i)
