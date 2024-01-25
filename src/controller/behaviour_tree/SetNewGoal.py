from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from src.controller.Knowledge import Knowledge

class SetNewGoal(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(SetNewGoal, self).__init__(name)
        self._controller = controller

    def setup(self):
        self.logger.debug(f"SetNewGoal::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"SetNewGoal::initialise {self.name}")

    def update(self):
        self.logger.debug(f"SetNewGoal::update {self.name}")
        new_goal = tuple(Knowledge().get_arrived_data()["pos"])
        Knowledge().set_goal(new_goal)
        return Status.SUCCESS

    def terminate(self, new_status):
        self.logger.debug(f"SetNewGoal::terminate {self.name} to {new_status}")
