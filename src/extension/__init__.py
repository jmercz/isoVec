
from .Material import Material

from ..isovec import Element
from ..isovec.isotopes import U_234, U_235, U_238
from ..isovec.exceptions import FractionError

def EnrichedUranium(t_enrichment: float) -> Element:
    """
    Creates uranium element object with t_enrichment as at.% for U-235.
    """
    if t_enrichment > 0.999946:
        raise FractionError("Enrichment must be lower than or equal to 99.9946 at.%")

    atFrac_U8 = 1 - t_enrichment - 0.000054

    U = Element("uranium ({0} at.% enrichment)".format(t_enrichment*1e2), 92, {
            U_234: 0.000054,
            U_235: t_enrichment,
            U_238: atFrac_U8
        })

    return U