from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from Knowledge import Knowledge
from py_trees import logging as log_tree


class WriteNode(Behaviour):
    _count: int

    def __init__(self, name):
        super(WriteNode, self).__init__(name)
        self._count = 0

    def setup(self):
        print(f"WriteNode::setup {self.name}")

    def initialise(self):
        print(f"WriteNode::initialise {self.name}")

    def update(self):
        print(f"WriteNode::update {self.name}")
        self._count += 1
        return Status.SUCCESS

    def terminate(self, new_status):
        print(f"WriteNode::terminate {self.name} to {new_status}")
