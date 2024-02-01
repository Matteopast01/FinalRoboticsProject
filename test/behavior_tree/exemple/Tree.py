from typing import Any
from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from ReadNode import ReadNode
from WriteNode import WriteNode

class BehaviourTree:
    _root: Any

    def __init__(self):
        self._create_bt()

    def _create_bt(self):
        # leaves
        read_node = ReadNode(name="read_node")
        write_node = WriteNode(name="write_node")

        # level nodes
        root = Sequence(name="sequence0L1B", memory=False)

        # add children
        root.add_children([read_node, write_node])


        self._root = root

    def tick(self):
        self._root.tick_once()
