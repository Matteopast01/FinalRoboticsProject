from time import sleep
from typing import Any

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .body import SimulatedPioneerBody

MOTION_WAIT = 0.5


class Subscriber(Node):
    _robot: SimulatedPioneerBody
    _controllerSubscriber: Any

    def __init__(self, robot):
        super().__init__("action_node")
        self._robot = robot
        self._actionSubscriber = self.create_subscription(String, "action_topic", self.sub_callback, 10)
        self.get_logger().info("Hello from action_module")

    def set_speed(self, right_value, left_value):
        self._robot.do_action("rightMotor", right_value)
        self._robot.do_action("leftMotor", left_value)

    def sub_callback(self, msg: String):
        self.get_logger().info(str(msg))
        action = str(msg)
        if action == "go_forward":
            self.set_speed(0.8, 0.8)
            sleep(MOTION_WAIT)
            self.set_speed(0, 0)

        elif action == "go_back":
            self.set_speed(-0.5, -0.5)
            sleep(MOTION_WAIT)
            self.set_speed(0, 0)

        elif action == "turn_left":
            self.set_speed(0.15, -0.15)
            sleep(MOTION_WAIT)
            self.set_speed(0,0)

        elif action == "turn_right":
            self.set_speed(-0.15, +0.15)
            sleep(MOTION_WAIT)
            self.set_speed(0, 0)


def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shtdown()
