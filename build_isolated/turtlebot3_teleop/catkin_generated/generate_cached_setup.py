# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_slam;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_simulations;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_navigation;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_fake;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_example;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_bringup;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_msgs;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_gazebo;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_description;/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3;/home/ikebe/turtlebot3_ws/devel_isolated/goal_send;/home/ikebe/turtlebot3_ws/devel;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/ikebe/turtlebot3_ws/devel_isolated/turtlebot3_teleop/env.sh')

output_filename = '/home/ikebe/turtlebot3_ws/build_isolated/turtlebot3_teleop/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
