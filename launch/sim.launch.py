#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ld = LaunchDescription()

    # Declare a launch argument for rviz
    rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Set to true to enable RViz visualization'
    )

    # Launch husky simulation environment
    clearpath_environment = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('clearpath'), '/clearpath_gz/launch/simulation.launch.py']),
        condition=LaunchConfiguration('rviz_arg'),
        remappings=[('some_topic', '/input_cloud'),
                    ('some_topic', '/imu')
                    ]
    )
    clearpath_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('clearpath'), '/clearpath_control/launch/control.launch.py'])
    )

    # clearpath has a built in slam option that could work - https://docs.clearpathrobotics.com/docs/ros/tutorials/navigation_demos/slam

    # Launch graph based slam
    graph_based_slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [get_package_share_directory('lidarslam_ros2'), '/graph_based_slam/launch/graphbasedslam.launch.py'])
    )
    # requires the following topics
    # /input_cloud  (sensor_msgs/PointCloud2)  
    # /tf(from "base_link" to LiDAR's frame)  
    # /initial_pose  (geometry_msgs/PoseStamed)(optional)  
    # /imu  (sensor_msgs/Imu)(optional)  
    # /tf(from "odom" to "base_link")(Odometry)(optional)  


    # # Launch for node in the g2o_slam package
    # node_1 = Node(
    #     package='your_package_name',
    #     executable='node_1_executable',
    #     name='node_1'
    # )

    ld.add_action(graph_based_slam)
    ld.add_action(clearpath_environment)
    # ld.add_action(node_1)

    return ld
