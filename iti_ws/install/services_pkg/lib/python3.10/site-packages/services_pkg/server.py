#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

node_name = "server"

class Server(Node):
    def __init__(self):
        super().__init__(node_name)
        self.create_service(AddTwoInts, "service_1", self.SrvCallback)
    
    def SrvCallback(self, request, response):
        
        response.sum = request.a + request.b
        self.get_logger().info("Request: a = %d, b = %d" % (request.a, request.b))
        self.get_logger().info("Response: %d" % response.sum)
        return response
    
def main(args = None):
    rclpy.init(args = args)
    node = Server()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()