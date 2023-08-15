"""Class for Substance.

Substance class serves as the (abstract) base class for `Element`, `Molecule` and
`Mixture`.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, TypeAlias, Union, Literal
from abc import ABCMeta, abstractmethod

from .constants import N_A
from .conversion import at_to_wt, wt_to_at, vol_to_at, at_to_vol
from .isotope import Isotope
from .node import Node, char_sets


Constituent: TypeAlias = Union["Substance", Isotope]

class Substance(metaclass=ABCMeta):
    """Abstract base class for all types of substances.

    Each substance has a name and is made of constituents, each accounting for a
    certain fraction, in this case saved as atomic (or mole) fraction. Every
    substance has a molar mass, that can be calculated from its constituents,
    since the basis is made of isotopes, that have their mass implemented.
    A density can generally not be calculated but instead must be stated
    explicitly. Optionally, a shorter name can be given in the form of a symbol.
    """
    
    @classmethod
    @abstractmethod
    def _get_allowed_classes(cls):
        """Returns a tuple of allowed classes for constituents."""
        return NotImplementedError
    
    _NORMALISE = True  # normalisation of atomic fractions

    @abstractmethod
    def __init__(self, name: str, constituents: dict[Constituent, float], mode: str = "_legacy", **kwargs) -> None:
        """Constructor of substance.
        
        Args:
            name:
                Descriptive name.
            constituents:
                Dictionary that maps a constituent of the substance to its
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
            not allowed as constituent of substance.
        """

        self._name = name                             # name of the substance
        self._constituents: dict[Constituent, float]  # {constituent: atomic (mole) fraction abundance}
        self._M: float                                # molar mass [g mol^-1]
        self._rho: float                              # density [g cm^-3]
        self._symbol: str                             # symbol of the substance

        # ensure input constituents are of allowed classes
        for constituent in constituents.keys():
            if not self.instance_is_allowed(constituent):
                type_names = ", ".join(_type.__name__ for _type in self._get_allowed_classes())
                raise ValueError(f"Could not create {self.__class__.__name__} object with type {constituent.__class__.__name__} as constituent.\n"
                                 + f"Valid classes for {self.__class__.__name__} constituents: {type_names}.")

        # ensure atomic fraction of input constituents
        if mode == "_legacy":  # as done before 1.1.0
            constituents = self._inp_constituents_legacy(constituents)
        elif mode in {"atomic", "at", "mole", "mol"}:  # no conversion, only assure positive values
            constituents = self._inp_constituents_atomic(constituents)
        elif mode in {"weight", "wt"}:  # convert from weight fractions
            constituents = self._inp_constituents_weight(constituents)
        elif mode in {"volume", "vol"}:  # convert from volume fractions
            constituents = self._inp_constituents_volume(constituents)
        elif mode == "_skip":  # no action
            constituents = constituents
        else:
            raise ValueError(f"Unknown constructor mode \"{mode}\".")

        # populate constituents dictionary
        x_sum = sum(constituents.values())
        if self._NORMALISE:  # normalise fractions
            self._constituents = {constituent: (x_i / x_sum) for constituent, x_i in constituents.items() if x_i > 0}
        else:  # no normalisation
            self._constituents = {constituent: x_i for constituent, x_i in constituents.items() if x_i > 0}

        # get molar mass and density from kwargs or calculate it
        self._M = kwargs.get("M", self._calc_M())
        self._rho = kwargs.get("rho", 0.0)
        self._symbol = kwargs.get("symbol", "")
    
    @classmethod
    def _inp_constituents_atomic(cls, inp_constituents: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given atomic (mole) fractions."""
        return {constituent: abs(x_i) for constituent, x_i in inp_constituents.items()}
    
    @classmethod
    def _inp_constituents_weight(cls, inp_constituents: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given weight fractions."""
        
        wt_fracs = [abs(w_i) for w_i in inp_constituents.values()]
        molar_masses = [constituent.M for constituent in inp_constituents.keys()]

        at_fracs = wt_to_at(wt_fracs, molar_masses)
        return {constituent: x_i for constituent, x_i in zip(inp_constituents.keys(), at_fracs)}
    
    @classmethod
    def _inp_constituents_volume(cls, inp_constituents: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given volume fractions."""
        
        vol_fracs = [abs(phi_i) for phi_i in inp_constituents.values()]
        molar_volumes = [constituent.V_m for constituent in inp_constituents.keys()]

        at_fracs = vol_to_at(vol_fracs, molar_volumes)
        return {constituent: x_i for constituent, x_i in zip(inp_constituents.keys(), at_fracs)}

    @classmethod
    def _inp_constituents_legacy(cls, inp_constituents: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions as done before 1.1.0.
        
        Legacy method to maintain backwards compatibility.
        """
        
        if not all(frac > 0 for frac in inp_constituents.values()):  # either all negative or mixed
            if all(frac < 0 for frac in inp_constituents.values()):  # all negative -> weight fractions given, need to be converted
                return cls._inp_constituents_weight(inp_constituents)
            else:  # mixed, not allowed
                raise ValueError(f"Could not create {cls.__name__}: Mixing of atomic and weight fractions is not allowed.")
        else:  # all positive -> atomic fractions given, no action needed
            return inp_constituents


    # ########
    # Factory Constructor
    # ########

    @classmethod
    def from_atomic(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing atomic (mole) fractions of constituents.

        Args:
            name:
                Descriptive name.
            constituents:
                Dictionary that maps a constituent of the substance to its
                atomic fraction. Values are normalsied and don't need to add up
                to unity.
            **kwargs:
                Keyword arguments to override values.
        
        Keyword Args:
            M (float):
                Set molar mass.
            rho (float):
                Set density.
            symbol (str):
                Short symbol.

        Returns:
            Substance instance.
        """
        return cls(name, constituents, mode="atomic", **kwargs)

    @classmethod
    def from_weight(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing weight fractions of constituents.

        Args:
            name:
                Descriptive name.
            constituents:
                Dictionary that maps a constituent of the substance to its
                weight fraction. Values are normalsied and don't need to add up
                to unity.
            **kwargs:
                Keyword arguments to override values.
        
        Keyword Args:
            M (float):
                Set molar mass.
            rho (float):
                Set density.
            symbol (str):
                Short symbol.
                
        Returns:
            Substance instance.
        """
        return cls(name, constituents, mode="weight", **kwargs)

    @classmethod
    def from_volume(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing volume fractions of constituents.
        
        Args:
            name:
                Descriptive name.
            constituents:
                Dictionary that maps a constituent of the substance to its
                volume fraction. Values are normalsied and don't need to add up
                to unity.
            **kwargs:
                Keyword arguments to override values.
        
        Keyword Args:
            M (float):
                Set molar mass.
            rho (float):
                Set density.
            symbol (str):
                Short symbol.
                
        Returns:
            Substance instance.
        """
        return cls(name, constituents, mode="volume", **kwargs)


    # ########
    # Properties
    # ########

    @property
    def name(self):
        """Given name."""
        return self._name

    @property
    def constituents(self):
        """Dictionary of constituents and their abundance (atomic (mole) fraction)."""
        return self._constituents

    @property
    def M(self):
        """Molar mass [g mol^-1]."""
        return self._M
    
    @property
    def rho(self):
        """Density [g cm^-3]."""
        return self._rho

    @property
    def symbol(self):
        """Symbol."""
        return self._symbol

    @property
    def V_m(self):
        """Molar volume [cm^3 mol^-1]."""
        return self._calc_V_m()
    
    @property
    def n(self):
        """Number density [cm^-3]."""
        return self._calc_n()


    # ########
    # Quantity Calculation
    # ########

    def _calc_M(self) -> float:
        r"""Calculates average molar mass.
        
        The molar masses of all constituents are weighted by their atomic
        fraction and summed up:
            $$\overline{M} = \sum_i \left( x_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """

        if all(constituent.M > 0 for constituent in self._constituents.keys()):
            return sum(x_i*constituent.M for constituent, x_i in self._constituents.items())
        else:
            return 0.0

    def _calc_V_m(self) -> float:
        r"""Calculates molar volume.

        Molar mass is divided by density:
            $$V_m = \frac{M}{\rho}$$
        Will return zero if calculation is not possible.
        """

        if self._M != 0 and self._rho != 0:
            return self._M / self._rho
        else:
            return 0.0
        
    def _calc_n(self) -> float:
        r"""Calculates number density.

        Density is normalised by the mass of a single atom or molecule:
            $$n = \frac{N_{\mathrm{A}}}{M} \rho$$
        Will return zero if calculation is not possible.
        """

        if self._M != 0 and self._rho != 0:
            return N_A / self._M * self._rho
        else:
            return 0.0

    
    # ########
    # Conversion
    # ########

    def get_constituents_in_wt(self) -> dict[Constituent, float]:
        """Returns constituent dictionary with weight fractions."""
        
        at_fracs = [x_i for x_i in self._constituents.values()]
        molar_masses = [constituent.M for constituent in self._constituents.keys()]

        wt_fracs = at_to_wt(at_fracs, molar_masses)
        return {constituent: w_i for constituent, w_i in zip(self._constituents.keys(), wt_fracs)}
   
    def get_constituents_in_vol(self) -> dict[Constituent, float]:
        """Returns constituent dictionary with volume fractions."""
        
        at_fracs = [x_i for x_i in self._constituents.values()]
        molar_volumes = [constituent.V_m for constituent in self._constituents.keys()]

        vol_fracs = at_to_vol(at_fracs, molar_volumes)
        return {constituent: phi_i for constituent, phi_i in zip(self._constituents.keys(), vol_fracs)}
        

    # ########
    # Isotope Collection
    # ########

    def _append_isotopes(
            self, dict_list: defaultdict[Isotope, list[float]], 
            by_weight: bool = False, f_p: float = 1.0, use_natural: bool = False
        ) -> defaultdict[Isotope, list[float]]:
        """Appends all isotopes with their desired fraction to given dictionary.
        
        Method is called upon each constituent, until `Isotope`s are extracted 
        from `Element`s. The fraction of the parent is multiplied onto the
        fraction of the constituents. Atomic and weight fractions are possible
        to be fetched. The `use_natural` flag will fetch a surrogate isotope 
        with appropriate mass, if the `Element` is natural.

        Args:
            dict_list:
                Container that collects all isotopes. Gets passed downwards.
            by_weight:
                Flag to fetch weight fractions of constituents.
            f_p:
                Parent fraction, that is multiplied onto constituent fractions.
            use_natural:
                Flag to use fraction of element, if it is natural.
        
        Returns:
            Dictionary that maps occuring isotopes to list of their fractions
        """
        
        if not by_weight:
            constituents = self._constituents
        else:
            constituents = self.get_constituents_in_wt()        

        for constituent, f_i in constituents.items():
            constituent._append_isotopes(dict_list, by_weight, f_p*f_i, use_natural)

        return dict_list
 
    def get_isotopes(
            self, mode: Literal["atomic", "weight"] = "atomic", 
            use_natural: bool = False
        ) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed desired fraction.
        
        Args:
            mode:
                Wether 'atomic' or 'weight' fractions are to be fetched.
            use_natural:
                Flag to use fraction of element, if it is natural.
        
        Returns:
            Dictionary that maps occuring isotopes to their fraction.
        """
        
        if mode in {"atomic", "at", "mole", "mol"}:
            gathered_isotopes = self._append_isotopes(defaultdict(list), by_weight=False, use_natural=use_natural)
        elif mode in {"weight", "wt"}:
            gathered_isotopes = self._append_isotopes(defaultdict(list), by_weight=True, use_natural=use_natural)
        else:
            raise ValueError(f"Mode \"{mode}\" not supported for gathering isotopes.")
        
        return {isotope: sum(fracs) for isotope, fracs in sorted(gathered_isotopes.items())}
        

    # ########
    # Functions
    # ########

    @classmethod
    def instance_is_allowed(cls, instance: Any) -> bool:
        """Returns, if given instane is of an allowed class (or subclass)."""
        return isinstance(instance, cls._get_allowed_classes())
    
    @classmethod
    def type_is_allowed(cls, type: type) -> bool:
        """Returns, if given type is an allowed class."""
        return all(type is allowed for allowed in cls._get_allowed_classes())


    # ########
    # Tree
    # ########        

    def make_node(
            self, atomic: bool = True, weight: bool = False, volume: bool = False, *,
            scale: bool = True, align_isotopes: bool = True
        ) -> Node:
        """Creates a hierarchical node structure with instance as the root.
        
        Args:
            atomic:
                Get atomic (mole) fraction for each node.
            weight:
                Get weight fraction for each node.
            volume:
                Get volume fraction for each node.
            scale:
                Flag to scale each constituents fraction by its parent fraction.
                If scaled, constituents of each parent add up to unity.
            align_isotopes:
                Flag to force all isotopes at maximum depth.
        
        Returns:
            Node structure with instance as root.
        """

        def add_constituents(parent_node: Node, x_p: float = 1.0, w_p: float = 1.0, phi_p: float = 1.0):

            x_i, w_i, phi_i = 0.0, 0.0, 0.0

            substance: Substance = parent_node.content
            constituents = list(substance.constituents.keys())

            # decide for fraction to be used
            if atomic:
                at_fracs = list(substance._constituents.values())
            if weight:
                wt_fracs = list(substance.get_constituents_in_wt().values())
            if volume:
                vol_fracs = list(substance.get_constituents_in_vol().values())

            for i, constituent in enumerate(constituents):
                
                # create data dictionary
                constituent_data = {}
                if atomic:
                    x_i = at_fracs[i] * x_p if scale else at_fracs[i]
                    constituent_data["x"] = x_i
                if weight:
                    w_i = wt_fracs[i] * w_p if scale else wt_fracs[i]
                    constituent_data["w"] = w_i
                if volume:
                    phi_i = vol_fracs[i] * phi_p if scale else vol_fracs[i]
                    constituent_data["phi"] = phi_i
                if constituent.M:
                    constituent_data["M"] = constituent.M
                try:
                    if constituent.rho:
                        constituent_data["rho"] = constituent.rho
                except AttributeError as ex:
                    pass

                # create node of constituent
                node = Node(label=str(constituent), content=constituent, parent=parent_node, data=constituent_data)

                # create child node for constituents of constituents (if applicable)
                if isinstance(constituent, Isotope):
                    if align_isotopes:
                        node.align_right()
                else:
                    add_constituents(parent_node=node, x_p=x_i, w_p=w_i, phi_p=phi_i)

        # create data dictionary
        root_data = {}
        if self._M:
            root_data["M"] = self._M
        if self._rho:
            root_data["rho"] = self._rho

        root = Node(label=str(self), content=self, data=root_data)
        add_constituents(parent_node=root)

        return root

    def print_tree(
            self, atomic: bool = True, weight: bool = False, volume: bool = False, *,
            scale: bool = True, align_isotopes: bool = True, 
            char_set: char_sets = "box_drawings_light"
        ) -> None:
        """Prints the hierarchical tree structure.
        
        Args:
            atomic:
                Get atomic (mole) fraction for each node.
            weight:
                Get weight fraction for each node.
            volume:
                Get volume fraction for each node.
            scale:
                Flag to scale each constituents fraction by its parent fraction.
                If scaled, constituents of each parent add up to unity.
            align_isotopes:
                Flag to align all isotopes in one column.
            char_set:
                Character set that is used to print lines in the tree.
        """
        self.make_node(atomic, weight, volume,
                       scale=scale, align_isotopes=align_isotopes).print_tree(char_set=char_set)


    # ########
    # Print
    # ########


    # ########
    # Operators
    # ########

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self.__class__.__name__} \"{self._name}\""

    def __hash__(self):
        return hash((self.__class__, self._name))
    
    def __eq__(self, other):
        if type(self) is type(other):
            return self._name == other._name
        else:
            return NotImplemented