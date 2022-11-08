import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
content1 = s.recv(1024).decode()
print content1
content2 = "Hi Server!"
s.sendall(content2.encode())
s.close()
