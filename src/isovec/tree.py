
from __future__ import annotations
from typing import TypeAlias, Any, Union, TypeVar
from collections.abc import Iterable

c_ver = "\u2502"
c_int = "\u251c"
c_hor = "\u2500"
c_ang = "\u2514"
node_lines = {
    "inter": c_int + 2*c_hor + " ",
    "last":  c_ang + 2*c_hor + " ",
    "fill":  4*c_hor,
    "vert":  c_ver + 3*" ",
    "empty": 4*" ",
}

Substance = TypeVar("Substance")
Isotope = TypeVar("Isotope")
Content: TypeAlias = Union[Substance, Isotope]

class Node:

    _nodes = 0

    def __init__(self, label: str, parent: Node = None, content: Content = None, id: Any = None, 
                 data: dict[str, float] = None, **kwargs) -> None:
        
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




    @property
    def id(self):
        """Returns identifier of node."""
        return self._id
    
    @property
    def label(self):
        """Returns label of node."""
        return self._label
    
    @property
    def content(self):
        """Returns content of node."""
        return self._content
    
    @property
    def parent(self):
        """Returns parent of node."""
        return self._parent
    
    @property
    def depth(self):
        """Returns depth of node."""
        return self._depth

    @property
    def children(self):
        """Returns children of node."""
        return self._children
    
    @property
    def data(self):
        """Returns dictionary with available data."""
        return self._data
    

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

    def align_right(self, value: bool = True) -> None:
        """Set alignment of node to right (max depth)."""
        self._right_align = True


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
        
    def _append_to(self, collection: list[Node]) -> None:
        """Append itself and children to list of nodes."""
        
        collection.append(self)
        for child in self._children:
            child._append_to(collection)


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
        for child in self._children:
            yield child


class Tree:
    
    def __init__(self, root: Node) -> None:
        
        self._root = root
        self._max_depth = self.count_max_depth()

    


    def flat(self) -> list[Node]:

        flat_list = []
        self._root._append_to(flat_list)

        return flat_list


    def count_max_depth(self) -> int:

        return max(node.depth for node in self.flat())


    
        


    def print(self) -> None:

        def print_node(node: Node):

            # construct prefix string
            pre = ""
            if node.depth > 0:
                for last in last_ones[:node.depth-1]:
                    pre += node_lines["empty"] if last else node_lines["vert"]
                pre += node_lines["last"] if last_ones[node.depth-1] else node_lines["inter"]
            if node._right_align:  # align at max depth
                pre = pre.rstrip() + (self._max_depth-node.depth)*node_lines["fill"] + " "

            # construct data string
            data_str = []
            for key, value in node.data.items():
                if key == "x":
                    data_str.append(f"{value*1e2:8.4f} at.%")
                if key == "w":
                    data_str.append(f"{value*1e2:8.4f} wt.%")
                if key == "phi":
                    data_str.append(f"{value*1e2:8.4f} vol.%")
                if key == "M":
                    data_str.append(f"{value:.4f} g/mol")
                if key == "rho":
                    data_str.append(f"{value:.4f} g/cm^3")
            data_str = "  |  ".join(data_str)

            # actual print of current node
            print(f"{pre}{node.content.__class__.__name__} \"{node.label}\": {data_str}")

            # print children
            if node._children:
                last_ones[node._depth] = False
                for child in node._children[:-1]:
                    print_node(child)
                else:
                    last_ones[node._depth] = True
                print_node(node._children[-1])

        last_ones = [False for i in range(self._max_depth)]
        print_node(self._root)

        


big_sep = "{0:64}".format("_" * 64)
med_sep = "{0:64}".format("-" * 64)
sma_sep = "{0:64}".format("- " * 32)