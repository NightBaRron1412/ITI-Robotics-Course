#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool, Int8


class Node2(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.pub1 = self.create_publisher(Int8, "number", 10)
        self.pub2 = self.create_publisher(Bool, "rest_flag", 10)
        self.create_subscription(String, "str_topic", self.SubCallback, 10)

    def SubCallback(self, msg):
        '''
        This function is called when a message is received
        on the topic "str_topic"
        '''
        num = Int8()
        num.data = int(msg.data[-1])
        self.pub1.publish(num)

        if num.data >= 5:
            flag_val = Bool()
            flag_val.data = True
            self.pub2.publish(flag_val)


def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
