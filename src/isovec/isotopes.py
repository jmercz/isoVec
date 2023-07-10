# module with all isotopes

from .isotope import Isotope


#   1: H  (hydrogen)
H_1    = Isotope("H-1"   ,   1,   1, 1.00782503223)
H      = Isotope("H"     ,   1,   1, 1.00782503223)  # alias
H_2    = Isotope("H-2"   ,   1,   2, 2.01410177812)
D      = Isotope("D"     ,   1,   2, 2.01410177812)  # alias
H_3    = Isotope("H-3"   ,   1,   3, 3.0160492779)
T      = Isotope("T"     ,   1,   3, 3.0160492779)   # alias

#   2: He (helium)
He_3   = Isotope("He-3"  ,   2,   3, 3.0160293201)
He_4   = Isotope("He-4"  ,   2,   4, 4.00260325413)

#   3: Li (lithium)
Li_6   = Isotope("Li-6"  ,   3,   6, 6.0151228874)
Li_7   = Isotope("Li-7"  ,   3,   7, 7.0160034366)

#   4: Be (berylium)
Be_9   = Isotope("Be-9"  ,   4,   9, 9.012183065)

#   5: B  (boron)
B_10   = Isotope("B-10"  ,   5,  10, 10.01293695)
B_11   = Isotope("B-11"  ,   5,  11, 11.00930536)

#   6: C  (carbon)
C_12   = Isotope("C-12"  ,   6,  12, 12.0)
C_13   = Isotope("C-13"  ,   6,  13, 13.00335483507)
C_14   = Isotope("C-14"  ,   6,  14, 14.0032419884)

#   7: N  (nitrogen)
N_14   = Isotope("N-14"  ,   7,  14, 14.00307400443)
N_15   = Isotope("N-15"  ,   7,  15, 15.00010889888)

#   8: O  (oxygen)
O_16   = Isotope("O-16"  ,   8,  16, 15.99491461957)
O_17   = Isotope("O-17"  ,   8,  17, 16.9991317565)
O_18   = Isotope("O-18"  ,   8,  18, 17.99915961286)

#   9: F  (fluorine)
F_19   = Isotope("F-19"  ,   9,  19, 18.99840316273)

#  10: Ne (neon)
Ne_20  = Isotope("Ne-20" ,  10,  20, 19.9924401762)
Ne_21  = Isotope("Ne-21" ,  10,  21, 20.993846685)
Ne_22  = Isotope("Ne-22" ,  10,  22, 21.991385114)

#  11: Na (sodium)
Na_23  = Isotope("Na-23" ,  11,  23, 22.989769282)

#  12: Mg (magnesium)
Mg_24  = Isotope("Mg-24" ,  12,  24, 23.985041697)
Mg_25  = Isotope("Mg-25" ,  12,  25, 24.985836976)
Mg_26  = Isotope("Mg-26" ,  12,  26, 25.982592968)

#  13: Al (aluminium)
Al_27  = Isotope("Al-27" ,  13,  27, 26.98153853)

#  14: Si (silicon)
Si_28  = Isotope("Si-28" ,  14,  28, 27.97692653465)
Si_29  = Isotope("Si-29" ,  14,  29, 28.9764946649)
Si_30  = Isotope("Si-30" ,  14,  30, 29.973770136)

#  15: P  (phosphorus)
P_31   = Isotope("P-31"  ,  15,  31, 30.97376199842)

#  16: S  (sulphur)
S_32   = Isotope("S-32"  ,  16,  32, 31.9720711744)
S_33   = Isotope("S-33"  ,  16,  33, 32.9714589098)
S_34   = Isotope("S-34"  ,  16,  34, 33.967867004)
S_36   = Isotope("S-36"  ,  16,  36, 35.96708071)

#  17: Cl (chlorine)
Cl_35  = Isotope("Cl-35" ,  17,  35, 34.968852682)
Cl_37  = Isotope("Cl-37" ,  17,  37, 36.965902602)

#  18: Ar (argon)
Ar_36  = Isotope("Ar-36" ,  18,  36, 35.967545105)
Ar_38  = Isotope("Ar-38" ,  18,  38, 37.96273211)
Ar_40  = Isotope("Ar-40" ,  18,  40, 39.9623831237)

#  19: K  (potassium)
K_39   = Isotope("K-39"  ,  19,  39, 38.9637064864)
K_40   = Isotope("K-40"  ,  19,  40, 39.963998166)
K_41   = Isotope("K-41"  ,  19,  41, 40.9618252579)

#  20: Ca (calcium)
Ca_40  = Isotope("Ca-40" ,  20,  40, 39.962590863)
Ca_42  = Isotope("Ca-42" ,  20,  42, 41.95861783)
Ca_43  = Isotope("Ca-43" ,  20,  43, 42.95876644)
Ca_44  = Isotope("Ca-44" ,  20,  44, 43.95548156)
Ca_46  = Isotope("Ca-46" ,  20,  46, 45.953689)
Ca_48  = Isotope("Ca-48" ,  20,  48, 47.95252276)

#  21: Sc (scandium)
Sc_45  = Isotope("Sc-45" ,  21,  45, 44.95590828)

#  22: Ti (titanium)
Ti_46  = Isotope("Ti-46" ,  22,  46, 45.95262772)
Ti_47  = Isotope("Ti-47" ,  22,  47, 46.95175879)
Ti_48  = Isotope("Ti-48" ,  22,  48, 47.94794198)
Ti_49  = Isotope("Ti-49" ,  22,  49, 48.94786568)
Ti_50  = Isotope("Ti-50" ,  22,  50, 49.94478689)

#  23: V  (vanadium)
V_50   = Isotope("V-50"  ,  23,  50, 49.94715601)
V_51   = Isotope("V-51"  ,  23,  51, 50.94395704)

#  24: Cr (chromium)
Cr_50  = Isotope("Cr-50" ,  24,  50, 49.94604183)
Cr_52  = Isotope("Cr-52" ,  24,  52, 51.94050623)
Cr_53  = Isotope("Cr-53" ,  24,  53, 52.94064815)
Cr_54  = Isotope("Cr-54" ,  24,  54, 53.93887916)

#  25: Mn (manganese)
Mn_55  = Isotope("Mn-55" ,  25,  55, 54.93804391)

#  26: Fe (iron)
Fe_54  = Isotope("Fe-54" ,  26,  54, 53.93960899)
Fe_56  = Isotope("Fe-56" ,  26,  56, 55.93493633)
Fe_57  = Isotope("Fe-57" ,  26,  57, 56.93539284)
Fe_58  = Isotope("Fe-58" ,  26,  58, 57.93327443)

#  27: Co (cobalt)
Co_59  = Isotope("Co-59" ,  27,  59, 58.93319429)

#  28: Ni (nickel)
Ni_58  = Isotope("Ni-58" ,  28,  58, 57.93534241)
Ni_60  = Isotope("Ni-60" ,  28,  60, 59.93078588)
Ni_61  = Isotope("Ni-61" ,  28,  61, 60.93105557)
Ni_62  = Isotope("Ni-62" ,  28,  62, 61.92834537)
Ni_64  = Isotope("Ni-64" ,  28,  64, 63.92796682)

#  29: Cu (copper)
Cu_63  = Isotope("Cu-63" ,  29,  63, 62.92959772)
Cu_65  = Isotope("Cu-65" ,  29,  65, 64.9277897)

#  30: Zn (zinc)
Zn_64  = Isotope("Zn-64" ,  30,  64, 63.92914201)
Zn_66  = Isotope("Zn-66" ,  30,  66, 65.92603381)
Zn_67  = Isotope("Zn-67" ,  30,  67, 66.92712775)
Zn_68  = Isotope("Zn-68" ,  30,  68, 67.92484455)
Zn_70  = Isotope("Zn-70" ,  30,  70, 69.9253192)

#  31: Ga (gallium)
Ga_69  = Isotope("Ga-69" ,  31,  69, 68.9255735)
Ga_71  = Isotope("Ga-71" ,  31,  71, 70.92470258)

#  32: Ge (germanium)
Ge_70  = Isotope("Ge-70" ,  32,  70, 69.92424875)
Ge_72  = Isotope("Ge-72" ,  32,  72, 71.922075826)
Ge_73  = Isotope("Ge-73" ,  32,  73, 72.923458956)
Ge_74  = Isotope("Ge-74" ,  32,  74, 73.921177761)
Ge_76  = Isotope("Ge-76" ,  32,  76, 75.921402726)

#  33: As (arsenic)
As_75  = Isotope("As-75" ,  33,  75, 74.92159457)

#  34: Se (selenium)
Se_74  = Isotope("Se-74" ,  34,  74, 73.922475934)
Se_76  = Isotope("Se-76" ,  34,  76, 75.919213704)
Se_77  = Isotope("Se-77" ,  34,  77, 76.919914154)
Se_78  = Isotope("Se-78" ,  34,  78, 77.91730928)
Se_80  = Isotope("Se-80" ,  34,  80, 79.9165218)
Se_82  = Isotope("Se-82" ,  34,  82, 81.9166995)

#  35: Br (bromine)
Br_79  = Isotope("Br-79" ,  35,  79, 78.9183376)
Br_81  = Isotope("Br-81" ,  35,  81, 80.9162897)

#  36: Kr (krypton)
Kr_78  = Isotope("Kr-78" ,  36,  78, 77.92036494)
Kr_80  = Isotope("Kr-80" ,  36,  80, 79.91637808)
Kr_82  = Isotope("Kr-82" ,  36,  82, 81.91348273)
Kr_83  = Isotope("Kr-83" ,  36,  83, 82.91412716)
Kr_84  = Isotope("Kr-84" ,  36,  84, 83.9114977282)
Kr_86  = Isotope("Kr-86" ,  36,  86, 85.9106106269)

#  37: Rb (rubidium)
Rb_85  = Isotope("Rb-85" ,  37,  85, 84.9117897379)
Rb_87  = Isotope("Rb-87" ,  37,  87, 86.909180531)

#  38: Sr (strontium)
Sr_84  = Isotope("Sr-84" ,  38,  84, 83.9134191)
Sr_86  = Isotope("Sr-86" ,  38,  86, 85.9092606)
Sr_87  = Isotope("Sr-87" ,  38,  87, 86.9088775)
Sr_88  = Isotope("Sr-88" ,  38,  88, 87.9056125)

#  39: Y  (yttrium)
Y_89   = Isotope("Y-89"  ,  39,  89, 88.9058403)

#  40: Zr (zirconium)
Zr_90  = Isotope("Zr-90" ,  40,  90, 89.9046977)
Zr_91  = Isotope("Zr-91" ,  40,  91, 90.9056396)
Zr_92  = Isotope("Zr-92" ,  40,  92, 91.9050347)
Zr_94  = Isotope("Zr-94" ,  40,  94, 93.9063108)
Zr_96  = Isotope("Zr-96" ,  40,  96, 95.9082714)

#  41: Nb (niobium)
Nb_93  = Isotope("Nb-93" ,  41,  93, 92.906373)

#  42: Mo (molybdenum)
Mo_92  = Isotope("Mo-92" ,  42,  92, 91.90680796)
Mo_94  = Isotope("Mo-94" ,  42,  94, 93.9050849)
Mo_95  = Isotope("Mo-95" ,  42,  95, 94.90583877)
Mo_96  = Isotope("Mo-96" ,  42,  96, 95.90467612)
Mo_97  = Isotope("Mo-97" ,  42,  97, 96.90601812)
Mo_98  = Isotope("Mo-98" ,  42,  98, 97.90540482)
Mo_100 = Isotope("Mo-100",  42, 100, 99.9074718)

#  43: Tc (technetium)
Tc_97  = Isotope("Tc-97" ,  43,  97, 96.9063667)
Tc_98  = Isotope("Tc-98" ,  43,  98, 97.9072124)
Tc_99  = Isotope("Tc-99" ,  43,  99, 98.9062508)

#  44: Ru (ruthenium)
Ru_96  = Isotope("Ru-96" ,  44,  96, 95.90759025)
Ru_98  = Isotope("Ru-98" ,  44,  98, 97.9052868)
Ru_99  = Isotope("Ru-99" ,  44,  99, 98.9059341)
Ru_100 = Isotope("Ru-100",  44, 100, 99.9042143)
Ru_101 = Isotope("Ru-101",  44, 101, 100.9055769)
Ru_102 = Isotope("Ru-102",  44, 102, 101.9043441)
Ru_104 = Isotope("Ru-104",  44, 104, 103.9054275)

#  45: Rh (rhodium)
Rh_103 = Isotope("Rh-103",  45, 103, 102.905498)

#  46: Pd (palladium)
Pd_102 = Isotope("Pd-102",  46, 102, 101.9056022)
Pd_104 = Isotope("Pd-104",  46, 104, 103.9040305)
Pd_105 = Isotope("Pd-105",  46, 105, 104.9050796)
Pd_106 = Isotope("Pd-106",  46, 106, 105.9034804)
Pd_108 = Isotope("Pd-108",  46, 108, 107.9038916)
Pd_110 = Isotope("Pd-110",  46, 110, 109.9051722)

#  47: Ag (silver)
Ag_107 = Isotope("Ag-107",  47, 107, 106.9050916)
Ag_109 = Isotope("Ag-109",  47, 109, 108.9047553)

#  48: Cd (cadmium)
Cd_106 = Isotope("Cd-106",  48, 106, 105.9064599)
Cd_108 = Isotope("Cd-108",  48, 108, 107.9041834)
Cd_110 = Isotope("Cd-110",  48, 110, 109.90300661)
Cd_111 = Isotope("Cd-111",  48, 111, 110.90418287)
Cd_112 = Isotope("Cd-112",  48, 112, 111.90276287)
Cd_113 = Isotope("Cd-113",  48, 113, 112.90440813)
Cd_114 = Isotope("Cd-114",  48, 114, 113.90336509)
Cd_116 = Isotope("Cd-116",  48, 116, 115.90476315)

#  49: In (indium)
In_113 = Isotope("In-113",  49, 113, 112.90406184)
In_115 = Isotope("In-115",  49, 115, 114.903878776)

#  50: Sn (tin)
Sn_112 = Isotope("Sn-112",  50, 112, 111.90482387)
Sn_114 = Isotope("Sn-114",  50, 114, 113.9027827)
Sn_115 = Isotope("Sn-115",  50, 115, 114.903344699)
Sn_116 = Isotope("Sn-116",  50, 116, 115.9017428)
Sn_117 = Isotope("Sn-117",  50, 117, 116.90295398)
Sn_118 = Isotope("Sn-118",  50, 118, 117.90160657)
Sn_119 = Isotope("Sn-119",  50, 119, 118.90331117)
Sn_120 = Isotope("Sn-120",  50, 120, 119.90220163)
Sn_122 = Isotope("Sn-122",  50, 122, 121.9034438)
Sn_124 = Isotope("Sn-124",  50, 124, 123.9052766)

#  51: Sb (antimony)
Sb_121 = Isotope("Sb-121",  51, 121, 120.903812)
Sb_123 = Isotope("Sb-123",  51, 123, 122.9042132)

#  52: Te (tellurium)
Te_120 = Isotope("Te-120",  52, 120, 119.9040593)
Te_122 = Isotope("Te-122",  52, 122, 121.9030435)
Te_123 = Isotope("Te-123",  52, 123, 122.9042698)
Te_124 = Isotope("Te-124",  52, 124, 123.9028171)
Te_125 = Isotope("Te-125",  52, 125, 124.9044299)
Te_126 = Isotope("Te-126",  52, 126, 125.9033109)
Te_128 = Isotope("Te-128",  52, 128, 127.90446128)
Te_130 = Isotope("Te-130",  52, 130, 129.906222748)

#  53: I  (iodine)
I_127  = Isotope("I-127" ,  53, 127, 126.9044719)

#  54: Xe (xenon)
Xe_124 = Isotope("Xe-124",  54, 124, 123.905892)
Xe_126 = Isotope("Xe-126",  54, 126, 125.9042983)
Xe_128 = Isotope("Xe-128",  54, 128, 127.903531)
Xe_129 = Isotope("Xe-129",  54, 129, 128.9047808611)
Xe_130 = Isotope("Xe-130",  54, 130, 129.903509349)
Xe_131 = Isotope("Xe-131",  54, 131, 130.90508406)
Xe_132 = Isotope("Xe-132",  54, 132, 131.9041550856)
Xe_134 = Isotope("Xe-134",  54, 134, 133.90539466)
Xe_136 = Isotope("Xe-136",  54, 136, 135.907214484)

#  55: Cs (caesium)
Cs_133 = Isotope("Cs-133",  55, 133, 132.905451961)

#  56: Ba (barium)
Ba_130 = Isotope("Ba-130",  56, 130, 129.9063207)
Ba_132 = Isotope("Ba-132",  56, 132, 131.9050611)
Ba_134 = Isotope("Ba-134",  56, 134, 133.90450818)
Ba_135 = Isotope("Ba-135",  56, 135, 134.90568838)
Ba_136 = Isotope("Ba-136",  56, 136, 135.90457573)
Ba_137 = Isotope("Ba-137",  56, 137, 136.90582714)
Ba_138 = Isotope("Ba-138",  56, 138, 137.905247)

#  57: La (lanthanum)
La_138 = Isotope("La-138",  57, 138, 137.9071149)
La_139 = Isotope("La-139",  57, 139, 138.9063563)

#  58: Ce (cerium)
Ce_136 = Isotope("Ce-136",  58, 136, 135.90712921)
Ce_138 = Isotope("Ce-138",  58, 138, 137.905991)
Ce_140 = Isotope("Ce-140",  58, 140, 139.9054431)
Ce_142 = Isotope("Ce-142",  58, 142, 141.9092504)

#  59: Pr (praseodymium)
Pr_141 = Isotope("Pr-141",  59, 141, 140.9076576)

#  60: Nd (neodymium)
Nd_142 = Isotope("Nd-142",  60, 142, 141.907729)
Nd_143 = Isotope("Nd-143",  60, 143, 142.90982)
Nd_144 = Isotope("Nd-144",  60, 144, 143.910093)
Nd_145 = Isotope("Nd-145",  60, 145, 144.9125793)
Nd_146 = Isotope("Nd-146",  60, 146, 145.9131226)
Nd_148 = Isotope("Nd-148",  60, 148, 147.9168993)
Nd_150 = Isotope("Nd-150",  60, 150, 149.9209022)

#  61: Pm (promethium)
Pm_145 = Isotope("Pm-145",  61, 145, 144.9127559)
Pm_147 = Isotope("Pm-147",  61, 147, 146.915145)

#  62: Sm (samarium)
Sm_144 = Isotope("Sm-144",  62, 144, 143.9120065)
Sm_147 = Isotope("Sm-147",  62, 147, 146.9149044)
Sm_148 = Isotope("Sm-148",  62, 148, 147.9148292)
Sm_149 = Isotope("Sm-149",  62, 149, 148.9171921)
Sm_150 = Isotope("Sm-150",  62, 150, 149.9172829)
Sm_152 = Isotope("Sm-152",  62, 152, 151.9197397)
Sm_154 = Isotope("Sm-154",  62, 154, 153.9222169)

#  63: Eu (europium)
Eu_151 = Isotope("Eu-151",  63, 151, 150.9198578)
Eu_153 = Isotope("Eu-153",  63, 153, 152.921238)

#  64: Gd (gadolinium)
Gd_152 = Isotope("Gd-152",  64, 152, 151.9197995)
Gd_154 = Isotope("Gd-154",  64, 154, 153.9208741)
Gd_155 = Isotope("Gd-155",  64, 155, 154.9226305)
Gd_156 = Isotope("Gd-156",  64, 156, 155.9221312)
Gd_157 = Isotope("Gd-157",  64, 157, 156.9239686)
Gd_158 = Isotope("Gd-158",  64, 158, 157.9241123)
Gd_160 = Isotope("Gd-160",  64, 160, 159.9270624)

#  65: Tb (terbium)
Tb_159 = Isotope("Tb-159",  65, 159, 158.9253547)

#  66: Dy (dysprosium)
Dy_156 = Isotope("Dy-156",  66, 156, 155.9242847)
Dy_158 = Isotope("Dy-158",  66, 158, 157.9244159)
Dy_160 = Isotope("Dy-160",  66, 160, 159.9252046)
Dy_161 = Isotope("Dy-161",  66, 161, 160.9269405)
Dy_162 = Isotope("Dy-162",  66, 162, 161.9268056)
Dy_163 = Isotope("Dy-163",  66, 163, 162.9287383)
Dy_164 = Isotope("Dy-164",  66, 164, 163.9291819)

#  67: Ho (holmium)
Ho_165 = Isotope("Ho-165",  67, 165, 164.9303288)

#  68: Er (erbium)
Er_162 = Isotope("Er-162",  68, 162, 161.9287884)
Er_164 = Isotope("Er-164",  68, 164, 163.9292088)
Er_166 = Isotope("Er-166",  68, 166, 165.9302995)
Er_167 = Isotope("Er-167",  68, 167, 166.9320546)
Er_168 = Isotope("Er-168",  68, 168, 167.9323767)
Er_170 = Isotope("Er-170",  68, 170, 169.9354702)

#  69: Tm (thulium)
Tm_169 = Isotope("Tm-169",  69, 169, 168.9342179)

#  70: Yb (ytterbium)
Yb_168 = Isotope("Yb-168",  70, 168, 167.9338896)
Yb_170 = Isotope("Yb-170",  70, 170, 169.9347664)
Yb_171 = Isotope("Yb-171",  70, 171, 170.9363302)
Yb_172 = Isotope("Yb-172",  70, 172, 171.9363859)
Yb_173 = Isotope("Yb-173",  70, 173, 172.9382151)
Yb_174 = Isotope("Yb-174",  70, 174, 173.9388664)
Yb_176 = Isotope("Yb-176",  70, 176, 175.9425764)

#  71: Lu (lutetium)
Lu_175 = Isotope("Lu-175",  71, 175, 174.9407752)
Lu_176 = Isotope("Lu-176",  71, 176, 175.9426897)

#  72: Hf (hafnium)
Hf_174 = Isotope("Hf-174",  72, 174, 173.9400461)
Hf_176 = Isotope("Hf-176",  72, 176, 175.9414076)
Hf_177 = Isotope("Hf-177",  72, 177, 176.9432277)
Hf_178 = Isotope("Hf-178",  72, 178, 177.9437058)
Hf_179 = Isotope("Hf-179",  72, 179, 178.9458232)
Hf_180 = Isotope("Hf-180",  72, 180, 179.946557)

#  73: Ta (tantalum)
Ta_180 = Isotope("Ta-180",  73, 180, 179.9474648)
Ta_181 = Isotope("Ta-181",  73, 181, 180.9479958)

#  74: W  (tungsten)
W_180  = Isotope("W-180" ,  74, 180, 179.9467108)
W_182  = Isotope("W-182" ,  74, 182, 181.94820394)
W_183  = Isotope("W-183" ,  74, 183, 182.95022275)
W_184  = Isotope("W-184" ,  74, 184, 183.95093092)
W_186  = Isotope("W-186" ,  74, 186, 185.9543628)

#  75: Re (rhenium)
Re_185 = Isotope("Re-185",  75, 185, 184.9529545)
Re_187 = Isotope("Re-187",  75, 187, 186.9557501)

#  76: Os (osmium)
Os_184 = Isotope("Os-184",  76, 184, 183.9524885)
Os_186 = Isotope("Os-186",  76, 186, 185.953835)
Os_187 = Isotope("Os-187",  76, 187, 186.9557474)
Os_188 = Isotope("Os-188",  76, 188, 187.9558352)
Os_189 = Isotope("Os-189",  76, 189, 188.9581442)
Os_190 = Isotope("Os-190",  76, 190, 189.9584437)
Os_192 = Isotope("Os-192",  76, 192, 191.961477)

#  77: Ir (iridium)
Ir_191 = Isotope("Ir-191",  77, 191, 190.9605893)
Ir_193 = Isotope("Ir-193",  77, 193, 192.9629216)

#  78: Pt (platinum)
Pt_190 = Isotope("Pt-190",  78, 190, 189.9599297)
Pt_192 = Isotope("Pt-192",  78, 192, 191.9610387)
Pt_194 = Isotope("Pt-194",  78, 194, 193.9626809)
Pt_195 = Isotope("Pt-195",  78, 195, 194.9647917)
Pt_196 = Isotope("Pt-196",  78, 196, 195.96495209)
Pt_198 = Isotope("Pt-198",  78, 198, 197.9678949)

#  79: Au (gold)
Au_197 = Isotope("Au-197",  79, 197, 196.96656879)

#  80: Hg (mercury)
Hg_196 = Isotope("Hg-196",  80, 196, 195.9658326)
Hg_198 = Isotope("Hg-198",  80, 198, 197.9667686)
Hg_199 = Isotope("Hg-199",  80, 199, 198.96828064)
Hg_200 = Isotope("Hg-200",  80, 200, 199.96832659)
Hg_201 = Isotope("Hg-201",  80, 201, 200.97030284)
Hg_202 = Isotope("Hg-202",  80, 202, 201.9706434)
Hg_204 = Isotope("Hg-204",  80, 204, 203.97349398)

#  81: Tl (thallium)
Tl_203 = Isotope("Tl-203",  81, 203, 202.9723446)
Tl_205 = Isotope("Tl-205",  81, 205, 204.9744278)

#  82: Pb (lead)
Pb_204 = Isotope("Pb-204",  82, 204, 203.973044)
Pb_206 = Isotope("Pb-206",  82, 206, 205.9744657)
Pb_207 = Isotope("Pb-207",  82, 207, 206.9758973)
Pb_208 = Isotope("Pb-208",  82, 208, 207.9766525)

#  83: Bi (bismuth)
Bi_209 = Isotope("Bi-209",  83, 209, 208.9803991)

#  84: Po (polonium)
Po_209 = Isotope("Po-209",  84, 209, 208.9824308)
Po_210 = Isotope("Po-210",  84, 210, 209.9828741)

#  85: At (astatine)
At_210 = Isotope("At-210",  85, 210, 209.9871479)
At_211 = Isotope("At-211",  85, 211, 210.9874966)

#  86: Rn (radon)
Rn_211 = Isotope("Rn-211",  86, 211, 210.9906011)
Rn_220 = Isotope("Rn-220",  86, 220, 220.0113941)
Rn_222 = Isotope("Rn-222",  86, 222, 222.0175782)

#  87: Fr (francium)
Fr_223 = Isotope("Fr-223",  87, 223, 223.019736)

#  88: Ra (radium)
Ra_223 = Isotope("Ra-223",  88, 223, 223.0185023)
Ra_224 = Isotope("Ra-224",  88, 224, 224.020212)
Ra_226 = Isotope("Ra-226",  88, 226, 226.0254103)
Ra_228 = Isotope("Ra-228",  88, 228, 228.0310707)

#  89: Ac (actinium)
Ac_227 = Isotope("Ac-227",  89, 227, 227.0277523)

#  90: Th (thorium)
Th_230 = Isotope("Th-230",  90, 230, 230.0331341)
Th_232 = Isotope("Th-232",  90, 232, 232.0380558)

#  91: Pa (protactinium)
Pa_231 = Isotope("Pa-231",  91, 231, 231.0358842)

#  92: U  (uranium)
U_233  = Isotope("U-233" ,  92, 233, 233.0396355)
U_234  = Isotope("U-234" ,  92, 234, 234.0409523)
U_235  = Isotope("U-235" ,  92, 235, 235.0439301)
U_236  = Isotope("U-236" ,  92, 236, 236.0455682)
U_238  = Isotope("U-238" ,  92, 238, 238.0507884)

#  93: Np (neptunium)
Np_236 = Isotope("Np-236",  93, 236, 236.04657)
Np_237 = Isotope("Np-237",  93, 237, 237.0481736)

#  94: Pu (plutonium)
Pu_238 = Isotope("Pu-238",  94, 238, 238.0495601)
Pu_239 = Isotope("Pu-239",  94, 239, 239.0521636)
Pu_240 = Isotope("Pu-240",  94, 240, 240.0538138)
Pu_241 = Isotope("Pu-241",  94, 241, 241.0568517)
Pu_242 = Isotope("Pu-242",  94, 242, 242.0587428)
Pu_244 = Isotope("Pu-244",  94, 244, 244.0642053)

#  95: Am (americium)
Am_241 = Isotope("Am-241",  95, 241, 241.0568293)
Am_243 = Isotope("Am-243",  95, 243, 243.0613813)

#  96: Cm (curium)
Cm_243 = Isotope("Cm-243",  96, 243, 243.0613893)
Cm_244 = Isotope("Cm-244",  96, 244, 244.0627528)
Cm_245 = Isotope("Cm-245",  96, 245, 245.0654915)
Cm_246 = Isotope("Cm-246",  96, 246, 246.0672238)
Cm_247 = Isotope("Cm-247",  96, 247, 247.0703541)
Cm_248 = Isotope("Cm-248",  96, 248, 248.0723499)

#  97: Bk (berkelium)
Bk_247 = Isotope("Bk-247",  97, 247, 247.0703073)
Bk_249 = Isotope("Bk-249",  97, 249, 249.0749877)

#  98: Cf (californium)
Cf_249 = Isotope("Cf-249",  98, 249, 249.0748539)
Cf_250 = Isotope("Cf-250",  98, 250, 250.0764062)
Cf_251 = Isotope("Cf-251",  98, 251, 251.0795886)
Cf_252 = Isotope("Cf-252",  98, 252, 252.0816272)

#  99: Es (einsteinium)
Es_252 = Isotope("Es-252",  99, 252, 252.08298)

# 100: Fm (fermium)
Fm_257 = Isotope("Fm-257", 100, 257, 257.0951061)

# 101: Md (mendelevium)
Md_258 = Isotope("Md-258", 101, 258, 258.0984315)
Md_260 = Isotope("Md-260", 101, 260, 260.10365)

# 102: No (nobelium)
No_259 = Isotope("No-259", 102, 259, 259.10103)

# 103: Lr (lawrencium)
Lr_262 = Isotope("Lr-262", 103, 262, 262.10961)

# 104: Rf (rutherfordium)
Rf_267 = Isotope("Rf-267", 104, 267, 267.12179)

# 105: Db (dubnium)
Db_268 = Isotope("Db-268", 105, 268, 268.12567)

# 106: Sg (seaborgium)
Sg_271 = Isotope("Sg-271", 106, 271, 271.13393)

# 107: Bh (bohrium)
Bh_272 = Isotope("Bh-272", 107, 272, 272.13826)

# 108: Hs (hassium)
Hs_270 = Isotope("Hs-270", 108, 270, 270.13429)

# 109: Mt (meitnerium)
Mt_276 = Isotope("Mt-276", 109, 276, 276.15159)

# 110: Ds (darmstadtium)
Ds_281 = Isotope("Ds-281", 110, 281, 281.16451)

# 111: Rg (roentgenium)
Rg_280 = Isotope("Rg-280", 111, 280, 280.16514)

# 112: Cn (copernicium)
Cn_285 = Isotope("Cn-285", 112, 285, 285.17712)

# 113: Nh (nihonium)
Nh_284 = Isotope("Nh-284", 113, 284, 284.17873)

# 114: Fl (flerovium)
Fl_289 = Isotope("Fl-289", 114, 289, 289.19042)

# 115: Mc (moscovium)
Mc_288 = Isotope("Mc-288", 115, 288, 288.19274)

# 116: Lv (livermorium)
Lv_293 = Isotope("Lv-293", 116, 293, 293.20449)

# 117: Ts (tennessine)
Ts_292 = Isotope("Ts-292", 117, 292, 292.20746)

# 118: Og (oganesson)
Og_294 = Isotope("Og-294", 118, 294, 294.21392)
