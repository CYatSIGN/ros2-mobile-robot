import os 

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    navigation_pkg = get_package_share_directory(
        'my_robot_navigation'
    )

    nav2_pkg = get_package_share_directory(
        'nav2_bringup'
    )

    map_file = os.path.join(
        navigation_pkg,
        'maps',
        'indoor_map.yaml'
    )

    params_file = os.path.join(
        navigation_pkg,
        'config',
        'nav2_params.yaml'
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                nav2_pkg,
                'launch',
                'bringup_launch.py'
            )
        ),
        launch_arguments={
            'map':map_file,
            'use_sim_time': 'true',
            'params_file': params_file,
            'autostart': 'true'
        }.items()
    )


    return LaunchDescription([
        navigation
    ])