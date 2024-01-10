import json
from time import sleep
from typing import Any
from Computation import Computation

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from .body import SimulatedPioneerBody

MOTION_WAIT = 0.5


class Perception(Node):
    _proximity_sub: Any
    _orientation_sub: Any
    _img_sub: Any
    _knowledge_pub: Any
    _controller_pub: Any
    _computation: Computation

    def __init__(self):
        super().__init__("perception_node")
        self._computation = None
        self._proximity_sub = self.create_subscription(String, "proximity_sensors", self._proximity_callback, 10)
        self._orientation_sub = self.create_subscription(Float32, "orientation_sensor", self.orientation_callback, 10)
        self._img_sub = self.create_subscription(String, "camera_sensor", self.camera_callback, 10)
        self._knowledge_pub = self.create_publisher(String, "new_node_map", 10)
        self._controller_pub = self.create_publisher(String, "free_side", 10)
        self.get_logger().info("Hello from perception_module")

    def camera_callback(self, msg: String):
        self.get_logger().info(str(msg))
        action = str(msg)
        try:
            getattr(self, action)()
        except:
            raise Exception(f"Unknown command {action}")

    def orientation_callback(self, msg: Float32):
        self.get_logger().info("orientation: "+str(msg))
        if self._computation is None:
            self._computation = Computation(msg.data)
        else:
            self._computation.set_orientation(msg.data)

    def proximity_callback(self, msg: String):
        self.get_logger().info("proximity: "+str(msg))
        self._computation.compute_position_robot()
        data_dict = json.loads(msg.data)
        controller_dict = {}
        for side, value in data_dict.items():
            is_side_free = self._computation.is_side_free(value)
            controller_dict[side] = is_side_free
            if is_side_free:
                data = self._computation.compute_position_node(side)
                data_to_send = {"x": data[0], "y": data[1]}
                self._knowledge_pub.publish(json.dumps(data_to_send))
        self._controller_pub.publish(json.dumps(controller_dict))







def main(args=None):
    rclpy.init(args=args)
    node = Perception()
    rclpy.spin(node)
    rclpy.shtdown()
