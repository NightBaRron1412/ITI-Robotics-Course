#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

node_name = "Int_publisher"

class node1(Node):
    def __init__(self):
        super().__init__(node_name)
        self.pub = self.create_publisher(Int64, 'number', 10)
        
        timer_period = 0.5  # seconds
        
        self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info("Pub_Node_Started_ok")
        
    def timer_callback(self):
        msg = Int64()
        msg.data = 5
        self.pub.publish(msg)
        self.get_logger().info(str(msg.data))
        
def main(args = None):
    rclpy.init(args = args)
    node = node1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()