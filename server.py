import socket
import pdb
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





