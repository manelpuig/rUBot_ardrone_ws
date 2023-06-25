# **Tello Drone Install**
Follow the documentation in:
https://github.com/anqixu/tello_driver/tree/master

Some modifications are explained in:
https://www.youtube.com/watch?v=uMiXP_AwhmM

These modifications are:
- sudo apt install python3-pip
- sudo -H pip3 install -e .
- open file tello_driver_node.py and change to python3
- catkin_make

# **Running the driver**

Turn on drone and wait for its front lights to blink amber

connect WiFi to drone's access point (e.g. TELLO_######)

$ roslaunch tello_driver tello_node.launch

To see the camera:

$ rosrun rqt_image_view rqt_image_view /tello/image_raw/compressed