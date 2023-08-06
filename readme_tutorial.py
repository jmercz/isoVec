
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
    nitrogen2:                 78.084E-02,  # Molecule
    oxygen2:        iso.percent(20.946),    # Molecule
    iso.Ar_nat:     iso.percent( 0.9340),   # Element
    carbon_dioxide:            417.0E-06,   # Molecule
    iso.Ne_nat:        iso.ppm( 18.18),     # Element
    iso.He_nat:        iso.ppm(  5.24),     # Element
    methane:           iso.ppm(  1.87),     # Molecule
    iso.Kr_nat:        iso.ppm(  1.14)      # Element
})
air.print_overview(True)

isotope_vector = air.get_isotopes(use_natural=False)
for isotope, at_frac in isotope_vector.items():
    print(f"{isotope.name:>6}: {at_frac*1e2:.4f} at.%")

print()
isotope_vector_wt = air.get_isotopes(mode="weight", use_natural=False)
for isotope, wt_frac in isotope_vector_wt.items():
    print(f"{isotope.name:>6}: {wt_frac*1e2:.4f} wt.%")

print()
tree = air.print_tree(weight=True, align_isotopes=True)
print()

