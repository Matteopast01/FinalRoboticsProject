from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class IsCenterNextNode(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(IsCenterNextNode, self).__init__(name)
        self._controller = controller

    def setup(self):
        self._controller.print_log(f"IsCenterNextNode::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"IsCenterNextNode::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"IsCenterNextNode::update {self.name}")
        graph = Knowledge().get_graph()
        next_node = Knowledge().get_next_node()
        current_node = Knowledge().get_current_node()
        self._controller.print_log(f"IsCenterNextNode:: next_node {next_node}, current_node {current_node}")
        if Knowledge().is_side_free("center") and graph.is_nodes_position_equals(Knowledge().get_neighbor("center"), next_node):
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        self._controller.print_log(f"IsCenterNextNode::terminate {self.name} to {new_status}")
