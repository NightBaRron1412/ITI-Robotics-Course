#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, Empty
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from math import sqrt, atan2, pi
from time import time

node_name = "control_node"


class ControlNode(Node):

    def __init__(self):
        super().__init__(node_name)
        self.pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

        self.create_timer(1/30, self.pub_call)

        self.create_subscription(Pose, "turtle1/pose",
                                 self.turtle1_sub_call, 10)
        self.create_subscription(
            Pose, "donatello/pose", self.donatello_sub_call, 10)

        self.kill_client = self.create_client(Kill, "kill")
        self.spawn_client = self.create_client(Trigger, "spawn_trigger")
        self.clear_client = self.create_client(Empty, "clear")

        self.get_logger().info("Node_Started, Waiting for Target information...")

        # Target
        self.target_x = 0  # Target x
        self.target_y = 0  # Target y
        self.tolerance = 0.01  # Tolerance

        # Commands
        self.lin_vel = 0
        self.ang_vel = 0

        # Timer
        self.start_time = 0  # timer to prevent multiple service executions

        ################### PIDs Gains   ####################
        self.Kp_lin = 2
        self.Ki_lin = 0.000001
        self.Kd_lin = 0.1

        self.Kp_ang = 3
        self.Ki_ang = 0
        self.Kd_ang = 0.1

        ################### PIDs Errors   ####################
        self.dt = 1/30        # Consecutive time between to timer callbacks
        self.error_lin = 0    # Linear distance to target
        self.cumm_error_lin = 0
        self.error_rate_lin = 0
        self.last_error_lin = 0

        self.theta = 0        # theta current pose to target pos -> desired_theta
        self.error_ang = 0    # diff desired_theta - current heading
        self.cumm_error_ang = 0
        self.error_rate_ang = 0
        self.last_error_ang = 0

        ################### PIDs Components   ####################
        self.p_lin = 0        # Proportional Term = Kp * error_lin
        self.i_lin = 0        # Integration Term = Ki * cumm_error_lin
        self.d_lin = 0        # Derivative Term = Kd * error_rate_lin

        self.p_ang = 0
        self.i_ang = 0
        self.d_ang = 0

        self.spawn_client_service()

    def clear_client_service(self):
        while (self.clear_client.wait_for_service(0.25) == False):
            self.get_logger().warn("Requesting Approval to assassinate")

        request = Empty.Request()

        self.clear_client.call_async(request)

    def kill_client_service(self):
        while (self.kill_client.wait_for_service(0.25) == False):
            self.get_logger().warn("Requesting Approval to assassinate")

        request = Kill.Request()
        request.name = "donatello"

        kill_future_obj = self.kill_client.call_async(request)
        self.start_time = time()
        kill_future_obj.add_done_callback(self.kill_future_call_back)

    def kill_future_call_back(self, _):
        self.donatello_dead = True
        self.clear_client_service()
        self.spawn_client_service()

    def spawn_client_service(self):
        while (self.spawn_client.wait_for_service(0.25) == False):
            self.get_logger().warn("Waiting for information about new target location...")

        request = Trigger.Request()

        spawn_future_obj = self.spawn_client.call_async(request)
        spawn_future_obj.add_done_callback(self.spawn_future_call_back)

    def spawn_future_call_back(self, _):
        self.get_logger().info("Moving to new target")
        self.donatello_dead = False

    def donatello_sub_call(self, pose):
        self.target_x = pose.x  # Target x
        self.target_y = pose.y  # Target y

    def turtle1_sub_call(self, pose):
        self.now_x = pose.x
        self.now_y = pose.y
        self.now_theta = pose.theta

        ################### Linear and Angular Error Calc ####################
        self.error_lin = sqrt(
            ((self.target_x - self.now_x) ** 2) + ((self.target_y - self.now_y) ** 2))

        self.theta = atan2((self.target_y-self.now_y),
                           (self.target_x-self.now_x))
        self.error_ang = self.theta-self.now_theta

        if self.error_ang > pi:
            self.error_ang -= 2 * pi
            print('dec')
        elif self.error_ang < -pi:
            self.error_ang += 2 * pi
            print('inc')

        ################### Linear Gain ####################
        self.p_lin = self.error_lin*self.Kp_lin  # Proportional Term

        # Summing Error for Intergranal Term
        self.cumm_error_lin += self.error_lin*self.dt
        self.i_lin = self.cumm_error_lin*self.Ki_lin  # Integral term

        self.error_rate_lin = (self.error_lin-self.last_error_lin)/self.dt
        self.d_lin = self.error_rate_lin*self.Kd_lin  # Derivative Term

        self.last_error_lin = self.error_lin  # Last error update for I and D terms

        self.lin_vel = self.p_lin+self.i_lin+self.d_lin  # OUTPUT Linear Velocity

        ################### Angular Gain ####################
        self.p_ang = self.error_ang*self.Kp_ang  # Proportional Term

        # Summing Error for Intergranal Term
        self.cumm_error_ang += self.error_ang*self.dt
        self.i_ang = self.cumm_error_ang*self.Ki_ang  # Integral Term

        self.error_rate_ang = (self.error_ang-self.last_error_ang)/self.dt
        self.d_ang = self.error_rate_ang*self.Kd_ang  # Derivative Term

        self.last_error_ang = self.error_ang  # Last error update for I and D terms

        self.ang_vel = self.p_ang+self.i_ang+self.d_ang  # OUTPUT Angular Velocity

        if ((abs(self.error_lin)) < self.tolerance):
            self.lin_vel = 0
            self.lin_ang = 0
            if (self.donatello_dead == False):
                self.get_logger().info("Target Reached, Assassinating Donatello")
                if (time() - self.start_time > 0.1):
                    self.kill_client_service()

        else:
            self.get_logger().warn(' lin_gain: '+str(self.lin_vel)+' ang_gain: '+str(self.ang_vel) +
                                   ' error_ang: '+str(self.error_ang)+' error_lin: '+str(self.error_lin))

    def pub_call(self):
        msg = Twist()
        msg.linear.x = float(self.lin_vel)
        msg.angular.z = float(self.ang_vel)
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
