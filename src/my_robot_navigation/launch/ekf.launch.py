import os 

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # Locate EKF configuration
    navigation_pkg = get_package_share_directory(
        'my_robot_navigation'
    )

    ekf_config = os.path.join(
        navigation_pkg,
        'config',
        'ekf.yaml'
    )

    # Launch Extended Kalman Filter
    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[ekf_config]
    )

    return LaunchDescription([
        ekf_node
    ])