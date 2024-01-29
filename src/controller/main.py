import json
from time import sleep
from typing import Any
import random
from isrlab_project.ReadConfig import ReadConfig
import base64
from isrlab_project.controller.behaviour_tree.BehaviourTree import BehaviourTree
from isrlab_project.controller.Knowledge import Knowledge
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
    _action_pub: Any
    _behavior_tree: BehaviourTree
    _config: ReadConfig
    _orientation_sub: Any

    def __init__(self):
        super().__init__("controller_node")
        self._behavior_tree = BehaviourTree(self)
        self._config = ReadConfig()

        self._free_side_sub = self.create_subscription(String, "free_side", self.free_side_callback, 10)
        self._arrived_sub = self.create_subscription(String, "arrived", self.arrived_callback, 10)
        self._orientation_sub = self.create_subscription(Float32, "orientation", self.orientation_callback, 10)

        self._action_pub = self.create_publisher(String, "action_topic", 10)

        self.get_logger().info("Hello from controller_module")

    def free_side_callback(self, msg: String):
        self.get_logger().info("free side: " + str(msg))
        dict_side = json.loads(msg.data)
        for side, dict_new_node in dict_side.items():
            new_node = (dict_new_node["dx"], dict_new_node["dy"])
            Knowledge().add_delta_pos_neighbors(side, new_node)

        self._behavior_tree.tick()

    def arrived_callback(self, msg: String):
        self.get_logger().info("arrived: " + str(msg))
        Knowledge().set_arrived_data_json(msg.data)

    def orientation_callback(self, msg: Float32):
        self.get_logger().info("orientation: " + str(msg))
        Knowledge().set_orientation(msg.data)

    def perform_action(self, action):
        action_msg = String()
        action_msg.data = action
        self._action_pub.publish(action_msg)

    def print_log(self, text):
        self.get_logger().info("python print : " + str(text))


def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    rclpy.shtdown()
