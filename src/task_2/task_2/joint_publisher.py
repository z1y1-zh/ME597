import rclpy
from rclpy.node import Node

from task_2_interfaces.msg import JointData


class JointPublisher(Node):

    def __init__(self):
        super().__init__('joint_publisher')

	# Publish custom JointData messages on joint_topic.
	
        self.publisher_ = self.create_publisher(
            JointData,
            'joint_topic',
            10
        )

        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0.0

    def timer_callback(self):
        msg = JointData()
	
	#Input position and velocity data to the message.
        msg.center.x = self.count
        msg.center.y = self.count + 1.0
        msg.center.z = self.count + 2.0
        msg.vel = 0.5

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing: center=({msg.center.x:.1f}, '
            f'{msg.center.y:.1f}, {msg.center.z:.1f}), '
            f'vel={msg.vel:.1f}'
        )

        self.count += 1.0


def main(args=None):
    rclpy.init(args=args)

    node = JointPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
