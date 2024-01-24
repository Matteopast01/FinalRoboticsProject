from time import sleep
from time import time
import numpy as np
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.Knowledge import Knowledge


class SetCurrentPosition(Behaviour):
  def __init__(self, name):
    super(SetCurrentPosition, self).__init__(name)


  def setup(self):
    self.logger.debug(f"SetCurrentPosition::setup {self.name}")

  def initialise(self):
    self.logger.debug(f"SetCurrentPosition::initialise {self.name}")

  def update(self):
    self.logger.debug(f"SetCurrentPosition::update {self.name}")
    orientation = Knowledge().get_orientation()
    action = Knowledge().get_action()
    last_position = Knowledge().get_current_node()
    start_action_time = Knowledge().get_start_action_time()
    now = time()
    speed = Knowledge().read_config_var("SPEED")
    if action == "go_forward":
      space = (now - start_action_time) * speed
      x_pos = last_position[0] + space * np.cos(orientation)
      y_pos = last_position[1] + space * np.sin(orientation)
      Knowledge().set_current_node((x_pos, y_pos))
    return Status.SUCCESS


  def terminate(self, new_status):
    self.logger.debug(f"SetCurrentPosition::terminate {self.name} to {new_status}")
