#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from math import sin, cos, pi
from geometry_msgs.msg import Quaternion
from tf2_ros import TransformBroadcaster, TransformStamped


def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - \
        cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + \
        sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - \
        sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + \
        sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)


node_name = "lidar_tf2_frame_publisher"


class FramePublisher(Node):

    def __init__(self):
        super().__init__(node_name)

        # Initialize the transform broadcaster
        self.br = TransformBroadcaster(self)
        t = TransformStamped()
        self.get_logger().info(f"{node_name} started")

        degree = pi / 180.0
        loop_rate = self.create_rate(30)

        while rclpy.ok():

            # assigning tf variables
            t.header.stamp = self.get_clock().now().to_msg()
            t.header.frame_id = "servo_link"
            t.child_frame_id = "lidar_link"

            for deg in range(-30, 30 + 1):
                rclpy.spin_once(self)
                t.transform.rotation = euler_to_quaternion(
                    0, deg * degree, 0)  # roll,pitch,yaw

                # Send the transformation
                self.br.sendTransform(t)

                # This will adjust as needed per iteration
                loop_rate.sleep()

            # Reverse the direction
            for deg in range(-30, 30 + 1):
                rclpy.spin_once(self)
                t.transform.rotation = euler_to_quaternion(
                    0, -deg * degree, 0)  # roll,pitch,yaw

                self.br.sendTransform(t)

                loop_rate.sleep()


def main(args=None):
    rclpy.init(args=args)
    node = FramePublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
