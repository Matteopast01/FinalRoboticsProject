from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class ComputeNodeAndPath(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(ComputeNodeAndPath, self).__init__(name)
        self._controller = controller

    def setup(self):
        self.logger.debug(f"ComputeNodeAndPath::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"ComputeNodeAndPath::initialise {self.name}")

    def update(self):
        self.logger.debug(f"ComputeNodeAndPath::update {self.name}")
        priority_queue = Knowledge().get_graph().get_priority_queue()
        while len(priority_queue) > 0:
            node = priority_queue.pop()
            path = Knowledge.get_graph().path_to_next_node(node)
            if len(path) > 0:
                Knowledge.set_path(path)
                return Status.SUCCESS
        return Status.FAILURE

    def terminate(self, new_status):
        self.logger.debug(f"ComputeNodeAndPath::terminate {self.name} to {new_status}")
