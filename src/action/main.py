#!/usr/bin/env python3
from time import sleep
from typing import Any
from ..ReadConfig import ReadConfig

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .body import SimulatedPioneerBody




class Subscriber(Node):
    _robot: SimulatedPioneerBody
    _controllerSubscriber: Any
    _config: ReadConfig
    _speed: float

    def __init__(self, robot):
        super().__init__("action_node")
        self._robot = robot
        self._actionSubscriber = self.create_subscription(String, "action_topic", self.sub_callback, 10)
        self.get_logger().info("Hello from action_module")
        self._config = ReadConfig()
        self._speed = self._config.read_data("SPEED")

    def set_speed(self, right_value, left_value):
        self._robot.do_action("rightMotor", right_value)
        self._robot.do_action("leftMotor", left_value)

    def go_forward(self):
        self.set_speed(self._speed, self._speed)

    def go_back(self):
        self.set_speed(-self._speed, -self._speed)

    def turn_left(self):
        self.set_speed(0.1, -0.1)

    def turn_right(self):
        self.set_speed(-0.1, +0.1)

    def stop(self):
        self.set_speed(0, 0)

    def sub_callback(self, msg: String):
        self.get_logger().info(str(msg.data))
        action = str(msg.data)
        try:
            getattr(self, action)()
        except:
            raise Exception(f"Unknown command {action}")


def main(args=None):
    robot = SimulatedPioneerBody("action_module")
    #robot.start()
    rclpy.init(args=args)
    node = Subscriber(robot)
    rclpy.spin(node)
    rclpy.shtdown()
    robot.stop()
