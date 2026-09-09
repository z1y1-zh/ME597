from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Start the publisher and subscriber nodes together
    return LaunchDescription([
        Node(
            package='task_1',
            executable='talker',
            output='screen',
        ),
        Node(
            package='task_1',
            executable='listener',
            output='screen',
        ),
    ])
