# module for element symbols and names and natural elements

from .exceptions import *
from .element import Element
from .isotopes import *






# ################
# natural elements
# ################

#   1: H  (hydrogen)
H_nat = Element("natural hydrogen", {
        H_1:    9.998850E-01,
        H_2:    1.150000E-04
    })

#   2: He (helium)
He_nat = Element("natural helium", {
        He_3:   1.340000E-06,
        He_4:   9.999987E-01
    })

#   3: Li (lithium)
Li_nat = Element("natural lithium", {
        Li_6:   7.590000E-02,
        Li_7:   9.241000E-01
    })

#   4: Be (berylium)
Be_nat = Element("natural berylium", {
        Be_9:   1.000000E+00
    })

#   5: B  (boron)
B_nat = Element("natural boron", {
        B_10:   1.990000E-01,
        B_11:   8.010000E-01
    })

#   6: C  (carbon)
C_nat = Element("natural carbon", {
        C_12:   9.893000E-01,
        C_13:   1.070000E-02
    })

#   7: N  (nitrogen)
N_nat = Element("natural nitrogen", {
        N_14:   9.963600E-01,
        N_15:   3.640000E-03
    })

#   8: O  (oxygen)
O_nat = Element("natural oxygen", {
        O_16:   9.975700E-01,
        O_17:   3.800000E-04,
        O_18:   2.050000E-03
    })

#   9: F  (fluorine)
F_nat = Element("natural fluorine", {
        F_19:   1.000000E+00
    })

#  10: Ne (neon)
Ne_nat = Element("natural neon", {
        Ne_20:  9.048000E-01,
        Ne_21:  2.700000E-03,
        Ne_22:  9.250000E-02
    })

#  11: Na (sodium)
Na_nat = Element("natural sodium", {
        Na_23:  1.000000E+00
    })

#  12: Mg (magnesium)
Mg_nat = Element("natural magnesium", {
        Mg_24:  7.899000E-01,
        Mg_25:  1.000000E-01,
        Mg_26:  1.101000E-01
    })

#  13: Al (aluminium)
Al_nat = Element("natural aluminium", {
        Al_27:  1.000000E+00
    })

#  14: Si (silicon)
Si_nat = Element("natural silicon", {
        Si_28:  9.222300E-01,
        Si_29:  4.685000E-02,
        Si_30:  3.092000E-02
    })

#  15: P  (phosphorus)
P_nat = Element("natural phosphorus", {
        P_31:   1.000000E+00
    })

#  16: S  (sulphur)
S_nat = Element("natural sulphur", {
        S_32:   9.499000E-01,
        S_33:   7.500000E-03,
        S_34:   4.250000E-02,
        S_36:   1.000000E-04
    })

#  17: Cl (chlorine)
Cl_nat = Element("natural chlorine", {
        Cl_35:  7.576000E-01,
        Cl_37:  2.424000E-01
    })

#  18: Ar (argon)
Ar_nat = Element("natural argon", {
        Ar_36:  3.336000E-03,
        Ar_38:  6.290000E-04,
        Ar_40:  9.960350E-01
    })

#  19: K  (potassium)
K_nat = Element("natural potassium", {
        K_39:   9.325810E-01,
        K_40:   1.170000E-04,
        K_41:   6.730200E-02
    })

#  20: Ca (calcium)
Ca_nat = Element("natural calcium", {
        Ca_40:  9.694100E-01,
        Ca_42:  6.470000E-03,
        Ca_43:  1.350000E-03,
        Ca_44:  2.086000E-02,
        Ca_46:  4.000000E-05,
        Ca_48:  1.870000E-03
    })

#  21: Sc (scandium)
Sc_nat = Element("natural scandium", {
        Sc_45:  1.000000E+00
    })

#  22: Ti (titanium)
Ti_nat = Element("natural titanium",{
        Ti_46:  8.250000E-02,
        Ti_47:  7.440000E-02,
        Ti_48:  7.372000E-01,
        Ti_49:  5.410000E-02,
        Ti_50:  5.180000E-02
    })

#  23: V  (vanadium)
V_nat = Element("natural vanadium", {
        V_50:   2.500000E-03,
        V_51:   9.975000E-01
    })

#  24: Cr (chromium)
Cr_nat = Element("natural chromium", {
        Cr_50:  4.345000E-02,
        Cr_52:  8.378900E-01,
        Cr_53:  9.501000E-02,
        Cr_54:  2.365000E-02
    })

#  25: Mn (manganese)
Mn_nat = Element("natural manganese", {
        Mn_55:  1.000000E+00
    })

#  26: Fe (iron)
Fe_nat = Element("natural iron", {
        Fe_54:  5.845000E-02,
        Fe_56:  9.175400E-01,
        Fe_57:  2.119000E-02,
        Fe_58:  2.820000E-03
    })

#  27: Co (cobalt)
Co_nat = Element("natural cobalt", {
        Co_59:  1.000000E+00
    })

#  28: Ni (nickel)
Ni_nat = Element("natural nickel", {
        Ni_58:  6.807700E-01,
        Ni_60:  2.622300E-01,
        Ni_61:  1.139900E-02,
        Ni_62:  3.634600E-02,
        Ni_64:  9.255000E-03
    })

#  29: Cu (copper)
Cu_nat = Element("natural copper", {
        Cu_63:  6.915000E-01,
        Cu_65:  3.085000E-01
    })

#  30: Zn (zinc)
Zn_nat = Element("natural zinc", {
        Zn_64:  4.917000E-01,
        Zn_66:  2.773000E-01,
        Zn_67:  4.040000E-02,
        Zn_68:  1.845000E-01,
        Zn_70:  6.100000E-03
    })

#  31: Ga (gallium)
Ga_nat = Element("natural gallium", {
        Ga_69:  6.010800E-01,
        Ga_71:  3.989200E-01
    })

#  32: Ge (germanium)
Ge_nat = Element("natural germanium", {
        Ge_70:  2.057000E-01,
        Ge_72:  2.745000E-01,
        Ge_73:  7.750000E-02,
        Ge_74:  3.650000E-01,
        Ge_76:  7.730000E-02
    })

#  33: As (arsenic)
As_nat = Element("natural arsenic", {
        As_75:  1.000000E+00
    })

#  34: Se (selenium)
Se_nat = Element("natural selenium", {
        Se_74:  8.900000E-03,
        Se_76:  9.370000E-02,
        Se_77:  7.630000E-02,
        Se_78:  2.377000E-01,
        Se_80:  4.961000E-01,
        Se_82:  8.730000E-02
    })

#  35: Br (bromine)
Br_nat = Element("natural bromine", {
        Br_79:  5.069000E-01,
        Br_81:  4.931000E-01
    })

#  36: Kr (krypton)
Kr_nat = Element("natural krypton", {
        Kr_78:  3.550000E-03,
        Kr_80:  2.286000E-02,
        Kr_82:  1.159300E-01,
        Kr_83:  1.150000E-01,
        Kr_84:  5.698700E-01,
        Kr_86:  1.727900E-01
    })

#  37: Rb (rubidium)
Rb_nat = Element("natural rubidium", {
        Rb_85:  7.217000E-01,
        Rb_87:  2.783000E-01
    })

#  38: Sr (strontium)
Sr_nat = Element("natural strontium", {
        Sr_84:  5.600000E-03,
        Sr_86:  9.860000E-02,
        Sr_87:  7.000000E-02,
        Sr_88:  8.258000E-01
    })

#  39: Y  (yttrium)
Y_nat = Element("natural yttrium", {
        Y_89:   1.000000E+00
    })

#  40: Zr (zirconium)
Zr_nat = Element("natural zirconium", {
        Zr_90:  5.145000E-01,
        Zr_91:  1.122000E-01,
        Zr_92:  1.715000E-01,
        Zr_94:  1.738000E-01,
        Zr_96:  2.800000E-02
    })

#  41: Nb (niobium)
Nb_nat = Element("natural niobium", {
        Nb_93:  1.000000E+00
    })

#  42: Mo (molybdenum)
Mo_nat = Element("natural molybdenum", {
        Mo_92:  1.453000E-01,
        Mo_94:  9.150000E-02,
        Mo_95:  1.584000E-01,
        Mo_96:  1.667000E-01,
        Mo_97:  9.600000E-02,
        Mo_98:  2.439000E-01,
        Mo_100: 9.820000E-02
    })

#  43: Tc (technetium)
# not naturally occuring

#  44: Ru (ruthenium)
Ru_nat = Element("natural ruthenium", {
        Ru_96:  5.540000E-02,
        Ru_98:  1.870000E-02,
        Ru_99:  1.276000E-01,
        Ru_100: 1.260000E-01,
        Ru_101: 1.706000E-01,
        Ru_102: 3.155000E-01,
        Ru_104: 1.862000E-01
    })

#  45: Rh (rhodium)
Rh_nat = Element("natural rhodium", {
        Rh_103: 1.000000E+00
    })

#  46: Pd (palladium)
Pd_nat = Element("natural palladium", {
        Pd_102: 1.020000E-02,
        Pd_104: 1.114000E-01,
        Pd_105: 2.233000E-01,
        Pd_106: 2.733000E-01,
        Pd_108: 2.646000E-01,
        Pd_110: 1.172000E-01
    })

#  47: Ag (silver)
Ag_nat = Element("natural silver", {
        Ag_107: 5.183900E-01,
        Ag_109: 4.816100E-01
    })

#  48: Cd (cadmium)
Cd_nat = Element("natural cadmium", {
        Cd_106: 1.250000E-02,
        Cd_108: 8.900000E-03,
        Cd_110: 1.249000E-01,
        Cd_111: 1.280000E-01,
        Cd_112: 2.413000E-01,
        Cd_113: 1.222000E-01,
        Cd_114: 2.873000E-01,
        Cd_116: 7.490000E-02
    })

#  49: In (indium)
In_nat = Element("natural indium", {
        In_113: 4.290000E-02,
        In_115: 9.571000E-01
    })

#  50: Sn (tin)
Sn_nat = Element("natural tin", {
        Sn_112: 9.700000E-03,
        Sn_114: 6.600000E-03,
        Sn_115: 3.400000E-03,
        Sn_116: 1.454000E-01,
        Sn_117: 7.680000E-02,
        Sn_118: 2.422000E-01,
        Sn_119: 8.590000E-02,
        Sn_120: 3.258000E-01,
        Sn_122: 4.630000E-02,
        Sn_124: 5.790000E-02
    })

#  51: Sb (antimony)
Sb_nat = Element("natural antimony", {
        Sb_121: 5.721000E-01,
        Sb_123: 4.279000E-01
    })

#  52: Te (tellurium)
Te_nat = Element("natural tellurium", {
        Te_120: 9.000000E-04,
        Te_122: 2.550000E-02,
        Te_123: 8.900000E-03,
        Te_124: 4.740000E-02,
        Te_125: 7.070000E-02,
        Te_126: 1.884000E-01,
        Te_128: 3.174000E-01,
        Te_130: 3.408000E-01
    })

#  53: I  (iodine)
I_nat = Element("natural iodine", {
        I_127:  1.000000E+00
    })

#  54: Xe (xenon)
Xe_nat = Element("natural xenon", {
        Xe_124: 9.520000E-04,
        Xe_126: 8.900000E-04,
        Xe_128: 1.910200E-02,
        Xe_129: 2.640060E-01,
        Xe_130: 4.071000E-02,
        Xe_131: 2.123240E-01,
        Xe_132: 2.690860E-01,
        Xe_134: 1.043570E-01,
        Xe_136: 8.857300E-02
    })

#  55: Cs (caesium)
Cs_nat = Element("natural caesium", {
        Cs_133: 1.000000E+00
    })

#  56: Ba (barium)
Ba_nat = Element("natural barium", {
        Ba_130: 1.060000E-03,
        Ba_132: 1.010000E-03,
        Ba_134: 2.417000E-02,
        Ba_135: 6.592000E-02,
        Ba_136: 7.854000E-02,
        Ba_137: 1.123200E-01,
        Ba_138: 7.169800E-01
    })

#  57: La (lanthanum)
La_nat = Element("natural lanthanum", {
        La_138: 8.881000E-04,
        La_139: 9.991119E-01
    })

#  58: Ce (cerium)
Ce_nat = Element("natural cerium", {
        Ce_136: 1.850000E-03,
        Ce_138: 2.510000E-03,
        Ce_140: 8.845000E-01,
        Ce_142: 1.111400E-01
    })

#  59: Pr (praseodymium)
Pr_nat = Element("natural praseodymium", {
        Pr_141: 1.000000E+00
    })

#  60: Nd (neodymium)
Nd_nat = Element("natural neodymium", {
        Nd_142: 2.715200E-01,
        Nd_143: 1.217400E-01,
        Nd_144: 2.379800E-01,
        Nd_145: 8.293000E-02,
        Nd_146: 1.718900E-01,
        Nd_148: 5.756000E-02,
        Nd_150: 5.638000E-02
    })

#  61: Pm (promethium)
# not naturally occuring

#  62: Sm (samarium)
Sm_nat = Element("natural samarium", {
        Sm_144: 3.070000E-02,
        Sm_147: 1.499000E-01,
        Sm_148: 1.124000E-01,
        Sm_149: 1.382000E-01,
        Sm_150: 7.380000E-02,
        Sm_152: 2.675000E-01,
        Sm_154: 2.275000E-01
    })

#  63: Eu (europium)
Eu_nat = Element("natural europium", {
        Eu_151: 4.781000E-01,
        Eu_153: 5.219000E-01
    })

#  64: Gd (gadolinium)
Gd_nat = Element("natural gadolinium", {
        Gd_152: 2.000000E-03,
        Gd_154: 2.180000E-02,
        Gd_155: 1.480000E-01,
        Gd_156: 2.047000E-01,
        Gd_157: 1.565000E-01,
        Gd_158: 2.484000E-01,
        Gd_160: 2.186000E-01
    })

#  65: Tb (terbium)
Tb_nat = Element("natural terbium", {
        Tb_159: 1.000000E+00
    })

#  66: Dy (dysprosium)
Dy_nat = Element("natural dysprosium", {
        Dy_156: 5.600000E-04,
        Dy_158: 9.500000E-04,
        Dy_160: 2.329000E-02,
        Dy_161: 1.888900E-01,
        Dy_162: 2.547500E-01,
        Dy_163: 2.489600E-01,
        Dy_164: 2.826000E-01
    })

#  67: Ho (holmium)
Ho_nat = Element("natural holmium", {
        Ho_165: 1.000000E+00
    })

#  68: Er (erbium)
Er_nat = Element("natural erbium", {
        Er_162: 1.390000E-03,
        Er_164: 1.601000E-02,
        Er_166: 3.350300E-01,
        Er_167: 2.286900E-01,
        Er_168: 2.697800E-01,
        Er_170: 1.491000E-01
    })

#  69: Tm (thulium)
Tm_nat = Element("natural thulium", {
        Tm_169: 1.000000E+00
    })

#  70: Yb (ytterbium)
Yb_nat = Element("natural ytterbium", {
        Yb_168: 1.230000E-03,
        Yb_170: 2.982000E-02,
        Yb_171: 1.409000E-01,
        Yb_172: 2.168000E-01,
        Yb_173: 1.610300E-01,
        Yb_174: 3.202600E-01,
        Yb_176: 1.299600E-01
    })

#  71: Lu (lutetium)
Lu_nat = Element("natural lutetium", {
        Lu_175: 9.740100E-01,
        Lu_176: 2.599000E-02
    })

#  72: Hf (hafnium)
Hf_nat = Element("natural hafnium", {
        Hf_174: 1.600000E-03,
        Hf_176: 5.260000E-02,
        Hf_177: 1.860000E-01,
        Hf_178: 2.728000E-01,
        Hf_179: 1.362000E-01,
        Hf_180: 3.508000E-01
    })

#  73: Ta (tantalum)
Ta_nat = Element("natural tantalum", {
        Ta_180: 1.201000E-04,
        Ta_181: 9.998799E-01
    })

#  74: W  (tungsten)
W_nat = Element("natural tungsten", {
        W_180:  1.200000E-03,
        W_182:  2.650000E-01,
        W_183:  1.431000E-01,
        W_184:  3.064000E-01,
        W_186:  2.843000E-01
    })

#  75: Re (rhenium)
Re_nat = Element("natural rhenium", {
        Re_185: 3.740000E-01,
        Re_187: 6.260000E-01
    })

#  76: Os (osmium)
Os_nat = Element("natural osmium", {
        Os_184: 2.000000E-04,
        Os_186: 1.590000E-02,
        Os_187: 1.960000E-02,
        Os_188: 1.324000E-01,
        Os_189: 1.615000E-01,
        Os_190: 2.626000E-01,
        Os_192: 4.078000E-01
    })

#  77: Ir (iridium)
Ir_nat = Element("natural iridium", {
        Ir_191: 3.730000E-01,
        Ir_193: 6.270000E-01
    })

#  78: Pt (platinum)
Pt_nat = Element("natural platinum", {
        Pt_190: 1.200000E-04,
        Pt_192: 7.820000E-03,
        Pt_194: 3.286000E-01,
        Pt_195: 3.378000E-01,
        Pt_196: 2.521000E-01,
        Pt_198: 7.356000E-02
    })

#  79: Au (gold)
Au_nat = Element("natural gold", {
        Au_197: 1.000000E+00
    })

#  80: Hg (mercury)
Hg_nat = Element("natural mercury", {
        Hg_196: 1.500000E-03,
        Hg_198: 9.970000E-02,
        Hg_199: 1.687000E-01,
        Hg_200: 2.310000E-01,
        Hg_201: 1.318000E-01,
        Hg_202: 2.986000E-01,
        Hg_204: 6.870000E-02
    })

#  81: Tl (thallium)
Tl_nat = Element("natural thallium", {
        Tl_203: 2.952000E-01,
        Tl_205: 7.048000E-01
    })

#  82: Pb (lead)
Pb_nat = Element("natural lead", {
        Pb_204: 1.400000E-02,
        Pb_206: 2.410000E-01,
        Pb_207: 2.210000E-01,
        Pb_208: 5.240000E-01
    })

#  83: Bi (bismuth)
Bi_nat = Element("natural bismuth", {
        Bi_209: 1.000000E+00
    })

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
        Th_232: 1.000000E+00
    })

#  91: Pa (protactinium)
Pa_nat = Element("natural protactinium", {
        Pa_231: 1.000000E+00
    })

#  92: U  (uranium)
U_nat = Element("natural uranium", {
        U_234:  5.400000E-05,
        U_235:  7.204000E-03,
        U_238:  9.927420E-01
    })

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
