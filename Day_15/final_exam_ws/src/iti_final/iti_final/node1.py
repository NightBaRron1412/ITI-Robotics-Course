#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

node_name = "node1"


class Node1(Node):

    def __init__(self):
        super().__init__(node_name)

        self.timer_period = 1.0
        self.counter = 0

        self.pub = self.create_publisher(String, "number", 10)
        self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()

        if (self.counter % 2 == 0):
            msg.data = "Add, 5"
        else:
            msg.data = "Add, 4"

        self.pub.publish(msg)

        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
