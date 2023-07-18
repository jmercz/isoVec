
from __future__ import annotations
from typing import TypeAlias, Any
from collections.abc import Iterable

from .isotope import Isotope
from .substance import Substance

c_ver = "\u2502"
c_int = "\u251c"
c_hor = "\u2500"
c_ang = "\u2514"


Content: TypeAlias = Substance | Isotope

class Node:

    _nodes = 0

    def __init__(self, name: str, content: Content = None, parent: Node = None, id: Any = None, **kwargs) -> None:
        
        self._nodes += 1

        self._name = name

        if id is None:
            self._id = self._nodes
        else:
            self._id = id

        self._content: Content = content

        self._parent: Node = parent
        self._children: list[Node] = []

        self._fractions: dict[str, float] = {}
        self._search_dict_for_fracs(kwargs)


    @property
    def id(self) -> Any:
        """Returns identifier of node."""
        return self._id
    
    @property
    def content(self) -> Content:
        """Returns content of node."""
    
    @property
    def parent(self) -> Node:
        """Returns parent of node."""
        return self._parent

    @property
    def children(self) -> list[Node]:
        """Returns children of node."""
        return self._children
    
    @property
    def fractions(self) -> dict[str, float]:
        """Returns dictionary with available fractions."""
        return self._fractions
    

    def set_parent(self, new_parent: Node) -> None:
        """Sets parent of node."""

        if self._parent is not None:
            self._parent._children.remove(self)  # remove itself from old parent

        self._parent = new_parent

    def add_children(self, *args) -> None:
        """Adds children to node."""

        for arg in args:
            if isinstance(arg, Iterable):
                self.add_children(arg)
            elif isinstance(arg, Node):
                arg.set_parent(self)
                self._children.append(arg)
            else:
                self.__class__(str(arg), content=arg, parent=self)


    def is_root(self) -> bool:
        """Returns if node is root node (first)."""

        if self._parent is None:
            return True
        else:
            return False
    
    def is_leaf(self) -> bool:
        """Returns if node is leaf node (last)."""

        if not self._children:
            return True
        else:
            return False
        

    def _search_dict_for_fracs(self, search_dict: dict[str, float]) -> None:
        """Search in dictionary for fraction keywords and save fraction."""

        for key, value in search_dict.items():

            # atomic (mole) fraction
            if key in {"x", "atomic", "at", "mole", "mol"}:
                self._fractions["x"] = value

            # weight fraction
            elif key in {"w", "weight", "wt"}:
                self._fractions["w"] = value

            # volume fraction
            elif key in {"phi", "volume", "vol"}:
                self._fractions["phi"] = value

    def __str__(self) -> str:
        return f"{self._}"
    
    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self._id == other._id
        else:
            return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self._id)



big_sep = "{0:64}".format("_" * 64)
med_sep = "{0:64}".format("-" * 64)
sma_sep = "{0:64}".format("- " * 32)