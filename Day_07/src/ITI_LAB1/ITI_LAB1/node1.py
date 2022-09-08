#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool


class Node1(Node):
    def __init__(self):
        super().__init__("str_publisher")

        self.pub = self.create_publisher(String, "str_topic", 10)
        self.create_subscription(Bool, "rest_flag", self.SubCallback, 10)

        timer_period = 0.5  # seconds

        self.counter = 0

        self.create_timer(timer_period, self.TimerCallback)

    def TimerCallback(self):
        '''
        This function is called every timer_period seconds
        to publish a message
        '''
        msg = String()
        msg.data = f"Amir is publishing, {self.counter}"
        self.pub.publish(msg)
        self.counter += 1

    def SubCallback(self, flag_val):
        '''
        This function is called when a message is received
        on the topic "rest_flag"
        '''
        if flag_val.data == True:
            self.counter = 0


def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
