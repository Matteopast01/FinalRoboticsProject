from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.main import Controller


class IsThereAComputedPath(Behaviour):
    _controller: Controller

    def __init__(self, name, controller):
        super(IsThereAComputedPath, self).__init__(name)
        self_controller = controller

    def setup(self):
        self.logger.debug(f"IsThereAComputedPath::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"IsThereAComputedPath::initialise {self.name}")

    def update(self):
        self.logger.debug(f"IsThereAComputedPath::update {self.name}")

    def terminate(self, new_status):
        self.logger.debug(f"IsThereAComputedPath::terminate {self.name} to {new_status}")
