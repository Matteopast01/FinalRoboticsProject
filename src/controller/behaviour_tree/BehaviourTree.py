from typing import Any
from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree

from isrlab_project.controller.behaviour_tree.CheckFinalGoal import CheckFinalGoal
from isrlab_project.controller.behaviour_tree.AddNewNodes import AddNewNodes
from isrlab_project.controller.behaviour_tree.CheckPositionGoal import CheckPositionGoal
from isrlab_project.controller.behaviour_tree.CheckFinalGoal import CheckFinalGoal
from isrlab_project.controller.behaviour_tree.Error import Error
from isrlab_project.controller.behaviour_tree.SetNewGoal import SetNewGoal
from isrlab_project.controller.behaviour_tree.ComputeNodeAndPath import ComputeNodeAndPath
from isrlab_project.controller.behaviour_tree.FindQrCode import FindQrCode
from isrlab_project.controller.behaviour_tree.GoToNextPathNode import GoToNextPathNode
from isrlab_project.controller.behaviour_tree.SetEndGame import SetEndGame
from isrlab_project.controller.behaviour_tree.CheckEndGame import CheckEndGame
from isrlab_project.controller.behaviour_tree.IsThereAComputedPath import IsThereAComputedPath
from isrlab_project.controller.behaviour_tree.ResetPriorityQueue import ResetPriorityQueue
from isrlab_project.controller.behaviour_tree.SetCurrentPosition import SetCurrentPosition


class BehaviorTree:
    _root: Any

    def __init__(self):
        self._create_bt()

    def _create_bt(self):
        # leaves
        checkEndGame = CheckEndGame(name="CheckEndGame")
        setCurrentPosition = SetCurrentPosition(name="SetCurrentPosition")
        addNewNodes = AddNewNodes(name="AddNewNodes")
        checkPositionalGoal = CheckPositionGoal(name="CheckPositionalGoal")
        error2B = Error(name="Error2B")
        findQrCode = FindQrCode(name="FindQrCode")
        checkFinalGoal = CheckFinalGoal(name="checkFinalGoal")
        setEndGame = SetEndGame(name="SetEndGame")
        setNewGoal = SetNewGoal(name="SetNewGoal")
        resetPriorityQueue = ResetPriorityQueue(name="ResetPriorityQueue")
        isThereAComputedPath = IsThereAComputedPath(name="IsThereAComputedPath")
        computeNodeAndPath = ComputeNodeAndPath(name="ComputeNodeAndPath")
        error3B = Error(name="error3B")
        goToNextPathNode = GoToNextPathNode(name="GoToNextPathNode")

        # level nodes

        # add children

        self._root = root

    def tick(self):
        self._root.tick_once()
