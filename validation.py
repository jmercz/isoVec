
import copy

from src import isovec as iso

if __name__ == "__main__":

    ###################
    ### Ni80Cr20
    ###################
    # test conversion from weight to atom percent
    # as in https://www.plasmaterials.com/converting-atomic-percent-to-weight-percent-and-vice-versa/
    # Alloy of 80 wt.% Nickel and 20 wt.% Chromium

    print()
    print("Ni80Cr20 Test Case")
    print()

    ## hand calculation

    # conversion formula given on webpage
    atPercX = lambda wtPercX, atWtX, wtPercY, atWtY: (wtPercX/atWtX) / ((wtPercX/atWtX) + (wtPercY/atWtY)) * 100
    print()
    print(f"Nickel:   {atPercX(80, 58.71, 20, 51.99):.4f} at.%")
    print(f"Chromium: {atPercX(20, 51.99, 80, 58.71):.4f} at.%")
    print()


    ## isovec calculation

    # create copies of elements and overwrite atomic weights to match source
    nickel = copy.deepcopy(iso.Ni_nat)
    nickel._atomicWeight = 58.71
    chromium = copy.deepcopy(iso.Cr_nat)
    chromium._atomicWeight = 51.99

    print(30*"#")
    print()
    print("Alloy calculated by script:")
    Ni80Cr20 = iso.Mixture("Ni80Cr20", {
        nickel:   -80e-2,
        chromium: -20e-2
    })
    Ni80Cr20.PrintOverview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### Fe-7wt%C
    ###################
    # test conversion from weight to atom percent
    # as in https://www.southampton.ac.uk/~pasr1/g7.htm
    # Alloy of 93 wt.% Iron and 7 wt.% Carbon

    print()
    print("Fe-7wt%C Test Case")
    print()

    print()
    print(f"Carbon: 26 at.%")
    print()

    print(30*"#")
    print()
    print("Alloy calculated by script:")
    Fe7C = iso.Mixture("Fe-7C", {
        iso.Fe_nat: -93e-2,
        iso.C_nat:   -7e-2
    })
    Fe7C.PrintOverview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### Fe-25at%C
    ###################
    # test conversion from atom to weight percent
    # as in https://www.southampton.ac.uk/~pasr1/g7.htm
    # Alloy of 75 at.% Iron and 25 at.% Carbon

    print()
    print("Fe-25at%C Test Case")
    print()

    print()
    print(f"Carbon: 6.66 wt.%")
    print()

    print(30*"#")
    print()
    print("Alloy calculated by script:")
    Fe25C = iso.Mixture("Fe-25at.%C", {
        iso.Fe_nat: 75e-2,
        iso.C_nat:  25e-2
    })
    Fe25C.PrintOverview(True)



    print()
    print()
    print(80*"X")
    ###################
    ### 98 g Sn - 65 g Pb
    ###################
    # test conversion from weight to atom percent
    # as in https://www.youtube.com/watch?v=0otCqXjZkOw
    # Alloy of 98 g tin and 65 g lead

    print()
    print("98 g Sn - 65 g Pb Test Case")
    print()

    print()
    print(f"Tin:  72.47 at.%")
    print(f"Lead: 27.53 at.%")
    print()

    print(30*"#")
    print()
    print("Alloy calculated by script:")
    m_tin = 98 # [g]
    m_lead = 65 # [g]
    m_tot = m_tin + m_lead
    SnPb = iso.Mixture("Sn(98)Pb(65)", {
        iso.Sn_nat: -m_tin/m_tot,
        iso.Pb_nat: -m_lead/m_tot
    })
    SnPb.PrintOverview(True)

    SnPb2 = iso.Mixture("Sn(98)Pb(65)_direct", {
        iso.Sn_nat: -98,
        iso.Pb_nat: -65
    })
    SnPb2.PrintOverview(True)