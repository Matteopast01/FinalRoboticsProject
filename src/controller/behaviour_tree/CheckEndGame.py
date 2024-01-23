from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class CheckEndGame(Behaviour):
    def __init__(self, name):
        super(CheckEndGame, self).__init__(name)

    def setup(self):
        self.logger.debug(f"CheckEndGame::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"CheckEndGame::initialise {self.name}")

    def update(self):
        self.logger.debug(f"CheckEndGame::update {self.name}")
        if Knowledge().get_end_game():
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        self.logger.debug(f"CheckEndGame::terminate {self.name} to {new_status}")
