# Modelling, Simulation, and Control of a Differential-Drive Mobile Robot in ROS2 and Gazebo
A simulation-based robotics project focused on modelling, controlling, and enabling autonomous navigation of a differential-drive mobile robot using **ROS2 Jazzy**, **Gazebo**, and **Nav2**.

The project involves developing a simplified robot model using URDF, simulating its behaviour in a custom Gazebo environment and utilising SLAM to achieve autonomous movement. 

## Project Overview
The main objective is to develop a differential-drive mobile robot capable of navigating a predefined simulated environment. Using sensor data from onboard LiDAR and IMU, the robot can perceive its surroundings, generate a map for the environment, and navigate autonomously while avoiding obstacles. 

The project integrates several key robotics tools and frameworks:
- ROS2 Jazzy 
- URDF
- Gazebo
- LiDAR and IMU
- SLAM
- Nav2
- RViz2

## Modelling
### Mobile Robot Structure
The mobile robot is written in URDF file, consisting of a rectangular base link with two back wheels and one caster wheel for balance. The mobile robot is equipped with a LiDAR sensor and IMU sensor for positioning feedback. 

### Gazebo World
The Gazebo world consists of 4 walls that acts as a boundary for the robot to move within and a wall around the centre as an obstacle.