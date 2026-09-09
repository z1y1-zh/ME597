from task_2_interfaces.srv import JointState

import rclpy
from rclpy.node import Node


class JointService(Node):

    def __init__(self):
        super().__init__('joint_service_server')

        self.service = self.create_service(
            JointState,
            'joint_service',
            self.service_callback
        )

        self.get_logger().info('Joint service is ready.')

    def service_callback(self, request, response):
        total = request.x + request.y + request.z

        response.valid = total >= 0.0

        self.get_logger().info(
            f'Request: x={request.x:.1f}, '
            f'y={request.y:.1f}, z={request.z:.1f}; '
            f'sum={total:.1f}, valid={response.valid}'
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    joint_service = JointService()

    rclpy.spin(joint_service)

    joint_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
