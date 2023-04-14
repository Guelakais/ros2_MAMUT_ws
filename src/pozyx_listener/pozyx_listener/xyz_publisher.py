import serial
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class pozyx_listener(Node):
    serialport
    def __init__(self):
        super().__init__('pozyx_listener')
        serialport = serial.Serial(
                port ="/dev/ttyAMA0",baudrate=115200
                )
        self.publisher=self.create_publisher(String,'topic',10)
        timer_period=0.5
        self.timer=self.create_timer(timer_period,self.timer_callback)
        self.i=0

    def timer_callback(self):
        data = serialPort.readline().decode().strip()
        msg = String()
        msg.data = 'Position Data: %d' % serialPort.readline().decode().strip()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    print('Hi from pozyx_listener.')
    publisher = pozyx_listener()
    rclpy.spin(publisher)


if __name__ == '__main__':
    main()
