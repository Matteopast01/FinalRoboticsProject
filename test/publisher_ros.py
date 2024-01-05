#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
        def __init__(self):
                super().__init__("first_node")
                self.get_logger().info("Hello from ROS")
                self.create_timer(1.0, self.timer_callback)
                self.publisher = self.create_publisher(String, "my_first_topic", 10)
                self.timer = self.create_timer(0.5, self.my_pub_method)
        def timer_callback(self):
                self.get_logger().info("daje")
        def my_pub_method(self):
                msg = String()
                msg.data = "prova"
                self.publisher.publish(msg)
                self.get_logger().info('Publish: "%s"' % msg.data)
def main(args=None):
        rclpy.init(args=args) #init ros comunication
        node = MyNode()
        rclpy.spin(node) # usuful for not stop immediatly the execution until do not key ctr c
        rclpy.shutdown()