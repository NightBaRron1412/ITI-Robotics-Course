#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):

	def __init__(self):
		super().__init__("node_name")
		self.create_timer(1, self.timer_call) #callback function
		self.pub1 = self.create_publisher(String, "topic_1", 10)
		self.pub2 = self.create_publisher(String, "topic_2", 10)
		print("I'm in init") #debug
		self.counter = 0

	def timer_call(self): #callback func
		print("Timer Called")

		msg = String()
		msg.data = f"topic 1 message is {self.counter}"
		self.counter += 1
		self.pub1.publish(msg)




def main(args = None):
	rclpy.init(args = args)
	node = MyNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == "__main__":
	main()
