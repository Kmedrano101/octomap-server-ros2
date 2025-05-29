#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

"""
  Example launch file for octomap_server mapping: 
  Listens to incoming PointCloud2 data and incrementally builds an octomap. 
  The data is sent out in different representations.
"""

def generate_launch_description():

    # Create octomap server node
    octomap_server_node = Node(
        package='octomap_server',
        executable='octomap_server_node',
        name='octomap_server',
        parameters=[{
            'frame_id': 'camera_init', # simulated frame: map
            'base_frame_id': 'body', # simulated frame: drone_base_link
            'use_sim_time': False,
            'resolution': 0.5,
            'sensor_model/max_range': 70.0,
            'sensor_model/min_range': 0.05,
            'publish_free_space': True,
            'project_2d_map': True,
            'filter_ground_plane': False
        }],
        remappings=[
            ('cloud_in', '/cloud_registered'), # simulated topic: /px4_drone/depth_camera/points_transformed
        ]
    )
    
    # Return the launch description
    return LaunchDescription([
        octomap_server_node
    ]) 
    