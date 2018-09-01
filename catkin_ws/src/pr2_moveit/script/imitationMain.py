#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

from imitationClass import *
from sklearn.externals import joblib

def sample_reshape(sample):
    print('========================')
    sample=np.asarray(sample)
    # print('Sample shape before:',sample.shape)
    # print('type:',type(sample))
    sample=sample.reshape((1,6))
    # print('Sample shape after:',sample.shape)
    # print('type:',type(sample))
    return sample


def main():


    #Instantiate an object in order to get the model for pose estimation
    pose_OBJ=poseEstimation()
    #Instantiate an object in order to get the model for mapping from pose estimation frame into robot frame
    map_OBJ=mappingRobot()
    #Instantiate an object in order to command the robot movement
    robot_OBJ=moveGroup()
    #Instantiate an object in order to get the  key points
    keyOBJ=keyPoints()
    #Instantiate an object in order to retrieve the MultiOutputRegressor
    loaded_model = joblib.load('nn_keras/pre_trained_model.sav')
    # Instantiate an object in order to read from input camera
    cap = cv2.VideoCapture(0)
    #Instantiate an object in order to plot the data set
    plotOBJ=dataPlot()
    #while(True):

    # Capture frame-by-frame
    #_, frame = cap.read()
    #Estimate human poses from a single image
    pose=pose_OBJ.model_PEST.inference(tmp,pose_OBJ.resize_to_default,pose_OBJ.resize_out_ratio)
    # draw points and draw lines
    #img= TfPoseEstimator.draw_humans(tmp, pose, imgcopy=False)

    # show img with cv2 when working with the camera
    #cv2.imshow('Pose Estimation', img)

    # show image with matplotlib
    #plotOBJ.plotting(img)

    # get the key points for the right hand
    sample=keyOBJ.get_keypoints(pose)

    # get the sample with a new shape
    sample=sample_reshape(sample)


    #Make predictions
    y_hat1=loaded_model.predict(sample)
    y_hat2=map_OBJ.loaded_model.predict(sample)
    print(y_hat1)
    print(y_hat2)


    robot_OBJ.go_to_joint_state(y_hat1)

    #Mapping from pose estimation frame into robot frame
    #jointsPredict=map_OBJ.loaded_model.predict(whateverX_test)

    # #=================================
    # # release the video capture object
    # cap.release()
    # # Closes all the frames
    # cv2.destroyAllWindows()



    # print "============ Press `Enter` to start (press ctrl-d to exit) ......"
    # raw_input()
    # demoOBJECT = moveGroup()
    #
    # counter=0
    # while(True):
    #     print "\n============ Press `Enter` to execute a movement using a joint state goal ..."
    #     raw_input()
    #     counter+=1
    #     demoOBJECT.go_to_joint_state(counter)

if __name__=='__main__':
    tmp='images/q1.jpg'
    #Load the image
    tmp= cv2.imread(tmp, cv2.IMREAD_COLOR)
    try:
        main()
    except rospy.ROSInterruptException:
        pass
