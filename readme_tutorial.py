
from src import isovec as iso


nitrogen = iso.Element("nitrogen", {
    iso.N_14: 9.963600E-01,
    iso.N_15: 3.640000E-03
})


carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})

methane = iso.Molecule("methane", {
    iso.C_nat: 1,
    iso.H_nat: 4
})
nitrogen2 = iso.Molecule("molecular nitrogen", { iso.N_nat: 2})
oxygen2 = iso.Molecule("molecular oxygen", { iso.O_nat: 2})


air = iso.Mixture("air", {
    nitrogen2:                  78.084E-02,  # Molecule
    oxygen2:        iso.percent(20.946),     # Molecule
    iso.Ar_nat:     iso.percent( 0.9340),    # Element
    carbon_dioxide:            417.0E-06,    # Molecule
    iso.Ne_nat:        iso.ppm( 18.18),      # Element
    iso.He_nat:        iso.ppm(  5.24),      # Element
    methane:           iso.ppm(  1.87),      # Molecule
    iso.Kr_nat:        iso.ppm(  1.14)       # Element
})
air.print_tree_input(weight=True)

print()
element_vector = air.get_elements(mode="atomic")
for element, at_frac in element_vector.items():
    print(f"{element.symbol:>2}: {at_frac:.4E}")

print()
isotope_vector = air.get_isotopes(mode="atomic", use_natural=(iso.O_nat,))
for isotope, at_frac in isotope_vector.items():
    isotope_name = isotope.name.replace("-0", "-nat")  # surrogate Isotopes have a mass number of zero
    print(f"{isotope_name:>6}: {at_frac:.4E}")

print()
air.print_tree_composition(weight=True)