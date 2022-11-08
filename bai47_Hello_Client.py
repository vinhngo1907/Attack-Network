import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hi Server!", ('127.0.0.1', 9999))
data, (addr, port) = s.recvfrom(1024)
print data
s.close()
