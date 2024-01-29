from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class CheckEndGame(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(CheckEndGame, self).__init__(name)
        self._controller = controller

    def setup(self):
        self._controller.print_log(f"CheckEndGame::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"CheckEndGame::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"CheckEndGame::update {self.name}")
        if Knowledge().get_end_game():
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        self._controller.print_log(f"CheckEndGame::terminate {self.name} to {new_status}")
