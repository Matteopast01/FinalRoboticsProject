from typing import Any
from time import sleep
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Sequence
from py_trees.composites import Selector
from py_trees import logging as log_tree
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


class BehaviourTree:
    _root: Any

    def __init__(self, controller_handle):
        self._create_bt(controller_handle)

    def _create_bt(self, controller_handle):
        # leaves
        checkEndGame = CheckEndGame(name="CheckEndGame", controller = controller_handle)
        setCurrentPosition = SetCurrentPosition(name="SetCurrentPosition", controller = controller_handle)
        addNewNodes = AddNewNodes(name="AddNewNodes", controller = controller_handle)
        checkPositionalGoal = CheckPositionGoal(name="CheckPositionalGoal", controller = controller_handle)
        error2B = Error(name="Error2B", controller = controller_handle)
        findQrCode = FindQrCode(name="FindQrCode", controller = controller_handle)
        checkFinalGoal = CheckFinalGoal(name="checkFinalGoal", controller = controller_handle)
        setEndGame = SetEndGame(name="SetEndGame", controller = controller_handle)
        setNewGoal = SetNewGoal(name="SetNewGoal", controller = controller_handle)
        resetPriorityQueue = ResetPriorityQueue(name="ResetPriorityQueue", controller = controller_handle)
        isThereAComputedPath = IsThereAComputedPath(name="IsThereAComputedPath",controller = controller_handle)
        computeNodeAndPath = ComputeNodeAndPath(name="ComputeNodeAndPath", controller = controller_handle)
        error3B = Error(name="error3B", controller = controller_handle)
        goToNextPathNode = GoToNextPathNode(name="GoToNextPathNode", controller = controller_handle)

        # level nodes
        sequence5L1B = Sequence(name="sequence5L1B", memory=True)
        sequence5L2B = Sequence(name="sequence5L1B", memory=True)
        selector4L2B = Selector(name="selector4L2B", memory=True)
        sequence3L1B = Sequence(name="sequence3L1B", memory=True)
        selector2L4B = Selector(name="selector2L4B", memory=True)
        sequence1L2B = Sequence(name="sequence1L2B", memory=True)
        sequence1L3B = Sequence(name="sequence1L3B", memory=True)
        selector2L1B = Selector(name="selector2L1B", memory=True)
        sequence2L2B = Sequence(name="sequence2L2B", memory=True)
        root = Sequence(name="root", memory=True)


        # add children
        sequence5L1B.add_children([checkFinalGoal,setEndGame])
        sequence5L2B.add_children([setNewGoal,resetPriorityQueue])
        selector4L2B.add_children([sequence5L1B, sequence5L2B])
        sequence3L1B.add_children([findQrCode, selector4L2B])
        selector2L4B.add_children([sequence3L1B, error2B])
        sequence1L2B.add_children([setCurrentPosition, addNewNodes,checkPositionalGoal,selector2L4B])
        selector2L1B.add_children([isThereAComputedPath,computeNodeAndPath,error3B])
        sequence2L2B.add_children([goToNextPathNode])
        sequence1L3B.add_children([selector2L1B,sequence2L2B])
        root.add_children([checkEndGame,sequence1L2B,sequence1L3B])


        self._root = root

    def tick(self):
        self._root.tick_once()
