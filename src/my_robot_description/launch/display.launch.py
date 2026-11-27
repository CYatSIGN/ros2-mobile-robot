# Setup only for visualisation of the robot's URDf description in 3D 

from launch import LaunchDescription

from launch_ros.actions import Node

from ament_index_python.packages import (
    get_package_share_directory
)

import os


def generate_launch_description():
    # Locate the robot description package
    package_path = get_package_share_directory(
        'my_robot_description'
    )

    # Locate the URDF file
    urdf_path = os.path.join(
        package_path,
        'urdf',
        'my_robot.urdf'
    )

    # Read the URDF file
    with open(urdf_path, 'r') as file:
        robot_description = file.read()

    # Publish robot transformation
    # Reads URDF and publishes TF transformations between the robot's links
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description
        }]
    )

    # Publish joint positions
    # Publishes joint positions for movable joints
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description
        }]
    )

    # Locate saved RViz configurations
    rviz_config = os.path.join(
        package_path,
        'rviz',
        'robot.rviz'
    )

    # Use saved configuration if available
    if os.path.isfile(rviz_config):
        rviz_arguments = ['-d', rviz_config]

    else:
        rviz_arguments = []

    # Launch RViz2 to view robot in 3D
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=rviz_arguments
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        rviz
    ])