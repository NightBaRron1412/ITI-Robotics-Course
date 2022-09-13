#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import SetBool

node_name = "reset_client"


class node3(Node):
    def __init__(self):
        super().__init__(node_name)
        self.client = self.create_client(SetBool, "reset_srv")

        self.service_client(True)

    def service_client(self, reset):
        while self.client.wait_for_service(0.25) == False:
            self.get_logger().warn("Waiting for server")

        self.get_logger().warn("Server OK, Making request")

        request = SetBool.Request()
        request.data = reset

        future_obj = self.client.call_async(request)
        future_obj.add_done_callback(self.future_callback)

        self.get_logger().warn("OK_CALL")

    def future_callback(self, future_msg):
        response = future_msg.result()
        self.get_logger().info(
            f"Counter_Done Reset  Respond: {response.success}")


def main(args=None):
    rclpy.init(args=args)
    node = node3()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
