
# Changelog

## Version 1.2.1 (xx/11/2023)

- added `copy()` function to `Substance`
	- deep-copy of the substance
	- keyword arguments to change properties are:
		- `name` for the descriptive name
		- `symbol` for the symbol
		- `rho` for density
		- `M` for molar mass



## Version 1.2.0.1 (03/11/2023)

- fixed typos in "README.md"



## Version 1.2.0 (03/11/2023)

This update features a major overhaul of the routines to fetch isotopic (and elemental) compositions.
Atomic fractions of `Molecule`s in `Mixture`s cannot be passed down directly.
This would underestimate the atomic fraction of the `Element`s of that `Molecule`.
Instead, all `Element`s have to be collected according to their actual atomic abundance and subsequently be normalised.
When the composition input mode was `weight` and the isotopic composition was fetched in `weight` as well, values were **correct** (because of back and forth conversion).
Update 1.1.1 was ment to adress the faulty isotopic composition, when fetched in ´atomic´ mode, but introduced other errors and is thus discouraged to be used.
The respective releases on PyPI therefore have been yanked.
This new approach also required changes to the tree-printing routine.
`print_tree()` has been replaced by `print_tree_input()`, that acts like the old `print_tree(scale=False)`.
To show the actual (scaled) elemental and isotopic composition, `print_tree_composition()` has to be used.

- added `get_elements()` method to `Substance` for elemental composition of that `Substance`
	- keyword `mode` for either "atomic" or "weight" fractions
- added option for `get_isotopes()` to supply explicit collection of (natural) elements to be considered
	- removed the internal method `_append_isotopes()`
	- instead uses `_isotopic_composition()`, `_elemental_composition()` and `_append_elements()` to get correct (atomic) composition
		- `_isotopic_composition()`, `_elemental_composition()` return a dictionary, matching the position in the tree hierarchy to the `Isotope` or `Element` and their fraction respectively
- added `surrogate_isotope()` method to `Element` to get a surrogate `Isotope` object in case of a natural element (used for `use_natural` algorithm)
- removed `print_overview()` from `Mixture`, `Molecule` and `Element`, because it doesn't comply with the new approach and has been superseded by tree-printing
- `Node`s in the tree use their position in the tree-hierarchy as their id
- replaced `print_tree()` with
	- `print_tree_input()`
		- shows input composition in selected fraction modes (`atomic`, `weight` and `volume`)
		- similar to old `print_tree(scale=False)`
	- `print_tree_composition()`
		- shows scaled composition of `Element`s and `Isotopes`s of a `Substance`
		- possible fraction modes: `atomic` and `weight`
		- uses `Node` id to fetch the correct composition value from `_isotopic_composition()` or `_elemental_composition()` dictionary
- added more sophisticated right alignment options for tree-plotting
	- added `_print_depth()` method for `Node` class, to get desired level of printing that `Node` object
	- new prefix generation in `print_node()` of `Node` class
	- right-alignment-preference class variable for `Substance`
	- `Element`s and `Isotope`s are respectively right aligned in `print_tree_composition()`
- added internal conversion consistency case to "validation.py"
- added detailed air case to "validation.py"



## Version 1.1.1.1 (16/10/2023)

- fixed problem with tree plotting of molecules, that lead to wrong atomic isotope vectors
	- changed molar mass of molecule to average molar mass (as other substances)
	- added molar mass of molecule (is calculated as before)
	- added `_get_data_dict()` to `Substance` (and `Molecule`) for more flexibility in tree plotting
- added option for `get_isotopes()` to supply explicit collection of (natural) elements to be considered


## Version 1.1.1 (16/10/2023)

- fixed problem with molar mass of molecules, that lead to wrong atomic isotope vectors
	- changed molar mass of molecule to average molar mass (as other substances)
	- added molar mass of molecule (is calculated as before)
	- added `_get_data_dict()` to `Substance` (and `Molecule`) for more flexibility in tree plotting
- added option for `get_isotopes()` to supply explicit collection of (natural) elements to be considered


## Version 1.1.0 (18/08/2023)

This updates marks a big overhaul of the code structure.
`Element`, `Molecule` and `Mixture` now inherit from the abstract base class `Substance`.
This will help in terms of future maintainability.
Volume fractions are introduced as a possible input for `Mixture`s.
All modules, classes, methods and constants received docstrings for documentation and a more helpful API.
Now, all isotopes from the NIST database are implemented, increasing the available `Isotope` object count from 357 to 3355.
Added `Node` class for easier access to hierarchical tree structure of substances.
Furthermore, this class allows a tree structure print, that should be clearer than previous print methods.
`Isotope`, `Substance` and all subclasses received various additional attributes and methods for enhanced functionality.


### Isotope

- changes to `Isotope`:
	- added attribute relative atomic mass `A_r`
		- molar mass `M` is calculated via `A_r` and molar mass constant `M_u` (according to 2019 redefinitions)
	- added isomeric state `I`
	- added property `ZA` (notation)
	- added property `ZAI` (notation)
	- name is not longer a positional argument in constructor and is generated automatically, but can be overriden with `name` keyword
	- added `element_symbol()` method to get symbol of associated element
- added all isotopes from [NIST database](https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses)
	- total amount: 3355 isotopes


### Substance and subclasses

- `Substance` base class for maintainability
	- unified attributes and methods where possible
	- renaming of internal variables to consent with physical quantities
		- attribute `constituents` is now called more appropriately `composition`
	- added attribute for density `rho` (necessary for volume fraction conversions)
		- can generally not be calculated and must be given explicitly during construction (as keyword argument)
	- added attribute `symbol` for shorter names
	- added constructor argument `mode` for "atomic", "weight" and "volume" fractions as input
		- added dedicated constructor wrappers: `from_atomic()`, `from_weight()` and `from_volume()`
	- constructor checks, if given constituents are allowed
	- added methods to return compositions in weight fractions (`get_composition_in_wt()`) and volume fractions (`get_composition_in_vol()`)
	- added properties for molar volume `V_m` and number density `n`
		- added methods to compute those values
	- added methods `make_node()` and `print_tree()` for querrying and printing (see class `Node` below)
	- changes to `get_isotopes()` method
		- keyword `mode` for either "atomic" or "weight" fractions
		- keyword `use_natural` to return elemental composition (only for natural elements)
- changes to `Element`:
	- constituents in composition limited to `Isotope` objects
	- added attribute `is_natural` to mark implemented natural elements, that can alter the behaviour in `get_isotopes()` method
	- added attribute `Z` as atomic number (similar to `Isotope`)
	- added attribute relative atomic mass `A_r`
		- is calculated as weighted mean from its composition
	- added `element_symbol()` method to get `symbol`
		- is used to generate `symbol` automatically
- changes to `Molecule`:
	- constituents in composition limited to `Element` objects
	- added attribute `atoms` to track number of atoms
	- added property `constituent_atoms` that returns composition dictionary not with fractions, but with number of each `Element`
	- `symbol` is automatically generated by its elements and their count (rough estimate of chemical symbol)
- changes to `Mixture`:
	- constituents in composition limited to `Element`, `Molecule` and `Mixture` objects
	- tries to calculate attribute `rho` by itself
		- only possible if all constituents have a density given
	- only use case for new volume fractions


### Node

- added `Node` class for easier access to hierarchical tree structure of substances
	- access `Substance` or `Isotope` via the attribute `content`
	- additional information, like calculated (scaled) fractions, is stored in dictionary attribute `data`
		- keys: atomic fraction (`"x"`), weight fraction (`"w"`), volume fraction (`"phi"`), molar mass (`"M"`) and density (`"rho"`), 
	- querry tree structure via:
		- `get_nodes_by_label()`: search for name of `Node`
		- `get_nodes_by_content()`: search for `Substance` or `Isotope` object
		- returns a list of `Node`s that match criterion
	- `print_tree()` method to print tree structure as such
		- additional `data` is printed as well
		- successor to `print_overview()` method


### General

- added docstrings (in accordance to [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html))
	- better documentation
	- improvements for API
- added all possible conversion methods for atomic and weight fractions, as well as newly introduced volume fractions
- changed official required Python version to 3.10 (might not be necessary)
- updated README and its tutorial to reflect changes and improvements
- removed custom exceptions (using default ones instead) and "exceptions.py"
- removed "printer.py"; separator strings are in "node.py"
- created "constants.py" for physical constants and mapping dictionaries for symbol and names of elements
- added volume fraction case to "validation.py"
- added comparison tables (package *tabular*) to "validation.py"
- ... probably lots of other stuff I've missed



## Version 1.0.2 (12/07/2023)

The whole source code was adjusted to the PEP 8 Style Guide for Python Code.
This was no easy choice, as it would obviously break parts of the API.
However, isoVec is still a fairly new package and the user base therefore is most likely slim to none.
In favour of more consistency with standard and other popular Python packages, as well as future maintainability, the style of this package was changed.
Presumably, changes for users will be limited to the `PrintOverview` method (now `print_overview`) and the `GetIsotopes` method (now `get_isotopes`).


- adjusted naming convections to PEP 8 style guide (Docstrings will follow in the near future, presumably
- fixed a bug, when `get_isotopes` is called sequentially
	- the dictionary would unintentionally clutter up with isotopes from former calls
	- since dictionaries are mutable objects and Python compiles functions (and thus their default values) at the beginning, the very same dictionary is used every call, even though an empty one should be created
	- this beahviour is described nicely in an [article by Don Cross](https://towardsdatascience.com/python-pitfall-mutable-default-arguments-9385e8265422)



## Version 1.0.1 (20/06/2023)

- added conversion functions:
	- percent (per hundred): `percent`, `perc`, `pc`
	- per mille (per thousand): `permille`, `pm`
	- per myriad (per ten thousand): `permyriad`, `bp`
	- per cent mille (per hundred thousand): `percentmille`, `pcm`
	- parts-per-million: `ppm`
	- parts-per-billion: `ppb`
	- parts-per-trillion: `ppt`
	- parts-per-quadrillion: `ppq`



## Version 1.0.0 (14/06/2023)

- initial release