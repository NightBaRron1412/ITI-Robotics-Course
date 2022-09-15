#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from std_srvs.srv import Trigger
from random import uniform
from math import pi

node_name = "spawn_node"


class SpawnNode(Node):

    def __init__(self):
        super().__init__(node_name)

        self.create_service(Trigger, "spawn_trigger", self.trigger_callback)
        self.spawn_client = self.create_client(Spawn, "spawn")

        self.get_logger().info("Spawn node started!")

    def trigger_callback(self, _, response):
        self.spawn_service_client()

        response.success = True
        return response

    def spawn_service_client(self):
        while (self.spawn_client.wait_for_service(0.25) == False):
            self.get_logger().warn("Waiting for service")

        request = Spawn.Request()
        request.x = round(uniform(1, 10), 8)
        request.y = round(uniform(1, 10), 8)
        request.theta = round(uniform(-pi, pi), 4)
        request.name = "donatello"
        future_obj = self.spawn_client.call_async(request)
        future_obj.add_done_callback(self.future_call_back)

    def future_call_back(self, future_msg):
        response = future_msg.result()
        self.get_logger().info(response.name.capitalize() + " has been located!")


def main(args=None):
    rclpy.init(args=args)
    node = SpawnNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
