from typing import Any
from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
from isrlab_project.controller.behaviour_tree.CheckFinalGoal import CheckFinalGoal
from isrlab_project.controller.behaviour_tree.CheckPositionGoal import CheckPositionGoal
from isrlab_project.controller.behaviour_tree.ComputeNextNode import ComputeNextNode
from isrlab_project.controller.behaviour_tree.Error import Error
from isrlab_project.controller.behaviour_tree.GoNextNode import GoNextNode
from isrlab_project.controller.behaviour_tree.SetNewGoal import SetNewGoal


class BehaviorTree:
    _root: Any

    def __init__(self):
        self._create_bt()

    def _create_bt(self):

        #leaves
        go_next_node = GoNextNode(name="GoNextNode")
        compute_next_node = ComputeNextNode(name="ComputeNextNode")
        check_position_goal = CheckPositionGoal(name="CheckPositionGoal")
        error = Error(name="error")
        set_new_goal = SetNewGoal(name="SetNewGoal")
        check_final_goal = CheckFinalGoal(name="CheckFinalGoal")

        #level nodes
        root = Selector(name="selector", memory=True)

        sequence_2b_1l = Sequence(name="sequence2B1L", memory=True)
        sequence_3b_1l = Sequence(name="sequence3B1L", memory=True)

        selector_2b_2l = Selector(name="selector2B2L", memory=True)

        sequence_2b_3l = Sequence(name="sequence2B3L", memory=True)

        #add children
        sequence_2b_3l.add_children([set_new_goal])
        selector_2b_2l.add_children([error, sequence_2b_3l])
        sequence_2b_1l.add_children([selector_2b_2l, check_position_goal])
        sequence_3b_1l.add_children([go_next_node, compute_next_node])
        root.add_children([check_final_goal, sequence_2b_1l, sequence_3b_1l])

        self._root = root

    def tick(self):
        self._root.tick_once()
