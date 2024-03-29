# ENPM690 HW3
## Vijay Chevireddi (119491485)
 'Homework 3 ENPM690'
####PART1
### Install Dependencies
To, install these dependencies, run the following commands below.
```sh
sudo apt -y install ros-humble-gazebo-ros-pkgs
sudo apt -y install ros-humble-turtlebot3*
sudo apt -y install ros-humble-turtlebot4-desktop
```
### Launch and Teleoperate
```sh
#Run
 ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
#Teleoperate (Open another terminal and run the below command)
 ros2 run turtlebot3_teleop teleop_keyboard
```
####PART2
### Building and Running
To build and run the simulation, run the following commands.
Firstly, navigate to the source code folder in your workspace ([ros2_ws]/src).
```sh
#Create a workspace and src folder in the workspace
 mkdir -p ~/ros2_ws/src
#Copy the 2 packages provided by me in ~/ros2_ws/src
 copy the packages "my_roomba_controller" and "turtlebot3_simulations" present in 
the src.zip file I provided into the src folder of ros2_ws.
```
Build the workspace
```sh
#Make sure you are in the ros2 workspace directory
 cd ~/ros2_ws
#Make sure there are no dangling dependencies using rosdep
 rosdep install -i --from-path src --rosdistro humble -y
#Build the package:
 colcon build
#If you see a cmake warning, build the workspace again using colcon build
 colcon build
#Install the package:
 source install/setup.bash
```
To run the launch file that executes the simulation, run the following command.
```sh
#Run the Simulation
 ros2 launch turtlebot3_gazebo creddy_world.launch.py
```
#(BONUS POINTS)
####DOCKER
To run the docker container follow the below steps.
Install Docker in Ubuntu using this link: 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-onubuntu-20-04
Running GUI applications like Gazebo from a Docker container requires configuring 
the container to use the host's display server. This setup involves forwarding X11 
(the windowing system used by Linux for GUIs) from the container to your host 
machine. If Gazebo is not opening, it's likely because the container doesn't have 
access to your host's display server. Here are the steps to run Gazebo (or any GUI 
application) from a Docker container on a Linux host:
STEP1: Install X11 X Server Utilities on Your Host (if not already installed)
```sh
 sudo apt-get update && sudo apt-get install -y x11-xserver-utils
```
STEP2: Allow Docker to Access the Host's X Server 
```sh
xhost +local:root
```
There are two ways to run the docker image I created:
WAY1: Pull the image from my Docker Hub account and run the image
```sh
sudo docker pull vijaydevmasters/my_roomba_controller_image:creddy_hw3
sudo docker run -it --rm -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-
unix my_roomba_controller_image
```
```sh
If gazebo is not opening then the access to the host's X server was not setup 
correctly. Run the below command again and then run the image
 xhost +local:root
 sudo docker run -it --rm -e DISPLAY=${DISPLAY} -v 
/tmp/.X11-unix:/tmp/.X11-unix my_roomba_controller_image
```
WAY2: Load the Docker image: my_roomba_controller_image.tar and run the image
```sh
#Copy the file "my_roomba_controller_image.tar" that I provided in ~/ros2_ws
#Load the image using my_roomba_controller_image.tar that is provided by me(Make 
sure that the .tar file is in the directory where you are at present before running
the below command)
 sudo docker load < my_roomba_controller_image.tar
Run the docker image
 sudo docker run -it --rm -e DISPLAY=${DISPLAY} -v 
/tmp/.X11-unix:/tmp/.X11-unix my_roomba_controller_image
```
```sh
If gazebo is not opening then the access to the host's X server was not setup 
correctly. Run the below command again and then run the image
 xhost +local:root
 sudo docker run -it --rm -e DISPLAY=${DISPLAY} -v 
/tmp/.X11-unix:/tmp/.X11-unix my_roomba_controller_image
