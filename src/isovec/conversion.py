
def WtToAt(constituents: dict[any, float]) -> dict[any, float]:
    """
    Converts weight fraction from dictionary to atomic fraction
    """

    try:
        # calculate (constant) denominator for conversion
        denominator = sum([wtFraction / constituent.atomicWeight for constituent, wtFraction in constituents.items()])

        # convert and overwrite to atomic fraction
        conv_constituents: dict[any, float] = {}
        for constituent, wtFraction in constituents.items():
            conv_constituents[constituent] = (wtFraction/constituent.atomicWeight) / denominator # now atomic fraction

        return conv_constituents

    except:
        raise TypeError(f"One of the constituents does not have an atomic weight.")

def AtToWt(constituents: dict[any, float]) -> dict[any, float]:
    """
    Converts atomic fraction from dictionary to weight fraction 
    """

    try:
        # calculate (constant) denominator for conversion
        denominator = sum([atFraction * constituent.atomicWeight for constituent, atFraction in constituents.items()])

        # convert and overwrite to weight fraction
        conv_constituents: dict[any, float] = {}
        for constituent, atFraction in constituents.items():
            conv_constituents[constituent] = (atFraction * constituent.atomicWeight) / denominator # now weight fraction

        return conv_constituents

    except:
        raise TypeError(f"One of the constituents does not have an atomic weight.")

def percent(value: float):
    """ Converts value from percent """
    return value*1e-2
perc = percent # function alias
pc   = percent # function alias

def permille(value: float):
    """ Converts value from per mille """
    return value*1e-3
pm = permille # function alias

def permyriad(value: float):
    """ Converts value from per myriad """
    return value*1e-4
bp = permyriad # function alias

def percentmille(value: float):
    """ Converts value from per cent mille """
    return value*1e-5
pcm = percentmille # function alias

def ppm(value: float):
    """ Converts value from parts per million """
    return value*1e-6

def ppb(value: float):
    """ Converts value from parts per billion  """
    return value*1e-9

def ppt(value: float):
    """ Converts value from parts per trillion """
    return value*1e-12

def ppq(value: float):
    """ Converts value from parts per quadrillion """
    return value*1e-15