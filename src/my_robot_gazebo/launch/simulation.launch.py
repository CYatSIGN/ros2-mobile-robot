import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Locate ROS2 packages
    gazebo_pkg = get_package_share_directory('ros_gz_sim')
    description_pkg = get_package_share_directory('my_robot_description')

    # Locate robot URDF
    urdf_path = os.path.join(
        description_pkg,
        'urdf',
        'my_robot.urdf'
    )

    # Read robot description
    with open(urdf_path,'r') as file:
        robot_description = file.read()

    # Publish robot TF transformations
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )

    # Locate Gazebo world
    world_path = os.path.join(
        get_package_share_directory('my_robot_gazebo'),
        'worlds',
        'lidar_world.sdf'
    )


    # Launch Gazebo Harmonic
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                gazebo_pkg,
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': f'-r {world_path}'
        }.items()
    )

    # Spawn robot into Gazebo
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'lidar_world',
            '-file', urdf_path,
            '-name', 'my_robot',
            '-x', '0',
            '-y', '0',
            '-z', '0.3'
        ],
        output='screen'
    )

    # Allow Gazebo to start (5seconds delay) before spawning
    # Increase time delay if they are multiple entities to spawn in the world
    delayed_spawn = TimerAction(
        period=10.0,
        actions=[spawn_robot]
    )

    # Bridge ROS2 velocity commands and Gazebo odometry
    # [ means Gazebo to ROS2; ] means ROS2 to Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # ROS 2 → Gazebo
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',

            # Gazebo → ROS 2
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/imu/data@sensor_msgs/msg/Imu[gz.msgs.IMU',
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        bridge,
        robot_state_publisher,
        delayed_spawn
    ])
