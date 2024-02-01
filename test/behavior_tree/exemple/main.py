from Tree import BehaviourTree
from time import sleep
from py_trees import logging as log_tree

tree = BehaviourTree()
log_tree.level = log_tree.Level.DEBUG
while True:
    tree.tick()
    sleep(0.1)
