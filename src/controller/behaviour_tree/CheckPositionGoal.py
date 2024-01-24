from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge
from isrlab_project.controller.main import Controller


class CheckPositionGoal(Behaviour):
    _controller: Controller
    def __init__(self, name, controller):
        super(CheckPositionGoal, self).__init__(name)
        self._controller = controller
    def setup(self):
        self.logger.debug(f"CheckPositionGoal::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"CheckPositionGoal::initialise {self.name}")

    def update(self):
        self.logger.debug(f"CheckPositionGoal::update {self.name}")
        current_node = Knowledge().get_current_node()
        goal_node = Knowledge().get_goal()
        reached_goal_node = Knowledge().get_graph().is_nodes_position_equals(current_node, goal_node)
        if reached_goal_node:
            self._controller.perform_action("stop")
            return Status.SUCCESS
        else:
            return Status.FAILURE


    def terminate(self, new_status):
        self.logger.debug(f"CheckPositionGoal::terminate {self.name} to {new_status}")
