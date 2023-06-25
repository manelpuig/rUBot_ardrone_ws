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

# **Tello drone device registering**

First time you have to register your Tello drone device:
- Download the Tello app: https://play.google.com/store/apps/details?id=com.ryzerobotics.tello&hl=es_UY&pli=1
- connect the mobile phone to the Tello Access point
- You will be asked to register your device
- test the take-off first control
- perform a landing

Now you are ready to work with your computer using ROS

# **Running the driver**

Whe using ROS in Docker to control your Tello drone:
- Turn on drone and wait for its front lights to blink amber
- connect WiFi to drone's access point (e.g. TELLO_######)
- Start the main Tello node
```shell
roslaunch tello_driver tello_node.launch
```
- Open a new terminal and see all the topics
- Open 2 new terminals and type for take off and landing
```shell
rostopic pub /tello/takeoff std_msgs/Empty "{}"
rostopic pub /tello/land std_msgs/Empty "{}
```

To see the camera:

$ rosrun rqt_image_view rqt_image_view /tello/image_raw/compressed