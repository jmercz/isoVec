
from __future__ import annotations
from collections import defaultdict
from typing import Any, TypeAlias, Union
from abc import ABCMeta, abstractmethod

from .conversion import at_to_wt, wt_to_at, vol_to_at, at_to_vol
from .isotope import Isotope


Constituent: TypeAlias = Union["Substance", Isotope]

class Substance(metaclass=ABCMeta):
    
    #_ALLOWED_CLASSES = (Constituent,)  # allowed classes as constituents
    @classmethod
    @abstractmethod
    def _GET_ALLOWED_CLASSES(cls):
        """Returns a tuple of allowed classes for constituents."""
        return NotImplementedError
    
    _NORMALISE = True  # normalisation of atomic fractions

    @abstractmethod
    def __init__(self, name: str, constituents: dict[Constituent, float], mode: str = "_legacy", **kwargs) -> None:    

        self._name = name                             # name of the substance
        self._constituents: dict[Constituent, float]  # {constituent: atomic (mole) fraction abundance}
        self._M: float                                # molar mass [g mol^-1]
        self._rho: float                              # density [g cm^-3]

        # ensure input constituents are of allowed classes
        for constituent in constituents.keys():
            if not self.instance_is_allowed(constituent):
                type_names = ", ".join(t.__name__ for t in self._ALLOWED_CLASSES)
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
                cls._inp_constituents_weight(inp_constituents)
            else:  # mixed, not allowed
                raise ValueError(f"Could not create {cls.__name__}: Mixing of atomic and weight fractions is not allowed.")
        else:  # all positive -> atomic fractions given, no action needed
            return inp_constituents


    # ########
    # Factory Constructor
    # ########

    @classmethod
    def from_atomic(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their atomic (mole) fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="atomic", **kwargs)

    @classmethod
    def from_weight(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their weight fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="weight", **kwargs)

    @classmethod
    def from_volume(cls, name: str, constituents: dict[Constituent, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their volume fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="volume", **kwargs)


    # ########
    # Properties
    # ########

    @property
    def name(self):
        """Name of the substance."""
        return self._name

    @property
    def constituents(self):
        """Dictionary of constituents and their abundance (atomic (mole) fraction)."""
        return self._constituents

    @property
    def M(self):
        """Molar mass [g mol^-1] of the substance."""
        return self._M
    
    @property
    def rho(self):
        """Density [g cm^-3] of the substance."""
        return self._rho

    @property
    def V_m(self):
        """Molar volume [cm^3 mol^-1] of the substance."""
        return self._calc_V_m()


    # ########
    # Quantity Calculation
    # ########

    def _calc_M(self) -> float:
        r"""Calculates average molar mass of the substance.
        
        The molar masses of all constituents are weighted by their atomic fraction and summed up:
            $$\overline{M} = \sum_i \left( x_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """

        if all(constituent.M > 0 for constituent in self._constituents.keys()):
            return sum(x_i*constituent.M for constituent, x_i in self._constituents.items())
        else:
            return 0.0

    def _calc_rho(self) -> float:
        r"""Calculates average density of the mixture.
        
        The densities of all constituents are weighted by their weight fraction, summed up and inversed:
            $$\overline{\rho} = \left( \sum_i \frac{w_i}{\rho_i} \right)^{-1}$$
        Will return zero if calculation is not possible.
        """
        return 0.0
        if all(constituent.has_M() for constituent in self._constituents.keys()):
            wt_constituents = self.convert_to_wt()
        else:
            return 0.0

        if all(constituent.has_rho() for constituent in wt_constituents.keys()):
            summed = sum(w_i / constituent.rho for constituent, w_i in wt_constituents.items())
            return summed**-1
        else:
            return 0.0

    def _calc_V_m(self) -> float:
        r"""Calculates molar volume of the substance.
        Molar mass is divided by density:
            $$V_m = \frac{M}{\rho}$$
        Will return zero if calculation is not possible.
        """
        if self._M != 0 and self._rho != 0:
            return self._M / self._rho
        else:
            return 0.0

    
    # ########
    # Conversion
    # ########

    def get_constituents_in_wt(self) -> dict[Constituent, float]:
        """Returns constituent dictionary of substance with weight fractions."""
        
        at_fracs = [x_i for x_i in self._constituents.values()]
        molar_masses = [constituent.M for constituent in self._constituents.keys()]

        wt_fracs = at_to_wt(at_fracs, molar_masses)
        return {constituent: w_i for constituent, w_i in zip(self._constituents.keys(), wt_fracs)}
   
    def get_constituents_in_vol(self) -> dict[Constituent, float]:
        """Returns constituent dictionary of substance with volume fractions."""
        
        at_fracs = [x_i for x_i in self._constituents.values()]
        molar_volumes = [constituent.V_m for constituent in self._constituents.keys()]

        vol_fracs = at_to_vol(at_fracs, molar_volumes)
        return {constituent: phi_i for constituent, phi_i in zip(self._constituents.keys(), vol_fracs)}
        

    # ########
    # Isotope Collection
    # ########

    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]], x_p: float = 1.0) -> defaultdict[Isotope, list[float]]:
        """Appends all isotopes with their atomic (mole) fraction to given dictionary."""
        for constituent, x_i in self._constituents.items():
            constituent._append_isotopes(dict_list, x_p*x_i)
        return dict_list

    def get_isotopes(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic (mole) fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes(defaultdict(list)).items())}


    # ########
    # Functions
    # ########

    @classmethod
    def instance_is_allowed(cls, instance: Any) -> bool:
        """Returns, if given instane is of an allowed class (or subclass)."""
        #return isinstance(instance, cls._ALLOWED_CLASSES)
        return isinstance(instance, cls._GET_ALLOWED_CLASSES())
    
    @classmethod
    def type_is_allowed(cls, type: type) -> bool:
        """Returns, if given type is an allowed class."""
        #return all(type is allowed for allowed in cls._ALLOWED_CLASSES)
        return all(type is allowed for allowed in cls._GET_ALLOWED_CLASSES())


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