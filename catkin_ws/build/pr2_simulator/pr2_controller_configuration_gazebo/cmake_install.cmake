# Install script for directory: /home/casch/Dropbox/humanoid_robot/catkin_ws/src/pr2_simulator/pr2_controller_configuration_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/casch/Dropbox/humanoid_robot/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/casch/Dropbox/humanoid_robot/catkin_ws/build/pr2_simulator/pr2_controller_configuration_gazebo/catkin_generated/installspace/pr2_controller_configuration_gazebo.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pr2_controller_configuration_gazebo/cmake" TYPE FILE FILES
    "/home/casch/Dropbox/humanoid_robot/catkin_ws/build/pr2_simulator/pr2_controller_configuration_gazebo/catkin_generated/installspace/pr2_controller_configuration_gazeboConfig.cmake"
    "/home/casch/Dropbox/humanoid_robot/catkin_ws/build/pr2_simulator/pr2_controller_configuration_gazebo/catkin_generated/installspace/pr2_controller_configuration_gazeboConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pr2_controller_configuration_gazebo" TYPE FILE FILES "/home/casch/Dropbox/humanoid_robot/catkin_ws/src/pr2_simulator/pr2_controller_configuration_gazebo/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pr2_controller_configuration_gazebo/config" TYPE DIRECTORY FILES "/home/casch/Dropbox/humanoid_robot/catkin_ws/src/pr2_simulator/pr2_controller_configuration_gazebo/config/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pr2_controller_configuration_gazebo/launch" TYPE DIRECTORY FILES "/home/casch/Dropbox/humanoid_robot/catkin_ws/src/pr2_simulator/pr2_controller_configuration_gazebo/launch/")
endif()

