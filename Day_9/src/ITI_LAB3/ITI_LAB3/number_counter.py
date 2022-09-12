#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import SetBool

node_name = "number_counter"

class node2(Node):
    def __init__(self):
        super().__init__(node_name)
        self.subscription = self.create_subscription(Int64, 'number', self.sub_callback, 10)
        self.pub = self.create_publisher(Int64, 'number_counter', 10)
        self.create_service(SetBool, "reset_srv", self.srv_callback)
        
        self.counter = 0
        
        self.get_logger().info("Sub_Node Started")

    def sub_callback(self, msg):
        num = Int64()
        num.data = self.counter * msg.data
        self.get_logger().info(f"I got data and counter is {num.data}")
        self.pub.publish(num)
        self.counter += 1
        
    def srv_callback(self, request, response):
        response.success = True
        self.counter = 0
        self.get_logger().info("Done resetting counter to 0")
        return response
        
        
def main(args = None):
    rclpy.init(args = args)
    node = node2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()