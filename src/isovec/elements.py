# module for element symbols and names and natural elements

from .element import Element
from .isotopes import *


# ################
# natural elements
# ################

#   1: H  (hydrogen)
H_nat = Element("natural hydrogen", {
    H_1:    9.9988500E-01,
    H_2:    1.1500000E-04
}, natural=True)

#   2: He (helium)
He_nat = Element("natural helium", {
    He_3:   1.3400000E-06,
    He_4:   9.9999866E-01
}, natural=True)

#   3: Li (lithium)
Li_nat = Element("natural lithium", {
    Li_6:   7.5900000E-02,
    Li_7:   9.2410000E-01
}, natural=True)

#   4: Be (berylium)
Be_nat = Element("natural berylium", {
    Be_9:   1.0000000E+00
}, natural=True)

#   5: B  (boron)
B_nat = Element("natural boron", {
    B_10:   1.9900000E-01,
    B_11:   8.0100000E-01
}, natural=True)

#   6: C  (carbon)
C_nat = Element("natural carbon", {
    C_12:   9.8930000E-01,
    C_13:   1.0700000E-02
}, natural=True)

#   7: N  (nitrogen)
N_nat = Element("natural nitrogen", {
    N_14:   9.9636000E-01,
    N_15:   3.6400000E-03
}, natural=True)

#   8: O  (oxygen)
O_nat = Element("natural oxygen", {
    O_16:   9.9757000E-01,
    O_17:   3.8000000E-04,
    O_18:   2.0500000E-03
}, natural=True)

#   9: F  (fluorine)
F_nat = Element("natural fluorine", {
    F_19:   1.0000000E+00
}, natural=True)

#  10: Ne (neon)
Ne_nat = Element("natural neon", {
    Ne_20:  9.0480000E-01,
    Ne_21:  2.7000000E-03,
    Ne_22:  9.2500000E-02
}, natural=True)

#  11: Na (sodium)
Na_nat = Element("natural sodium", {
    Na_23:  1.0000000E+00
}, natural=True)

#  12: Mg (magnesium)
Mg_nat = Element("natural magnesium", {
    Mg_24:  7.8990000E-01,
    Mg_25:  1.0000000E-01,
    Mg_26:  1.1010000E-01
}, natural=True)

#  13: Al (aluminium)
Al_nat = Element("natural aluminium", {
    Al_27:  1.0000000E+00
}, natural=True)

#  14: Si (silicon)
Si_nat = Element("natural silicon", {
    Si_28:  9.2223000E-01,
    Si_29:  4.6850000E-02,
    Si_30:  3.0920000E-02
}, natural=True)

#  15: P  (phosphorus)
P_nat = Element("natural phosphorus", {
    P_31:   1.0000000E+00
}, natural=True)

#  16: S  (sulphur)
S_nat = Element("natural sulphur", {
    S_32:   9.4990000E-01,
    S_33:   7.5000000E-03,
    S_34:   4.2500000E-02,
    S_36:   1.0000000E-04
}, natural=True)

#  17: Cl (chlorine)
Cl_nat = Element("natural chlorine", {
    Cl_35:  7.5760000E-01,
    Cl_37:  2.4240000E-01
}, natural=True)

#  18: Ar (argon)
Ar_nat = Element("natural argon", {
    Ar_36:  3.3360000E-03,
    Ar_38:  6.2900000E-04,
    Ar_40:  9.9603500E-01
}, natural=True)

#  19: K  (potassium)
K_nat = Element("natural potassium", {
    K_39:   9.3258100E-01,
    K_40:   1.1700000E-04,
    K_41:   6.7302000E-02
}, natural=True)

#  20: Ca (calcium)
Ca_nat = Element("natural calcium", {
    Ca_40:  9.6941000E-01,
    Ca_42:  6.4700000E-03,
    Ca_43:  1.3500000E-03,
    Ca_44:  2.0860000E-02,
    Ca_46:  4.0000000E-05,
    Ca_48:  1.8700000E-03
}, natural=True)

#  21: Sc (scandium)
Sc_nat = Element("natural scandium", {
    Sc_45:  1.0000000E+00
}, natural=True)

#  22: Ti (titanium)
Ti_nat = Element("natural titanium", {
    Ti_46:  8.2500000E-02,
    Ti_47:  7.4400000E-02,
    Ti_48:  7.3720000E-01,
    Ti_49:  5.4100000E-02,
    Ti_50:  5.1800000E-02
}, natural=True)

#  23: V  (vanadium)
V_nat = Element("natural vanadium", {
    V_50:   2.5000000E-03,
    V_51:   9.9750000E-01
}, natural=True)

#  24: Cr (chromium)
Cr_nat = Element("natural chromium", {
    Cr_50:  4.3450000E-02,
    Cr_52:  8.3789000E-01,
    Cr_53:  9.5010000E-02,
    Cr_54:  2.3650000E-02
}, natural=True)

#  25: Mn (manganese)
Mn_nat = Element("natural manganese", {
    Mn_55:  1.0000000E+00
}, natural=True)

#  26: Fe (iron)
Fe_nat = Element("natural iron", {
    Fe_54:  5.8450000E-02,
    Fe_56:  9.1754000E-01,
    Fe_57:  2.1190000E-02,
    Fe_58:  2.8200000E-03
}, natural=True)

#  27: Co (cobalt)
Co_nat = Element("natural cobalt", {
    Co_59:  1.0000000E+00
}, natural=True)

#  28: Ni (nickel)
Ni_nat = Element("natural nickel", {
    Ni_58:  6.8077000E-01,
    Ni_60:  2.6223000E-01,
    Ni_61:  1.1399000E-02,
    Ni_62:  3.6346000E-02,
    Ni_64:  9.2550000E-03
}, natural=True)

#  29: Cu (copper)
Cu_nat = Element("natural copper", {
    Cu_63:  6.9150000E-01,
    Cu_65:  3.0850000E-01
}, natural=True)

#  30: Zn (zinc)
Zn_nat = Element("natural zinc", {
    Zn_64:  4.9170000E-01,
    Zn_66:  2.7730000E-01,
    Zn_67:  4.0400000E-02,
    Zn_68:  1.8450000E-01,
    Zn_70:  6.1000000E-03
}, natural=True)

#  31: Ga (gallium)
Ga_nat = Element("natural gallium", {
    Ga_69:  6.0108000E-01,
    Ga_71:  3.9892000E-01
}, natural=True)

#  32: Ge (germanium)
Ge_nat = Element("natural germanium", {
    Ge_70:  2.0570000E-01,
    Ge_72:  2.7450000E-01,
    Ge_73:  7.7500000E-02,
    Ge_74:  3.6500000E-01,
    Ge_76:  7.7300000E-02
}, natural=True)

#  33: As (arsenic)
As_nat = Element("natural arsenic", {
    As_75:  1.0000000E+00
}, natural=True)

#  34: Se (selenium)
Se_nat = Element("natural selenium", {
    Se_74:  8.9000000E-03,
    Se_76:  9.3700000E-02,
    Se_77:  7.6300000E-02,
    Se_78:  2.3770000E-01,
    Se_80:  4.9610000E-01,
    Se_82:  8.7300000E-02
}, natural=True)

#  35: Br (bromine)
Br_nat = Element("natural bromine", {
    Br_79:  5.0690000E-01,
    Br_81:  4.9310000E-01
}, natural=True)

#  36: Kr (krypton)
Kr_nat = Element("natural krypton", {
    Kr_78:  3.5500000E-03,
    Kr_80:  2.2860000E-02,
    Kr_82:  1.1593000E-01,
    Kr_83:  1.1500000E-01,
    Kr_84:  5.6987000E-01,
    Kr_86:  1.7279000E-01
}, natural=True)

#  37: Rb (rubidium)
Rb_nat = Element("natural rubidium", {
    Rb_85:  7.2170000E-01,
    Rb_87:  2.7830000E-01
}, natural=True)

#  38: Sr (strontium)
Sr_nat = Element("natural strontium", {
    Sr_84:  5.6000000E-03,
    Sr_86:  9.8600000E-02,
    Sr_87:  7.0000000E-02,
    Sr_88:  8.2580000E-01
}, natural=True)

#  39: Y  (yttrium)
Y_nat = Element("natural yttrium", {
    Y_89:   1.0000000E+00
}, natural=True)

#  40: Zr (zirconium)
Zr_nat = Element("natural zirconium", {
    Zr_90:  5.1450000E-01,
    Zr_91:  1.1220000E-01,
    Zr_92:  1.7150000E-01,
    Zr_94:  1.7380000E-01,
    Zr_96:  2.8000000E-02
}, natural=True)

#  41: Nb (niobium)
Nb_nat = Element("natural niobium", {
    Nb_93:  1.0000000E+00
}, natural=True)

#  42: Mo (molybdenum)
Mo_nat = Element("natural molybdenum", {
    Mo_92:  1.4530000E-01,
    Mo_94:  9.1500000E-02,
    Mo_95:  1.5840000E-01,
    Mo_96:  1.6670000E-01,
    Mo_97:  9.6000000E-02,
    Mo_98:  2.4390000E-01,
    Mo_100: 9.8200000E-02
}, natural=True)

#  43: Tc (technetium)
# not naturally occuring

#  44: Ru (ruthenium)
Ru_nat = Element("natural ruthenium", {
    Ru_96:  5.5400000E-02,
    Ru_98:  1.8700000E-02,
    Ru_99:  1.2760000E-01,
    Ru_100: 1.2600000E-01,
    Ru_101: 1.7060000E-01,
    Ru_102: 3.1550000E-01,
    Ru_104: 1.8620000E-01
}, natural=True)

#  45: Rh (rhodium)
Rh_nat = Element("natural rhodium", {
    Rh_103: 1.0000000E+00
}, natural=True)

#  46: Pd (palladium)
Pd_nat = Element("natural palladium", {
    Pd_102: 1.0200000E-02,
    Pd_104: 1.1140000E-01,
    Pd_105: 2.2330000E-01,
    Pd_106: 2.7330000E-01,
    Pd_108: 2.6460000E-01,
    Pd_110: 1.1720000E-01
}, natural=True)

#  47: Ag (silver)
Ag_nat = Element("natural silver", {
    Ag_107: 5.1839000E-01,
    Ag_109: 4.8161000E-01
}, natural=True)

#  48: Cd (cadmium)
Cd_nat = Element("natural cadmium", {
    Cd_106: 1.2500000E-02,
    Cd_108: 8.9000000E-03,
    Cd_110: 1.2490000E-01,
    Cd_111: 1.2800000E-01,
    Cd_112: 2.4130000E-01,
    Cd_113: 1.2220000E-01,
    Cd_114: 2.8730000E-01,
    Cd_116: 7.4900000E-02
}, natural=True)

#  49: In (indium)
In_nat = Element("natural indium", {
    In_113: 4.2900000E-02,
    In_115: 9.5710000E-01
}, natural=True)

#  50: Sn (tin)
Sn_nat = Element("natural tin", {
    Sn_112: 9.7000000E-03,
    Sn_114: 6.6000000E-03,
    Sn_115: 3.4000000E-03,
    Sn_116: 1.4540000E-01,
    Sn_117: 7.6800000E-02,
    Sn_118: 2.4220000E-01,
    Sn_119: 8.5900000E-02,
    Sn_120: 3.2580000E-01,
    Sn_122: 4.6300000E-02,
    Sn_124: 5.7900000E-02
}, natural=True)

#  51: Sb (antimony)
Sb_nat = Element("natural antimony", {
    Sb_121: 5.7210000E-01,
    Sb_123: 4.2790000E-01
}, natural=True)

#  52: Te (tellurium)
Te_nat = Element("natural tellurium", {
    Te_120: 9.0000000E-04,
    Te_122: 2.5500000E-02,
    Te_123: 8.9000000E-03,
    Te_124: 4.7400000E-02,
    Te_125: 7.0700000E-02,
    Te_126: 1.8840000E-01,
    Te_128: 3.1740000E-01,
    Te_130: 3.4080000E-01
}, natural=True)

#  53: I  (iodine)
I_nat = Element("natural iodine", {
    I_127:  1.0000000E+00
}, natural=True)

#  54: Xe (xenon)
Xe_nat = Element("natural xenon", {
    Xe_124: 9.5200000E-04,
    Xe_126: 8.9000000E-04,
    Xe_128: 1.9102000E-02,
    Xe_129: 2.6400600E-01,
    Xe_130: 4.0710000E-02,
    Xe_131: 2.1232400E-01,
    Xe_132: 2.6908600E-01,
    Xe_134: 1.0435700E-01,
    Xe_136: 8.8573000E-02
}, natural=True)

#  55: Cs (caesium)
Cs_nat = Element("natural caesium", {
    Cs_133: 1.0000000E+00
}, natural=True)

#  56: Ba (barium)
Ba_nat = Element("natural barium", {
    Ba_130: 1.0600000E-03,
    Ba_132: 1.0100000E-03,
    Ba_134: 2.4170000E-02,
    Ba_135: 6.5920000E-02,
    Ba_136: 7.8540000E-02,
    Ba_137: 1.1232000E-01,
    Ba_138: 7.1698000E-01
}, natural=True)

#  57: La (lanthanum)
La_nat = Element("natural lanthanum", {
    La_138: 8.8810000E-04,
    La_139: 9.9911190E-01
}, natural=True)

#  58: Ce (cerium)
Ce_nat = Element("natural cerium", {
    Ce_136: 1.8500000E-03,
    Ce_138: 2.5100000E-03,
    Ce_140: 8.8450000E-01,
    Ce_142: 1.1114000E-01
}, natural=True)

#  59: Pr (praseodymium)
Pr_nat = Element("natural praseodymium", {
    Pr_141: 1.0000000E+00
}, natural=True)

#  60: Nd (neodymium)
Nd_nat = Element("natural neodymium", {
    Nd_142: 2.7152000E-01,
    Nd_143: 1.2174000E-01,
    Nd_144: 2.3798000E-01,
    Nd_145: 8.2930000E-02,
    Nd_146: 1.7189000E-01,
    Nd_148: 5.7560000E-02,
    Nd_150: 5.6380000E-02
}, natural=True)

#  61: Pm (promethium)
# not naturally occuring

#  62: Sm (samarium)
Sm_nat = Element("natural samarium", {
    Sm_144: 3.0700000E-02,
    Sm_147: 1.4990000E-01,
    Sm_148: 1.1240000E-01,
    Sm_149: 1.3820000E-01,
    Sm_150: 7.3800000E-02,
    Sm_152: 2.6750000E-01,
    Sm_154: 2.2750000E-01
}, natural=True)

#  63: Eu (europium)
Eu_nat = Element("natural europium", {
    Eu_151: 4.7810000E-01,
    Eu_153: 5.2190000E-01
}, natural=True)

#  64: Gd (gadolinium)
Gd_nat = Element("natural gadolinium", {
    Gd_152: 2.0000000E-03,
    Gd_154: 2.1800000E-02,
    Gd_155: 1.4800000E-01,
    Gd_156: 2.0470000E-01,
    Gd_157: 1.5650000E-01,
    Gd_158: 2.4840000E-01,
    Gd_160: 2.1860000E-01
}, natural=True)

#  65: Tb (terbium)
Tb_nat = Element("natural terbium", {
    Tb_159: 1.0000000E+00
}, natural=True)

#  66: Dy (dysprosium)
Dy_nat = Element("natural dysprosium", {
    Dy_156: 5.6000000E-04,
    Dy_158: 9.5000000E-04,
    Dy_160: 2.3290000E-02,
    Dy_161: 1.8889000E-01,
    Dy_162: 2.5475000E-01,
    Dy_163: 2.4896000E-01,
    Dy_164: 2.8260000E-01
}, natural=True)

#  67: Ho (holmium)
Ho_nat = Element("natural holmium", {
    Ho_165: 1.0000000E+00
}, natural=True)

#  68: Er (erbium)
Er_nat = Element("natural erbium", {
    Er_162: 1.3900000E-03,
    Er_164: 1.6010000E-02,
    Er_166: 3.3503000E-01,
    Er_167: 2.2869000E-01,
    Er_168: 2.6978000E-01,
    Er_170: 1.4910000E-01
}, natural=True)

#  69: Tm (thulium)
Tm_nat = Element("natural thulium", {
    Tm_169: 1.0000000E+00
}, natural=True)

#  70: Yb (ytterbium)
Yb_nat = Element("natural ytterbium", {
    Yb_168: 1.2300000E-03,
    Yb_170: 2.9820000E-02,
    Yb_171: 1.4090000E-01,
    Yb_172: 2.1680000E-01,
    Yb_173: 1.6103000E-01,
    Yb_174: 3.2026000E-01,
    Yb_176: 1.2996000E-01
}, natural=True)

#  71: Lu (lutetium)
Lu_nat = Element("natural lutetium", {
    Lu_175: 9.7401000E-01,
    Lu_176: 2.5990000E-02
}, natural=True)

#  72: Hf (hafnium)
Hf_nat = Element("natural hafnium", {
    Hf_174: 1.6000000E-03,
    Hf_176: 5.2600000E-02,
    Hf_177: 1.8600000E-01,
    Hf_178: 2.7280000E-01,
    Hf_179: 1.3620000E-01,
    Hf_180: 3.5080000E-01
}, natural=True)

#  73: Ta (tantalum)
Ta_nat = Element("natural tantalum", {
    Ta_180: 1.2010000E-04,
    Ta_181: 9.9987990E-01
}, natural=True)

#  74: W  (tungsten)
W_nat = Element("natural tungsten", {
    W_180:  1.2000000E-03,
    W_182:  2.6500000E-01,
    W_183:  1.4310000E-01,
    W_184:  3.0640000E-01,
    W_186:  2.8430000E-01
}, natural=True)

#  75: Re (rhenium)
Re_nat = Element("natural rhenium", {
    Re_185: 3.7400000E-01,
    Re_187: 6.2600000E-01
}, natural=True)

#  76: Os (osmium)
Os_nat = Element("natural osmium", {
    Os_184: 2.0000000E-04,
    Os_186: 1.5900000E-02,
    Os_187: 1.9600000E-02,
    Os_188: 1.3240000E-01,
    Os_189: 1.6150000E-01,
    Os_190: 2.6260000E-01,
    Os_192: 4.0780000E-01
}, natural=True)

#  77: Ir (iridium)
Ir_nat = Element("natural iridium", {
    Ir_191: 3.7300000E-01,
    Ir_193: 6.2700000E-01
}, natural=True)

#  78: Pt (platinum)
Pt_nat = Element("natural platinum", {
    Pt_190: 1.2000000E-04,
    Pt_192: 7.8200000E-03,
    Pt_194: 3.2860000E-01,
    Pt_195: 3.3780000E-01,
    Pt_196: 2.5210000E-01,
    Pt_198: 7.3560000E-02
}, natural=True)

#  79: Au (gold)
Au_nat = Element("natural gold", {
    Au_197: 1.0000000E+00
}, natural=True)

#  80: Hg (mercury)
Hg_nat = Element("natural mercury", {
    Hg_196: 1.5000000E-03,
    Hg_198: 9.9700000E-02,
    Hg_199: 1.6870000E-01,
    Hg_200: 2.3100000E-01,
    Hg_201: 1.3180000E-01,
    Hg_202: 2.9860000E-01,
    Hg_204: 6.8700000E-02
}, natural=True)

#  81: Tl (thallium)
Tl_nat = Element("natural thallium", {
    Tl_203: 2.9520000E-01,
    Tl_205: 7.0480000E-01
}, natural=True)

#  82: Pb (lead)
Pb_nat = Element("natural lead", {
    Pb_204: 1.4000000E-02,
    Pb_206: 2.4100000E-01,
    Pb_207: 2.2100000E-01,
    Pb_208: 5.2400000E-01
}, natural=True)

#  83: Bi (bismuth)
Bi_nat = Element("natural bismuth", {
    Bi_209: 1.0000000E+00
}, natural=True)

#  84: Po (polonium)
# not naturally occuring

#  85: At (astatine)
# not naturally occuring

#  86: Rn (radon)
# not naturally occuring

#  87: Fr (francium)
# not naturally occuring

#  88: Ra (radium)
# not naturally occuring

#  89: Ac (actinium)
# not naturally occuring

#  90: Th (thorium)
Th_nat = Element("natural thorium", {
    Th_232: 1.0000000E+00
}, natural=True)

#  91: Pa (protactinium)
Pa_nat = Element("natural protactinium", {
    Pa_231: 1.0000000E+00
}, natural=True)

#  92: U  (uranium)
U_nat = Element("natural uranium", {
    U_234:  5.4000000E-05,
    U_235:  7.2040000E-03,
    U_238:  9.9274200E-01
}, natural=True)

#  93: Np (neptunium)
# not naturally occuring

#  94: Pu (plutonium)
# not naturally occuring

#  95: Am (americium)
# not naturally occuring

#  96: Cm (curium)
# not naturally occuring

#  97: Bk (berkelium)
# not naturally occuring

#  98: Cf (californium)
# not naturally occuring

#  99: Es (einsteinium)
# not naturally occuring

# 100: Fm (fermium)
# not naturally occuring

# 101: Md (mendelevium)
# not naturally occuring

# 102: No (nobelium)
# not naturally occuring

# 103: Lr (lawrencium)
# not naturally occuring

# 104: Rf (rutherfordium)
# not naturally occuring

# 105: Db (dubnium)
# not naturally occuring

# 106: Sg (seaborgium)
# not naturally occuring

# 107: Bh (bohrium)
# not naturally occuring

# 108: Hs (hassium)
# not naturally occuring

# 109: Mt (meitnerium)
# not naturally occuring

# 110: Ds (darmstadtium)
# not naturally occuring

# 111: Rg (roentgenium)
# not naturally occuring

# 112: Cn (copernicium)
# not naturally occuring

# 113: Nh (nihonium)
# not naturally occuring

# 114: Fl (flerovium)
# not naturally occuring

# 115: Mc (moscovium)
# not naturally occuring

# 116: Lv (livermorium)
# not naturally occuring

# 117: Ts (tennessine)
# not naturally occuring

# 118: Og (oganesson)
# not naturally occuring
