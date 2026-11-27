#!/usr/bin/env python3

import sys
import select
import termios
import tty

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.5

class WASDTeleop(Node):

    def __init__(self):
        super().__init__('wasd_teleop')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.linear = 0.0
        self.angular = 0.0

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.linear
        msg.angular.z = self.angular
        self.publisher.publish(msg)

    def stop(self):
        self.linear = 0.0
        self.angular = 0.0
        self.publish_velocity()

def main():
    rclpy.init()
    node = WASDTeleop()

    settings = termios.tcgetattr(sys.stdin)

    print("\n===== WASD Robot Control =====")
    print("W : Forward")
    print("S : Backward")
    print("A : Rotate left")
    print("D : Rotate right")
    print("SPACE : Stop")
    print("Q : Quit")
    print("==============================\n")

    try:
        tty.setcbreak(sys.stdin.fileno())

        while rclpy.ok():

            if select.select([sys.stdin], [], [], 0.1)[0]:
                key = sys.stdin.read(1).lower()

                if key == 'w':
                    node.linear = LINEAR_SPEED
                    node.angular = 0.0

                elif key == 's':
                    node.linear = -LINEAR_SPEED
                    node.angular = 0.0

                elif key == 'a':
                    node.linear = 0.0
                    node.angular = ANGULAR_SPEED

                elif key == 'd':
                    node.linear = 0.0
                    node.angular = -ANGULAR_SPEED

                elif key == ' ':
                    node.stop()

                elif key == 'q':
                    break 
                
            node.publish_velocity()

    except KeyboardInterrupt:
        pass

    finally:
        node.stop()
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            settings
        )
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
                