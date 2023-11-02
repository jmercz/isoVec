
from collections import defaultdict
import numpy as np

from src import isovec as iso

# TODO: copy function
# TODO (far): IAEA Livechart Data Download API class


SiC = iso.Molecule("SiC molecule", {
    iso.Si_nat: 1,
    iso.C_nat: 1
}, rho = 3.21)
SiC_new = iso.Mixture("SiC molecule mixture", {
    iso.Si_nat: 1,
    iso.C_nat: 1
}, rho = 3.21)

U = iso.Mixture("uranium", {
    iso.U_nat: 1,
}, rho=19)


mixture_mode = "atomic"
matrix_molecule = iso.Mixture("matrix", {
    SiC: 0.5,
    iso.U_nat: 0.5
}, mode=mixture_mode)
matrix_mixture = iso.Mixture("matrix", {
    SiC_new: 0.5,
    iso.U_nat: 0.5
}, mode=mixture_mode)

matrix_molecule.print_tree_input(weight=True, volume=True)
print()
matrix_molecule.print_tree_composition(weight=True)
print()

elem_mol = matrix_molecule.get_elements(mode="atomic")
iso_mol = matrix_molecule.get_isotopes(mode="atomic", use_natural=(iso.C_nat,))

elem_mol = matrix_molecule._elemental_composition(by_weight=False)
iso_mol = matrix_molecule._isotopic_composition(by_weight=False, use_natural=(iso.C_nat,))


a = matrix_molecule._compare_converted_isotopes()
print()
a = matrix_mixture._compare_converted_isotopes()
pass