import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))
while True:
	data, (addr, port) = s.recvfrom(1024)
	print "Received data from", addr, "port", port
	print data
	content = "Hello "+socket.gethostname()+"!"
	s.sendto(content, (addr, port))
