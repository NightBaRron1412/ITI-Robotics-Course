#! /usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt, atan2


class Twist_Pub_Node(Node):
    def __init__(self):
        super().__init__("Twist_Pub_Node")
        self.pub_ob = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.create_timer(1/30, self.pub_call)
        self.create_subscription(Pose, "turtle1/pose", self.sub_call, 10)

        self.get_logger().info("Node_Started")

        # Target
        self.desierd_x = 9  # Target x
        self.desired_y = 7  # Target y
        self.flag_reached = False  # We reached the target

        # Commands
        self.lin_vel = 0
        self.ang_vel = 0

        ################### PIDs Gains   ####################
        self.Kp_lin = 2
        self.Ki_lin = 0.000001
        self.Kd_lin = 0.1

        self.Kp_ang = 3
        self.Ki_ang = 0
        self.Kd_ang = 0.1

        ################### PIDs Errors   ####################
        self.dt = 1/30        # Consective time between to timer callbacks
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

    def sub_call(self, msg):
        self.now_x = msg.x
        self.now_y = msg.y
        self.now_theta = msg.theta
        self.error_lin = sqrt(
            ((self.desierd_x-self.now_x)**2)+((self.desired_y-self.now_y)**2))

        self.theta = atan2((self.desired_y-self.now_y),
                           (self.desierd_x-self.now_x))
        self.error_ang = self.theta-self.now_theta
        if self.error_ang > math.pi:
            self.error_ang -= 2*math.pi
            print('dec')
        elif self.error_ang < -math.pi:
            self.error_ang += 2*math.pi
            print('inc')

            ## Linear Gain ##
        self.p_lin = self.error_lin*self.Kp_lin
        self.cumm_error_lin += self.error_lin*self.dt
        self.i_lin = self.cumm_error_lin*self.Ki_lin
        self.error_rate_lin = (self.error_lin-self.last_error_lin)/self.dt
        self.d_lin = self.error_rate_lin*self.Kd_lin
        self.last_error_lin = self.error_lin

        self.lin_vel = self.p_lin+self.i_lin+self.d_lin  # OUTPUT Linear Velocity

        ## Angular Gain ##

        self.p_ang = self.error_ang*self.Kp_ang
        self.cumm_error_ang += self.error_ang*self.dt
        self.i_ang = self.cumm_error_ang*self.Ki_ang
        self.error_rate_ang = (self.error_ang-self.last_error_ang)/self.dt
        self.d_ang = self.error_rate_ang*self.Kd_ang
        self.last_error_ang = self.error_ang

        self.ang_vel = self.p_ang+self.i_ang+self.d_ang  # OUTPUT Angular Velocity

        if (abs(self.error_lin)) < 0.005:
            self.lin_vel = 0
            self.ang_vel = 0
            if self.flag_reached == False:
                self.get_logger().info("Done Target Reached ^__^")
                self.flag_reached = True
        else:
            self.get_logger().warn(' lin_gain: '+str(self.lin_vel)+' ang_gain: '+str(self.ang_vel) +
                                   ' error_ang: '+str(self.error_ang)+' error_lin: '+str(self.error_lin))

    def pub_call(self):
        msg = Twist()
        msg.linear.x = float(self.lin_vel)
        msg.angular.z = float(self.ang_vel)
        self.pub_ob.publish(msg)
        #self.get_logger().info("linear dist="+str(self.error_lin))


def main(args=None):
    rclpy.init(args=args)
    sub = Twist_Pub_Node()
    rclpy.spin(sub)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
