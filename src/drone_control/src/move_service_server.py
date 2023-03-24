#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from my_service_pkg.srv import drone_msg,drone_msgResponse


def execute_circle():
    # Command the drone to execute a circle trajectory
    rospy.loginfo("Moving in a circle...")
    radius = 1.0  # the radius of the circle
    angular_speed = 1.0  # the angular speed of the drone
    _move_msg=Twist()

    # Move the drone in a circular path
    t0 = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - t0 < 10.0:  # move for 10 seconds
        _move_msg.linear.x = angular_speed * radius
        _move_msg.angular.z = angular_speed
        my_pub.publish(_move_msg)
        rospy.sleep(0.1)


    rospy.loginfo("Executing circle trajectory...")

    _move_msg.linear.x = 0.0
    _move_msg.angular.z = 0.0
    my_pub.publish(_move_msg)

    # ... code to execute the circle trajectory ...

def execute_square():

    # Command the drone to execute a square trajectory
    rospy.loginfo("Executing square trajectory...")
    # ... code to execute the square trajectory ...

def execute_triangle():
    # Command the drone to execute a triangle trajectory
    rospy.loginfo("Executing triangle trajectory...")
    # ... code to execute the triangle trajectory ...


# function that makes the drone stop
def stop_drone(self):
  rospy.loginfo("Stopping...")
  self._move_msg.linear.x = 0.0
  self._move_msg.angular.z = 0.0
  self.publish_once_in_cmd_vel(self._move_msg)

# function that makes the drone turn
def turn_drone(self):
  rospy.loginfo("Turning...")
  self._move_msg.linear.x = 0.0
  self._move_msg.angular.z = 1.0
  self.publish_once_in_cmd_vel(self._move_msg)

# function that makes the drone move forward
def move_forward_drone(self):
  rospy.loginfo("Moving forward...")
  self._move_msg.linear.x = 1.0
  self._move_msg.angular.z = 0.0
  self.publish_once_in_cmd_vel(self._move_msg)



def handle_trajectory_service(req):
    # Process the service request

     if req.label == "circle" | req.label == "square" |  req.label == "triangle" : 

        if req.label == "circle":
            execute_circle()   
        elif req.label == "square":
            execute_square()   
        elif req.label == "triangle":
            execute_triangle()   

        return drone_msgResponse(success=True, message="Trajectory executed successfully")

     else:
      return drone_msgResponse(success=False, message="Invalid request")


rospy.init_node('trajectory_service_server')
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
_move_msg=Twist()

    # Create a service server and register the callback function
srv = rospy.Service('execute_trajectory', drone_msg, handle_trajectory_service)

rospy.loginfo("Trajectory Service Server is ready.")

    # Spin the node to prevent it from exiting
rospy.spin()