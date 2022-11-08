import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)
print "Da khoi tao xong Server."
while True:
	clientConnection, (clientHost, clientPort) = s.accept()
	print "Connected to Client:", clientHost, "port", clientPort
	while True:
                try:
                        content = clientConnection.recv(1024).decode()
                        if (content == "#quit"):
                                break
                        clientConnection.sendall(content.encode())
                except:
                        break
	clientConnection.close()
	print "Disconnected to Client:", clientHost, "port", clientPort
