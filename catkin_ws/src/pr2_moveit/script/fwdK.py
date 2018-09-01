#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list



class move_group(object):

    def __init__(self):
        ''' First initialize moveit_commander and rospy.'''
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_python',anonymous=True)

        '''Instantiate a RobotCommander object. This object is an interface to
        the robot as a whole.'''
        self.robot = moveit_commander.RobotCommander()

        '''Instantiate a MoveGroupCommander object.  This object is an interface
        to one group of joints.'''
        self.group = moveit_commander.MoveGroupCommander("right_arm")

        """ Get the current configuration of the group as a list (these are values published on /joint_states) """
        self.home_joints= self.group.get_current_joint_values()
        ''''Get the current pose of the end-effector of the group.'''
        self.home_state=self.robot.get_current_state()

        '''Instantiate a `PlanningSceneInterface`_ object.  This object is an interface
        to the world surrounding the robot:'''
        self.scene = moveit_commander.PlanningSceneInterface()
        self.tmp_joints=list()
        self.tmp_joints=['r_shoulder_pan_joint',
                      'r_shoulder_lift_joint',
                      'r_upper_arm_roll_joint',
                      'r_elbow_flex_joint',
                      'r_forearm_roll_joint',
                      'r_wrist_flex_joint',
                      'r_wrist_roll_joint']


    def go_to_joint_state(self,counter):
        group = self.group

        ## Planning to a joint-space goal
        #================================
        joint_goal=group.get_random_joint_values()
        print "============ Joint values: "

        for i in range(len(joint_goal)):
            print(i,self.tmp_joints[i],joint_goal[i])
        print('joint_goal')
        print(joint_goal)
        group.set_joint_value_target(joint_goal)

        plan = group.plan()
        #When working with the real robot uncomment the following line...
        #group.execute(plan)

        print "============ Waiting while RVIZ displays plan..."
        self.box_alert()
        print('Counte:',counter)
        print('done!!!')

    def box_alert(self):
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = self.group.get_planning_frame()
        box_pose.pose.position.x =0;
        box_pose.pose.position.y = 0.5;
        box_pose.pose.position.z = 0.5;
        box_pose.pose.orientation.w = 0.5
        box_name = "box"
        import time
        for i in range(12):
            self.scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))
            time.sleep(0.3)
            self.scene.remove_world_object(box_name)
            time.sleep(0.3)


def group_python():
    print "============ Press `Enter` to start (press ctrl-d to exit) ......"
    raw_input()
    demoOBJECT = move_group()
    counter=0
    while(True):
        print "\n============ Press `Enter` to execute a movement using a joint state goal ..."
        raw_input()
        counter+=1
        demoOBJECT.go_to_joint_state(counter)

if __name__=='__main__':
    try:
        group_python()
    except rospy.ROSInterruptException:
        pass



'''
https://github.com/ros-planning/moveit/blob/kinetic-devel/moveit_commander/src/moveit_commander/move_group.py
'''
