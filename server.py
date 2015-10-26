import socket

s= socket.socket()
port = 8081
s.bind(('',port))
f = open('stored.mp4','wb')
print 'waiting'
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Connected to', addr
    packet = c.recv(1024)
    while(packet):
        f.write(packet)
        packet = c.recv(1024)
    f.close()
    print 'Done'
    c.close()



