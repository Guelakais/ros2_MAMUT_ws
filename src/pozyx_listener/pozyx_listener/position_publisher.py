#!/usr/bin/env python3

import serial
import time

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point


class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')

        # Open the serial port
        self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)

        # Setup publisher
        self.publisher_ = self.create_publisher(Point, 'position', 10)

        # Read data from the serial port and publish it as a ROS message
        while True:
            line = self.ser.readline().decode('utf-8').strip()
            data = line.split('#')
            if len(data) == 3:
                x, y, z = map(float, data)
                msg = Point()
                msg.x = x
                msg.y = y
                msg.z = z
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: x=%f, y=%f, z=%f' % (msg.x, msg.y, msg.z))
            rate.sleep(0.01)

def main(args=None):
    rclpy.init(args=args)

    position_publisher = PositionPublisher()

    rclpy.spin(position_publisher)

    position_publisher.ser.close()
    position_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
