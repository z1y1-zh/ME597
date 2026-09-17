import math
import rclpy
from sensor_msgs.msg import LaserScan
from rclpy.node import Node
from geometry_msgs.msg import Twist


class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')

        self.target_distance = 0.35

        self.kp = 0.8
        self.ki = 0.05
        self.kd = 0.005

        self.integral = 0.0
        self.previous_error = None
        self.previous_time = self.get_clock().now().nanoseconds * 1e-9

        self.velocity_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10,
        )
        self.scan_subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.timer_callback,
            10,
        )
        self.get_logger().info('PID Controller node has started.')

    def timer_callback(self, message):
        forward_distance = message.ranges[0]

        if not math.isfinite(forward_distance):
            stop_message = Twist()
            self.velocity_publisher.publish(stop_message)
            self.get_logger().warning('Forward distance is not valid.')
            return

        current_time = self.get_clock().now().nanoseconds * 1e-9
        dt = current_time - self.previous_time

        error = forward_distance - self.target_distance

        if dt > 0.0:
            self.integral = self.integral + error * dt
            self.integral = max(-0.5, min(0.5, self.integral))

        if self.previous_error is None or dt <= 0.0:
            derivative = 0.0
        else:
            derivative = (error - self.previous_error) / dt

        control_output = (
            self.kp * error
            + self.ki * self.integral
            + self.kd * derivative
        )

        limited_output = max(-0.15, min(0.15, control_output))

        velocity_message = Twist()
        velocity_message.linear.x = limited_output
        velocity_message.angular.z = 0.0

        self.velocity_publisher.publish(velocity_message)

        self.previous_error = error
        self.previous_time = current_time

        self.get_logger().info(
            f'Distance: {forward_distance:.2f} m, '
            f'Error: {error:.2f} m, '
            f'PID output: {control_output:.3f}'
            f'Command: {limited_output:.3f} m/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = PIDController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
