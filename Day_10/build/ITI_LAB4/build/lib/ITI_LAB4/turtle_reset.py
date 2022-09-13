#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
from turtlesim.msg import Pose

node_name = "turtle_reset"


class MainNode(Node):
    def __init__(self):
        super().__init__(node_name)
        self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)
        self.client = self.create_client(Empty, "reset")

        self.get_logger().info("Node initialized, watching pose topic")

    def service_client(self):
        while (self.client.wait_for_service(0.25) == False):
            self.get_logger().warn("Waiting for server")

        request = Empty.Request()
        self.client.call_async(request)

    def pose_callback(self, pose):
        if (pose.x <= 3 or pose.x >= 8 or pose.y <= 3 or pose.y >= 8):
            self.service_client()
            self.get_logger().warn("Turtle is out of bounds, resetting")


def main(args=None):
    rclpy.init(args=args)
    node = MainNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
