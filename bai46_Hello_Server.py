import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)
while True:
    clientConnection, (clienthost, clientport) = s.accept()
    print "Connected to Client:", clienthost, "port", clientport
    content1 = "Hello "+socket.gethostname()+"!"
    clientConnection.sendall(content1.encode())
    content2 = clientConnection.recv(1024).decode()
    print content2
    clientConnection.close()
    
