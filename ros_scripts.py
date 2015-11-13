import socket
import subprocess
import rostopic
import time

def create_bag():
    try:
        rostopic.rosgraph.Master('/rostopic').getPid()
        subprocess.Popen(['rosrun', 'BagFromImages', 'BagFromImages', 'images/', '.png', '30', 'ORB_SLAM/Data/Example.bag']).wait()
    except socket.error:
        print 'trying again'
        create_bag()

def play_bag():
    try:
        rostopic.rosgraph.Master('/rostopic').getPid()
        subprocess.Popen(['rosbag', 'play', 'ORB_SLAM/Data/Example.bag']).wait()
    except socket.error:
        raise rostopic.ROSTopicIOException("can't run ORB_SLAM")
    
def checkROS():
    try:
        rostopic.rosgraph.Master('/rostopic').getPid()
    except socket.error:
        launchROS()
    
def launchROS():
    try:
        subprocess.Popen(['roslaunch', 'ORB_SLAM/ExampleGroovyOrNewer.launch'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except:
        raise rostopic.ROSTopicException("Can't launch ROS Master")
