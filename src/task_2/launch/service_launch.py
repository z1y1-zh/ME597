from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Start the service server and publisher nodes together.
    return LaunchDescription([
        Node(
            package='task_2',
            executable='service',
            ),
        Node(
            package='task_2',
            executable='talker',
            )
    ])
