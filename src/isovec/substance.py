
from __future__ import annotations
from typing import Any
from abc import ABCMeta, abstractmethod
from collections import defaultdict

from .conversion import at_to_wt, wt_to_at, vol_to_at, at_to_vol
from .isotope import Isotope

class Substance(metaclass=ABCMeta):

    #@abstractmethod
    def __init__(self, name: str, constituents: dict[Any, float], mode: str = "_legacy", **kwargs) -> None:
        
        def _treat_constituents(inp_constituents: dict[Any, float], mode: str) -> dict[Any, float]:
            if mode == "_legacy":  # as done before 1.1.0
                return self._legacy_constituents(inp_constituents)
            elif mode in {"atomic", "at", "mole", "mol"}:  # no conversion, only assure absolute magnitude of values
                return {constituent: abs(x_i) for constituent, x_i in inp_constituents.items()}
            elif mode in {"weight", "wt"}:  # convert from weight fractions
                return self._convert_from_wt_from(inp_constituents)
            elif mode in {"volume", "vol"}:  # convert from volume fractions
                return self._convert_from_vol_from(inp_constituents)
            elif mode == "_skip":  # no action
                return inp_constituents
            else:
                raise ValueError(f"Unknown constructor mode \"{mode}\".")

        self._name = name                                 # name of the substance
        self._constituents: dict[Any, float] = {}         # {constituent: atomic (mole) fraction abundance}
        self._M: float = kwargs.get("M", self._calc_M())  # molar mass
        self._rho: float = kwargs.get("rho", 0.0)         # density

        # ensure atomic fraction
        constituents = _treat_constituents(constituents, mode)

        # populate dictionary
        x_sum = sum(constituents.values())
        if kwargs.get("norm", True):  # normalise fractions
            self._constituents = {constituent: (x_i / x_sum) for constituent, x_i in constituents.items() if x_i > 0}
        else:
            self._constituents = {constituent: x_i for constituent, x_i in constituents.items() if x_i > 0}

    def _legacy_constituents(self, inp_constituents: dict[Any, float]) -> dict[Any, float]:
        """Sets the constituents dictionary as done before 1.1.0.
        
        Legacy method to maintain backwards compatibility.
        """
        
        if not all(frac > 0 for frac in inp_constituents.values()):
            # either all negative or mixed
            if all(frac < 0 for frac in inp_constituents.values()):
                # given in terms of weight fraction, needs to be converted
                self._convert_from_wt_from({constituent: abs(w_i) for constituent, w_i in inp_constituents.items()})
            else:
                raise ValueError(f"Could not create {__class__.__name__} \"{self._name}\": Mixing of atomic and weight fractions is not allowed.")
        else:
            # given in terms of atomic fraction, no action needed
            return inp_constituents


    # ########
    # Factory Constructor
    # ########

    @classmethod
    def from_atomic(cls, name: str, constituents: dict[Any, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their atomic (mole) fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="atomic", **kwargs)

    @classmethod
    def from_weight(cls, name: str, constituents: dict[Any, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their weight fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="weight", **kwargs)

    @classmethod
    def from_volume(cls, name: str, constituents: dict[Any, float], **kwargs) -> Substance:
        """Returns substance by providing constituents with their volume fraction.
        
        Signs of the fractions are ignored.
        """
        return cls(name, constituents, mode="volume", **kwargs)


    # ########
    # Getter
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
    def V_m(self):
        """Molar volume [m^3 mol^-1] of the substance."""
        return self.calc_V_m()


    # ########
    # Quantity Calculation
    # ########

    def _calc_M(self) -> float:
        """Calculates average molar mass of the substance.
        
        The molar masses of all constituents are weighted by their atomic fraction and summed up:
            $$\overline{M} = \sum_i \left( x_i \cdot M_i \right)$$
        Will return zero if calculation is not possible.
        """

        if all(constituent.has_M() for constituent in self._constituents.keys()):
            return sum(x_i*constituent._M for constituent, x_i in self._constituents.items())
        else:
            return 0.0

    def _calc_rho(self) -> float:
        """Calculates average density of the mixture.
        
        The densities of all constituents are weighted by their weight fraction, summed up and inversed:
            $$\overline{\rho} = \left( \sum_i \frac{w_i}{\rho_i} \right)^{-1}$$
        Will return zero if calculation is not possible.
        """

        if all(constituent.has_M() for constituent in self._constituents.keys()):
            wt_constituents = self.convert_to_wt()
        else:
            return 0.0

        if all(constituent.has_rho() for constituent in wt_constituents.keys()):
            summed = sum(w_i / constituent.rho for constituent, w_i in wt_constituents.items())
            return summed**-1
        else:
            return 0.0

    def calc_V_m(self) -> float:
        """Calculates molar volume of the substance."""
        if self._M != 0 and self._rho != 0:
            return self._M / self._rho
        else:
            return 0.0


    # ########
    # Quantity Validation
    # ########

    def has_M(self) -> bool:
        """Returns validity of molar mass value."""
        
        if self._M > 0.0:
            return True
        else:
            return False

    def has_rho(self) -> bool:
        """Returns validity of density value."""
        
        if self._rho > 0.0:
            return True
        else:
            return False

    def has_V_m(self) -> bool:
        """Returns validity of molar volume value."""
        
        if (self._M > 0.0) and (self._rho > 0):
            return True
        else:
            return False

    
    # ########
    # Conversion
    # ########

    @staticmethod
    def _convert_from_wt_from(constituents: dict[Any, float]) -> dict[Any, float]:
        """Returns constituent dictionary with atomic fractions for supplied weight fractions."""

        wt_fracs = [abs(w_i) for w_i in constituents.values()]
        molar_masses = [constituent.M for constituent in constituents.keys()]

        at_fracs = wt_to_at(wt_fracs, molar_masses)
        return {constituent: x_i for constituent, x_i in zip(constituents.keys(), at_fracs)}

    @staticmethod
    def _convert_to_wt_from(constituents: dict[Any, float]) -> dict[Any, float]:
        """Returns constituent dictionary with weight fractions."""

        at_fracs = [x_i for x_i in constituents.values()]
        molar_masses = [constituent.M for constituent in constituents.keys()]

        wt_fracs = at_to_wt(at_fracs, molar_masses)
        return {constituent: w_i for constituent, w_i in zip(constituents.keys(), wt_fracs)}

    def convert_to_wt(self) -> dict[Any, float]:
        """Returns constituent dictionary of substance with weight fractions."""
        return self._convert_to_wt_from(self._constituents)
   
    
    @staticmethod
    def _convert_from_vol_from(constituents: dict[Any, float]) -> dict[Any, float]:
        """Returns constituent dictionary with atomic fractions for supplied volume fractions."""

        vol_fracs = [abs(phi_i) for phi_i in constituents.values()]
        molar_volumes = [constituent.V_m for constituent in constituents.keys()]

        at_fracs = vol_to_at(vol_fracs, molar_volumes)
        return {constituent: x_i for constituent, x_i in zip(constituents.keys(), at_fracs)}

    @staticmethod
    def _convert_to_vol_from(constituents: dict[Any, float]) -> dict[Any, float]:
        """Returns constituent dictionary with volume fractions."""

        at_fracs = [x_i for x_i in constituents.values()]
        molar_volumes = [constituent.V_m for constituent in constituents.keys()]

        vol_fracs = at_to_vol(at_fracs, molar_volumes)
        return {constituent: phi_i for constituent, phi_i in zip(constituents.keys(), vol_fracs)}

    def convert_to_vol(self) -> dict[Any, float]:
        """Returns constituent dictionary of substance with volume fractions."""
        return self._convert_to_vol_from(self._constituents)
        
    # ########
    # Isotope Collection
    # ########

    def _append_isotopes(self, dict_list: defaultdict[Isotope, list[float]] = None, par_at_frac: float = 1.0) -> defaultdict[Isotope, list[float]]:
        """Appends all isotopes with their atomic (mole) fraction to given dictionary."""

        if dict_list is None:
            dict_list = defaultdict(list)  # new defaultdict should be the default value for dict_list, but those are mutable and stay the same object over multiple function calls (clutter up)
                                           # thanks to Don Cross' article: https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422

        for constituent, at_frac in self._constituents.items():
            dict_list = constituent._append_isotopes(dict_list, par_at_frac*at_frac)

        return dict_list

    def get_isotopes(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic (mole) fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes().items())}

    def _append_isotopes2(self, dict_list: defaultdict[Isotope, list[float]], x_p: float = 1.0) -> None:
        """Appends all isotopes with their atomic (mole) fraction to given dictionary."""
        for constituent, x_i in self._constituents.items():
            constituent._append_isotopes2(dict_list, x_p*x_i)

    def get_isotopes2(self) -> dict[Isotope, float]:
        """Returns dict of all contained isotopes with their summed atomic (mole) fraction."""
        return {isotope: sum(at_fracs) for isotope, at_fracs in sorted(self._append_isotopes(defaultdict(list)).items())}

    # ########
    # Print
    # ########

    def string(self) -> str:
        """Returns substrance name."""
        return self._name


    # ########
    # Operators
    # ########

    def __str__(self):
        return self.string()

    def __repr__(self):
        return self.string()
