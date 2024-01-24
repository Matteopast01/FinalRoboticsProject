from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree


class GoToNextPathNode(Behaviour):
  def __init__(self, name):
    super(GoToNextPathNode, self).__init__(name)


  def setup(self):
    self.logger.debug(f"GoToNextNode::setup {self.name}")

  def initialise(self):
    self.logger.debug(f"GoToNextNode::initialise {self.name}")

  def update(self):
    self.logger.debug(f"GoToNextNode::update {self.name}")

  def terminate(self, new_status):
    self.logger.debug(f"GoToNextNode::terminate {self.name} to {new_status}")

