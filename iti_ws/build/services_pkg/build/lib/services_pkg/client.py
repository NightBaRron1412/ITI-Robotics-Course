#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

node_name = "client"

class Client(Node):
    def __init__(self):
        super().__init__(node_name)
        self.client = self.create_client(AddTwoInts, "service_1")
        
        self.service_client(8, 9);
        self.service_client(20, 4);
        
    def service_client(self, a, b):
        while self.client.wait_for_service(0.25) == False:
            self.get_logger().warn("Waiting for server")
            
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        
        future_obj = self.client.call_async(request)
        future_obj.add_done_callback(self.FutureCallback)
        
    def FutureCallback(self, future_msg):
        response = future_msg.result()
        self.get_logger().info("Result is: %d" % response.sum)
    
def main(args = None):
    rclpy.init(args = args)
    node = Client()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()