
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

    print_raw_output = True  # print raw output of script calculations

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
    res_tree = Ni80Cr20.make_node("input")
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
        Ni80Cr20.print_tree_input(weight=True)



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
    res_tree = Fe7C.make_node("input")
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
        Fe7C.print_tree_input(weight=True)



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
    res_tree = Fe25C.make_node("input", weight=True)
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
        Fe25C.print_tree_input(weight=True)



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
    SnPb_dir = iso.Mixture("Sn(98)Pb(65)_direct", {
        iso.Sn_nat: -98,
        iso.Pb_nat: -65
    })

    # extract results
    res_tree = SnPb.make_node("input")
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
        SnPb.print_tree_input(weight=True)

        print()
        print("--- Alloy calculated by script with masses entered directly (shows normalisation): ---")
        SnPb_dir.print_tree_input(weight=True)



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
    res_tree = mix.make_node("input", weight=True)
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
        mix.print_tree_input(weight=True, volume=True)



    print()
    print()
    print(80*"X")
    ###################
    ### Internal composition fetching and conversion
    ###################
    desc = r"""
    test consistency of internal composition fetching and conversion
    """

    print()
    print(r"Internal composition fetching and conversion")
    print(desc)

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
    differences = air._compare_converted_isotopes()

    print()
    dif_at = differences["at"]
    i_max_dif_at = dif_at.index(max(dif_at, key=abs))
    print(f"Maximum atomic difference: {dif_at[i_max_dif_at]} (" + str(differences["rel_at"][i_max_dif_at]) + ")")
    dif_wt = differences["wt"]
    i_max_dif_wt = dif_wt.index(max(dif_wt, key=abs))
    print(f"Maximum weight difference: {dif_wt[i_max_dif_wt]} (" + str(differences["rel_wt"][i_max_dif_wt]) + ")")



    print()
    print()
    print(80*"X")
    ###################
    ### Detailed air composition
    ###################
    desc = r"""
    test conversion from atomic to weight percent for air
    as in https://de.wikipedia.org/wiki/Luft#Zusammensetzung
    """

    print()
    print(r"Detailed air composition")
    print(desc)

    N2 = iso.Molecule("molecular nitrogen", {iso.N_nat: 2})
    O2 = iso.Molecule("molecular oxygen",   {iso.O_nat: 2})
    H2 = iso.Molecule("molecular hydrogen", {iso.H_nat: 2})
    CO2 = iso.Molecule("carbon dioxide", {
        iso.C_nat:  1,
        iso.O_nat:  2
    }, symbol="CO2")
    CH4 = iso.Molecule("methane", {
        iso.C_nat:  1,
        iso.H_nat:  4
    }, symbol="CH4")
    N2O = iso.Molecule("dinitrogen oxide", {
        iso.N_nat:  2,
        iso.O_nat:  1
    }, symbol="N2O")
    CO = iso.Molecule("carbon monoxide", {
        iso.C_nat:  1,
        iso.O_nat:  1
    }, symbol="CO")
    CCl2F2 = iso.Molecule("dichlorodifluoromethane", {
        iso.C_nat:  1,
        iso.Cl_nat: 2,
        iso.F_nat:  2
    }, symbol="CCl2F2")
    CCl3F = iso.Molecule("trichlorofluoromethane", {
        iso.C_nat:  1,
        iso.Cl_nat: 3,
        iso.F_nat:  1
    }, symbol="CCl3F")
    CHClF2 = iso.Molecule("chlorodifluoromethane", {
        iso.C_nat:  1,
        iso.H_nat:  1,
        iso.Cl_nat: 1,
        iso.F_nat:  2
    }, symbol="CHClF2")
    CCl4 = iso.Molecule("tetrachloromethane", {
        iso.C_nat:  1,
        iso.Cl_nat: 4,
    }, symbol="CCl4")
    CClF2CCl2F = iso.Molecule("1,1,2-trichloro-1,2,2-trifluoroethane", {
        iso.C_nat:  2,
        iso.Cl_nat: 3,
        iso.F_nat:  3,
    }, symbol="CClF2CCl2F")
    C2H3Cl2F = iso.Molecule("1,1-dichloro-1-fluoroethane", {
        iso.C_nat:  2,
        iso.H_nat:  3,
        iso.Cl_nat: 2,
        iso.F_nat:  1,
    }, symbol="C2H3Cl2F")
    C2H3ClF2 = iso.Molecule("1-chloro-1,1-difluoroethane", {
        iso.C_nat:  2,
        iso.H_nat:  3,
        iso.Cl_nat: 1,
        iso.F_nat:  2,
    }, symbol="C2H3ClF2")
    SF6 = iso.Molecule("sulphur hexafluoride", {
        iso.S_nat:  1,
        iso.F_nat:  6,
    }, symbol="SF6")
    CBrClF2 = iso.Molecule("bromochlorodifluoromethane", {
        iso.C_nat:  1,
        iso.Br_nat: 1,
        iso.Cl_nat: 1,
        iso.F_nat:  2,
    }, symbol="CBrClF2")
    CBrF3 = iso.Molecule("bromotrifluoromethane", {
        iso.C_nat:  1,
        iso.Br_nat: 1,
        iso.F_nat:  3,
    }, symbol="CBrF3")

    air = iso.Mixture("dry air", {
        # main components
        N2:         iso.percent(78.084),
        O2:         iso.percent(20.942),
        iso.Ar_nat: iso.percent( 0.934),
        # trace gases
        CO2:        iso.ppm(400.0),
        iso.Ne_nat: iso.ppm( 18.18),
        iso.He_nat: iso.ppm(  5.24),
        CH4:        iso.ppm(  1.85),
        iso.Kr_nat: iso.ppm(  1.14),

        H2:         iso.ppb(500.0),
        N2O:        iso.ppb(328.0),
        CO:         iso.ppb(175.0),
        iso.Xe_nat: iso.ppb( 87.0),

        CCl2F2:     iso.ppt(520.0),
        CCl3F:      iso.ppt(234.0),
        CHClF2:     iso.ppt(253.0),
        CCl4:       iso.ppt( 81.0),
        CClF2CCl2F: iso.ppt( 71.0),
        C2H3Cl2F:   iso.ppt( 26.0),
        C2H3ClF2:   iso.ppt( 23.0),
        SF6:        iso.ppt(  8.0),
        CBrClF2:    iso.ppt(  4.0),
        CBrF3:      iso.ppt(  3.4),
    }, mode="atomic")

    # extract results
    res_tree = air.make_node("input", weight=True)
    res_table = [
        compare("N2 [wt.%]", 75.518, round(res_tree.get_nodes_by_content(N2)[0].data["w"]*1e2, 3)),
        compare("O2 [wt.%]", 23.135, round(res_tree.get_nodes_by_content(O2)[0].data["w"]*1e2, 3)),
        compare("Ar [wt.%]",  1.288, round(res_tree.get_nodes_by_content(iso.Ar_nat)[0].data["w"]*1e2, 3)),
        [],
        compare("CO2 [wt.ppm]",  590, round(res_tree.get_nodes_by_content(CO2)[0].data["w"]*1e6, 0)),
        compare("Ne [wt.ppm]",    12.67, round(res_tree.get_nodes_by_content(iso.Ne_nat)[0].data["w"]*1e6, 2)),
        compare("He [wt.ppm]",     0.72, round(res_tree.get_nodes_by_content(iso.He_nat)[0].data["w"]*1e6, 2)),
        compare("CH4 [wt.ppm]",    0.97, round(res_tree.get_nodes_by_content(CH4)[0].data["w"]*1e6, 2)),
        compare("Kr [wt.ppm]",     3.30, round(res_tree.get_nodes_by_content(iso.Kr_nat)[0].data["w"]*1e6, 2)),
        [],
        compare("H2 [wt.ppb]",    36, round(res_tree.get_nodes_by_content(H2)[0].data["w"]*1e9, 0)),
        compare("N2O [wt.ppb]",  480, round(res_tree.get_nodes_by_content(N2O)[0].data["w"]*1e9, 0)),
        compare("CO [wt.ppb]",   175, round(res_tree.get_nodes_by_content(CO)[0].data["w"]*1e9, 0)),
        compare("Xe [wt.ppb]",   400, round(res_tree.get_nodes_by_content(iso.Xe_nat)[0].data["w"]*1e9, 0)),
        [],
        compare("CCl2F2 [wt.ppt]",    2200, round(res_tree.get_nodes_by_content(CCl2F2)[0].data["w"]*1e12, 0)),
        compare("CCl3F [wt.ppt]",     1100, round(res_tree.get_nodes_by_content(CCl3F)[0].data["w"]*1e12, 0)),
        compare("CHClF2 [wt.ppt]",     480, round(res_tree.get_nodes_by_content(CHClF2)[0].data["w"]*1e12, 0)),
        compare("CCl4 [wt.ppt]",       510, round(res_tree.get_nodes_by_content(CCl4)[0].data["w"]*1e12, 0)),
        compare("CClF2CCl2F [wt.ppt]", 520, round(res_tree.get_nodes_by_content(CClF2CCl2F)[0].data["w"]*1e12, 0)),
        compare("C2H3Cl2F [wt.ppt]",    70, round(res_tree.get_nodes_by_content(C2H3Cl2F)[0].data["w"]*1e12, 0)),
        compare("C2H3ClF2 [wt.ppt]",    50, round(res_tree.get_nodes_by_content(C2H3ClF2)[0].data["w"]*1e12, 0)),
        compare("SF6 [wt.ppt]",         25, round(res_tree.get_nodes_by_content(SF6)[0].data["w"]*1e12, 0)),
        compare("CBrClF2 [wt.ppt]",     25, round(res_tree.get_nodes_by_content(CBrClF2)[0].data["w"]*1e12, 0)),
        compare("CBrF3 [wt.ppt]",       13, round(res_tree.get_nodes_by_content(CBrF3)[0].data["w"]*1e12, 0)),
    ]
    print(tabulate(res_table, headers=headers, **table_kwargs))
    print()

    if print_raw_output:
        print(30*"#")
        print()
        print("--- Mixture calculated by script: ---")
        air.print_tree_input(weight=True)
