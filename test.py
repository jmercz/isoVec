
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
a = SiC.get_elements("weight")

U = iso.Mixture("uranium", {
    iso.U_nat: 1,
}, rho=19)


mixture_mode = "weight"
matrix_molecule = iso.Mixture("matrix", {
    SiC: 0.5,
    iso.U_nat: 0.5
}, mode=mixture_mode)
matrix_mixture = iso.Mixture("matrix", {
    SiC_new: 0.5,
    iso.U_nat: 0.5
}, mode=mixture_mode)

tmp_mol = matrix_molecule.get_elements(mode="atomic")
tmp_mix = matrix_mixture.get_elements(mode="atomic")


## old, with molecule (NOT correct)

isotopes = matrix_molecule.get_isotopes(mode="atomic")
iso_with_1 = isotopes.keys()
iso1_at_molecule = list(isotopes.values())

isotopes = matrix_molecule.get_isotopes(mode="weight")
iso_with_1 = isotopes.keys()
iso1_wt_molecule = list(isotopes.values())

## old, with mixture (correct)

isotopes = matrix_mixture.get_isotopes(mode="atomic")
iso_with_1 = isotopes.keys()
iso1_at_mixture = list(isotopes.values())

isotopes = matrix_mixture.get_isotopes(mode="weight")
iso_with_1 = isotopes.keys()
iso1_wt_mixture = list(isotopes.values())

## new

# extract isotopes in atomic mode and convert to weight
tmp = matrix_molecule.get_isotopes2(mode="atomic")
iso_with_at = tmp.keys()
iso2_at_molecule = list(tmp.values())
conv_wt = iso.at_to_wt(at_fracs=iso2_at_molecule, molar_masses=[isotope.M for isotope in iso_with_at])

# extract isotopes in weight mode and convert to atomic
tmp = matrix_molecule.get_isotopes2(mode="weight")
iso_with_wt = tmp.keys()
iso2_wt_molecule = list(tmp.values())
conv_at = iso.wt_to_at(wt_fracs=iso2_wt_molecule, molar_masses=[isotope.M for isotope in iso_with_wt])

iso2_at_mixture = list(matrix_mixture.get_isotopes2(mode="atomic").values())
iso2_wt_mixture = list(matrix_mixture.get_isotopes2(mode="weight").values())

print()
print(f"Mixture mode: {mixture_mode}")
print()

if False:

    assert(iso_with_at == iso_with_wt)

    differences = defaultdict(list)

    print("##########################################################")
    print("")
    print("Internal consistency of `get_isotopes2`")
    print()

    # print for atomic percent
    print(f"Isotope |   direct at.%  | converted at.%  |  difference at.% (relative difference)")
    for i, isotope in enumerate(iso_with_at):
        dir = iso2_at_molecule[i]
        conv = conv_at[i]
        dif = dir - conv
        dif_rel = dif / dir
        print(f"{isotope.name:>7} |  {dir:12.10f}  |  {conv: 12.10f}  |  {dif: 12.9e} ({dif_rel: 12.9e})")
        differences["at"].append(dif)
        differences["rel_at"].append(dif_rel)

    print()

    # print for weight percent
    print(f"Isotope |   direct wt.%  | converted wt.%  |  difference wt.% (relative difference)")
    for i, isotope in enumerate(iso_with_wt):
        dir = iso2_wt_molecule[i]
        conv = conv_wt[i]
        dif = dir - conv
        dif_rel = dif / dir
        print(f"{isotope.name:>7} |  {dir:12.10f}  |  {conv: 12.10f}  |  {dif: 12.9e} ({dif_rel: 12.9e})")
        differences["wt"].append(dif)
        differences["rel_wt"].append(dif_rel)

    print("")
    print("##########################################################")

    print()

    differences2 = matrix_molecule._compare_converted_isotopes2()
    dif_dif_at = np.array(differences["at"]) - np.array(differences2["at"])
    dif_dif_wt = np.array(differences["wt"]) - np.array(differences2["wt"])
    print(dif_dif_at)
    print(dif_dif_wt)
    exit(0)


print()
print("`get_isotopes`  in \"atomic\" mode, when using `Molecule` against")
print("`get_isotopes2` in \"atomic\" mode, when using `Molecule`")
for isot, i1, i2 in zip(iso_with_1, iso1_at_molecule, iso2_at_molecule):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

print()
print("`get_isotopes`  in \"weight\" mode, when using `Molecule` against")
print("`get_isotopes2` in \"weight\" mode, when using `Molecule`")
for isot, i1, i2 in zip(iso_with_1, iso1_wt_molecule, iso2_wt_molecule):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

print()
print("`get_isotopes`  in \"atomic\" mode, when using `Mixture` against")
print("`get_isotopes2` in \"atomic\" mode, when using `Molecule`")
for isot, i1, i2 in zip(iso_with_1, iso1_at_mixture, iso2_at_molecule):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

print()
print("`get_isotopes`  in \"weight\" mode, when using `Mixture` against")
print("`get_isotopes2` in \"weight\" mode, when using `Molecule`")
for isot, i1, i2 in zip(iso_with_1, iso1_wt_mixture, iso2_wt_molecule):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

print()
print("`get_isotopes2` in \"atomic\" mode, when using `Molecule` against")
print("`get_isotopes2` in \"atomic\" mode, when using `Mixture`")
for isot, i1, i2 in zip(iso_with_1, iso2_at_molecule, iso2_at_mixture):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

print()
print("`get_isotopes2` in \"weight\" mode, when using `Molecule` against")
print("`get_isotopes2` in \"weight\" mode, when using `Mixture`")
for isot, i1, i2 in zip(iso_with_1, iso2_wt_molecule, iso2_wt_mixture):
    print(f"{isot.name:>7} |  {i1:12.10f}  |  {i2: 12.10f}  |  {i1-i2: 12.9e} ({(i1-i2)/i1: 12.9e})")

exit(0)



#a = matrix._compare_converted_isotopes()
pass