import sys

import rclpy
from rclpy.node import Node

from task_2_interfaces.srv import JointState


class JointClient(Node):

    def __init__(self):
        super().__init__('joint_client')

        self.client = self.create_client(
            JointState,
            'joint_service'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Joint service is not available, waiting again...'
            )

        self.request = JointState.Request()

    def send_request(self, x, y, z):
        self.request.x = float(x)
        self.request.y = float(y)
        self.request.z = float(z)

        return self.client.call_async(self.request)


def main(args=None):
    if len(sys.argv) != 4:
        print('Warning: ROS 2 requires x, y, and z.')
        return

    rclpy.init(args=args)

    joint_client = JointClient()

    future = joint_client.send_request(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    rclpy.spin_until_future_complete(joint_client, future)

    response = future.result()

    joint_client.get_logger().info(
        f'Request: x={float(sys.argv[1]):.1f}, '
        f'y={float(sys.argv[2]):.1f}, '
        f'z={float(sys.argv[3]):.1f}; '
        f'valid={response.valid}'
    )

    joint_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
