
import copy

from tabulate import tabulate

from src import isovec as iso

def _compare_converted_isotopes(substance: iso.Substance) -> dict[str, list[float]]:
        """Debug function to test consistency of fraction modes.
        
        Gets isotopes of substance via "atomic" and "weight" mode, then converts
        each case and compares the atomic and weight fractions from each case
        respectively. For correct behaviour, differences should approach zero.
        """

        print("#######################")
        print("  Get isotopes in atomic fraction:")
        tmp = substance.get_isotopes(mode="atomic", use_natural=(iso.C_nat,))
        iso_with_at = tmp.keys()
        iso_at = list(tmp.values())
        iso_at_to_wt = iso.at_to_wt(at_fracs=iso_at, molar_masses=[isotope.M for isotope in iso_with_at])
        print(f"Isotope |          at.%  |          wt.%")
        for i, isotope in enumerate(iso_with_at):
            print(f"{isotope.name:>6}  |  {iso_at[i]:12.10f}  |  {iso_at_to_wt[i]:12.10f}")
        
        print("#######################")
        print("  Get isotopes in weight fraction:")
        tmp = substance.get_isotopes(mode="weight", use_natural=(iso.C_nat,))
        iso_with_wt = tmp.keys()
        iso_wt = list(tmp.values())
        iso_wt_to_at = iso.wt_to_at(wt_fracs=iso_wt, molar_masses=[isotope.M for isotope in iso_with_wt])
        print(f"Isotope |          at.%  |          wt.%")
        for i, isotope in enumerate(iso_with_wt):
            print(f"{isotope.name:>6}  |  {iso_wt_to_at[i]:12.10f}  |  {iso_wt[i]:12.10f}")
        
        
        print("#######################")
        print("  Difference:")
        differences = {"at": [], "wt": []}
        print(f"Isotope |              at.%  |              wt.%")
        for i, isotope in enumerate(iso_with_wt):

            cur_dif_at = iso_at[i]-iso_wt_to_at[i]
            differences["at"].append(cur_dif_at)

            cur_dif_wt = iso_at_to_wt[i]-iso_wt[i]
            differences["wt"].append(cur_dif_wt)

            print(f"{isotope.name:>6}  |  {cur_dif_at: 12.9e}  |  {cur_dif_wt: 12.9e}")
        print("#######################")

        return differences


if __name__ == "__main__":

    print_raw_output = False  # print raw output of script calculations

    # tabulate options
    headers = ["", "expected result", "script result", "deviation"]  # header row for table
    def compare(comparison: str, expected: float, script: float) -> list:
        """Make row for table that compares expected and script results."""
        return [comparison, expected, script, script - expected]
    table_kwargs = {
        "tablefmt": "github",
        "stralign": "right"
    }

    ###################
    ### Ni80Cr20
    ###################
    desc = r"""
    test conversion from weight to atom percent
    as in https://www.plasmaterials.com/converting-atomic-percent-to-weight-percent-and-vice-versa/
    Alloy of 80 wt.% Nickel and 20 wt.% Chromium
    """

    print()
    print(r"Ni80Cr20 Test Case")
    print(desc)

    ## hand calculation

    # conversion formula given on webpage
    atPercX = lambda wtPercX, atWtX, wtPercY, atWtY: (wtPercX/atWtX) / ((wtPercX/atWtX) + (wtPercY/atWtY)) * 100


    ## isovec calculation

    # create copies of elements and overwrite atomic weights to match source
    nickel = copy.deepcopy(iso.Ni_nat)
    nickel._atomicWeight = 58.71
    chromium = copy.deepcopy(iso.Cr_nat)
    chromium._atomicWeight = 51.99

    Ni80Cr20 = iso.Mixture("Ni80Cr20", {
        nickel:   -80e-2,
        chromium: -20e-2
    })

    # extract results
    res_tree = Ni80Cr20.make_node()
    wtP_Ni = round(res_tree.get_nodes_by_content(nickel)[0].data["x"]*100, 2)
    wtP_Cr = round(res_tree.get_nodes_by_content(chromium)[0].data["x"]*100, 2)

    res_table = [
        compare("Nickel [at.%]",   round(atPercX(80, 58.71, 20, 51.99), 2), wtP_Ni),
        compare("Chromium [at.%]", round(atPercX(20, 51.99, 80, 58.71), 2), wtP_Cr),
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Alloy calculated by script: ---")
        Ni80Cr20.print_overview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### Fe-7wt%C
    ###################
    desc = r"""
    test conversion from weight to atom percent
    as in https://www.southampton.ac.uk/~pasr1/g7.htm
    Alloy of 93 wt.% Iron and 7 wt.% Carbon
    """

    print()
    print(r"Fe-7wt%C Test Case")
    print(desc)

    Fe7C = iso.Mixture("Fe-7C", {
        iso.Fe_nat: -93e-2,
        iso.C_nat:   -7e-2
    })

    # extract results
    res_tree = Fe7C.make_node()
    wtP_C = round(res_tree.get_nodes_by_content(iso.C_nat)[0].data["x"]*100, 0)

    res_table = [
        compare("Carbon [at.%]", 26, wtP_C),
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Alloy calculated by script: ---")
        Fe7C.print_overview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### Fe-25at%C
    ###################
    desc = r"""
    test conversion from atom to weight percent
    as in https://www.southampton.ac.uk/~pasr1/g7.htm
    Alloy of 75 at.% Iron and 25 at.% Carbon
    """

    print()
    print(r"Fe-25at%C Test Case")
    print(desc)

    Fe25C = iso.Mixture("Fe-25at.%C", {
        iso.Fe_nat: 75e-2,
        iso.C_nat:  25e-2
    })

    # extract results
    res_tree = Fe25C.make_node(weight=True)
    wtP_C = round(res_tree.get_nodes_by_content(iso.C_nat)[0].data["w"]*100, 2)

    res_table = [
        compare("Carbon [wt.%]", 6.66, wtP_C),
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Alloy calculated by script: ---")
        Fe25C.print_overview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### 98 g Sn - 65 g Pb
    ###################
    desc = r"""
    test conversion from weight to atom percent
    as in https://www.youtube.com/watch?v=0otCqXjZkOw
    Alloy of 98 g tin and 65 g lead
    """

    print()
    print(r"98 g Sn - 65 g Pb Test Case")
    print(desc)

    m_tin = 98  # [g]
    m_lead = 65  # [g]
    m_tot = m_tin + m_lead
    SnPb = iso.Mixture("Sn(98)Pb(65)", {
        iso.Sn_nat: -m_tin/m_tot,
        iso.Pb_nat: -m_lead/m_tot
    })
    SnPb2 = iso.Mixture("Sn(98)Pb(65)_direct", {
        iso.Sn_nat: -98,
        iso.Pb_nat: -65
    })

    # extract results
    res_tree = SnPb.make_node()
    atP_Sn = round(res_tree.get_nodes_by_content(iso.Sn_nat)[0].data["x"]*100, 2)
    atP_Pb = round(res_tree.get_nodes_by_content(iso.Pb_nat)[0].data["x"]*100, 2)

    res_table = [
        compare("Tin [at.%]",  72.47, atP_Sn),
        compare("Lead [at.%]", 27.53, atP_Pb)
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Alloy calculated by script: ---")
        SnPb.print_overview(True)

        print()
        print("--- Alloy calculated by script with masses entered directly (shows normalisation): ---")
        SnPb2.print_overview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### 20 vol.% alcohol in water
    ###################
    desc = r"""
    test conversion from volume to weight percent
    as in https://rechneronline.de/volume-mass-percent/
    Mixture of 20 vol.% alcohol in water
    """

    print()
    print(r"20 vol.% alcohol in water Test Case")
    print(desc)

    alcohol = iso.Molecule(
        "alcohol", {},
        M=46.08,
        rho=0.789  # from website
    )
    water = iso.Molecule(
        "water", {},
        M=18.01528,
        rho=1.  # from website
    )
    mix = iso.Mixture("mix", {
        alcohol: 20,
        water: 100-20
    }, mode="volume")

    # extract results
    res_tree = mix.make_node(weight=True)
    wtP_alcohol = round(res_tree.get_nodes_by_content(alcohol)[0].data["w"]*100, 1)

    res_table = [
        compare("Alcohol [vol.%]", 16.5, wtP_alcohol)
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Mixture calculated by script: ---")
        mix.print_tree(weight=True, volume=True)