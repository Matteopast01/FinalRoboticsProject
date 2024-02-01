from time import time
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from random import random
from isrlab_project.controller.Knowledge import Knowledge


class GoToNextPathNode(Behaviour):
    _controller: Any
    _next_node: tuple
    _setted_next_node: bool
    _action: str

    def __init__(self, name, controller):
        super(GoToNextPathNode, self).__init__(name)
        self._controller = controller
        self._setted_next_node = False
        self._action = ""

    def setup(self):
        self._controller.print_log(f"GoToNextNode::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"GoToNextNode::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"GoToNextNode::update {self.name}")
        #center_node = 
        #left_node = Knowledge().get_neighbor("left")
        #right_node = Knowledge().get_neighbor("right")
        current_position = Knowledge().get_current_node()
        graph = Knowledge().get_graph()
        if not self._setted_next_node:
            self._next_node = Knowledge().get_path().pop(0)

        

        if graph.is_nodes_position_equals(current_position, self._next_node):
            self._setted_next_node = False
            Knowledge().set_start_action_time(time())
            return Status.SUCCESS
        if Knowledge().is_side_free("center") and graph.is_nodes_position_equals(Knowledge().get_neighbor("center"), self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("go_forward")
            Knowledge().set_start_action_time(time())
            self._action = ""
            return Status.SUCCESS
        elif self._action != "":
            self._setted_next_node = True
            self._controller.perform_action(self._action)
            Knowledge().set_start_action_time(time())
            return Status.SUCCESS
        elif Knowledge().is_side_free("left") and graph.is_nodes_position_equals(Knowledge().get_neighbor("left"), self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("turn_left")
            Knowledge().set_start_action_time(time())
            self._action = "turn_left"
            return Status.SUCCESS
        elif Knowledge().is_side_free("right") and graph.is_nodes_position_equals(Knowledge().get_neighbor("right"), self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("turn_right")
            Knowledge().set_start_action_time(time())
            self._action = "turn_right"
            return Status.SUCCESS
        else:
            self._setted_next_node = True
            Knowledge().set_start_action_time(time())
            if random() > 0.5:
                self._controller.perform_action("turn_left")
                self._action = "turn_left"
                return Status.SUCCESS
            else:
                self._controller.perform_action("turn_right")
                self._action = "turn_right"
                return Status.SUCCESS




    def terminate(self, new_status):
        self._controller.print_log(f"GoToNextNode::terminate {self.name} to {new_status}")
