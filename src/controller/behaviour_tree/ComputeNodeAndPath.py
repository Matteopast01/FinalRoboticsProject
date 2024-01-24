from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree


class ComputeNodeAndPath(Behaviour):
  def __init__(self, name):
    super(ComputeNodeAndPath, self).__init__(name)


  def setup(self):
    self.logger.debug(f"ComputeNodeAndPath::setup {self.name}")

  def initialise(self):
    self.logger.debug(f"ComputeNodeAndPath::initialise {self.name}")

  def update(self):
    self.logger.debug(f"ComputeNodeAndPath::update {self.name}")

  def terminate(self, new_status):
    self.logger.debug(f"ComputeNodeAndPath::terminate {self.name} to {new_status}")

