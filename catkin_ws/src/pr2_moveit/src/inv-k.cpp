/*
 * inv-k.cpp
 * Copyright (C) 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
 *
 * Distributed under terms of the BSD license.
 */

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <moveit_visual_tools/moveit_visual_tools.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "inverse_kinematics");
    ros::NodeHandle node_handle;
    ros::AsyncSpinner spinner(1);
    spinner.start();

    // Setup
    // MoveIt! operates on sets of joints called "planning groups"
    static const std::string PLANNING_GROUP = "right_arm";

    // The :move_group_interface:`MoveGroup` class can be setup using just the name of the planning group you would like to control and plan for.
    moveit::planning_interface::MoveGroupInterface move_group(PLANNING_GROUP);

    // Raw pointers are frequently used to refer to the planning group for improved performance.
    const robot_state::JointModelGroup *joint_model_group = move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP);


    // Visualization
    // The package MoveItVisualTools for visualizing objects, robots, and trajectories in Rviz. Also debugging tools
    namespace rvt = rviz_visual_tools;
    moveit_visual_tools::MoveItVisualTools visual_tools("odom_combined");
    visual_tools.deleteAllMarkers();
    // Remote control is an introspection tool that allows users to step through the script a keyboard in Rviz
    visual_tools.loadRemoteControl();
    // Rviz provides many types of markers, in this demo we will use text, cylinders, and spheres
    Eigen::Affine3d text_pose = Eigen::Affine3d::Identity();
    text_pose.translation().z() = 1.60; // above head of PR2
    visual_tools.publishText(text_pose, "Inverse Kinematics", rvt::WHITE, rvt::XLARGE);
    // Batch publishing is used to reduce the number of messages being sent to Rviz for large visualizations
    visual_tools.trigger();
    visual_tools.prompt("next step");

    // Getting Basic Information
    // We can print the name of the reference frame for this robot.
    ROS_INFO_NAMED("###", "Reference frame: %s", move_group.getPlanningFrame().c_str());
    // We can also print the name of the end-effector link for this group.
    ROS_INFO_NAMED("###", "End effector link: %s", move_group.getEndEffectorLink().c_str());

    // Planning to a pose goal
    //###############################
    // To start, we'll create an pointer that references the current robot's state.
    // RobotState is the object that contains all the current position/velocity/acceleration data.
    moveit::core::RobotStatePtr current_state = move_group.getCurrentState();


    // Next get the current set of joint values for the group.
    std::vector<double> joint_group_positions;
    current_state->copyJointGroupPositions(joint_model_group, joint_group_positions);


    //Printing information about joints
    //=====================================================================================

    const std::vector<std::string>& joint_names = joint_model_group->getVariableNames();

    // We can retreive the current set of joint values stored in the state for the PR2 arm.
    std::vector<double> joint_values;
    current_state->copyJointGroupPositions(joint_model_group, joint_values);


    std::cout<<"==================================================="<<std::endl;
    std::cout<<"Joint values-->Current state... )\n"<<std::endl;
    for (std::size_t i = 0; i < joint_names.size(); ++i)
    {
        ROS_INFO("Joint %s: %f", joint_names[i].c_str(), joint_values[i]);
    }
    const Eigen::Affine3d &end_effector_state1 = current_state->getGlobalLinkTransform("r_wrist_roll_link");


    /* Print end-effector pose. Remember that this is in the model frame */
    std::cout<<"End-effector pose"<<std::endl;
    ROS_INFO_STREAM("Translation: \n" << end_effector_state1.translation() << "\n");
    ROS_INFO_STREAM("Rotation: \n" << end_effector_state1.rotation() << "\n");
    std::cout<<"===================================================="<<std::endl;

    //=====================================================================================


    // Inverse Kinematics
    // We can plan a motion for this group to a desired pose for the end-effector.
    std::cout<<".......................................................\n"<<std::endl;
    std::cout<<"Inverse Kinematics \n"<<std::endl;
    std::cout<<".......................................................\n"<<std::endl;

    geometry_msgs::Pose target_pose1;
    target_pose1.orientation.w = 1.0;
    target_pose1.position.x = 0.28;
    target_pose1.position.y = -0.7;
    target_pose1.position.z = 1.0;

    move_group.setPoseTarget(target_pose1);


    ROS_INFO("%.f",target_pose1.orientation.w);

    // Now, we call the planner to compute the plan and visualize it. Note that we are just planning, not asking move_group
    // to actually move the robot.
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    bool success = (move_group.plan(my_plan) == moveit::planning_interface::MoveItErrorCode::SUCCESS);
    ROS_INFO_NAMED("###", "Visualizing plan (Pose goal) %s", success ? "" : "FAILED");

    //=====================================================================================

    std::cout<<"======================================================="<<std::endl;
    std::cout<<"Joint values--> final state... \n)"<<std::endl;
    for (std::size_t i = 0; i < joint_names.size(); ++i)
    {
        ROS_INFO("Joint %s: %f", joint_names[i].c_str(), joint_values[i]);
    }
    const Eigen::Affine3d &end_effector_state2 = current_state->getGlobalLinkTransform("r_wrist_roll_link");


    /* Print end-effector pose. Remember that this is in the model frame */
    std::cout<<"End-effector pose"<<std::endl;
    ROS_INFO_STREAM("Translation: \n" << end_effector_state2.translation() << "\n");
    ROS_INFO_STREAM("Rotation: \n" << end_effector_state2.rotation() << "\n");
    std::cout<<"=========================================================="<<std::endl;



    //=====================================================================================


    // Visualize the plan in Rviz
    visual_tools.deleteAllMarkers();
    ROS_INFO_NAMED("###", "Visualizing plan 1 as trajectory line");
    visual_tools.publishAxisLabeled(target_pose1, "pose1");
    visual_tools.publishText(text_pose, "Pose Goal", rvt::WHITE, rvt::XLARGE);
    visual_tools.publishTrajectoryLine(my_plan.trajectory_, joint_model_group);
    visual_tools.trigger();


    /* Uncomment below line when working with a real robot */
    move_group.move();



    // END

    ros::shutdown();
    return 0;
}











/*
The RobotModel and RobotState classes are the core classes that give you access to a robot’s kinematics.

The RobotModel class contains the relationships between all links and joints including their joint limit properties as loaded from the URDF.

The RobotState contains information about the robot at a snapshot in time, storing vectors of joint positions and optionally velocities and accelerations that can be used to obtain kinematic information about the robot that depends on it’s current state such as the Jacobian of an end effector.


*/


