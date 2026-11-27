# Modelling, Simulation, and Control of Differential-Drive Mobile Robot in ROS2 and Gazebo
Creating a simplistic URDF differential-drive mobile robot and simulating in Gazebo. Utitinsing navigation package to map out simulated world and enable autonomous driving in Rviz2.

## Project Overview
This project explores Unified Robot Description Format (URDF), Simulataneous Localisation and Mapping (SLAM), control, and sensor fusion, using Gazebo simulation. 

The objective is to create a simple mobile robot to interact in a pre-designed world and map out the obstacles and surrounding. Ultimately, enabling autonomous navigation in the pre-designed map using LiDar sensor and navigation algorithms.

## Modelling
The mobile robot is written in URDF file, consisting of a rectangular base link with two back wheels and one caster wheel for balance. The mobile robot is equipped with a LiDAR sensor and IMU sensor for positioning feedback. 

