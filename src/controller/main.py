import json
from time import sleep
from typing import Any
import random
from isrlab_project.controller.Knowledge import Graph
from isrlab_project.ReadConfig import ReadConfig
import base64
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Bool

MOTION_WAIT = 0.5


class Controller(Node):
    _new_node_sub: Any
    _free_side_sub: Any
    _arrived_sub: Any
    _knowledge_graph: Graph
    _is_acting: bool
    _action_performing: str
    _next_node: tuple
    _config: ReadConfig
    _path: list


    def __init__(self):
        super().__init__("controller_node")
        self._knowledge_graph = Graph((0, 0))
        self._is_acting = False
        self._action_performing = ""
        self._path = []
        self._config = ReadConfig()

        self._new_node_sub = self.create_subscription(String, "new_node_map", self.proximity_callback, 10)
        self._free_side_sub = self.create_subscription(String, "free_side", self.proximity_callback, 10)
        self._arrived_sub = self.create_subscription(Bool, "arrived", self.proximity_callback, 10)

        self._action_pub = self.create_publisher(String, "action_topic", 10)

        self.get_logger().info("Hello from controller_module")


    def free_side_callback(self, msg: String):
        self.get_logger().info("free side: " + str(msg))
        dict_side = json.loads(msg.data)
        dict_neighbors = {}
        for side, dict_new_node in dict_side.items():
            new_node = (self._current_node[0] + dict_new_node["x"], self._current_node[1] + dict_new_node["y"])
            dict_neighbors[side] = new_node
            if self._knowledge_graph.is_node_new(new_node):
                self._knowledge_graph.add_node(self._current_node, new_node)
        self.choose_action(dict_neighbors)


    def choose_action(self, current_neighbors):
        if self._is_acting:
            if self._action_performing == "turn" and \
                    "center" in current_neighbors and    \
                    current_neighbors["center"] == self._next_node: # TODO !!!Errore verifica se sto nel ragio prestabilito
                self.go_forward(current_neighbors)
        else:
            if len(self._path) == 0:
                next_node = self._knowledge_graph.get_next_node()
                self._path = self._knowledge_graph.path_to_next_node(next_node)
            self._next_node = self._path.pop(0)
            if "center" in current_neighbors and \
                    current_neighbors["center"] == self._next_node:  # TODO!!!Errore verifica se sto nel ragio prestabilito
                self.go_forward(current_neighbors)
            elif "left" in current_neighbors and \
                    current_neighbors["left"] == self._next_node:  #TODO !!!Errore verifica se sto nel ragio prestabilito
                self.turn_left()
            elif "right" in current_neighbors and \
                    current_neighbors["right"] == self._next_node:  # TODO !!!Errore verifica se sto nel ragio prestabilito
                self.turn_right()
            else:
                random_value = random.random()
                if random_value > 0.5:
                    self.turn_left()
                else:
                    self.turn_right()



        """
        se sto già facendo l'azione controlla se l'azione è conclusa ed eventualmente terminala
        altrimenti calcola il prossimo nodo e come raggiungerlo ed inzia l'azione





        if turn:
            if dict_side["center"] == next_node:
                publish_action(vai dritto)
                turn = false
                self.front = True
                time.sleep(MOTION_WAIT)
                publish_action(stop)
                self.front = False
        elif front:
            pass
        else:
            if len(self.path) == 0
                self.next_node = self.graph.next_node()
                self.path = self.bfs()
            self.next_node = self.path.pop(0)
            if "center" in dict_side and dict_side["center"] == next_node:
                publish_action(vai dritto)
                self.front = True
                time.sleep(MOTION_WAIT)
                publish_action(stop)
                self.front = False
            elif "left" in dict_side and dict_side["left"] == next_node:
                publish_action(vai a sinistra)
                self.turn_left = True
            elif "right" in dict_side and dict_side["right"] == next_node:
                 publish_action(vai a destra)
                self.turn_left = True
            else :
                turn_random

        """

    def go_forward(self, current_neighbors):
        self._action_pub.publish("go_forward")
        self._action_performing = "go_forward"
        self._is_acting = True
        sleep(self._config.read_data("MOTION_WAIT"))
        self._action_pub.publish("stop")
        self._knowledge_graph.set_current_node(self._next_node)  #TODO un pò ideale
        self._is_acting = False

    def turn_left(self):
        self._action_pub.publish("turn_left")
        self._action_performing = "turn_left"
        self._is_acting = True
        self._action_pub.publish("turn_left")

    def turn_right(self):
        self._action_pub.publish("turn_right")
        self._action_performing = "turn_right"
        self._is_acting = True
        self._action_pub.publish("turn_right")





    def arrived_callback(self, msg: Bool):
        self.get_logger().info("arrived: " + str(msg))
        if msg.data:
            action_msg = String()
            action_msg.data = "stop"
            self._action_pub.publish(action_msg)




def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    rclpy.shtdown()