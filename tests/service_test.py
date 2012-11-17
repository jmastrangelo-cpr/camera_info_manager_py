#!/usr/bin/env python

# This trivial node is useful for debugging set_camera_info service
# request handling problems.

PKG='camera_info_manager_py'
import roslib; roslib.load_manifest(PKG)
from camera_info_manager import *

rospy.init_node("service_test_node")

cinfo = CameraInfoManager()

# spin in the main thread: required for service callbacks
rospy.spin()
