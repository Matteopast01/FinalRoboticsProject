from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree


class AddNewNodes(Behaviour):
  def __init__(self, name):
    super(AddNewNodes, self).__init__(name)


  def setup(self):
    self.logger.debug(f"AddNewNodes::setup {self.name}")

  def initialise(self):
    self.logger.debug(f"AddNewNodes::initialise {self.name}")

  def update(self):
    self.logger.debug(f"AddNewNodes::update {self.name}")

  def terminate(self, new_status):
    self.logger.debug(f"AddNewNodes::terminate {self.name} to {new_status}")

from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge
from isrlab_project.controller.main import Controller


class AddNewNodes(Behaviour):
    _controller: Controller

    def __init__(self, name, controller):
        super(AddNewNodes, self).__init__(name)
        self._controller = controller

    def setup(self):
        self.logger.debug(f"AddNewNodes::setup {self.name}")

    def initialise(self):
        self.logger.debug(f"AddNewNodes::initialise {self.name}")

    def update(self):
        self.logger.debug(f"AddNewNodes::update {self.name}")
        for side in ["left", "right", "center"]:
            current_node = Knowledge().get_current_node()
            delta = Knowledge().get_delta_pos_neighbors(side)
            new_node_x = current_node[0] + delta[0]
            new_node_y = current_node[1] + delta[1]
            new_node = (new_node_x, new_node_y)
            Knowledge().add_neighbors(side, new_node)
            Knowledge().get_graph().add_node(current_node, new_node)
        return Status.SUCCESS

    def terminate(self, new_status):
        self.logger.debug(f"AddNewNodes::terminate {self.name} to {new_status}")
