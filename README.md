# isoVec

## Description

isoVec is a framework to build complex mixtures of materials and get atomic, weight or volume percentages of each of its substances down to the isotopic composition (the isotope vector, hence the name).
The information on relative atomic weights of isotopes, as well as their abundance in natural occuring elements, is taken from "*Atomic Weights and Isotopic Compositions with Relative Atomic Masses*" by the NIST Physical Measurement Laboratory [1].
This information is embedded in the form of `Isotope` and `Element` classes.
The user can also create custom `Elements`s and specify the isotopic composition manually.
`Molecule`s are made from `Element`s and `Mixture`s can be made from `Element`s, `Molecule`s and other `Mixture`s.
A thorough example is given in Section 'Example'.


## Installation

The source code of the most recent development version is hosted on [GitHub](https://github.com/jmercz/isoVec).
The binary installers and the source code of stable releases is available on the project site on the [Python Package Index (PyPI)](https://pypi.org/project/isovec) and can be simply installed from the repository via

```sh
pip install isovec
```

There are no additional dependencies other than core Python packages of Python 3.10.


## Example

The composition of the atmosphere of the Earth may serve as an example how to use isoVec.
The constituents and their atomic (mole) fractions are taken from the respective [Wikipedia article](https://en.wikipedia.org/wiki/Atmosphere_of_Earth#Composition) and are as of April 2022:

| Constituent                     | Atomic Fraction        |
| ------------------------------- | ---------------------- |
| Nitrogen (N<sub>2</sub>)        | 78.084 %               |
| Oxygen (O<sub>2</sub>)          | 20.946 %               |
| Argon (Ar)                      | 0.9340 %               |
| Carbon dioxide (CO<sub>2</sub>) | 417 ppm                |
| Neon (Ne)                       | 18.18 ppm              |
| Helium (He)                     | 5.24 ppm               |
| Methane (CH<sub>4</sub>)        | 1.87 ppm               |
| Krypton (Kr)                    | 1.14 ppm               |

It may be noted, that these values are often given as a volume fraction in other literature.
For a mixture of ideal gases (which is the case for air), volume and atomic fractions are equal.
Furthermore the amount of substance (mole) and number of particles (e.g. atoms) are proportional, being connected via the Avogadro constant.
Thus, atomic and mole fractions can and are used interchangeably in the following.

Let's assume for the following, that isoVec is imported with the following (shorter) alias.
Keep in mind, that all content is packed inside the given namespace.

```python
import isovec as iso
```

### Element

Natural occuring elements are already implemented and can be accessed via its symbol and "_nat".
Nitrogen for example is called with `N_nat`.
For the sake of this tutorial, we will define nitrogen again by ourselfs.
Furthermore, an extensive library of isotopes is implemented. Each `Isotope` is acessed via the elements symbol, followed by an underscore "\_" and its mass number (that is protons + neutrons).
Nitrogen-14 is therefore called via `N_14`.
An `Element` can only be composed of its respective isotopes, so `Isotope` objects with the same atomic number `Z`.

A custom `Element` is created with a unique name and its composition as a dictionary:

```python
nitrogen = iso.Element("nitrogen", {
    iso.N_14: 9.963600E-01,
    iso.N_15: 3.640000E-03
})
```

In composition dictionaries, positive values refer to an atomic fraction (as done before), while negative values refer to a weight fraction.
Whatever information is available or more convenient may be used, but atomic and weight fractions **cannot** be mixed inside one composition dictionary.
If the keyword argument `mode` is supplied with either `"atomic"`, `"weight"` or other short forms thereof, signs are ignored and the values of the dictionary are interpreted accordingly, making the construction call more verbose.
Alternatively, fraction-specific constructor methods can be called on the class, namely `from_atomic()` and `from_weight()`, in which case the keyword `mode` doesn't need to be supplied.
Otherwise, the syntax is identical to the ordinary constructor call.
The given composition doesn't necessarily need to add up to unity.
Instead, each fraction is normalised by the total sum of given fractions.

The molar mass of an element is calculated automatically, but could be overwritten when supplying the keyword argument `M=value` in the constructor.
Optionally, the density of the element can be supplied with the keyword argument `rho=value`, since densities of elements cannot be calculated automatically by the given informations.
The described behaviour of the constructur also applies to the following classes, if not stated otherwise.


### Molecule

The composition for a molecule is the number of atoms per element.
Therefore, only the `"atomic"` mode is valid, or in short positive values in the composition dictionary.
However, this class isn't strictly limited to molecules, but can be used for crystalline or amorphous structures with a stochiometric distribution.

Using the implemented natural elements, the `Molecule` for carbon dioxide is given by:

```python
carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})
```

Likewise, the other molecules are given as:

```python
methane = iso.Molecule("methane", {
    iso.C_nat: 1,
    iso.H_nat: 4
})
nitrogen2 = iso.Molecule("molecular nitrogen", { iso.N_nat: 2})
oxygen2 = iso.Molecule("molecular oxygen", { iso.O_nat: 2})
```

Note, that the molar mass of the entire molecule is calculated by default.


### Mixture

`Mixtures` can contain several pure elements, molecules and also other mixtures.
In contrast to `Element` and `Molecule`, it is also possible to supply volume fractions in the composition, provided that all constituents have a density defined.
This can be invoked either by supplying the keyword argument `mode="volume"` to the constructor, or calling the specific constructor `from_volume()`.

According to the table from the introduction, a mixture for air is given by the following (note the use of convencience functions for conversion, an extensive list can be found in the source code file "conversion.py"):

```python
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
```

When all constituents have their density defined, the density of the mixture can also be calculated automatically.

The material hierarchy can be printed in a tree-like structure, down to the isotopic composition, by invoking `print_tree()` on any substance we want to inspect:

```python
air.print_tree(weight=True, align_isotopes=True)
```

Setting the keywords `weight` or `volume` to `True` also calculates the weight and volume percent of each node respectively (where applicable), in addition to the atomic percentage that is printed by default (but can be deactivated via the keyword `atomic`).
The flag `align_isotopes` will align all isotopes in one column for better comparability.
This yields the following (excerpt of the) output:

```
Mixture "air": 28.9660 g/mol
├── Molecule "molecular nitrogen":  78.0775 at.%  |   75.5097 wt.%  |  28.0134 g/mol
│   └── Element "natural nitrogen":  78.0775 at.%  |   75.5097 wt.%  |  14.0067 g/mol
│       ├── Isotope   "N-14":  77.7933 at.%  |   75.2154 wt.%  |  14.0031 g/mol
│       └── Isotope   "N-15":   0.2842 at.%  |    0.2943 wt.%  |  15.0001 g/mol
├── Molecule "molecular oxygen":  20.9443 at.%  |   23.1372 wt.%  |  31.9988 g/mol
│   └── Element "natural oxygen":  20.9443 at.%  |   23.1372 wt.%  |  15.9994 g/mol
│       ├── Isotope   "O-16":  20.8934 at.%  |   23.0744 wt.%  |  15.9949 g/mol
│       ├── Isotope   "O-17":   0.0080 at.%  |    0.0093 wt.%  |  16.9991 g/mol
│       └── Isotope   "O-18":   0.0429 at.%  |    0.0534 wt.%  |  17.9992 g/mol
├── Element "natural argon":   0.9339 at.%  |    1.2880 wt.%  |  39.9478 g/mol
│   ├────── Isotope  "Ar-36":   0.0031 at.%  |    0.0039 wt.%  |  35.9675 g/mol
│   ├────── Isotope  "Ar-38":   0.0006 at.%  |    0.0008 wt.%  |  37.9627 g/mol
│   └────── Isotope  "Ar-40":   0.9302 at.%  |    1.2834 wt.%  |  39.9624 g/mol
   [...]
```

The fractions of subcomponents are scaled with their parent fraction by default, but this behaviour can be disabled via the keyword argument `scale`.
In other words, the fractions are multiplicative *downwards*.
If not scaled, the fractions will only sum up for one material composition, so on their 'sibling' level.
The format of the fraction values and the physical properties can be given by supplying the keywords `frac_fmt` and `prop_fmt` respectively with a format string.
Alternatively, a less feature-rich overview of all subcomponents in tabular form can be obtained by invoking `print_overview()`, also featuring the scale functionality.


### Isotope Composition

These printing routines don't sum recurring instances of a single isotope, something that might be of interest.
The method `get_isotopes()` can be called upon every substance and yields an ordered dictionary with the isotopes and their respective sum of either atomic (default) or weight fractions, depending on the `mode` keyword argument.
For the mixture of air, the following code

```python
isotope_vector = air.get_isotopes(mode="atomic")
for isotope, at_frac in isotope_vector.items():
    print(f"{isotope.name:>6}: {at_frac:.4E}")
```

yields the final isotope vector:

```
   H-1: 1.4957E-06
   H-2: 1.7203E-10
  He-3: 7.0210E-12
  He-4: 5.2396E-06
  C-12: 1.3787E-04
  C-13: 1.4912E-06
  N-14: 7.7793E-01
  N-15: 2.8420E-03
  O-16: 2.0921E-01
  O-17: 7.9694E-05
  O-18: 4.2993E-04
   [...]
```


#### Natural Element Composition

By setting the `get_isotopes()` keyword argument `use_natural=True`, a surrogate `Isotope` object is added to the list instead, if the `Element` object is one of the implemented natural elements. This surrogate object represents an element with natural occuring abundance. Since only natural elements were used in this tutorial, the following code:

```python
isotope_vector = air.get_isotopes(mode="atomic", use_natural=True)
for isotope, at_frac in isotope_vector.items():
    name = isotope.element_symbol() + "-nat"
    print(f"{name:>6}: {at_frac:.4E}")
```

yields the element vector:

```
 H-nat: 1.4959E-06
He-nat: 5.2396E-06
 C-nat: 1.3936E-04
 N-nat: 7.8077E-01
 O-nat: 2.0972E-01
Ne-nat: 1.8178E-05
Ar-nat: 9.3392E-03
Kr-nat: 1.1399E-06
```

Note that custom made elements are not subject to that behaviour, unless the keyword argument `natural=True` was specified in their constructor.


## Changelog

For a history of changes, refer to the file `CHANGELOG.md` in the source code distributions or directly on the [GitHub repository](https://github.com/jmercz/isoVec/blob/main/README.md).

## References

1. Coursey, J.S., Schwab, D.J., Tsai, J.J., and Dragoset, R.A. (2015), Atomic Weights and Isotopic Compositions (version 4.1). [Online] Available: https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses [Accessed 23 July 2023]. National Institute of Standards and Technology, Gaithersburg, MD.