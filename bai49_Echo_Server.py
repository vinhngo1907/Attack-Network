import socket
import threading
def handle_client(c, a, p):
	print "Connection from:", a, "port", p
	while True:
                try:
                        data = c.recv(1024)
                        if (data == "#quit"):
                                break
                        c.sendall(data)
                except:
                        break
	c.close()
	print "Disconnected to Client:", a, "port", p
	return

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 7777))
s.listen(5)
print "Da khoi tao xong Server."
while True:
	clientConnection, (clientHost, clientPort) = s.accept()
	t = threading.Thread(target=handle_client, args=(clientConnection, clientHost, clientPort))
	t.start()
