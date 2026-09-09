import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class TimeSubscriber(Node):

    def __init__(self):
        super().__init__('time_subscriber')
	
	#Subscribe to elapsed time on my_first_topic
        self.subscription = self.create_subscription(
            Float64,
            'my_first_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, message):
        original_value = message.data
        doubled_value = original_value * 2.0
	
	#Print the original and doubled value
        self.get_logger().info(
            f'Original: {original_value:.3f} s, '
            f'Doubled: {doubled_value:.3f} s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TimeSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

