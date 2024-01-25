from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class FindQrCode(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(FindQrCode, self).__init__(name)
        self._controller = controller

    def setup(self):
        self._controller.print_log(f"FindQrCode::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"FindQrCode::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"FindQrCode::update {self.name}")
        self._controller.perform_action("stop")
        if Knowledge().get_arrived_data()["arrived"]:
          return Status.SUCCESS
        else:
          self._controller.perform_action("turn_left")
          return Status.RUNNING

    def terminate(self, new_status):
        self._controller.print_log(f"FindQrCode::terminate {self.name} to {new_status}")
