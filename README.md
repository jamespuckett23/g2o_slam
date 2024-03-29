## This package works as a basis to control the husky clearpath robot

For more information on the clearpath husky robot, visit https://docs.clearpathrobotics.com/docs/ros/

# ws environment:
ws/src/
- clearpath_common/ -> https://github.com/clearpathrobotics/clearpath_common
- g2o_slam/ (this package)
- lidarslam_ros2/ -> https://github.com/rsasaki0109/lidarslam_ros2/tree/humble

# SLAM Options:
- Clearpath has a built in slam option that might be the simplist to get running. I don't know if it is visual or graph-based
- lidarslam_ros2 has a graph-based slam option that would be easy and simple as well. The benefit is that it is open source and its easy to adjust specifically for our needs

# Running:
- The launch file is not finished, but with a little more work the following should work
- ros2 launch g2o_slam sim.launch.py
    - Launches gazebo, rviz, clearpath-husky control, and lidarslam_ros2 (or clearpath's slam option)
    - Maps required topics to the lidarslam_ros2 package


# To do
- Flush out the bugs in sim.launch.py (make sure to use the correct launch files/map topics correctly/launch the slam)
- Select the best slam option
- Test in sim to place waypoints as desired