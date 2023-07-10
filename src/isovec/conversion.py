
from typing import Any

def wt_to_at(constituents: dict[Any, float]) -> dict[Any, float]:
    """Converts weight fractions from dictionary to atomic fractions."""

    try:
        # calculate (constant) denominator for conversion
        denominator = sum([wt_frac / constituent.atomic_wt for constituent, wt_frac in constituents.items()])

        # convert and overwrite to atomic fraction
        conv_constituents: dict[Any, float] = {}
        for constituent, wt_frac in constituents.items():
            conv_constituents[constituent] = (wt_frac/constituent.atomic_wt) / denominator # now atomic fraction

        return conv_constituents

    except:
        raise TypeError(f"One of the constituents does not have an atomic weight.")

def at_to_wt(constituents: dict[Any, float]) -> dict[Any, float]:
    """Converts atomic fractions from dictionary to weight fractions."""

    try:
        # calculate (constant) denominator for conversion
        denominator = sum([at_frac * constituent.atomic_wt for constituent, at_frac in constituents.items()])

        # convert and overwrite to weight fraction
        conv_constituents: dict[Any, float] = {}
        for constituent, at_frac in constituents.items():
            conv_constituents[constituent] = (at_frac * constituent.atomic_wt) / denominator # now weight fraction

        return conv_constituents

    except:
        raise TypeError(f"One of the constituents does not have an atomic weight.")


def percent(value: float):
    """Converts value from percent."""
    return value*1e-2
perc = percent # function alias
pc   = percent # function alias

def permille(value: float):
    """Converts value from per mille."""
    return value*1e-3
pm = permille # function alias

def permyriad(value: float):
    """Converts value from per myriad."""
    return value*1e-4
bp = permyriad # function alias

def percentmille(value: float):
    """Converts value from per cent mille."""
    return value*1e-5
pcm = percentmille # function alias

def ppm(value: float):
    """Converts value from parts per million."""
    return value*1e-6

def ppb(value: float):
    """Converts value from parts per billion."""
    return value*1e-9

def ppt(value: float):
    """Converts value from parts per trillion."""
    return value*1e-12

def ppq(value: float):
    """Converts value from parts per quadrillion."""
    return value*1e-15