import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__("my_subscriber")
        self.subscriber = self.create_subscription(String, "my_first_topic", self.sub_callback, 10)

    def sub_callback(self, msg: String):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shtdown()
