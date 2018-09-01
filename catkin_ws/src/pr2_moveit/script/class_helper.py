#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

from libraries import *


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

        self.tmp_joints=['r_shoulder_pan_joint',
                      'r_shoulder_lift_joint',
                      'r_upper_arm_roll_joint',
                      'r_elbow_flex_joint',
                      'r_forearm_roll_joint',
                      'r_wrist_flex_joint',
                      'r_wrist_roll_joint']

        self.part=['RAnkle = 0','RKnee = 1','RHip = 2','LHip = 3',
                    'LKnee = 4','LAnkle = 5','RWrist = 6',
                    'RElbow = 7','RShoulder = 8','LShoulder = 9',
                    'LElbow = 10','LWrist = 11','Neck = 12','Head = 13']
        self.part_xy=['RWrist = 6x','RWrist = 6y',
                        'RElbow = 7x','RElbow = 7y',
                        'RShoulder = 8x','RShoulder = 8y']
        self.header= copy.copy(self.tmp_joints)

        self.name_file='joint_data.csv'


        # with open(self.name_file, 'wb') as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     for i in range(len(self.part_xy)):
        #         self.header.append(self.part_xy[i])
        #     filewriter.writerow(self.header)

        #DEFAULT PARAMETERS
        self.resize='432x368'#Recommends : 432x368
        self.resize_to_default=True
        self.resize_out_ratio=4.0#default

        #pose estimation
        self.resize='432x368'#Recommends : 432x368
        self.resize_to_default=True
        self.resize_out_ratio=4.0#default

        self.model_add='./mobilenet_thin/graph_opt.pb'
        self.image_path='tmp.jpg'
        self.init_counter=0




    def go_to_joint_state(self):
        running=True
        group = self.group
        self.init_counter+=1;#save in the memory

        ## Planning to a joint-space goal
        joint_goal=group.get_random_joint_values()

        #===============================
        for i in range(len(joint_goal)):
            print(i,self.tmp_joints[i],joint_goal[i])

        group.set_joint_value_target(joint_goal)

        print "============ Waiting while RVIZ displays plan..."
        self.box_alert(running)
        running=False
        plan = group.plan()
        #When working with the real robot uncomment the following line...
        #group.execute(plan)
        import time
        time.sleep(18)
        self.box_alert(running)
        print('Imitate the robot movement, please!!!')

        '''Creating my CSV file'''
        self.csv_file(joint_goal)#go to my method csv file with the joint_goal

        #It is better to create a copy instead of passing the value directly, it will overwrite.
        print "============ Joint values: "
        #print(self.tmp_joints)
        #print(joint_goal)#for debugging

        print('Counte:',self.init_counter)
        print('done!!!')

    def box_alert(self,running):
        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = self.group.get_planning_frame()
        box_pose.pose.position.x =0;
        box_pose.pose.position.y = 0.5;
        box_pose.pose.position.z = 0.5;
        box_pose.pose.orientation.w = 0.5
        box_name = "box"
        if running:#show the box
            self.scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))
        else:
            self.scene.remove_world_object(box_name)

    def csv_file(self,joint_list):
        #Opening a file with the 'a' parameter allows you to append to the end of the file instead of simply overwriting the existing content.
        tmp_list=copy.copy(joint_list)#it is a good approach to create copy in order not to overwrite the arguments.
        with open(self.name_file, 'a') as csvfile:# a means append
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #Opening the webcamera to get a frame
            self.cv2_frame()
            #Get the pose estimation from the frame above
            tmp_pose_list=self.pose_estimation_img()
            #Append coordinates X and Y of my shoulder, elbow and wrist to my
            # my joints list and save them in the csv file.
            for i in tmp_pose_list:
                tmp_list.append(i)
            filewriter.writerow(tmp_list)

    def cv2_frame(self):
        cap = cv2.VideoCapture(0)
        print('====================================================================')
        print('Press "Q key" to get a sample pic in order to generate the keypoints!')
        print('=====================================================================')
        pbar = tqdm(ascii=True)
        counter1=0

        time_out = time.time() + 10
        while(True):
            counter1+=1
            # Capture frame-by-frame
            ret, frame = cap.read()

            if ret == True:
                cv2.imshow('frame',frame)
                if cv2.waitKey(30) & 0xFF == ord('q') or time.time()>time_out:
                    cv2.imwrite(self.image_path,frame)
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            else:
                break
            pbar.update(counter1)
            time.sleep(0.01)
        pbar.close()
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def pose_estimation_img(self):
        #Load the image
        img= cv2.imread(self.image_path, cv2.IMREAD_COLOR)

        #Resize image before they are processed.
        w, h = map(int, self.resize.split('x'))

        #Load my pretrained model according to my target size
        model_POSEest = TfPoseEstimator(self.model_add, target_size=(w, h))

        #Estimate human poses from a single image
        poseESTIMATION=model_POSEest.inference(img,True,4.0)

        points_2d=[];
        for human in poseESTIMATION:
            points_2d,visibility=common.MPIIPart.from_coco(human);

        #points_2d=np.array(points_2d)

        tmp=list()
        aux=[]
        tmptmp=list
        tmp_xy=[]
        for i in range(len(points_2d)):
            #print(self.part[i],':',points_2d[i])
            if (i==6)or(i==7)or(i==8):
                tmptmp=list(points_2d[i])
                tmp_xy.append(tmptmp[0])
                tmp_xy.append(tmptmp[1])
                tmp.append(list(points_2d[i]))
                aux.append(self.part[i])

        print('--------------------------------------------')
        print('keypoints of interest for the right hand!!!')
        print('--------------------------------------------')

        for i in range(len(tmp)):
            print(aux[i],tmp[i])

        # draw points and draw lines
        img= TfPoseEstimator.draw_humans(img, poseESTIMATION, imgcopy=False)

        #Colors and color conversions>>Convert image to RGB color for matplotlib
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # show image with matplotlib
        self.plotting(img)

        return tmp_xy

    def plotting(self,img):
        plt.figure('Pose Estimation!')
        plt.title('Result!')
        plt.imshow(img)
        plt.pause(4)
    '''
https://github.com/ros-planning/moveit/blob/kinetic-devel/moveit_commander/src/moveit_commander/move_group.py
'''
