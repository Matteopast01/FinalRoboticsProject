from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class FinalQrCode(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(FinalQrCode, self).__init__(name)
        self._controller = controller

    def setup(self):
        self.logger.debug(f"FinalQrCode::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"FinalQrCode::initialise {self.name}")

    def update(self):
        self.logger.debug(f"FinalQrCode::update {self.name}")
        self._controller.perform_action("stop")
        if Knowledge().get_arrived_data()["arrived"]:
          return Status.SUCCESS
        else:
          self._controller.perform_action("turn_left")
          return Status.RUNNING

    def terminate(self, new_status):
        self.logger.debug(f"FinalQrCode::terminate {self.name} to {new_status}")
