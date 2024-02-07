from time import sleep
from typing import Any
import numpy as np
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class ComputeAction(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(ComputeAction, self).__init__(name)
        self._controller = controller

    def setup(self):
        self._controller.print_log(f"ComputeAction::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"ComputeAction::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"ComputeAction::update {self.name}")

        current_node = Knowledge().get_current_node()
        next_node = Knowledge().get_next_node()
        next_orientation = self.convert_angle(np.arctan2(next_node[1] - current_node[1], next_node[0] - current_node[0]))
        current_orientation = self.convert_angle(Knowledge().get_orientation())
        angle_to_perform = next_orientation - current_orientation
        self._controller.print_log(f"ComputeAction:: angle current {current_orientation} next {next_orientation}")
        self._controller.print_log(f"ComputeAction:: current node {current_node} next node {next_node}")
        if angle_to_perform > 0.15:
            if np.abs(angle_to_perform) < np.pi:
                Knowledge().set_action("turn_left")
            else:
                Knowledge().set_action("turn_right")
        elif angle_to_perform <= -0.15:
            if np.abs(angle_to_perform) < np.pi:
                Knowledge().set_action("turn_right")
            else:
                Knowledge().set_action("turn_left")
        else:
            if Knowledge().is_side_free("center"):
                Knowledge().set_action("go_forward")
            else:
                Knowledge().set_next_node(None)

        return Status.SUCCESS

    def convert_angle(self, angle):
        if angle < 0:
            return 2 * np.pi + angle
        return angle

    def terminate(self, new_status):
        self._controller.print_log(f"ComputeAction::terminate {self.name} to {new_status}")
