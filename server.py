import socket
import pdb
import rostopic
import subprocess
from image_converter import img_converter
from purge import purge

s= socket.socket()
port = 8080
s.bind(('',port))
f = open('stored.mp4','wb')
s.listen(5)
while True:
    print 'waiting'
    c, addr = s.accept()
    print 'Connected to', addr
    f = open('stored.mp4','wb')
    packet = c.recv(1024)
    print 'receiving video ...'
    while(packet):
        f.write(packet)
        packet = c.recv(1024)
    f.close()
    print 'Done'
    c.close()
    purge()
    img_converter('stored.mp4')
    #check that ROS is running on the server
    try:
        rostopic.rosgraph.Master('/rostopic').getPid()
    except socket.error:
        try:
            subprocess.Popen(['roslaunch', 'ORB_SLAM/ExampleGroovyOrNewer.launch'])
        except error:
            raise rostopic.ROSTopicIOException("can't communicate with server")
    try:
        subprocess.Popen(['rosrun', 'BagFromImages', 'BagFromImages', 'images/', '.png', '30', 'ORB_SLAM/Data/Example.bag']) 
        subprocess.Popen(['rosbag', 'play', 'ORB_SLAM/Data/Example.bag'])
    except error:
        raise rostopic.ROSTopicIOException("can't run ORB_SLAM")
        




