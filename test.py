
from src import isovec as iso

# TODO: PEP-257 dicstrings (Google convention)
# TODO: print_overview gathering in own function (tree structure)
# TODO: isotope vector with mass fraction values
# TODO: allow (read) slicing
# TODO (far): IAEA Livechart Data Download API class

#carbon_dioxide = iso.Molecule("carbon dioxide", {
#    iso.C_nat: 1,
#    iso.O_nat: 2
#})

elem1 = iso.Element("elem1", {
    42:  0.5,
    iso.Fe_56:  0.5,
    })
print(elem1.constituents)
print(elem1.get_constituents_in_wt())

isos = elem1.get_isotopes()
print(isos)
elem1.rho