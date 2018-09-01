#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

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
from tqdm import *

#for pose estimation
import matplotlib.pyplot as plt
from tf_pose.estimator import TfPoseEstimator
from tf_pose import *
import numpy as np
import cv2
import sys
import time
from tqdm import *
from matplotlib import pyplot as plt
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from keras.models import model_from_json
import numpy,h5py
import os

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD



joints=['r_shoulder_pan_joint',
              'r_shoulder_lift_joint',
              'r_upper_arm_roll_joint',
              'r_elbow_flex_joint',
              'r_forearm_roll_joint',
              'r_wrist_flex_joint',
              'r_wrist_roll_joint']
