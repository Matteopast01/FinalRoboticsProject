from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from Knowledge import Knowledge


class ReadNode(Behaviour):

    def __init__(self, name):
        super(ReadNode, self).__init__(name)

    def setup(self):
        print(f"ReadNode::setup {self.name}")

    def initialise(self):
        print(f"ReadNode::initialise {self.name}")

    def update(self):
        print(f"ReadNode::update {self.name}")
        return Status.SUCCESS

    def terminate(self, new_status):
        print(f"ReadNode::terminate {self.name} to {new_status}")
