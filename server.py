import socket
import pdb

s= socket.socket()
port = 8080
s.bind(('',port))
f = open('stored.mp4','wb')
print 'waiting'
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Connected to', addr
    f = open('stored.mp4','wb')
    packet = c.recv(1024)
    while(packet):
        #pdb.set_trace()
        f.write(packet)
        packet = c.recv(1024)
    f.close()
    print 'Done'
    c.close()



