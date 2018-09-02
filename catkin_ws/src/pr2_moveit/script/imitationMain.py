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
    sample=sample.reshape((1,6))
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

    print "============ Press `Enter` to initialize (press ctrl-d to exit) ......"
    raw_input()
    time.sleep(3)

    counter=0
    while(True):
        counter+=1
        # Capture frame-by-frame
        _, frame = cap.read()

        #Estimate human poses from a single image
        pose=pose_OBJ.model_PEST.inference(frame,pose_OBJ.resize_to_default,pose_OBJ.resize_out_ratio)

        # draw points and draw lines
        img= TfPoseEstimator.draw_humans(frame, pose, imgcopy=False)

        # show img with cv2 when working with the camera
        cv2.imshow('Pose Estimation', img)

        if  cv2.waitKey(1) & 0xFF== ord('s'):
            print('Goodbye!!!')
            break
        # show image with matplotlib when working with a single image
        #plotOBJ.plotting(img)

        # get the key points for the right hand (a list data structure)
        sampleList=keyOBJ.get_keypoints(pose)

        # get the sample with a new shape from 1D array into 2D array
        print('wit the list:',len(sampleList))
        sampleArray=sample_reshape(sampleList)
        print('with the array:',sampleArray.shape)

        '''
        #Mapping from the pose estimation frame into the robot frame
        '''
        y_hat1=loaded_model.predict(sampleArray)
        y_hat2=map_OBJ.loaded_model.predict(sampleArray)

        #make the movement with the new predicted joint values
        robot_OBJ.go_to_joint_state(counter,y_hat1)

        #cleaning the list in order to avoid the append action
        del sampleList[:]

    #=================================
    # release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()


if __name__=='__main__':
    #tmp='images/q1.jpg'
    #Load the image
    #tmp= cv2.imread(tmp, cv2.IMREAD_COLOR)
    try:
        main()
    except rospy.ROSInterruptException:
        pass
