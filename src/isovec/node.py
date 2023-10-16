"""Class for Node, its helper classes and legacy seperator strings.

The Node class is used to create tree structures of `Substance` objects.
The TreeCharSet class is a helper class to streamline different line styles in
the printing routine of `Node`. `big_sep`, `med_sep` and `sma_sep` are used in
legacy printing routines of `Element`, `Molecule` and `Mixture`.
"""

from __future__ import annotations

from typing import TypeAlias, Any, Union, TypeVar, Literal
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeCharSet:
    """Class for tree structure line ploting of class Node.
    
    It contains a set of characters for vertical lines, intersection lines,
    horizontal lines and angled lines (used for the last element of each level).
    """

    c_ver: str  # character vertical
    c_int: str  # character intersection
    c_hor: str  # character horizontal
    c_ang: str  # character angled

    @property
    def inter(self) -> str:
        """'Intersection' string for nodes that have further siblings."""
        return self.c_int + 2*self.c_hor + " "
    
    @property
    def last(self) -> str:
        """'Last' string for nodes that have no further siblings (are the last child)."""
        return self.c_ang + 2*self.c_hor + " "
    
    @property
    def fill(self) -> str:
        """'Filler' string to connect a node at a deeper level."""
        return 4*self.c_hor

    @property
    def vert(self) -> str:
        """'Vertical' string as horizontal filler for a child being printed at a deeper level."""
        return self.c_ver + 3*" "
    
    @property
    def empty(self) -> str:
        """'Empty' string as a horizontal filler for a child being printed at a deeper level for the last element."""
        return 4*" "

treeCharSets = {
    "basic": TreeCharSet("|", "+", "-", "+"),
    "box_drawings_light": TreeCharSet("\u2502", "\u251c", "\u2500", "\u2514"),
}
char_sets: TypeAlias = Literal["basic"] | Literal["box_drawings_light"]


Content: TypeAlias = Union[TypeVar("Substance"), TypeVar("Isotope")]

class Node:
    """Class to represent `Substance` and `Isotope` in hierarchical structure.
    
    Each node has a unique id, that is either the n-th created object (counter
    for class) or can be set manually. Printed is the label, that has to be set
    manually. Each node can have a parent and multiple children, representing
    the hierarchy and placing the node at a certain depth of it. Right alligned
    nodes will be printed at the maximum depth. Furthermore, each node can have
    content assigned to it, which is either of type `Substance` or `Isotope`.
    Optionally data may be specified in a dictionary.
    """

    _nodes = 0  # counter

    def __init__(self, label: str, parent: Node = None, content: Content = None,
                 id: Any = None, data: dict[str, float] = None
        ) -> None:
        """Constructor of node.

        Args:
            label:
                Descriptive name.
            parent:
                Parent node.
            content:
                Associated substance or isotope.
            id:
                Unique identifier.
            data:
                Associated data, containing additional information of the
                content.
        """
        
        self._nodes += 1

        self._id: Any
        self._label = label
        self._content: Content = content
        
        self._parent: Node | None = None
        self._depth: int
        self._children: list[Node] = []
        if data:
            self._data = data
        else:
            self._data = {}

        self._right_align = False

        if id is None:
            self._id = self._nodes
        else:
            self._id = id

        self.set_parent(parent)


    # ########
    # Properties
    # ########

    @property
    def id(self):
        """Unique Identifier."""
        return self._id
    
    @property
    def label(self):
        """Descriptive label."""
        return self._label
    
    @property
    def content(self):
        """Associated content."""
        return self._content
    
    @property
    def parent(self):
        """Parent node."""
        return self._parent
    
    @property
    def depth(self):
        """Depth of node in hierarchy."""
        return self._depth

    @property
    def children(self):
        """Children nodes."""
        return self._children
    
    @property
    def data(self):
        """Dictionary with additional data about content."""
        return self._data
    

    # ########
    # Construction
    # ########

    def set_parent(self, new_parent: Node | None) -> None:
        """Sets parent of node."""

        if self._parent is not None:
            self._parent._children.remove(self)  # remove itself from old parent

        self._parent = new_parent
        if new_parent is not None:
            new_parent._children.append(self)
        
        self._depth = self.count_depth()  # calculate depth

    def add_children(self, *args) -> None:
        """Adds children to node."""

        for arg in args:
            if isinstance(arg, Iterable):
                self.add_children(arg)
            elif isinstance(arg, Node):
                arg.set_parent(self)
            else:
                self.__class__(str(arg), content=arg, parent=self)

    def add_data(self, key: str, value: float) -> None:
        """Adds key-value (str-float) pair to data of node."""
        self._data[key] = value

    def align_right(self, value: bool = True, label_size: int = -1) -> None:
        """Set alignment of node to right (max depth).
        
        Args:
            value:
                Wheter node shall be right aligned.
            label_size:
                Fix size of node label, for better alignment.
        """

        self._right_align = value
        if label_size > 0:
            self._label = f"{self._label:>{label_size}}"

    
    # ########
    # Analysis
    # ########

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
        
    def count_depth(self) -> int:
        """Returns depth of node by counting parents, starting from 0."""
        
        if self._parent is None:
            return 0
        else:
            depth = 0
            cur_parent = self._parent
            while cur_parent is not None:
                 depth += 1
                 cur_parent = cur_parent._parent
            return depth
    
    def max_depth(self) -> int:
        """Returns maximal depth of node structure."""
        return max(node.depth for node in self)


    # ########
    # Fetch
    # ########

    def get_nodes_by_label(self, target: str) -> list[Node]:
        """Returns all nodes, which label equals target.
        
        Args:
            target:
                Label to search for.
                
        Returns:
            List of nodes which label matches target label.
        """
        return [node for node in self if node._label == target]

    def get_nodes_by_content(self, target: Content) -> list[Node]:
        """Returns all nodes, which content equals target.
        
        Args:
            target:
                Content object to search for.
                
        Returns:
            List of nodes which content matches target content.
        """
        return [node for node in self if node._content == target]


    # ########
    # Print
    # ########

    def print_tree(
            self, char_set: char_sets = "box_drawings_light", *, 
            frac_fmt: str = "8.4f", prop_fmt: str = ".4f"
        ) -> None:
        """Prints node structure as tree.
        
        Args:
            char_set:
                Character set that is used to print lines in the tree.
            frac_fmt:
                Format string to be used for fractions.
            prop_fmt:
                Format string to be used for physical properties.
        """

        def print_node(node: Node):

            # construct prefix string
            pre = ""
            if node.depth > 0:
                for last in last_ones[:node.depth-1]:
                    pre += tcs.empty if last else tcs.vert
                pre += tcs.last if last_ones[node.depth-1] else tcs.inter
            if node._right_align:  # align at max depth
                pre = pre.rstrip() + (max_depth-node.depth)*tcs.fill + " "

            # construct data string
            data_str = []
            for key, value in node.data.items():
                if key == "x":
                    data_str.append(f"{value*1e2:{frac_fmt}} at.%")
                elif key == "w":
                    data_str.append(f"{value*1e2:{frac_fmt}} wt.%")
                elif key == "phi":
                    data_str.append(f"{value*1e2:{frac_fmt}} vol.%")
                elif key == "M":
                    tmp = f"{value:{prop_fmt}} g/mol"
                    if "M_mol" in node.data:
                        value2 = node.data["M_mol"]
                        tmp += f" ({value2:{prop_fmt}} g/mol)"
                    data_str.append(tmp)
                elif key == "rho":
                    data_str.append(f"{value:{prop_fmt}} g/cm^3")
            data_str =  "  |  ".join(data_str)

            # actual print of current node
            label_str = f"\"{node.label.strip()}\""
            label_str_len = len(node.label) + 2
            print(f"{pre}{node.content.__class__.__name__} {label_str:>{label_str_len}}: {data_str}")

            # print children
            if node._children:
                last_ones[node._depth] = False
                for child in node._children[:-1]:
                    print_node(child)
                else:
                    last_ones[node._depth] = True
                print_node(node._children[-1])

        # get tree character set
        try:
            tcs = treeCharSets[char_set]
        except KeyError as ex:
            print("Unknown character set for tree plotting. Instead using default value.")
            tcs = treeCharSets["box_drawings_light"]

        # setup print variables
        max_depth = self.max_depth()
        last_ones = [False for i in range(max_depth)]

        # start recursive printing routine
        print_node(self)


    # ########
    # Operators
    # ########

    def __str__(self) -> str:
        return f"{self._label}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} of \"{repr(self._content)}\""
    
    def __eq__(self, other) -> bool:
        if type(self) is type(other):
            return self._id == other._id
        else:
            return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.__class__, self._id))
    
    def __iter__(self):
        if self.is_root():
            yield self
        for child in self._children:
            yield child
            yield from child.__iter__()
        


big_sep = "{0:64}".format("_" * 64)
med_sep = "{0:64}".format("-" * 64)
sma_sep = "{0:64}".format("- " * 32)