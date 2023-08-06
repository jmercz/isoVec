
# Changelog

## Version 1.1.0 ()

- A_r for `Isotope`; molar mass M is calculated via molar mass constant (according to 2019 redefinitions)
- added all isotopes from NIST database
- Substance base class for maintainability
- ZAI for `Isotope`
- Natural flag for `Element`
- volume mode for mixture
- tree structure
- `get_isotopes` with optional `mode` weight and `use_natural` for elemental composition (for natural elements)

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