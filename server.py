
'''
    udp socket server
    Maxime Devos
'''

import socket
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print "waiting on port:", port
while 10:
    data, addr = s.recvfrom(1024)
    print data + "received from" + addr