cmake_minimum_required(VERSION 2.8.3)
project(pr2_moveit)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(Eigen3 REQUIRED)

# Eigen 3.2 (Wily) only provides EIGEN3_INCLUDE_DIR, not EIGEN3_INCLUDE_DIRS
if(NOT EIGEN3_INCLUDE_DIRS)
  set(EIGEN3_INCLUDE_DIRS ${EIGEN3_INCLUDE_DIR})
endif()

find_package(catkin REQUIRED
  COMPONENTS
    moveit_core
    moveit_ros_planning
    moveit_ros_planning_interface
    pluginlib
    geometric_shapes
    moveit_visual_tools
)

find_package(Boost REQUIRED system filesystem date_time thread)

catkin_package(
  CATKIN_DEPENDS
    moveit_core
    moveit_ros_planning_interface
    interactive_markers
  DEPENDS
    EIGEN3
)

###########
## Build ##
###########

include_directories(SYSTEM ${Boost_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIRS})
include_directories(${catkin_INCLUDE_DIRS})
link_directories(${catkin_LIBRARY_DIRS})

############################################################################


#########################################################################
add_executable(fwdk src/fwd-k.cpp)
target_link_libraries(fwdk ${catkin_LIBRARIES} ${Boost_LIBRARIES})
install(TARGETS fwdk DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

add_executable(invk src/inv-k.cpp)
target_link_libraries(invk ${catkin_LIBRARIES} ${Boost_LIBRARIES})
install(TARGETS invk DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
