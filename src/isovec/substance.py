"""Class for Substance.

Substance class serves as the (abstract) base class for `Element`, `Molecule` and
`Mixture`.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, TypeAlias, Union, Literal, Iterable
from abc import ABCMeta, abstractmethod

from .constants import N_A
from .conversion import at_to_wt, wt_to_at, vol_to_at, at_to_vol
from .isotope import Isotope
from .node import Node, char_sets


Constituent: TypeAlias = Union["Substance", Isotope]

class Substance(metaclass=ABCMeta):
    """Abstract base class for all types of substances.

    Each substance has a name and is a composition of constituents, each
    accounting for a certain fraction. Internally, this is saved as atomic (or
    mole) fraction. Every substance has a molar mass, that can be calculated
    from its composition, since the basis is made of isotopes, that have their 
    mass implemented. Density can generally not be calculated but instead must
    be stated explicitly. Optionally, a shorter name can be given in the form
    of a symbol.
    """
    
    @classmethod
    @abstractmethod
    def _get_allowed_constituents(cls):
        """Returns a tuple of allowed classes for constituents."""
        return NotImplementedError
    
    _NORMALISE = True  # normalisation of atomic fractions
    _RIGHT_ALIGN_PREF = None  # right alignment preference of substance in tree prints

    @abstractmethod
    def __init__(self, name: str, composition: dict[Constituent, float], mode: str = "_legacy", **kwargs) -> None:
        """Constructor of substance.
        
        Args:
            name:
                Descriptive name.
            composition:
                Dictionary that maps a constituent of the substance to its
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
            not allowed as constituent for substance.
        """

        self._name = name                             # name of the substance
        self._composition: dict[Constituent, float]   # {constituent: atomic (mole) fraction}
        self._M: float                                # molar mass [g mol^-1]
        self._rho: float                              # density [g cm^-3]
        self._symbol: str                             # symbol of the substance

        # ensure input constituents are of allowed classes
        for constituent in composition.keys():
            if not self.instance_is_allowed(constituent):
                type_names = ", ".join(_type.__name__ for _type in self._get_allowed_constituents())
                raise ValueError(f"Could not create {self.__class__.__name__} object with type {constituent.__class__.__name__} as constituent.\n"
                                 + f"Valid classes for {self.__class__.__name__} constituents: {type_names}.")

        # ensure atomic fraction of input composition
        if mode == "_legacy":  # as done before 1.1.0
            composition = self._inp_composition_legacy(composition)
        elif mode in {"atomic", "at", "mole", "mol"}:  # no conversion, only assure positive values
            composition = self._inp_composition_atomic(composition)
        elif mode in {"weight", "wt"}:  # convert from weight fractions
            composition = self._inp_composition_weight(composition)
        elif mode in {"volume", "vol"}:  # convert from volume fractions
            composition = self._inp_composition_volume(composition)
        elif mode == "_skip":  # no action
            composition = composition
        else:
            raise ValueError(f"Unknown constructor mode \"{mode}\".")

        # populate composition dictionary
        x_sum = sum(composition.values())
        if self._NORMALISE:  # normalise fractions
            self._composition = {constituent: (x_i / x_sum) for constituent, x_i in composition.items() if x_i > 0}
        else:  # no normalisation
            self._composition = {constituent: x_i for constituent, x_i in composition.items() if x_i > 0}

        # get molar mass and density from kwargs or calculate it
        self._M = kwargs.get("M", self._calc_M())
        self._rho = kwargs.get("rho", 0.0)
        self._symbol = kwargs.get("symbol", "")
    
    @classmethod
    def _inp_composition_atomic(cls, inp_composition: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given atomic (mole) fractions."""
        return {constituent: abs(x_i) for constituent, x_i in inp_composition.items()}
    
    @classmethod
    def _inp_composition_weight(cls, inp_composition: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given weight fractions."""
        
        wt_fracs = [abs(w_i) for w_i in inp_composition.values()]
        molar_masses = [constituent.M for constituent in inp_composition.keys()]

        at_fracs = wt_to_at(wt_fracs, molar_masses)
        return {constituent: x_i for constituent, x_i in zip(inp_composition.keys(), at_fracs)}
    
    @classmethod
    def _inp_composition_volume(cls, inp_composition: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions for given volume fractions."""
        
        vol_fracs = [abs(phi_i) for phi_i in inp_composition.values()]
        molar_volumes = [constituent.V_m for constituent in inp_composition.keys()]

        at_fracs = vol_to_at(vol_fracs, molar_volumes)
        return {constituent: x_i for constituent, x_i in zip(inp_composition.keys(), at_fracs)}

    @classmethod
    def _inp_composition_legacy(cls, inp_composition: dict[Constituent, float]) -> dict[Constituent, float]:
        """Returns constituent dictionary with atomic (mole) fractions as done before 1.1.0.
        
        Legacy method to maintain backwards compatibility.
        """
        
        if not all(frac > 0 for frac in inp_composition.values()):  # either all negative or mixed
            if all(frac < 0 for frac in inp_composition.values()):  # all negative -> weight fractions given, need to be converted
                return cls._inp_composition_weight(inp_composition)
            else:  # mixed, not allowed
                raise ValueError(f"Could not create {cls.__name__}: Mixing of atomic and weight fractions is not allowed.")
        else:  # all positive -> atomic fractions given, no action needed
            return inp_composition


    # ########
    # Factory Constructor
    # ########

    @classmethod
    def from_atomic(cls, name: str, composition: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing atomic (mole) fractions of constituents.

        Args:
            name:
                Descriptive name.
            composition:
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
        return cls(name, composition, mode="atomic", **kwargs)

    @classmethod
    def from_weight(cls, name: str, composition: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing weight fractions of constituents.

        Args:
            name:
                Descriptive name.
            composition:
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
        return cls(name, composition, mode="weight", **kwargs)

    @classmethod
    def from_volume(cls, name: str, composition: dict[Constituent, float], **kwargs) -> Substance:
        """Constructor for providing volume fractions of constituents.
        
        Args:
            name:
                Descriptive name.
            composition:
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
        return cls(name, composition, mode="volume", **kwargs)


    # ########
    # Properties
    # ########

    @property
    def name(self):
        """Given name."""
        return self._name

    @property
    def composition(self):
        """Dictionary of constituents and their atomic (mole) fraction."""
        return self._composition

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

        if all(constituent.M > 0 for constituent in self._composition.keys()):
            return sum(x_i*constituent.M for constituent, x_i in self._composition.items())
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

        Avogadro constant divided by molar volume (density is normalised by the
        mass of a single atom or molecule):
            $$n = \frac{N_{\mathrm{A}}}{V_m} = \frac{N_{\mathrm{A}}}{M} \rho$$
        Will return zero if calculation is not possible.
        """

        if self._M != 0 and self._rho != 0:
            return N_A / self._M * self._rho
        else:
            return 0.0

    
    # ########
    # Conversion
    # ########

    def get_composition_in_wt(self) -> dict[Constituent, float]:
        """Returns constituents with their weight fractions."""
        
        at_fracs = [x_i for x_i in self._composition.values()]
        molar_masses = [constituent.M for constituent in self._composition.keys()]

        wt_fracs = at_to_wt(at_fracs, molar_masses)
        return {constituent: w_i for constituent, w_i in zip(self._composition.keys(), wt_fracs)}
   
    def get_composition_in_vol(self) -> dict[Constituent, float]:
        """Returns constituents with their volume fractions."""
        
        at_fracs = [x_i for x_i in self._composition.values()]
        molar_volumes = [constituent.V_m for constituent in self._composition.keys()]

        vol_fracs = at_to_vol(at_fracs, molar_volumes)
        return {constituent: phi_i for constituent, phi_i in zip(self._composition.keys(), vol_fracs)}
        

    # ########
    # Collection
    # ########
    
    def _append_elements(
            self, element_list: dict[int, tuple[Substance, float]],
            by_weight: bool = False, f_p: float = 1.0
        ) -> dict[int, tuple[Substance, float]]:
        """Collects all contained elements.
        
        Method is called upon each constituent, until `Element`s are extracted.
        The fraction of the parent is multiplied onto the
        fraction of the constituent. Atomic and weight fractions are possible
        to be fetched. The element, its parent and the fraction of the element
        in the parent are used to generate a (unique) id. Fractions need to be
        normalised.

        Args:
            element_list:
                Container that collects all elements. Gets passed downwards.
                Index "-1" is reserved for counting.
            by_weight:
                Flag to fetch weight fractions of constituents.
            f_p:
                Parent fraction, that is multiplied onto constituent fractions.
            parent:
                Parent object used for generating id.
        
        Returns:
            Dictionary that maps id to element with its fraction
        """

        element_list[-1] = element_list[-1] + 1  # increase counter

        if not by_weight:
            composition = self._composition
        else:
            composition = self.get_composition_in_wt()  
        
        for constituent, f_i in composition.items():
            constituent._append_elements(element_list, by_weight, f_p*f_i)

        return element_list
    
    def _elemental_composition(
            self, by_weight: bool = False
        ) -> dict[int, tuple[Substance, float]]:
        """Collects all contained elements with their normalised fraction.
        
        Args:
            by_weight:
                Flag to fetch weight fractions of constituents.
            
        Returns:
            Dictionary that maps id to element with its fraction
        """

        # get raw elemental composition
        gathered_elements = self._append_elements({-1: -1}, by_weight)
        items = gathered_elements.pop(-1)  # remove counter
        
        # get sum for normalisation
        _, fractions = list(map(list, zip(*gathered_elements.values())))
        norm_tmp = sum(fractions)
        
        return {ident: (element, fraction/norm_tmp) for ident, (element, fraction) in gathered_elements.items()}

    def get_elements(self, mode: Literal["atomic", "weight"] = "atomic"):
        """Returns dict of all contained elements with their summed fraction.
        
        Args:
            mode:
                Wether 'atomic' or 'weight' fractions are to be fetched.
        
        Returns:
            Dictionary that maps occuring elements to their fraction.
        """

        if mode in {"atomic", "at", "mole", "mol"}:
            gathered_elements = self._elemental_composition(by_weight=False)
        elif mode in {"weight", "wt"}:
            gathered_elements = self._elemental_composition(by_weight=True)
        else:
            raise ValueError(f"Mode \"{mode}\" not supported for gathering elements.")
        
        elements = defaultdict(list)
        for element, fraction in gathered_elements.values():
            elements[element].append(fraction)

        return {element: sum(fracs) for element, fracs in sorted(elements.items())}
    
    def _isotopic_composition(
            self, by_weight: bool = False,
            use_natural: bool | Iterable = False
        ) -> dict[int, tuple[Isotope, float]]:
        """Collects all contained isotopes with their normalised fraction.
        
        Args:
            by_weight:
                Flag to fetch weight fractions of constituents.
            
        Returns:
            Dictionary that maps id to isotope with its fraction
        """

        elemental_composition = self._elemental_composition(by_weight)
        isotopic_composition = {}

        def append_isotopes(id: int, element: Substance, fraction: float):
            if not by_weight:
                composition = element._composition
            else:
                composition = element.get_composition_in_wt()
            for j, (isotope, iso_fraction) in enumerate(composition.items(), start=1):
                isotopic_composition[id+j] = (isotope, fraction*iso_fraction)

        def append_surrogate(id: int, element: Substance, fraction: float):
            surrogate = element.surrogate_isotope()
            if surrogate:
                isotopic_composition[id] = (surrogate, fraction)
            else:
                append_isotopes(id, element, fraction)

        for id, (element, fraction) in elemental_composition.items():
            if use_natural:
                if isinstance(use_natural, Iterable):  # have to check if considered
                    if element in use_natural:
                        append_surrogate(id, element, fraction)
                    else:
                        append_isotopes(id, element, fraction)
                else:  # must be boolean true, use elemental composition
                    append_surrogate(id, element, fraction)
            else:
                append_isotopes(id, element, fraction)

        return isotopic_composition
    
    def get_isotopes(
            self, mode: Literal["atomic", "weight"] = "atomic", 
            use_natural: bool | Iterable = False
        ) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed fraction.
        
        Args:
            mode:
                Wether 'atomic' or 'weight' fractions are to be fetched.
            use_natural:
                Flag to use fraction of element, if it is natural.
                Alternatively, a collection of elements can be supplied, that
                shall be considered.
        
        Returns:
            Dictionary that maps occuring isotopes to their fraction.
        """
        
        if mode in {"atomic", "at", "mole", "mol"}:
            gathered_isotopes = self._isotopic_composition(by_weight=False, use_natural=use_natural)
        elif mode in {"weight", "wt"}:
            gathered_isotopes = self._isotopic_composition(by_weight=True, use_natural=use_natural)
        else:
            raise ValueError(f"Mode \"{mode}\" not supported for gathering isotopes.")

        isotopes = defaultdict(list)
        for isotope, fraction in gathered_isotopes.values():
            isotopes[isotope].append(fraction)

        return {isotope: sum(fracs) for isotope, fracs in sorted(isotopes.items())}

        
    # ########
    # Functions
    # ########

    @classmethod
    def instance_is_allowed(cls, instance: Any) -> bool:
        """Returns, if given instane is of an allowed class (or subclass)."""
        return isinstance(instance, cls._get_allowed_constituents())
    
    @classmethod
    def type_is_allowed(cls, dtype: type) -> bool:
        """Returns, if given type is an allowed class."""
        return all(dtype is allowed for allowed in cls._get_allowed_constituents())


    # ########
    # Tree
    # ########        

    def make_node(
            self, tree_mode: Literal["input", "composition"],
            atomic: bool = True, weight: bool = False, volume: bool = False
        ) -> Node:
        """Creates a hierarchical node structure with instance as the root.
        
        Args:
            atomic:
                Get atomic (mole) fraction for each node.
            weight:
                Get weight fraction for each node.
            volume:
                Get volume fraction for each node.
        
        Returns:
            Node structure with instance as root.
        """

        def add_constituents_input(parent_node: Node):

            nonlocal node_i
            substance: Substance = parent_node.content
            constituents = list(substance.composition.keys())

            # decide for fraction to be used
            if atomic:
                at_fracs = list(substance._composition.values())
            if weight:
                try:
                    wt_fracs = list(substance.get_composition_in_wt().values())
                except ValueError as ex:  # constituent has no molar mass
                    wt_fracs = None
            if volume:
                try:
                    vol_fracs = list(substance.get_composition_in_vol().values())
                except (ValueError, AttributeError) as ex:  # constituent has no density or is an isotope
                    vol_fracs = None


            for i, constituent in enumerate(constituents):
                
                node_i += 1

                # create data dictionary
                constituent_data = {}
                if atomic:
                    constituent_data["x"] = at_fracs[i]
                if weight and wt_fracs:
                    constituent_data["w"] = wt_fracs[i]
                if volume and vol_fracs:
                    constituent_data["phi"] = vol_fracs[i]
                if constituent.M:
                    constituent_data["M"] = constituent.M
                try:
                    if constituent.rho:
                        constituent_data["rho"] = constituent.rho
                except AttributeError as ex:
                    pass

                # create node of constituent
                node = Node(label=str(constituent), content=constituent, parent=parent_node, data=constituent_data, id=node_i)

                # create child node for constituents of constituent (if applicable)
                if isinstance(constituent, Isotope):
                    continue
                else:
                    add_constituents_input(parent_node=node)
            
        def add_constituents_composition(parent_node: Node):

            nonlocal node_i
            substance: Substance = parent_node.content
            constituents = list(substance.composition.keys())

            for i, constituent in enumerate(constituents):

                node_i += 1
                
                # create data dictionary
                constituent_data = {}
                if atomic:
                    try:
                        constituent_data["x"] = composition_atomic[node_i][1]
                    except KeyError:
                        pass
                if weight:
                    try:
                        constituent_data["w"] = composition_weight[node_i][1]
                    except KeyError:
                        pass
                if constituent.M:
                    constituent_data["M"] = constituent.M
                try:
                    if constituent.rho:
                        constituent_data["rho"] = constituent.rho
                except AttributeError as ex:
                    pass

                # create node of constituent
                node = Node(label=str(constituent), content=constituent, parent=parent_node, data=constituent_data, id=node_i)
 
                # create child node for constituents of constituent (if applicable)
                if isinstance(constituent, Isotope):
                    node.align_right(level=-1, label_size=6)
                else:
                    node.align_right(level=constituent._RIGHT_ALIGN_PREF)
                    add_constituents_composition(parent_node=node)

        # create data dictionary
        root_data = {}
        if self._M:
            root_data["M"] = self._M
        if self._rho:
            root_data["rho"] = self._rho

        # create root node and start recursive hierarchy construction
        node_i = 0
        root = Node(label=str(self), content=self, data=root_data, id=node_i)
        if tree_mode == "input":
            add_constituents_input(parent_node=root)
        elif tree_mode == "composition":
            # atomic composition
            if atomic:
                composition_atomic = self._elemental_composition(by_weight=False)
                composition_atomic.update(self._isotopic_composition(by_weight=False))
            else:
                composition_atomic = None
            # weight composition
            if weight:
                composition_weight = self._elemental_composition(by_weight=True)
                composition_weight.update(self._isotopic_composition(by_weight=True))
            else:
                composition_weight = None
            # recursive hierarchy construction
            add_constituents_composition(parent_node=root)

        return root
    
    def print_tree_input(
            self, atomic: bool = True, weight: bool = False, volume: bool = False, *,
            char_set: char_sets = "box_drawings_light", **kwargs
        ) -> None:
        """Prints the hierarchical tree structure.
        
        Args:
            atomic:
                Get atomic (mole) fraction for each node.
            weight:
                Get weight fraction for each node.
            volume:
                Get volume fraction for each node.
            char_set:
                Character set that is used to print lines in the tree.
            **kwargs:
                Arguments passed to the plotting routine of Node.

        Keyword Args:
            frac_fmt (str):
                Format string to be used for fractions.
            prop_fmt (str):
                Format string to be used for physical properties.
        """
        self.make_node(
            "input", atomic, weight, volume,
        ).print_tree(char_set=char_set, **kwargs)

    def print_tree_composition(
            self, atomic: bool = True, weight: bool = False, *,
            char_set: char_sets = "box_drawings_light", **kwargs
        ) -> None:
        """Prints the hierarchical tree structure.
        
        Args:
            atomic:
                Get atomic (mole) fraction for each node.
            weight:
                Get weight fraction for each node.
            char_set:
                Character set that is used to print lines in the tree.
            **kwargs:
                Arguments passed to the plotting routine of Node.

        Keyword Args:
            frac_fmt (str):
                Format string to be used for fractions.
            prop_fmt (str):
                Format string to be used for physical properties.
        """
        self.make_node(
            "composition", atomic, weight,
        ).print_tree(char_set=char_set, **kwargs)


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
        

    # ########
    # Debug
    # ########
    
    def _compare_converted_isotopes(self) -> dict[str, list[float]]:
        """Debug function to test consistency of fraction modes.
        
        Gets isotopes of substance via "atomic" and "weight" mode, then converts
        each case and compares the atomic and weight fractions from each case
        respectively. For correct behaviour, differences should approach zero.
        """

        # extract isotopes in atomic mode and convert to weight
        tmp = self.get_isotopes(mode="atomic")
        iso_with_at = tmp.keys()
        direct_at = list(tmp.values())
        conv_wt = at_to_wt(at_fracs=direct_at, molar_masses=[isotope.M for isotope in iso_with_at])

        # extract isotopes in weight mode and convert to atomic
        tmp = self.get_isotopes(mode="weight")
        iso_with_wt = tmp.keys()
        direct_wt = list(tmp.values())
        conv_at = wt_to_at(wt_fracs=direct_wt, molar_masses=[isotope.M for isotope in iso_with_wt])

        assert(iso_with_at == iso_with_wt)

        differences = defaultdict(list)

        # print for atomic percent
        print(f"Isotope |   direct atomic  | converted atomic | difference atomic (relative difference)")
        for i, isotope in enumerate(iso_with_at):
            dir = direct_at[i]
            conv = conv_at[i]
            dif = dir - conv
            dif_rel = dif / dir
            print(f"{isotope.name:>7} |  {dir:14.12f}  |  {conv:14.12f}  |  {dif: 12.9e} ({dif_rel: 12.9e})")
            differences["at"].append(dif)
            differences["rel_at"].append(dif_rel)

        print()

        # print for weight percent
        print(f"Isotope |   direct weight  | converted weight | difference weight (relative difference)")
        for i, isotope in enumerate(iso_with_wt):
            dir = direct_wt[i]
            conv = conv_wt[i]
            dif = dir - conv
            dif_rel = dif / dir
            print(f"{isotope.name:>7} |  {dir:14.12f}  |  {conv:14.12f}  |  {dif: 12.9e} ({dif_rel: 12.9e})")
            differences["wt"].append(dif)
            differences["rel_wt"].append(dif_rel)
        

        return differences
    