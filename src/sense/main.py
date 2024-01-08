# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Byte
import base64
from .body import SimulatedPioneerBody
from typing import Any
import json


class MyNode(Node):
    _robot: SimulatedPioneerBody
    _proximity_sensors_publisher: Any
    _orientation_sensor_publisher: Any
    _img_sensor_publisher: Any

    def __init__(self, robot):
        super().__init__("sense_node")
        self._robot = robot
        self.get_logger().info("Hello from sense_module")
        self._proximity_sensors_publisher = self.create_publisher(String, "proximity_sensors", 10)
        self._orientation_sensor_publisher = self.create_publisher(Float32, "orientation_sensor", 10)
        self._img_sensor_publisher = self.create_publisher(String, "camera_sensor", 10)
        self.timer = self.create_timer(0.1, self.pub_callback)

    def pub_callback(self):
        self.my_pub_proximity_sensors()
        self.my_pub_orientation_sensor()
        self.my_pub_camera_sensor()

    def my_pub_camera_sensor(self):
        msg = String()
        msg.data = base64.b64encode(self._robot.read_camera()).decode('utf-8')
        self._img_sensor_publisher.publish(msg)
        self.get_logger().info('Publish Camera sensor')

    def my_pub_proximity_sensors(self):
        msg = String()
        msg.data = json.dumps(self._robot.read_proximity_sensor())
        self._proximity_sensors_publisher.publish(msg)
        self.get_logger().info('Publish Proximity sensor: "%s"' % msg.data)

    def my_pub_orientation_sensor(self):
        msg = Float32()
        msg.data = self._robot.read_orientation()
        self._orientation_sensor_publisher.publish(msg)
        self.get_logger().info('Publish Orientation sensor: "%s"' % msg.data)


def main(args=None):
    robot = SimulatedPioneerBody("sense_module")
    robot.start()
    rclpy.init(args=args)  # init ros comunication
    node = MyNode(robot)
    rclpy.spin(node)  # usuful for not stop immediatly the execution until do not key ctr c
    rclpy.shutdown()
    robot.stop()
