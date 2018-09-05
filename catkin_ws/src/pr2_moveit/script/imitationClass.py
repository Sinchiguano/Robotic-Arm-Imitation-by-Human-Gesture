#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

from imitationLibrary import*


jointsNames=joints


class rosInit(object):
    '''
    '''

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

        # """ Get the current configuration of the group as a list (these are values published on /joint_states) """
        # self.home_joints= self.group.get_current_joint_values()
        # ''''Get the current pose of the end-effector of the group.'''
        # self.home_state=self.robot.get_current_state()


class moveGroup(object):
    '''
    '''
    def __init__(self):

        self.rosInit_OBJECT=rosInit()
        self.tmp_joints=jointsNames

    def go_to_joint_state(self,counter,y_hat1):
        group = self.rosInit_OBJECT.group

        ## Planning to a joint-space goal
        #================================
        print('#================================')
        #joint_goal=group.get_random_joint_values()
        y_hat1=y_hat1.reshape(7,)
        #print(y_hat1.shape)
        joint_goal=y_hat1.tolist()

        print "============ Joint values: "
        for i in range(len(joint_goal)):
            print(i,self.tmp_joints[i],joint_goal[i])

        group.set_joint_value_target(joint_goal)

        plan = group.plan()

        #When working with the real robot uncomment the following line...
        #group.execute(plan)
        del joint_goal[:]
        print "============ Waiting while RVIZ displays plan..."
        print('Counter:',counter)
        print('done!!!')

class poseEstimation(object):
    '''
    '''
    def __init__(self):

        #DEFAULT PARAMETERS
        self.resize='432x368'#Recommends : 432x368
        self.resize_to_default=True
        self.resize_out_ratio=4.0#default
        self.model_path='mobilenet_thin/graph_opt.pb'

        #Resize image before they are processed.
        self.w, self.h = map(int, self.resize.split('x'))

        #Load my pretrained model according to my target size
        self.model_PEST = TfPoseEstimator(self.model_path, target_size=(self.w, self.h))

class keyPoints(object):
    '''
    '''
    def __init__(self):
        self.points_2d=list()
        self.tmp_xy=list()

    def get_keypoints(self,predictions):
        points_2d=list()
        for human in predictions:
            points_2d,visibility=common.MPIIPart.from_coco(human);
        for i in range(len(points_2d)):
            if (i==6)or(i==7)or(i==8):
                temp_list=list(points_2d[i])
                self.tmp_xy.append(temp_list[0])
                self.tmp_xy.append(temp_list[1])
        return self.tmp_xy

class mappingRobot(object):

    def __init__(self):

        #address to my pretrained model for the joints values
        self.nnModel='nn_keras/model.json'
        # load json and create model
        self.json_file = open(self.nnModel, 'r')
        self.loaded_model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("nn_keras/model.h5")
        self.loaded_model.compile(loss='mean_squared_error', optimizer='rmsprop')

class dataPlot(object):
    '''
    '''
    def __init__(self):
        self.tmp=list()

    def plotting(self,img):

        #Colors and color conversions>>Convert image to RGB color for matplotlib
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure('Pose Estimation!')
        plt.title('Result!')
        plt.imshow(img)
        plt.pause(6)
