#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

node_name = "turtle_prevent"


class MainNode(Node):
    def __init__(self):
        super().__init__(node_name)
        self.create_subscription(Pose, "/turtle1/pose", self.SubCallback, 10)
        self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

    def SubCallback(self, Pose):
        if (Pose.x >= 6 or Pose.y >= 6):
            cmd = Twist()
            
            cmd.linear.x = 0.0
            cmd.linear.y = 0.0
            cmd.linear.z = 0.0

            self.pub.publish(cmd)


def main(args = None):
    rclpy.init(args = args)
    node = MainNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
