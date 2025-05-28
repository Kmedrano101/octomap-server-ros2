# Octomap for ROS2

This package provides an integration of the OctoMap library with ROS2 (Humble distribution). It enables 3D occupancy mapping using octrees, allowing efficient environment representation for robotic applications. The package includes ROS2 nodes and interfaces for publishing, updating, and querying octomap data.

## Dependencies

To install the required Octomap ROS 2 packages (`octomap-ros`, `octomap-msgs`, and `octomap-mapping`) on ROS 2 Humble, run:

```bash
sudo apt install ros-humble-octomap-ros ros-humble-octomap-msgs ros-humble-octomap-mapping
```