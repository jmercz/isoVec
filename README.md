# isoVec

## Description

isoVec is a framework to build complex mixtures, get atomic or weight percentages of each of its substances down to the isotopic composition (the isotopce vector, hence the name).
The information on atomic weight, as well as abundance of those isotopes in natural occuring elements, is from "*Atomic Weights and Isotopic Compositions with Relative Atomic Masses*" by the NIST Physical Measurement Laboratory [1].
This information is given in the form of `Isotope` and `Element` classes.
The user can create custom elements and specify the isotopic composition manually. `Element`s make up `Molecule`s and `Element`s and `Molecule`s can make up a `Mixture`.
A thorough example is given in Section Example.


## Installation

The source code of the most recent development version is hosted on [GitHub](https://github.com/jmercz/isoVec).
The binary installers and the source code of stable releases is available on the project site on the [Python Package Index (PyPI)](https://pypi.org/project/isovec) and can be simply installed from the repository via

```sh
pip install isovec
```

There are no additional dependencies other than core Python packages of Python 3.9.


## Example

The composition of the atmosphere of the Earth may serve as an example how to use isoVec.
The constituents and their atomic (mole) fractions are taken from the respective [Wikipedia](https://en.wikipedia.org/wiki/Atmosphere_of_Earth#Composition) article and are as of April 2022:

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
Thus, atomic and mole fractions are used interchangeably in the following.

Let's assume for the following that you import isoVec with the following (shorter) alias.
Keep in mind, that all content is packed inside the given namespace.

```python
import isovec as iso
```

### Element

Natural occuring elements are already implemented and can be accessed via its symbol and "_nat".
Nitrogen for example is called with `N_nat`.
For the sake of this tutorial, we will define nitrogen again by ourselfs.
Each isotope is acessed via the elements symbol, an underscore "\_" and its mass number (that is protons + neutrons).
Nitrogen-14 is therefore called via `N_14`.
Naturally, an `Element` can only be composed of its respective isotopes, that is `Isotope` objects with the same atomic number.
We can now create a custom `Element` with a name to identify and the composition as a dictionary:

```python
nitrogen = iso.Element("nitrogen", {
    iso.N_14: 9.963600E-01,
    iso.N_15: 3.640000E-03
})
```

Whenever you supply a composition, positive values refer to a atomic fraction (as done before), while negative values refer to a weight fraction.
Use whatever information is available or more convencient, but you **cannot** mix atomic and weight fractions inside one composition dictionary.
Also, the composition doesn't necessarily need to add up to one.
Instead, each fraction is normalised by the total sum of given fractions.

### Molecule

Straightforward, the composition for a molecule is the number of atoms per element.
Therefore, only positive values for the compoosition are reasonable here.
The atomic weight of a molecule is calculated automatically, but could be overwritten when supplying the kwargs key-value pair `atomic_wt=value` in the constructor.
However, this class isn't strictly limited to molecules, but can be used for crystalline or amorphous structures with a stochiometric distribution.
Using the implemented natural elements, the `Molecule` for carbon dioxide is given by a name identifier and the atomic composition:

```python
carbon_dioxide = iso.Molecule("carbon dioxide", {
    iso.C_nat: 1,
    iso.O_nat: 2
})
```

Likewise we generate the other molecules:

```python
methane = iso.Molecule("methane", {
    iso.C_nat: 1,
    iso.H_nat: 4
})
nitrogen2 = iso.Molecule("molecular nitrogen", { iso.N_nat: 2})
oxygen2 = iso.Molecule("molecular oxygen", { iso.O_nat: 2})
```

### Mixture

The air is now a mixture of several molecules and pure elements, as stated in the table from the introduction.
This `Mixture` is given by a name identifier and the composition, in this case atomic (which again doesn't necessarily need to add up).
In the following definition, we also utilise helper functions for conversion (an extensive list ca be found in the documentation):

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

A printed overview of all subcomponents can be obtained by invoking `print_overview()` ony any substance we want to inspect:

```python
air.print_overview(True)
```

which yields the following (excerpt of the) output:

```
________________________________________________________________

 Mixture "air"
  100.0000 at.%  |  100.0000 wt.%

----------------------------------------------------------------
1. Molecule "molecular nitrogen": 28.0134 g/mol
     78.0775 at.%  |   75.5097 wt.%
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1.1. Element "natural nitrogen": 14.0067 g/mol
       78.0775 at.%  |   75.5097 wt.%

1.1.1.    N-14:    77.7933 at.%  |   75.2154 wt.%
1.1.2.    N-15:     0.2842 at.%  |    0.2943 wt.%
----------------------------------------------------------------
2. Molecule "molecular oxygen": 31.9988 g/mol
     20.9443 at.%  |   23.1372 wt.%
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
2.1. Element "natural oxygen": 15.9994 g/mol
       20.9443 at.%  |   23.1372 wt.%

2.1.1.    O-16:    20.8934 at.%  |   23.0744 wt.%
2.1.2.    O-17:     0.0080 at.%  |    0.0093 wt.%
2.1.3.    O-18:     0.0429 at.%  |    0.0534 wt.%
----------------------------------------------------------------
3. Element "natural argon": 39.9478 g/mol
      0.9339 at.%  |    1.2880 wt.%

3.1.      Ar-36:    0.0031 at.%  |    0.0039 wt.%
3.2.      Ar-38:    0.0006 at.%  |    0.0008 wt.%
3.3.      Ar-40:    0.9302 at.%  |    1.2834 wt.%
----------------------------------------------------------------
4. Molecule "carbon dioxide": 44.0095 g/mol
      0.0417 at.%  |    0.0634 wt.%
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
4.1. Element "natural carbon": 12.0107 g/mol
        0.0139 at.%  |    0.0173 wt.%

4.1.1.    C-12:     0.0138 at.%  |    0.0171 wt.%
4.1.2.    C-13:     0.0001 at.%  |    0.0002 wt.%
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
4.2. Element "natural oxygen": 15.9994 g/mol
        0.0278 at.%  |    0.0461 wt.%

4.2.1.    O-16:     0.0277 at.%  |    0.0459 wt.%
4.2.2.    O-17:     0.0000 at.%  |    0.0000 wt.%
4.2.3.    O-18:     0.0001 at.%  |    0.0001 wt.%
----------------------------------------------------------------
   [...]
```

The overview splits up all subcomponents in a layered manner and gives their atomic and weight fractions, down to the isotopic composition.
This function has an optional flag to scale the subcomponents, that is `False` by default.
If scaled, it will yield the fraction of the subcomponent compared to the top-level component, where the function was invoked on.
In other words, the fractions are multiplicative *downwards*.
If not scaled, the fractions will only sum up on their respective layer, for example 4.1 and 4.2 would add up to 100 %.

### Isotope Composition

As can be seen above, this doesn't sum up the fractions for the single isotopes, something we might be interested in.
The method `get_isotopes()` can be called upon every component and yields an ordered dictionary with the isotopes and their respective summed atomic fractions.
For our mixture of air, the following code

```python
isotope_vector = air.get_isotopes()
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


## Changelog

For a history of changes, refer to the file `CHANGELOG.md` in the source code distributions or directly on the [GitHub repository](https://github.com/jmercz/isoVec/blob/main/README.md).

## References

1. Coursey, J.S., Schwab, D.J., Tsai, J.J., and Dragoset, R.A. (2015), Atomic Weights and Isotopic Compositions (version 4.1). [Online] Available: https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses [Accessed 23 July 2023]. National Institute of Standards and Technology, Gaithersburg, MD.