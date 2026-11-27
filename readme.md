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
The mobile robot is modelled using the Unified Robot Description Format (URDF). Its structure consists of a rectangular chassis, two independently driven wheels positioned on either side of the base, and a passive caster wheel to provide stability. 

The differential-drive configuration allows the robot to mvoe forward, backward, as well as rotat by varying the relative velocities of its two drive wheels.

The robot is equipped with the following sensors:
- LiDARs sensor: Provides laser scan measurements of the surrounding environment for obstacle detection, mapping and navigation.
- IMU sensor: Provides inertial measurements, including angular velocity and linear acceleration, to support motion estimation and localisation. 

The robot model also defines the necessary links, joints, coordinate frames, and sensor configurations to integrate with ROS2 and Gazebo.

### Gazebo World
A custom Gazebo world is created to provide a controlled environment for testing the robot's movement and navigation capabilities. 

The environment consists of four boundary walls enclosing the simulation area, with an additional wall positioned near the centre to act as an obstacle. This layout provides a simple but effective environment for evaluating LiDAR-based obstacle detection, map generation, path planning, and autonomous navigation. 

## Simulation and Navigation
The robot is spawned into the Gazebo environment, where its movement and sensor data are integrated with ROS2. 

The Navigation 2 (Nav2) stack is used to enable autonomous navigation. The robot uses LiDAR data and a pre-generated occupancy grid map to localise itself, plan paths, and navigate towards specified goals. 

RViz2 provides a visual interface for monitoring the robot's position, map, sensor readings, planned paths, and navigation goals. 

The overall navigaton workflow involves:
1. Lauching the robot and Gazebo simulation.
2. Generating a map of the environment using SLAM.
3. Saving the generated occupancy grid map.
4. Localising the robot within the saved map using Adaptive Monte Carlo Localisation (AMCL).
5. Planning and executing navigation goals using Nav2. 
6. Visualising the navigation process in RViz2. 