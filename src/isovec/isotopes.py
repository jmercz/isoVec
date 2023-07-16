# module with all isotopes

from .isotope import Isotope


#   1: H  (hydrogen)
H_1    = Isotope(  1,   1, 1.00782503223)
H      = Isotope(  1,   1, 1.00782503223, name="H")  # alias
H_2    = Isotope(  1,   2, 2.01410177812)
D      = Isotope(  1,   2, 2.01410177812, name="D")  # alias
H_3    = Isotope(  1,   3, 3.0160492779)
T      = Isotope(  1,   3, 3.0160492779, name="T")   # alias

#   2: He (helium)
He_3   = Isotope(  2,   3, 3.0160293201)
He_4   = Isotope(  2,   4, 4.00260325413)

#   3: Li (lithium)
Li_6   = Isotope(  3,   6, 6.0151228874)
Li_7   = Isotope(  3,   7, 7.0160034366)

#   4: Be (berylium)
Be_9   = Isotope(  4,   9, 9.012183065)

#   5: B  (boron)
B_10   = Isotope(  5,  10, 10.01293695)
B_11   = Isotope(  5,  11, 11.00930536)

#   6: C  (carbon)
C_12   = Isotope(  6,  12, 12.0)
C_13   = Isotope(  6,  13, 13.00335483507)
C_14   = Isotope(  6,  14, 14.0032419884)

#   7: N  (nitrogen)
N_14   = Isotope(  7,  14, 14.00307400443)
N_15   = Isotope(  7,  15, 15.00010889888)

#   8: O  (oxygen)
O_16   = Isotope(  8,  16, 15.99491461957)
O_17   = Isotope(  8,  17, 16.9991317565)
O_18   = Isotope(  8,  18, 17.99915961286)

#   9: F  (fluorine)
F_19   = Isotope(  9,  19, 18.99840316273)

#  10: Ne (neon)
Ne_20  = Isotope( 10,  20, 19.9924401762)
Ne_21  = Isotope( 10,  21, 20.993846685)
Ne_22  = Isotope( 10,  22, 21.991385114)

#  11: Na (sodium)
Na_23  = Isotope( 11,  23, 22.989769282)

#  12: Mg (magnesium)
Mg_24  = Isotope( 12,  24, 23.985041697)
Mg_25  = Isotope( 12,  25, 24.985836976)
Mg_26  = Isotope( 12,  26, 25.982592968)

#  13: Al (aluminium)
Al_27  = Isotope( 13,  27, 26.98153853)

#  14: Si (silicon)
Si_28  = Isotope( 14,  28, 27.97692653465)
Si_29  = Isotope( 14,  29, 28.9764946649)
Si_30  = Isotope( 14,  30, 29.973770136)

#  15: P  (phosphorus)
P_31   = Isotope( 15,  31, 30.97376199842)

#  16: S  (sulphur)
S_32   = Isotope( 16,  32, 31.9720711744)
S_33   = Isotope( 16,  33, 32.9714589098)
S_34   = Isotope( 16,  34, 33.967867004)
S_36   = Isotope( 16,  36, 35.96708071)

#  17: Cl (chlorine)
Cl_35  = Isotope( 17,  35, 34.968852682)
Cl_37  = Isotope( 17,  37, 36.965902602)

#  18: Ar (argon)
Ar_36  = Isotope( 18,  36, 35.967545105)
Ar_38  = Isotope( 18,  38, 37.96273211)
Ar_40  = Isotope( 18,  40, 39.9623831237)

#  19: K  (potassium)
K_39   = Isotope( 19,  39, 38.9637064864)
K_40   = Isotope( 19,  40, 39.963998166)
K_41   = Isotope( 19,  41, 40.9618252579)

#  20: Ca (calcium)
Ca_40  = Isotope( 20,  40, 39.962590863)
Ca_42  = Isotope( 20,  42, 41.95861783)
Ca_43  = Isotope( 20,  43, 42.95876644)
Ca_44  = Isotope( 20,  44, 43.95548156)
Ca_46  = Isotope( 20,  46, 45.953689)
Ca_48  = Isotope( 20,  48, 47.95252276)

#  21: Sc (scandium)
Sc_45  = Isotope( 21,  45, 44.95590828)

#  22: Ti (titanium)
Ti_46  = Isotope( 22,  46, 45.95262772)
Ti_47  = Isotope( 22,  47, 46.95175879)
Ti_48  = Isotope( 22,  48, 47.94794198)
Ti_49  = Isotope( 22,  49, 48.94786568)
Ti_50  = Isotope( 22,  50, 49.94478689)

#  23: V  (vanadium)
V_50   = Isotope( 23,  50, 49.94715601)
V_51   = Isotope( 23,  51, 50.94395704)

#  24: Cr (chromium)
Cr_50  = Isotope( 24,  50, 49.94604183)
Cr_52  = Isotope( 24,  52, 51.94050623)
Cr_53  = Isotope( 24,  53, 52.94064815)
Cr_54  = Isotope( 24,  54, 53.93887916)

#  25: Mn (manganese)
Mn_55  = Isotope( 25,  55, 54.93804391)

#  26: Fe (iron)
Fe_54  = Isotope( 26,  54, 53.93960899)
Fe_56  = Isotope( 26,  56, 55.93493633)
Fe_57  = Isotope( 26,  57, 56.93539284)
Fe_58  = Isotope( 26,  58, 57.93327443)

#  27: Co (cobalt)
Co_59  = Isotope( 27,  59, 58.93319429)

#  28: Ni (nickel)
Ni_58  = Isotope( 28,  58, 57.93534241)
Ni_60  = Isotope( 28,  60, 59.93078588)
Ni_61  = Isotope( 28,  61, 60.93105557)
Ni_62  = Isotope( 28,  62, 61.92834537)
Ni_64  = Isotope( 28,  64, 63.92796682)

#  29: Cu (copper)
Cu_63  = Isotope( 29,  63, 62.92959772)
Cu_65  = Isotope( 29,  65, 64.9277897)

#  30: Zn (zinc)
Zn_64  = Isotope( 30,  64, 63.92914201)
Zn_66  = Isotope( 30,  66, 65.92603381)
Zn_67  = Isotope( 30,  67, 66.92712775)
Zn_68  = Isotope( 30,  68, 67.92484455)
Zn_70  = Isotope( 30,  70, 69.9253192)

#  31: Ga (gallium)
Ga_69  = Isotope( 31,  69, 68.9255735)
Ga_71  = Isotope( 31,  71, 70.92470258)

#  32: Ge (germanium)
Ge_70  = Isotope( 32,  70, 69.92424875)
Ge_72  = Isotope( 32,  72, 71.922075826)
Ge_73  = Isotope( 32,  73, 72.923458956)
Ge_74  = Isotope( 32,  74, 73.921177761)
Ge_76  = Isotope( 32,  76, 75.921402726)

#  33: As (arsenic)
As_75  = Isotope( 33,  75, 74.92159457)

#  34: Se (selenium)
Se_74  = Isotope( 34,  74, 73.922475934)
Se_76  = Isotope( 34,  76, 75.919213704)
Se_77  = Isotope( 34,  77, 76.919914154)
Se_78  = Isotope( 34,  78, 77.91730928)
Se_80  = Isotope( 34,  80, 79.9165218)
Se_82  = Isotope( 34,  82, 81.9166995)

#  35: Br (bromine)
Br_79  = Isotope( 35,  79, 78.9183376)
Br_81  = Isotope( 35,  81, 80.9162897)

#  36: Kr (krypton)
Kr_78  = Isotope( 36,  78, 77.92036494)
Kr_80  = Isotope( 36,  80, 79.91637808)
Kr_82  = Isotope( 36,  82, 81.91348273)
Kr_83  = Isotope( 36,  83, 82.91412716)
Kr_84  = Isotope( 36,  84, 83.9114977282)
Kr_86  = Isotope( 36,  86, 85.9106106269)

#  37: Rb (rubidium)
Rb_85  = Isotope( 37,  85, 84.9117897379)
Rb_87  = Isotope( 37,  87, 86.909180531)

#  38: Sr (strontium)
Sr_84  = Isotope( 38,  84, 83.9134191)
Sr_86  = Isotope( 38,  86, 85.9092606)
Sr_87  = Isotope( 38,  87, 86.9088775)
Sr_88  = Isotope( 38,  88, 87.9056125)

#  39: Y  (yttrium)
Y_89   = Isotope( 39,  89, 88.9058403)

#  40: Zr (zirconium)
Zr_90  = Isotope( 40,  90, 89.9046977)
Zr_91  = Isotope( 40,  91, 90.9056396)
Zr_92  = Isotope( 40,  92, 91.9050347)
Zr_94  = Isotope( 40,  94, 93.9063108)
Zr_96  = Isotope( 40,  96, 95.9082714)

#  41: Nb (niobium)
Nb_93  = Isotope( 41,  93, 92.906373)

#  42: Mo (molybdenum)
Mo_92  = Isotope( 42,  92, 91.90680796)
Mo_94  = Isotope( 42,  94, 93.9050849)
Mo_95  = Isotope( 42,  95, 94.90583877)
Mo_96  = Isotope( 42,  96, 95.90467612)
Mo_97  = Isotope( 42,  97, 96.90601812)
Mo_98  = Isotope( 42,  98, 97.90540482)
Mo_100 = Isotope( 42, 100, 99.9074718)

#  43: Tc (technetium)
Tc_97  = Isotope( 43,  97, 96.9063667)
Tc_98  = Isotope( 43,  98, 97.9072124)
Tc_99  = Isotope( 43,  99, 98.9062508)

#  44: Ru (ruthenium)
Ru_96  = Isotope( 44,  96, 95.90759025)
Ru_98  = Isotope( 44,  98, 97.9052868)
Ru_99  = Isotope( 44,  99, 98.9059341)
Ru_100 = Isotope( 44, 100, 99.9042143)
Ru_101 = Isotope( 44, 101, 100.9055769)
Ru_102 = Isotope( 44, 102, 101.9043441)
Ru_104 = Isotope( 44, 104, 103.9054275)

#  45: Rh (rhodium)
Rh_103 = Isotope( 45, 103, 102.905498)

#  46: Pd (palladium)
Pd_102 = Isotope( 46, 102, 101.9056022)
Pd_104 = Isotope( 46, 104, 103.9040305)
Pd_105 = Isotope( 46, 105, 104.9050796)
Pd_106 = Isotope( 46, 106, 105.9034804)
Pd_108 = Isotope( 46, 108, 107.9038916)
Pd_110 = Isotope( 46, 110, 109.9051722)

#  47: Ag (silver)
Ag_107 = Isotope( 47, 107, 106.9050916)
Ag_109 = Isotope( 47, 109, 108.9047553)

#  48: Cd (cadmium)
Cd_106 = Isotope( 48, 106, 105.9064599)
Cd_108 = Isotope( 48, 108, 107.9041834)
Cd_110 = Isotope( 48, 110, 109.90300661)
Cd_111 = Isotope( 48, 111, 110.90418287)
Cd_112 = Isotope( 48, 112, 111.90276287)
Cd_113 = Isotope( 48, 113, 112.90440813)
Cd_114 = Isotope( 48, 114, 113.90336509)
Cd_116 = Isotope( 48, 116, 115.90476315)

#  49: In (indium)
In_113 = Isotope( 49, 113, 112.90406184)
In_115 = Isotope( 49, 115, 114.903878776)

#  50: Sn (tin)
Sn_112 = Isotope( 50, 112, 111.90482387)
Sn_114 = Isotope( 50, 114, 113.9027827)
Sn_115 = Isotope( 50, 115, 114.903344699)
Sn_116 = Isotope( 50, 116, 115.9017428)
Sn_117 = Isotope( 50, 117, 116.90295398)
Sn_118 = Isotope( 50, 118, 117.90160657)
Sn_119 = Isotope( 50, 119, 118.90331117)
Sn_120 = Isotope( 50, 120, 119.90220163)
Sn_122 = Isotope( 50, 122, 121.9034438)
Sn_124 = Isotope( 50, 124, 123.9052766)

#  51: Sb (antimony)
Sb_121 = Isotope( 51, 121, 120.903812)
Sb_123 = Isotope( 51, 123, 122.9042132)

#  52: Te (tellurium)
Te_120 = Isotope( 52, 120, 119.9040593)
Te_122 = Isotope( 52, 122, 121.9030435)
Te_123 = Isotope( 52, 123, 122.9042698)
Te_124 = Isotope( 52, 124, 123.9028171)
Te_125 = Isotope( 52, 125, 124.9044299)
Te_126 = Isotope( 52, 126, 125.9033109)
Te_128 = Isotope( 52, 128, 127.90446128)
Te_130 = Isotope( 52, 130, 129.906222748)

#  53: I  (iodine)
I_127  = Isotope( 53, 127, 126.9044719)

#  54: Xe (xenon)
Xe_124 = Isotope( 54, 124, 123.905892)
Xe_126 = Isotope( 54, 126, 125.9042983)
Xe_128 = Isotope( 54, 128, 127.903531)
Xe_129 = Isotope( 54, 129, 128.9047808611)
Xe_130 = Isotope( 54, 130, 129.903509349)
Xe_131 = Isotope( 54, 131, 130.90508406)
Xe_132 = Isotope( 54, 132, 131.9041550856)
Xe_134 = Isotope( 54, 134, 133.90539466)
Xe_136 = Isotope( 54, 136, 135.907214484)

#  55: Cs (caesium)
Cs_133 = Isotope( 55, 133, 132.905451961)

#  56: Ba (barium)
Ba_130 = Isotope( 56, 130, 129.9063207)
Ba_132 = Isotope( 56, 132, 131.9050611)
Ba_134 = Isotope( 56, 134, 133.90450818)
Ba_135 = Isotope( 56, 135, 134.90568838)
Ba_136 = Isotope( 56, 136, 135.90457573)
Ba_137 = Isotope( 56, 137, 136.90582714)
Ba_138 = Isotope( 56, 138, 137.905247)

#  57: La (lanthanum)
La_138 = Isotope( 57, 138, 137.9071149)
La_139 = Isotope( 57, 139, 138.9063563)

#  58: Ce (cerium)
Ce_136 = Isotope( 58, 136, 135.90712921)
Ce_138 = Isotope( 58, 138, 137.905991)
Ce_140 = Isotope( 58, 140, 139.9054431)
Ce_142 = Isotope( 58, 142, 141.9092504)

#  59: Pr (praseodymium)
Pr_141 = Isotope( 59, 141, 140.9076576)

#  60: Nd (neodymium)
Nd_142 = Isotope( 60, 142, 141.907729)
Nd_143 = Isotope( 60, 143, 142.90982)
Nd_144 = Isotope( 60, 144, 143.910093)
Nd_145 = Isotope( 60, 145, 144.9125793)
Nd_146 = Isotope( 60, 146, 145.9131226)
Nd_148 = Isotope( 60, 148, 147.9168993)
Nd_150 = Isotope( 60, 150, 149.9209022)

#  61: Pm (promethium)
Pm_145 = Isotope( 61, 145, 144.9127559)
Pm_147 = Isotope( 61, 147, 146.915145)

#  62: Sm (samarium)
Sm_144 = Isotope( 62, 144, 143.9120065)
Sm_147 = Isotope( 62, 147, 146.9149044)
Sm_148 = Isotope( 62, 148, 147.9148292)
Sm_149 = Isotope( 62, 149, 148.9171921)
Sm_150 = Isotope( 62, 150, 149.9172829)
Sm_152 = Isotope( 62, 152, 151.9197397)
Sm_154 = Isotope( 62, 154, 153.9222169)

#  63: Eu (europium)
Eu_151 = Isotope( 63, 151, 150.9198578)
Eu_153 = Isotope( 63, 153, 152.921238)

#  64: Gd (gadolinium)
Gd_152 = Isotope( 64, 152, 151.9197995)
Gd_154 = Isotope( 64, 154, 153.9208741)
Gd_155 = Isotope( 64, 155, 154.9226305)
Gd_156 = Isotope( 64, 156, 155.9221312)
Gd_157 = Isotope( 64, 157, 156.9239686)
Gd_158 = Isotope( 64, 158, 157.9241123)
Gd_160 = Isotope( 64, 160, 159.9270624)

#  65: Tb (terbium)
Tb_159 = Isotope( 65, 159, 158.9253547)

#  66: Dy (dysprosium)
Dy_156 = Isotope( 66, 156, 155.9242847)
Dy_158 = Isotope( 66, 158, 157.9244159)
Dy_160 = Isotope( 66, 160, 159.9252046)
Dy_161 = Isotope( 66, 161, 160.9269405)
Dy_162 = Isotope( 66, 162, 161.9268056)
Dy_163 = Isotope( 66, 163, 162.9287383)
Dy_164 = Isotope( 66, 164, 163.9291819)

#  67: Ho (holmium)
Ho_165 = Isotope( 67, 165, 164.9303288)

#  68: Er (erbium)
Er_162 = Isotope( 68, 162, 161.9287884)
Er_164 = Isotope( 68, 164, 163.9292088)
Er_166 = Isotope( 68, 166, 165.9302995)
Er_167 = Isotope( 68, 167, 166.9320546)
Er_168 = Isotope( 68, 168, 167.9323767)
Er_170 = Isotope( 68, 170, 169.9354702)

#  69: Tm (thulium)
Tm_169 = Isotope( 69, 169, 168.9342179)

#  70: Yb (ytterbium)
Yb_168 = Isotope( 70, 168, 167.9338896)
Yb_170 = Isotope( 70, 170, 169.9347664)
Yb_171 = Isotope( 70, 171, 170.9363302)
Yb_172 = Isotope( 70, 172, 171.9363859)
Yb_173 = Isotope( 70, 173, 172.9382151)
Yb_174 = Isotope( 70, 174, 173.9388664)
Yb_176 = Isotope( 70, 176, 175.9425764)

#  71: Lu (lutetium)
Lu_175 = Isotope( 71, 175, 174.9407752)
Lu_176 = Isotope( 71, 176, 175.9426897)

#  72: Hf (hafnium)
Hf_174 = Isotope( 72, 174, 173.9400461)
Hf_176 = Isotope( 72, 176, 175.9414076)
Hf_177 = Isotope( 72, 177, 176.9432277)
Hf_178 = Isotope( 72, 178, 177.9437058)
Hf_179 = Isotope( 72, 179, 178.9458232)
Hf_180 = Isotope( 72, 180, 179.946557)

#  73: Ta (tantalum)
Ta_180 = Isotope( 73, 180, 179.9474648)
Ta_181 = Isotope( 73, 181, 180.9479958)

#  74: W  (tungsten)
W_180  = Isotope( 74, 180, 179.9467108)
W_182  = Isotope( 74, 182, 181.94820394)
W_183  = Isotope( 74, 183, 182.95022275)
W_184  = Isotope( 74, 184, 183.95093092)
W_186  = Isotope( 74, 186, 185.9543628)

#  75: Re (rhenium)
Re_185 = Isotope( 75, 185, 184.9529545)
Re_187 = Isotope( 75, 187, 186.9557501)

#  76: Os (osmium)
Os_184 = Isotope( 76, 184, 183.9524885)
Os_186 = Isotope( 76, 186, 185.953835)
Os_187 = Isotope( 76, 187, 186.9557474)
Os_188 = Isotope( 76, 188, 187.9558352)
Os_189 = Isotope( 76, 189, 188.9581442)
Os_190 = Isotope( 76, 190, 189.9584437)
Os_192 = Isotope( 76, 192, 191.961477)

#  77: Ir (iridium)
Ir_191 = Isotope( 77, 191, 190.9605893)
Ir_193 = Isotope( 77, 193, 192.9629216)

#  78: Pt (platinum)
Pt_190 = Isotope( 78, 190, 189.9599297)
Pt_192 = Isotope( 78, 192, 191.9610387)
Pt_194 = Isotope( 78, 194, 193.9626809)
Pt_195 = Isotope( 78, 195, 194.9647917)
Pt_196 = Isotope( 78, 196, 195.96495209)
Pt_198 = Isotope( 78, 198, 197.9678949)

#  79: Au (gold)
Au_197 = Isotope( 79, 197, 196.96656879)

#  80: Hg (mercury)
Hg_196 = Isotope( 80, 196, 195.9658326)
Hg_198 = Isotope( 80, 198, 197.9667686)
Hg_199 = Isotope( 80, 199, 198.96828064)
Hg_200 = Isotope( 80, 200, 199.96832659)
Hg_201 = Isotope( 80, 201, 200.97030284)
Hg_202 = Isotope( 80, 202, 201.9706434)
Hg_204 = Isotope( 80, 204, 203.97349398)

#  81: Tl (thallium)
Tl_203 = Isotope( 81, 203, 202.9723446)
Tl_205 = Isotope( 81, 205, 204.9744278)

#  82: Pb (lead)
Pb_204 = Isotope( 82, 204, 203.973044)
Pb_206 = Isotope( 82, 206, 205.9744657)
Pb_207 = Isotope( 82, 207, 206.9758973)
Pb_208 = Isotope( 82, 208, 207.9766525)

#  83: Bi (bismuth)
Bi_209 = Isotope( 83, 209, 208.9803991)

#  84: Po (polonium)
Po_209 = Isotope( 84, 209, 208.9824308)
Po_210 = Isotope( 84, 210, 209.9828741)

#  85: At (astatine)
At_210 = Isotope( 85, 210, 209.9871479)
At_211 = Isotope( 85, 211, 210.9874966)

#  86: Rn (radon)
Rn_211 = Isotope( 86, 211, 210.9906011)
Rn_220 = Isotope( 86, 220, 220.0113941)
Rn_222 = Isotope( 86, 222, 222.0175782)

#  87: Fr (francium)
Fr_223 = Isotope( 87, 223, 223.019736)

#  88: Ra (radium)
Ra_223 = Isotope( 88, 223, 223.0185023)
Ra_224 = Isotope( 88, 224, 224.020212)
Ra_226 = Isotope( 88, 226, 226.0254103)
Ra_228 = Isotope( 88, 228, 228.0310707)

#  89: Ac (actinium)
Ac_227 = Isotope( 89, 227, 227.0277523)

#  90: Th (thorium)
Th_230 = Isotope( 90, 230, 230.0331341)
Th_232 = Isotope( 90, 232, 232.0380558)

#  91: Pa (protactinium)
Pa_231 = Isotope( 91, 231, 231.0358842)

#  92: U  (uranium)
U_233  = Isotope( 92, 233, 233.0396355)
U_234  = Isotope( 92, 234, 234.0409523)
U_235  = Isotope( 92, 235, 235.0439301)
U_236  = Isotope( 92, 236, 236.0455682)
U_238  = Isotope( 92, 238, 238.0507884)

#  93: Np (neptunium)
Np_236 = Isotope( 93, 236, 236.04657)
Np_237 = Isotope( 93, 237, 237.0481736)

#  94: Pu (plutonium)
Pu_238 = Isotope( 94, 238, 238.0495601)
Pu_239 = Isotope( 94, 239, 239.0521636)
Pu_240 = Isotope( 94, 240, 240.0538138)
Pu_241 = Isotope( 94, 241, 241.0568517)
Pu_242 = Isotope( 94, 242, 242.0587428)
Pu_244 = Isotope( 94, 244, 244.0642053)

#  95: Am (americium)
Am_241 = Isotope( 95, 241, 241.0568293)
Am_243 = Isotope( 95, 243, 243.0613813)

#  96: Cm (curium)
Cm_243 = Isotope( 96, 243, 243.0613893)
Cm_244 = Isotope( 96, 244, 244.0627528)
Cm_245 = Isotope( 96, 245, 245.0654915)
Cm_246 = Isotope( 96, 246, 246.0672238)
Cm_247 = Isotope( 96, 247, 247.0703541)
Cm_248 = Isotope( 96, 248, 248.0723499)

#  97: Bk (berkelium)
Bk_247 = Isotope( 97, 247, 247.0703073)
Bk_249 = Isotope( 97, 249, 249.0749877)

#  98: Cf (californium)
Cf_249 = Isotope( 98, 249, 249.0748539)
Cf_250 = Isotope( 98, 250, 250.0764062)
Cf_251 = Isotope( 98, 251, 251.0795886)
Cf_252 = Isotope( 98, 252, 252.0816272)

#  99: Es (einsteinium)
Es_252 = Isotope( 99, 252, 252.08298)

# 100: Fm (fermium)
Fm_257 = Isotope( 100, 257, 257.0951061)

# 101: Md (mendelevium)
Md_258 = Isotope(101, 258, 258.0984315)
Md_260 = Isotope(101, 260, 260.10365)

# 102: No (nobelium)
No_259 = Isotope(102, 259, 259.10103)

# 103: Lr (lawrencium)
Lr_262 = Isotope(103, 262, 262.10961)

# 104: Rf (rutherfordium)
Rf_267 = Isotope(104, 267, 267.12179)

# 105: Db (dubnium)
Db_268 = Isotope(105, 268, 268.12567)

# 106: Sg (seaborgium)
Sg_271 = Isotope(106, 271, 271.13393)

# 107: Bh (bohrium)
Bh_272 = Isotope(107, 272, 272.13826)

# 108: Hs (hassium)
Hs_270 = Isotope(108, 270, 270.13429)

# 109: Mt (meitnerium)
Mt_276 = Isotope(109, 276, 276.15159)

# 110: Ds (darmstadtium)
Ds_281 = Isotope(110, 281, 281.16451)

# 111: Rg (roentgenium)
Rg_280 = Isotope(111, 280, 280.16514)

# 112: Cn (copernicium)
Cn_285 = Isotope(112, 285, 285.17712)

# 113: Nh (nihonium)
Nh_284 = Isotope(113, 284, 284.17873)

# 114: Fl (flerovium)
Fl_289 = Isotope(114, 289, 289.19042)

# 115: Mc (moscovium)
Mc_288 = Isotope(115, 288, 288.19274)

# 116: Lv (livermorium)
Lv_293 = Isotope(116, 293, 293.20449)

# 117: Ts (tennessine)
Ts_292 = Isotope(117, 292, 292.20746)

# 118: Og (oganesson)
Og_294 = Isotope(118, 294, 294.21392)
