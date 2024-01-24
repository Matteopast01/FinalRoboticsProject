from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.main import Controller


class SetEndGame(Behaviour):
    _controller: Controller

    def __init__(self, name, controller):
        super(SetEndGame, self).__init__(name)
        self._controller = controller

    def setup(self):
        self.logger.debug(f"SetEndGame::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"SetEndGame::initialise {self.name}")

    def update(self):
        self.logger.debug(f"SetEndGame::update {self.name}")

    def terminate(self, new_status):
        self.logger.debug(f"SetEndGame::terminate {self.name} to {new_status}")
