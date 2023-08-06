
from src import isovec as iso

# TODO: PEP-257 dicstrings (Google convention)
# TODO: allow (read) slicing
# TODO: copy function
# TODO (far): IAEA Livechart Data Download API class

carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})
tree = carbon_dioxide.make_node(weight=True)
tree.print_tree()
#cont_O = tree.get_nodes_by_content(iso.O_nat)

nitrogen2 = iso.Molecule("molecular nitrogen", { iso.N_nat: 2})

air = iso.Mixture("air", {
    carbon_dioxide:   iso.percent(50),  # Molecule
    nitrogen2:        iso.percent(50)   # Molecule
})

air.print_tree(weight=True)
air_tree = air.make_node(weight=True)
cont_O = air_tree.get_nodes_by_content(iso.O_nat)

print()
isotope_vector = air.get_isotopes(mode="atomic")
isotopes = list(isotope_vector.keys())
at_fracs = list(isotope_vector.values())


isotope_vector = air.get_isotopes(mode="weight")
wt_fracs = list(isotope_vector.values())
for isotope, at_frac, wt_frac in zip(isotopes, at_fracs, wt_fracs):
    print(f"{isotope.name:>6}: {at_frac*1e2:7.4f} at.% | {wt_frac*1e2:7.4f} wt.%")
pass