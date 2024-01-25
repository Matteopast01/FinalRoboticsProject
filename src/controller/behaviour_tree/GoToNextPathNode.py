from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from random import random
from isrlab_project.controller.main import Controller
from isrlab_project.controller.Knowledge import Knowledge


class GoToNextPathNode(Behaviour):
    _controller: Controller
    _next_node: tuple
    _setted_next_node: bool
    _action: str

    def __init__(self, name, controller):
        super(GoToNextPathNode, self).__init__(name)
        self._controller = controller
        self._setted_next_node = False

    def setup(self):
        self.logger.debug(f"GoToNextNode::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"GoToNextNode::initialise {self.name}")

    def update(self):
        self.logger.debug(f"GoToNextNode::update {self.name}")
        center_node = Knowledge().get_neighbor("center")
        left_node = Knowledge().get_neighbor("left")
        right_node = Knowledge().get_neighbor("right")
        current_position = Knowledge().get_current_node()
        graph = Knowledge().get_graph()
        if not self._setted_next_node:
            self._next_node = Knowledge().get_path()[-1] #TODO una volta scelto come implementare la coda va cambiato in accordo

        if graph.is_nodes_position_equals(current_position, self._next_node):
            self._setted_next_node = False
            return Status.SUCCESS
        if graph.is_nodes_position_equals(center_node, self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("go_forward")
            self._action = ""
            return Status.RUNNING
        elif self._action != "":
            self._setted_next_node = True
            self._controller.perform_action(self._action)
        elif graph.is_nodes_position_equals(left_node, self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("turn_left")
            self._action = "turn_left"
            return Status.RUNNING
        elif graph.is_nodes_position_equals(right_node, self._next_node):
            self._setted_next_node = True
            self._controller.perform_action("turn_right")
            self._action = "turn_right"
            return Status.RUNNING
        else:
            self._setted_next_node = True
            if random() > 0.5:
                self._controller.perform_action("turn_left")
                self._action = "turn_left"
                return Status.RUNNING
            else:
                self._controller.perform_action("turn_right")
                self._action = "turn_right"
                return Status.RUNNING



    def terminate(self, new_status):
        self.logger.debug(f"GoToNextNode::terminate {self.name} to {new_status}")
