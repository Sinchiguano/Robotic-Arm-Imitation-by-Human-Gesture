#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import csv
import copy
import numpy as np
import cv2
import sys
import time
from tqdm import *
from matplotlib import pyplot as plt

#for pose estimation
import cv2
import matplotlib.pyplot as plt
from tf_pose.estimator import TfPoseEstimator
from tf_pose import *

joints=['r_shoulder_pan_joint',
              'r_shoulder_lift_joint',
              'r_upper_arm_roll_joint',
              'r_elbow_flex_joint',
              'r_forearm_roll_joint',
              'r_wrist_flex_joint',
              'r_wrist_roll_joint']
