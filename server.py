import socket
import pdb
import rostopic
import subprocess
import time
from image_converter import img_converter
from purge import purge
from ros_scripts import checkROS
from ros_scripts import launchROS
from ros_scripts import create_bag
from ros_scripts import play_bag

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
    print 'Video Received'
    c.close()
    print 'purge old images...'
    purge()
    img_converter('stored.mp4')
    #check that ROS is running on the server
    print 'checking ROS...'
    checkROS()
    time.sleep(20)
    create_bag()
    play_bag()

