# isoVec

## Description

isoVec is a framework to build complex mixtures of materials and get atomic (mole), weight or volume percentages of each of its substances down to the isotopic composition (the isotope vector, hence the name).
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
The constituents and their mole fractions are taken from the respective [Wikipedia article](https://en.wikipedia.org/wiki/Atmosphere_of_Earth#Composition) and are as of April 2022:

| Constituent                     | Mole Fraction          |
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
For a mixture of ideal gases (which is the case for air), volume and mole fractions are equal.
Furthermore the amount of substance (mole) and number of particles (e.g. atoms) are proportional in an element, being connected via the Avogadro constant $N_\mathrm{A}$.
Here, the terms mole and atomic fraction can be used interchangeably.
In general, and especially when dealing with molecules containing multiple atoms per particle, this is not strictly correct, but is done regardless in the API for the sake of convenience.
One should be aware of this and always consider the current context.

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

The composition for a `Molecule` is the number of atoms per `Element`.
Therefore, only the `"atomic"` mode is valid, or in short positive values in the composition dictionary.
However, this class isn't strictly limited to molecules, but can be used for crystalline or amorphous structures with a stochiometric distribution.

Using the implemented natural `Element`s, the `Molecule` for carbon dioxide is given by:

```python
carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})
```

Likewise, the other `Molecule`s are given as:

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

`Mixtures` can contain several pure `Element`s, `Molecule`s and also other `Mixture`s.
In contrast to `Element` and `Molecule`, it is also possible to supply volume fractions in the composition, provided that all constituents have a density defined.
This can be invoked either by supplying the keyword argument `mode="volume"` to the constructor, or calling the specific constructor `from_volume()`.

According to the table from the introduction, a `Mixture` for air is defined by the following:

```python
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
```

Note the use of convencience functions for conversion, an extensive list can be found in the source code file "conversion.py"
When all constituents have their density defined, the density of the `Mixture` can also be calculated automatically.

The entered material hierarchy can be printed in a tree-like structure by invoking `print_tree_input()` on any substance we want to inspect:

```python
air.print_tree_input(weight=True)
```

The percentage refers to the fraction in the parent and will sum up to 100 % on their 'sibling' level.
Setting the keywords `weight` or `volume` to `True` also calculates the weight and volume percent of each node respectively (where applicable), in addition to the atomic percentage that is printed by default (but can be deactivated via the keyword `atomic`).
This yields the following (excerpt of the) output:

```
Mixture "air": 28.9660 g/mol
├── Molecule "molecular nitrogen":  78.0775 at.%  |   75.5097 wt.%  |  28.0134 g/mol
│   └── Element "natural nitrogen": 100.0000 at.%  |  100.0000 wt.%  |  14.0067 g/mol
│       ├── Isotope "N-14":  99.6360 at.%  |   99.6102 wt.%  |  14.0031 g/mol
│       └── Isotope "N-15":   0.3640 at.%  |    0.3898 wt.%  |  15.0001 g/mol
├── Molecule "molecular oxygen":  20.9443 at.%  |   23.1372 wt.%  |  31.9988 g/mol
│   └── Element "natural oxygen": 100.0000 at.%  |  100.0000 wt.%  |  15.9994 g/mol
│       ├── Isotope "O-16":  99.7570 at.%  |   99.7290 wt.%  |  15.9949 g/mol
│       ├── Isotope "O-17":   0.0380 at.%  |    0.0404 wt.%  |  16.9991 g/mol
│       └── Isotope "O-18":   0.2050 at.%  |    0.2306 wt.%  |  17.9992 g/mol
├── Element "natural argon":   0.9339 at.%  |    1.2880 wt.%  |  39.9478 g/mol
│   ├── Isotope "Ar-36":   0.3336 at.%  |    0.3004 wt.%  |  35.9675 g/mol
│   ├── Isotope "Ar-38":   0.0629 at.%  |    0.0598 wt.%  |  37.9627 g/mol
│   └── Isotope "Ar-40":  99.6035 at.%  |   99.6399 wt.%  |  39.9624 g/mol
   [...]
```

The format of the fraction values and the physical properties can be given by supplying the keywords `frac_fmt` and `prop_fmt` respectively with a format string.


### Elemental & Isotopic Composition

To obtain the elemental composition, the method `get_elements()` can be called upon a substance, yielding an ordered dictionary with elements and their respective summed fractions.
With the `mode` keyword argument, fractions can be fetched in terms of `"atomic"` or `"weight"`.
For the mixture of air, the following code

```python
element_vector = air.get_elements(mode="atomic")
for element, at_frac in element_vector.items():
    print(f"{element.symbol:>2}: {at_frac:.4E}")
```

yields the elemental composition:

```
 H: 3.7565E-06
He: 2.6315E-06
 C: 2.1036E-04
 N: 7.8428E-01
 O: 2.1080E-01
Ne: 9.1301E-06
Ar: 4.6906E-03
Kr: 5.7251E-07
```

Similarly, `get_isotopes()` yields the isotopic composition of a substance.
Additionally, the keyword argument `use_natural` can be used to represent the isotopic composition of a natural `Element` with a surrogate `Isotope` object.
This surrogate object represents an element with natural occuring abundance.
`use_natural=True` applies this behaviour to all natural elements.
Alternatively, a collection (iterable) of natural `Element` objects can be passed as the argument, limiting the behaviour to those specified.
Note that custom made elements are not subject to that behaviour, unless the keyword argument `natural=True` was specified in their constructor.
The (atomic) isotopic composition of air - considering natural oxygen as one - can be fetched with the following code:

```python
isotope_vector = air.get_isotopes(mode="atomic", use_natural=(iso.O_nat,))
for isotope, at_frac in isotope_vector.items():
    isotope_name = isotope.name.replace("-0", "-nat")  # surrogate Isotopes have a mass number of zero
    print(f"{isotope_name:>6}: {at_frac:.4E}")
```

yields the isotope vector (with all oxygen isotopes, that are part of a natural composition `Element`, being condensed into a surrogate `Isotope` object):

```
   H-1: 3.7560E-06
   H-2: 4.3200E-10
  He-3: 3.5263E-12
  He-4: 2.6315E-06
  C-12: 2.0811E-04
  C-13: 2.2508E-06
  N-14: 7.8143E-01
  N-15: 2.8548E-03
 O-nat: 2.1080E-01
   [...]
```

The composition can also be printed in a tree-hierarchy.
Both `atomic` and `weight` fractions can be fetched and are limited to `Element` and `Isotope` objects.
The following code

```python
air.print_tree_composition(weight=True)
```

yields the composition tree:

```
Mixture "air": 28.9660 g/mol
├── Molecule "molecular nitrogen": 28.0134 g/mol
│   └── Element "natural nitrogen":  78.4281 at.%  |   75.5097 wt.%  |  14.0067 g/mol
│       ├── Isotope   "N-14":  78.1426 at.%  |   75.2154 wt.%  |  14.0031 g/mol
│       └── Isotope   "N-15":   0.2855 at.%  |    0.2943 wt.%  |  15.0001 g/mol
├── Molecule "molecular oxygen": 31.9988 g/mol
│   └── Element "natural oxygen":  21.0383 at.%  |   23.1372 wt.%  |  15.9994 g/mol
│       ├── Isotope   "O-16":  20.9872 at.%  |   23.0744 wt.%  |  15.9949 g/mol
│       ├── Isotope   "O-17":   0.0080 at.%  |    0.0093 wt.%  |  16.9991 g/mol
│       └── Isotope   "O-18":   0.0431 at.%  |    0.0534 wt.%  |  17.9992 g/mol
├────── Element "natural argon":   0.4691 at.%  |    1.2880 wt.%  |  39.9478 g/mol
│       ├── Isotope  "Ar-36":   0.0016 at.%  |    0.0039 wt.%  |  35.9675 g/mol
│       ├── Isotope  "Ar-38":   0.0003 at.%  |    0.0008 wt.%  |  37.9627 g/mol
│       └── Isotope  "Ar-40":   0.4672 at.%  |    1.2834 wt.%  |  39.9624 g/mol
├── Molecule "carbon dioxide": 44.0095 g/mol
│   ├── Element "natural carbon":   0.0209 at.%  |    0.0173 wt.%  |  12.0107 g/mol
│   │   ├── Isotope   "C-12":   0.0207 at.%  |    0.0171 wt.%  |  12.0000 g/mol
│   │   └── Isotope   "C-13":   0.0002 at.%  |    0.0002 wt.%  |  13.0034 g/mol
│   └── Element "natural oxygen":   0.0419 at.%  |    0.0461 wt.%  |  15.9994 g/mol
│       ├── Isotope   "O-16":   0.0418 at.%  |    0.0459 wt.%  |  15.9949 g/mol
│       ├── Isotope   "O-17":   0.0000 at.%  |    0.0000 wt.%  |  16.9991 g/mol
│       └── Isotope   "O-18":   0.0001 at.%  |    0.0001 wt.%  |  17.9992 g/mol
   [...]
```

Compared to the fetching algorithms shown before, these compositions are not summed for each `Element` or `Isotope`, but the percentage can be traced back to each individual component.
For example, the amount of "natural oxygen" and its `Isotope`s are listed in the `Molecule` "molecular oxygen" $(\mathrm{O_2})$ and the `Molecule` "carbon dioxide" $(\mathrm{CO_2})$ individually.


## Changelog

For a history of changes, refer to the file `CHANGELOG.md` in the source code distributions or directly on the [GitHub repository](https://github.com/jmercz/isoVec/blob/main/README.md).

## References

1. Coursey, J.S., Schwab, D.J., Tsai, J.J., and Dragoset, R.A. (2015), Atomic Weights and Isotopic Compositions (version 4.1). [Online] Available: https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses [Accessed 23 July 2023]. National Institute of Standards and Technology, Gaithersburg, MD.