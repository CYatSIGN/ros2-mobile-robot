import os 

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # Locate navigation package
    navigation_pkg = get_package_share_directory(
        'my_robot_navigation'
    )

    # Locate SLAM Toolbox package
    slam_pkg = get_package_share_directory(
        'slam_toolbox'
    )

    # Locate SLAM configuration file
    slam_config = os.path.join(
        navigation_pkg,
        'config',
        'slam.yaml'
    )

    # Launch SLAM Toolbox
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                slam_pkg,
                'launch',
                'online_async_launch.py'
            )
        ),
        launch_arguments={
            'slam_params_file': slam_config,
            'use_sim_time': 'true'
        }.items()
    )

    return LaunchDescription([
        slam
    ])