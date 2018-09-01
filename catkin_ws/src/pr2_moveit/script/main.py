#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
#from fwdK_csv import *
from class_helper import *


def main():
    print "============ Press `Enter` to start (press ctrl-d to exit) ......"
    raw_input()
    demoOBJECT = move_group()

    #demoOBJECT.pose_estimation_img()
    #exit(0)

    counter=0
    while(True):
        print "\n============ Press `Enter` to execute a movement using a joint state goal ..."
        raw_input()
        demoOBJECT.go_to_joint_state()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
