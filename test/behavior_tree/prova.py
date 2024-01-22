from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree


class Action(Behaviour):
  def __init__(self, name, update, max_attempt_count=1):
    super(Action, self).__init__(name)
    self._update = update
    self.max_attempt_count = max_attempt_count
    self.attempt_count = max_attempt_count

  def setup(self):
    self.logger.debug(f"Action::setup {self.name}")

  def initialise(self):
    self.attempt_count = self.max_attempt_count
    self.logger.debug(f"Action::initialise {self.name}")

  def update(self):
    return self._update(self)

  def terminate(self, new_status):
    self.logger.debug(f"Action::terminate {self.name} to {new_status}")


class Condition(Behaviour):
  def __init__(self, name, update):
    super(Condition, self).__init__(name)

  def setup(self):
    self.logger.debug(f"Condition::setup {self.name}")

  def initialise(self):
    self.logger.debug(f"Condition::initialise {self.name}")

  def update(self):
    self.logger.debug(f"Condition::update {self.name}")
    sleep(1)
    return Status.SUCCESS

  def terminate(self, new_status):
    self.logger.debug(f"Condition::terminate {self.name} to {new_status}")


def update_func_running(obj):
  obj.attempt_count -= 1
  obj.logger.debug(f"Action::update {obj.name}")
  sleep(1)
  if not obj.attempt_count:
    return Status.SUCCESS

  return Status.RUNNING

def update_func_failure(obj):
  obj.attempt_count -= 1
  obj.logger.debug(f"Action::update {obj.name}")
  sleep(1)
  return Status.SUCCESS

def make_bt():
  root = Selector(name="selector", memory=True)

  failure_action = Action("failure", update_func_failure)
  other_action = Action("other", update_func_running)
  root.add_children([failure_action, other_action])

  return root


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