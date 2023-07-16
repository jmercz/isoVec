
from src import isovec as iso

# TODO: PEP-257 dicstrings (Google convention)
# TODO: print_overview gathering in own function (tree structure)
# TODO: isotope vector with mass fraction values
# TODO: allow (read) slicing
# TODO (far): IAEA Livechart Data Download API class

carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})

elem1 = iso.Substance("elem1", {
    iso.Fe_54:  0.5,
    iso.Fe_56:  0.5,
    })
print(elem1.constituents)
print(elem1.convert_to_wt())

elem2 = iso.Substance.from_weight("elem2", {
    iso.Fe_54:  0.49091997453009345,
    iso.Fe_56:  0.5090800254699065,
    })
print(elem2.constituents)