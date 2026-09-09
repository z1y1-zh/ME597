import rclpy
from rclpy.node import Node

from task_2_interfaces.msg import JointData


class JointSubscriber(Node):

    def __init__(self):
        super().__init__('joint_subscriber')
	
	# Subscribe to custom JointData messages from joint_topic.
        self.subscription = self.create_subscription(
            JointData,
            'joint_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
	#Log all data received in the JointData message.
        self.get_logger().info(
            f'Received: center=({msg.center.x:.1f}, '
            f'{msg.center.y:.1f}, {msg.center.z:.1f}), '
            f'vel={msg.vel:.1f}'
        )


def main(args=None):
    rclpy.init(args=args)

    joint_subscriber = JointSubscriber()

    rclpy.spin(joint_subscriber)

    joint_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
