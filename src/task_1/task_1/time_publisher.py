import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class TimePublisher(Node):
    """Publish how long this node has been running, in seconds."""

    def __init__(self):
        super().__init__('time_publisher')

        # Create a publisher on my_first_topic using Float64 messages.
        self.publisher_ = self.create_publisher(
            Float64,
            'my_first_topic',
            10
        )

        # Save the ROS clock time at which this node starts.
        self.start_time = self.get_clock().now()

        # Run timer_callback every 0.5 seconds, giving a frequency of 2 Hz.
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        # Calculate elapsed time and convert nanoseconds to seconds.
        elapsed_time = self.get_clock().now() - self.start_time

        message = Float64()
        message.data = elapsed_time.nanoseconds / 1_000_000_000.0

        self.publisher_.publish(message)


def main(args=None):
    rclpy.init(args=args)

    node = TimePublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

