#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MyNode(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.laser_sub_ = self.create_subscription(LaserScan, "/scan",self.subscriber_move_callback, 10)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/cmd_vel", 10)
        # self.timer_ = self.create_timer(0.5, self.move_callback)

        self.get_logger().info("Controller Node for ROOMBA Started")
        self.speed = 0.2
        self.turn_speed = 0.5


    def subscriber_move_callback(self, msg):
        # Process scan data and decide on actions
        is_obstacle_in_front = min(min(msg.ranges[0:30]), min(msg.ranges[-30:])) < 0.6

        twist = Twist()

        if is_obstacle_in_front:
            twist.linear.x = 0.0
            twist.angular.z = self.turn_speed
        else:
            twist.linear.x = self.speed
            twist.angular.z = 0.0

        self.cmd_vel_pub_.publish(twist)
        


def main(args=None):
    rclpy.init(args=args)


    node = MyNode()
    

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
