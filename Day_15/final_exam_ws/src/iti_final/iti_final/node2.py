#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int64

node_name = "node2"


class Node2(Node):

    def __init__(self):
        super().__init__(node_name)

        self.accumulated_number = 0

        self.create_subscription(String, "number", self.sub_callback, 10)
        self.pub = self.create_publisher(Int64, "accumulated_number", 10)

    def sub_callback(self, msg):
        self.accumulated_number += int(msg.data[-1])
        if (self.accumulated_number % 2 == 0):
            msg = Int64()
            msg.data = self.accumulated_number
            self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
