from time import sleep
from typing import Any

from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree


class CheckFinalGoal(Behaviour):
    _controller: Any

    def __init__(self, name, controller):
        super(CheckFinalGoal, self).__init__(name)
        self._controller = controller

    def setup(self):
        self._controller.print_log(f"CheckFinalGoal::setup {self.name}")

    def initialise(self):
        self._controller.print_log(f"CheckFinalGoal::initialise {self.name}")

    def update(self):
        self._controller.print_log(f"CheckFinalGoal::initialise {self.name}")
        text_to_decode = ""
        decoded_text = ""
        if decoded_text == "prova":
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        self._controller.print_log(f"CheckFinalGoal::terminate {self.name} to {new_status}")

def make_bt():
  root = Selector(name="root", memory=True)

if __name__ == "__main__":
  log_tree.level = log_tree.Level.DEBUG
  tree = make_bt()
  try:
    print("New Tick")
    tree.tick_once()
    sleep(0.1)
    print("New Tick")
    tree.tick_once()
    sleep(0.1)
    print("New Tick")
    tree.tick_once()
    sleep(0.1)
    print("New Tick")
    tree.tick_once()
  except KeyboardInterrupt:
    pass